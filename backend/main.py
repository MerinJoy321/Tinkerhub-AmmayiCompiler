# main.py — FastAPI app, route registration, CORS, static mounts

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import CORS_ALLOWED_ORIGINS, MAX_ANGER_SCORE, anger_level_from_score
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

app = FastAPI(title="AMMAYI.EXE Backend", version="0.1.0")

# ── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── static audio assets ───────────────────────────────────────────────────────
_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
if os.path.isdir(_ASSETS_DIR):
    app.mount("/assets", StaticFiles(directory=_ASSETS_DIR), name="assets")

# ── in-memory state (Chunk 1 — replaced by DB in Chunk 2) ────────────────────
_state = {
    "anger_score": 0,
    "total_errors": 0,
    "total_successes": 0,
    "current_failure_streak": 0,
    "longest_failure_streak": 0,
    "total_sessions": 0,
    "escape_attempts": 0,
    "highest_anger": 0,
    "last_error_type": None,
    "last_error_signature": None,
    "last_response_id": None,
    "last_event_at": None,
}

# sessions: just a set of known session_ids for Chunk 1
_known_sessions: set = set()


# ── helpers ───────────────────────────────────────────────────────────────────

def _snapshot() -> StateSnapshot:
    level, label = anger_level_from_score(_state["anger_score"])
    return StateSnapshot(
        anger_score=_state["anger_score"],
        anger_level=level,
        anger_label=label,
        total_errors=_state["total_errors"],
        total_successes=_state["total_successes"],
        current_failure_streak=_state["current_failure_streak"],
        longest_failure_streak=_state["longest_failure_streak"],
        total_sessions=_state["total_sessions"],
        escape_attempts=_state["escape_attempts"],
        highest_anger=_state["highest_anger"],
    )


def _add_anger(delta: int):
    _state["anger_score"] = min(_state["anger_score"] + delta, MAX_ANGER_SCORE)
    _state["highest_anger"] = max(_state["highest_anger"], _state["anger_score"])


def _compute_situations_for_error(error_type: str, error_signature: str) -> set:
    from datetime import datetime, timezone
    from config import RAPID_REPEAT_THRESHOLD_SECONDS, LONG_STREAK_THRESHOLD

    tags = {"generic"}

    # first time this error_type?
    if _state["last_error_type"] != error_type:
        tags.add("first_time_error")
    else:
        tags.add("repeated_error_type")

    if _state["last_error_signature"] == error_signature:
        tags.add("exact_repeat")

    # rapid repeat
    if _state["last_event_at"]:
        try:
            last = datetime.fromisoformat(_state["last_event_at"])
            now = datetime.now(timezone.utc)
            # make both timezone-aware or both naive
            if last.tzinfo is None:
                from datetime import timezone as tz
                last = last.replace(tzinfo=tz.utc)
            delta_secs = (now - last).total_seconds()
            if delta_secs < RAPID_REPEAT_THRESHOLD_SECONDS:
                tags.add("rapid_repeat")
        except Exception:
            pass

    if _state["current_failure_streak"] >= LONG_STREAK_THRESHOLD:
        tags.add("long_streak")

    return tags


def _wrap_response(r: dict) -> AmmayiResponse:
    return AmmayiResponse(id=r["id"], text_ml=r["text_ml"], audio=r.get("audio"))


# ── routes ─────────────────────────────────────────────────────────────────────

@app.get("/api/health")
def health():
    return {"status": "ok", "message": "Ammayi is watching."}


@app.post("/api/session/start", response_model=SessionStartResponse)
def session_start(req: SessionStartRequest):
    from uuid import uuid4

    existing = req.existing_session_id
    is_escape = False
    ammayi_resp = None

    if existing and existing in _known_sessions:
        # RESUME — no escalation
        return SessionStartResponse(
            session_id=existing,
            is_new_session=False,
            is_escape_attempt=False,
            ammayi_response=None,
            state=_snapshot(),
        )

    # NEW session
    new_id = str(uuid4())
    _known_sessions.add(new_id)
    _state["total_sessions"] += 1

    if _state["total_sessions"] > 1:
        # escape attempt
        is_escape = True
        _state["escape_attempts"] += 1
        delta = 5 if _state["escape_attempts"] > 1 else 3
        _add_anger(delta)

        situations = {"escape_attempt", "generic"}
        if _state["escape_attempts"] > 1:
            situations.add("repeated_escape")

        r = select_response(
            event_type="ESCAPE_ATTEMPT",
            error_type=None,
            situations=situations,
            anger_score=_state["anger_score"],
            current_streak=_state["current_failure_streak"],
            escape_attempts=_state["escape_attempts"],
            last_response_id=_state["last_response_id"],
            current_session_id=new_id,
        )
        _state["last_response_id"] = r["id"]
        ammayi_resp = _wrap_response(r)

    return SessionStartResponse(
        session_id=new_id,
        is_new_session=True,
        is_escape_attempt=is_escape,
        ammayi_response=ammayi_resp,
        state=_snapshot(),
    )


