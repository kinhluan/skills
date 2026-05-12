---
name: ddd-patterns
description: Advanced Domain-Driven Design (DDD) Integration Patterns. Use this skill for implementing CQRS, Event Sourcing, the Outbox Pattern, and Anti-Corruption Layers (ACL) in distributed systems.
metadata:
  tags: ["ddd", "advanced-patterns", "cqrs", "event-sourcing", "outbox", "saga", "distributed-systems"]
---

# Domain-Driven Design (DDD): Advanced Patterns

Advanced integration patterns for handling complex distributed system interactions, data consistency, and cross-boundary communication. Use these patterns when a single Bounded Context's tactical patterns are insufficient.

> "Distributed systems are different. If we don't know that, we are building them wrong." — Udi Dahan

---

## 🧭 When to Use Advanced Patterns

| Situation | Pattern(s) | Complexity |
|-----------|-----------|------------|
| Read model needs different shape than write model | **CQRS** | Medium |
| Need full audit trail of all state changes | **Event Sourcing** | High |
| Need atomic DB + message broker consistency | **Outbox** | Medium |
| Long-running business process across contexts | **Saga** | High |
| External system has incompatible model | **ACL** | Medium |
| High read load, simple queries | **CQRS + Read Model** | Medium |

**Warning:** These patterns add significant complexity. Don't use them unless you have a clear problem they solve.

---

## 1️⃣ CQRS (Command Query Responsibility Segregation)

**Definition:** Separate the read (Query) model from the write (Command) model. Each is optimized for its purpose.

### Why CQRS?

| Aspect | Traditional CRUD | CQRS |
|--------|-----------------|------|
| Read model | Same as write model | Optimized for queries (denormalized) |
| Write model | Same as read model | Optimized for business rules (normalized) |
| Schema | Single schema | Separate schemas per model |
| Scaling | Scale together | Scale independently |

### Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Command   │────▶│  Command    │
│             │     │   API       │     │  Handler    │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │  Write DB   │
                                        │ (Normalized)│
                                        │ PostgreSQL  │
                                        └──────┬──────┘
                                               │
                                               │ Events
                                               ▼
                                        ┌─────────────┐
                                        │  Event Bus  │
                                        │   (Kafka)   │
                                        └──────┬──────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │◀────│   Query     │◀────│  Projector  │
│             │     │   API       │     │  (Consumer) │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │  Read DB    │
                                        │(Denormalized)│
                                        │Elasticsearch│
                                        └─────────────┘
```

### Implementation Example (Go)

```go
// ============ COMMAND SIDE ============

// Command
type PlaceOrderCommand struct {
    CustomerID uuid.UUID
    Items      []OrderItemDTO
    CouponCode string
}

// Command Handler
type PlaceOrderHandler struct {
    orderRepo   order.Repository
    pricingSvc  *PricingService
    eventBus    EventBus
}

func (h *PlaceOrderHandler) Handle(ctx context.Context, cmd PlaceOrderCommand) error {
    // 1. Load/build aggregate
    items := convertItems(cmd.Items)
    total := h.pricingSvc.CalculateTotal(items, cmd.CouponCode)

    order, err := order.New(cmd.CustomerID, items, total)
    if err != nil {
        return err
    }

    // 2. Save aggregate (generates events)
    if err := h.orderRepo.Save(ctx, order); err != nil {
        return err
    }

    // 3. Events published by repository
    return nil
}

// ============ QUERY SIDE ============

// Read Model (denormalized for specific query)
type OrderSummary struct {
    OrderID      uuid.UUID
    CustomerName string
    Total        string
    Status       string
    ItemCount    int
    CreatedAt    time.Time
}

// Query
type GetCustomerOrdersQuery struct {
    CustomerID uuid.UUID
    Page       int
    PageSize   int
}

// Query Handler
type OrderQueryHandler struct {
    readDB *sql.DB // separate read-optimized DB
}

func (h *OrderQueryHandler) Handle(
    ctx context.Context,
    q GetCustomerOrdersQuery,
) ([]OrderSummary, error) {
    // Optimized query — no joins needed
    rows, err := h.readDB.QueryContext(ctx, `
        SELECT order_id, customer_name, total, status, item_count, created_at
        FROM order_summaries
        WHERE customer_id = $1
        ORDER BY created_at DESC
        LIMIT $2 OFFSET $3
    `, q.CustomerID, q.PageSize, (q.Page-1)*q.PageSize)
    // ... scan rows
}

