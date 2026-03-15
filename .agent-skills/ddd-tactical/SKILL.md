---
name: ddd-tactical
description: Tactical Domain-Driven Design (DDD) with Scoring Rubric. Use this skill when designing internal domain models (Entities, VOs, Aggregates) or performing architectural reviews of existing codebases.
metadata:
  tags: ["ddd", "tactical-design", "aggregates", "clean-architecture", "domain-review"]
---

# Domain-Driven Design (DDD): Tactical Building Blocks & Review

Tactical DDD focuses on the technical implementation of domain models within a single Bounded Context.

## 🧱 Key Building Blocks (Mandatory Review)

- **Aggregate Root (AR):** The entry point to a cluster of objects. Only the AR should be referenced by other components.
- **Value Object (VO):** Immutable, identity-less objects defined by their state (e.g., `Money`, `Email`). Use them instead of primitives (e.g., `string`).
- **Domain Event:** Something significant happened in the domain (e.g., `OrderPaid`). Use them for decoupled side effects.

## ⭐ Domain Model Scoring Rubric (0-10)

Use this rubric to rate your current domain design:

1.  **Immutability (2 pts):** Are Value Objects immutable and used instead of primitives?
2.  **Invariants (2 pts):** Does the Aggregate Root enforce business rules consistently before any state change?
3.  **Encapsulation (2 pts):** Are internal parts of the aggregate hidden from the outside?
4.  **Identity (2 pts):** Does every Entity have a globally unique, stable identity?
5.  **Ubiquitous (2 pts):** Do class and method names match the business language exactly?

*Goal: Target 8/10 or higher for Core Domains.*

## 🚫 Tactical Anti-Patterns (The "Don'ts")

- **The Anemic Model:** Entities with only getters/setters and no logic. (Score: 0/10).
- **The God Aggregate:** A single Aggregate that contains too many entities (Spaghetti logic). (Score: 3/10).
- **Primitive Obsession:** Using `int`, `string` for things that have rules (e.g., `Age`, `SKU`). (Score: 5/10).
- **Leaking Domain:** Returning domain entities directly in your Web/API layer. *Solution: Use DTOs.*

## ⚡ Domain Events Pattern
Collect events inside the Aggregate and publish them after the transaction completes:
```python
class Order(AggregateRoot):
    def pay(self, payment):
        if self.is_paid: raise Error()
        self.apply(OrderPaidEvent(self.id))
```
