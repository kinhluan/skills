---
name: evolutionary-architecture
description: Design and maintain architectures that support guided, incremental change. Use this skill for fitness functions, architecture testing, strangler fig patterns, and protecting architectural characteristics as systems evolve.
metadata:
  tags: ["architecture", "evolutionary", "fitness-functions", "strangler-fig", "architecture-testing", "refactoring"]
---

# Evolutionary Architecture

"An evolutionary architecture supports guided, incremental change as a first principle across multiple dimensions." — Neal Ford, Rebecca Parsons, Pat Kua

Traditional architecture tries to predict the future. Evolutionary architecture accepts that change is inevitable and builds mechanisms to guide it safely.

---

## 🎯 Core Concepts

### The Three Pillars

```
┌─────────────────────────────────────────────────────────────┐
│              EVOLUTIONARY ARCHITECTURE                       │
│                                                              │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│   │  Incremental │  │   Fitness   │  │ Appropriate │       │
│   │    Change    │  │  Functions  │  │   Coupling  │       │
│   │              │  │             │  │             │       │
│   │ Deployment   │  │ Automated   │  │ Quantum     │       │
│   │ pipelines    │  │ tests that  │  │ boundaries  │       │
│   │ Feature      │  │ verify      │  │ Team        │       │
│   │ toggles      │  │ architecture│  │ alignment   │       │
│   │              │  │ goals       │  │             │       │
│   └─────────────┘  └─────────────┘  └─────────────┘       │
│                                                              │
│   Change without guidance = chaos                            │
│   Fitness without change = stagnation                        │
│   Coupling without fitness = fragile                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 1️⃣ Fitness Functions

**Definition:** Automated tests that verify architectural goals and constraints. Like unit tests for architecture.

### Types of Fitness Functions

| Type | Scope | When It Runs | Example |
|------|-------|-------------|---------|
| **Atomic** | Single component | Unit test phase | "No package has >20 classes" |
| **Holistic** | Whole system | Integration test | "API response time < 200ms" |
| **Triggered** | On specific event | Pre-commit/PR | "No new circular dependencies" |
| **Continuous** | Ongoing | Production | "Error rate < 0.1%" |

### Fitness Function Examples

#### Example 1: Dependency Direction (Atomic)

**Goal:** Domain layer must not import infrastructure layer (Clean Architecture).

**Go (using import-linter):**
```yaml
# .importlinter
[importlinter:contract:clean-architecture]
name = Domain does not depend on Infrastructure
type = forbidden
source_modules =
    myproject.domain
forbidden_modules =
    myproject.infrastructure
    myproject.adapter
```

**Python (using import-linter):**
```ini
[importlinter:contract:domain-independence]
name = Domain layer is independent
type = forbidden
source_modules =
    myproject.domain
forbidden_modules =
    myproject.infrastructure
    myproject.adapters
```

#### Example 2: API Latency (Holistic)

**Goal:** 95th percentile API response time < 200ms.

```python
# test/fitness/test_api_latency.py
import pytest
from locust import HttpUser, task, between

class APILatencyFitness:
    def test_p95_latency(self):
        """95th percentile API latency must be < 200ms"""
        result = run_load_test(
            endpoint="/api/v1/orders",
            duration="5m",
            users=100
        )
        assert result.p95_latency_ms < 200, \
            f"P95 latency {result.p95_latency_ms}ms exceeds 200ms threshold"

    def test_error_rate(self):
        """Error rate must be < 0.1%"""
        assert result.error_rate < 0.001, \
            f"Error rate {result.error_rate} exceeds 0.1% threshold"
```

#### Example 3: No Circular Dependencies (Triggered)

**Go:**
```bash
# .github/workflows/fitness.yml
- name: Check circular dependencies
  run: |
    go install github.com/fzipp/gocyclo@latest
    gocyclo -over 15 ./... || exit 1

- name: Check architecture boundaries
  run: |
    pip install import-linter
    lint-imports
```

**JavaScript/TypeScript:**
```bash
# package.json
{
  "scripts": {
    "fitness:deps": "madge --circular src/",
    "fitness:coverage": "jest --coverage --coverageThreshold='{\"global\":{\"branches\":80}}'"
  }
}
```

#### Example 4: Database Migration Safety (Triggered)

```python
# test/fitness/test_migrations.py
class MigrationFitness:
    def test_no_destructive_migrations(self):
        """Migrations must not drop columns without deprecation period"""
        for migration in get_pending_migrations():
            assert not migration.has_drop_column(), \
                f"Migration {migration.name} drops column. Use deprecation first."

    def test_migration_runtime(self):
        """Migrations must complete in < 5 seconds"""
        for migration in get_pending_migrations():
            runtime = estimate_migration_runtime(migration)
            assert runtime < 5, \
                f"Migration {migration.name} estimated at {runtime}s. Break into smaller migrations."
