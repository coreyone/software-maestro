#!/usr/bin/env python3
"""Validate and score Software Maestro binary skill evals."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CASE_KEYS = {
    "id",
    "prompt",
    "pass_rule",
    "must",
    "must_not",
    "pass_fixture",
    "fail_fixture",
}


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def score_case(case: dict[str, Any], candidate: str) -> tuple[bool, list[str]]:
    normalized = normalize(candidate)
    failures: list[str] = []

    for requirement in case["must"]:
        alternatives = requirement if isinstance(requirement, list) else [requirement]
        if not any(normalize(term) in normalized for term in alternatives):
            failures.append(f"missing one of: {alternatives}")

    for forbidden in case["must_not"]:
        alternatives = forbidden if isinstance(forbidden, list) else [forbidden]
        matched = [term for term in alternatives if normalize(term) in normalized]
        if matched:
            failures.append(f"contains forbidden text: {matched}")

    return not failures, failures


def validate_term_group(value: Any, location: str) -> list[str]:
    errors: list[str] = []
    if isinstance(value, str):
        if not value.strip():
            errors.append(f"{location}: empty term")
        return errors
    if not isinstance(value, list) or not value:
        return [f"{location}: expected a string or non-empty list of alternatives"]
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{location}[{index}]: expected a non-empty string")
    return errors


def validate_suite(eval_path: Path) -> tuple[int, int, list[str]]:
    errors: list[str] = []
    try:
        suite = json.loads(eval_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        return 0, 0, [f"{eval_path}: {exc}"]

    skill_dir = eval_path.parent.parent
    skill_name = suite.get("skill")
    if skill_name != skill_dir.name:
        errors.append(
            f"{eval_path}: skill {skill_name!r} does not match directory {skill_dir.name!r}"
        )

    if suite.get("version") != 1:
        errors.append(f"{eval_path}: version must be 1")

    trigger_cases = suite.get("trigger_cases")
    if not isinstance(trigger_cases, list) or not trigger_cases:
        errors.append(f"{eval_path}: trigger_cases must be a non-empty list")
        trigger_cases = []
    else:
        polarities = set()
        for index, case in enumerate(trigger_cases):
            location = f"{eval_path}: trigger_cases[{index}]"
            if not isinstance(case, dict):
                errors.append(f"{location}: expected an object")
                continue
            if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
                errors.append(f"{location}: prompt must be a non-empty string")
            if not isinstance(case.get("trigger"), bool):
                errors.append(f"{location}: trigger must be boolean")
            else:
                polarities.add(case["trigger"])
        if polarities != {True, False}:
            errors.append(f"{eval_path}: trigger_cases must include true and false cases")

    binary_cases = suite.get("binary_cases")
    if not isinstance(binary_cases, list) or not binary_cases:
        errors.append(f"{eval_path}: binary_cases must be a non-empty list")
        binary_cases = []

    seen_ids: set[str] = set()
    for index, case in enumerate(binary_cases):
        location = f"{eval_path}: binary_cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{location}: expected an object")
            continue

        missing = REQUIRED_CASE_KEYS - case.keys()
        if missing:
            errors.append(f"{location}: missing keys {sorted(missing)}")
            continue

        case_id = case["id"]
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9-]+", case_id):
            errors.append(f"{location}: id must use lowercase letters, digits, and hyphens")
        elif case_id in seen_ids:
            errors.append(f"{location}: duplicate id {case_id!r}")
        else:
            seen_ids.add(case_id)

        for key in ("prompt", "pass_rule", "pass_fixture", "fail_fixture"):
            if not isinstance(case[key], str) or not case[key].strip():
                errors.append(f"{location}: {key} must be a non-empty string")

        for key in ("must", "must_not"):
            if not isinstance(case[key], list):
                errors.append(f"{location}: {key} must be a list")
                continue
            for term_index, term_group in enumerate(case[key]):
                errors.extend(
                    validate_term_group(term_group, f"{location}: {key}[{term_index}]")
                )

        if any(error.startswith(location) for error in errors):
            continue

        pass_result, pass_failures = score_case(case, case["pass_fixture"])
        if not pass_result:
            errors.append(
                f"{location}: pass_fixture failed its grader: {'; '.join(pass_failures)}"
            )

        fail_result, _ = score_case(case, case["fail_fixture"])
        if fail_result:
            errors.append(f"{location}: fail_fixture unexpectedly passed its grader")

    return len(trigger_cases), len(binary_cases), errors


def find_eval_files(paths: list[str]) -> list[Path]:
    if not paths:
        return sorted(ROOT.glob("*/*/evals/cases.json"))

    resolved: list[Path] = []
    for raw_path in paths:
        candidate = Path(raw_path).resolve()
        if candidate.is_dir():
            candidate = candidate / "evals" / "cases.json"
        resolved.append(candidate)
    return resolved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Skill directories or cases.json files")
    parser.add_argument("--case", dest="case_id", help="Score one binary case")
    parser.add_argument("--response", type=Path, help="Candidate response file")
    args = parser.parse_args()

    eval_files = find_eval_files(args.paths)
    if not eval_files:
        print("No binary eval suites found.", file=sys.stderr)
        return 1

    if args.case_id or args.response:
        if not (args.case_id and args.response) or len(eval_files) != 1:
            parser.error("--case and --response require exactly one eval suite")
        suite = json.loads(eval_files[0].read_text())
        matching = [
            case for case in suite["binary_cases"] if case["id"] == args.case_id
        ]
        if not matching:
            print(f"Unknown case: {args.case_id}", file=sys.stderr)
            return 2
        passed, failures = score_case(matching[0], args.response.read_text())
        print("PASS" if passed else "FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 0 if passed else 1

    total_triggers = 0
    total_binary = 0
    all_errors: list[str] = []
    for eval_file in eval_files:
        triggers, binary, errors = validate_suite(eval_file)
        total_triggers += triggers
        total_binary += binary
        all_errors.extend(errors)

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1

    print(
        f"PASS: {len(eval_files)} suites, "
        f"{total_triggers} trigger cases, {total_binary} binary cases"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
