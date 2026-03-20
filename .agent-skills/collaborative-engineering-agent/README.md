# 🤝 Collaborative Engineering Agent (CEA)

CEA is a unified framework designed to transform a general-purpose AI agent into a **Senior Software Engineer** and **Project Manager**. It bridges the gap between writing code and managing a professional software development lifecycle (SDLC).

## 🚀 Core Components

### 1. Agentic Project Management (PM)
CEA manages the repository's health using a **Markdown-based Kanban** system and GitHub's native Issue/PR tracking.
- **Kanban Flow:** `BACKLOG` → `IN-PROGRESS` → `REVIEW` → `FIXING` → `DONE`.
- **Standardized Labeling:** Integrated patterns from `DmitriyBaklikov`, `alphaolomi`, and `Graphite` for advanced filtering.

### 2. GitOps & SecOps
Security and Infrastructure are treated as first-class citizens.
- **Pre-commit Audits:** Mandatory checks for secrets and vulnerabilities.
- **Automated Fixes:** AI-driven PRs for CI security failures.
- **Infrastructure Tracking:** Dedicated labeling for CI/CD, Docker, and K8s changes.

### 3. Dialectical Review Engine (DRE)
The heart of CEA's quality control. It enforces a **"Critique-Fix-Verify"** loop:
- **Phase A (Analysis):** Deep architectural insight.
- **Phase B (Pushback):** Mandatory "Devil's Advocate" feedback (Min 2 points).
- **Phase C (Fix):** Applying changes with technical rationale.
- **Phase D (Verify):** Re-review and regression testing.

## 📂 Directory Structure

```text
.agent-skills/collaborative-engineering-agent/
├── SKILL.md                # Detailed instructions & workflows
├── SKILL.toon              # Condensed version for context efficiency
├── README.md               # This overview
└── references/             # Standardized templates
    ├── kanban-template.md  # Markdown Kanban board
    ├── pr-template.md      # Graphite/Gitmore style PR description
    ├── bug-report-template.md # Structured bug reporting
    ├── review-checklist.md  # DRE criteria
    ├── labeling-standards.md # Unified labeling guide
    └── downstream-impact-checklist.md # API & microservices stability
```

## 🛠 Usage

### For the AI Agent
To activate this skill, use triggers like:
- *"Review this code and provide pushback."*
- *"Start a new feature and initialize the Kanban board."*
- *"Audit the security of this PR."*

### For Developers
- **Check the References:** Use the templates in `references/` to maintain consistency across the team.
- **Follow the DRE:** When the agent provides a "Pushback," treat it as a technical debate to reach the best architectural decision.

## 📜 Standards Integration
CEA synthesizes industry-leading practices from:
- **DmitriyBaklikov & alphaolomi:** For robust GitHub labeling.
- **Graphite:** For high-context PR descriptions.
- **Gitmore.io:** For self-review checklists and impact assessment.
