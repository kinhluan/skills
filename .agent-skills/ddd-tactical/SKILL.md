---
name: ddd-tactical
description: Tactical Domain-Driven Design (DDD) building blocks. Use this skill when designing internal domain models including Entities, Value Objects, Aggregates, Domain Services, and Repositories.
metadata:
  tags: ["ddd", "tactical-design", "aggregates", "clean-architecture"]
---

# Domain-Driven Design (DDD): Tactical Building Blocks

Tactical DDD focuses on the technical implementation of domain models within a single Bounded Context.

## 🧱 Key Building Blocks

1.  **Entity:** An object defined by its identity (e.g., `User` with a unique ID).
2.  **Value Object:** An object defined by its attributes, with no identity (e.g., `Money`, `Address`). Should be immutable.
3.  **Aggregate:** A cluster of associated objects treated as a single unit for data changes. Every Aggregate has an **Aggregate Root**.
4.  **Domain Service:** Logic that doesn't naturally belong to an Entity or Value Object (e.g., `PaymentProcessor`).
5.  **Repository:** A mechanism for encapsulating storage and retrieval of Aggregates.

## 🔗 Tactical DDD to C4 Model Mapping

- **Aggregate Root:** Maps to a **Component (L3)**.
- **Entities & Value Objects:** Map to **Code (L4)**.

## 🚫 Tactical Anti-Patterns

1.  **Leaking Infrastructure:** Including persistence (SQL) or transport (REST) logic in the domain layer. *Solution: Use the Repository pattern and ACL.*
2.  **Large Aggregates:** Aggregates that grow too big, causing performance and concurrency issues. *Solution: Keep Aggregates small and use IDs to reference other Aggregates.*
3.  **Anemic Objects:** Entities that only have getters and setters with no business logic. *Solution: Move business logic from Services into Entities.*

## 🚶 Implementation Workflow

1.  **Identify Aggregates:** Determine transactional boundaries.
2.  **Model Entities & Value Objects:** Define the state and behavior.
3.  **Implement Repositories:** Define the interface for data access.
4.  **Define Domain Services:** Handle orchestration that spans multiple Aggregates.
