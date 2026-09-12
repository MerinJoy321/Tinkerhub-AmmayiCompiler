# database.py — SQLite connection + schema creation

import sqlite3
import os

# database lives at  <repo_root>/database/ammayi.db
_DB_DIR = os.path.join(os.path.dirname(__file__), "..", "database")
DB_PATH = os.path.join(_DB_DIR, "ammayi.db")


def get_conn() -> sqlite3.Connection:
    """Return a connection with row_factory set so rows behave like dicts."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")   # safer concurrent reads
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    """Create tables and seed the singleton ammayi_state row if needed."""
    os.makedirs(_DB_DIR, exist_ok=True)

    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS ammayi_state (
                id                      INTEGER PRIMARY KEY DEFAULT 1,
                anger_score             INTEGER NOT NULL DEFAULT 0,
                total_errors            INTEGER NOT NULL DEFAULT 0,
                total_successes         INTEGER NOT NULL DEFAULT 0,
                current_failure_streak  INTEGER NOT NULL DEFAULT 0,
                longest_failure_streak  INTEGER NOT NULL DEFAULT 0,
                total_sessions          INTEGER NOT NULL DEFAULT 0,
                escape_attempts         INTEGER NOT NULL DEFAULT 0,
                highest_anger           INTEGER NOT NULL DEFAULT 0,
                last_error_type         TEXT,
                last_error_signature    TEXT,
                last_event_type         TEXT,
                last_event_at           TEXT,
                last_response_id        TEXT,
                created_at              TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS sessions (
                id              TEXT PRIMARY KEY,
                started_at      TEXT NOT NULL DEFAULT (datetime('now')),
                ended_at        TEXT,
                error_count     INTEGER NOT NULL DEFAULT 0,
                success_count   INTEGER NOT NULL DEFAULT 0,
                escape_detected INTEGER NOT NULL DEFAULT 0,
                starting_anger  INTEGER NOT NULL DEFAULT 0,
                ending_anger    INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS events (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id   TEXT,
                timestamp    TEXT NOT NULL DEFAULT (datetime('now')),
                event_type   TEXT NOT NULL,
                error_type   TEXT,
                anger_before INTEGER NOT NULL DEFAULT 0,
                anger_after  INTEGER NOT NULL DEFAULT 0,
                metadata     TEXT
            );

            CREATE TABLE IF NOT EXISTS response_usage (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                response_id TEXT NOT NULL,
                session_id  TEXT,
                used_at     TEXT NOT NULL DEFAULT (datetime('now'))
            );
        """)

        # Ensure the singleton row exists (id=1)
        conn.execute(
            "INSERT OR IGNORE INTO ammayi_state (id) VALUES (1)"
        )
        conn.commit()
