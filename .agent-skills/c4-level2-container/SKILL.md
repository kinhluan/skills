---
name: c4-level2-container
description: Specialized in Container diagrams (Level 2) with Infrastructure mapping. Use this skill when the user requests decomposing systems into separately deployable units, identifying the tech stack, and mapping infrastructure components (Docker, K8s).
metadata:
  tags: ["architecture", "c4-level2", "containers", "devops", "microservices"]
---

# C4 Level 2: Container Diagram & Infrastructure Mapping

The Container diagram represents the high-level **technical architecture** — web apps, mobile apps, databases, background jobs, message brokers. In C4, "Container" means a separately deployable/runnable unit, NOT Docker (though Docker containers often map 1:1).

> "A container is something that needs to be running in order for the overall software system to work." — Simon Brown

---

## 🎯 Stakeholder Focus

| Stakeholder | What they need from L2 | Questions they ask |
|-------------|------------------------|-------------------|
| **Architects** | Tech decisions, API boundaries | "Why Go for API and React for frontend?" |
| **Developers** | System structure, cross-app communication | "How do services talk to each other?" |
| **Ops/DevOps** | Deployment strategy, infrastructure | "How many containers? What needs monitoring?" |
| **Security** | Trust boundaries, data flow | "What protocols encrypt data in transit?" |

---

## 🏗️ Container Types & Mapping

| Container Type | Description | Maps To | Example Tech |
|---------------|-------------|---------|-------------|
| **Web Application** | Browser-based UI | Build artifact (SPA bundle) | React, Vue, Angular |
| **Mobile App** | Native or cross-platform mobile | App store binary | iOS (Swift), Android (Kotlin), Flutter |
| **API Application** | HTTP/gRPC API server | Docker container, K8s deployment | Go, Python/FastAPI, Node.js/Express, Java/Spring |
| **Database** | Persistent data store | Managed DB, persistent volume | PostgreSQL, MySQL, MongoDB, Redis |
| **Message Broker** | Async messaging | K8s StatefulSet, managed service | Kafka, RabbitMQ, AWS SQS, NATS |
| **File Store** | Object/blob storage | Cloud bucket, NFS | S3, GCS, Azure Blob |
| **Background Worker** | Async job processor | K8s CronJob, queue consumer | Celery, Sidekiq, Go worker |
| **Cache** | In-memory data | Redis/Memcached instance | Redis, Memcached |

### Infrastructure Mapping Rules

```
L2 Container          →   Infrastructure Artifact
─────────────────────────────────────────────────────
Web App               →   Docker image + Nginx/CDN
API Service           →   Docker container + K8s Deployment
Database              →   Cloud SQL / RDS / Persistent Volume
Message Broker        →   K8s StatefulSet / Managed Service
Background Worker     →   K8s CronJob / Queue Consumer
Cache                 →   Redis Cluster / ElastiCache
```

---

## 🚫 Anti-Patterns to Guard (Level 2)

| Anti-Pattern | Symptom | Fix |
|-------------|---------|-----|
| **Flowchart Confusion** | Business logic steps in diagram | Use sequence diagram for flows. L2 shows structure, not process |
| **Library as Container** | "Shared Utils", "Common Library" as boxes | Libraries are code (L3/L4), not deployable units |
| **Diagram Overload** | >10 containers in one view | Split: "Customer View", "Admin View", "Data Pipeline View" |
| **Missing Protocols** | Arrows without labels | Every arrow needs protocol: "JSON/HTTPS", "gRPC/TCP", "SQL/TCP" |
| **Shared Database** | Multiple containers → one DB without ownership | Each container should own its data. Shared DB = tight coupling |
| **Missing Boundaries** | Containers floating without system boundary | Wrap in `System_Boundary` to show scope |

---

## 🔍 Codebase Scanning (L2 Synthesis)

To identify containers in an existing codebase, scan for:

### Build Manifests (Tech Stack)
```bash
# JavaScript/TypeScript
package.json → frontend framework, backend runtime

# Go
go.mod → modules, HTTP framework (gin, echo, chi)

# Java
pom.xml / build.gradle → Spring Boot, dependencies

# Python
requirements.txt / pyproject.toml → FastAPI, Django, Flask
```

### Deployment Artifacts
```bash
Dockerfile          → Container definition
docker-compose.yml  → Multi-container setup
k8s/                → Kubernetes manifests
terraform/          → Infrastructure as Code
serverless.yml      → Serverless functions (Lambda, etc.)
```

