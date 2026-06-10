---
name: javascript-typescript
description: Modern JavaScript and TypeScript development best practices (2024-2025). Use for frontend, backend, full-stack, React/Next.js, Node.js, testing, linting, and production deployment.
metadata:
  tags: ["javascript", "typescript", "frontend", "backend", "nodejs", "react", "nextjs", "testing", "linting", "bun", "pnpm"]
---

# JavaScript & TypeScript

Modern JS/TS development covering project setup, TypeScript strict mode, React/Next.js patterns, state management, testing, linting, and production deployment. Targets Node.js 20+, TypeScript 5.5+, React 19+, pnpm, bun.

> "Make invalid states unrepresentable." — The TypeScript Way

---

## 1. Project Setup

### Package Manager

| Tool | Best For | Install | Speed | Lockfile |
|---|---|---|---|---|
| **pnpm** (recommended) | Monorepos, disk efficiency, strict dependency resolution | `corepack enable && corepack prepare pnpm@latest --activate` | Fast | `pnpm-lock.yaml` |
| **bun** | Runtime + bundler + test runner in one, fastest install | `curl -fsSL https://bun.sh/install \| bash` | Fastest | `bun.lockb` |
| npm | Default, no setup needed | Built-in with Node.js | Slowest | `package-lock.json` |

**pnpm workflow:**
```bash
# Enable corepack (Node.js 16.13+) — one-time setup
corepack enable
corepack prepare pnpm@latest --activate

# Project init
pnpm init
pnpm add typescript react react-dom
pnpm add -D @types/react @types/react-dom eslint prettier vitest

# Monorepo workspace
pnpm-workspace.yaml:
  packages:
    - 'packages/*'
    - 'apps/*'

# Workspace commands
pnpm -r install          # install all workspaces
pnpm --filter web build  # build only 'web' package
pnpm -r exec tsc --noEmit # type-check all
```

**bun workflow:**
```bash
# Install (macOS/Linux)
curl -fsSL https://bun.sh/install | bash

# Project init — creates bun.lockb, package.json, tsconfig.json
bun init

# Install dependencies (10-100x faster than npm)
bun add typescript react react-dom
bun add -D @types/react @types/react-dom

# Run scripts (no need for 'run')
bun dev                  # runs 'dev' script
bun test                 # built-in test runner (Jest-compatible)
bun build                # built-in bundler

# Runtime: drop-in Node.js replacement
bun run server.ts        # instead of node server.ts
bun --hot server.ts      # hot reload (no nodemon needed)
```

**When to choose what:**
```
Monorepo with 5+ packages     → pnpm (workspace filtering, strict hoisting)
Single app, speed critical    → bun (runtime + bundler + test in one)
Enterprise / CI consistency   → pnpm (mature, predictable, corepack)
Quick prototype / side project → bun (fastest everything)
```

**Lockfile hygiene (critical for CI reproducibility):**
```bash
# pnpm — deterministic, content-addressable
pnpm install --frozen-lockfile   # CI: fail if lockfile out of sync
pnpm install --no-frozen-lockfile # Local: update lockfile

# bun — binary lockfile, very fast
bun install --frozen-lockfile     # CI
bun install --no-save             # Local, don't update lockfile
```

### TypeScript Configuration (`tsconfig.json`)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

**Key strict flags:**
| Flag | Effect |
|---|---|
| `strictNullChecks` | `null`/`undefined` are separate types |
| `noUncheckedIndexedAccess` | `arr[0]` is `T \| undefined` |
| `exactOptionalPropertyTypes` | `?` means absent, not `\| undefined` |

---

## 2. Type Best Practices

### Prefer Interfaces for Object Shapes

```typescript
// ✅ Interface — extensible, better error messages
interface User {
  id: string;
  name: string;
  email: string;
}

// ✅ Type — for unions, tuples, mapped types
type Status = 'idle' | 'loading' | 'success' | 'error';
type ApiResponse<T> = { data: T; status: number } | { error: string; status: number };

// ❌ Don't use type for simple objects (unless you need union)
```

### Discriminated Unions

```typescript
type LoadingState = { status: 'loading' };
type SuccessState<T> = { status: 'success'; data: T };
type ErrorState = { status: 'error'; error: string };

type AsyncState<T> = LoadingState | SuccessState<T> | ErrorState;

function handleState<T>(state: AsyncState<T>): T | null {
  switch (state.status) {
    case 'loading': return null;
    case 'success': return state.data;  // TypeScript knows data exists
    case 'error': throw new Error(state.error);
    default: return exhaustiveCheck(state);
  }
}

function exhaustiveCheck(x: never): never {
  throw new Error(`Unhandled case: ${x}`);
}
```

