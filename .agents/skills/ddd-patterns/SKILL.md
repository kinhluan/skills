---
name: ddd-patterns
description: Advanced Domain-Driven Design (DDD) Integration Patterns. Use this skill for implementing CQRS, Event Sourcing, the Outbox Pattern, and Anti-Corruption Layers (ACL) in distributed systems.
metadata:
  tags: ["ddd", "advanced-patterns", "cqrs", "event-sourcing", "outbox"]
---

# Domain-Driven Design (DDD): Advanced Patterns

Advanced integration patterns for handling complex distributed system interactions and transactional consistency.

## 🚀 Advanced Patterns

1.  **CQRS (Command Query Responsibility Segregation):** Separation of write (Command) and read (Query) models to optimize performance and scalability.
2.  **Event Sourcing:** Capturing all changes to the state of an application as a sequence of events (The current state is reconstructed from the log).
3.  **Outbox Pattern:** Ensuring transactional consistency between a database and a message broker. (Save to DB and a 'Message Outbox' in the same transaction).
4.  **ACL (Anti-Corruption Layer):** Translating and isolating external systems' models to maintain the integrity of your core domain model.

## ⚡ CQRS + Event Sourcing Workflow

1.  **Command Side:** Receives request -> Aggregate Root (AR) validates -> AR emits Event -> Event saved to **Event Store**.
2.  **Projection Side:** **Projector** listens to Events -> Updates **Read Model** (Optimized for queries: e.g., Elasticsearch, Read DB).
3.  **Query Side:** Reads from Read Model only.

## 🚫 Advanced Anti-Patterns

- **Premature CQRS:** Adding CQRS to simple systems. (Increases complexity needlessly).
- **The Giant Event:** Capturing too much state in a single event. (Events should be granular business facts).
- **Ignoring Eventual Consistency:** Forgetting that Read Models may be out of sync for a short time. *Solution: Compensating actions or UI feedback.*

## 🔗 Integration Checklist

- [ ] Is the Outbox pattern used for cross-container communication?
- [ ] Is the ACL properly shielding the Core Domain?
- [ ] Are events immutable and versioned?
