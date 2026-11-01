---
name: ddd-patterns
description: Select and design advanced Domain-Driven Design integration patterns such as anti-corruption layers, outbox/inbox, sagas, CQRS, and event sourcing. Use when bounded contexts need reliable coordination, translation, asynchronous consistency, or separate read/write models.
metadata:
  tags: ["ddd", "integration", "outbox", "saga", "cqrs", "event-sourcing"]
---

# DDD Integration Patterns

Start from bounded contexts, ownership, invariants, and failure modes. These patterns add operational and cognitive cost; use the smallest one that solves an observed force.

## Decision Guide

| Force | Candidate |
|---|---|
| protect one model from another model/API | anti-corruption layer |
| atomically persist state and publish intent | transactional outbox |
| deduplicate at-least-once delivery | inbox/idempotent consumer |
| coordinate a long-running cross-context outcome | process manager or saga |
| optimize a materially different read model | CQRS |
| require event history as source of truth | event sourcing |

Do not equate CQRS with event sourcing, saga with distributed transaction, or event publication with exactly-once processing.

## Workflow

1. Name participating contexts and the owner of each invariant.
2. Describe commands, events, queries, and data contracts in domain language.
3. Define delivery guarantees, ordering scope, duplication, timeout, retry, and poison-message behavior.
4. Select orchestration or choreography from ownership and observability needs.
5. Design idempotency, compensation, reconciliation, and manual recovery.
6. Version contracts for additive evolution and consumer lag.
7. Instrument correlation/causation IDs, state transitions, lag, retry, and dead-letter flow.
8. Test crash points and replay before production.

## Pattern Guardrails

### Outbox/Inbox

Commit aggregate state and outbox record in one local transaction. Publish asynchronously. Consumers must tolerate duplicates. Monitor unpublished age and provide replay/reconciliation.

### Saga/Process Manager

Define the state machine, owner, deadlines, compensations, and terminal/manual states. Compensation is a business action and may not perfectly undo reality.

### CQRS

Use when read/write models truly differ. Document projection lag and UX behavior under eventual consistency. A separate class for reads is not by itself a reason for separate infrastructure.

### Event Sourcing

Use only when event history is the authoritative domain model and the team can own schema evolution, replay, snapshots, privacy erasure constraints, debugging, and projection rebuilds. Events are immutable facts; corrections are new events.

### Anti-Corruption Layer

Keep translation at the boundary. Do not leak external DTOs or terminology into the domain. Test mapping loss and unknown enum/version behavior.

## Output

Return the observed forces, chosen/rejected patterns, consistency and ownership model, failure-state table, contract/version strategy, observability, recovery procedure, and tests.

Read [references/detailed-guide.md](references/detailed-guide.md) only for the selected pattern's detailed examples.
