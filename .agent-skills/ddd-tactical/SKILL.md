---
name: ddd-tactical
description: Tactical Domain-Driven Design (DDD) with Scoring Rubric. Use this skill when designing internal domain models or performing architectural reviews to ensure domain logic is isolated and rich.
metadata:
  tags: ["ddd", "tactical-design", "aggregates", "clean-architecture", "domain-review"]
---

# Domain-Driven Design (DDD): Tactical Building Blocks & Review

Tactical DDD focuses on the **technical implementation** of rich domain models within a single Bounded Context.

"The heart of DDD is the Domain Model itself." — Martin Fowler.

## 🧱 Key Building Blocks (Mandatory Review)

- **Aggregate Root (AR):** The cluster entry point. Only the AR should be referenced from outside.
- **Value Object (VO):** Immutable, identity-less objects defined by state (e.g., `Money`, `Email`). **Always prefer VOs over primitives.**
- **Domain Event:** A record of something significant that happened in the domain (e.g., `OrderPaid`).

## ⭐ Domain Model Scoring Rubric (0-10)

Rate your domain design based on these criteria:

1.  **Immutability (2 pts):** Are Value Objects used correctly instead of primitives?
2.  **Invariants (2 pts):** Does the Aggregate Root enforce business rules *before* any state change?
3.  **Encapsulation (2 pts):** Are internal aggregate parts hidden from the outside?
4.  **Identity (2 pts):** Does every Entity have a globally unique, stable identity?
5.  **Ubiquitous Language (2 pts):** Do class and method names match the business language exactly?

*Goal: Target 8/10 or higher for Core Domains.*

## 🚫 Tactical Anti-Patterns (The "Don'ts")

- **The Anemic Model:** Entities with only getters/setters and no logic. Logic is leaked into Services. (Score: 0/10).
- **The God Aggregate:** A single Aggregate that contains too many entities. (Score: 3/10).
- **Primitive Obsession:** Using `int`, `string` for things that have rules (e.g., `Age`). (Score: 5/10).
- **Leaking Domain:** Returning domain entities directly in your Web/API layer. *Solution: Use DTOs.*

## ⚡ Domain Events Pattern
Collect events inside the Aggregate and publish them after the transaction completes:
```python
class Order(AggregateRoot):
    def pay(self, payment):
        if self.is_paid: raise Error()
        self.apply(OrderPaidEvent(self.id))
```

## 📦 Tactical Artifacts

After designing the tactical model, create:
1. **`docs/domain/model-summary.md`** — Summary of all Aggregates, Entities, and Value Objects.
2. **`docs/domain/logic-rules.md`** — Detailed list of business invariants enforced by Aggregate Roots.
3. **Visual Class Diagram** — Mermaid `classDiagram` to visualize tactical relationships.
