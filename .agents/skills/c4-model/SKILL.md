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

1.  **The "Spaghetti" Diagram:** Drawing more than 20 elements in one diagram. *Solution: Break into multiple views.*
2.  **Tech Leakage in L1:** Mentioning "React" or "PostgreSQL" in System Context. *Solution: Focus on the "What", not "How".*
3.  **Missing Descriptions:** Boxes with only names. *Solution: Every box needs a one-sentence responsibility description.*
4.  **Ambiguous Arrows:** Labels like "Uses", "Sends", "Connects". *Solution: Use action verbs like "Authenticates user via", "Publishes order event to".*
5.  **Phantom Containers:** Modeling a shared library as a container. *Solution: Libraries are components (L3), not containers (L2) unless they run independently.*

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
