---
name: c4-model
description: Professional C4 model architecture hub for "Design-to-Code Sync". Use this skill to navigate the C4 hierarchy, map diagrams to stakeholders, avoid architectural anti-patterns, and choose the right level for designing or documenting existing codebases.
metadata:
---

# C4 Model: Design-to-Code Sync Hub

The C4 model is a hierarchical approach to describing software architecture. This skill set focuses on **Design-to-Code Sync**: ensuring your diagrams reflect actual code reality and your code follows intended design.

## 🎯 Stakeholder Mapping

| Level | Name | Audience | Focus |
| :--- | :--- | :--- | :--- |
| **L1** | **System Context** | Executives, PMs, Users, Devs | Business value, User Journeys, Scope |
| **L2** | **Container** | Architects, Developers, Ops | Tech Stack, Deployable units, API boundaries |
| **L3** | **Component** | Developers, Architects | Internal logic, Layering, Code structure |
| **L4** | **Code** | Developers | Implementation details, ERDs, Class diagrams |

## 🚫 Architectural Anti-Patterns (The "Don'ts")

... (unchanged) ...

## 📦 Standard Artifacts

Every C4 modeling session should produce the following artifacts to ensure persistence and visibility:

1.  **Architecture Source (Mermaid):** Always save the Mermaid code in a `.mermaid` file inside `docs/architecture/`.
2.  **Architectural Decision Record (ADR):** For any major tech choice, create a simple Markdown file explaining the "Why".
3.  **Visual Preview (Claude):** When working in Claude, always wrap Mermaid code in ` ```mermaid ` blocks to trigger the Artifact preview window.

### Output Structure Recommendation:
```text
docs/architecture/
├── L1-system-context.mermaid
├── L2-containers.mermaid
└── architecture-decisions.md
```

## 🚀 Specialized Workflows

- **Context Level:** Use `c4-level1-context` to map business scope and user journeys.
- **Container Level:** Use `c4-level2-container` to define the tech stack and infrastructure (Docker/K8s).
- **Component Level:** Use `c4-level3-component` to bridge the gap between design and folder structure.
- **Code Level:** Use `c4-level4-code` for complex data models or critical logic.

## 🔍 Smart Synthesis (Design-to-Code)

When documenting an existing project, always **scan the codebase first**:
- Check `package.json`, `pom.xml`, `go.mod` to identify Containers (L2).
- Scan folder structures (e.g., `src/services`, `internal/`) to identify Components (L3).
- Look for `Dockerfile` or `docker-compose.yml` to verify Deployment mapping.
