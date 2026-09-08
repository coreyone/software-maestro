#!/usr/bin/env python3
"""Regression tests for the Hermes compatibility export."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import export_hermes_skills as exporter


class ExportHermesSkillsTests(unittest.TestCase):
    def add_skill(self, root: Path, path: str, name: str = "example-skill") -> Path:
        skill_dir = root / path
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: Example skill\n---\n\n# Example\n",
            encoding="utf-8",
        )
        return skill_dir

    def test_inventory_excludes_only_the_configured_export_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output_root = root / "skills"
            self.add_skill(root, "product/skills/example")
            self.add_skill(root, "skills/generated", name="generated-skill")

            skills = exporter.source_skills(root, output_root)

            self.assertEqual(set(skills), {"example-skill"})

    def test_duplicate_slugs_fail_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.add_skill(root, "product/one")
            self.add_skill(root, "engineering/two")

            with self.assertRaises(SystemExit):
                exporter.source_skills(root, root / "skills")

    def test_write_and_check_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output_root = root / "skills"
            manifest_path = output_root / "_software_maestro_manifest.json"
            self.add_skill(root, "product/example")
            skills = exporter.source_skills(root, output_root)

            self.assertEqual(exporter.write(skills, root, output_root, manifest_path), 0)
            self.assertEqual(exporter.check(skills, output_root, manifest_path), 0)

            (skills["example-skill"] / "SKILL.md").write_text(
                "---\nname: example-skill\ndescription: Changed\n---\n\n# Changed\n",
                encoding="utf-8",
            )
            self.assertEqual(exporter.check(skills, output_root, manifest_path), 1)

    def test_symlink_in_skill_package_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill_dir = self.add_skill(root, "product/example")
            (skill_dir / "references").mkdir()
            (skill_dir / "references" / "link.md").symlink_to(skill_dir / "SKILL.md")

            with self.assertRaises(SystemExit):
                exporter.source_skills(root, root / "skills")

    def test_failed_write_preserves_the_last_good_export(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output_root = root / "skills"
            manifest_path = output_root / "_software_maestro_manifest.json"
            self.add_skill(root, "product/example")
            skills = exporter.source_skills(root, output_root)
            exporter.write(skills, root, output_root, manifest_path)
            original = (output_root / "example-skill" / "SKILL.md").read_bytes()

            with patch.object(exporter.shutil, "copytree", side_effect=OSError("test failure")):
                with self.assertRaises(OSError):
                    exporter.write(skills, root, output_root, manifest_path)

            self.assertEqual(
                (output_root / "example-skill" / "SKILL.md").read_bytes(), original
            )
            self.assertEqual(exporter.check(skills, output_root, manifest_path), 0)
            self.assertEqual(list(root.glob(".hermes-export-*")), [])


if __name__ == "__main__":
    unittest.main()
