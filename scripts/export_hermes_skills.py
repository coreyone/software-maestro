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
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "skills"
MANIFEST_PATH = OUTPUT_ROOT / "_software_maestro_manifest.json"
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def source_skills(root: Path = ROOT, output_root: Path = OUTPUT_ROOT) -> dict[str, Path]:
    """Return Hermes slug to canonical skill directory mappings."""
    found: dict[str, Path] = {}
    for skill_md in sorted(root.rglob("SKILL.md")):
        relative = skill_md.relative_to(root)
        if ".git" in relative.parts or is_within(skill_md, output_root):
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
    match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", body, re.DOTALL)
    if not match:
        fail(f"{path}: missing or unterminated YAML frontmatter")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^(name|description):\s*(.+?)\s*$", line)
        if not field:
            continue
        value = field.group(2)
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        values[field.group(1)] = value

    for required in ("name", "description"):
        if not values.get(required):
            fail(f"{path}: frontmatter requires {required}")
    return values


def load_manifest(manifest_path: Path = MANIFEST_PATH) -> set[str]:
    if not manifest_path.is_file():
        return set()
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if data.get("format") != 1:
            fail(f"{manifest_path}: unsupported manifest format")
        entries = data.get("generated_skills")
        if not isinstance(entries, list):
            fail(f"{manifest_path}: generated_skills must be a list")
        slugs: set[str] = set()
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get("slug"), str):
                fail(f"{manifest_path}: each generated skill must have a slug")
            slug = entry["slug"]
            if not SLUG_RE.fullmatch(slug):
                fail(f"{manifest_path}: invalid generated skill slug {slug!r}")
            if slug in slugs:
                fail(f"{manifest_path}: duplicate generated skill slug {slug!r}")
            slugs.add(slug)
        return slugs
    except (OSError, AttributeError, TypeError, json.JSONDecodeError) as exc:
        fail(f"cannot read {manifest_path}: {exc}")


def expected_files(source_dir: Path) -> set[str]:
    return {
        path.relative_to(source_dir).as_posix()
        for path in source_dir.rglob("*")
        if path.is_file() and not path.is_symlink()
    }


def same_tree(source_dir: Path, target_dir: Path) -> bool:
    if source_dir.is_symlink() or target_dir.is_symlink():
        return False
    if any(path.is_symlink() for path in source_dir.rglob("*")):
        return False
    if any(path.is_symlink() for path in target_dir.rglob("*")):
        return False

    source_files = expected_files(source_dir)
    target_files = expected_files(target_dir)
    if source_files != target_files:
        return False
    return all(
        (source_dir / relative).read_bytes() == (target_dir / relative).read_bytes()
        for relative in source_files
    )


def manifest_payload(skills: dict[str, Path], root: Path) -> str:
    manifest = {
        "format": 1,
        "generated_by": "scripts/export_hermes_skills.py",
        "generated_skills": [
            {
                "slug": slug,
                "source": source_dir.relative_to(root).as_posix(),
            }
            for slug, source_dir in sorted(skills.items())
        ],
    }
    return json.dumps(manifest, indent=2) + "\n"


def check(
    skills: dict[str, Path],
    output_root: Path = OUTPUT_ROOT,
    manifest_path: Path = MANIFEST_PATH,
) -> int:
    if not output_root.is_dir() or output_root.is_symlink():
        print("Hermes export is missing: skills/")
        return 1

    managed = load_manifest(manifest_path)
    expected = set(skills)
    errors: list[str] = []
    if managed != expected:
        errors.append("manifest does not match the canonical skill inventory")

    for slug, source_dir in skills.items():
        target_dir = output_root / slug
        if not target_dir.is_dir() or target_dir.is_symlink():
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


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def write(
    skills: dict[str, Path],
    root: Path = ROOT,
    output_root: Path = OUTPUT_ROOT,
    manifest_path: Path = MANIFEST_PATH,
) -> int:
    output_root.mkdir(parents=True, exist_ok=True)
    if output_root.is_symlink():
        fail(f"refusing to write through symlink: {output_root}")

    managed = load_manifest(manifest_path)
    expected = set(skills)
    for slug in expected:
        target_dir = output_root / slug
        if target_dir.is_symlink():
            fail(f"refusing to replace symlink: {target_dir}")
        if target_dir.exists() and slug not in managed:
            fail(f"refusing to overwrite unmanaged Hermes skill: {target_dir}")

    staging_root = Path(tempfile.mkdtemp(prefix=".hermes-export-", dir=root))
    backup_root = Path(tempfile.mkdtemp(prefix=".hermes-export-backup-", dir=root))
    moved: list[str] = []
    installed: list[str] = []
    manifest_tmp: Path | None = None
    try:
        for slug, source_dir in skills.items():
            shutil.copytree(source_dir, staging_root / slug)

        for slug in sorted(managed - expected):
            stale_dir = output_root / slug
            if stale_dir.exists() or stale_dir.is_symlink():
                if stale_dir.is_symlink():
                    fail(f"refusing to replace symlink: {stale_dir}")
                os.replace(stale_dir, backup_root / slug)
                moved.append(slug)

        for slug in sorted(skills):
            target_dir = output_root / slug
            if target_dir.exists():
                os.replace(target_dir, backup_root / slug)
                moved.append(slug)
            os.replace(staging_root / slug, target_dir)
            installed.append(slug)

        fd, manifest_tmp_name = tempfile.mkstemp(
            prefix="._software_maestro_manifest.", suffix=".tmp", dir=output_root
        )
        manifest_tmp = Path(manifest_tmp_name)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(manifest_payload(skills, root))
        os.replace(manifest_tmp, manifest_path)
        manifest_tmp = None
    except BaseException:
        if manifest_tmp is not None:
            remove_path(manifest_tmp)
        for slug in reversed(installed):
            remove_path(output_root / slug)
        for slug in reversed(moved):
            backup_dir = backup_root / slug
            if backup_dir.exists() or backup_dir.is_symlink():
                os.replace(backup_dir, output_root / slug)
        shutil.rmtree(backup_root, ignore_errors=True)
        raise
    else:
        shutil.rmtree(backup_root, ignore_errors=True)
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)

    print(f"Wrote Hermes export: {len(skills)} skills")
    return check(skills, output_root, manifest_path)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="regenerate the flat Hermes export")
    mode.add_argument("--check", action="store_true", help="verify the flat Hermes export")
    args = parser.parse_args()
    skills = source_skills()
    return write(skills) if args.write else check(skills)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
