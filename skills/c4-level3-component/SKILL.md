---
description: Specialized in Component diagrams (Level 3) with folder structure mapping.
  Use this skill when the user needs to zoom into a single container to identify internal
  components, their responsibilities, and how they map to actual code folders (src/services,
  internal/).
metadata:
  tags:
  - architecture
  - c4-level3
  - components
  - code-structure
  - clean-architecture
  version: 1.0.0
name: c4-level3-component
---

# C4 Level 3: Component Diagram & Folder Mapping

Level 3 focuses on the **internal architecture** of a single container, bridging the gap between high-level containers and low-level code. This is where architecture patterns (Clean, Hexagonal, Onion, Vertical Slice) become visible.

> "A component is a grouping of related functionality behind a well-defined interface." — Simon Brown

---

## 🎯 Stakeholder Focus

| Stakeholder | What they need from L3 | Questions they ask |
|-------------|------------------------|-------------------|
| **Developers** | Module boundaries, where to add new code | "Where does the payment logic go?" |
| **Tech Leads** | Layering, Separation of Concerns | "Is our dependency direction correct?" |
| **Architects** | Design consistency, pattern adherence | "Are we following Clean Architecture?" |
| **New Hires** | Onboarding, codebase navigation | "How is this container organized?" |

---

## 🏗️ Architecture Patterns & Component Mapping

### Pattern 1: Layered Architecture (Traditional)

```
┌─────────────────────────────────────────┐
│  Presentation Layer                     │
│  ├─ Controller/Handler                  │
│  └─ DTO/ViewModel                       │
├─────────────────────────────────────────┤
│  Business Logic Layer                   │
│  ├─ Service                             │
│  └─ Domain Model (Entity, VO)           │
├─────────────────────────────────────────┤
│  Data Access Layer                      │
│  ├─ Repository                          │
│  └─ ORM/Data Mapper                     │
└─────────────────────────────────────────┘
```

**Folder Mapping:**
```
src/
├── api/              → Presentation (controllers, handlers)
├── services/         → Business Logic (application services)
├── domain/           → Domain Model (entities, value objects)
├── repositories/     → Data Access (repository interfaces + implementations)
└── dto/              → Data Transfer Objects
```

### Pattern 2: Clean Architecture (Robert C. Martin)

```
         ┌─────────────┐
         │  Frameworks │  ← Outer: UI, DB, External APIs
         │  & Drivers  │
         └──────┬──────┘
                │ depends on
         ┌──────┴──────┐
         │  Interface  │  ← Adapters: Controllers, Presenters, Gateways
         │   Adapters  │
         └──────┬──────┘
                │ depends on
         ┌──────┴──────┐
         │  Use Cases  │  ← Application Business Rules
         │  (Services) │
         └──────┬──────┘
                │ depends on
         ┌──────┴──────┐
         │   Entities  │  ← Enterprise Business Rules (innermost)
         └─────────────┘
```

**Dependency Rule:** Dependencies point INWARD only. Inner circles know nothing about outer circles.

**Folder Mapping (Go example):**
```
internal/
├── domain/           → Entities (pure business logic, no dependencies)
│   ├── order.go
│   └── value_objects.go
├── usecase/          → Use Cases (application services)
│   ├── place_order.go
│   └── cancel_order.go
├── interface/        → Adapters (driven + driving)
│   ├── controller/   → HTTP handlers
│   ├── presenter/    → Response formatters
│   └── gateway/      → External API clients
└── infrastructure/   → Frameworks (DB, cache, message queue)
    ├── repository/   → DB implementations
    └── messaging/    → Event publishers
```

### Pattern 3: Hexagonal Architecture (Ports & Adapters)

```
              ┌──────────────┐
    ┌─────────│   Driving    │─────────┐
    │         │   Adapters   │         │
    │  HTTP   │  (Primary)   │  CLI    │
    │ Handler │              │ Tool    │
    └────┬────┴──────────────┴────┬────┘
         │                        │
         │    ┌──────────────┐    │
         └───▶│   Application │◀───┘
              │   Core (Domain)│
              │               │
         ┌───▶│   Ports       │◀───┐
         │    └──────────────┘    │
    ┌────┴────┬──────────────┬────┴────┐
    │  DB     │   External   │ Message │
    │ Adapter │   API Client │ Queue   │
    │(Driven) │   (Driven)   │Adapter  │
    └─────────┴──────────────┴─────────┘
         Driven Adapters (Secondary)
```

**Key Concepts:**
- **Port:** Interface defining what the application needs (driven) or provides (driving)
- **Adapter:** Implementation of a port for a specific technology
- **Domain:** Pure business logic, zero external dependencies

