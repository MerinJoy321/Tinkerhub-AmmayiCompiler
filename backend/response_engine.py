# response_engine.py — candidate scoring + selection + fallback tiers

import json
import os
import random
from typing import Optional

from config import MIN_ACCEPTABLE_RESPONSE_SCORE, anger_level_from_score

# ── load library once at import time ─────────────────────────────────────────

_LIBRARY_PATH = os.path.join(os.path.dirname(__file__), "data", "ammayi", "responses.json")

def _load_library():
    with open(_LIBRARY_PATH, encoding="utf-8") as f:
        return json.load(f)

LIBRARY: list[dict] = _load_library()

# ── absolute fallback (never fails) ──────────────────────────────────────────

ABSOLUTE_FALLBACK = {
    "id": "FALLBACK",
    "text_ml": "ഓ, ഇതും ഒരു error ആണോ.",
    "audio": None,
}


def select_response(
    event_type: str,          # ERROR / SUCCESS / ESCAPE_ATTEMPT / NEW_SESSION / EXCUSE / MAKE_IT_WORSE
    error_type: Optional[str],
    situations: set,          # set of situation tag strings
    anger_score: int,
    current_streak: int,
    escape_attempts: int,
    last_response_id: Optional[str] = None,
    current_session_id: Optional[str] = None,
    response_usage: Optional[dict] = None,  # {response_id: {"last_used_session_id": ...}}
) -> dict:
    """
    Score every candidate in the library and return the best match.
    Falls through to ABSOLUTE_FALLBACK if the library is empty or all scores are too low.
    """
    anger_level, _ = anger_level_from_score(anger_score)
    response_usage = response_usage or {}

    def score(r: dict) -> int:
        s = 0

        # ── event type gate ───────────────────────────────────────────────────
        if event_type not in r.get("event_types", []):
            return -9999

        # ── error type matching ───────────────────────────────────────────────
        if error_type is not None:
            if error_type in r.get("error_types", []):
                s += 30
            elif "ANY" in r.get("error_types", []):
                s += 10
            else:
                s -= 5   # wrong error type but not excluded yet
        else:
            if "ANY" in r.get("error_types", []):
                s += 30

        # ── situation matching ────────────────────────────────────────────────
        if any(tag in r.get("situations", []) for tag in situations):
            s += 30

        # ── anger range (hard filter) ─────────────────────────────────────────
        lo, hi = r.get("anger_range", [0, 8])
        if lo <= anger_level <= hi:
            s += 20
        else:
            s -= 100   # hard filter: out of anger range

        # ── streak gate ───────────────────────────────────────────────────────
        if current_streak >= r.get("min_streak", 0):
            s += 10
        else:
            s -= 100   # hard filter

        # ── escape attempts gate ──────────────────────────────────────────────
        if escape_attempts >= r.get("min_escape_attempts", 0):
            s += 5
        else:
            s -= 100   # hard filter

        # ── priority tie-break ────────────────────────────────────────────────
        s += r.get("priority", 0)

        # ── anti-repetition ───────────────────────────────────────────────────
        if r["id"] == last_response_id:
            s -= 50
        usage = response_usage.get(r["id"], {})
        if usage.get("last_used_session_id") == current_session_id and current_session_id:
            s -= 15

        return s

    # ── tier 1: normal scoring ────────────────────────────────────────────────
    scored = [(score(r), r) for r in LIBRARY]
    scored.sort(key=lambda x: x[0], reverse=True)

    if scored and scored[0][0] >= MIN_ACCEPTABLE_RESPONSE_SCORE:
        # pick among tied top scorers randomly
        top_score = scored[0][0]
        top = [r for sc, r in scored if sc == top_score]
        return random.choice(top)

    # ── tier 2: drop anger hard filter, use soft ──────────────────────────────
    def score_t2(r: dict) -> int:
        s = 0
        if event_type not in r.get("event_types", []):
            return -9999
        if error_type is not None:
            if error_type in r.get("error_types", []):
                s += 30
            elif "ANY" in r.get("error_types", []):
                s += 10
        else:
            if "ANY" in r.get("error_types", []):
                s += 30
        if any(tag in r.get("situations", []) for tag in situations):
            s += 30
        lo, hi = r.get("anger_range", [0, 8])
        if lo <= anger_level <= hi:
            s += 20   # soft bonus, not hard filter
        if current_streak >= r.get("min_streak", 0):
            s += 10
        if escape_attempts >= r.get("min_escape_attempts", 0):
            s += 5
        s += r.get("priority", 0)
        if r["id"] == last_response_id:
            s -= 50
        return s

    scored_t2 = [(score_t2(r), r) for r in LIBRARY if event_type in r.get("event_types", [])]
    if scored_t2:
        scored_t2.sort(key=lambda x: x[0], reverse=True)
        if scored_t2[0][0] > 0:
            top_score = scored_t2[0][0]
            top = [r for sc, r in scored_t2 if sc == top_score]
            return random.choice(top)

    # ── tier 3: generic bucket for this event_type ────────────────────────────
    generic = [
        r for r in LIBRARY
        if event_type in r.get("event_types", []) and "generic" in r.get("situations", [])
    ]
    if generic:
        # pick closest anger level
        best = min(generic, key=lambda r: abs(
            (r.get("anger_range", [0, 8])[0] + r.get("anger_range", [0, 8])[1]) / 2 - anger_level
        ))
        return best

    # ── tier 4: absolute fallback ─────────────────────────────────────────────
    return ABSOLUTE_FALLBACK
