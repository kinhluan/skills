#!/usr/bin/env python3
"""Suggest the most relevant kinhluan skills for a user prompt."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from dataclasses import dataclass


NAMESPACE = "kinhluan-skills"
MAX_SUGGESTIONS = 3


@dataclass(frozen=True)
class Route:
    skill: str
    keywords: tuple[str, ...]
    priority: int = 0


def route(skill: str, *keywords: str, priority: int = 0) -> Route:
    return Route(skill=skill, keywords=keywords, priority=priority)


SKILL_ROUTES = [
    route(
        "agent-expertise-protocol",
        "agent governance",
        "expertise protocol",
        "user sovereignty",
        "agent escalation",
    ),
    route(
        "ai-figure-generation",
        "scientific figure",
        "research figure",
        "paper illustration",
        "ai figure",
        "hình minh họa khoa học",
        priority=3,
    ),
    route(
        "api-security",
        "api security",
        "owasp api",
        "graphql security",
        "oauth security",
        "api authentication",
        priority=4,
    ),
    route(
        "architecture-decision-records",
        "architecture decision record",
        "decision record",
        "madr",
        "adr",
        "quyết định kiến trúc",
        priority=3,
    ),
    route(
        "art-of-war-software-engineering",
        "should we build",
        "should we invest",
        "is the timing right",
        "resource allocation",
        "competitive strategy",
        "art of war",
        "sun tzu",
        "binh pháp",
        priority=2,
    ),
    route(
        "browser-automation",
        "browser automation",
        "playwright",
        "puppeteer",
        "chrome extension",
        "web scraping",
        "content script",
        "manifest v3",
        "tự động hóa trình duyệt",
        "cào dữ liệu web",
        priority=2,
    ),
    route(
        "business-product-leadership",
        "jobs to be done",
        "product strategy",
        "product market",
        "product leadership",
        "jtbd",
        "mvp",
        "chiến lược sản phẩm",
    ),
    route(
        "c4-level1-context",
        "system context diagram",
        "c4 level 1",
        "c4 level1",
        "context diagram",
        "sơ đồ ngữ cảnh",
        priority=5,
    ),
    route(
        "c4-level2-container",
        "c4 container diagram",
        "c4 level 2",
        "c4 level2",
        "container diagram",
        "sơ đồ container",
        priority=5,
    ),
    route(
        "c4-level3-component",
        "c4 component diagram",
        "c4 level 3",
        "c4 level3",
        "component diagram",
        "sơ đồ component",
        priority=5,
    ),
    route(
        "c4-level4-code",
        "c4 code diagram",
        "c4 level 4",
        "c4 level4",
        "class diagram",
        "er diagram",
        "uml",
        priority=5,
    ),
    route(
        "c4-model",
        "c4 model",
        "architecture diagram",
        "system diagram",
        "sơ đồ kiến trúc",
    ),
    route(
        "clean-architecture",
        "clean architecture",
        "dependency rule",
        "ports and adapters",
        "use case layer",
        "hexagonal architecture",
        priority=3,
    ),
    route(
        "cloud-security",
        "cloud security",
        "aws security",
        "azure security",
        "gcp security",
        "iam policy",
        "bucket security",
        priority=4,
    ),
    route(
        "code-quality-gate",
        "quality gate",
        "sonarqube",
        "sonarcloud",
        "static analysis",
        "lint failure",
        "coverage gate",
        priority=4,
    ),
    route(
        "collaborative-engineering-agent",
        "engineering workflow",
        "agentic project management",
        "sdlc workflow",
        "gitops secops",
        "collaborative engineering",
    ),
    route(
        "conference-paper",
        "conference paper",
        "poster abstract",
        "conference poster",
        "bài báo hội nghị",
        priority=3,
    ),
    route(
        "container-security",
        "kubernetes container security",
        "docker container security",
        "container security",
        "kubernetes security",
        "pod security",
        "image scanning",
        "trivy",
        "falco",
        priority=6,
    ),
    route(
        "ddd-core",
        "strategic ddd",
        "bounded context",
        "ubiquitous language",
        "event storming",
        "domain driven design",
        "domain-driven design",
    ),
    route(
        "ddd-patterns",
        "ddd integration",
        "event sourcing",
        "anti-corruption layer",
        "transactional outbox",
        "cqrs",
        "saga",
        priority=4,
    ),
    route(
        "ddd-tactical",
        "tactical ddd",
        "domain aggregate",
        "value object",
        "domain event",
        "domain service",
        "aggregate",
        priority=3,
    ),
    route(
        "defense-prep",
        "thesis defense",
        "doctoral defense",
        "defense questions",
        "bảo vệ luận văn",
        "hội đồng bảo vệ",
        priority=3,
    ),
    route(
        "diffusion-release-tracking",
        "diffusion of innovations",
        "release adoption",
        "early adopters",
        "rogers diffusion",
        "adoption curve",
        "crossing the chasm",
        priority=2,
    ),
    route(
        "docker-containerization",
        "dockerfile",
        "docker compose",
        "containerize",
        "docker image",
        "docker",
    ),
    route(
        "dora-core",
        "dora metrics",
        "deployment frequency",
        "change lead time",
        "change fail rate",
        "deployment rework rate",
        "failed deployment recovery time",
        "delivery performance",
        priority=3,
    ),
    route(
        "evolutionary-architecture",
        "evolutionary architecture",
        "architecture fitness function",
        "strangler fig",
        "incremental architecture",
    ),
    route(
        "experiment-tracking",
        "track experiments",
        "experiment log",
        "compare runs",
        "reproduce experiment",
        "theo dõi thí nghiệm",
    ),
    route(
        "federated-learning-dqn",
        "federated dqn",
        "federated reinforcement learning",
        "deep q-network",
        "federated learning",
        "học liên kết",
        priority=4,
    ),
    route(
        "git-workflow",
        "git workflow",
        "branching strategy",
        "trunk based development",
        "gitflow",
        "branch naming",
        "commit convention",
        "release tag",
    ),
    route(
        "golang-development",
        "go concurrency",
        "go module",
        "golang",
        "gofmt",
        "go",
        priority=2,
    ),
    route(
        "internal-critique",
        "self review paper",
        "pre-submission review",
        "critique my paper",
        "tự đánh giá bài báo",
        "reviewer simulation",
    ),
    route(
        "javascript-typescript",
        "typescript",
        "javascript",
        "node.js",
        "nodejs",
        "vitest",
        "jest",
    ),
    route(
        "journal-q1-polish",
        "q1 journal",
        "journal polish",
        "q1 polish",
        "scopus journal",
        "isi journal",
        "polish manuscript",
        priority=3,
    ),
    route(
        "kinhluan-router",
        "choose the right skill",
        "use the right skill",
        "route this task",
        "dùng skill phù hợp",
        "chọn skill",
        priority=5,
    ),
    route(
        "kubernetes-orchestration",
        "kubernetes",
        "helm chart",
        "deployment yaml",
        "kubectl",
        "k8s",
    ),
    route(
        "merge-request-review",
        "review this pull request",
        "review this merge request",
        "review this pr",
        "review this mr",
        "pr review",
        "mr review",
        priority=4,
    ),
    route(
        "milestone-tracker",
        "research milestone",
        "phd timeline",
        "committee deadline",
        "track milestone",
        "tiến độ nghiên cứu",
    ),
    route(
        "paper-audit",
        "audit paper against code",
        "paper code audit",
        "verify paper claims",
        "compare paper and repository",
        "đối chiếu bài báo và mã",
        priority=5,
    ),
    route(
        "paper-writing",
        "write research paper",
        "write paper",
        "paper section",
        "latex paper",
        "viết bài báo",
    ),
    route(
        "penetration-testing",
        "authorized penetration test",
        "penetration testing",
        "pentest scope",
        "burp suite",
        "nmap assessment",
        "kiểm thử xâm nhập",
        priority=4,
    ),
    route(
        "phd-proposal",
        "phd proposal",
        "research proposal",
        "doctoral proposal",
        "đề cương nghiên cứu",
        "đề xuất nghiên cứu",
    ),
    route(
        "problem-discovery",
        "validate the problem",
        "should we build this product",
        "problem interview",
        "is there demand",
        "problem discovery",
        "xác nhận vấn đề",
        priority=2,
    ),
    route(
        "product-analytics",
        "product analytics",
        "funnel analysis",
        "cohort analysis",
        "north star metric",
        "a/b test",
        "product metrics",
        priority=2,
    ),
    route(
        "product-ux-research",
        "ux research",
        "usability test",
        "user persona",
        "journey map",
        "user interview guide",
        "nghiên cứu người dùng",
        priority=2,
    ),
    route(
        "progress-report",
        "research progress report",
        "advisor progress",
        "monthly research report",
        "báo cáo tiến độ",
    ),
    route(
        "proposal-defense",
        "proposal defense",
        "defend proposal",
        "proposal presentation",
        "bảo vệ đề cương",
        priority=4,
    ),
    route(
        "publication-strategy",
        "publication strategy",
        "choose a venue",
        "conference deadline",
        "journal submission",
        "paper rebuttal",
        "nộp bài báo",
    ),
    route(
        "python-development",
        "python",
        "fastapi",
        "pydantic",
        "pytest",
        "ruff",
        "sqlalchemy",
    ),
    route(
        "research-design",
        "research methodology",
        "experiment design",
        "ablation plan",
        "evaluation protocol",
        "thiết kế thực nghiệm",
        priority=2,
    ),
    route(
        "research-question",
        "research question",
        "research hypothesis",
        "contribution statement",
        "câu hỏi nghiên cứu",
        "giả thuyết nghiên cứu",
        priority=2,
    ),
    route(
        "research-watch",
        "monitor new papers",
        "research watch",
        "weekly paper alert",
        "literature alert",
        "track new publications",
        "theo dõi bài báo mới",
        priority=5,
    ),
    route(
        "research-workspace-standard",
        "research workspace",
        "research directory structure",
        "research artifact management",
        "experiment folders",
    ),
    route(
        "scheduling-algorithms",
        "job scheduling algorithm",
        "scheduling algorithm",
        "multilevel feedback queue",
        "mlfq",
        "lập lịch",
    ),
    route(
        "second-brain-reflection",
        "second brain",
        "knowledge reflection",
        "lessons learned",
        "knowledge compression",
        "personal knowledge management",
        "pkm",
    ),
    route(
        "security-analysis",
        "security audit",
        "vulnerability analysis",
        "security review",
        "owasp",
        "vulnerability",
        "bảo mật",
    ),
    route(
        "slide-automation",
        "automate slides",
        "generate slides",
        "research slides",
        "presentation deck",
        "slide automation",
        "tạo slide",
        priority=3,
    ),
    route(
        "sota-survey",
        "state of the art survey",
        "literature survey",
        "systematic literature review",
        "related work survey",
        "sota",
        "khảo sát tài liệu",
    ),
    route(
        "technical-english-cs",
        "technical english",
        "academic english",
        "computer science english",
        "ieee writing style",
        "viết tiếng anh học thuật",
    ),
    route(
        "technical-report",
        "technical report",
        "system report",
        "experiment report",
        "engineering report",
        "báo cáo kỹ thuật",
    ),
    route(
        "thesis-writing",
        "write thesis",
        "thesis chapter",
        "doctoral dissertation",
        "master's thesis",
        "viết luận văn",
    ),
    route(
        "threat-modeling",
        "threat modeling",
        "threat model",
        "attack tree",
        "stride",
        "security design review",
        priority=4,
    ),
    route(
        "vietnamese-cs-terminology",
        "vietnamese cs terminology",
        "translate computer science terms",
        "dịch thuật ngữ",
        "thuật ngữ công nghệ thông tin",
    ),
    route(
        "vietnamese-writing-standard",
        "vietnamese writing",
        "vietnamese spelling",
        "chính tả tiếng việt",
        "dấu câu tiếng việt",
        "viết tiếng việt",
    ),
    route(
        "why-strategic-rationale",
        "why build this",
        "strategic rationale",
        "value proposition",
        "working backwards",
        "pr/faq",
        "tại sao xây dựng",
        priority=2,
    ),
]


def normalize(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def keyword_matches(prompt: str, keyword: str) -> bool:
    normalized_keyword = normalize(keyword)
    if not normalized_keyword:
        return False
    if re.fullmatch(r"[\w+-]+", normalized_keyword):
        pattern = rf"(?<![\w+-]){re.escape(normalized_keyword)}(?![\w+-])"
        return re.search(pattern, prompt) is not None
    return normalized_keyword in prompt


def route_score(prompt: str, candidate: Route) -> tuple[int, int]:
    matches = [
        normalize(keyword)
        for keyword in candidate.keywords
        if keyword_matches(prompt, keyword)
    ]
    if not matches:
        return (0, 0)
    phrase_score = sum(10 + 5 * keyword.count(" ") + min(len(keyword), 40) for keyword in matches)
    exact_bonus = 50 if prompt in matches else 0
    return (phrase_score + exact_bonus + candidate.priority, max(map(len, matches)))


def match_skills(prompt: str, limit: int = MAX_SUGGESTIONS) -> list[str]:
    normalized_prompt = normalize(prompt)
    if not normalized_prompt or limit <= 0:
        return []

    ranked: list[tuple[int, int, int, str]] = []
    for index, candidate in enumerate(SKILL_ROUTES):
        score, specificity = route_score(normalized_prompt, candidate)
        if score:
            ranked.append((score, specificity, -index, candidate.skill))
    ranked.sort(reverse=True)
    return [skill for _, _, _, skill in ranked[:limit]]


def route_names() -> list[str]:
    return [candidate.skill for candidate in SKILL_ROUTES]


def prompt_from_input(raw: str) -> str:
    if not raw.strip():
        return ""
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return raw
    if not isinstance(payload, dict):
        return str(payload)
    for key in ("prompt", "message"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return ""


def main() -> int:
    prompt = prompt_from_input(sys.stdin.read())
    matches = match_skills(prompt)
    if matches:
        qualified = ", ".join(f"{NAMESPACE}:{skill}" for skill in matches)
        print(f"[skill-router] Relevant skills, most specific first: {qualified}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