**Folder Mapping:**
```
src/
├── application/          → Use cases, domain services
│   ├── port/
│   │   ├── in/          → Driving ports (interfaces app exposes)
│   │   └── out/         → Driven ports (interfaces app needs)
│   └── service/
├── domain/              → Entities, value objects, domain events
└── adapter/
    ├── in/              → Driving adapters (HTTP, CLI, messaging)
    │   ├── web/
    │   └── cli/
    └── out/             → Driven adapters (DB, external APIs)
        ├── persistence/
        └── external/
```

### Pattern 4: Vertical Slice Architecture

```
src/
├── features/
│   ├── place_order/          → One folder per feature
│   │   ├── handler.go        → HTTP handler
│   │   ├── command.go        → CQRS command
│   │   ├── validator.go      → Input validation
│   │   ├── service.go        → Business logic
│   │   ├── repository.go     → Data access
│   │   └── dto.go            → Request/response types
│   │
│   ├── cancel_order/
│   │   ├── handler.go
│   │   ├── command.go
│   │   └── ...
│   │
│   └── list_orders/
│       ├── handler.go
│       ├── query.go          → CQRS query
│       └── ...
│
└── shared/                   → Cross-cutting concerns
    ├── middleware/
    ├── auth/
    └── logging/
```

**Principle:** Each feature is self-contained. No horizontal layers. Changes to "Place Order" only touch `features/place_order/`.

---

## 📝 Mermaid Templates

### Template A: Layered Architecture (API Service)
```mermaid
C4Component
    title Component Diagram for API Service

    Container(spa, "Web App", "React/TS", "Customer SPA")

    Container_Boundary(api, "API Service") {
        Component(auth_ctrl, "Auth Controller", "Go Handler", "Handles login, registration, token refresh.")
        Component(order_ctrl, "Order Controller", "Go Handler", "Handles order CRUD operations.")

        Component(auth_svc, "Auth Service", "Go", "Validates credentials, generates JWTs.")
        Component(order_svc, "Order Service", "Go", "Business logic for order lifecycle.")
        Component(payment_svc, "Payment Service", "Go", "Orchestrates payment processing.")

        Component(auth_repo, "Auth Repository", "SQL Client", "User persistence.")
        Component(order_repo, "Order Repository", "SQL Client", "Order persistence.")
        Component(payment_client, "Payment Client", "HTTP Client", "Stripe API integration.")

        Component(jwt_util, "JWT Utility", "Go", "Token generation and validation.")
        Component(event_pub, "Event Publisher", "Go", "Publishes domain events.")
    }

    ContainerDb(db, "Database", "PostgreSQL", "Primary data store.")
    System_Ext(stripe, "Stripe", "Payment processing.")

    Rel(spa, auth_ctrl, "POST /login", "JSON/HTTPS")
    Rel(spa, order_ctrl, "POST /orders", "JSON/HTTPS")

    Rel(auth_ctrl, auth_svc, "Calls", "Method call")
    Rel(order_ctrl, order_svc, "Calls", "Method call")

    Rel(auth_svc, auth_repo, "Uses", "Method call")
    Rel(auth_svc, jwt_util, "Uses", "Method call")
    Rel(order_svc, order_repo, "Uses", "Method call")
    Rel(order_svc, payment_svc, "Uses", "Method call")
    Rel(payment_svc, payment_client, "Uses", "Method call")
    Rel(order_svc, event_pub, "Uses", "Method call")

    Rel(auth_repo, db, "Reads/Writes", "SQL/TCP")
    Rel(order_repo, db, "Reads/Writes", "SQL/TCP")
    Rel(payment_client, stripe, "API calls", "REST/HTTPS")
```

### Template B: Clean Architecture (Go)
```mermaid
C4Component
    title Component Diagram — Clean Architecture (Order Service)

    Container(spa, "Web App", "React", "Customer UI")

    Container_Boundary(order_service, "Order Service (Clean Arch)") {
        Component(handler, "HTTP Handler", "Go", "Adapter: converts HTTP to use case input.")
        Component(presenter, "JSON Presenter", "Go", "Adapter: formats use case output.")

        Component(place_order_uc, "Place Order Use Case", "Go", "Application: orchestrates order creation.")
        Component(cancel_order_uc, "Cancel Order Use Case", "Go", "Application: handles cancellation.")

        Component(order_entity, "Order Entity", "Go", "Domain: order business rules.")
        Component(order_repo_intf, "Order Repository (Interface)", "Go", "Domain: port for persistence.")
        Component(payment_intf, "Payment Gateway (Interface)", "Go", "Domain: port for payments.")

        Component(order_repo_impl, "Order Repository (Impl)", "Go + SQL", "Infrastructure: PostgreSQL adapter.")
        Component(stripe_adapter, "Stripe Adapter", "Go + HTTP", "Infrastructure: Stripe API adapter.")
    }

    ContainerDb(db, "Order DB", "PostgreSQL")
    System_Ext(stripe, "Stripe API")

    Rel(spa, handler, "POST /orders", "JSON/HTTPS")
    Rel(handler, place_order_uc, "Invokes", "Method call")
    Rel(place_order_uc, order_entity, "Creates", "Method call")
    Rel(place_order_uc, order_repo_intf, "Saves via", "Interface")
    Rel(place_order_uc, payment_intf, "Charges via", "Interface")

    Rel(order_repo_intf, order_repo_impl, "Implemented by", "Dependency Injection")
    Rel(payment_intf, stripe_adapter, "Implemented by", "Dependency Injection")

    Rel(order_repo_impl, db, "SQL queries", "TCP")
    Rel(stripe_adapter, stripe, "API calls", "HTTPS")
```

