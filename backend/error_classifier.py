# error_classifier.py — parse subprocess output into error_type + signature

import re
import hashlib
from dataclasses import dataclass, field
from typing import Optional

from execution_engine import ExecutionResult

# MVP error set per AGENTS.md §33 / architecture §5.1
KNOWN_ERRORS = {
    "NameError",
    "TypeError",
    "SyntaxError",
    "AttributeError",
    "IndexError",
    "KeyError",
    "ValueError",
    "ZeroDivisionError",
    "RecursionError",
    "TimeoutError",
}

# regex: grab the exception class name from the last non-empty line of stderr
# handles both  "NameError: ..."  and  "  NameError: ..."
_EXC_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)(?:\s*:|\s*$)")

# patterns used to strip volatile info before hashing the error signature
_LINE_NO_RE = re.compile(r"\bline \d+\b", re.IGNORECASE)
_QUOTED_NAME_RE = re.compile(r"'[^']*'")   # strip quoted names like 'x'


@dataclass
class ClassifiedError:
    error_type: str                      # e.g. "NameError" or "Exception"
    error_signature: str                 # sha1 hex for exact-repeat detection
    raw_message: str                     # last meaningful line from stderr


def _last_meaningful_line(stderr: str) -> str:
    """Return the last non-empty line of stderr (where the exception lives)."""
    lines = [l.strip() for l in stderr.splitlines() if l.strip()]
    return lines[-1] if lines else ""


def _normalize_message(msg: str) -> str:
    """Strip line numbers and quoted names so 'same mistake' hashing is stable."""
    msg = _LINE_NO_RE.sub("", msg)
    msg = _QUOTED_NAME_RE.sub("'?'", msg)
    return msg.strip().lower()


def classify(result: ExecutionResult) -> Optional[ClassifiedError]:
    """
    Returns None on SUCCESS (returncode == 0, no stderr).
    Returns a ClassifiedError for any failure including timeout.
    """
    if result.timed_out:
        sig = hashlib.sha1(b"TimeoutError:timeout").hexdigest()[:16]
        return ClassifiedError(
            error_type="TimeoutError",
            error_signature=sig,
            raw_message=result.stderr,
        )

    if result.returncode == 0 and not result.stderr.strip():
        return None  # genuine success

    last_line = _last_meaningful_line(result.stderr)
    error_type = "Exception"  # default

    m = _EXC_RE.match(last_line)
    if m:
        candidate = m.group(1)
        if candidate in KNOWN_ERRORS:
            error_type = candidate
        elif candidate.endswith("Error") or candidate.endswith("Exception"):
            error_type = candidate  # keep specific unknown errors as-is

    normalized = _normalize_message(last_line)
    sig_input = f"{error_type}:{normalized}".encode("utf-8")
    signature = hashlib.sha1(sig_input).hexdigest()[:16]

    return ClassifiedError(
        error_type=error_type,
        error_signature=signature,
        raw_message=last_line,
    )
