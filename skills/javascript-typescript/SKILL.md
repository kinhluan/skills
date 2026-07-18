---
name: javascript-typescript
description: Implement, review, debug, test, or modernize JavaScript and TypeScript for browsers, Node.js, services, and frontend applications. Use for typing, async behavior, React/UI code, package tooling, tests, runtime compatibility, or performance.
metadata:
  tags: ["javascript", "typescript", "nodejs", "frontend", "testing", "async"]
---

# JavaScript and TypeScript

Follow the repository's runtime, package manager, lockfile, module system, framework, compiler, and browser support. Inspect configuration and CI before changing dependencies or syntax.

## Workflow

1. Read local instructions and identify the runtime boundary.
2. Reproduce the behavior with the existing package manager and scripts.
3. Trace types and data from untrusted input to side effects.
4. Implement the smallest coherent change without mixing unrelated dependency or formatting churn.
5. Run configured typecheck, lint, tests, and build.
6. Check bundle/runtime compatibility, accessibility, security, and cleanup.

Use repository scripts rather than assuming command names:

```bash
npm run typecheck
npm run lint
npm test
npm run build
```

Do not switch npm/pnpm/yarn/bun or regenerate a lockfile without evidence that the repository expects it.

## TypeScript Rules

- Prefer `unknown` over `any` at untrusted boundaries; narrow before use.
- Model variants with discriminated unions and make exhaustive handling visible.
- Keep assertions rare and local; prove invariants with runtime validation when data crosses a boundary.
- Avoid wrapper types (`String`, `Number`) and unsafe non-null assertions.
- Generate types from one authoritative schema when practical.
- Keep public exports intentional and stable.

## Async and State

- await or deliberately own every promise;
- handle cancellation/timeouts for network and long-running work;
- avoid races between stale responses and current UI state;
- clean up listeners, timers, subscriptions, streams, and abort controllers;
- make retried side effects idempotent or surface uncertainty;
- distinguish operational failure from invalid user input.

## Browser and UI

Use semantic HTML, keyboard access, visible focus, accessible names, and framework-recommended state patterns. Test user-observable behavior rather than implementation details. Do not inject untrusted HTML or URLs without contextual validation and encoding.

## Node and APIs

Validate input, bound payloads and concurrency, use parameterized data access, avoid synchronous blocking work on request paths, and keep secrets out of logs. Handle process shutdown and in-flight work explicitly.

## Dependencies and Performance

Add a dependency only after checking maintenance, license, security, runtime/bundle cost, and whether the platform already provides the capability. Measure before optimizing and report the workload and tool used.

## Output

Report behavior changed, runtime/type/dependency decisions, checks actually run, and residual compatibility risk.

Read [references/detailed-guide.md](references/detailed-guide.md) only for the relevant framework or pattern. Verify version-sensitive guidance against official runtime, TypeScript, and framework documentation.
