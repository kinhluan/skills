from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
sys.path.insert(0, str(ROOT / "scripts"))

import package_skills  # noqa: E402
import sync_manifest  # noqa: E402


class RepositoryIntegrityTest(unittest.TestCase):
    def test_canonical_source_is_real_skills_directory(self) -> None:
        self.assertTrue(SKILLS.is_dir())
        self.assertFalse(SKILLS.is_symlink())
        self.assertFalse((ROOT / ".agent-skills").exists())

    def test_manifest_is_derived_from_canonical_sources(self) -> None:
        current = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
        expected = sync_manifest.build_manifest(ROOT / "skills.json", SKILLS)
        self.assertEqual(expected, current)
        self.assertEqual(64, len(current["skills"]))
        self.assertTrue(
            all(entry["path"] == f"./skills/{entry['name']}" for entry in current["skills"])
        )

    def test_skills_use_single_authoritative_instruction_file(self) -> None:
        self.assertEqual([], list(SKILLS.rglob("SKILL.toon")))
        nested = [
            path
            for path in SKILLS.rglob("SKILL.md")
            if path.parent.parent != SKILLS
        ]
        self.assertEqual([], nested)
        for skill_md in SKILLS.glob("*/SKILL.md"):
            self.assertLessEqual(
                len(skill_md.read_text(encoding="utf-8").splitlines()),
                500,
                skill_md,
            )

    def test_dora_uses_current_five_metric_model(self) -> None:
        content = (SKILLS / "dora-core" / "SKILL.md").read_text(encoding="utf-8")
        for metric in (
            "Change lead time",
            "Deployment frequency",
            "Failed deployment recovery time",
            "Change fail rate",
            "Deployment rework rate",
        ):
            self.assertIn(metric, content)
        self.assertNotIn("## The 4 Key Metrics", content)
        self.assertNotIn("973×", content)

    def test_audited_unsafe_or_stale_claims_do_not_regress(self) -> None:
        corpus = "\n".join(
            path.read_text(encoding="utf-8") for path in sorted(SKILLS.rglob("*.md"))
        )
        banned = (
            "useradd -m -s /bin/bash backdoor",
            "Store sensitive data in `chrome.storage.local` (encrypted at rest by OS)",
            "Ignore unranked venues unless citations > 100",
            "minimum 30 for metaheuristics",
            "publicationDateOrYear=2024:2025",
            "SOM should be ≥$10M",
        )
        for claim in banned:
            self.assertNotIn(claim, corpus)

    def test_archive_build_is_deterministic(self) -> None:
        skill = SKILLS / "dora-core"
        first = package_skills.archive_bytes(skill)
        second = package_skills.archive_bytes(skill)
        self.assertEqual(first, second)
        self.assertTrue(first.startswith(b"PK"))


if __name__ == "__main__":
    unittest.main()
