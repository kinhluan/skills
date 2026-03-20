# Collaborative Engineering Agent (CEA) Framework

The **Collaborative Engineering Agent (CEA)** is a unified framework designed to bridge the gap between AI code generation and professional software engineering practices. It transforms a general-purpose AI agent into a Senior Software Engineer, Architect, and Project Manager through a structured, dialectical, and secure development lifecycle.

---

## 🏗 Framework Architecture

CEA is built upon four foundational pillars:

### 1. Dialectical Review Engine (DRE)
The heart of CEA is the **Critique-Fix-Verify** loop. Unlike standard code generation, CEA mandates a "pushback" phase where the agent must act as its own critic (Devil's Advocate) before finalizing any implementation.

*   **Phase A: Analysis:** Deep intent mapping and architectural alignment.
*   **Phase B: Pushback:** Identifying edge cases, performance bottlenecks, and technical debt.
*   **Phase C: Fix:** Applying changes with a documented technical rationale ("The Why").
*   **Phase D: Verify:** Regression testing and re-review against initial critiques.

### 2. Multi-Agent Identity & Protocol (IACP)
CEA standardizes how multiple agents interact within a project by defining explicit roles and a communication handshake.

*   **Roles:** `Architect`, `Developer`, `Security Auditor`, `Product Owner`, `Reviewer`.
*   **Handshake:** Agents must declare their identity and objective before contributing to a thread.
*   **Conflict Resolution:** Defined arbitration paths (e.g., Security Auditor has the final say on safety vs. speed).

### 3. Agentic Project Management (PM)
CEA manages the "meta-data" of development directly within the repository.
*   **Markdown Kanban:** Tracking tasks through `docs/kanban/*.md` files (States: `BACKLOG`, `IN-PROGRESS`, `REVIEW`, `FIXING`, `DONE`).
*   **Unified Labeling:** A consolidated labeling strategy combining `DmitriyBaklikov` (Status/Type) and `alphaolomi` (Milestone/Environment) patterns.

### 4. GitOps & SecOps
CEA treats security and infrastructure as core requirements, not afterthoughts.
*   **Pre-commit Audits:** Automated secret detection and vulnerability scanning.
*   **Impact Assessment:** Mandatory checklists for downstream service stability and API breaking changes.

---

## 📂 Standard Artifacts & Templates

CEA provides standardized templates in `.agent-skills/collaborative-engineering-agent/references/`:

| Artifact | Purpose | Standard Source |
| :--- | :--- | :--- |
| `pr-template.md` | High-context PR descriptions with test plans and DRE summaries. | Graphite & Gitmore |
| `kanban-template.md`| Markdown-based task tracking for agents. | Custom CEA |
| `labeling-standards.md`| Unified GitHub label hierarchy. | DmitriyBaklikov & alphaolomi |
| `review-checklist.md`| DRE criteria for architecture, security, and performance. | Google Eng-Practices |
| `bug-report-template.md`| Structured reports for consistent reproduction. | Industry Standard |
| `downstream-impact.md`| API contract and microservice stability checks. | Gitmore |
| `agent-interaction.md`| Multi-agent role and communication guide. | Custom CEA |

---

## 🛠 Usage & Integration

### Activation Triggers
Agents activate CEA when they encounter prompts such as:
- *"Initialize a new feature using the CEA framework."*
- *"Perform a dialectical review of this PR."*
- *"Audit the security and downstream impact of these changes."*
- *"Declare your role as Architect and critique this proposal."*

### Developer Workflow
1.  **Plan:** Agent creates a Kanban file and breaks the feature into atomic tasks.
2.  **Code:** Agent implements the task, performing a self-audit for secrets.
3.  **Review:** Agent initiates the DRE, providing at least two critical pushbacks.
4.  **PR:** Agent generates a PR using the high-context template and relevant labels.

---

## 📜 Philosophy
CEA is built on the belief that **Great Code is the result of High-Quality Friction**. By forcing agents to justify their decisions and interact through defined roles, we reduce hallucinations and ensure that AI-generated software meets professional engineering standards.
