# config.py — all tunable constants in one place

EXEC_TIMEOUT_SECONDS = 5
MAX_STDOUT_CHARS = 4000
RAPID_REPEAT_THRESHOLD_SECONDS = 12
LONG_STREAK_THRESHOLD = 5
MAX_ANGER_SCORE = 20
MIN_ACCEPTABLE_RESPONSE_SCORE = 30

CORS_ALLOWED_ORIGINS = ["*"]  # tighten to Stitch origin before demo

# Anger score → level mapping (0-8)
ANGER_SCORE_TO_LEVEL = [
    (0,  0, "CALM"),
    (2,  1, "UNIMPRESSED"),
    (4,  2, "SUSPICIOUS"),
    (6,  3, "DISAPPOINTED"),
    (8,  4, "ANNOYED"),
    (10, 5, "ANGRY"),
    (12, 6, "FURIOUS"),
    (14, 7, "AMMAYI RAGE"),
    (20, 8, "INCENSED"),
]

def anger_level_from_score(score: int) -> tuple[int, str]:
    """Return (level 0-8, label) for a given raw score."""
    for threshold, level, label in reversed(ANGER_SCORE_TO_LEVEL):
        if score >= threshold:
            return level, label
    return 0, "CALM"
