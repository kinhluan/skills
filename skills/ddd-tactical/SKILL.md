---
name: ddd-tactical
description: Model and review tactical Domain-Driven Design inside one bounded context using aggregates, entities, value objects, domain services, repositories, factories, and domain events. Use when code must enforce domain invariants or an anemic/overgrown domain model needs redesign.
metadata:
  tags: ["ddd", "aggregates", "value-objects", "domain-events", "repositories"]
---

# Tactical DDD

Confirm the bounded context and ubiquitous language before choosing tactical patterns. Model behavior and invariants, not a database diagram with domain names.

## Workflow

1. Collect commands, policies, invariants, lifecycle, and failure cases from domain examples.
2. Identify identity-bearing concepts and immutable descriptive values.
3. Draw candidate consistency boundaries.
4. Choose an aggregate root that guards each boundary.
5. Keep cross-aggregate references by identity and coordinate across them at the application/process level.
6. Place behavior where the knowledge lives; use a domain service only when no entity/value object naturally owns it.
7. Define repository interfaces around aggregate persistence needs, not tables.
8. Emit domain events for facts other parts of the model need to react to.
9. Test invariants and state transitions without infrastructure.

## Building Blocks

| Building block | Use |
|---|---|
| entity | continuity and identity across state changes |
| value object | immutable, equality-by-value concept that validates itself |
| aggregate | transactional consistency boundary |
| domain service | stateless domain operation spanning concepts |
| factory | valid creation when construction is complex |
| repository | collection-like access to aggregate roots |
| domain event | meaningful fact that already occurred |

Not every noun needs a class, repository, factory, or event.

## Aggregate Rules

- Keep the boundary as small as the invariant permits.
- Enforce invariants synchronously inside one aggregate transaction.
- Avoid loading an unbounded object graph.
- Do not expose mutable internals.
- Model commands as intention-revealing behavior, not public setters.
- Use optimistic concurrency or another explicit conflict policy.
- Treat cross-aggregate consistency as eventual unless a proven invariant requires a different boundary.
- Do not split or merge aggregates solely for ORM convenience.

## Review Questions

- Which business rule would become invalid if two commands race?
- Can invalid state be constructed or persisted?
- Is behavior trapped in application services while entities are data bags?
- Does infrastructure terminology leak into the domain?
- Are domain events facts in past tense with stable meaning?
- Does repository usage reveal query/reporting needs that belong in a read model?
- Are transaction boundaries and retries safe?

Avoid numeric “DDD quality scores” unless the team defines a repeatable rubric and uses it as a conversation aid, not proof of design quality.

## Output

```markdown
## Tactical Model — [bounded context]

**Ubiquitous language:** [...]
**Commands/invariants:** [...]
**Aggregate boundaries:** [...]
**Entities/value objects:** [...]
**Domain services:** [...]
**Repositories:** [...]
**Domain events:** [...]
**Concurrency/transaction policy:** [...]
**Tests:** [examples proving invariants]
**Open boundary risks:** [...]
```

Read [references/detailed-guide.md](references/detailed-guide.md) only for the relevant building block or implementation example. Use `ddd-patterns` for cross-context integration.
