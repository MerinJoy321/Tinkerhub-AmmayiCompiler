# state_manager.py — load/save AmmayiState, session bookkeeping

from datetime import datetime, timezone
from typing import Optional

from database import get_conn
from config import MAX_ANGER_SCORE, anger_level_from_score


# ── ammayi_state (singleton row id=1) ────────────────────────────────────────

def get_state() -> dict:
    """Load the singleton Ammayi state row and return it as a plain dict."""
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM ammayi_state WHERE id = 1").fetchone()
        return dict(row)


def update_state(**fields) -> dict:
    """
    Update any subset of ammayi_state columns by keyword argument.
    Returns the updated state dict.

    Example:
        update_state(anger_score=5, total_errors=3)
    """
    if not fields:
        return get_state()

    set_clause = ", ".join(f"{k} = :{k}" for k in fields)
    fields["_id"] = 1
    with get_conn() as conn:
        conn.execute(
            f"UPDATE ammayi_state SET {set_clause} WHERE id = :_id",
            fields,
        )
        conn.commit()
    return get_state()


def add_anger(delta: int) -> dict:
    """
    Atomically add delta to anger_score (clamped to MAX_ANGER_SCORE).
    Updates highest_anger if needed. Returns updated state.
    """
    with get_conn() as conn:
        conn.execute(
            """
            UPDATE ammayi_state
            SET
                anger_score   = MIN(anger_score + :delta, :cap),
                highest_anger = MAX(highest_anger, MIN(anger_score + :delta, :cap))
            WHERE id = 1
            """,
            {"delta": delta, "cap": MAX_ANGER_SCORE},
        )
        conn.commit()
    return get_state()


def state_snapshot(state: Optional[dict] = None) -> dict:
    """
    Return a dict ready to build a StateSnapshot model.
    Pass an already-loaded state dict to avoid a second DB hit.
    """
    if state is None:
        state = get_state()
    level, label = anger_level_from_score(state["anger_score"])
    return {
        "anger_score":             state["anger_score"],
        "anger_level":             level,
        "anger_label":             label,
        "total_errors":            state["total_errors"],
        "total_successes":         state["total_successes"],
        "current_failure_streak":  state["current_failure_streak"],
        "longest_failure_streak":  state["longest_failure_streak"],
        "total_sessions":          state["total_sessions"],
        "escape_attempts":         state["escape_attempts"],
        "highest_anger":           state["highest_anger"],
    }


# ── sessions ──────────────────────────────────────────────────────────────────

def create_session(session_id: str, starting_anger: int, escape_detected: bool = False) -> dict:
    """Insert a new session row and return it."""
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO sessions (id, started_at, escape_detected, starting_anger, ending_anger)
            VALUES (:id, :started_at, :escape, :starting_anger, :starting_anger)
            """,
            {
                "id": session_id,
                "started_at": _now(),
                "escape": 1 if escape_detected else 0,
                "starting_anger": starting_anger,
            },
        )
        conn.commit()
    return get_session(session_id)


def get_session(session_id: str) -> Optional[dict]:
    """Return the session row as a dict, or None if not found."""
    with get_conn() as conn:
        row = conn.execute(
            "SELECT * FROM sessions WHERE id = ?", (session_id,)
        ).fetchone()
        return dict(row) if row else None


def update_session(session_id: str, **fields):
    """Update a session row by keyword argument."""
    if not fields:
        return
    set_clause = ", ".join(f"{k} = :{k}" for k in fields)
    fields["_id"] = session_id
    with get_conn() as conn:
        conn.execute(
            f"UPDATE sessions SET {set_clause} WHERE id = :_id", fields
        )
        conn.commit()


# ── events (append-only log) ──────────────────────────────────────────────────

def record_event(
    session_id: str,
    event_type: str,
    anger_before: int,
    anger_after: int,
    error_type: Optional[str] = None,
    response_id: Optional[str] = None,
    metadata: Optional[str] = None,
):
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO events
                (session_id, timestamp, event_type, error_type, anger_before, anger_after, response_id, metadata)
            VALUES
                (:session_id, :ts, :event_type, :error_type, :anger_before, :anger_after, :response_id, :metadata)
            """,
            {
                "session_id": session_id,
                "ts": _now(),
                "event_type": event_type,
                "error_type": error_type,
                "anger_before": anger_before,
                "anger_after": anger_after,
                "response_id": response_id,
                "metadata": metadata,
            },
        )
        conn.commit()


# ── response_usage ────────────────────────────────────────────────────────────

def record_response_usage(response_id: str, session_id: str):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO response_usage (response_id, session_id, used_at) VALUES (?, ?, ?)",
            (response_id, session_id, _now()),
        )
        conn.commit()


def get_last_used_session_for_response(response_id: str) -> Optional[str]:
    """Return the session_id of the most recent use of a response, or None."""
    with get_conn() as conn:
        row = conn.execute(
            "SELECT session_id FROM response_usage WHERE response_id = ? ORDER BY used_at DESC LIMIT 1",
            (response_id,),
        ).fetchone()
        return row["session_id"] if row else None


# ── internal util ─────────────────────────────────────────────────────────────

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ── history query ─────────────────────────────────────────────────────────────

def get_recent_events(limit: int = 20) -> list[dict]:
    """Return the most recent events, newest first, as a list of dicts."""
    limit = max(1, min(limit, 100))  # clamp 1–100
    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT id, timestamp, session_id, event_type, error_type,
                   anger_before, anger_after, response_id
            FROM events
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]
