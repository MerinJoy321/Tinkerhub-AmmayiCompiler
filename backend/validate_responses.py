#!/usr/bin/env python3
"""
validate_responses.py
Validates data/ammayi/responses.json against canonical requirements:
  - Exactly 55 entries
  - IDs R001 through R055, no gaps, no duplicates
  - Every entry has a non-empty text_ml
  - Every audio path matches the response's own R-number
  - No required field missing

Run from the backend/ directory:
    python validate_responses.py
"""

import json
import os
import sys

EXPECTED_COUNT = 55
RESPONSES_PATH = os.path.join(os.path.dirname(__file__), "data", "ammayi", "responses.json")

def main():
    errors = []

    with open(RESPONSES_PATH, encoding="utf-8") as f:
        library = json.load(f)

    # 1. Count
    if len(library) != EXPECTED_COUNT:
        errors.append(f"Expected {EXPECTED_COUNT} responses, found {len(library)}")

    # 2. IDs: R001–R055, no gaps, no duplicates
    expected_ids = {f"R{i:03d}" for i in range(1, EXPECTED_COUNT + 1)}
    found_ids = []
    for entry in library:
        rid = entry.get("id", "")
        found_ids.append(rid)

    found_set = set(found_ids)
    missing = expected_ids - found_set
    extra = found_set - expected_ids
    duplicates = [rid for rid in found_ids if found_ids.count(rid) > 1]

    if missing:
        errors.append(f"Missing IDs: {sorted(missing)}")
    if extra:
        errors.append(f"Unexpected IDs: {sorted(extra)}")
    if duplicates:
        errors.append(f"Duplicate IDs: {sorted(set(duplicates))}")

    # 3. Per-entry checks
    for entry in library:
        rid = entry.get("id", "?")

        # text_ml must be non-empty
        text = entry.get("text_ml", "")
        if not text or not text.strip():
            errors.append(f"{rid}: text_ml is empty or missing")

        # audio path must match R-number (if present)
        audio = entry.get("audio")
        if audio:
            expected_audio = f"/assets/audio/ammayi/{rid}.wav"
            if audio != expected_audio:
                errors.append(f"{rid}: audio path is '{audio}', expected '{expected_audio}'")

        # required structural fields
        for field in ["event_types", "error_types", "situations", "anger_range"]:
            if field not in entry:
                errors.append(f"{rid}: missing field '{field}'")

    # 4. Report
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"VALIDATION PASSED: {len(library)} canonical responses, R001–R055, all checks OK.")
        sys.exit(0)

if __name__ == "__main__":
    main()
