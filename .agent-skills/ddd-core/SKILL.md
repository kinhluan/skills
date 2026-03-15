---
name: ddd-core
description: Strategic Domain-Driven Design (DDD) for high-level architecture. Use this skill for defining Bounded Contexts, Ubiquitous Language, and mapping domain models to the C4 architecture (Context Map to L1/L2).
metadata:
  tags: ["ddd", "architecture", "strategic-design", "bounded-context"]
---

# Domain-Driven Design (DDD): Strategic Hub

DDD is an approach to software development that centers the design on a deep understanding of the business domain.

## 🎯 Core Strategic Patterns

1.  **Ubiquitous Language:** A shared language used by both technical and business people to describe the domain.
2.  **Bounded Context:** A logical boundary within which a particular domain model is defined and applicable.
3.  **Context Map:** A visualization of the relationships and integrations between different Bounded Contexts.

## 🔗 DDD to C4 Model Mapping

| DDD Concept | C4 Level | Visualization |
| :--- | :--- | :--- |
| **Domain/Subdomain** | **L1: System Context** | The high-level business landscape. |
| **Bounded Context** | **L2: Container** | A deployable unit (Microservice, API). |
| **Aggregate/Service** | **L3: Component** | Major logic groupings inside a container. |
| **Entities/VOs** | **L4: Code** | Implementation details (Classes). |

## 🚫 DDD Anti-Patterns

1.  **The Shared Database:** Multiple Bounded Contexts sharing a single database schema. *Solution: Each Bounded Context (Container) owns its data.*
2.  **The Big Ball of Mud:** A system with no clear boundaries where everything depends on everything. *Solution: Define Bounded Contexts and use an ACL.*
3.  **Anemic Domain Model:** Moving logic out of domain objects into "Service" classes. *Solution: Keep business logic inside Aggregates.*

## 🚶 Integration Workflow

1.  **Event Storming:** Discover domains and bounded contexts.
2.  **Define Boundaries:** Map Bounded Contexts to C4 Containers (L2).
3.  **Establish Relationships:** Define Upstream/Downstream and ACLs in Context Maps.
