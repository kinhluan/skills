---
name: tdd-red-green-refactor
description: Drive implementation with TDD (red-green-refactor). Use when writing new behavior, fixing a bug, or refactoring behind a failing test first. pytest, Jest/Vitest, Go testing.
metadata:
  tags: ["tdd", "testing", "red-green-refactor", "pytest", "jest", "vitest", "go-test", "refactoring"]
  version: 1.0.0
---

# TDD: Red → Green → Refactor

Test-Driven Development is a design loop, not a coverage ritual. A failing test names the next behavior. Production code exists only to make that test pass. Refactor only while green.

> "The goal is clean code that works." — Kent Beck, *Test-Driven Development by Example*

Language-specific test APIs live in `python-development`, `javascript-typescript`, and `golang-development`. This skill owns the **cycle, laws, and when to stop**. Architecture tests (fitness functions) belong in `evolutionary-architecture`.

---

## When to use

| Situation | TDD? |
|-----------|------|
| New domain behavior / use case | ✅ Yes |
| Bug with a known reproduction | ✅ Yes — failing test first |
| Refactor of production code | ✅ Characterization test, then change |
| Spike / learning a library | ❌ No — throwaway, then TDD the keeper |
| Generated code, schema dumps | ❌ No |
| Pure config / one-line glue | ⚠️ Skip or one characterization test |

---

## Three laws (Beck)

1. **You may not write production code** unless it is to make a failing test pass.
2. **You may not write more of a test** than is sufficient to fail (compile failure counts as fail).
3. **You may not write more production code** than is sufficient to pass the currently failing test.

Violate any law and you are no longer doing TDD — you are writing tests after the fact.

---

## The cycle

```
RED     write one failing test (smallest behavior)
  ↓
GREEN   write the minimum code that passes (fake it if needed)
  ↓
REFACTOR  remove duplication, name intent, keep tests green
  ↓
repeat  next behavior — one increment, not a feature dump
```

**Cadence:** minutes, not hours. If red lasts more than a few minutes, the step is too big. Split the test.

### Red

- One behavior per test. Name it as a specification: `withdraw_refuses_when_balance_insufficient`.
- Assert on an observable outcome (return value, event, persisted state), not on private methods.
- The test must fail for the **right reason**. A compile error is red; an assertion on the wrong thing is a false red.

### Green

Three legal moves, cheapest first:

| Move | When |
|------|------|
| **Fake it** | Return a constant. Use when the real algorithm is not obvious yet. |
| **Obvious implementation** | Write the real code immediately when it is trivial and you are sure. |
| **Triangulation** | Add a second example that forces the fake to generalize. |

Do not generalize on one example. Do not gold-plate on green.

### Refactor

Allowed only while the suite is green.

- Remove duplication between tests and production (the third example often reveals the abstraction).
- Rename toward the ubiquitous language (`ddd-tactical`).
- Move code across layers only if the Dependency Rule still holds (`clean-architecture`): domain/use-case tests must not import adapters.
- **No new behavior during refactor.** New behavior is a new red.

---

## What to test (SE, not QA)

TDD here is the engineer's design tool. QC owns coverage gates and Sonar. Do not wait on a quality-gate skill to write the next test.

**Prefer:**

- Domain invariants and use-case outcomes (ports, not frameworks).
- Regression tests that pin a bug (`reproduces issue #N`).
- Boundary cases the type system cannot encode.

**Avoid as the first test:**

- Framework wiring, DI container graphs, CSS.
- Tests that assert mock call order instead of state.
- End-to-end UI as the inner loop (slow; keep for a thin outer belt).

Test pyramid for this skill:

```
        /\
       /E2E\        few, slow, against running system
      /------\
     / Contr. \     optional; HTTP contract or handler tests
    /----------\
   /   Unit     \   default TDD loop — domain + use cases
  /--------------\
```

---

## Language recipes (inner loop)

### Python (pytest)

```python
def test_allocate_rejects_when_capacity_exceeded():
    ward = Ward(capacity=1)
    ward.allocate(Patient(esi=2))

    with pytest.raises(WardFull):
        ward.allocate(Patient(esi=3))
```

- One assert that matters; `pytest.raises` for expected failures.
- No I/O in unit tests: fake the port (`Protocol`), do not hit the adapter.
- `pytest -q --tb=short path/to/test.py::test_name` during the loop.

### TypeScript (Vitest / Jest)

```ts
it("refuses withdraw when balance is insufficient", () => {
  const account = Account.open({ balance: 50 });
  expect(() => account.withdraw(80)).toThrow(InsufficientFunds);
});
```

- `it("does X when Y")` — behavior, not method name.
- Prefer fake in-memory repos over mocking every method.
- `vitest -t "insufficient"` for the focused red/green.

### Go

```go
func TestWithdraw_InsufficientFunds(t *testing.T) {
    t.Parallel()
    acc := OpenAccount(50)
    err := acc.Withdraw(80)
    if !errors.Is(err, ErrInsufficientFunds) {
        t.Fatalf("got %v", err)
    }
}
```

- Table tests **after** the first example is green, not before you understand the behavior.
- `go test -run TestWithdraw_InsufficientFunds -count=1`.
- Keep domain tests inside the domain package (`package ward` or `package ward_test` for black-box).

---

## Bug-first TDD

1. Write a test that fails the same way the bug fails (red that matches prod).
2. Confirm it fails (if it passes, you have not reproduced).
3. Fix production code until green.
4. Refactor if the fix left a mess.
5. Leave the test in the suite — that is the regression pin.

---

## Refactoring existing untested code

Do not TDD a rewrite of a ball of mud in one pass.

1. Add a **characterization test** around current behavior (may be ugly, may hit a real collaborator).
2. Green = "this is what it does today."
3. Refactor toward seams (extract port, move logic inward).
4. Only then add new behavior via red-green.

Strangler steps for a larger shift: `evolutionary-architecture`.

---

## Done when

- Latest test went red for the right reason, then green.
- No extra production code beyond that test.
- Names match the domain language.
- You can point to the next test or honestly say the increment is done.

**Stop** if you are designing a framework, drawing C4, or writing an ADR — switch to those skills. TDD does not replace `architecture-decision-records`.

---

## Anti-patterns

| Smell | Fix |
|-------|-----|
| Tests written after a 400-line dump | Throw away the dump or wrap it with characterization tests, then resume the cycle |
| Testing private methods | Test the behavior that uses them; private is an implementation detail |
| Mock-heavy tests that break on rename | Fake the port; assert state/events |
| Suite red for 30+ minutes | Split the test; you skipped green |
| Refactor while red | Undo. Get green first |
| Coverage target as the goal | Coverage is a QC gate. TDD goal is a design that is easy to change |
