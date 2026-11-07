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

    def test_pasture_routes_for_parallel_agent_work(self) -> None:
        self.assert_routes("Start a pasture-task for this branch.", "pasture")
        self.assert_routes("Read the dev server pane with herdr.", "pasture")
        self.assert_routes("Run parallel agents on this repo.", "pasture")

    def test_tdd_routes_to_red_green_refactor(self) -> None:
        routes = skill_router.match_skills("Use TDD: write a failing test first.")
        self.assertEqual("tdd-red-green-refactor", routes[0])

    def test_pr_authoring_routes_to_merge_request_review(self) -> None:
        self.assert_routes(
            "Help me write a PR description and answer review comments.",
            "merge-request-review",
        )

    def test_architecture_drift_routes_to_architecture_review(self) -> None:
        routes = skill_router.match_skills("Check architecture drift: C4 vs code.")
        self.assertEqual("architecture-review", routes[0])

    def test_pedagogy_skills_are_routed(self) -> None:
        self.assertEqual(
            "socratic-teaching",
            skill_router.match_skills("Teach me recursion with Socratic questions.")[0],
        )
        self.assertEqual(
            "exam-rubric",
            skill_router.match_skills("Chấm bài này theo rubric.")[0],
        )

    def test_ai_and_dependency_security_route_to_security_analysis(self) -> None:
        self.assert_routes(
            "Review our agent for prompt injection and MCP security.",
            "security-analysis",
        )
        self.assert_routes("Triage this Dependabot alert.", "security-analysis")

    def test_computer_use_routes_to_agent_cli_skills(self) -> None:
        routes = skill_router.match_skills(
            "Open the website with agent-browser and debug the web page console errors."
        )
        self.assertEqual("agent-browser", routes[0], routes)
        self.assert_routes("Dogfood this web app and file a bug hunt report.", "agent-browser")
        self.assert_routes("Control Slack, an Electron app, over a remote debugging port.", "agent-browser")
        routes = skill_router.match_skills("Use agent-desktop to change System Settings.")
        self.assertEqual("agent-desktop", routes[0], routes)
        self.assert_routes("mở app Notes rồi dùng app để tạo ghi chú", "agent-desktop")
        self.assert_routes("Write a Playwright test.", "browser-automation")

    def test_security_depth_skills_are_routed(self) -> None:
        cases = {
            "Generate an SBOM and check which dependencies are end-of-life.": "dependency-management",
            "Plan the upgrade quarkus 3.20 to the latest LTS.": "dependency-management",
            "dò cve và nâng cấp thư viện cho service": "dependency-management",
            "Design a double-entry ledger with an idempotency key for payments.": "payment-systems",
            "thiết kế luồng thanh toán và đối soát": "payment-systems",
            "Review this database schema design and the isolation level.": "database-design",
            "thiết kế database cho cassandra": "database-design",
        }
        for prompt, skill in cases.items():
            with self.subTest(prompt=prompt):
                self.assertEqual(skill, skill_router.match_skills(prompt)[0])
        self.assert_routes("Check this Java code for deserialization and XXE.", "security-analysis")
        self.assert_routes("Roll out semgrep and gitleaks secret scanning.", "security-analysis")

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
