---
name: clean-architecture
description: Apply Clean Architecture principles (Dependency Rule, layers, boundaries) to design maintainable, testable systems. Use when structuring code, defining component boundaries, or choosing between layered/hexagonal/onion architectures. Maps to C4 Model L3 Components and DDD Tactical patterns.
metadata:
  tags: ["clean-architecture", "dependency-rule", "hexagonal-architecture", "onion-architecture", "ports-and-adapters", "layered-architecture", "boundaries", "use-cases", "testability"]
---

# Clean Architecture

**Separate stable business rules from volatile technical details.**

Clean Architecture, formalized by Robert C. Martin (Uncle Bob) in *Clean Architecture: A Craftsman's Guide to Software Structure and Design* (2017), is an evolution of Layered Architecture, Hexagonal Architecture (Alistair Cockburn, 2005), and Onion Architecture (Jeffrey Palermo). It provides a set of principles for organizing code so that business logic remains independent of frameworks, UI, and databases.

> "The goal of software architecture is to minimize the human resources required to build and maintain the required system." — Robert C. Martin

---

## 1. The Dependency Rule

**Source code dependencies must always point inward, toward higher-level policies, never outward toward lower-level details.**

```
┌─────────────────────────────────────────────────────────────┐
│                    OUTER LAYERS (Details)                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Frameworks & Drivers                                │   │
│  │  (React, FastAPI, gRPC, PostgreSQL, Redis, AWS)     │   │
│  │  ▲                                                  │   │
│  │  │ depends on                                       │   │
│  │  ▼                                                  │   │
│  │  Interface Adapters                                  │   │
│  │  (Controllers, Presenters, Gateways, Repositories)  │   │
│  │  ▲                                                  │   │
│  │  │ depends on                                       │   │
│  │  ▼                                                  │   │
│  │  Application Business Rules                          │   │
│  │  (Use Cases, Interactors, Application Services)     │   │
│  │  ▲                                                  │   │
│  │  │ depends on                                       │   │
│  │  ▼                                                  │   │
│  │  Enterprise Business Rules                           │   │
│  │  (Entities, Domain Objects, Value Objects)          │   │
│  └─────────────────────────────────────────────────────┘   │
│                    INNER LAYERS (Policies)                   │
└─────────────────────────────────────────────────────────────┘
```

**Key implication:** The inner circles (Entities, Use Cases) know **nothing** about the outer circles. They don't import framework libraries, don't know about the database, don't depend on the HTTP layer.

---

## 2. The Four Layers

### Layer 1: Entities (Enterprise Business Rules)

**What:** Core business objects that encapsulate the most general and high-level rules.

**Characteristics:**
- Independent of the application — could be shared across multiple apps in the same domain
- Contain business logic that would exist even without this specific application
- Plain objects, no framework dependencies

```typescript
// entity/Order.ts — pure business logic, no framework imports
export class Order {
  private constructor(
    private readonly id: string,
    private items: OrderItem[],
    private status: OrderStatus
  ) {}

  static create(items: OrderItem[]): Order {
    return new Order(crypto.randomUUID(), items, OrderStatus.PENDING);
  }

  addItem(item: OrderItem): void {
    if (this.status !== OrderStatus.PENDING) {
      throw new DomainError('Cannot modify a submitted order');
    }
    this.items.push(item);
  }

  submit(): void {
    if (this.items.length === 0) {
      throw new DomainError('Cannot submit empty order');
    }
    this.status = OrderStatus.SUBMITTED;
  }

  getTotal(): Money {
    return this.items.reduce(
      (sum, item) => sum.add(item.price.multiply(item.quantity)),
      Money.zero()
    );
  }
}
```

### Layer 2: Use Cases (Application Business Rules)

**What:** Application-specific business rules. Orchestrate the flow of data to and from entities.

**Characteristics:**
- One Use Case = one user story / one JTBD outcome
- Contains NO framework code
- Depends only on Entities and interfaces (ports) defined in the same layer

```typescript
// usecase/SubmitOrder.ts
import { Order } from '../entity/Order';
import { OrderRepository } from './port/OrderRepository';
import { PaymentGateway } from './port/PaymentGateway';
import { NotificationService } from './port/NotificationService';

export interface SubmitOrderInput {
  orderId: string;
  paymentMethod: PaymentMethod;
}

export interface SubmitOrderOutput {
  success: boolean;
  transactionId?: string;
  error?: string;
}

export class SubmitOrderUseCase {
  constructor(
    private orderRepo: OrderRepository,
    private paymentGateway: PaymentGateway,
    private notifier: NotificationService
  ) {}

  async execute(input: SubmitOrderInput): Promise<SubmitOrderOutput> {
    const order = await this.orderRepo.findById(input.orderId);
    if (!order) {
      return { success: false, error: 'Order not found' };
    }

    order.submit();

    const payment = await this.paymentGateway.charge(
      order.getTotal(),
      input.paymentMethod
    );

    if (!payment.success) {
      return { success: false, error: payment.error };
    }

    await this.orderRepo.save(order);
    await this.notifier.sendOrderConfirmation(order);

    return { success: true, transactionId: payment.transactionId };
  }
}
```

