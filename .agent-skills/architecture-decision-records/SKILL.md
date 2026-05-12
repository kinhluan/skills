---
name: architecture-decision-records
description: Create and manage Architecture Decision Records (ADRs) using MADR 4.0.0 format. Use this skill when evaluating technology choices, documenting design decisions, or reviewing past architectural choices.
metadata:
  tags: ["architecture", "adr", "decision-records", "madr", "documentation", "tech-radar"]
---

# Architecture Decision Records (ADR)

An Architecture Decision Record captures the context, decision, and consequences of significant technical choices. ADRs prevent re-litigating settled decisions and preserve institutional knowledge.

> "Architecture is the stuff that's hard to change. Document why you chose it." — Michael Nygard

---

## 🎯 When to Write an ADR

| Situation | Write ADR? | Template |
|-----------|-----------|----------|
| Choosing a database (PostgreSQL vs MongoDB) | ✅ Yes | MADR Full |
| Adopting a framework (React vs Vue) | ✅ Yes | MADR Full |
| REST vs GraphQL vs gRPC | ✅ Yes | MADR Full |
| Adding a new microservice | ✅ Yes | MADR Full |
| Choosing a cloud provider | ✅ Yes | MADR Full |
| Fixing a typo in config | ❌ No | — |
| Adding a linter rule | ⚠️ Maybe | MADR Minimal |
| Updating a dependency version | ⚠️ Maybe | Y-Statement |

**Rule of thumb:** If the decision will affect the team for >6 months, write an ADR.

---

## 📝 MADR 4.0.0 Template (Full)

MADR (Markdown Architectural Decision Records) is the industry standard. Version 4.0.0 was released September 2024.

```markdown
---
status: proposed | accepted | rejected | deprecated | superseded by ADR-0012
date: 2024-01-15
decision-makers: [@alice, @bob]
consulted: [@charlie, @diana]
informed: [@team-backend]
---

# Use PostgreSQL as Primary Database

## Context and Problem Statement

We need a relational database for our e-commerce platform. The database must:
- Support ACID transactions for order processing
- Handle complex queries for reporting
- Scale to 10M+ products
- Have strong community support and tooling

## Decision Drivers

- **Data consistency:** Orders and payments require ACID guarantees
- **Query complexity:** Product search, order history, analytics need JOINs
- **Team expertise:** Team has 5+ years PostgreSQL experience
- **Operational cost:** Managed service availability (AWS RDS, GCP Cloud SQL)
- **Ecosystem:** ORM support, migration tools, monitoring

## Considered Options

- PostgreSQL
- MySQL
- MongoDB
- CockroachDB

## Decision Outcome

Chosen option: **"PostgreSQL"**, because it best satisfies our decision drivers:
- Full ACID compliance for financial transactions
- Advanced JSON support for flexible product attributes
- Excellent query planner for complex analytics
- Managed services available on AWS, GCP, Azure
- Team already proficient

### Consequences

- **Good**, because ACID transactions prevent data corruption in order processing
- **Good**, because JSONB columns allow flexible schema for product attributes without full NoSQL
- **Good**, because AWS RDS provides automated backups, failover, and patching
- **Bad**, because horizontal scaling requires read replicas or sharding (more complex than DynamoDB)
- **Bad**, because schema migrations require downtime or complex blue/green deployment

### Confirmation

- Validate: Run load test with 10M products + concurrent orders
- Revisit if: Write throughput exceeds 10K TPS or horizontal scaling becomes critical

## Pros and Cons of the Options

### PostgreSQL

- **Good**, because full ACID compliance and advanced SQL features
- **Good**, because JSONB provides document-like flexibility within relational structure
- **Good**, because mature ecosystem (PostGIS, full-text search, partitioning)
- **Bad**, because vertical scaling limits on single-node writes
- **Bad**, because schema changes require migration planning

### MySQL

- **Good**, because widely used, good performance for simple queries
- **Good**, because AWS Aurora provides excellent managed service
- **Bad**, because less advanced query planner for complex analytics
- **Bad**, because JSON support less mature than PostgreSQL JSONB

### MongoDB

- **Good**, because schema flexibility for rapidly changing product attributes
- **Good**, because horizontal scaling via sharding is native
- **Bad**, because eventual consistency unacceptable for financial transactions
- **Bad**, because team lacks operational experience
- **Bad**, because complex JOINs require application-level processing

### CockroachDB

- **Good**, because distributed SQL with horizontal scaling
- **Good**, because PostgreSQL-compatible wire protocol
- **Bad**, because higher operational complexity
- **Bad**, because smaller community, fewer managed service options
- **Bad**, because overkill for current scale (premature optimization)

## More Information

- [PostgreSQL vs MySQL comparison](https://www.postgresql.org/about/)
- [AWS RDS PostgreSQL](https://aws.amazon.com/rds/postgresql/)
- Related: ADR-0005 (Read Replica Strategy)
```