### Branded Types for Type-Safe IDs

```typescript
type UserId = string & { __brand: 'UserId' };
type OrderId = string & { __brand: 'OrderId' };

function createUserId(id: string): UserId {
  return id as UserId;
}

// Now this is a type error:
// const userId: UserId = createUserId('123');
// const orderId: OrderId = userId;  // ❌ Compile error
```

### Utility Types

```typescript
// Partial, Required, Pick, Omit
 type UpdateUserInput = Partial<Pick<User, 'name' | 'email'>>;

// ReturnType, Parameters
 type ApiReturn = ReturnType<typeof fetchUser>;
 type ApiParams = Parameters<typeof fetchUser>;

// Record, Readonly
 type ConfigMap = Record<string, string>;
 type ImmutableUser = Readonly<User>;

// Awaited (unwraps Promise)
 type UserData = Awaited<ReturnType<typeof fetchUser>>;
```

---

## 3. Modern JavaScript (ES2022+)

### Nullish Coalescing & Optional Chaining

```typescript
const value = config.timeout ?? 5000;  // only null/undefined, not 0 or ''
const name = user?.profile?.name ?? 'Anonymous';
```

### Top-Level Await

```typescript
// In ES modules
const data = await fetch('/api/config').then(r => r.json());
export const config = data;
```

### Private Class Fields

```typescript
class Counter {
  #count = 0;  // truly private, not just convention

  increment() {
    this.#count++;
    return this.#count;
  }

  get #formatted() {  // private getter
    return `Count: ${this.#count}`;
  }
}
```

### Array Methods

```typescript
const nums = [1, 2, 3, 4, 5];

// Modern methods (no mutation)
const doubled = nums.map(n => n * 2);
const evens = nums.filter(n => n % 2 === 0);
const sum = nums.reduce((a, b) => a + b, 0);
const firstEven = nums.find(n => n % 2 === 0);  // number | undefined
const hasEven = nums.some(n => n % 2 === 0);
const allPositive = nums.every(n => n > 0);

// toSorted, toReversed, toSpliced (ES2023 — non-mutating)
const sorted = nums.toSorted((a, b) => b - a);
const reversed = nums.toReversed();
```

---

## 4. React 19+ Patterns

### Server Components (Next.js App Router)

```tsx
// app/page.tsx — Server Component by default
import { db } from '@/lib/db';

export default async function Page() {
  const users = await db.query('SELECT * FROM users');  // runs on server

  return (
    <main>
      <h1>Users</h1>
      <UserList users={users} />
      <UserForm />  {/* Client Component */}
    </main>
  );
}

// components/UserForm.tsx — Client Component
'use client';

import { useState } from 'react';

export function UserForm() {
  const [name, setName] = useState('');
  // ... client-side interactivity
}
```

### Hooks Best Practices

```tsx
import { useState, useEffect, useCallback, useMemo, useRef } from 'react';

// Custom hook for data fetching
function useApi<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const controller = new AbortController();
    fetch(url, { signal: controller.signal })
      .then(r => r.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, [url]);

  return { data, error, loading };
}

// Usage
function UserProfile({ userId }: { userId: string }) {
  const { data: user, error, loading } = useApi<User>(`/api/users/${userId}`);

  if (loading) return <Skeleton />;
  if (error) return <ErrorMessage error={error} />;
  if (!user) return <NotFound />;

  return <UserCard user={user} />;
}
```

### useMemo / useCallback

```tsx
// ✅ Use when computation is expensive
const sortedUsers = useMemo(
  () => users.sort((a, b) => a.name.localeCompare(b.name)),
  [users]
);

// ✅ Use when passing callbacks to optimized children
const handleSubmit = useCallback(
  (data: FormData) => {
    api.submit(data);
  },
  []
);

// ❌ Don't overuse — React is fast enough for simple cases
```

### React 19 Actions

```tsx
// Server Actions (Next.js)
'use server';

export async function createUser(formData: FormData) {
  'use server';
  const name = formData.get('name') as string;
  await db.insert('users', { name });
  revalidatePath('/users');
}

// Client usage with useActionState
import { useActionState } from 'react';

function UserForm() {
  const [state, formAction, pending] = useActionState(createUser, null);

  return (
    <form action={formAction}>
      <input name="name" required />
      <button disabled={pending}>
        {pending ? 'Creating...' : 'Create'}
      </button>
      {state?.error && <p>{state.error}</p>}
    </form>
  );
}
```

---

## 5. State Management

### Zustand (Recommended)

```typescript
import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

interface UserStore {
  user: User | null;
  setUser: (user: User | null) => void;
  logout: () => void;
}