@app.post("/api/execute", response_model=ExecuteResponse)
def execute(req: ExecuteRequest):
    from datetime import datetime, timezone

    if req.session_id not in _known_sessions:
        # auto-register unknown session rather than 400 — frontend may not have called /session/start
        _known_sessions.add(req.session_id)

    result = run_user_code(req.code)
    classified = classify(result)

    now_iso = datetime.now(timezone.utc).isoformat()

    if classified is None:
        # SUCCESS
        _state["total_successes"] += 1
        _state["current_failure_streak"] = 0
        # anger never decreases
        situations = {"success", "generic"}
        if _state["current_failure_streak"] >= 4:
            situations.add("long_streak")

        r = select_response(
            event_type="SUCCESS",
            error_type=None,
            situations=situations,
            anger_score=_state["anger_score"],
            current_streak=0,
            escape_attempts=_state["escape_attempts"],
            last_response_id=_state["last_response_id"],
            current_session_id=req.session_id,
        )
        _state["last_response_id"] = r["id"]
        _state["last_event_at"] = now_iso

        return ExecuteResponse(
            stdout=result.stdout,
            stderr=result.stderr,
            success=True,
            error_type=None,
            timed_out=False,
            ammayi_response=_wrap_response(r),
            state=_snapshot(),
        )

    # ERROR
    error_type = classified.error_type
    error_sig = classified.error_signature
    situations = _compute_situations_for_error(error_type, error_sig)

    # anger delta
    delta = 1
    if "exact_repeat" in situations:
        delta += 1
    if "rapid_repeat" in situations:
        delta += 1
    delta = min(delta, 3)
    _add_anger(delta)

    _state["total_errors"] += 1
    _state["current_failure_streak"] += 1
    _state["longest_failure_streak"] = max(
        _state["longest_failure_streak"], _state["current_failure_streak"]
    )
    _state["last_error_type"] = error_type
    _state["last_error_signature"] = error_sig
    _state["last_event_at"] = now_iso

    r = select_response(
        event_type="ERROR",
        error_type=error_type,
        situations=situations,
        anger_score=_state["anger_score"],
        current_streak=_state["current_failure_streak"],
        escape_attempts=_state["escape_attempts"],
        last_response_id=_state["last_response_id"],
        current_session_id=req.session_id,
    )
    _state["last_response_id"] = r["id"]

    return ExecuteResponse(
        stdout=result.stdout,
        stderr=result.stderr,
        success=False,
        error_type=error_type,
        timed_out=result.timed_out,
        ammayi_response=_wrap_response(r),
        state=_snapshot(),
    )


@app.post("/api/excuse", response_model=SimpleEventResponse)
def excuse(req: ExcuseRequest):
    if req.session_id not in _known_sessions:
        _known_sessions.add(req.session_id)

    _add_anger(1)
    r = select_response(
        event_type="EXCUSE",
        error_type=None,
        situations={"excuse", "generic"},
        anger_score=_state["anger_score"],
        current_streak=_state["current_failure_streak"],
        escape_attempts=_state["escape_attempts"],
        last_response_id=_state["last_response_id"],
        current_session_id=req.session_id,
    )
    _state["last_response_id"] = r["id"]
    return SimpleEventResponse(ammayi_response=_wrap_response(r), state=_snapshot())


@app.post("/api/make-it-worse", response_model=SimpleEventResponse)
def make_it_worse(req: MakeItWorseRequest):
    if req.session_id not in _known_sessions:
        _known_sessions.add(req.session_id)

    _add_anger(1)
    r = select_response(
        event_type="MAKE_IT_WORSE",
        error_type=None,
        situations={"make_it_worse", "generic"},
        anger_score=_state["anger_score"],
        current_streak=_state["current_failure_streak"],
        escape_attempts=_state["escape_attempts"],
        last_response_id=_state["last_response_id"],
        current_session_id=req.session_id,
    )
    _state["last_response_id"] = r["id"]
    return SimpleEventResponse(ammayi_response=_wrap_response(r), state=_snapshot())


@app.get("/api/state", response_model=StateSnapshot)
def get_state():
    return _snapshot()


@app.get("/api/stats", response_model=StateSnapshot)
def get_stats():
    return _snapshot()