---

## 📝 MADR Minimal Template

For smaller decisions, use the minimal template:

```markdown
---
status: accepted
date: 2024-01-15
---

# Adopt Ruff for Python Linting

## Context

We currently use flake8 + black + isort. Three tools with separate configs.

## Decision

Replace with Ruff — one tool, faster, compatible.

## Consequences

- **Good**: Single config file, 10-100x faster
- **Bad**: Team needs to learn new rule codes
- **Mitigation**: Migration guide in docs/python-tooling.md
```

---

## 📝 Y-Statement Template

For the fastest documentation (one sentence):

```markdown
# Y-Statement: API Gateway Selection

In the context of **building a microservices architecture**,
facing **the need for centralized API management, authentication, and rate limiting**,
we decided for **Kong Gateway**
and against **AWS API Gateway and custom Nginx solution**,
to achieve **vendor independence, plugin extensibility, and team familiarity with Lua**,
accepting that **we need to manage Kong infrastructure ourselves**.
```

---

## 🏗️ ADR Directory Structure

```
docs/
├── adr/
│   ├── README.md              # Index and guidelines
│   ├── template.md            # Your team's MADR template
│   ├── 0001-record-architecture-decisions.md
│   ├── 0002-use-postgresql.md
│   ├── 0003-caching-strategy.md
│   ├── 0004-microservices-vs-monolith.md
│   ├── 0005-read-replica-strategy.md
│   ├── 0006-graphql-api.md
│   ├── 0007-event-driven-architecture.md
│   ├── 0015-adopt-kubernetes.md
│   ├── 0016-container-orchestration.md  # [SUPERSEDED by 0015]
│   └── 0020-deprecate-rest-v1.md        # Supersedes implicit earlier decision
```

### ADR Index (README.md)

```markdown
# Architecture Decision Records

## Index

| ADR | Title | Status | Date | Supersedes |
|-----|-------|--------|------|------------|
| 0001 | Record Architecture Decisions | Accepted | 2024-01-10 | — |
| 0002 | Use PostgreSQL as Primary Database | Accepted | 2024-01-15 | — |
| 0003 | Caching Strategy with Redis | Accepted | 2024-01-20 | — |
| 0004 | Start with Modular Monolith | Accepted | 2024-02-01 | — |
| 0005 | Read Replica Strategy | Accepted | 2024-02-15 | — |
| 0006 | GraphQL for Mobile API | Accepted | 2024-03-01 | — |
| 0007 | Event-Driven Architecture | Accepted | 2024-03-15 | — |
| 0015 | Adopt Kubernetes | Accepted | 2024-06-01 | 0016 |
| 0016 | Container Orchestration with Docker Swarm | Deprecated | 2024-01-30 | — |
| 0020 | Deprecate REST API v1 | Accepted | 2024-08-01 | — |

## Status Definitions

- **Proposed**: Under discussion, seeking feedback
- **Accepted**: Decision made, being implemented
- **Rejected**: Considered but not adopted
- **Deprecated**: No longer relevant, but was accepted
- **Superseded**: Replaced by a newer ADR

## Creating a New ADR

1. Copy `template.md` to `NNNN-title-with-dashes.md`
2. Fill in all sections
3. Submit PR for team review
4. Update this index after merge
```

