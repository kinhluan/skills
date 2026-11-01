---
name: golang-development
description: Implement, review, debug, or modernize Go code and modules with idiomatic APIs, concurrency, error handling, testing, profiling, and tooling. Use for Go services, libraries, CLIs, goroutine/channel issues, module management, or performance work.
metadata:
  tags: ["go", "golang", "concurrency", "testing", "modules", "performance"]
---

# Go Development

Follow the repository's supported Go version, toolchain, style, and dependency policy. Check `go.mod`, CI, and the official release notes before recommending version-specific APIs.

## Workflow

1. Read repository instructions and relevant packages/tests.
2. Establish the supported toolchain with `go version` and `go.mod`.
3. Trace ownership, API contracts, goroutine lifetime, cancellation, and errors.
4. Implement the smallest coherent change.
5. Format and verify with the project's commands; commonly:

```bash
gofmt -w <changed-files>
go test ./...
go vet ./...
```

Run race detection, fuzzing, benchmarks, staticcheck, or integration tests when the risk warrants them and the tools are configured.

## Core Rules

- Make the zero value useful where practical.
- Accept interfaces at consumer boundaries; return concrete types unless abstraction is needed.
- Keep interfaces small and behavior-focused.
- Wrap errors with useful context and preserve identity with `%w`.
- Use `errors.Is`/`errors.As`; do not parse error strings.
- Pass `context.Context` explicitly as the first parameter for cancellable work; do not store it in structs.
- Define goroutine ownership and termination. Every send, receive, lock, and wait needs a cancellation/failure story.
- Close channels from the sending side that owns them; do not close merely to signal one consumer unless the protocol calls for it.
- Avoid shared mutable state; when required, document synchronization and test with `-race`.
- Keep package names short, lowercase, and responsibility-based. Avoid utility dumping grounds.
- Treat panics as process/programmer failures, not normal library error handling.

## Service and API Checks

- bound request, retry, and shutdown time;
- distinguish client cancellation from server failure;
- validate inputs at the boundary and enforce invariants in the domain;
- keep database transactions short and propagate cancellation;
- expose actionable logs/metrics without secrets or high-cardinality identifiers;
- make retries idempotent or explicitly unsafe;
- drain and close HTTP response bodies appropriately.

## Performance

Measure before optimizing. Add or run a representative benchmark, inspect allocations, and profile the real bottleneck. Prefer a clear algorithmic improvement over pooling or unsafe tricks. State dataset, CPU/toolchain, benchmark flags, and variance when reporting results.

## Output

Report the behavior changed, important Go-specific decisions, commands actually run, race/performance evidence when relevant, and residual compatibility risk.

For patterns and examples, read [references/detailed-guide.md](references/detailed-guide.md) only for the relevant topic. Treat version numbers and dependency releases in that guide as examples and verify them against [Go releases](https://go.dev/doc/devel/release) and package documentation.
