# models.py — Pydantic request/response schemas

from pydantic import BaseModel, Field
from typing import Optional


# ── inbound ──────────────────────────────────────────────────────────────────

class ExecuteRequest(BaseModel):
    session_id: str
    code: str = Field(..., min_length=1, max_length=20_000)


class SessionStartRequest(BaseModel):
    existing_session_id: Optional[str] = None


class ExcuseRequest(BaseModel):
    session_id: str
    excuse_text: str = Field(..., max_length=2000)


class MakeItWorseRequest(BaseModel):
    session_id: str


# ── shared outbound pieces ────────────────────────────────────────────────────

class AmmayiResponse(BaseModel):
    id: str
    text_ml: str
    audio: Optional[str] = None   # path like "assets/audio/ammayi/R001.wav", or null


class StateSnapshot(BaseModel):
    anger_score: int
    anger_level: int
    anger_label: str
    total_errors: int
    total_successes: int
    current_failure_streak: int
    longest_failure_streak: int
    total_sessions: int
    escape_attempts: int
    highest_anger: int


# ── outbound ─────────────────────────────────────────────────────────────────

class ExecuteResponse(BaseModel):
    stdout: str
    stderr: str
    success: bool
    error_type: Optional[str] = None
    timed_out: bool
    ammayi_response: AmmayiResponse
    state: StateSnapshot


class SessionStartResponse(BaseModel):
    session_id: str
    is_new_session: bool
    is_escape_attempt: bool
    ammayi_response: Optional[AmmayiResponse] = None
    state: StateSnapshot


class SimpleEventResponse(BaseModel):
    ammayi_response: AmmayiResponse
    state: StateSnapshot