export const useUserStore = create<UserStore>()(
  devtools(
    persist(
      (set) => ({
        user: null,
        setUser: (user) => set({ user }),
        logout: () => set({ user: null }),
      }),
      { name: 'user-storage' }
    )
  )
);

// Usage
function Profile() {
  const { user, logout } = useUserStore();
  // ...
}
```

### TanStack Query (Server State)

```typescript
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

// Fetch
function useUsers() {
  return useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json()),
    staleTime: 5 * 60 * 1000,  // 5 minutes
  });
}

// Mutate
function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (user: NewUser) =>
      fetch('/api/users', { method: 'POST', body: JSON.stringify(user) }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });
}
```

---

## 6. Testing

### Vitest (Recommended over Jest)

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
  },
});
```

```typescript
// src/utils/calculate.test.ts
import { describe, it, expect } from 'vitest';
import { calculateTotal } from './calculate';

describe('calculateTotal', () => {
  it('sums items correctly', () => {
    const items = [
      { price: 10, quantity: 2 },
      { price: 5, quantity: 1 },
    ];
    expect(calculateTotal(items)).toBe(25);
  });

  it('handles empty cart', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('throws on negative price', () => {
    expect(() => calculateTotal([{ price: -1, quantity: 1 }]))
      .toThrow('Price must be positive');
  });
});
```

### React Testing Library

```tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { UserForm } from './UserForm';

it('submits form with user data', async () => {
  const onSubmit = vi.fn();
  render(<UserForm onSubmit={onSubmit} />);

  fireEvent.change(screen.getByLabelText(/name/i), {
    target: { value: 'Alice' },
  });
  fireEvent.click(screen.getByRole('button', { name: /submit/i }));

  await waitFor(() => {
    expect(onSubmit).toHaveBeenCalledWith({ name: 'Alice' });
  });
});
```

### Playwright (E2E)

```typescript
// tests/e2e/login.spec.ts
import { test, expect } from '@playwright/test';

test('user can log in', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name="email"]', 'user@example.com');
  await page.fill('[name="password"]', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});
```

---

## 7. Linting & Formatting

### ESLint (Flat Config)

```javascript
// eslint.config.js
import js from '@eslint/js';
import ts from 'typescript-eslint';
import react from 'eslint-plugin-react';
import reactHooks from 'eslint-plugin-react-hooks';
import prettier from 'eslint-config-prettier';

export default [
  js.configs.recommended,
  ...ts.configs.recommendedTypeChecked,
  react.configs.flat.recommended,
  reactHooks.configs['recommended-latest'],
  prettier,
  {
    languageOptions: {
      parserOptions: {
        project: './tsconfig.json',
      },
    },
    rules: {
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/explicit-function-return-type': 'off',
      'react/react-in-jsx-scope': 'off',
      'react/prop-types': 'off',
    },
  },
];
```

### Prettier

```json
// .prettierrc
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100
}
```

---

## 8. Node.js Backend

### Fastify (Recommended over Express)

```typescript
import fastify from 'fastify';
import { z } from 'zod';

const app = fastify({ logger: true });

// Validation with Zod
const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
  age: z.number().min(0).optional(),
});

app.post('/users', async (request, reply) => {
  const body = createUserSchema.parse(request.body);
  const user = await db.users.create(body);
  reply.status(201).send(user);
});

// Error handler
app.setErrorHandler((error, request, reply) => {
  app.log.error(error);
  if (error instanceof z.ZodError) {
    reply.status(400).send({ error: 'Validation failed', details: error.errors });
    return;
  }
  reply.status(500).send({ error: 'Internal server error' });
});

await app.listen({ port: 3000 });
```

### tRPC (Type-Safe APIs)

```typescript
// server/router.ts
import { initTRPC } from '@trpc/server';
import { z } from 'zod';

const t = initTRPC.create();

export const appRouter = t.router({
  user: t.router({
    get: t.procedure
      .input(z.object({ id: z.string() }))
      .query(async ({ input }) => {
        return db.users.findById(input.id);
      }),
    create: t.procedure
      .input(z.object({ name: z.string(), email: z.string().email() }))
      .mutation(async ({ input }) => {
        return db.users.create(input);
      }),
  }),
});

export type AppRouter = typeof appRouter;

// client usage
import { createTRPCReact } from '@trpc/react-query';
const trpc = createTRPCReact<AppRouter>();

// Fully type-safe: autocomplete works for 'user.get', 'user.create'
const { data } = trpc.user.get.useQuery({ id: '123' });
```

---

