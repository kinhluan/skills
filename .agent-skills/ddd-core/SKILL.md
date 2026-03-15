---
name: ddd-core
description: Professional Strategic Domain-Driven Design (DDD) Hub. Use this skill for Event Storming workshops, identifying Subdomain Types (Core, Supporting, Generic), defining Bounded Contexts, and mapping Domain Models to C4 Architecture.
metadata:
  tags: ["ddd", "architecture", "strategic-design", "bounded-context", "event-storming"]
---

# Domain-Driven Design (DDD): Strategic Hub & Workshop

Strategic DDD is about identifying what to build and how to organize teams around Bounded Contexts.

## 🌪 Virtual Event Storming Workflow

Use this workflow to discover domains through a collaborative workshop with AI:
1.  **Big Picture:** Identify all **Domain Events** (Past tense: e.g., `OrderPlaced`, `PaymentFailed`).
2.  **Commands:** Identify the triggers for those events (e.g., `PlaceOrder`, `MakePayment`).
3.  **Policy & Logic:** Define rules that link commands and events (e.g., "If payment fails, cancel order").
4.  **Aggregate Identification:** Group related commands/events into consistency boundaries (Aggregates).
5.  **Bounded Context Mapping:** Group Aggregates into logical contexts.

## 🎯 Subdomain Types (ROI Focus)

- **Core Domain:** Your unique competitive advantage. High complexity, high value. (e.g., Pricing algorithm). *Strategy: Build in-house with top talent.*
- **Supporting Subdomain:** Necessary but not a differentiator. Medium complexity. (e.g., Inventory tracking). *Strategy: Build or use open-source.*
- **Generic Subdomain:** Standard problems with off-the-shelf solutions. Low differentiation. (e.g., Authentication, Email). *Strategy: Buy/Use SaaS.*

## 🔗 Context Mapping Patterns (Upstream/Downstream)

- **ACL (Anti-Corruption Layer):** A layer that translates external models to your internal domain. (Recommended for Core Domains).
- **OHS (Open Host Service):** A public API that others can use to interact with your domain.
- **Shared Kernel:** Two contexts sharing a part of the model (High risk, use sparingly).
- **Conformist:** Downstream team strictly follows the upstream model.

## 🚫 Strategic Anti-Patterns
- **The Generic Core:** Wasting top talent on building generic things (like Auth).
- **Context Leakage:** Using a model from one Bounded Context directly in another without translation (ACL).
- **Anemic Bounded Context:** A context that has no clear responsibility or ubiquitous language.