---

## 🛠 Folder Structure Mapping by Language

### Go (Clean Architecture)
```
internal/
├── domain/
│   ├── entity/
│   │   └── order.go
│   ├── valueobject/
│   │   └── money.go
│   └── event/
│       └── order_placed.go
├── usecase/
│   ├── place_order.go
│   └── cancel_order.go
├── adapter/
│   ├── in/
│   │   └── http/
│   │       └── order_handler.go
│   └── out/
│       ├── persistence/
│       │   └── order_repository.go
│       └── payment/
│           └── stripe_adapter.go
└── config/
    └── app.go
```

### Python (Hexagonal / FastAPI)
```
src/
├── domain/
│   ├── models/
│   │   └── order.py
│   ├── value_objects/
│   │   └── money.py
│   └── events/
│       └── order_placed.py
├── application/
│   ├── ports/
│   │   ├── in/
│   │   │   └── order_use_case.py
│   │   └── out/
│   │       ├── order_repository.py
│   │       └── payment_gateway.py
│   └── services/
│       └── order_service.py
├── adapters/
│   ├── in/
│   │   └── web/
│   │       └── order_router.py
│   └── out/
│       ├── persistence/
│       │   └── sqlalchemy_order_repo.py
│       └── payment/
│           └── stripe_client.py
└── main.py
```

### TypeScript (Vertical Slice / NestJS-style)
```
src/
├── features/
│   ├── orders/
│   │   ├── orders.module.ts
│   │   ├── place-order/
│   │   │   ├── place-order.handler.ts
│   │   │   ├── place-order.command.ts
│   │   │   └── place-order.dto.ts
│   │   ├── cancel-order/
│   │   │   └── ...
│   │   └── list-orders/
│   │       └── ...
│   └── payments/
│       └── ...
├── shared/
│   ├── decorators/
│   ├── filters/
│   └── guards/
└── main.ts
```

---

## 🚫 Anti-Patterns to Guard (Level 3)

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Over-Detailing** | Every class drawn | Only major logical groupings (5-15 components) |
| **Mixing Containers** | Components from multiple containers | Focus on ONE container per diagram |
| **Circular Dependencies** | A→B→C→A cycle | Refactor: extract shared interface, merge, or restructure |
| **Anemic Components** | Component with no clear responsibility | Rename to reflect single responsibility |
| **Layer Violation** | Domain imports infrastructure | In Clean/Hexagonal: domain must have zero external deps |
| **God Component** | One component handles everything | Split by responsibility or feature |

---

## 🔍 Codebase Scanning (L3 Synthesis)

```bash
# Identify component boundaries by folder structure
find src -type d -maxdepth 2 | sort

# Look for architecture patterns
grep -r "interface\|abstract class\|port\|adapter" src/ --include="*.go" --include="*.ts" --include="*.py"

# Check dependency direction (domain should not import infrastructure)
# In Go: check go.mod or import paths
grep -r "infrastructure\|adapter\|external" internal/domain/ || echo "✅ Clean: domain has no infra imports"

# Find circular dependencies
# Go: use golang.org/x/tools/cmd/depgraph or go mod graph
# Python: use pipdeptree or import-linter
# TypeScript: use madge
```

---

## ✅ Level 3 Success Criteria

- [ ] Does the diagram map directly to the container's folder structure?
- [ ] Are internal interactions (method calls/internal events) clearly labeled?
- [ ] Is it clear how each component contributes to the container's responsibility?
- [ ] **STRICT:** Does it focus only on the zoomed-in container?
- [ ] **STRICT:** Are there ≤15 components?
- [ ] Does the dependency direction follow the chosen architecture pattern?
- [ ] Are circular dependencies identified and resolved?

---

## 🔄 From L3 to L4

| L3 Signal | L4 Action |
|-----------|-----------|
| "This component has complex internal logic" | UML class diagram |
| "The data model is hard to understand" | ERD (Entity Relationship Diagram) |
| "New developers struggle with this module" | Document key classes and their relationships |
| "We need to refactor this component" | L4 reveals exact coupling points |

**Next:** Use `c4-level4-code` for implementation details.

---

## 📚 References

- [C4 Model — Component Diagram](https://c4model.com/#ComponentDiagram) — Simon Brown
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) — Robert C. Martin
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — Alistair Cockburn
- [Vertical Slice Architecture](https://jimmybogard.com/vertical-slice-architecture/) — Jimmy Bogard
