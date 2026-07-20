---
name: clean-architecture
description: Design or refactor code boundaries so business policy does not depend on volatile frameworks, databases, UI, or infrastructure. Use for Clean/Hexagonal/Onion architecture, dependency-rule reviews, ports and adapters, use cases, component boundaries, or testability.
metadata:
  tags: ["clean-architecture", "dependency-rule", "ports-and-adapters", "boundaries", "testability"]
---

# Clean Architecture

Protect stable policy from volatile details. Apply the dependency rule at meaningful component/module boundaries; do not reproduce a fixed four-layer folder tree in every application.

## Workflow

1. Identify business policy, use cases, inputs/outputs, and volatile details.
2. Inspect source-code dependencies, runtime calls, data shapes, and ownership.
3. Choose boundaries where independent testing or replacement has real value.
4. Define inward-owned ports using domain/use-case language.
5. Implement outward adapters for web, database, messaging, UI, and vendors.
6. Translate boundary DTOs rather than leaking framework or persistence types inward.
7. Wire dependencies at a composition root.
8. Test policy through ports and add adapter contract/integration tests.
9. Measure whether the boundary reduces change cost; remove abstractions that only forward calls.

Runtime control may flow outward while source dependencies point inward.

## Boundary Rules

- domain policy must not import a web framework, ORM, queue client, or vendor SDK;
- use cases coordinate intent and transactions without becoming a grab bag;
- interfaces belong near the consumer/policy that needs them;
- adapters handle protocol, serialization, retries, and infrastructure errors;
- map errors into stable boundary semantics;
- keep transaction and consistency ownership explicit;
- prevent transport/database DTOs from becoming the domain model;
- avoid global service locators and hidden dependencies.

## Calibrate the Design

Simple CRUD may need fewer boundaries than a complex core domain. A modular monolith can follow the dependency rule; microservices are not required. “Repository,” “service,” and “use case” names do not prove clean architecture—inspect dependency direction and change coupling.

## Review Questions

- Can policy tests run without network, database, clock, or framework boot?
- Which dependency changes force policy changes?
- Are abstractions stable and behavior-oriented?
- Does mapping preserve validation and error meaning?
- Where do authorization, transactions, retries, and idempotency live?
- Are packages organized around capabilities or only technical layers?
- Is the abstraction cost lower than expected volatility?

## Output

Return the current dependency map, proposed boundaries/ports/adapters, violations with evidence, migration slices, test strategy, tradeoffs, and what should deliberately remain simple.

Read [references/detailed-guide.md](references/detailed-guide.md) only for a relevant pattern or code example. Use `ddd-tactical` when the main problem is domain invariants and `c4-level3-component` for component visualization.
