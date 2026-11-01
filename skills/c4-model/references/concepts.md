# C4 Model Concepts

The C4 model is a hierarchical approach to describing software architecture, from high-level context to technical details.

## 1. The Hierarchy

### Level 1: System Context
- **Goal:** Show the big picture: how your software system fits into the world around it.
- **Audience:** Non-technical people (users, stakeholders), developers, architects.
- **Content:** Users (Person) and other systems (Software System) that interact with your system. Exclude technical details like programming languages and frameworks.

### Level 2: Container
- **Goal:** Zoom into a single software system to show the containers that make it up.
- **Audience:** Developers, architects, operations staff.
- **Definition:** A "Container" is a separately runnable/deployable unit (e.g., a web application, mobile app, database, microservice).
- **Content:** Containers, how they interact, and key technologies (e.g., React, Spring Boot, MySQL).

### Level 3: Component
- **Goal:** Zoom into a single container to show the components inside it.
- **Audience:** Developers, architects.
- **Definition:** A "Component" is a grouping of related functionality/classes encapsulated behind a clean interface.
- **Content:** Major components within a container (e.g., Auth component, Payment gateway wrapper).

### Level 4: Code
- **Goal:** Describe how a component is implemented (e.g., UML class diagrams, ER diagrams).
- **Audience:** Developers.
- **Recommendation:** Usually optional unless particularly complex or critical.

## 2. Core Elements

- **Person:** An end-user, admin, support staff... (Whoever uses the system).
- **Software System:** A complete software system that provides value to users (your system or a third-party system).
- **Container:** A web app, microservice, database, cloud service... (Separately deployable software).
- **Component:** A logical part of a container (Module, Service class, Repository).

## 3. Relationships

Every arrow between elements should have a label describing the action (e.g., "Sends payment request", "Saves user data") and the technology/protocol (e.g., "HTTPS/JSON", "SQL/TCP").
