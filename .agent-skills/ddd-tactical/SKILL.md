---
name: ddd-tactical
description: Tactical Domain-Driven Design (DDD) with Scoring Rubric. Use this skill when designing internal domain models or performing architectural reviews to ensure domain logic is isolated and rich.
metadata:
  tags: ["ddd", "tactical-design", "aggregates", "clean-architecture", "domain-review", "value-object"]
---

# Domain-Driven Design (DDD): Tactical Building Blocks & Review

Tactical DDD focuses on the **technical implementation** of rich domain models within a single Bounded Context. While Strategic DDD answers "What to build and where?", Tactical DDD answers "How do we model this in code?"

> "The heart of DDD is the Domain Model itself." — Eric Evans

---

## 🧱 Building Blocks Reference

### 1. Entity

**Definition:** An object with a unique identity that persists over time. Two entities with the same ID are the same entity, even if their attributes differ.

**Characteristics:**
- Has a globally unique, stable identity (UUID, auto-increment, natural key)
- Mutable state (attributes can change)
- Identity equality: `a.id == b.id` means `a == b`
- Encapsulates business logic (not just data + getters/setters)

**Code Examples:**

**Go:**
```go
type Order struct {
    ID        uuid.UUID
    CustomerID uuid.UUID
    Items     []OrderItem
    Status    OrderStatus
    CreatedAt time.Time
}

func (o *Order) Cancel(reason string) error {
    if o.Status == OrderStatusShipped {
        return fmt.Errorf("cannot cancel shipped order")
    }
    if o.Status == OrderStatusCancelled {
        return fmt.Errorf("order already cancelled")
    }
    o.Status = OrderStatusCancelled
    o.recordEvent(OrderCancelledEvent{
        OrderID: o.ID,
        Reason:  reason,
        At:      time.Now(),
    })
    return nil
}

func (o Order) Equals(other Order) bool {
    return o.ID == other.ID // identity equality
}
```

**Python:**
```python
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class Order:
    id: UUID = field(default_factory=uuid4)
    customer_id: UUID = field(default_factory=uuid4)
    items: list = field(default_factory=list)
    status: str = "PENDING"
    created_at: datetime = field(default_factory=datetime.utcnow)
    _events: list = field(default_factory=list, repr=False)

    def cancel(self, reason: str) -> None:
        if self.status == "SHIPPED":
            raise ValueError("Cannot cancel shipped order")
        if self.status == "CANCELLED":
            raise ValueError("Order already cancelled")
        self.status = "CANCELLED"
        self._events.append(OrderCancelledEvent(
            order_id=self.id,
            reason=reason,
            at=datetime.utcnow()
        ))
```

**TypeScript:**
```typescript
class Order {
    private _events: DomainEvent[] = [];

    constructor(
        public readonly id: UUID,
        public readonly customerId: UUID,
        public items: OrderItem[],
        public status: OrderStatus = OrderStatus.PENDING,
        public readonly createdAt: Date = new Date()
    ) {}

    cancel(reason: string): void {
        if (this.status === OrderStatus.SHIPPED) {
            throw new Error('Cannot cancel shipped order');
        }
        if (this.status === OrderStatus.CANCELLED) {
            throw new Error('Order already cancelled');
        }
        this.status = OrderStatus.CANCELLED;
        this._events.push(new OrderCancelledEvent(this.id, reason, new Date()));
    }

    pullEvents(): DomainEvent[] {
        const events = [...this._events];
        this._events = [];
        return events;
    }
}
```

---

### 2. Value Object

**Definition:** An immutable object defined entirely by its attributes. Two VOs with the same values are equal. No identity.

