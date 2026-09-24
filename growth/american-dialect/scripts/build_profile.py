#!/usr/bin/env python3
"""
Build a state-aggregated profile from a machine-readable Harvard Dialect Survey JS file.

Expected input structure (as used by tjstum/dialect's dialect-data-survey.js):
    const DIALECT_SURVEY_QUESTIONS = [ ... ];
    const DIALECT_SURVEY_STATE_DATA = { ... };

Only HDS question IDs 1..122 are retained. Modeled/extended questions are rejected.

This script computes descriptive state-level aggregates. State groups are proxies, not
linguistic dialect boundaries.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGIONS_PATH = ROOT / "assets" / "region-proxies.json"

def extract_json_assignment(text: str, variable: str) -> Any:
    marker = f"const {variable} ="
    start = text.find(marker)
    if start < 0:
        raise ValueError(f"Could not find {variable}")
    i = start + len(marker)
    while i < len(text) and text[i].isspace():
        i += 1
    if i >= len(text) or text[i] not in "[{":
        raise ValueError(f"{variable} does not begin with JSON-like data")
    opening = text[i]
    closing = "]" if opening == "[" else "}"
    depth = 0
    in_string = False
    escape = False
    for j in range(i, len(text)):
        ch = text[j]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == opening:
            depth += 1
        elif ch == closing:
            depth -= 1
            if depth == 0:
                return json.loads(text[i:j+1])
    raise ValueError(f"Unterminated data for {variable}")

def hq_number(q: dict[str, Any]) -> int | None:
    if isinstance(q.get("hq"), int):
        return q["hq"]
    m = re.fullmatch(r"q_(\d+)", str(q.get("id", "")))
    return int(m.group(1)) if m else None

def load_regions() -> dict[str, Any]:
    return json.loads(REGIONS_PATH.read_text(encoding="utf-8"))["regions"]

def choose_states(region: str, explicit_states: list[str] | None) -> list[str]:
    if explicit_states:
        return [s.upper() for s in explicit_states]
    regions = load_regions()
    if region.upper() in {
        "AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA",
        "KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM",
        "NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA",
        "WV","WI","WY"
    }:
        return [region.upper()]
    if region not in regions:
        raise ValueError(f"Unknown region {region!r}. Available: {', '.join(sorted(regions))}")
    return regions[region]["states"]

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path, help="Path to dialect-data-survey.js")
    ap.add_argument("--region", default="midwest")
    ap.add_argument("--states", nargs="*", help="Explicit state abbreviations; overrides --region")
    ap.add_argument("--min-share", type=float, default=35.0,
                    help="Minimum target-region percentage to include an answer (default: 35)")
    ap.add_argument("--min-lift", type=float, default=5.0,
                    help="Minimum target minus national percentage-point lift (default: 5)")
    ap.add_argument("--top", type=int, default=80)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    text = args.source.read_text(encoding="utf-8")
    questions = extract_json_assignment(text, "DIALECT_SURVEY_QUESTIONS")
    state_data = extract_json_assignment(text, "DIALECT_SURVEY_STATE_DATA")

    # Original HDS only.
    q_by_id: dict[str, dict[str, Any]] = {}
    for q in questions:
        hq = hq_number(q)
        if hq is None or not (1 <= hq <= 122):
            continue
        q_by_id[q["id"]] = q

    states = choose_states(args.region, args.states)
    missing = [s for s in states if s not in state_data]
    if missing:
        raise ValueError(f"Missing state data: {', '.join(missing)}")

    all_states = list(state_data.keys())
    records: list[dict[str, Any]] = []

    for qid, q in q_by_id.items():
        opts = {o["id"]: o["label"] for o in q.get("options", [])}
        regional: dict[str, float] = {}
        national: dict[str, float] = {}

        for aid, label in opts.items():
            rv = [float(state_data[s].get(qid, {}).get(aid, 0.0)) for s in states]
            nv = [float(state_data[s].get(qid, {}).get(aid, 0.0)) for s in all_states]
            regional[aid] = statistics.fmean(rv) if rv else 0.0
            national[aid] = statistics.fmean(nv) if nv else 0.0

        ranked = sorted(regional, key=regional.get, reverse=True)
        if not ranked:
            continue
        best = ranked[0]
        second = regional[ranked[1]] if len(ranked) > 1 else 0.0
        share = regional[best]
        lift = share - national[best]
        margin = share - second

        if share < args.min_share or lift < args.min_lift:
            continue

        records.append({
            "question_id": qid,
            "hds_question": hq_number(q),
            "question": q.get("text"),
            "answer_id": best,
            "answer": opts.get(best, best),
            "regional_share": round(share, 2),
            "national_share": round(national[best], 2),
            "lift": round(lift, 2),
            "margin": round(margin, 2),
            "states": states,
            "evidence_class": "direct-hds",
            "source_id": "Vaux-Golder-2003-HDS",
        })

    records.sort(key=lambda r: (r["lift"], r["margin"], r["regional_share"]), reverse=True)
    records = records[: args.top]

    payload = {
        "profile": args.region,
        "source": str(args.source),
        "source_scope": "Harvard Dialect Survey questions 1-122 only",
        "states": states,
        "method": "unweighted mean of state-level answer percentages",
        "warning": "State aggregation is a computational proxy, not a dialect boundary or individual-level probability.",
        "thresholds": {
            "min_share_percent": args.min_share,
            "min_lift_percentage_points": args.min_lift,
        },
        "features": records,
    }

    out = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out, encoding="utf-8")
        print(args.output)
    else:
        print(out, end="")

if __name__ == "__main__":
    main()
