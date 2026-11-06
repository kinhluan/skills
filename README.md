<div align="center">

# 🧭 The Art of Agent Skills

**`kinhluan-skills`** · **A portable library of 71 agent skills for software delivery, architecture, security, product leadership, and academic research.**

[![Validate](https://github.com/kinhluan/skills/actions/workflows/validate.yml/badge.svg)](https://github.com/kinhluan/skills/actions/workflows/validate.yml)
[![Skills](https://img.shields.io/badge/skills-71-6f42c1)](skills.json)
[![Agent Skills spec](https://img.shields.io/badge/spec-Agent%20Skills-0a7ea4)](https://agentskills.io/specification)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[🚀 Install](#-installation) · [📚 Catalog](#-skill-catalog) · [🛠️ Development](#️-development) · [📖 Fieldbook](#-fieldbook) · [🧱 Principles](#-design-principles)

</div>

---

The repository follows the [Agent Skills specification](https://agentskills.io/specification). You can use it as a **Claude Code plugin**, a **Gemini CLI extension**, or a source for any skills-compatible agent.

## ✨ Highlights

| | |
|---|---|
| 📈 **Delivery** | DORA assessment using all five current metrics |
| 🏛️ **Architecture** | C4 Levels 1–4 (container and deployment views kept separate), strategic and tactical DDD, Clean Architecture, ADRs |
| ⚙️ **Engineering** | Python, Go, and TypeScript, plus Docker, Kubernetes, TDD, quality gates, and merge-request review |
| 🛡️ **Security** | OWASP 2025, API, cloud, container, and LLM/agent security, plus authorized pentesting with explicit safety boundaries |
| 🎯 **Product** | Product discovery, analytics, UX research, adoption, and strategy |
| 🎓 **Research** | The full research workflow, from SOTA survey through publication to thesis defense |
| 🧭 **Routing** | A portable prompt router whose specificity ranking is covered by tests |

## 🚀 Installation

### 🤖 Claude Code

```text
/plugin marketplace add kinhluan/skills
/plugin install kinhluan-skills
/reload-plugins
```

Skills appear as `kinhluan-skills:<skill-name>`.

### ♊ Gemini CLI

```bash
gemini extensions install https://github.com/kinhluan/skills
```

### 🧩 Skills-compatible agents

```bash
npx skills add kinhluan/skills
```

## 📚 Skill Catalog

The groups below match the categories on the Fieldbook site. The full catalog is generated in [`skills.json`](skills.json).

<details>
<summary><b>🎓 Research & Scholarship</b> (21)</summary>

| Skill | Use it for |
|---|---|
| [`sota-survey`](skills/sota-survey/SKILL.md) | Rigorous state-of-the-art literature surveys |
| [`research-question`](skills/research-question/SKILL.md) | Research questions, hypotheses, and contribution statements |
| [`research-design`](skills/research-design/SKILL.md) | Experiment protocols, baselines, metrics, and ablations |
| [`research-watch`](skills/research-watch/SKILL.md) | Recurring watches on papers, authors, and venues |
| [`research-workspace-standard`](skills/research-workspace-standard/SKILL.md) | Directory and artifact standards for agentic research |
| [`experiment-tracking`](skills/experiment-tracking/SKILL.md) | Logging, comparing, and reproducing experiments |
| [`paper-writing`](skills/paper-writing/SKILL.md) | Structure and academic tone for papers and chapters |
| [`conference-paper`](skills/conference-paper/SKILL.md) | Short papers, posters, and oral presentations |
| [`journal-q1-polish`](skills/journal-q1-polish/SKILL.md) | Final polish before submitting to a Q1 journal |
| [`paper-audit`](skills/paper-audit/SKILL.md) | Checking a paper's claims against its public code |
| [`internal-critique`](skills/internal-critique/SKILL.md) | A tough simulated reviewer before you share a draft |
| [`publication-strategy`](skills/publication-strategy/SKILL.md) | Venue choice, submission plans, and rebuttals |
| [`technical-report`](skills/technical-report/SKILL.md) | Experiment, design, and internal research reports |
| [`progress-report`](skills/progress-report/SKILL.md) | Updates for advisors, committees, and funders |
| [`phd-proposal`](skills/phd-proposal/SKILL.md) | Writing or reviewing a research proposal |
| [`proposal-defense`](skills/proposal-defense/SKILL.md) | Proposal defense slides and committee Q&A |
| [`thesis-writing`](skills/thesis-writing/SKILL.md) | Full thesis chapter structure |
| [`defense-prep`](skills/defense-prep/SKILL.md) | Preparing for the final defense |
| [`milestone-tracker`](skills/milestone-tracker/SKILL.md) | PhD timeline, deadlines, and committee meetings |
| [`slide-automation`](skills/slide-automation/SKILL.md) | Reproducible decks built from papers and data |
| [`ai-figure-generation`](skills/ai-figure-generation/SKILL.md) | Scientific figures made with image models |

</details>

<details>
<summary><b>🏛️ Architecture & Domain</b> (12)</summary>

| Skill | Use it for |
|---|---|
| [`c4-model`](skills/c4-model/SKILL.md) | Hub for the C4 hierarchy and design-to-code sync |
| [`c4-level1-context`](skills/c4-level1-context/SKILL.md) | System context and user journeys |
| [`c4-level2-container`](skills/c4-level2-container/SKILL.md) | Deployable applications and data stores |
| [`c4-level3-component`](skills/c4-level3-component/SKILL.md) | Components mapped to code folders |
| [`c4-level4-code`](skills/c4-level4-code/SKILL.md) | UML class and ER diagrams |
| [`architecture-review`](skills/architecture-review/SKILL.md) | C4 vs. code, fitness functions, and architecture drift |
| [`architecture-decision-records`](skills/architecture-decision-records/SKILL.md) | ADRs in MADR 4.0.0 format |
| [`clean-architecture`](skills/clean-architecture/SKILL.md) | Keeping business policy independent of frameworks |
| [`evolutionary-architecture`](skills/evolutionary-architecture/SKILL.md) | Fitness functions and strangler fig migrations |
| [`ddd-core`](skills/ddd-core/SKILL.md) | Event Storming, subdomains, and bounded contexts |
| [`ddd-tactical`](skills/ddd-tactical/SKILL.md) | Aggregates, entities, and value objects |
| [`ddd-patterns`](skills/ddd-patterns/SKILL.md) | ACL, outbox/inbox, CQRS, and event sourcing |

</details>

<details>
<summary><b>⚙️ Engineering & Delivery</b> (16)</summary>

| Skill | Use it for |
|---|---|
| [`python-development`](skills/python-development/SKILL.md) | Typing, packaging, and testing modern Python |
| [`golang-development`](skills/golang-development/SKILL.md) | Idiomatic Go APIs, concurrency, and modules |
| [`javascript-typescript`](skills/javascript-typescript/SKILL.md) | JavaScript and TypeScript for browsers, Node.js, and frameworks |
| [`tdd-red-green-refactor`](skills/tdd-red-green-refactor/SKILL.md) | Test-first development in red-green-refactor cycles |
| [`code-quality-gate`](skills/code-quality-gate/SKILL.md) | Linters, type checks, coverage, and SAST gates |
| [`merge-request-review`](skills/merge-request-review/SKILL.md) | Reviewing a PR or MR, or preparing one for review |
| [`git-workflow`](skills/git-workflow/SKILL.md) | Trunk-based development, release branches, and naming |
| [`collaborative-engineering-agent`](skills/collaborative-engineering-agent/SKILL.md) | Taking a bounded change from intent through verification |
| [`pasture`](skills/pasture/SKILL.md) | Working alongside other agents in pasture: worktrees, stacks, herdr, shared rules |
| [`dora-core`](skills/dora-core/SKILL.md) | The five DORA delivery metrics |
| [`docker-containerization`](skills/docker-containerization/SKILL.md) | Multi-stage builds, health checks, and distroless images |
| [`kubernetes-orchestration`](skills/kubernetes-orchestration/SKILL.md) | Kubernetes deployment and orchestration |
| [`scheduling-algorithms`](skills/scheduling-algorithms/SKILL.md) | Scheduling for operating systems, clusters, and workflows |
| [`federated-learning-dqn`](skills/federated-learning-dqn/SKILL.md) | Federated learning combined with DQN |
| [`socratic-teaching`](skills/socratic-teaching/SKILL.md) | Teaching CS through Socratic questions |
| [`exam-rubric`](skills/exam-rubric/SKILL.md) | Grading CS work against an explicit rubric |

</details>

<details>
<summary><b>🎯 Product & Strategy</b> (7)</summary>

| Skill | Use it for |
|---|---|
| [`why-strategic-rationale`](skills/why-strategic-rationale/SKILL.md) | Strategic rationale before anything gets built |
| [`problem-discovery`](skills/problem-discovery/SKILL.md) | Checking that a problem is worth solving |
| [`business-product-leadership`](skills/business-product-leadership/SKILL.md) | JTBD, value propositions, MVPs, and go-to-market |
| [`product-analytics`](skills/product-analytics/SKILL.md) | Metrics, A/B tests, and funnels |
| [`product-ux-research`](skills/product-ux-research/SKILL.md) | Personas, journey maps, and usability testing |
| [`diffusion-release-tracking`](skills/diffusion-release-tracking/SKILL.md) | Phased rollouts based on Rogers' adoption curve |
| [`art-of-war-software-engineering`](skills/art-of-war-software-engineering/SKILL.md) | Evaluating an initiative with the five factors (Ngũ Sự) |

</details>

<details>
<summary><b>🛡️ Security & Resilience</b> (6)</summary>

| Skill | Use it for |
|---|---|
| [`security-analysis`](skills/security-analysis/SKILL.md) | Code, dependency, CI, and LLM/agent security against OWASP 2025 |
| [`threat-modeling`](skills/threat-modeling/SKILL.md) | STRIDE, attack trees, and risk assessment |
| [`api-security`](skills/api-security/SKILL.md) | REST, GraphQL, webhooks, and OAuth |
| [`cloud-security`](skills/cloud-security/SKILL.md) | IAM and hardening on AWS, GCP, and Azure |
| [`container-security`](skills/container-security/SKILL.md) | Images, runtimes, Kubernetes, and supply chain |
| [`penetration-testing`](skills/penetration-testing/SKILL.md) | Authorized, bounded, non-destructive pentests |

</details>

<details>
<summary><b>🤖 Agents & Automation</b> (5) · <b>🗣️ Language & Knowledge</b> (4)</summary>

| Skill | Use it for |
|---|---|
| [`kinhluan-router`](skills/kinhluan-router/SKILL.md) | Choosing the smallest set of skills that fits a task |
| [`agent-expertise-protocol`](skills/agent-expertise-protocol/SKILL.md) | Authority, uncertainty, and handoff rules for agents |
| [`agent-browser`](skills/agent-browser/SKILL.md) | Opening, exploring, dogfooding, and debugging websites and Electron apps |
| [`agent-desktop`](skills/agent-desktop/SKILL.md) | Launching, exploring, and debugging native desktop apps through the accessibility tree |
| [`browser-automation`](skills/browser-automation/SKILL.md) | Playwright, web extraction, and Manifest V3 extensions |
| [`technical-english-cs`](skills/technical-english-cs/SKILL.md) | Technical English in IEEE/ACM style |
| [`vietnamese-cs-terminology`](skills/vietnamese-cs-terminology/SKILL.md) | Academic Vietnamese terms for computer science |
| [`vietnamese-writing-standard`](skills/vietnamese-writing-standard/SKILL.md) | Vietnamese spelling, punctuation, and tone |
| [`second-brain-reflection`](skills/second-brain-reflection/SKILL.md) | Turning lessons into reusable rules |

</details>

## 🗂️ Repository Layout

```text
skills/              📦 canonical skill sources and platform discovery root
hooks/hooks.json     🪝 portable Claude plugin router hook
scripts/             🔧 validation, routing, manifest, and packaging tools
tests/               🧪 router and repository regression tests
site/                🌐 Astro source for the Fieldbook site
dist/                📀 committed deterministic .skill archives
skills.json          🧾 generated publication manifest
```

Each skill has a single authoritative `SKILL.md`. Supporting files sit in directly linked folders:

- 📄 `references/`: detailed material
- 🔧 `scripts/`: deterministic helpers
- 🎨 `assets/`: output templates and other assets

The repository deliberately keeps no second, condensed copy of any skill.

## 🛠️ Development

Install the validation dependency:

```bash
python3 -m pip install -r requirements-dev.txt
```

Then use:

```bash
make sync-manifest  # regenerate skills.json from skills/
make validate       # validate metadata, links, routes, and release config
make test           # run router regression tests
make package        # rebuild deterministic dist/*.skill archives
make check          # validate + test + verify committed archives
```

> [!IMPORTANT]
> CI runs `make check`. The release version must be identical in `skills.json`, the Claude plugin metadata, the marketplace entry, and `gemini-extension.json`.

## 📖 Fieldbook

`site/` holds a source-driven Astro site that presents the library as the **Kinhluan Fieldbook**. It includes:

- 🧭 Ngũ Sự (the five factors) as a strategic lens
- 🔥 Active pursuits
- 🛤️ Outcome-oriented learning paths
- 📄 A full page for every skill
- 🔎 Client-side catalog search

```bash
make site-install
make site-dev
make site-check
```

Skill pages are generated directly from `skills.json` and `skills/*/SKILL.md`, so never maintain a second copy of skill content in the site.

> [!NOTE]
> After changes reach `main`, the `Deploy Fieldbook` workflow publishes the static build to GitHub Pages. A maintainer must first set the Pages source to **GitHub Actions** in the repository settings; this is a one-time step.

## 🧱 Design Principles

- 📏 Keep `SKILL.md` under 500 lines and use progressive disclosure.
- 🎯 Put the triggering context in `description`.
- 📚 Prefer current primary documentation for any time-sensitive claim.
- ⚖️ Treat thresholds as calibrated decisions, not universal laws.
- 🔐 Keep local implementation authority separate from external or consequential actions.
- ✅ Validate generated manifests and archives instead of editing them by hand.

## 📄 License

Released under the [MIT License](LICENSE) · © 2026 Luân B.

---

<div align="center">
<sub>🧭 Built for agents that know their terrain — ☯️ Đạo · 🌤️ Thiên · ⛰️ Địa · 🎖️ Tướng · ⚙️ Pháp</sub>
</div>