### Layer 3: Interface Adapters

**What:** Convert data from the format most convenient for Use Cases and Entities, to the format most convenient for external agencies (frameworks, UI, database).

**Characteristics:**
- Controllers handle HTTP requests
- Presenters format responses
- Repositories implement data access interfaces
- Gateways wrap external APIs

```typescript
// adapter/controller/OrderController.ts
import { SubmitOrderUseCase } from '../../usecase/SubmitOrder';

export class OrderController {
  constructor(private submitOrder: SubmitOrderUseCase) {}

  async handleSubmit(req: HttpRequest): Promise<HttpResponse> {
    const result = await this.submitOrder.execute({
      orderId: req.body.orderId,
      paymentMethod: req.body.paymentMethod
    });

    if (!result.success) {
      return { status: 400, body: { error: result.error } };
    }

    return { status: 200, body: { transactionId: result.transactionId } };
  }
}
```

```typescript
// adapter/repository/PostgresOrderRepository.ts
import { OrderRepository } from '../../usecase/port/OrderRepository';

export class PostgresOrderRepository implements OrderRepository {
  constructor(private db: Knex) {}

  async findById(id: string): Promise<Order | null> {
    const row = await this.db('orders').where({ id }).first();
    return row ? this.toEntity(row) : null;
  }

  async save(order: Order): Promise<void> {
    await this.db('orders')
      .insert(this.toRow(order))
      .onConflict('id')
      .merge();
  }

  private toEntity(row: OrderRow): Order { /* ... */ }
  private toRow(order: Order): OrderRow { /* ... */ }
}
```

### Layer 4: Frameworks & Drivers

**What:** The outermost layer — frameworks, tools, and delivery mechanisms.

**Characteristics:**
- React, Vue, Next.js (UI)
- Fastify, Express, FastAPI (HTTP)
- PostgreSQL, MongoDB, Redis (Database)
- AWS, GCP, Azure (Infrastructure)
- This layer contains **only glue code** — wiring dependencies together

```typescript
// main.ts — composition root, only place where framework imports exist
import fastify from 'fastify';
import knex from 'knex';
import { OrderController } from './adapter/controller/OrderController';
import { SubmitOrderUseCase } from './usecase/SubmitOrder';
import { PostgresOrderRepository } from './adapter/repository/PostgresOrderRepository';
import { StripePaymentGateway } from './adapter/gateway/StripePaymentGateway';
import { EmailNotificationService } from './adapter/service/EmailNotificationService';

const app = fastify();
const db = knex({ client: 'pg', connection: process.env.DATABASE_URL });

// Wire dependencies — this is the ONLY place outer layers connect
const orderRepo = new PostgresOrderRepository(db);
const paymentGateway = new StripePaymentGateway(process.env.STRIPE_KEY);
const notifier = new EmailNotificationService();
const submitOrder = new SubmitOrderUseCase(orderRepo, paymentGateway, notifier);
const orderController = new OrderController(submitOrder);

app.post('/orders/:id/submit', orderController.handleSubmit.bind(orderController));
```

---

## 3. Ports and Adapters (Hexagonal Architecture)

Clean Architecture is conceptually equivalent to **Hexagonal Architecture** (Alistair Cockburn). The terminology differs:

| Clean Architecture | Hexagonal / Ports & Adapters | Meaning |
|---|---|---|
| Use Case | Application Service | Orchestrates business flow |
| Interface Adapter | Adapter | Bridges between app and external world |
| Port (implicit) | Port | Interface defined by the application, implemented by adapter |
| Entity | Domain Model | Core business logic |

```
                    ┌─────────────────┐
                    │   HTTP Client   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  HTTP Adapter   │ ←── Driver Adapter
                    │  (Controller)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │              ┌─────▼─────┐              │
        │              │           │              │
        │   ┌──────────┤  Port     ├──────────┐   │
        │   │          │ (interface)│          │   │
        │   │          └───────────┘          │   │
        │   │                                 │   │
        │   │    ┌───────────────────────┐    │   │
        │   │    │    APPLICATION        │    │   │
        │   │    │  ┌─────────────────┐  │    │   │
        │   │    │  │   Use Cases     │  │    │   │
        │   │    │  └─────────────────┘  │    │   │
        │   │    │  ┌─────────────────┐  │    │   │
        │   │    │  │    Entities     │  │    │   │
        │   │    │  └─────────────────┘  │    │   │
        │   │    └───────────────────────┘    │   │
        │   │                                 │   │
        │   │          ┌───────────┐          │   │
        │   │          │   Port    │          │   │
        │   │          │(interface)│          │   │
        │   │          └─────┬─────┘          │   │
        │   │                │                │   │
        │   └────────────────┼────────────────┘   │
        │                    │                    │
        │           ┌────────▼────────┐           │
        │           │  DB Adapter     │ ←── Driven Adapter
        │           │ (Repository)    │
        │           └────────┬────────┘           │
        │                    │                    │
        │           ┌────────▼────────┐           │
        │           │   PostgreSQL    │           │
        │           └─────────────────┘           │
        └─────────────────────────────────────────┘
```

