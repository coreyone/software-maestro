#!/usr/bin/env python3
"""Audit a dialect profile for research-only policy violations."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ALLOWED_EVIDENCE = {
    "direct-hds", "peer-reviewed", "academic-book", "academic-project", "dissertation"
}
BANNED_UNSOURCED_MARKERS = {
    "ope", "uff da", "you betcha", "dontcha know", "midwest nice"
}

def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("profile", type=Path)
    args = ap.parse_args()

    data = json.loads(args.profile.read_text(encoding="utf-8"))
    features = data.get("features", [])
    errors: list[str] = []

    if not isinstance(features, list):
        fail("features must be a list", errors)
        features = []

    for i, f in enumerate(features):
        prefix = f"feature[{i}]"
        if not isinstance(f, dict):
            fail(f"{prefix}: must be an object", errors)
            continue

        hq = f.get("hds_question")
        if hq is not None and not (isinstance(hq, int) and 1 <= hq <= 122):
            fail(f"{prefix}: HDS question must be 1..122 or null", errors)

        evidence = f.get("evidence")
        if evidence is None:
            # Generated HDS profile uses single source_id/evidence_class fields.
            ec = f.get("evidence_class")
            sid = f.get("source_id")
            if ec not in ALLOWED_EVIDENCE or not sid:
                fail(f"{prefix}: missing valid research evidence", errors)
        else:
            if not evidence:
                fail(f"{prefix}: evidence list is empty", errors)
            for e in evidence:
                if e.get("evidence_class") not in ALLOWED_EVIDENCE:
                    fail(f"{prefix}: invalid evidence class {e.get('evidence_class')!r}", errors)
                if not e.get("source_id"):
                    fail(f"{prefix}: missing source_id", errors)

        text = " ".join(str(f.get(k, "")) for k in ("id","form","notes")).lower()
        for marker in BANNED_UNSOURCED_MARKERS:
            if marker in text and not f.get("evidence"):
                fail(f"{prefix}: stereotype marker {marker!r} lacks explicit evidence", errors)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)

    print(f"OK: {len(features)} features; research-scope audit passed")

if __name__ == "__main__":
    main()