## 9. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| React/Next.js patterns | `python-development` | FastAPI backend for full-stack |
| Docker for JS apps | `docker-containerization` | Multi-stage builds, Node.js images |
| K8s deployment | `kubernetes-orchestration` | Manifests for JS services |
| Security | `security-analysis` | OWASP for web apps, auth patterns |
| Testing | `evolutionary-architecture` | Fitness functions, architecture tests |

---

## 10. Bun Runtime Deep Dive

Bun is an all-in-one JavaScript runtime (faster than Node.js), bundler, test runner, and package manager.

### Bun vs Node.js

| Feature | Bun | Node.js |
|---|---|---|
| Runtime speed | ~3x faster | Baseline |
| Package manager | Built-in (`bun install`) | npm (external) |
| Bundler | Built-in (`bun build`) | webpack/esbuild/rollup (external) |
| Test runner | Built-in (`bun test`) | jest/vitest (external) |
| TypeScript | Native (no `ts-node`) | Requires transpilation |
| ESM/CJS | Both, seamless | ESM still experimental in some cases |
| `.env` loading | Built-in (`Bun.env`) | Requires `dotenv` package |
| File I/O | `Bun.file()` — fast native | `fs` module |
| SQLite | Built-in (`bun:sqlite`) | Requires `better-sqlite3` |
| Web APIs | Native `fetch`, `WebSocket` | Added in v18+ |

### Bun Server (Drop-in for Express/Fastify)

```typescript
// server.ts — native TypeScript, no build step needed
const server = Bun.serve({
  port: 3000,
  fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === '/api/users') {
      return Response.json([{ id: 1, name: 'Alice' }]);
    }

    if (url.pathname === '/api/upload' && req.method === 'POST') {
      const formData = await req.formData();
      const file = formData.get('file') as File;
      await Bun.write(`./uploads/${file.name}`, file);
      return Response.json({ uploaded: file.name });
    }

    return new Response('Not Found', { status: 404 });
  },
});

console.log(`Server running at http://localhost:${server.port}`);
```

### Bun SQLite (Built-in)

```typescript
import { Database } from 'bun:sqlite';

const db = new Database('app.db');

// Create table
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`);

// Prepared statement (fast, safe from SQL injection)
const insert = db.prepare('INSERT INTO users (email) VALUES (?)');
insert.run('alice@example.com');

// Query with typed results
const query = db.query<{ id: number; email: string }, []>(
  'SELECT id, email FROM users WHERE created_at > datetime("now", "-7 days")'
);
const recentUsers = query.all();
// recentUsers: { id: number; email: string }[]
```

### Bun File I/O

```typescript
// Read file — returns Blob, lazy loading
const file = Bun.file('./data.json');
const text = await file.text();        // string
const json = await file.json();        // parsed JSON
const arrayBuffer = await file.arrayBuffer();

// Write file — fast, uses fastest system call
await Bun.write('./output.json', JSON.stringify(data));

// Stream large files
const writer = Bun.file('./large.zip').writer();
for await (const chunk of readableStream) {
  writer.write(chunk);
}
writer.end();
```

### Bun Testing

```typescript
// math.test.ts — Jest-compatible API, built-in
import { describe, test, expect } from 'bun:test';

describe('math', () => {
  test('adds numbers', () => {
    expect(1 + 1).toBe(2);
  });

  test('async operations', async () => {
    const result = await fetch('http://localhost:3000/api/health');
    expect(result.status).toBe(200);
  });

  test('snapshot testing', () => {
    expect({ name: 'bun', version: '1.0' }).toMatchSnapshot();
  });
});

// Run: bun test (auto-discovers *.test.ts)
```

### Bun Bundling

```bash
# Bundle for production — replaces webpack/esbuild
bun build ./src/index.ts --outdir ./dist --target bun

# Bundle for browser
bun build ./src/index.ts --outdir ./dist --target browser

# Bundle for Node.js compatibility
bun build ./src/index.ts --outdir ./dist --target node

# Minify + sourcemap
bun build ./src/index.ts --outdir ./dist --minify --sourcemap
```

### Bun in Docker

```dockerfile
# Dockerfile — multi-stage with Bun
FROM oven/bun:1-alpine AS builder
WORKDIR /app
COPY package.json bun.lockb ./
RUN bun install --frozen-lockfile
COPY . .
RUN bun build ./src/server.ts --outdir ./dist --target bun

FROM oven/bun:1-alpine AS runtime
WORKDIR /app
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["bun", "./dist/server.js"]
```

### Bun Environment

```typescript
// .env loaded automatically — no dotenv needed
const apiKey = Bun.env.API_KEY;        // string | undefined
const port = Number(Bun.env.PORT) || 3000;

// Or use process.env (backward compatible)
const nodeEnv = process.env.NODE_ENV || 'development';
```

