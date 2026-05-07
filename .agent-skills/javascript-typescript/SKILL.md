---
name: javascript-typescript
description: JavaScript and TypeScript development best practices
metadata:
  tags: ["javascript", "typescript", "frontend", "backend", "nodejs"]
---

# JavaScript & TypeScript

Best practices for JavaScript and TypeScript development.

## When to Use

- Writing frontend or backend JavaScript/TypeScript code
- Setting up new Node.js or browser projects
- Code review and refactoring

## TypeScript Guidelines

### Strict Mode

Always enable strict mode in `tsconfig.json`:

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true
  }
}
```

### Type Best Practices

```typescript
// Prefer interfaces for object shapes
interface User {
  id: string;
  name: string;
  email: string;
}

// Use union types for alternatives
type Status = 'idle' | 'loading' | 'success' | 'error';

// Prefer readonly for immutable data
class Config {
  readonly apiUrl: string;
}
```

## JavaScript Patterns

### Async/Await

```javascript
// Prefer async/await over promise chains
async function fetchData(url) {
  const response = await fetch(url);
  return response.json();
}
```

### Error Handling

```javascript
try {
  await operation();
} catch (error) {
  logger.error('Operation failed', { error });
  throw error; // Re-throw or handle
}
```

## Resources

- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