### Service Boundaries
```bash
# Look for separate entry points
src/main.go         → API service
cmd/worker/main.go  → Background worker
web/                → Frontend application
```

---

## 📝 Mermaid Templates

### Template A: Monolith with Frontend
```mermaid
C4Container
    title Container Diagram for E-Commerce Platform

    Person(customer, "Customer", "Registered user browsing products.")

    System_Boundary(ecommerce, "E-Commerce Platform") {
        Container(web_app, "Web Application", "React/TypeScript", "Customer-facing SPA.")
        Container(api, "API Service", "Go/gRPC", "Business logic, authentication, order processing.")
        ContainerDb(db, "Primary Database", "PostgreSQL", "Users, products, orders, inventory.")
        Container(cache, "Cache", "Redis", "Session store, product catalog cache.")
        Container(worker, "Order Processor", "Go", "Processes payment confirmation, sends emails.")
        ContainerQueue(queue, "Message Queue", "RabbitMQ", "Async order events.")
    }

    System_Ext(payment, "Payment Gateway", "Stripe/PayPal")
    System_Ext(email, "Email Service", "SendGrid")

    Rel(customer, web_app, "Browses, purchases", "HTTPS")
    Rel(web_app, api, "Calls API", "JSON/HTTPS")
    Rel(api, db, "Reads/Writes", "SQL/TCP")
    Rel(api, cache, "Caches data", "Redis Protocol")
    Rel(api, queue, "Publishes events", "AMQP")
    Rel(worker, queue, "Consumes events", "AMQP")
    Rel(worker, email, "Sends emails", "REST API/HTTPS")
    Rel(api, payment, "Processes payments", "REST API/HTTPS")
```

### Template B: Microservices Architecture
```mermaid
C4Container
    title Container Diagram for Microservices Platform

    Person(customer, "Customer", "End user of the platform.")

    Container(api_gateway, "API Gateway", "Kong/AWS API Gateway", "Routing, rate limiting, auth.")
    Container(web_app, "Web App", "Next.js", "Customer-facing UI.")

    System_Boundary(platform, "Platform Services") {
        Container(user_svc, "User Service", "Go/gRPC", "User profiles, authentication.")
        Container(order_svc, "Order Service", "Go/gRPC", "Order creation, status tracking.")
        Container(product_svc, "Product Service", "Python/FastAPI", "Product catalog, search.")
        Container(inventory_svc, "Inventory Service", "Go/gRPC", "Stock levels, reservations.")
        Container(notification_svc, "Notification Service", "Node.js", "Email, SMS, push notifications.")

        ContainerDb(user_db, "User DB", "PostgreSQL", "User data.")
        ContainerDb(order_db, "Order DB", "PostgreSQL", "Order data.")
        ContainerDb(product_db, "Product DB", "MongoDB", "Product documents.")
        ContainerDb(inventory_db, "Inventory DB", "PostgreSQL", "Stock data.")

        ContainerQueue(event_bus, "Event Bus", "Kafka", "Domain events between services.")
    }

    System_Ext(payment, "Payment Gateway", "Stripe")
    System_Ext(search, "Search Engine", "Elasticsearch")

    Rel(customer, web_app, "Uses", "HTTPS")
    Rel(web_app, api_gateway, "Calls APIs", "JSON/HTTPS")
    Rel(api_gateway, user_svc, "Routes to", "gRPC/TLS")
    Rel(api_gateway, order_svc, "Routes to", "gRPC/TLS")
    Rel(api_gateway, product_svc, "Routes to", "gRPC/TLS")

    Rel(user_svc, user_db, "Reads/Writes", "SQL/TCP")
    Rel(order_svc, order_db, "Reads/Writes", "SQL/TCP")
    Rel(product_svc, product_db, "Reads/Writes", "MongoDB Protocol")
    Rel(inventory_svc, inventory_db, "Reads/Writes", "SQL/TCP")

    Rel(order_svc, event_bus, "Publishes OrderPlaced", "Kafka Protocol")
    Rel(inventory_svc, event_bus, "Consumes OrderPlaced", "Kafka Protocol")
    Rel(notification_svc, event_bus, "Consumes OrderPlaced", "Kafka Protocol")

    Rel(order_svc, payment, "Processes payment", "REST API/HTTPS")
    Rel(product_svc, search, "Indexes products", "REST API/HTTPS")
```