// ============ PROJECTOR (syncs read model) ============

type OrderProjector struct {
    readDB *sql.DB
}

func (p *OrderProjector) OnOrderPlaced(event OrderPlacedEvent) error {
    _, err := p.readDB.Exec(`
        INSERT INTO order_summaries (order_id, customer_id, total, status, item_count, created_at)
        VALUES ($1, $2, $3, 'PENDING', $4, $5)
    `, event.OrderID, event.CustomerID, event.Total.String(),
        len(event.Items), event.CreatedAt)
    return err
}

func (p *OrderProjector) OnOrderPaid(event OrderPaidEvent) error {
    _, err := p.readDB.Exec(`
        UPDATE order_summaries SET status = 'PAID' WHERE order_id = $1
    `, event.OrderID)
    return err
}
```

### CQRS Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Premature CQRS** | Simple CRUD app with CQRS | Remove CQRS. Use simple CRUD |
| **Shared Database** | Command and Query use same DB | Separate schemas or physical DBs |
| **Eventual Consistency Confusion** | Users expect immediate read-after-write | Show "processing" state, or use synchronous projection |
| **Over-Projection** | Projecting every field to read model | Only project fields needed for queries |

---

## 2️⃣ Event Sourcing

**Definition:** Store the state of an application as a sequence of events. The current state is derived by replaying events.

### Why Event Sourcing?

| Benefit | Description |
|---------|-------------|
| **Full Audit Trail** | Every change is recorded with timestamp and reason |
| **Temporal Queries** | "What was the state at time T?" |
| **Event Replay** | Rebuild read models, debug issues by replaying |
| **Natural CQRS** | Events feed read model projections |

### Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Command   │────▶│  Aggregate  │────▶│  Event      │
│   Handler   │     │  (applies   │     │  Store      │
│             │     │   events)   │     │ (Append-only)│
└─────────────┘     └──────┬──────┘     └─────────────┘
                           │
                           │ generates
                           ▼
                    ┌─────────────┐
                    │  Domain     │
                    │  Events     │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌─────────┐  ┌─────────┐  ┌─────────┐
        │ Read    │  │ Read    │  │ Read    │
        │ Model 1 │  │ Model 2 │  │ Model 3 │
        └─────────┘  └─────────┘  └─────────┘
```

### Implementation Example (Go)

```go
// Event Store interface
type EventStore interface {
    Append(ctx context.Context, streamID string, events []DomainEvent, expectedVersion int) error
    Read(ctx context.Context, streamID string) ([]StoredEvent, error)
    ReadAll(ctx context.Context, afterPosition int64) ([]StoredEvent, error)
}

// Stored event in DB
type StoredEvent struct {
    StreamID    string
    StreamType  string
    Position    int64
    EventType   string
    EventData   json.RawMessage
    OccurredAt  time.Time
}

// Aggregate with event sourcing
type Order struct {
    ID      uuid.UUID
    Version int // optimistic concurrency
    // state derived from events
    CustomerID uuid.UUID
    Items      []OrderItem
    Status     OrderStatus
    Total      Money
    // uncommitted events
    pendingEvents []DomainEvent
}

// Apply event to mutate state
func (o *Order) apply(event DomainEvent) {
    switch e := event.(type) {
    case OrderCreatedEvent:
        o.ID = e.OrderID
        o.CustomerID = e.CustomerID
        o.Status = OrderStatusPending
        o.Total = e.Total
    case OrderItemAddedEvent:
        o.Items = append(o.Items, OrderItem{
            ProductID: e.ProductID,
            Quantity:  e.Quantity,
            UnitPrice: e.UnitPrice,
        })
    case OrderPaidEvent:
        o.Status = OrderStatusPaid
    }
    o.Version++
}

// Reconstruct from events
func OrderFromEvents(events []DomainEvent) *Order {
    order := &Order{}
    for _, event := range events {
        order.apply(event)
    }
    return order
}

// Command creates event
func (o *Order) Pay(payment Money) error {
    if o.Status != OrderStatusPending {
        return errors.New("order not pending")
    }
    if !o.Total.Equals(payment) {
        return errors.New("payment mismatch")
    }
    o.pendingEvents = append(o.pendingEvents, OrderPaidEvent{
        OrderID: o.ID,
        Amount:  payment,
        PaidAt:  time.Now(),
    })
    o.apply(o.pendingEvents[len(o.pendingEvents)-1])
    return nil
}

// Repository loads and saves
func (r *EventSourcedOrderRepository) FindByID(
    ctx context.Context,
    id uuid.UUID,
) (*Order, error) {
    events, err := r.eventStore.Read(ctx, "order-"+id.String())
    if err != nil {
        return nil, err
    }
    domainEvents := make([]DomainEvent, len(events))
    for i, e := range events {
        domainEvents[i] = deserialize(e.EventType, e.EventData)
    }
    return OrderFromEvents(domainEvents), nil
}

func (r *EventSourcedOrderRepository) Save(
    ctx context.Context,
    order *Order,
) error {
    if len(order.pendingEvents) == 0 {
        return nil
    }
    err := r.eventStore.Append(
        ctx,
        "order-"+order.ID.String(),
        order.pendingEvents,
        order.Version-len(order.pendingEvents), // expected version
    )
    if err != nil {
        return err // optimistic concurrency conflict
    }
    order.pendingEvents = nil
    return nil
}
```

