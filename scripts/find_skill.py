#!/usr/bin/env python3
"""
Software Maestro Skill Finder
Fast, zero-dependency local search utility to discover and inspect skills across software-maestro.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]

# ANSI Colors
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
DIM = "\033[2m"
RESET = "\033[0m"


def parse_skill(skill_md_path: Path) -> Optional[Dict[str, Any]]:
    try:
        content = skill_md_path.read_text(encoding="utf-8")
    except Exception:
        return None

    fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None

    fm_text = fm_match.group(1)
    name_match = re.search(r"name:\s*([^\n]+)", fm_text)
    desc_match = re.search(r"description:\s*([^\n]+|\".*?\"|'.*?')", fm_text, re.DOTALL)

    name = name_match.group(1).strip().strip('"').strip("'") if name_match else skill_md_path.parent.name
    raw_desc = desc_match.group(1).strip().strip('"').strip("'") if desc_match else ""

    # Extract Trigger, Scope, Boundary
    trigger_match = re.search(r"Trigger:\s*(.*?)(?=\s*(?:Scope:|Boundary:|$))", raw_desc, re.IGNORECASE | re.DOTALL)
    scope_match = re.search(r"Scope:\s*(.*?)(?=\s*(?:Boundary:|$))", raw_desc, re.IGNORECASE | re.DOTALL)
    boundary_match = re.search(r"Boundary:\s*(.*?)$", raw_desc, re.IGNORECASE | re.DOTALL)

    trigger = trigger_match.group(1).strip() if trigger_match else ""
    scope = scope_match.group(1).strip() if scope_match else ""
    boundary = boundary_match.group(1).strip() if boundary_match else ""

    # Extract Lineage / Theorists / Lead heading from body
    lineage_match = re.search(r"(?:Lineage|Origins|Theorists|Foundational Methodologies)[\*:\s]+([^\n]+)", content, re.IGNORECASE)
    lineage = lineage_match.group(1).strip().strip("*").strip("_") if lineage_match else ""

    rel_path = skill_md_path.relative_to(ROOT)
    domain = rel_path.parts[0] if len(rel_path.parts) > 1 else "root"
    subdomain = rel_path.parts[1] if len(rel_path.parts) > 2 else ""

    return {
        "name": name,
        "path": str(skill_md_path),
        "rel_path": str(rel_path),
        "domain": domain,
        "subdomain": subdomain,
        "description": raw_desc,
        "trigger": trigger,
        "scope": scope,
        "boundary": boundary,
        "lineage": lineage,
        "body": content,
    }


def score_skill(skill: Dict[str, Any], query_terms: List[str]) -> int:
    score = 0
    name_lower = skill["name"].casefold()
    trigger_lower = skill["trigger"].casefold()
    scope_lower = skill["scope"].casefold()
    desc_lower = skill["description"].casefold()
    lineage_lower = skill["lineage"].casefold()
    body_lower = skill["body"].casefold()
    rel_path_lower = skill["rel_path"].casefold()

    full_query = " ".join(query_terms).casefold()

    # Exact full-phrase matches
    if full_query == name_lower or full_query == f"/{name_lower}":
        score += 150
    elif full_query in name_lower or full_query in rel_path_lower:
        score += 80

    if full_query in trigger_lower:
        score += 60
    if full_query in scope_lower or full_query in desc_lower:
        score += 40
    if full_query in lineage_lower:
        score += 40

    # Term-by-term scoring
    for term in query_terms:
        term_clean = term.strip("/").casefold()
        if not term_clean:
            continue

        if term_clean == name_lower:
            score += 100
        elif term_clean in name_lower:
            score += 35

        if term_clean in trigger_lower:
            score += 25
        if term_clean in lineage_lower:
            score += 20
        if term_clean in scope_lower or term_clean in desc_lower:
            score += 15
        if term_clean in rel_path_lower:
            score += 10
        if term_clean in body_lower:
            score += 3

    return score


def find_skills(
    query: Optional[str] = None,
    domain_filter: Optional[str] = None,
) -> List[Tuple[Dict[str, Any], int]]:
    skill_files = sorted(list(ROOT.glob("**/SKILL.md")))
    results: List[Tuple[Dict[str, Any], int]] = []

    query_terms = query.strip().split() if query and query.strip() else []

    for sf in skill_files:
        skill = parse_skill(sf)
        if not skill:
            continue

        if domain_filter and skill["domain"].casefold() != domain_filter.casefold():
            continue

        if not query_terms:
            results.append((skill, 1))
        else:
            score = score_skill(skill, query_terms)
            if score > 0:
                results.append((skill, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def print_terminal_results(results: List[Tuple[Dict[str, Any], int]], limit: int = 5):
    if not results:
        print(f"\n{RED}No matching skills found in software-maestro.{RESET}\n")
        return

    print(f"\n{BOLD}{GREEN}Found {len(results)} matching skill(s) in software-maestro:{RESET}\n")

    for i, (s, score) in enumerate(results[:limit], 1):
        print(f"{BOLD}{CYAN}{i}. /{s['name']}{RESET} {DIM}(Score: {score} | {s['rel_path']}){RESET}")
        if s["lineage"]:
            print(f"   {YELLOW}Framework & Lineage:{RESET} {s['lineage']}")
        if s["scope"]:
            print(f"   {BOLD}Scope:{RESET} {s['scope']}")
        if s["trigger"]:
            print(f"   {GREEN}Triggers:{RESET} {s['trigger']}")
        if s["boundary"]:
            print(f"   {RED}Boundary:{RESET} {s['boundary']}")
        print(f"   {DIM}Path: file://{s['path']}{RESET}\n")

    if len(results) > limit:
        print(f"{DIM}... and {len(results) - limit} more match(es). Use --all to view all.{RESET}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Search, discover, and inspect local Software Maestro agent skills."
    )
    parser.add_argument("query", nargs="*", default=[], help="Keywords or skill name to search for")
    parser.add_argument("--domain", "-d", help="Filter by lifecycle domain (product, design, engineering, etc.)")
    parser.add_argument("--all", "-a", action="store_true", help="Show all matching results without limit")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()
    query_str = " ".join(args.query).strip()

    results = find_skills(query=query_str, domain_filter=args.domain)

    if args.json:
        payload = [
            {
                "name": s["name"],
                "slash_command": f"/{s['name']}",
                "score": score,
                "domain": s["domain"],
                "subdomain": s["subdomain"],
                "rel_path": s["rel_path"],
                "path": s["path"],
                "lineage": s["lineage"],
                "scope": s["scope"],
                "trigger": s["trigger"],
                "boundary": s["boundary"],
            }
            for s, score in results
        ]
        print(json.dumps(payload, indent=2))
        return

    limit = 999 if args.all or not query_str else 5
    print_terminal_results(results, limit=limit)


if __name__ == "__main__":
    main()
