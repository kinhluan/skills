---
name: python-development
description: Implement, review, debug, test, package, or modernize Python applications and libraries. Use for Python typing, async code, FastAPI/Pydantic, data access, project tooling, dependency management, testing, or performance work.
metadata:
  tags: ["python", "typing", "asyncio", "testing", "packaging", "fastapi"]
---

# Python Development

Use the Python versions and tools declared by the repository. Inspect `pyproject.toml`, lock files, CI, and runtime constraints before choosing syntax, packages, or configuration.

## Workflow

1. Read local instructions and the smallest relevant code/test surface.
2. Confirm interpreter and environment without modifying global Python.
3. Reproduce the behavior or define a failing test.
4. Implement a focused, typed change consistent with local patterns.
5. Run the configured formatter, linter, type checker, and tests.
6. Inspect dependency, compatibility, migration, and security impact.

Common commands are examples only:

```bash
python -m pytest
ruff check .
ruff format --check .
mypy .
```

Use the project's actual commands and do not claim a check passed when it was unavailable.

## Core Rules

- Prefer explicit data models and narrow interfaces over dictionaries with implicit shape.
- Type public boundaries and complex internal transformations; avoid `Any` as an escape hatch.
- Distinguish absence, invalid input, and operational failure.
- Raise specific exceptions and preserve the causal chain with `raise ... from ...`.
- Use context managers for resources and transactions.
- Keep imports side-effect-light and configuration explicit.
- Do not use mutable default arguments.
- Avoid broad exception catches unless adding context, cleanup, or a deliberate boundary response.
- Validate untrusted input at the edge; do not deserialize or execute untrusted code.
- Keep secrets out of source, logs, exception messages, fixtures, and serialized models.

## Async and Concurrency

Use async only across an async I/O path. Do not call blocking I/O in the event loop. Define cancellation, timeout, task ownership, backpressure, and cleanup. Use structured task groups supported by the repository's Python baseline. Protect shared state or avoid it.

## Web/Data Boundaries

- separate transport schemas from domain behavior when their lifecycles differ;
- define transaction scope and avoid hidden N+1 queries;
- make retries bounded and safe for the operation;
- return stable error contracts without leaking internals;
- validate migrations and backward compatibility;
- use parameterized queries and framework-supported encoding.

## Tests

Test observable behavior, boundaries, failure paths, and regression conditions. Use property-based, integration, concurrency, or performance tests when they cover a material risk. Keep fixtures small and deterministic; do not over-mock the unit under test.

## Output

Report behavior changed, compatibility/dependency decisions, commands actually run, and remaining risk.

Read [references/detailed-guide.md](references/detailed-guide.md) only for relevant patterns or examples. Verify version-sensitive guidance against the supported interpreter and [Python documentation](https://docs.python.org/3/).
