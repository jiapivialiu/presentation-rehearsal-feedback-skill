from __future__ import annotations

import csv
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
CASES = ROOT / "evals" / "cases.yaml"


class RepositoryTests(unittest.TestCase):
    def test_skill_frontmatter_and_size(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        self.assertLess(len(text.splitlines()), 500)
        self.assertTrue(text.startswith("---\n"))
        frontmatter = text.split("---", 2)[1].strip().splitlines()
        keys = {line.split(":", 1)[0].strip() for line in frontmatter if ":" in line}
        self.assertEqual(keys, {"name", "description"})
        self.assertIn("name: presentation-rehearsal-feedback-skill", frontmatter)

    def test_portable_core_has_no_provider_or_old_name(self) -> None:
        provider_name = "mac" + "parakeet"
        old_skill_name = "defence" + "-feedback-synthesis"
        text = SKILL.read_text(encoding="utf-8").lower()
        self.assertNotIn(provider_name, text)
        self.assertNotIn(old_skill_name, text)
        for platform_term in ("codex", "openai", "mcp"):
            self.assertNotIn(platform_term, text)

    def test_repository_has_no_provider_artifacts_or_local_paths(self) -> None:
        provider_name = "mac" + "parakeet"
        old_skill_name = "defence" + "-feedback-synthesis"
        user_root = b"/" + b"Users" + b"/"
        home_root = b"/" + b"home" + b"/"
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
                continue
            data = path.read_bytes()
            self.assertNotIn(provider_name.encode(), data.lower(), path.as_posix())
            self.assertNotIn(old_skill_name.encode(), data.lower(), path.as_posix())
            self.assertNotIn(user_root, data, path.as_posix())
            self.assertNotIn(home_root, data, path.as_posix())

    def test_openai_metadata_matches_skill(self) -> None:
        text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Presentation Rehearsal Feedback"', text)
        self.assertIn("$presentation-rehearsal-feedback-skill", text)
        match = re.search(r'short_description: "([^"]+)"', text)
        self.assertIsNotNone(match)
        self.assertGreaterEqual(len(match.group(1)), 25)
        self.assertLessEqual(len(match.group(1)), 64)

    def test_readme_documents_open_input_and_compatibility(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        required_phrase = (
            "The skill works with transcripts, notes, processed transcripts, reviewer "
            "feedback, and related presentation materials explicitly identified by the "
            "user, in any format the active agent can read."
        )
        self.assertIn(required_phrase, text)
        expected_install_paths = (
            ".agents/skills/presentation-rehearsal-feedback-skill/",
            ".cursor/skills/presentation-rehearsal-feedback-skill/",
            ".claude/skills/presentation-rehearsal-feedback-skill/",
            ".github/skills/presentation-rehearsal-feedback-skill/",
        )
        for install_path in expected_install_paths:
            self.assertIn(install_path, text)
        for platform in ("Codex", "Cursor", "Claude Code", "GitHub Copilot"):
            self.assertIn(platform, text)
        self.assertIn("Known limitations", text)
        self.assertIn("Tested compatibility", text)

    def test_repository_has_one_canonical_skill_copy(self) -> None:
        skill_files = [
            path
            for path in ROOT.rglob("SKILL.md")
            if ".git" not in path.parts
        ]
        self.assertEqual(skill_files, [SKILL])
        self.assertFalse((ROOT / ".agents" / "skills").exists())
        self.assertFalse((ROOT / ".claude").exists())
        self.assertFalse((ROOT / ".cursor").exists())
        self.assertFalse((ROOT / ".github" / "skills").exists())

    def test_mit_license_is_present(self) -> None:
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("MIT License\n"))
        self.assertIn("Copyright (c) 2026", text)
        self.assertIn(
            'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND',
            text,
        )
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("licensed under the [MIT License](LICENSE)", readme)

    def test_fourteen_declared_cases_exist(self) -> None:
        text = CASES.read_text(encoding="utf-8")
        case_ids = re.findall(r'case_id: "([^"]+)"', text)
        input_lists = re.findall(r"inputs: \[([^]]+)\]", text)
        self.assertEqual(len(case_ids), 14)
        self.assertEqual(len(set(case_ids)), 14)
        self.assertEqual(len(input_lists), 14)
        for raw_list in input_lists:
            paths = re.findall(r'"([^"]+)"', raw_list)
            self.assertTrue(paths)
            for relative in paths:
                fixture = ROOT / "evals" / relative
                self.assertTrue(fixture.is_file(), relative)
                self.assertGreater(fixture.stat().st_size, 0, relative)

    def test_structured_synthetic_fixtures_parse(self) -> None:
        cases_dir = ROOT / "evals" / "cases"
        for path in cases_dir.glob("*.json"):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))
        for path in cases_dir.glob("*.jsonl"):
            with self.subTest(path=path.name):
                rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
                self.assertTrue(rows)
        for path in cases_dir.glob("*.csv"):
            with self.subTest(path=path.name):
                with path.open(encoding="utf-8", newline="") as stream:
                    rows = list(csv.DictReader(stream))
                self.assertTrue(rows)
        for path in cases_dir.glob("*.svg"):
            with self.subTest(path=path.name):
                ET.parse(path)

    def test_approval_and_inclusive_rules_are_explicit(self) -> None:
        text = SKILL.read_text(encoding="utf-8").lower()
        self.assertIn("explicitly approves specific proposed changes", text)
        self.assertIn("partial approval", text)
        self.assertIn("sounding \"more native.\"", text)
        self.assertIn("code-switching", text)


if __name__ == "__main__":
    unittest.main()
