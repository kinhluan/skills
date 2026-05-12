---
name: c4-model
description: Professional C4 model architecture hub for "Design-to-Code Sync". Use this skill to navigate the C4 hierarchy, map diagrams to stakeholders, avoid architectural anti-patterns, and choose the right level for designing or documenting existing codebases.
metadata:
  tags: ["architecture", "c4-model", "design", "documentation", "structurizr"]
---

# C4 Model: Design-to-Code Sync Hub

The C4 model, created by Simon Brown, is a hierarchical approach to describing software architecture through four levels of abstraction. This skill focuses on **Design-to-Code Sync**: ensuring diagrams reflect actual code reality and code follows intended design.

> "The C4 model is a simple way to bring consistency to how you and your team describe and diagram software architecture." — Simon Brown

---

## 🎯 The 4-Level Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│  L1: SYSTEM CONTEXT                                         │
│  "Who uses the system and what external things does it      │
│   interact with?"                                           │
│  Audience: Executives, PMs, non-technical stakeholders      │
│  Scope: People + Systems (internal & external)              │
├─────────────────────────────────────────────────────────────┤
│  L2: CONTAINERS                                             │
│  "What are the high-level technology building blocks?"      │
│  Audience: Architects, developers, ops                      │
│  Scope: Apps, databases, message brokers, file systems      │
├─────────────────────────────────────────────────────────────┤
│  L3: COMPONENTS                                             │
│  "What are the logical building blocks inside each          │
│   container?"                                               │
│  Audience: Developers, tech leads                           │
│  Scope: Controllers, services, repositories, gateways       │
├─────────────────────────────────────────────────────────────┤
│  L4: CODE (optional)                                        │
│  "How is a component implemented?"                          │
│  Audience: Developers working on the component              │
│  Scope: Classes, interfaces, database schemas               │
└─────────────────────────────────────────────────────────────┘
```

**Key principle:** Each level zooms into the previous one. You cannot draw L3 without first having L2.

---

## 🧭 When to Use Which Level

| Situation | Start With | Why |
|-----------|-----------|-----|
| New project, no existing diagrams | L1 System Context | Establish scope and stakeholders first |
| Existing monolith, planning microservices | L2 Container | Identify deployable boundaries |
| Code review reveals tight coupling | L3 Component | Find circular dependencies |
| Complex domain model needs documentation | L4 Code | UML class diagram or ERD |
| Onboarding new developer | L1 → L2 → L3 | Progressive disclosure |
| Pitching to investors | L1 only | Business value, not technology |

---

## 🔄 The C4 Workflow

```
Phase 1: DISCOVER          Phase 2: MODEL           Phase 3: SYNC
┌──────────────────┐      ┌──────────────────┐     ┌──────────────────┐
│ Interview        │      │ Draw L1 Context  │     │ Scan codebase    │
│ stakeholders     │─────▶│ (Mermaid/        │────▶│ for drift        │
│ Identify users   │      │  Structurizr)    │     │ Update diagrams  │
│ List external    │      │                  │     │                  │
│ systems          │      │ Draw L2 Container│     │ Verify L2 maps   │
└──────────────────┘      │ (tech stack)     │     │ to Dockerfile/   │
                          │                  │     │ docker-compose   │
                          │ Draw L3 Component│     │                  │
                          │ (per container)  │     │ Verify L3 maps   │
                          │                  │     │ to folder struct │
                          │ L4: Optional     │     │                  │
                          │ (complex only)   │     │ ADR for major    │
                          └──────────────────┘     │ decisions        │
                                                   └──────────────────┘
