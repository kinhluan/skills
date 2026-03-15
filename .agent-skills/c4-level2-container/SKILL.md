---
name: c4-level2-container
description: Specialized in Container diagrams (Level 2) with Infrastructure mapping. Use this skill when the user requests decomposing systems into separately deployable units, identifying the tech stack, and mapping infrastructure components (Docker, K8s).
metadata:
---

# C4 Level 2: Container Diagram & Infrastructure Mapping

The Container diagram represents the high-level **technical architecture** (web apps, mobile apps, databases, background jobs).

## 🎯 Stakeholder Focus
- **Architects:** High-level tech decisions and API boundaries.
- **Developers:** High-level system structure and cross-app communication.
- **Ops/DevOps:** Deployment strategy and infrastructure mapping.

## 🛠 Infrastructure Mapping
Level 2 should ideally map to actual infrastructure components:
- **Web App/Mobile App:** Maps to a build artifact or deployment.
- **API/Service:** Maps to a Docker container or K8s deployment.
- **Database:** Maps to a managed cloud DB or persistent container.
- **Message Broker:** Maps to Kafka, RabbitMQ, or Pub/Sub.

## 🚫 Anti-Patterns to Guard (Level 2)
- **NOT A FLOWCHART:** Avoid modeling complex business logic; use a sequence diagram for that.
- **NO LIBRARIES:** Shared libraries (DLL, JAR, NuGet) are NOT containers.
- **READABILITY:** If the system has >10 containers, consider multiple Level 2 views (e.g., "Customer View", "Admin View").

## 🔍 Codebase Scanning (L2 Synthesis)
To identify containers in an existing codebase, scan for:
- **Build manifests:** `package.json`, `pom.xml`, `go.mod`, `requirements.txt`.
- **Docker files:** `Dockerfile`, `docker-compose.yml`.
- **Infrastructure:** `Terraform` files, `k8s/` manifests.

## Mermaid Template (Enhanced C4Container)
```mermaid
C4Container
    title [System Name] - Container Diagram

    Person(customer, "User", "Uses the system to browse products.")
    
    System_Boundary(my_system, "System Name") {
        Container(web_app, "Web App", "React/TypeScript", "User interface for browsing products.")
        Container(api_svc, "API Service", "Go/gRPC", "Main business logic and API gateway.")
        ContainerDb(user_db, "User DB", "PostgreSQL", "Stores user profiles and history.")
        Container(worker, "Order Processor", "NodeJS/TS", "Processes background order tasks.")
    }
    
    System_Ext(bank, "Bank API", "REST API")

    Rel(customer, web_app, "Uses", "HTTPS")
    Rel(web_app, api_svc, "Calls API", "JSON/HTTPS")
    Rel(api_svc, user_db, "Reads/Writes", "gRPC/TCP")
    Rel(api_svc, worker, "Triggers processing", "Pub/Sub")
    Rel(worker, bank, "Finalizes payment", "HTTPS/REST")
```

## Level 2 Success Criteria
- [ ] Are all containers separately deployable units?
- [ ] Are all cross-container protocols (JSON, SQL, gRPC) specified?
- [ ] Is the diagram readable and clearly bounded?
- [ ] **SMART:** Do the containers match build/deployment artifacts in the code?