### Event Sourcing Anti-Patterns

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Giant Event** | One event captures entire aggregate state | Split into granular business facts |
| **No Schema Versioning** | Can't evolve event schema | Add version field, support upcasting |
| **Missing Snapshot** | Replay 10,000 events to load aggregate | Snapshot every N events |
| **Event as API** | External systems consume raw events | Use published language / integration events |

---

## 3️⃣ Outbox Pattern

**Definition:** Ensure atomic consistency between database state and message publication by writing messages to an "outbox" table in the same transaction.

### The Problem

```
Without Outbox:
  1. Save order to DB ✅
  2. Publish OrderPlaced event ❌ (network failure)
  → DB has order, but no event. Inconsistent.

With Outbox:
  1. Save order to DB ✅
  2. Save event to outbox table (same transaction) ✅
  3. Background process reads outbox and publishes ✅
  → Atomic. Either both succeed or both fail.
```

### Implementation (Go + PostgreSQL)

```go
// Outbox table schema:
// CREATE TABLE outbox (
//     id SERIAL PRIMARY KEY,
//     aggregate_type VARCHAR(255) NOT NULL,
//     aggregate_id VARCHAR(255) NOT NULL,
//     event_type VARCHAR(255) NOT NULL,
//     payload JSONB NOT NULL,
//     created_at TIMESTAMP NOT NULL DEFAULT NOW(),
//     published_at TIMESTAMP,
//     UNIQUE(aggregate_type, aggregate_id, event_type, payload)
// );

// Repository saves aggregate + outbox in one transaction
func (r *OrderRepository) Save(ctx context.Context, order *Order) error {
    tx, err := r.db.BeginTx(ctx, nil)
    if err != nil {
        return err
    }
    defer tx.Rollback()

    // 1. Save aggregate state
    if err := r.saveOrder(tx, order); err != nil {
        return err
    }

    // 2. Save events to outbox (same transaction!)
    events := order.PullEvents()
    for _, event := range events {
        payload, _ := json.Marshal(event)
        _, err := tx.ExecContext(ctx, `
            INSERT INTO outbox (aggregate_type, aggregate_id, event_type, payload)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT DO NOTHING
        `, "order", order.ID.String(), event.EventName(), payload)
        if err != nil {
            return err
        }
    }

    return tx.Commit()
}

// Background relay process
type OutboxRelay struct {
    db       *sql.DB
    eventBus EventBus
    pollInterval time.Duration
}

func (r *OutboxRelay) Start(ctx context.Context) {
    ticker := time.NewTicker(r.pollInterval)
    defer ticker.Stop()

    for {
        select {
        case <-ctx.Done():
            return
        case <-ticker.C:
            r.processOutbox(ctx)
        }
    }
}

func (r *OutboxRelay) processOutbox(ctx context.Context) error {
    rows, err := r.db.QueryContext(ctx, `
        SELECT id, aggregate_type, aggregate_id, event_type, payload
        FROM outbox
        WHERE published_at IS NULL
        ORDER BY id
        LIMIT 100
        FOR UPDATE SKIP LOCKED
    `)
    if err != nil {
        return err
    }
    defer rows.Close()

    for rows.Next() {
        var id int
        var aggType, aggID, eventType string
        var payload []byte
        rows.Scan(&id, &aggType, &aggID, &eventType, &payload)

        // Publish to event bus
        event := deserialize(eventType, payload)
        if err := r.eventBus.Publish(ctx, event); err != nil {
            log.Printf("failed to publish outbox event %d: %v", id, err)
            continue // will retry on next poll
        }

        // Mark as published
        _, err = r.db.ExecContext(ctx, `
            UPDATE outbox SET published_at = NOW() WHERE id = $1
        `, id)
        if err != nil {
            log.Printf("failed to mark outbox event %d as published: %v", id, err)
        }
    }
    return rows.Err()
}
```