```

---

## 2️⃣ Architecture Testing

### Testing Architectural Characteristics ("-ilities")

| Characteristic | Fitness Function | Tool |
|----------------|-----------------|------|
| **Performance** | Response time < X ms under Y load | k6, Locust, Artillery |
| **Scalability** | Throughput scales linearly to N nodes | Custom load tests |
| **Security** | No secrets in code, dependencies scanned | git-secrets, Snyk, Trivy |
| **Maintainability** | Cyclomatic complexity < 15 per function | gocyclo, radon, eslint |
| **Testability** | Code coverage > 80% | pytest, jest, go test |
| **Observability** | All services expose /health and /metrics | Custom validators |
| **Coupling** | No circular dependencies between modules | madge, import-linter |
| **Modularity** | Package cohesion score > threshold | jdepend, structure101 |

### CI/CD Integration

```yaml
# .github/workflows/architecture-fitness.yml
name: Architecture Fitness

on: [pull_request]

jobs:
  fitness:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # 1. Dependency direction
      - name: Check Clean Architecture boundaries
        run: |
          pip install import-linter
          lint-imports

      # 2. Cyclomatic complexity
      - name: Check complexity
        run: |
          go install github.com/fzipp/gocyclo@latest
          gocyclo -over 15 ./...

      # 3. No secrets
      - name: Scan for secrets
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main

      # 4. API latency (if changes touch API)
      - name: Performance regression test
        if: contains(github.event.pull_request.changed_files, 'api/')
        run: |
          docker-compose up -d
          k6 run --summary-trend-stats="avg,min,med,max,p(95),p(99)" tests/performance/api.js

      # 5. Coverage gate
      - name: Test coverage
        run: |
          go test -coverprofile=coverage.out ./...
          go tool cover -func=coverage.out | grep total | awk '{print $3}' | sed 's/%//' | awk '{if ($1 < 80) exit 1}'
```

---

## 3️⃣ Strangler Fig Pattern

**Definition:** Gradually replace a legacy system by building new functionality around it, routing traffic incrementally, until the old system is "strangled" and can be removed.

### Why Strangler Fig?

| Approach | Risk | Time |
|----------|------|------|
| Big Bang Rewrite | Very High | Long |
| Strangler Fig | Low | Gradual |

### Implementation Strategy

```
Phase 1: ROUTE          Phase 2: EXTRACT        Phase 3: STRANGLE
┌─────────────┐        ┌─────────────┐        ┌─────────────┐
│   Client    │        │   Client    │        │   Client    │
└──────┬──────┘        └──────┬──────┘        └──────┬──────┘
       │                      │                      │
       ▼                      ▼                      ▼
┌─────────────┐        ┌─────────────┐        ┌─────────────┐
│  Facade/    │        │  Facade/    │        │   New       │
│  Router     │        │  Router     │        │   Service   │
│  (new)      │        │  (new)      │        │  (full)     │
└──────┬──────┘        └──────┬──────┘        └─────────────┘
       │                      │
       ▼                      ▼
┌─────────────┐        ┌─────────────┐
│   Legacy    │        │   Legacy    │
│   System    │        │   System    │
│  (monolith) │        │  (partial)  │
└─────────────┘        └──────┬──────┘
                              │
                              ▼
                        ┌─────────────┐
                        │   New       │
                        │   Service   │
                        │  (extracted)│
                        └─────────────┘
```

### Routing Strategies

| Strategy | When to Use | Implementation |
|----------|-------------|----------------|
| **URL-based** | Different endpoints | `/api/v2/orders` → new, `/api/v1/orders` → legacy |
| **Feature flag** | Same endpoint, new feature | LaunchDarkly, Unleash: `if (flag.enabled) new() else legacy()` |
| **Canary** | Gradual traffic shift | Route 5% → new, 95% → legacy, increase over time |
| **Data-based** | Different user segments | New users → new system, old users → legacy |

### Example: Feature Flag Router

```go
type OrderRouter struct {
    legacyService *LegacyOrderService
    newService    *NewOrderService
    flags         FeatureFlagClient
}