---

## 🔄 ADR Lifecycle

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ PROPOSED │───▶│ ACCEPTED │───▶│DEPRECATED│    │ REJECTED │
└──────────┘    └────┬─────┘    └────┬─────┘    └──────────┘
                     │               │
                     │         ┌─────┘
                     │         ▼
                     │    ┌──────────┐
                     └───▶│SUPERSEDED│
                          │ by ADR-X │
                          └──────────┘
```

### State Transitions

| From | To | Trigger |
|------|-----|---------|
| Proposed | Accepted | Team consensus in PR review |
| Proposed | Rejected | Better alternative found |
| Accepted | Deprecated | Technology no longer used |
| Accepted | Superseded | New ADR replaces this decision |
| Deprecated | — | Historical reference only |

---

## 🛠️ Automation with adr-tools

```bash
# Install
brew install adr-tools

# Initialize ADR directory
adr init docs/adr

# Create new ADR (auto-numbers)
adr new "Use PostgreSQL as Primary Database"
# Creates: docs/adr/0002-use-postgresql-as-primary-database.md

# Supersede an ADR
adr new -s 3 "Use Redis Cluster for Caching"
# Creates new ADR that supersedes ADR-0003

# Link related ADRs
adr link 5 "Enables" 6 "Is enabled by"

# Generate table of contents
adr generate toc > docs/adr/README.md
```

---

## 🎯 Decision Quality Checklist

Before accepting an ADR, verify:

- [ ] **Context is clear:** Someone reading this in 2 years understands the problem
- [ ] **Drivers are explicit:** Criteria for evaluating options are stated
- [ ] **Options are comprehensive:** At least 3 alternatives considered (including "do nothing")
- [ ] **Trade-offs are honest:** Both good and bad consequences documented
- [ ] **Decision is reversible:** How hard to undo? (should be stated)
- [ ] **Confirmation defined:** How will we know this decision was correct?
- [ ] **Stakeholders consulted:** Decision-makers, consulted, informed listed
- [ ] **Related ADRs linked:** Dependencies and superseded decisions referenced

---

## 🚫 ADR Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Decision Without Context** | "We chose X" with no explanation | Always include "why this problem matters" |
| **One Option Only** | Only the chosen option documented | Document all considered options with pros/cons |
| **No Consequences** | Only positive outcomes listed | Be honest about negative consequences |
| **Perpetual Proposed** | ADR stays "proposed" for months | Set decision deadline (e.g., 2 weeks) |
| **Editing Accepted ADRs** | Changing ADR-0002 after acceptance | Create ADR-0020 that supersedes it |
| **ADR for Everything** | ADR for linter rule changes | Use minimal template or skip for trivial decisions |
| **Missing Links** | Related decisions not connected | Use `adr link` or manual references |

---

## 🔗 Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `c4-model` | ADRs document "why" behind C4 L2 container choices |
| `ddd-core` | ADRs capture subdomain classification decisions |
| `why-strategic-rationale` | ADR = technical implementation of WHY statement |
| `evolutionary-architecture` | ADRs track architectural dimension decisions |

---

## 📚 References

- [MADR 4.0.0](https://adr.github.io/madr/) — Official specification
- [ADR GitHub Organization](https://github.com/adr) — Templates and tools
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) — Michael Nygard (original)
- [Y-Statements](https://www.infoq.com/articles/sustainable-architectural-design-decisions/) — Sustainable Architectural Decisions
- [adr-tools](https://github.com/npryce/adr-tools) — Command-line tools
