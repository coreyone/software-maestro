#!/usr/bin/env python3
"""Export software-maestro's domain tree to Hermes' flat tap layout.

The canonical skill tree stays organized by lifecycle domain. Hermes taps scan
only the immediate child directories of the configured path, so this script
materializes a flat compatibility tree under ``skills/`` without changing the
canonical files used by Codex, Gemini, Claude, or other clients.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "skills"
MANIFEST_PATH = OUTPUT_ROOT / "_software_maestro_manifest.json"
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def source_skills() -> dict[str, Path]:
    """Return Hermes slug to canonical skill directory mappings."""
    found: dict[str, Path] = {}
    for skill_md in sorted(ROOT.rglob("SKILL.md")):
        if ".git" in skill_md.parts or "skills" in skill_md.relative_to(ROOT).parts:
            continue

        body = skill_md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(body, skill_md)
        slug = frontmatter["name"]
        if not SLUG_RE.fullmatch(slug):
            fail(f"{skill_md}: name must be lowercase-hyphen format, got {slug!r}")
        if slug in found:
            fail(f"duplicate Hermes slug {slug!r}: {found[slug]} and {skill_md}")

        skill_dir = skill_md.parent
        for path in skill_dir.rglob("*"):
            if path.is_symlink():
                fail(f"{skill_dir}: symlinks are not portable in a GitHub tap")
        found[slug] = skill_dir
    return found


def parse_frontmatter(body: str, path: Path) -> dict[str, str]:
    """Parse the required scalar frontmatter without adding a YAML dependency."""
    if not body.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    end = body.find("\n---\n", 4)
    if end < 0:
        fail(f"{path}: unterminated YAML frontmatter")

    values: dict[str, str] = {}
    for line in body[4:end].splitlines():
        match = re.match(r"^(name|description):\s*(.+?)\s*$", line)
        if not match:
            continue
        value = match.group(2)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[match.group(1)] = value

    for required in ("name", "description"):
        if not values.get(required):
            fail(f"{path}: frontmatter requires {required}")
    return values


def load_manifest() -> set[str]:
    if not MANIFEST_PATH.is_file():
        return set()
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        return {entry["slug"] for entry in data.get("generated_skills", [])}
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        fail(f"cannot read {MANIFEST_PATH}: {exc}")


def expected_files(source_dir: Path) -> set[str]:
    return {path.relative_to(source_dir).as_posix() for path in source_dir.rglob("*") if path.is_file()}


def same_tree(source_dir: Path, target_dir: Path) -> bool:
    source_files = expected_files(source_dir)
    target_files = {path.relative_to(target_dir).as_posix() for path in target_dir.rglob("*") if path.is_file()}
    if source_files != target_files:
        return False
    return all(
        (source_dir / relative).read_bytes() == (target_dir / relative).read_bytes()
        for relative in source_files
    )


def check(skills: dict[str, Path]) -> int:
    if not OUTPUT_ROOT.is_dir():
        print("Hermes export is missing: skills/")
        return 1

    managed = load_manifest()
    expected = set(skills)
    errors: list[str] = []
    if managed != expected:
        errors.append("manifest does not match the canonical skill inventory")

    for slug, source_dir in skills.items():
        target_dir = OUTPUT_ROOT / slug
        if not target_dir.is_dir():
            errors.append(f"missing export: skills/{slug}/")
        elif not same_tree(source_dir, target_dir):
            errors.append(f"stale export: skills/{slug}/")

    if errors:
        print("Hermes export is out of date:")
        for error in errors:
            print(f"- {error}")
        print("Run: python3 scripts/export_hermes_skills.py --write")
        return 1

    print(f"Hermes export is current: {len(skills)} skills")
    return 0


def write(skills: dict[str, Path]) -> int:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    managed = load_manifest()

    for slug in managed - set(skills):
        stale_dir = OUTPUT_ROOT / slug
        if stale_dir.exists():
            shutil.rmtree(stale_dir)

    for slug, source_dir in skills.items():
        target_dir = OUTPUT_ROOT / slug
        if target_dir.exists() and slug not in managed:
            fail(f"refusing to overwrite unmanaged Hermes skill: {target_dir}")
        if target_dir.exists():
            shutil.rmtree(target_dir)
        shutil.copytree(source_dir, target_dir)

    manifest = {
        "format": 1,
        "generated_by": "scripts/export_hermes_skills.py",
        "generated_skills": [
            {
                "slug": slug,
                "source": source_dir.relative_to(ROOT).as_posix(),
            }
            for slug, source_dir in sorted(skills.items())
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote Hermes export: {len(skills)} skills")
    return check(skills)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="regenerate the flat Hermes export")
    args = parser.parse_args()
    skills = source_skills()
    return write(skills) if args.write else check(skills)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