func (r *OrderRouter) GetOrder(ctx context.Context, id uuid.UUID) (*Order, error) {
    // Check if this user should use new service
    if r.flags.IsEnabled(ctx, "new-order-service", getUserID(ctx)) {
        return r.newService.GetOrder(ctx, id)
    }
    return r.legacyService.GetOrder(ctx, id)
}

func (r *OrderRouter) CreateOrder(ctx context.Context, cmd CreateOrderCommand) (*Order, error) {
    // All new orders go to new service
    return r.newService.CreateOrder(ctx, cmd)
}
```

---

## 4️⃣ Architectural Dimensions

Identify which dimensions of your architecture need to evolve:

```
┌─────────────────────────────────────────────────────────────┐
│                    ARCHITECTURAL DIMENSIONS                  │
│                                                              │
│  Technical          Business           Operational          │
│  ─────────          ────────           ───────────          │
│  • Tech stack       • Features         • Scalability        │
│  • Data storage     • Domain model     • Performance        │
│  • Communication    • Business rules   • Security           │
│  • Integration      • Regulations      • Observability      │
│                                                              │
│  Each dimension needs:                                       │
│  1. Current state measurement                                │
│  2. Target state definition                                  │
│  3. Fitness function to guard it                             │
└─────────────────────────────────────────────────────────────┘
```

### Dimension Example: Scalability

| Metric | Current | Target | Fitness Function |
|--------|---------|--------|-----------------|
| Orders/second | 100 | 1000 | Load test: sustain 1000 orders/sec for 5 min |
| Database connections | 50 | 200 | Monitor: alert at 150 connections |
| Cache hit rate | 60% | 85% | Monitor: alert if < 80% for 1 hour |

---

## 5️⃣ Conway's Law & Team Alignment

> "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." — Melvin Conway

### Implications

| Team Structure | Architecture Result |
|---------------|---------------------|
| One big team | Monolith (natural) |
| Frontend + Backend teams | Frontend/Backend split |
| Feature teams (cross-functional) | Vertical slices, microservices |
| Platform + Product teams | Platform + product services |

### Team Topologies Mapping

| Team Type | Owns | Architecture |
|-----------|------|-------------|
| **Stream-aligned** | One business capability | One Bounded Context / Service |
| **Platform** | Internal tools, infrastructure | Platform services, shared libraries |
| **Complicated Subsystem** | Complex domain (ML, security) | Specialized service |
| **Enabling** | Temporary expertise injection | No permanent ownership |

---

## 🚫 Evolutionary Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Fitness Function Theater** | Tests exist but never fail | Make them fail intentionally to verify they work |
| **Ignoring Failures** | Fitness fails, but PR merges anyway | Block merge on fitness failure |
| **Too Many Dimensions** | 50 fitness functions, team overwhelmed | Start with 3-5 most critical |
| **Static Architecture** | No changes in 6 months | Architecture should evolve; stasis is a smell |
| **Wrong Coupling** | Services chatty across team boundaries | Reorganize teams or service boundaries |
| **Premature Extraction** | Microservices at 3-person startup | Start monolith, extract when pain appears |

---

## 📋 Evolutionary Architecture Checklist

When starting a new project:

- [ ] Identified 3-5 critical architectural dimensions
- [ ] Defined fitness functions for each dimension
- [ ] Integrated fitness functions into CI/CD
- [ ] Chose appropriate coupling (monolith → modular → microservices)
- [ ] Aligned team structure with architecture boundaries
- [ ] Planned strangler fig path for legacy integration (if applicable)
- [ ] Documented architecture decisions in ADRs

---

## 🔗 Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `c4-model` | C4 diagrams show current architecture; fitness functions verify it |
| `ddd-core` | Bounded Contexts = natural architectural quantum boundaries |
| `architecture-decision-records` | ADRs document "why" for each evolutionary step |
| `dora-core` | Deployment Frequency + Lead Time = incremental change velocity |

---

## 📚 References

- [Evolutionary Architecture](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/) — Neal Ford, Rebecca Parsons, Pat Kua (O'Reilly)
- [Software Architecture: The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/) — Ford, Richards, Sadalage, Dehghani
- [Fitness Function-Driven Development](https://www.thoughtworks.com/insights/articles/fitness-function-driven-development) — ThoughtWorks
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) — Martin Fowler
- [Team Topologies](https://teamtopologies.com/) — Skelton, Pais
- [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html) — Martin Fowler