**Key rule:** The application defines **ports** (interfaces). Adapters implement them. The application never knows which adapter is plugged in.

---

## 4. Boundaries and Crossing Them

### The Boundary Crossing Rule

**Data structures crossing boundaries must be simple, serializable DTOs — never framework-specific types.**

```typescript
// ❌ BAD: Framework type leaks into Use Case
class SubmitOrderUseCase {
  async execute(req: FastifyRequest): Promise<FastifyReply> { // ❌
    // ...
  }
}

// ✅ GOOD: Plain DTO in, plain DTO out
interface SubmitOrderInput {
  orderId: string;
  paymentMethod: PaymentMethod;
}

interface SubmitOrderOutput {
  success: boolean;
  transactionId?: string;
}

class SubmitOrderUseCase {
  async execute(input: SubmitOrderInput): Promise<SubmitOrderOutput> {
    // ... pure business logic
  }
}
```

### Boundary Types

| Boundary | What it separates | Example |
|---|---|---|
| **Use Case → Entity** | App logic ↔ Domain logic | Use Case calls `order.submit()` |
| **Adapter → Use Case** | Framework ↔ App logic | Controller calls Use Case |
| **Adapter → External** | App ↔ Database/API | Repository calls PostgreSQL |
| **Process Boundary** | Different deployable units | gRPC/HTTP between services |

---

## 5. Package by Component (Simon Brown)

Simon Brown, creator of C4 Model, contributed "The Missing Chapter" to Uncle Bob's *Clean Architecture* book. His key insight:

> **Organize code by component, not by layer.**

### Package by Layer (Anti-pattern)

```
src/
  controllers/     ← All controllers
  services/        ← All services
  repositories/    ← All repositories
  models/          ← All entities
```

**Problem:** Business logic scattered across layers. High coupling. Hard to find related code.

### Package by Feature (Better)

```
src/
  order/
    controller.ts
    service.ts
    repository.ts
    model.ts
  user/
    controller.ts
    service.ts
    repository.ts
    model.ts
```

**Problem:** Still no encapsulation — `user/service.ts` can import `order/model.ts` directly.

### Package by Component (Recommended)

```
src/
  order/
    index.ts              ← Public API: OrderService, Order, OrderRepository
    internal/
      OrderEntity.ts      ← Entities (private)
      SubmitOrder.ts      ← Use Case (private)
      OrderController.ts  ← Adapter (private)
      PostgresOrderRepo.ts ← Adapter (private)
  user/
    index.ts              ← Public API: UserService, User, UserRepository
    internal/
      ...
```

**Benefits:**
- Each component is self-contained
- Public API surface is small and intentional
- Internal structure can change without affecting other components
- Maps directly to **C4 L3 Components**

---

## 6. Clean Architecture + C4 Model Integration

| C4 Level | Clean Architecture Layer | What to Draw |
|---|---|---|
| **L1 System Context** | System boundary | External actors, other systems |
| **L2 Containers** | Deployable units | Web app, API service, database, message queue |
| **L3 Components** | Package by Component | Order component, User component, Payment component |
| **L4 Code** | Classes inside component | Entities, Use Cases, Repositories, Controllers |

**Workflow:**
```
1. C4 L1 → Define system scope and external dependencies
2. C4 L2 → Identify containers (deployable units)
3. Clean Architecture → Design component boundaries within each container
4. C4 L3 → Draw components as self-contained packages
5. Clean Architecture → Implement: Entities → Use Cases → Adapters
6. C4 L4 → Document complex Entities with UML class diagrams
```

---

## 7. Clean Architecture + DDD Integration

| Clean Architecture | DDD Tactical | Relationship |
|---|---|---|
| **Entity** | **Aggregate Root / Entity** | Same concept — encapsulates business rules |
| **Value Object** | **Value Object** | Identical — immutable, compared by value |
| **Use Case** | **Application Service** | Orchestrates domain operations |
| **Repository (port)** | **Repository** | Abstracts persistence |
| **Domain Service** | **Domain Service** | Cross-aggregate business logic |
| **Interface Adapter** | **Infrastructure Layer** | Implements ports with concrete technology |