```

---

## 🚫 Architectural Anti-Patterns (The "Don'ts")

### 1. The "Spaghetti" Diagram
**Symptom:** More than 20 elements in one diagram.  
**Solution:** Break into multiple views (e.g., "Customer Journey View", "Admin View").  
**Reference:** Simon Brown recommends 5-15 elements per diagram for readability.

### 2. Tech Leakage in L1
**Symptom:** Mentioning "React", "PostgreSQL", "Kafka" in System Context.  
**Solution:** L1 focuses on "What", not "How". Use "Product Catalog" not "PostgreSQL".  
**Rule:** If a non-technical stakeholder wouldn't understand it, it doesn't belong in L1.

### 3. Missing Descriptions
**Symptom:** Boxes with only names.  
**Solution:** Every element needs a one-sentence responsibility description.  
**Template:** `[Name]` — `[What it does]` for `[Who]`.

### 4. Ambiguous Arrows
**Symptom:** Labels like "Uses", "Sends", "Connects".  
**Solution:** Use action verbs: "Authenticates user via", "Publishes order event to", "Queries inventory from".

### 5. Phantom Containers
**Symptom:** Modeling a shared library (e.g., "utils.jar") as a container.  
**Solution:** Libraries are components (L3), not containers (L2). Containers must be independently deployable/runnable.

### 6. The "Everything Diagram"
**Symptom:** Trying to show L1, L2, and L3 in one diagram.  
**Solution:** One diagram per level. Use hyperlinks or navigation to connect them.

### 7. Stale Diagrams
**Symptom:** Diagrams don't match the code.  
**Solution:** Use "Design-to-Code Sync" — scan codebase on every major refactor. Store diagrams as code (Mermaid/Structurizr DSL) in version control.

---

## 🛠 Tooling: Mermaid vs Structurizr DSL

| Aspect | Mermaid | Structurizr DSL |
|--------|---------|-----------------|
| **Format** | Markdown code block | `.dsl` text file |
| **Rendering** | GitHub, GitLab, docs | Structurizr Lite/Cloud |
| **Model reuse** | Each diagram standalone | Single model → multiple views |
| **C4 compliance** | Manual (C4Context, C4Container plugins) | Enforced by DSL |
| **AI-friendly** | Good | Excellent (text-based, structured) |
| **Best for** | Quick docs, READMEs | Serious architecture, CI/CD |

**Recommendation:** Use Mermaid for quick sketches and READMEs. Use Structurizr DSL for project architecture that lives in version control.

### Structurizr DSL Quick Example
```dsl
workspace {
    model {
        user = person "Customer" "A registered user of the platform."
        ecommerce = softwareSystem "E-Commerce Platform" "Allows customers to browse and purchase products." {
            webapp = container "Web Application" "React/TypeScript" "Customer-facing UI."
            api = container "API Service" "Go/gRPC" "Business logic and API gateway."
            db = container "Database" "PostgreSQL" "Stores products, orders, users."
        }
        payment = softwareSystem "Payment Gateway" "External" "Processes payments."

        user -> webapp "Browses and purchases"
        webapp -> api "Calls API"
        api -> db "Reads/Writes"
        api -> payment "Processes payment"
    }
    views {
        systemContext ecommerce "SystemContext" {
            include *
            autolayout lr
        }
        container ecommerce "Containers" {
            include *
            autolayout lr
        }
        theme default
    }
}
```

---

## 📦 Standard Artifacts

Every C4 modeling session should produce:

```
docs/architecture/
├── workspace.dsl              # Structurizr DSL (single source of truth)
├── L1-system-context.md       # Mermaid for README/docs
├── L2-containers.md
├── L3-components/
│   ├── api-service.md
│   └── web-app.md
├── architecture-decisions.md  # ADRs for major tech choices
└── README.md                  # Index + navigation
```

---

## 🔗 C4 + DDD Integration Matrix

| C4 Level | DDD Concept | Mapping |
|----------|-------------|---------|
| **L1 System Context** | Bounded Contexts (high-level) | Each system in L1 ≈ one Bounded Context |
| **L2 Container** | Subdomains | Containers within a system map to Core/Supporting/Generic subdomains |
| **L2 Container** | Context Map | Relationships between containers = Upstream/Downstream |
| **L3 Component** | Aggregate Roots | Major components often correspond to ARs |
| **L3 Component** | Domain Services | Components with cross-aggregate logic |
| **L4 Code** | Entities, Value Objects | Classes in UML/class diagrams |

**Workflow:** Use `ddd-core` to discover Bounded Contexts → map to L1/L2 → use `c4-level3-component` to design internals → verify with `ddd-tactical` scoring rubric.

---

## 🚦 DORA: Loosely Coupled Architecture

DORA research identifies **Loosely Coupled Architecture** as the #1 predictor of high Deployment Frequency. C4 decisions directly affect delivery:

- **C4 L2 containers** should be independently deployable — each owns its data
- **Conway's Law:** Tightly coupled teams → tightly coupled architecture → Low DORA tier
- **Anti-pattern:** Shared database between containers = coordinated deployments

For DORA metrics assessment, use `dora-core` skill.

---

## 🔍 Smart Synthesis (Design-to-Code)

When documenting an existing project, scan the codebase first:

| C4 Level | Scan For | Maps To |
|----------|----------|---------|
| L2 | `package.json`, `pom.xml`, `go.mod`, `requirements.txt` | Container tech stack |
| L2 | `Dockerfile`, `docker-compose.yml`, `k8s/` | Deployment mapping |
| L2 | `terraform/`, CloudFormation | Infrastructure components |
| L3 | `src/services/`, `internal/`, `pkg/` | Component boundaries |
| L3 | `*_test.go`, `*.test.ts` | Component responsibilities (test names reveal intent) |
| L4 | Domain classes, DB migrations | UML classes, ERD tables |

---

## 📚 References

- [C4 Model Official](https://c4model.com/) — Simon Brown
- [Structurizr DSL](https://docs.structurizr.com/dsl) — Reference implementation
- [Software Architecture for Developers](https://simonbrown.je/#books) — Simon Brown's book
- [The C4 Model on ThoughtWorks Tech Radar](https://www.thoughtworks.com/radar/techniques/c4-model)
