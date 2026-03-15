---
name: ddd-core
description: Professional Strategic Domain-Driven Design (DDD) Hub. Use this skill for Event Storming, identifying Subdomains, defining Bounded Contexts, and mapping Domain Models to the heart of your architecture.
metadata:
  tags: ["ddd", "architecture", "strategic-design", "bounded-context", "event-storming"]
---

# Domain-Driven Design (DDD): Strategic Hub & Workshop

"The heart of software is its ability to solve domain-related problems for its user." — Martin Fowler.

Strategic DDD is about **taming complexity** by identifying what to build and how to organize teams around **Bounded Contexts**.

## 🌪 Virtual Event Storming Workflow

Use this workflow to discover domains through a collaborative workshop with AI:
1.  **Big Picture:** Identify all **Domain Events** (Past tense: e.g., `OrderPlaced`).
2.  **Commands:** Identify the triggers for those events (e.g., `PlaceOrder`).
3.  **Policy & Logic:** Define rules that link commands and events.
4.  **Aggregate Identification:** Group related commands/events into consistency boundaries.
5.  **Bounded Context Mapping:** Group Aggregates into logical contexts.

## 🎯 Subdomain Types (ROI Focus)

- **Core Domain:** Your unique competitive advantage. High complexity, high value. *Strategy: Build in-house with top talent.*
- **Supporting Subdomain:** Necessary but not a differentiator. Medium complexity. *Strategy: Build or use open-source.*
- **Generic Subdomain:** Standard problems with off-the-shelf solutions. *Strategy: Buy/Use SaaS.*

## 🔗 Context Mapping Patterns (Upstream/Downstream)

- **ACL (Anti-Corruption Layer):** Translates external models to your internal domain. (Highly recommended to shield Core Domains).
- **OHS (Open Host Service):** A public API for your domain.
- **Shared Kernel:** Two contexts sharing part of the model (High risk, use sparingly).
- **Conformist:** Downstream team strictly follows the upstream model.

## 🚫 Strategic Anti-Patterns
- **The Generic Core:** Wasting top talent on building generic things (like Auth).
- **Context Leakage:** Using a model from one Bounded Context directly in another without translation (ACL).
- **Anemic Bounded Context:** A context that has no clear responsibility or ubiquitous language.
