#!/usr/bin/env python3
"""
Skill router hook for kinhluan-skills.
Reads user prompt from stdin (Claude Code UserPromptSubmit hook format),
matches intent to relevant kinhluan skills, outputs hint to Claude.
"""
import sys
import json
import re

SKILL_ROUTES = [
    # Research pipeline
    {
        "skill": "kinhluan-skills:sota-survey",
        "keywords": ["survey", "literature", "papers", "related work", "state of the art", "sota",
                     "khảo sát", "tài liệu", "bài báo", "nghiên cứu liên quan"],
    },
    {
        "skill": "kinhluan-skills:research-question",
        "keywords": ["research question", "hypothesis", "rq1", "rq2", "contribution", "novelty",
                     "câu hỏi nghiên cứu", "đóng góp", "giả thuyết"],
    },
    {
        "skill": "kinhluan-skills:research-design",
        "keywords": ["experiment design", "methodology", "baseline", "ablation", "evaluation plan",
                     "thiết kế thực nghiệm", "phương pháp", "baseline"],
    },
    {
        "skill": "kinhluan-skills:paper-writing",
        "keywords": ["write paper", "thesis chapter", "abstract", "introduction section", "latex",
                     "viết bài", "chương luận văn", "abstract", "introduction"],
    },
    {
        "skill": "kinhluan-skills:defense-prep",
        "keywords": ["defense", "thesis defense", "committee", "oral exam", "bảo vệ", "hội đồng",
                     "phản biện", "bảo vệ luận văn"],
    },
    {
        "skill": "kinhluan-skills:phd-proposal",
        "keywords": ["proposal", "research proposal", "phd proposal", "đề xuất nghiên cứu",
                     "đề cương", "proposal"],
    },
    {
        "skill": "kinhluan-skills:experiment-tracking",
        "keywords": ["track experiment", "log results", "compare runs", "results table",
                     "theo dõi thí nghiệm", "kết quả thực nghiệm"],
    },
    {
        "skill": "kinhluan-skills:internal-critique",
        "keywords": ["self review", "review paper", "reviewer feedback", "pre-submission",
                     "tự đánh giá", "review bài", "phản biện"],
    },
    {
        "skill": "kinhluan-skills:milestone-tracker",
        "keywords": ["milestone", "deadline", "schedule phd", "timeline", "progress check",
                     "tiến độ", "deadline", "lịch trình"],
    },
    # Architecture
    {
        "skill": "kinhluan-skills:c4-model",
        "keywords": ["c4", "architecture diagram", "system diagram", "c4 model",
                     "sơ đồ kiến trúc", "kiến trúc hệ thống"],
    },
    {
        "skill": "kinhluan-skills:c4-level1-context",
        "keywords": ["context diagram", "system context", "level 1", "c4 level 1",
                     "sơ đồ ngữ cảnh", "c4 level1"],
    },
    {
        "skill": "kinhluan-skills:c4-level2-container",
        "keywords": ["container diagram", "level 2", "c4 level 2", "services diagram",
                     "sơ đồ container", "c4 level2"],
    },
    {
        "skill": "kinhluan-skills:c4-level3-component",
        "keywords": ["component diagram", "level 3", "c4 level 3", "internal components",
                     "sơ đồ component", "c4 level3"],
    },
    {
        "skill": "kinhluan-skills:c4-level4-code",
        "keywords": ["class diagram", "er diagram", "level 4", "c4 level 4", "uml",
                     "sơ đồ lớp", "c4 level4"],
    },
    # DDD
    {
        "skill": "kinhluan-skills:ddd-core",
        "keywords": ["ddd", "domain driven", "bounded context", "ubiquitous language",
                     "strategic ddd", "domain model", "domain-driven"],
    },
    {
        "skill": "kinhluan-skills:ddd-tactical",
        "keywords": ["aggregate", "entity", "value object", "repository pattern", "domain service",
                     "tactical ddd", "domain event"],
    },
    {
        "skill": "kinhluan-skills:ddd-patterns",
        "keywords": ["saga", "cqrs", "event sourcing", "anti-corruption layer", "acl",
                     "integration pattern", "ddd integration"],
    },
    # DevOps
    {
        "skill": "kinhluan-skills:docker-containerization",
        "keywords": ["docker", "dockerfile", "container", "docker-compose", "image build",
                     "containerize"],
    },
    {
        "skill": "kinhluan-skills:kubernetes-orchestration",
        "keywords": ["kubernetes", "k8s", "pod", "deployment yaml", "helm", "ingress", "kubectl"],
    },
    {
        "skill": "kinhluan-skills:dora-core",
        "keywords": ["dora", "deployment frequency", "lead time", "change failure rate", "mttr",
                     "devops metrics", "delivery performance"],
    },
    # ML/Research specific
    {
        "skill": "kinhluan-skills:federated-learning-dqn",
        "keywords": ["federated learning", "dqn", "deep q-network", "fl", "privacy preserving",
                     "học liên kết", "học tăng cường"],
    },
    {
        "skill": "kinhluan-skills:scheduling-algorithms",
        "keywords": ["scheduling", "mlfq", "queue", "job scheduling", "multilevel feedback",
                     "lập lịch", "thuật toán lập lịch"],
    },
    # Strategy/Business
    {
        "skill": "kinhluan-skills:business-product-leadership",
        "keywords": ["jtbd", "jobs to be done", "product market", "mvp", "product strategy",
                     "user story", "chiến lược sản phẩm"],
    },
    {
        "skill": "kinhluan-skills:why-strategic-rationale",
        "keywords": ["why build", "value proposition", "working backwards", "pr/faq", "rationale",
                     "tại sao xây dựng", "giá trị"],
    },
    {
        "skill": "kinhluan-skills:problem-discovery",
        "keywords": ["validate problem", "is there demand", "problem exists", "user interviews",
                     "xác nhận vấn đề", "có nhu cầu không"],
    },
    {
        "skill": "kinhluan-skills:diffusion-release-tracking",
        "keywords": ["diffusion", "rogers", "innovators", "early adopters", "chasm", "release tracking",
                     "lan truyền", "adoption"],
    },
    {
        "skill": "kinhluan-skills:art-of-war-software-engineering",
        "keywords": ["art of war", "competitive", "strategy", "sun tzu", "resource allocation",
                     "timing right", "binh pháp", "chiến lược"],
    },
    {
        "skill": "kinhluan-skills:dora-core",
        "keywords": ["four keys", "elite performer", "delivery metrics"],
    },
    # Writing/Language
    {
        "skill": "kinhluan-skills:vietnamese-cs-terminology",
        "keywords": ["dịch thuật ngữ", "tiếng việt cs", "thuật ngữ it", "vietnamese terminology",
                     "dịch sang tiếng việt"],
    },
    {
        "skill": "kinhluan-skills:technical-english-cs",
        "keywords": ["technical english", "academic writing", "ieee style", "acm style",
                     "viết tiếng anh", "academic english"],
    },
    {
        "skill": "kinhluan-skills:vietnamese-writing-standard",
        "keywords": ["chính tả", "dấu câu tiếng việt", "viết chuẩn", "vietnamese writing",
                     "lỗi chính tả"],
    },
    # Dev
    {
        "skill": "kinhluan-skills:python-development",
        "keywords": ["python", "fastapi", "pydantic", "uv project", "ruff", "pytest",
                     "sqlalchemy", "async python"],
    },
    {
        "skill": "kinhluan-skills:javascript-typescript",
        "keywords": ["typescript", "javascript", "react", "node.js", "ts types", "jest", "vitest"],
    },
    {
        "skill": "kinhluan-skills:security-analysis",
        "keywords": ["security", "vulnerability", "owasp", "pentest", "sql injection", "xss",
                     "bảo mật", "lỗ hổng"],
    },
    # Meta/Architecture patterns
    {
        "skill": "kinhluan-skills:architecture-decision-records",
        "keywords": ["adr", "architecture decision", "madr", "decision record",
                     "quyết định kiến trúc"],
    },
    {
        "skill": "kinhluan-skills:evolutionary-architecture",
        "keywords": ["fitness function", "strangler fig", "incremental change", "architecture testing",
                     "kiến trúc tiến hóa"],
    },
    {
        "skill": "kinhluan-skills:collaborative-engineering-agent",
        "keywords": ["sdlc", "gitops", "secops", "dialectica", "agentic project"],
    },
    {
        "skill": "kinhluan-skills:publication-strategy",
        "keywords": ["publication venue", "submit paper", "rebuttal", "conference", "journal",
                     "nộp bài báo", "venue", "rebuttal"],
    },
    {
        "skill": "kinhluan-skills:second-brain-reflection",
        "keywords": ["second brain", "knowledge management", "lessons learned", "compress knowledge",
                     "note taking", "pkm"],
    },
    {
        "skill": "kinhluan-skills:research-workspace-standard",
        "keywords": ["research workspace", "directory structure", "agentic research", "artifact management"],
    },
]


def match_skills(prompt: str) -> list[str]:
    prompt_lower = prompt.lower()
    matched = []
    seen = set()
    for route in SKILL_ROUTES:
        for kw in route["keywords"]:
            if kw in prompt_lower and route["skill"] not in seen:
                matched.append(route["skill"])
                seen.add(route["skill"])
                break
    return matched[:3]  # Max 3 suggestions to avoid noise


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
        prompt = data.get("prompt", "") or data.get("message", "") or raw
    except (json.JSONDecodeError, Exception):
        prompt = sys.stdin.read() if not raw else raw

    if not prompt:
        sys.exit(0)

    matched = match_skills(str(prompt))
    if matched:
        skills_hint = ", ".join(matched)
        print(f"[skill-router] Relevant kinhluan-skills detected: {skills_hint}")
        if len(matched) > 1:
            print(f"[skill-router] Invoke the most specific one via Skill tool.")


if __name__ == "__main__":
    main()
