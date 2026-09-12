# escape_detector.py — deterministic session classification
#
# Three outcomes:
#   RESUME          — supplied session_id is recognised in the DB
#   FIRST_SESSION   — no session history exists at all
#   ESCAPE_ATTEMPT  — history exists but the supplied session_id is unknown/missing

from typing import Optional
import state_manager as sm

RESUME = "RESUME"
FIRST_SESSION = "FIRST_SESSION"
ESCAPE_ATTEMPT = "ESCAPE_ATTEMPT"


def classify_session_start(existing_session_id: Optional[str]) -> str:
    """
    Return one of RESUME / FIRST_SESSION / ESCAPE_ATTEMPT.

    Logic (per architecture §6.1):
    - If existing_session_id is supplied AND it exists in the sessions table → RESUME.
    - If total_sessions == 0 → FIRST_SESSION.
    - Otherwise → ESCAPE_ATTEMPT.
    """
    if existing_session_id:
        session = sm.get_session(existing_session_id)
        if session is not None:
            return RESUME

    state = sm.get_state()
    if state["total_sessions"] == 0:
        return FIRST_SESSION

    return ESCAPE_ATTEMPT


def escape_anger_delta(escape_attempts_after_increment: int) -> int:
    """
    Return the anger delta for an escape attempt.
      first escape  (escape_attempts == 1 after increment) → +3
      repeated      (escape_attempts  > 1 after increment) → +5
    """
    return 3 if escape_attempts_after_increment == 1 else 5
