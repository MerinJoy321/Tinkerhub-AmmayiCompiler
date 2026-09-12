# execution_engine.py — run user Python code in a subprocess, never exec()

import subprocess
import tempfile
import os
import sys
from dataclasses import dataclass

from config import EXEC_TIMEOUT_SECONDS, MAX_STDOUT_CHARS


@dataclass
class ExecutionResult:
    stdout: str
    stderr: str
    returncode: int
    timed_out: bool


def run_user_code(code: str) -> ExecutionResult:
    """
    Execute user-supplied Python code in an isolated subprocess.
    - Uses a temp file so we don't hit Windows command-line length limits.
    - Uses python -I (isolated mode: no site-packages, no PYTHONPATH).
    - Enforces a hard timeout.
    - Runs from a scratch temp dir so accidental writes don't touch our code.
    - Truncates stdout/stderr to MAX_STDOUT_CHARS.
    """
    with tempfile.TemporaryDirectory() as run_dir:
        # write user code to a temp file inside the scratch dir
        code_path = os.path.join(run_dir, "user_code.py")
        with open(code_path, "w", encoding="utf-8") as f:
            f.write(code)

        # minimal environment — no PYTHONPATH, no site-packages leakage
        minimal_env = {
            "PATH": os.environ.get("PATH", ""),
            "SYSTEMROOT": os.environ.get("SYSTEMROOT", ""),   # Windows needs this
            "TEMP": os.environ.get("TEMP", run_dir),
            "TMP": os.environ.get("TMP", run_dir),
        }

        python_exe = sys.executable  # same interpreter that's running the server

        try:
            result = subprocess.run(
                [python_exe, "-I", code_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=EXEC_TIMEOUT_SECONDS,
                cwd=run_dir,
                env=minimal_env,
            )
            return ExecutionResult(
                stdout=result.stdout[:MAX_STDOUT_CHARS],
                stderr=result.stderr[:MAX_STDOUT_CHARS],
                returncode=result.returncode,
                timed_out=False,
            )

        except subprocess.TimeoutExpired:
            return ExecutionResult(
                stdout="",
                stderr=f"TimeoutError: execution exceeded {EXEC_TIMEOUT_SECONDS} seconds",
                returncode=1,
                timed_out=True,
            )
        except Exception as exc:
            return ExecutionResult(
                stdout="",
                stderr=f"ExecutionEngineError: {exc}",
                returncode=1,
                timed_out=False,
            )
