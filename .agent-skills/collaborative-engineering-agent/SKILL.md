---
name: collaborative-engineering-agent
description: Unified SDLC skill for Agentic Project Management, GitOps/SecOps, and Dialectical Review loops.
metadata:
  version: 1.0.0
  triggers:
    - "Manage project"
    - "Start a feature"
    - "Review code"
    - "Fix and re-review"
    - "Create PR/Issue"
    - "GitOps/SecOps automation"
    - "Refine this task"
---

# 🤝 Collaborative Engineering Agent (CEA)

The Collaborative Engineering Agent (CEA) is the engine that drives the **How** of modern software development. It transforms a general-purpose AI into a Senior Software Engineer and Project Manager.

## 📋 1. Agentic Project Management (PM)

CEA uses a **Markdown-based Kanban** system for tracking progress without external tools.

### Tasks & Issues
- **Task Breakdown:** Every feature request must be broken into atomic tasks (e.g., `docs/kanban/feature-x.md`).
- **Issue Creation:** Use `gh issue create` with specific labels (`bug`, `feat`, `sec`, `refactor`).
- **Labeling:** Always categorize issues and PRs correctly to enable filtering.

### Kanban States
- `BACKLOG`: Future work.
- `IN-PROGRESS`: Active development.
- `REVIEW`: Code is waiting for feedback/critique.
- `FIXING`: Addressing review feedback.
- `DONE`: Merged and verified.

## 🛡 2. GitOps & SecOps

Security and Infrastructure are not "afterthoughts"—they are part of every commit.

### Rules
- **Pre-commit Audit:** Before any commit, run a local security check (e.g., `grep` for secrets, `semgrep` if available).
- **GitOps PRs:** Infrastructure changes (Docker, K8s, Terraform) must be clearly labeled as `infrastructure`.
- **Automated Fixes:** If a CI security scan fails, the agent should automatically create a fix-branch and PR.

## 🔍 3. Dialectical Review Engine (DRE)

This is the core of the **"Critique-Fix-Verify"** loop.

### Phase A: Analysis & Insight
- Don't just check syntax. Look for **Trade-offs**, **Architecture Alignment**, and **Scalability**.
- *Output:* A summary of *what* the code does and *why* it was built this way.

### Phase B: Pushback & Critique (Devil's Advocate)
- **MANDATORY:** Always provide at least 2 critical pushbacks.
- *Examples:* "How does this handle N+1 queries?", "What if the third-party API is down?", "Is this DRY enough?".

### Phase C: Fix & Rationale
- Apply fixes based on the critique.
- **Explain the "Why":** *"I replaced the linear search with a Hash Map to reduce time complexity from O(n) to O(1) as discussed."*

### Phase D: Re-review & Verification
- Check the fix against the original critique.
- Run tests to ensure no regressions.
- *Final Step:* Summarize the delta between the original and the final version.

## 🚀 4. GitHub Mastery & Labeling Standards

CEA uses a standardized labeling strategy (inspired by DmitriyBaklikov & alphaolomi) and high-quality PR descriptions (following Graphite best practices).

### Label Categories
- **Milestones:** `[v1.0]`, `[v2.0]`, `[Sprint 5]`. (Formatted with square brackets, dull colors).
- **Status (Actionable):** `status:WIP`, `status:needs-review`, `status:in-review`, `status:fixing`, `status:done`, `status:blocked`.
- **Type (Indicator):** `type:feature`, `type:bug`, `type:security`, `type:refactor`, `type:infrastructure`, `type:breaking-change`, `type:docs`.
- **Management (Deployment):** `env:staging`, `env:production`, `env:qa-needed`.
- **Priority (Management):** `priority:high`, `priority:medium`, `priority:low`.
- **Context:** `context:frontend`, `context:backend`, `context:api`, `context:core`.

### Pull Request Standards (Graphite & Gitmore Best Practices)
- **Atomic PRs:** Keep PRs small (<200 lines).
- **Multi-Template Strategy:** CEA uses specialized templates in `.agent-skills/collaborative-engineering-agent/references/` (Bug vs Feature).
- **Labeling:** Every PR must have at least one **Status** and one **Type** label.
- **Structured Description:** Use the `references/pr-template.md` which enforces:
  - **The "What" and "Why":** Clear summary and context.
  - **Visual Evidence:** Mandatory screenshots/GIFs for UI changes.
  - **Verification:** Specific steps, environment setup, and automated test commands.
  - **Self-Review Checklist:** Confirmation of manual code audit and internal quality.
  - **Impact Assessment:** Explicit check for **Downstream Impact** or API breaking changes.
  - **Pushback Summary:** The outcome of the Dialectical Review.

## 🤖 5. Multi-Agent Collaboration & Identity

In a multi-agent environment, clarity of **Identity** and **Role** is mandatory to prevent overlap and ensure high-quality friction (dialectics).

### Agent Role Declaration
Every agent must declare its role at the start of a session or a major task.
- **Architect (Lead):** Focuses on system design, C4 diagrams, and long-term scalability.
- **Developer (Coder):** Focuses on implementation, DRY principles, and performance.
- **Security Auditor (SecOps):** Focuses on vulnerabilities, secret detection, and compliance.
- **Product Owner (PM):** Focuses on JTBD, user value, and Kanban updates.
- **Reviewer (The Critic):** Focuses on the Dialectical Review Engine (DRE) pushbacks.

### Inter-Agent Communication Protocol (IACP)
When agents with different roles interact, they follow the **Request-Critique-Resolve** loop:
1.  **Identity Handshake:** "I am acting as [Role]. My objective is [Goal]."
2.  **Structured Proposal:** Agent A proposes a solution with technical rationale.
3.  **Role-Based Critique:** Agent B provides feedback *from its specific role's perspective* (e.g., Security Agent ignores style but flags a missing `chmod`).
4.  **Conflict Resolution:** If agents disagree, they must present **Trade-offs** to the User (The Final Arbiter) or follow the Architect's decision.

### Cross-Role Dialectics
- **Dev vs. SecOps:** Dev wants speed; SecOps wants safety. *Resolution:* Automated security scans must pass before Dev can mark a task as DONE.
- **PM vs. Architect:** PM wants MVP; Architect wants a robust foundation. *Resolution:* Use the **Master Framework** to map JTBD to C4 L2 containers.

## 📊 DORA Alignment

CEA practices map directly to DORA metrics. Use `dora-core` skill to assess current tier and identify gaps:

| CEA Practice | DORA Metric Improved |
|---|---|
| Atomic PRs (<200 lines) | Lead Time ↓ — smaller changes integrate and deploy faster |
| Trunk-based dev / short-lived branches | Lead Time ↓, Deployment Frequency ↑ |
| Dialectical Review Engine (DRE) | Change Failure Rate ↓ — catches issues before merge |
| Automated fix-branch on CI failure | MTTR ↓ — structured recovery path reduces restore time |
| Pre-commit security audit | Change Failure Rate ↓ — shifts left on security |
| Observability labels (`env:production`) | MTTR ↓ — faster incident scoping |
