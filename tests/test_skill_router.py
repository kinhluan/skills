from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import skill_router  # noqa: E402


class SkillRouterTest(unittest.TestCase):
    def assert_routes(self, prompt: str, *expected: str) -> None:
        routes = skill_router.match_skills(prompt)
        for skill in expected:
            self.assertIn(skill, routes, routes)

    def test_build_decision_routes_to_strategy(self) -> None:
        self.assert_routes(
            "Should we build this product idea?",
            "art-of-war-software-engineering",
            "problem-discovery",
        )

    def test_specific_container_security_wins(self) -> None:
        routes = skill_router.match_skills(
            "Review our Kubernetes container security and pod policy."
        )
        self.assertEqual("container-security", routes[0])
        self.assertIn("kubernetes-orchestration", routes)

    def test_go_short_keyword_uses_word_boundaries(self) -> None:
        self.assert_routes("Help diagnose a Go concurrency leak.", "golang-development")
        self.assertNotIn(
            "golang-development",
            skill_router.match_skills("Our ongoing migration needs a review."),
        )

    def test_slides_and_figures_route_to_both_specific_skills(self) -> None:
        self.assert_routes(
            "Generate research slides and a scientific figure.",
            "slide-automation",
            "ai-figure-generation",
        )

    def test_paper_audit_is_not_generic_writing(self) -> None:
        routes = skill_router.match_skills(
            "Audit this paper against its code and verify paper claims."
        )
        self.assertEqual("paper-audit", routes[0])

    def test_research_watch_beats_generic_survey(self) -> None:
        routes = skill_router.match_skills(
            "Set up a weekly paper alert to monitor new papers."
        )
        self.assertEqual("research-watch", routes[0])

    def test_new_release_skills_are_routed(self) -> None:
        self.assert_routes("Review this PR.", "merge-request-review")
        self.assert_routes("The SonarQube quality gate failed.", "code-quality-gate")
        self.assert_routes("Choose a trunk based Git workflow.", "git-workflow")

    def test_hook_payload_parsing(self) -> None:
        raw = json.dumps({"prompt": "Use Playwright for browser automation."})
        self.assertEqual(
            "Use Playwright for browser automation.",
            skill_router.prompt_from_input(raw),
        )

    def test_empty_prompt_has_no_route(self) -> None:
        self.assertEqual([], skill_router.match_skills(""))


if __name__ == "__main__":
    unittest.main()
