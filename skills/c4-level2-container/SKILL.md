---
name: c4-level2-container
description: Create or review a C4 container diagram showing the separately runnable/deployable applications and data stores inside one software system, their responsibilities, technologies, and relationships. Use for C4 Level 2 architecture views, not physical deployment topology.
metadata:
  tags: ["architecture", "c4", "container-diagram", "software-system", "boundaries"]
---

# C4 Level 2: Container Diagram

In the C4 model, a container is an application or data store that must be running for the software system to work. It is not necessarily a Docker container, Kubernetes workload, virtual machine, process, repository, or team.

Keep the logical container view separate from a C4 deployment diagram:

- Container diagram: applications/data stores, responsibilities, technologies, and communication.
- Deployment diagram: instances of software systems/containers deployed onto infrastructure nodes in a particular environment.

A single C4 container may have multiple runtime instances, sidecars, jobs, or infrastructure resources. Conversely, a deployment unit can package more than one logical concern. Record the mapping in a deployment view only when it is useful.

## Workflow

1. Confirm the software system boundary and audience.
2. Read the Level 1 context view or reconstruct people and external systems.
3. Inspect runtime entry points, build artifacts, data stores, and communication paths.
4. Identify logical applications/data stores by responsibility and runtime boundary.
5. Draw relationships with purpose and protocol/technology where useful.
6. Compare the view with code and runtime evidence.
7. Create a separate deployment diagram if the question concerns nodes, regions, clusters, replicas, or environment topology.

## Evidence Sources

- application entry points and build manifests;
- deployment descriptors, process managers, and infrastructure configuration;
- database/message schemas and ownership;
- API clients, network policies, runtime traces, and service catalog;
- operator and developer confirmation.

Do not assume every `Dockerfile` is a distinct C4 container or that every directory is independently runnable.

## Element Rules

For each container, record:

- name;
- type (application or data store);
- one-sentence responsibility;
- primary technology;
- owned data, if applicable;
- relationships to people, external systems, and other containers.

Useful examples include server-side web applications, single-page applications, mobile apps, APIs, background processors, databases, file stores, and message brokers. Managed services can be containers inside the system boundary or external systems depending on ownership and the view's story.

## Relationship Rules

Label why one element communicates with another. Add protocol/technology only when known and valuable. Show direction clearly. Do not turn the structural view into a request-by-request flowchart; use a dynamic diagram for a scenario.

## Common Mistakes

- showing classes, libraries, modules, or shared utilities as containers;
- equating “container” with Docker/Kubernetes;
- adding regions, nodes, replicas, load balancers, and pods to a logical container view;
- inventing one database per service as a universal rule;
- hiding a genuinely shared database rather than showing it and documenting coupling;
- choosing microservices because the diagram looks cleaner;
- drawing relationships without responsibility or evidence;
- overloading one view instead of creating scoped views for different stories.

## Review Checklist

- [ ] The system boundary is explicit.
- [ ] Every element is a runnable application or data store.
- [ ] Names and responsibilities are technology-neutral enough to explain purpose.
- [ ] Technologies and relationships match current evidence.
- [ ] External systems and people remain visible when relevant.
- [ ] Shared data ownership and coupling are represented honestly.
- [ ] Deployment topology is in a separate deployment view.
- [ ] The diagram has a title, scope, legend, and last-verified date.

## Output

Return:

1. audience and scope;
2. container inventory with evidence;
3. diagram source (Structurizr DSL, PlantUML, Mermaid, or the repository's format);
4. assumptions and unresolved boundaries;
5. validation against code/runtime;
6. whether a separate deployment view is needed.

## Primary References

- [C4 container diagram](https://c4model.com/diagrams/container)
- [C4 deployment diagram](https://c4model.com/diagrams/deployment)
- [Structurizr DSL](https://docs.structurizr.com/dsl)