---

## 4️⃣ Saga Pattern

**Definition:** A sequence of local transactions where each transaction updates data and publishes an event/message to trigger the next transaction. If a step fails, compensating transactions undo previous steps.

### Types

| Type | Coordination | When to Use |
|------|-------------|-------------|
| **Orchestration** | Central coordinator saga | Complex flows, need visibility |
| **Choreography** | Event-driven, no central coordinator | Simple flows, loose coupling |

### Orchestration Saga Example: Order Processing

```
┌─────────────┐
│  Saga       │
│ Coordinator │
└──────┬──────┘
       │ 1. ReserveInventory
       ▼
┌─────────────┐     2. InventoryReserved
│  Inventory  │────────────────▶
│  Service    │
└─────────────┘
       ▲
       │ 3. ProcessPayment
       ▼
┌─────────────┐     4. PaymentConfirmed
│  Payment    │────────────────▶
│  Service    │
└─────────────┘
       ▲
       │ 5. CreateShipment
       ▼
┌─────────────┐     6. ShipmentCreated
│  Shipping   │────────────────▶
│  Service    │
└─────────────┘
       │
       │ (if any step fails)
       ▼
┌─────────────┐
│ Compensate: │
│ - ReleaseInventory
│ - RefundPayment
│ - CancelShipment
└─────────────┘
```

### Go Implementation (Orchestration)

```go
type OrderSaga struct {
    inventorySvc InventoryClient
    paymentSvc   PaymentClient
    shippingSvc  ShippingClient
    sagaRepo     SagaRepository
}

func (s *OrderSaga) Start(ctx context.Context, order Order) error {
    saga := SagaState{
        ID:      uuid.New(),
        OrderID: order.ID,
        Status:  SagaStatusStarted,
        Steps: []SagaStep{
            {Name: "reserve_inventory", Status: StepStatusPending},
            {Name: "process_payment", Status: StepStatusPending},
            {Name: "create_shipment", Status: StepStatusPending},
        },
    }

    if err := s.sagaRepo.Save(ctx, saga); err != nil {
        return err
    }

    // Step 1: Reserve Inventory
    reservation, err := s.inventorySvc.Reserve(ctx, order.Items)
    if err != nil {
        return s.compensate(ctx, saga) // nothing to undo yet
    }
    saga.Steps[0].Status = StepStatusCompleted
    saga.Steps[0].Result = reservation.ID
    s.sagaRepo.Save(ctx, saga)

    // Step 2: Process Payment
    payment, err := s.paymentSvc.Charge(ctx, order.Total, order.CustomerID)
    if err != nil {
        return s.compensate(ctx, saga) // undo inventory reservation
    }
    saga.Steps[1].Status = StepStatusCompleted
    saga.Steps[1].Result = payment.ID
    s.sagaRepo.Save(ctx, saga)

    // Step 3: Create Shipment
    shipment, err := s.shippingSvc.Create(ctx, order.ID, order.ShippingAddress)
    if err != nil {
        return s.compensate(ctx, saga) // undo payment + inventory
    }
    saga.Steps[2].Status = StepStatusCompleted
    saga.Steps[2].Result = shipment.ID
    saga.Status = SagaStatusCompleted
    s.sagaRepo.Save(ctx, saga)

    return nil
}

func (s *OrderSaga) compensate(ctx context.Context, saga SagaState) error {
    saga.Status = SagaStatusCompensating
    s.sagaRepo.Save(ctx, saga)

    // Compensate in reverse order
    for i := len(saga.Steps) - 1; i >= 0; i-- {
        step := saga.Steps[i]
        if step.Status != StepStatusCompleted {
            continue
        }

        switch step.Name {
        case "create_shipment":
            s.shippingSvc.Cancel(ctx, step.Result)
        case "process_payment":
            s.paymentSvc.Refund(ctx, step.Result)
        case "reserve_inventory":
            s.inventorySvc.Release(ctx, step.Result)
        }

        step.Status = StepStatusCompensated
        s.sagaRepo.Save(ctx, saga)
    }

    saga.Status = SagaStatusCompensated
    return s.sagaRepo.Save(ctx, saga)
}
```