**Characteristics:**
- Immutable (created once, never modified)
- Value equality: all fields must match
- Self-validating (invalid state impossible)
- Replace primitives (don't use `string` for email, `int` for age)

**Code Examples:**

**Go:**
```go
type Money struct {
    Amount   decimal.Decimal
    Currency string // ISO 4217
}

func NewMoney(amount decimal.Decimal, currency string) (Money, error) {
    if amount.IsNegative() {
        return Money{}, errors.New("amount cannot be negative")
    }
    if !isValidCurrency(currency) {
        return Money{}, fmt.Errorf("invalid currency: %s", currency)
    }
    return Money{Amount: amount, Currency: currency}, nil
}

func (m Money) Add(other Money) (Money, error) {
    if m.Currency != other.Currency {
        return Money{}, errors.New("cannot add different currencies")
    }
    return NewMoney(m.Amount.Add(other.Amount), m.Currency)
}

func (m Money) Equals(other Money) bool {
    return m.Amount.Equal(other.Amount) && m.Currency == other.Currency
}

// Usage: always valid
price, _ := NewMoney(decimal.NewFromFloat(99.99), "USD")
discount, _ := NewMoney(decimal.NewFromFloat(10.00), "USD")
final, _ := price.Subtract(discount) // $89.99 USD
```

**Python:**
```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.currency not in {"USD", "EUR", "VND", "JPY"}:
            raise ValueError(f"Invalid currency: {self.currency}")

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

# Usage
price = Money(Decimal("99.99"), "USD")
discount = Money(Decimal("10.00"), "USD")
final = price.add(discount)  # Money(109.99, "USD")
```

**TypeScript:**
```typescript
class Money {
    constructor(
        public readonly amount: Decimal,
        public readonly currency: string
    ) {
        if (amount.isNegative()) {
            throw new Error('Amount cannot be negative');
        }
        if (!VALID_CURRENCIES.has(currency)) {
            throw new Error(`Invalid currency: ${currency}`);
        }
    }

    add(other: Money): Money {
        if (this.currency !== other.currency) {
            throw new Error('Cannot add different currencies');
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }

    equals(other: Money): boolean {
        return this.amount.equals(other.amount) && this.currency === other.currency;
    }
}
```

---

### 3. Aggregate Root

**Definition:** A cluster of associated objects treated as a single unit for data changes. The Aggregate Root is the only entry point — external code cannot reference internal entities directly.

**Characteristics:**
- One Aggregate Root (AR) per aggregate
- AR controls all state changes within the aggregate
- Internal entities are accessed only through the AR
- Transaction boundary: one transaction per aggregate
- Enforces invariants (business rules that must always be true)

**Code Example (Go):**
```go
type Order struct { // Aggregate Root
    ID     uuid.UUID
    CustomerID uuid.UUID
    items  []OrderItem  // internal: accessed only through Order
    status OrderStatus
    total  Money
    events []DomainEvent
}

type OrderItem struct { // Entity within aggregate
    ProductID uuid.UUID
    Quantity  int
    UnitPrice Money
}

// Invariant: total must equal sum of item subtotals
func (o *Order) AddItem(productID uuid.UUID, quantity int, price Money) error {
    if o.status != OrderStatusPending {
        return errors.New("cannot modify non-pending order")
    }
    if quantity <= 0 {
        return errors.New("quantity must be positive")
    }

    item := OrderItem{
        ProductID: productID,
        Quantity:  quantity,
        UnitPrice: price,
    }
    o.items = append(o.items, item)
    o.recalculateTotal() // invariant enforcement
    return nil
}

func (o *Order) recalculateTotal() {
    total := MustNewMoney(decimal.Zero, o.total.Currency)
    for _, item := range o.items {
        subtotal, _ := item.UnitPrice.Multiply(item.Quantity)
        total, _ = total.Add(subtotal)
    }
    o.total = total
}

// Invariant: cannot pay wrong amount
func (o *Order) Pay(payment Money) error {
    if !o.total.Equals(payment) {
        return fmt.Errorf("payment %v does not match total %v", payment, o.total)
    }
    o.status = OrderStatusPaid
    o.recordEvent(OrderPaidEvent{OrderID: o.ID})
    return nil
}
```

---

### 4. Domain Service

**Definition:** Stateless business logic that doesn't belong to any Entity or Value Object. Used when logic involves multiple aggregates or doesn't fit a single entity.

**When to use:**
- Calculations spanning multiple aggregates
- Operations that don't have a natural "owner"
- External service coordination (with domain rules)

**Code Example:**
```go
// PricingService calculates order totals with discounts
// This logic doesn't belong to Order (doesn't own discount rules)
// or Product (doesn't know about orders)
type PricingService struct {
    discountRepo DiscountRepository
}

func (s *PricingService) CalculateTotal(
    items []OrderItem,
    customer Customer,
    couponCode string,
) (Money, error) {
    subtotal := calculateSubtotal(items)

    // Apply customer tier discount
    tierDiscount := s.customerTierDiscount(customer.Tier)
    afterTier, _ := subtotal.Multiply(1 - tierDiscount)

    // Apply coupon if valid
    if couponCode != "" {
        coupon, err := s.discountRepo.FindByCode(couponCode)
        if err != nil {
            return Money{}, err
        }
        if !coupon.IsValidFor(customer, items) {
            return Money{}, errors.New("coupon not applicable")
        }
        afterTier, _ = afterTier.Subtract(coupon.Amount)
    }

    // Add tax
    tax := s.calculateTax(afterTier, customer.ShippingAddress.Country)
    total, _ := afterTier.Add(tax)

    return total, nil
}
```

---

### 5. Repository

**Definition:** An abstraction over persistence. The domain defines the interface; infrastructure provides the implementation.

**Pattern:**
```
Domain Layer          → defines interface (port)
                      │
Infrastructure Layer  → implements interface (adapter)
```

**Go Example:**
```go
// domain/order/repository.go — defined in domain layer
package order

type Repository interface {
    FindByID(ctx context.Context, id uuid.UUID) (*Order, error)
    FindByCustomer(ctx context.Context, customerID uuid.UUID) ([]*Order, error)
    Save(ctx context.Context, order *Order) error
    Delete(ctx context.Context, id uuid.UUID) error
}

// infrastructure/persistence/postgres_order_repo.go — implemented in infra layer
package persistence

type PostgresOrderRepository struct {
    db *sql.DB
}

func (r *PostgresOrderRepository) FindByID(
    ctx context.Context,
    id uuid.UUID,
) (*order.Order, error) {
    // SQL implementation
}

func (r *PostgresOrderRepository) Save(
    ctx context.Context,
    o *order.Order,
) error {
    // SQL implementation with event extraction
    events := o.PullEvents()
    for _, event := range events {
        // publish to event bus
    }
    return nil
}
```

---

### 6. Factory

**Definition:** Encapsulates complex object creation logic. Used when creating an aggregate involves multiple steps or invariants.

**Go Example:**
```go
type OrderFactory struct {
    idGenerator IDGenerator
    clock       Clock
}

func (f *OrderFactory) CreateOrder(
    customerID uuid.UUID,
    items []OrderItem,
) (*Order, error) {
    if len(items) == 0 {
        return nil, errors.New("order must have at least one item")
    }

    order := &Order{
        ID:         f.idGenerator.Generate(),
        CustomerID: customerID,
        Items:      items,
        Status:     OrderStatusPending,
        CreatedAt:  f.clock.Now(),
    }
    order.recalculateTotal()

    order.recordEvent(OrderCreatedEvent{
        OrderID:    order.ID,
        CustomerID: customerID,
        Total:      order.Total,
        At:         order.CreatedAt,
    })

    return order, nil
}
```

---

### 7. Domain Event

**Definition:** A record of something significant that happened in the domain. Events are immutable and represent past facts.

**Pattern:**
```
1. Event occurs inside aggregate
2. Aggregate collects events internally
3. Repository extracts events on save
4. Events are published to event bus
5. Other aggregates/consumers react
```

**Go Example:**
```go
// Event definition
type OrderPaidEvent struct {
    OrderID   uuid.UUID
    Amount    Money
    PaidAt    time.Time
}

func (e OrderPaidEvent) EventName() string { return "order.paid" }

// Inside aggregate
func (o *Order) Pay(payment Money) error {
    // ... validation ...
    o.status = OrderStatusPaid
    o.recordEvent(OrderPaidEvent{
        OrderID: o.ID,
        Amount:  payment,
        PaidAt:  time.Now(),
    })
    return nil
}

func (o *Order) recordEvent(event DomainEvent) {
    o.events = append(o.events, event)
}

func (o *Order) PullEvents() []DomainEvent {
    events := o.events
    o.events = nil
    return events
}
```

---

### 8. Specification Pattern

**Definition:** Encapsulates query criteria as reusable, composable objects.

**Go Example:**
```go
// Specification interface
type OrderSpecification interface {
    IsSatisfiedBy(order Order) bool
    ToSQL() (string, []interface{})
}

// Concrete specifications
type OverdueOrderSpecification struct {
    Now time.Time
}

func (s OverdueOrderSpecification) IsSatisfiedBy(order Order) bool {
    if order.Status != OrderStatusPaid {
        return false
    }
    dueDate := order.CreatedAt.Add(7 * 24 * time.Hour)
    return s.Now.After(dueDate) && order.Status != OrderStatusShipped
}

func (s OverdueOrderSpecification) ToSQL() (string, []interface{}) {
    return "status = ? AND created_at < ?",
        []interface{}{OrderStatusPaid, s.Now.Add(-7 * 24 * time.Hour)}
}

// Composable specifications
type AndSpecification struct {
    Left, Right OrderSpecification
}

func (s AndSpecification) IsSatisfiedBy(order Order) bool {
    return s.Left.IsSatisfiedBy(order) && s.Right.IsSatisfiedBy(order)
}

// Usage
overdue := OverdueOrderSpecification{Now: time.Now()}
highValue := HighValueOrderSpecification{MinAmount: MustNewMoney(decimal.NewFromFloat(1000), "USD")}
critical := AndSpecification{Left: overdue, Right: highValue}

// In memory
for _, order := range orders {
    if critical.IsSatisfiedBy(order) {
        // handle critical overdue high-value order
    }
}

// In database
sql, args := critical.ToSQL()
rows, _ := db.Query("SELECT * FROM orders WHERE "+sql, args...)
```

---

## ⭐ Domain Model Scoring Rubric (0-10)

Rate your domain design:

| Criterion | Points | Check |
|-----------|--------|-------|
| **Immutability** | 2 | Value Objects are immutable, created via factory/constructor with validation |
| **Invariants** | 2 | Aggregate Roots enforce business rules before any state change |
| **Encapsulation** | 2 | Internal aggregate parts hidden; only AR exposes public methods |
| **Identity** | 2 | Entities have stable, globally unique IDs; VOs have value equality |
| **Ubiquitous Language** | 2 | Class/method names match business language exactly |

**Scoring:**
- **10/10:** Exemplary. Domain logic is fully encapsulated, rich, and self-validating.
- **8-9/10:** Good. Minor gaps in encapsulation or language alignment.
- **6-7/10:** Fair. Some anemic models, primitive obsession, or leaked logic.
- **≤5/10:** Poor. Significant refactoring needed. Likely anemic domain model.

**Goal:** Target 8/10 or higher for Core Domains.

---

## 🚫 Tactical Anti-Patterns

| Anti-Pattern | Score | Symptom | Fix |
|-------------|-------|---------|-----|
| **Anemic Model** | 0/10 | Entities with only getters/setters, logic in Services | Move business rules into entities |
| **God Aggregate** | 3/10 | Single aggregate with 10+ entities | Split by consistency boundary |
| **Primitive Obsession** | 5/10 | `string email`, `int age` instead of VOs | Create Email, Age VOs with validation |
| **Leaking Domain** | 4/10 | Returning domain entities in API responses | Use DTOs at boundary |
| **Missing Invariants** | 3/10 | Invalid states possible (negative quantity) | Validate in constructor/methods |
| **Getter/Setter Abuse** | 2/10 | Public setters allow any state change | Make fields private, expose behavior methods |

---

## 📦 Tactical Artifacts

After designing the tactical model, create:

```
docs/domain/
├── model-summary.md          # All aggregates, entities, VOs
├── logic-rules.md            # Business invariants enforced by ARs
├── ubiquitous-language.md    # Glossary: business term → code term
└── diagrams/
    └── class-diagram.mermaid # UML of key aggregates
```

---

## 📚 References

- [Domain-Driven Design](https://www.domainlanguage.com/ddd/) — Eric Evans, Chapters 5-12 (Tactical)
- [Implementing Domain-Driven Design](https://kalele.io/book/) — Vaughn Vernon
- [Patterns of Enterprise Application Architecture](https://martinfowler.com/books/eaa.html) — Martin Fowler
