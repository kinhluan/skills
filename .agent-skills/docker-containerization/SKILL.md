---
name: docker-containerization
description: Docker containerization best practices and patterns
metadata:
  tags: ["docker", "containers", "devops", "deployment", "compose"]
---

# Docker & Containerization

Best practices for Docker and containerized applications.

## When to Use

- Containerizing applications
- Writing or optimizing Dockerfiles
- Setting up development or production environments

## Dockerfile Best Practices

### Multi-Stage Builds

```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Security Practices

```dockerfile
# Use specific versions, not latest
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser
USER appuser

# Minimize layers and cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    package \
    && rm -rf /var/lib/apt/lists/*
```

### .dockerignore

```
node_modules
.git
*.log
.env
.DS_Store
```

## Docker Compose

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db
  
  db:
    image: postgres:15-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## Resources

- [Docker Docs](https://docs.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
