# main.py — FastAPI app, route registration, CORS, static mounts

import os
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import (
    CORS_ALLOWED_ORIGINS, MAX_ANGER_SCORE,
    RAPID_REPEAT_THRESHOLD_SECONDS, LONG_STREAK_THRESHOLD,
)
from models import (
    ExecuteRequest, ExecuteResponse,
    SessionStartRequest, SessionStartResponse,
    ExcuseRequest, MakeItWorseRequest,
    SimpleEventResponse,
    AmmayiResponse, StateSnapshot,
)
from execution_engine import run_user_code
from error_classifier import classify
from response_engine import select_response
from database import init_db
import state_manager as sm

# ── app setup ─────────────────────────────────────────────────────────────────

app = FastAPI(title="AMMAYI.EXE Backend", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
if os.path.isdir(_ASSETS_DIR):
    app.mount("/assets", StaticFiles(directory=_ASSETS_DIR), name="assets")


@app.on_event("startup")
def startup():
    init_db()


# ── helpers ───────────────────────────────────────────────────────────────────

def _snapshot(state: dict = None) -> StateSnapshot:
    d = sm.state_snapshot(state)
    return StateSnapshot(**d)


def _wrap_response(r: dict) -> AmmayiResponse:
    return AmmayiResponse(id=r["id"], text_ml=r["text_ml"], audio=r.get("audio"))


def _compute_situations_for_error(state: dict, error_type: str, error_signature: str) -> set:
    tags = {"generic"}

    if state["last_error_type"] != error_type:
        tags.add("first_time_error")
    else:
        tags.add("repeated_error_type")

    if state["last_error_signature"] == error_signature:
        tags.add("exact_repeat")

    if state["last_event_at"]:
        try:
            last = datetime.fromisoformat(state["last_event_at"])
            now = datetime.now(timezone.utc)
            if last.tzinfo is None:
                last = last.replace(tzinfo=timezone.utc)
            if (now - last).total_seconds() < RAPID_REPEAT_THRESHOLD_SECONDS:
                tags.add("rapid_repeat")
        except Exception:
            pass

    if state["current_failure_streak"] >= LONG_STREAK_THRESHOLD:
        tags.add("long_streak")

    return tags


def _anger_delta_for_error(situations: set) -> int:
    delta = 1
    if "exact_repeat" in situations:
        delta += 1
    if "rapid_repeat" in situations:
        delta += 1
    return min(delta, 3)


def _response_usage_map(response_id: str, session_id: str) -> dict:
    """Build the minimal usage map that response_engine expects."""
    last_session = sm.get_last_used_session_for_response(response_id)
    return {response_id: {"last_used_session_id": last_session}}


# ── routes ─────────────────────────────────────────────────────────────────────

@app.get("/api/health")
def health():
    return {"status": "ok", "message": "Ammayi is watching."}


@app.get("/api/state", response_model=StateSnapshot)
def get_state():
    return _snapshot()


@app.get("/api/stats", response_model=StateSnapshot)
def get_stats():
    return _snapshot()


@app.post("/api/session/start", response_model=SessionStartResponse)
def session_start(req: SessionStartRequest):
    existing = req.existing_session_id

    # RESUME — session already exists in DB
    if existing and sm.get_session(existing):
        return SessionStartResponse(
            session_id=existing,
            is_new_session=False,
            is_escape_attempt=False,
            ammayi_response=None,
            state=_snapshot(),
        )

    # NEW session
    state = sm.get_state()
    new_id = str(uuid4())
    is_escape = False
    ammayi_resp = None

    # increment total_sessions first so the new value is reflected in state
    new_total_sessions = state["total_sessions"] + 1

    if state["total_sessions"] > 0:
        # Escape attempt — there was already at least one prior session
        is_escape = True
        new_escape_attempts = state["escape_attempts"] + 1
        delta = 5 if new_escape_attempts > 1 else 3

        anger_before = state["anger_score"]
        updated = sm.add_anger(delta)
        sm.update_state(
            total_sessions=new_total_sessions,
            escape_attempts=new_escape_attempts,
            last_event_type="ESCAPE_ATTEMPT",
            last_event_at=sm._now(),
        )
        state = sm.get_state()

        situations = {"escape_attempt", "generic"}
        if state["escape_attempts"] > 1:
            situations.add("repeated_escape")

        r = select_response(
            event_type="ESCAPE_ATTEMPT",
            error_type=None,
            situations=situations,
            anger_score=state["anger_score"],
            current_streak=state["current_failure_streak"],
            escape_attempts=state["escape_attempts"],
            last_response_id=state["last_response_id"],
            current_session_id=new_id,
        )
        sm.update_state(last_response_id=r["id"])
        sm.record_response_usage(r["id"], new_id)
        sm.record_event(
            session_id=new_id,
            event_type="ESCAPE_ATTEMPT",
            anger_before=anger_before,
            anger_after=state["anger_score"],
        )
        ammayi_resp = _wrap_response(r)
    else:
        # Genuinely first session ever
        sm.update_state(
            total_sessions=new_total_sessions,
            last_event_type="NEW_SESSION",
            last_event_at=sm._now(),
        )
        state = sm.get_state()

    sm.create_session(new_id, starting_anger=state["anger_score"], escape_detected=is_escape)

    return SessionStartResponse(
        session_id=new_id,
        is_new_session=True,
        is_escape_attempt=is_escape,
        ammayi_response=ammayi_resp,
        state=_snapshot(state),
    )


@app.post("/api/execute", response_model=ExecuteResponse)
def execute(req: ExecuteRequest):
    # auto-register unknown session so /execute works even without /session/start
    if not sm.get_session(req.session_id):
        state = sm.get_state()
        sm.create_session(req.session_id, starting_anger=state["anger_score"])

    result = run_user_code(req.code)
    classified = classify(result)
    state = sm.get_state()

    if classified is None:
        # ── SUCCESS ──────────────────────────────────────────────────────────
        anger_before = state["anger_score"]
        # anger does NOT change
        situations = {"success", "generic"}
        if state["current_failure_streak"] >= LONG_STREAK_THRESHOLD:
            situations.add("long_streak")

        r = select_response(
            event_type="SUCCESS",
            error_type=None,
            situations=situations,
            anger_score=state["anger_score"],
            current_streak=0,
            escape_attempts=state["escape_attempts"],
            last_response_id=state["last_response_id"],
            current_session_id=req.session_id,
            response_usage=_response_usage_map(state["last_response_id"] or "NONE", req.session_id),
        )

        sm.update_state(
            total_successes=state["total_successes"] + 1,
            current_failure_streak=0,
            last_event_type="SUCCESS",
            last_event_at=sm._now(),
            last_response_id=r["id"],
        )
        sm.record_response_usage(r["id"], req.session_id)
        sm.record_event(
            session_id=req.session_id,
            event_type="SUCCESS",
            anger_before=anger_before,
            anger_after=anger_before,  # anger unchanged
        )
        sm.update_session(
            req.session_id,
            success_count=state.get("total_successes", 0) + 1,
            ending_anger=anger_before,
        )

        state = sm.get_state()
        return ExecuteResponse(
            stdout=result.stdout,
            stderr=result.stderr,
            success=True,
            error_type=None,
            timed_out=False,
            ammayi_response=_wrap_response(r),
            state=_snapshot(state),
        )

    # ── ERROR ─────────────────────────────────────────────────────────────────
    error_type = classified.error_type
    error_sig = classified.error_signature
    situations = _compute_situations_for_error(state, error_type, error_sig)
    delta = _anger_delta_for_error(situations)

    anger_before = state["anger_score"]
    sm.add_anger(delta)
    state = sm.get_state()

    new_streak = state["current_failure_streak"] + 1
    new_longest = max(state["longest_failure_streak"], new_streak)

    sm.update_state(
        total_errors=state["total_errors"] + 1,
        current_failure_streak=new_streak,
        longest_failure_streak=new_longest,
        last_error_type=error_type,
        last_error_signature=error_sig,
        last_event_type="ERROR",
        last_event_at=sm._now(),
    )
    state = sm.get_state()

    r = select_response(
        event_type="ERROR",
        error_type=error_type,
        situations=situations,
        anger_score=state["anger_score"],
        current_streak=state["current_failure_streak"],
        escape_attempts=state["escape_attempts"],
        last_response_id=state["last_response_id"],
        current_session_id=req.session_id,
        response_usage=_response_usage_map(state["last_response_id"] or "NONE", req.session_id),
    )

    sm.update_state(last_response_id=r["id"])
    sm.record_response_usage(r["id"], req.session_id)
    sm.record_event(
        session_id=req.session_id,
        event_type="ERROR",
        anger_before=anger_before,
        anger_after=state["anger_score"],
        error_type=error_type,
    )
    sm.update_session(
        req.session_id,
        error_count=state["total_errors"],
        ending_anger=state["anger_score"],
    )

    state = sm.get_state()
    return ExecuteResponse(
        stdout=result.stdout,
        stderr=result.stderr,
        success=False,
        error_type=error_type,
        timed_out=result.timed_out,
        ammayi_response=_wrap_response(r),
        state=_snapshot(state),
    )


@app.post("/api/excuse", response_model=SimpleEventResponse)
def excuse(req: ExcuseRequest):
    if not sm.get_session(req.session_id):
        state = sm.get_state()
        sm.create_session(req.session_id, starting_anger=state["anger_score"])

    state = sm.get_state()
    anger_before = state["anger_score"]
    sm.add_anger(1)
    state = sm.get_state()

    r = select_response(
        event_type="EXCUSE",
        error_type=None,
        situations={"excuse", "generic"},
        anger_score=state["anger_score"],
        current_streak=state["current_failure_streak"],
        escape_attempts=state["escape_attempts"],
        last_response_id=state["last_response_id"],
        current_session_id=req.session_id,
    )
    sm.update_state(last_response_id=r["id"], last_event_type="EXCUSE", last_event_at=sm._now())
    sm.record_response_usage(r["id"], req.session_id)
    sm.record_event(req.session_id, "EXCUSE", anger_before, state["anger_score"])

    return SimpleEventResponse(ammayi_response=_wrap_response(r), state=_snapshot())


@app.post("/api/make-it-worse", response_model=SimpleEventResponse)
def make_it_worse(req: MakeItWorseRequest):
    if not sm.get_session(req.session_id):
        state = sm.get_state()
        sm.create_session(req.session_id, starting_anger=state["anger_score"])

    state = sm.get_state()
    anger_before = state["anger_score"]
    sm.add_anger(1)
    state = sm.get_state()

    r = select_response(
        event_type="MAKE_IT_WORSE",
        error_type=None,
        situations={"make_it_worse", "generic"},
        anger_score=state["anger_score"],
        current_streak=state["current_failure_streak"],
        escape_attempts=state["escape_attempts"],
        last_response_id=state["last_response_id"],
        current_session_id=req.session_id,
    )
    sm.update_state(last_response_id=r["id"], last_event_type="MAKE_IT_WORSE", last_event_at=sm._now())
    sm.record_response_usage(r["id"], req.session_id)
    sm.record_event(req.session_id, "MAKE_IT_WORSE", anger_before, state["anger_score"])

    return SimpleEventResponse(ammayi_response=_wrap_response(r), state=_snapshot())