### Template C: Serverless / Event-Driven
```mermaid
C4Container
    title Container Diagram for Serverless Data Pipeline

    Person(analyst, "Data Analyst", "Consumes processed data.")

    System_Boundary(pipeline, "Data Pipeline") {
        Container(ingestion, "Ingestion Function", "AWS Lambda / Python", "Receives and validates incoming data.")
        Container(transform, "Transform Function", "AWS Lambda / Python", "Cleans and enriches data.")
        Container(store, "Data Store", "S3", "Raw and processed data files.")
        Container(warehouse, "Data Warehouse", "Snowflake", "Structured data for analytics.")
        Container(scheduler, "Scheduler", "AWS EventBridge", "Triggers pipeline runs.")
    }

    System_Ext(source, "Data Source", "External API / SFTP")
    System_Ext(dashboard, "BI Dashboard", "Tableau / Looker")

    Rel(source, ingestion, "Pushes data", "HTTPS / SFTP")
    Rel(scheduler, ingestion, "Triggers", "EventBridge")
    Rel(ingestion, store, "Stores raw", "S3 API")
    Rel(ingestion, transform, "Invokes", "Lambda Invoke")
    Rel(transform, warehouse, "Loads processed", "Snowflake SQL")
    Rel(analyst, dashboard, "Views reports", "HTTPS")
    Rel(dashboard, warehouse, "Queries", "SQL/JDBC")
```

---

## 🏗️ Deployment Patterns

### Pattern 1: Single Monolith
```
┌─────────────────────────────┐
│  Load Balancer              │
└─────────────┬───────────────┘
              │
    ┌─────────┴─────────┐
    │  Monolithic App   │
    │  (Web + API +     │
    │   Background)     │
    └─────────┬─────────┘
              │
    ┌─────────┴─────────┐
    │  Database         │
    └───────────────────┘
```
**When to use:** Small team (<5), simple domain, rapid prototyping.

### Pattern 2: Frontend + Backend Split
```
┌─────────────┐     ┌─────────────┐
│  CDN/Web    │────▶│  API        │
│  (React)    │     │  (Go/Java)  │
└─────────────┘     └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         ┌────────┐  ┌────────┐  ┌────────┐
         │  DB    │  │ Cache  │  │ Queue  │
         └────────┘  └────────┘  └────────┘
```
**When to use:** Separate frontend/backend teams, different deployment cadences.

### Pattern 3: Microservices with API Gateway
```
                    ┌─────────────┐
                    │  API Gateway │
                    │  (Kong/AWS)  │
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   ┌─────────┐      ┌─────────┐      ┌─────────┐
   │ Service │      │ Service │      │ Service │
   │   A     │      │   B     │      │   C     │
   └────┬────┘      └────┬────┘      └────┬────┘
        │                │                │
        ▼                ▼                ▼
   ┌─────────┐      ┌─────────┐      ┌─────────┐
   │  DB A   │      │  DB B   │      │  DB C   │
   └─────────┘      └─────────┘      └─────────┘
```
**When to use:** Multiple teams, independent deployability, complex domain.

---

## ✅ Level 2 Success Criteria

- [ ] Are all containers separately deployable/runnable units?
- [ ] Are all cross-container protocols (JSON, SQL, gRPC) specified?
- [ ] Is the diagram readable (≤10 containers per view)?
- [ ] **SMART:** Do containers match build/deployment artifacts in the code?
- [ ] **SMART:** Does each container own its data (no shared DB)?
- [ ] Are external systems clearly marked?
- [ ] Is there a system boundary around owned containers?

---

## 🔄 From L2 to L3

When you're ready to zoom into a container:

| L2 Signal | L3 Action |
|-----------|-----------|
| "This container has 5+ responsibilities" | Split into components |
| "Developers don't understand internal structure" | Draw component diagram |
| "We have circular imports" | L3 reveals dependency cycles |
| "This is our Core Domain" | Deep dive with `ddd-tactical` |

**Next:** Use `c4-level3-component` to design internal architecture.

---

## 📚 References

- [C4 Model — Container Diagram](https://c4model.com/#ContainerDiagram) — Simon Brown
- [Structurizr DSL — Container View](https://docs.structurizr.com/dsl/language#container-view)
- [Building Microservices](https://samnewman.io/books/building_microservices/) — Sam Newman
