---
name: c4-level3-component
description: Specialized in Component diagrams (Level 3) with folder structure mapping. Use this skill when the user needs to zoom into a single container to identify internal components, their responsibilities, and how they map to actual code folders (src/services, internal/).
metadata:
---

# C4 Level 3: Component Diagram & Folder Mapping

Level 3 focuses on the **internal architecture** of a single container, bridging the gap between high-level containers and low-level code.

## 🎯 Stakeholder Focus
- **Developers:** Understanding internal module boundaries and dependencies.
- **Architects:** Ensuring proper layering and Separation of Concerns.

## 🛠 Folder Structure Mapping
Level 3 should ideally map to your folder structure:
- **Controller/Handler:** Maps to `src/api`, `internal/handler`.
- **Service/Logic:** Maps to `src/services`, `internal/usecase`.
- **Repository/Data Access:** Maps to `src/db`, `internal/repository`.
- **Infrastructure Wrapper:** Maps to `pkg/email`, `src/adapters`.

## 🚫 Anti-Patterns to Guard (Level 3)
- **OVER-DETAILING:** Don't draw every class. Only draw major logical groupings.
- **MIXING CONTAINERS:** Focus only on ONE container at a time.
- **CIRCULAR DEPENDENCIES:** Level 3 is the best place to identify and fix tight coupling.

## 🔍 Codebase Scanning (L3 Synthesis)
To identify components in a container, scan for:
- **Folder Names:** `services/`, `controllers/`, `handlers/`, `repositories/`, `models/`.
- **Project Structure Patterns:** Layered architecture, Clean Architecture (Hexagonal), or Feature-based folders.

## Mermaid Template (Enhanced C4Component)
```mermaid
C4Component
    title [Container Name] - Component Diagram

    Container(spa, "Web App", "React/TS", "Single Page Application")
    
    Container_Boundary(api_svc, "API Service") {
        Component(order_ctrl, "Order Handler", "Go Handler", "Handles incoming REST requests.")
        Component(order_svc, "Order Service", "Go Logic", "Processes business logic for orders.")
        Component(inv_repo, "Inventory Client", "Go Client", "Wraps calls to the Inventory system.")
        Component(db_repo, "Database Repository", "SQL Client", "Handles SQL queries for orders.")
    }

    ContainerDb(db, "Order Database", "PostgreSQL", "Stores orders.")

    Rel(spa, order_ctrl, "Submits orders", "JSON/HTTPS")
    Rel(order_ctrl, order_svc, "Calls logic", "Method call")
    Rel(order_svc, inv_repo, "Checks stock", "Method call")
    Rel(order_svc, db_repo, "Saves order", "Method call")
    Rel(db_repo, db, "Writes", "SQL/TCP")
```

## Level 3 Success Criteria
- [ ] Does the diagram map directly to the container's folder structure?
- [ ] Are internal interactions (method calls/internal events) clearly labeled?
- [ ] Is it clear how each component contributes to the container's responsibility?
- [ ] **STRICT:** Does it focus only on the zoomed-in container?