---

## 11. pnpm Monorepo Deep Dive

pnpm workspaces are the most disk-efficient and strict monorepo solution.

### Workspace Structure

```
my-monorepo/
├── pnpm-workspace.yaml
├── package.json          # root scripts + shared devDeps
├── pnpm-lock.yaml
├── turbo.json            # (optional) build pipeline
├── packages/
│   ├── ui/               # shared UI component library
│   │   ├── package.json  # { "name": "@myrepo/ui" }
│   │   └── src/
│   ├── utils/            # shared utilities
│   │   ├── package.json  # { "name": "@myrepo/utils" }
│   │   └── src/
│   └── types/            # shared TypeScript types
│       ├── package.json  # { "name": "@myrepo/types" }
│       └── src/
└── apps/
    ├── web/              # Next.js app
    │   ├── package.json  # dependencies: { "@myrepo/ui": "workspace:*" }
    │   └── src/
    └── api/              # Fastify/Hono API
        ├── package.json
        └── src/
```

### pnpm-workspace.yaml

```yaml
packages:
  - 'packages/*'
  - 'apps/*'
  - '!**/test/**'  # exclude test fixtures
```

### Root package.json

```json
{
  "name": "my-monorepo",
  "private": true,
  "packageManager": "pnpm@9.0.0",
  "scripts": {
    "build": "pnpm -r build",
    "dev": "pnpm --parallel dev",
    "test": "pnpm -r test",
    "lint": "pnpm -r lint",
    "typecheck": "pnpm -r typecheck",
    "clean": "pnpm -r exec rm -rf dist node_modules/.cache"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.5.0",
    "eslint": "^9.0.0",
    "prettier": "^3.0.0"
  }
}
```

### Workspace Dependencies

```json
// apps/web/package.json
{
  "name": "@myrepo/web",
  "dependencies": {
    "next": "^14.0.0",
    "@myrepo/ui": "workspace:*",      // always use local version
    "@myrepo/utils": "workspace:^"     // use local, compatible with publish
  },
  "devDependencies": {
    "@myrepo/types": "workspace:*"
  }
}
```

### pnpm Workspace Commands

```bash
# Install all dependencies (creates single node_modules at root + per-package)
pnpm install

# Add dependency to specific workspace
pnpm --filter @myrepo/web add next
pnpm --filter @myrepo/ui add -D @types/react

# Add workspace-internal dependency
pnpm --filter @myrepo/web add @myrepo/ui --workspace

# Run script in all workspaces
pnpm -r build                    # sequential (respects topo order)
pnpm --parallel dev              # parallel (for dev servers)

# Run script in specific workspace
pnpm --filter @myrepo/web dev

# Execute command in all workspaces
pnpm -r exec tsc --noEmit        # type-check all

# Clean everything
pnpm -r exec rm -rf dist node_modules
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

### pnpm Catalogs (pnpm 9.5+) — Unified Versions

```yaml
# pnpm-workspace.yaml
packages:
  - 'packages/*'
  - 'apps/*'

catalog:
  react: ^18.3.1
  react-dom: ^18.3.1
  typescript: ^5.5.0
  eslint: ^9.0.0

catalogs:
  types:
    '@types/react': ^18.3.3
    '@types/node': ^20.14.0
```

```json
// apps/web/package.json — use catalog version
{
  "dependencies": {
    "react": "catalog:",
    "react-dom": "catalog:"
  },
  "devDependencies": {
    "@types/react": "catalog:types"
  }
}
```

### pnpm Overrides — Emergency Patches

```json
// package.json — force specific version everywhere
{
  "pnpm": {
    "overrides": {
      "lodash": "4.17.21",
      "vite@<5.0.0": "5.0.0"
    }
  }
}
```

### pnpm + Turbo (Build Pipeline)

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["build"]
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

```bash
# Run with Turbo — caches builds, skips unchanged packages
npx turbo build
npx turbo test
npx turbo dev --filter=@myrepo/web
```

---

## References

- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [React Documentation](https://react.dev/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Vitest Documentation](https://vitest.dev/)
- [TanStack Query](https://tanstack.com/query/latest)
- [Zustand](https://github.com/pmndrs/zustand)
- [tRPC](https://trpc.io/)
- [Fastify](https://www.fastify.io/)
- [Bun Documentation](https://bun.sh/docs)
- [pnpm Workspaces](https://pnpm.io/workspaces)
- [pnpm Catalogs](https://pnpm.io/catalogs)
- [Turbo Repo](https://turbo.build/)
