---
name: docker-containerization
description: Docker containerization best practices and patterns for production deployment. Multi-stage builds, security scanning, health checks, compose, BuildKit, and distroless images.
metadata:
  tags: ["docker", "containers", "devops", "deployment", "compose", "security", "multi-stage"]
---

# Docker & Containerization

Production-grade containerization patterns for multiple languages and deployment scenarios.

---

## 1. Dockerfile Best Practices

### Multi-Stage Builds

```dockerfile
# syntax=docker/dockerfile:1

# === Stage 1: Dependencies ===
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

# === Stage 2: Build ===
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# === Stage 3: Production ===
FROM node:20-alpine AS production
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000

# Security: run as non-root
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Copy only what's needed
COPY --from=deps --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --chown=nodejs:nodejs package.json ./

USER nodejs
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node -e "require('http').get('http://localhost:3000/health', (r) => r.statusCode === 200 ? process.exit(0) : process.exit(1))"

CMD ["node", "dist/main.js"]
```

### Python Multi-Stage

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.12-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
RUN pip install --user -e ".[dev]"

# === Runtime ===
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN useradd --create-home --uid 1000 appuser && \
    mkdir -p /app && chown appuser:appuser /app

COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

COPY --chown=appuser:appuser src/ ./src/
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Go Distroless

```dockerfile
# syntax=docker/dockerfile:1

FROM golang:1.23-alpine AS builder
WORKDIR /app
RUN apk add --no-cache git ca-certificates tzdata
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o /bin/app ./cmd/api

FROM gcr.io/distroless/static-debian12:nonroot
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /bin/app /app
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/app"]
```

---

## 2. Security

### Non-Root User

```dockerfile
# Alpine
RUN addgroup -g 1001 -S appgroup && \
    adduser -S appuser -u 1001 -G appgroup
USER appuser

# Debian/Ubuntu
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
USER appuser
```

### Minimal Base Images

| Image | Size | Use Case |
|---|---|---|
| `distroless/static` | ~2MB | Go, Rust, static binaries |
| `alpine:latest` | ~5MB | General, has shell for debugging |
| `debian:bookworm-slim` | ~30MB | When glibc needed |
| `chainguard/static` | ~2MB | Hardened, minimal |

### Security Scanning

```bash
# Trivy (recommended)
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image myapp:latest

# Scan before push
trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:latest

# Grype (alternative)
grype myapp:latest

# Docker Scout (Docker Hub)
docker scout cves myapp:latest
```

### .dockerignore

```
# Git
.git
.gitignore

# Dependencies
node_modules
vendor
.venv
__pycache__

# Build outputs
dist
build
coverage
*.test
*.out

# IDE
.vscode
.idea
*.swp

# Docs
*.md
docs/

# Env
.env
.env.*

# OS
.DS_Store
Thumbs.db
```

---

## 3. Docker Compose

### Development

```yaml
# docker-compose.yml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: development
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/app
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes:
      - redisdata:/data

volumes:
  pgdata:
  redisdata:
```

### Production

```yaml
# docker-compose.prod.yml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      target: production
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 128M
    environment:
      - NODE_ENV=production
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

---

## 4. BuildKit Features

```bash
# Enable BuildKit
export DOCKER_BUILDKIT=1

# Build with cache mount (faster rebuilds)
docker build --secret id=npmrc,src=$HOME/.npmrc .

# Dockerfile with cache mount
RUN --mount=type=cache,target=/root/.npm \
    npm ci

# SSH mount for private repos
RUN --mount=type=ssh git clone git@github.com:org/private.git

# Secret mount for build-time secrets
RUN --mount=type=secret,id=api_key \
    API_KEY=$(cat /run/secrets/api_key) npm run build
```

---

## 5. Health Checks

```dockerfile
# HTTP health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# TCP health check
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD nc -z localhost 5432 || exit 1

# Custom script
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD /app/healthcheck.sh
```

---

## 6. Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| Container patterns | `python-development` | Python-specific Docker |
| Container patterns | `golang-development` | Go distroless builds |
| Container patterns | `javascript-typescript` | Node.js multi-stage |
| Orchestration | `kubernetes-orchestration` | K8s deployment |
| Security | `security-analysis` | Image scanning, secrets |