**Key difference:**
- **DDD** focuses on *discovering* the domain model (Event Storming, Ubiquitous Language)
- **Clean Architecture** focuses on *structuring* the code to protect that model from technical details

**Best practice:** Use DDD to discover the model, then use Clean Architecture to implement it.

---

## 8. Testing Strategy

Clean Architecture enables a **testing pyramid** without integration tests for every case:

```
         ┌─────────┐
         │   E2E   │  ← 1-2 tests: happy path through HTTP + DB
         │  (slow) │
         └────┬────┘
              │
         ┌────▼────┐
         │ Adapter │  ← Mock the port, test adapter logic
         │  Tests  │
         └────┬────┘
              │
         ┌────▼────┐
         │  Use    │  ← Mock repositories, test business flow
         │  Case   │
         │  Tests  │
         └────┬────┘
              │
         ┌────▼────┐
         │ Entity  │  ← Pure unit tests, no mocks needed
         │  Tests  │     Fastest, most comprehensive
         └─────────┘
```

```typescript
// Entity test — pure, fast, no mocks
import { Order } from './Order';

describe('Order', () => {
  it('cannot submit empty order', () => {
    const order = Order.create([]);
    expect(() => order.submit()).toThrow('Cannot submit empty order');
  });

  it('calculates total correctly', () => {
    const order = Order.create([
      { productId: '1', price: Money.of(10), quantity: 2 },
      { productId: '2', price: Money.of(5), quantity: 3 }
    ]);
    expect(order.getTotal()).toEqual(Money.of(35));
  });
});

// Use Case test — mock ports, test orchestration
import { SubmitOrderUseCase } from './SubmitOrder';

describe('SubmitOrderUseCase', () => {
  it('charges payment and confirms order', async () => {
    const orderRepo = { findById: vi.fn(), save: vi.fn() };
    const paymentGateway = { charge: vi.fn() };
    const notifier = { sendOrderConfirmation: vi.fn() };

    const useCase = new SubmitOrderUseCase(orderRepo, paymentGateway, notifier);
    const result = await useCase.execute({ orderId: '123', paymentMethod: 'card' });

    expect(result.success).toBe(true);
    expect(paymentGateway.charge).toHaveBeenCalled();
    expect(notifier.sendOrderConfirmation).toHaveBeenCalled();
  });
});
```

---

## 9. Anti-Patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Framework in Entities** | Entity imports `mongoose`, `typeorm`, `@prisma/client` | Extract ORM schema to adapter layer. Entity stays pure. |
| **Use Case calls HTTP** | Use Case imports `axios`, `fetch` | Create Gateway port + adapter. Use Case depends on interface. |
| **God Use Case** | One Use Case handles 5+ different flows | Split into smaller, focused Use Cases. One per user story. |
| **Leaky Repository** | Repository returns ORM entities instead of domain entities | Repository maps ORM → Domain Entity before returning. |
| **Missing Ports** | Direct instantiation of adapters in Use Cases | Define interfaces (ports) in Use Case layer, inject implementations. |
| **Anemic Domain Model** | Entities are just data bags with getters/setters | Push business logic into Entities. Use Cases only orchestrate. |

---

## 10. Decision Framework

**When to use Clean Architecture:**

```
Complex business logic? ──→ YES ──→ Use Clean Architecture
    │
    └──→ NO ──→ Simple CRUD? ──→ YES ──→ Simple layered / MVC is fine
                  │
                  └──→ NO ──→ Prototype / MVP? ──→ YES ──→ Start simple,
                                                          refactor later
```

**When Clean Architecture is overkill:**
- Simple CRUD applications with no complex business rules
- Prototypes / throwaway code
- Scripts and CLI tools
- Simple static sites

---

## Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| Code structure | `c4-model` | Visualize components at L3 |
| Domain modeling | `ddd-tactical` | Aggregates, Entities, Value Objects |
| Strategic boundaries | `ddd-core` | Bounded Contexts map to L2 Containers |
| Delivery speed | `dora-core` | Loosely coupled components = high DF |
| Testing strategy | `javascript-typescript` | Vitest, testing patterns |
| Python backend | `python-development` | FastAPI + Clean Architecture |
| Go backend | `golang-development` | Go + Clean Architecture patterns |

---

## References

- [Clean Architecture](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164) — Robert C. Martin (2017)
- [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) — Alistair Cockburn (2005)
- [C4 Model](https://c4model.com/) — Simon Brown
- [Package by Component](http://www.codingthearchitecture.com/2015/03/08/package_by_component_and_architecturally_aligned_testing.html) — Simon Brown
- [The Clean Code Blog](https://blog.cleancoder.com/) — Robert C. Martin