---

## 5️⃣ Anti-Corruption Layer (ACL)

**Definition:** A translation layer that isolates your domain model from external systems' incompatible models.

### Why ACL?

```
Without ACL:
  Your Domain ──direct uses──▶ External Model (leaks into your domain)

With ACL:
  Your Domain ──uses──▶ ACL ──translates──▶ External Model
```

### Implementation (Go)

```go
// Your domain model (clean, no external dependencies)
package domain

type Order struct {
    ID     uuid.UUID
    Total  Money
    Status OrderStatus
}

// External API model (messy, you don't control it)
package external

type StripeCharge struct {
    ID            string  `json:"id"`
    Amount        int     `json:"amount"` // in cents!
    Currency      string  `json:"currency"`
    Status        string  `json:"status"`
    ReceiptURL    string  `json:"receipt_url"`
    FailureCode   string  `json:"failure_code"`
    FailureMessage string `json:"failure_message"`
}

// ACL: translates between your domain and external model
package acl

type StripePaymentAdapter struct {
    client *stripe.Client
}

func (a *StripePaymentAdapter) Charge(
    ctx context.Context,
    amount domain.Money,
    customerID uuid.UUID,
) (domain.PaymentResult, error) {
    // Translate domain → external
    stripeAmount := amount.Amount.Mul(decimal.NewFromInt(100)).IntPart() // cents

    charge, err := a.client.CreateCharge(ctx, external.StripeChargeRequest{
        Amount:   stripeAmount,
        Currency: strings.ToLower(amount.Currency),
        Customer: customerID.String(),
    })
    if err != nil {
        return domain.PaymentResult{}, fmt.Errorf("stripe charge failed: %w", err)
    }

    // Translate external → domain
    return a.toDomainResult(charge), nil
}

func (a *StripePaymentAdapter) toDomainResult(
    charge external.StripeCharge,
) domain.PaymentResult {
    status := domain.PaymentStatusPending
    switch charge.Status {
    case "succeeded":
        status = domain.PaymentStatusSucceeded
    case "failed":
        status = domain.PaymentStatusFailed
    }

    amount := decimal.NewFromInt(int64(charge.Amount)).Div(decimal.NewFromInt(100))

    return domain.PaymentResult{
        TransactionID: charge.ID,
        Amount:        domain.MustNewMoney(amount, strings.ToUpper(charge.Currency)),
        Status:        status,
        ReceiptURL:    charge.ReceiptURL,
        FailureReason: charge.FailureMessage,
    }
}
```

---

## 📋 Pattern Selection Flowchart

```
Do you need to separate read/write models?
├── YES → Do you need full audit trail?
│         ├── YES → Event Sourcing + CQRS
│         └── NO  → CQRS only
│
├── NO → Do you need cross-service consistency?
│        ├── YES → Do you need to undo on failure?
│        │        ├── YES → Saga Pattern
│        │        └── NO  → Outbox Pattern
│        │
│        └── NO → Is there an external system with different model?
│                 ├── YES → Anti-Corruption Layer
│                 └── NO  → Standard DDD Tactical patterns
```

---

## 📚 References

- [CQRS, Task Based UIs, Event Sourcing](https://cqrs.wordpress.com/documents/) — Greg Young
- [Exploring CQRS and Event Sourcing](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/jj554200(v=pandp.10)) — Microsoft patterns & practices
- [The Outbox Pattern](https://microservices.io/patterns/data/transactional-outbox.html) — Chris Richardson
- [Saga Pattern](https://microservices.io/patterns/data/saga.html) — Chris Richardson
- [Anti-Corruption Layer](https://docs.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer) — Azure Architecture Center
- [Domain-Driven Design: Tackling Complexity](https://www.domainlanguage.com/ddd/) — Eric Evans
