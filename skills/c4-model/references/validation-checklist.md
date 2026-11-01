# Architecture Review Checklist (C4 Model)

Use this checklist to ensure your architectural design adheres to C4 model principles.

## 1. General Checks
- [ ] Every element has a clear name.
- [ ] Every element has a brief description.
- [ ] Every relationship has a label.
- [ ] Every relationship includes technology/protocol information (at Level 2 and above).
- [ ] Diagrams have titles indicating the Level and goal.

## 2. Level 1: System Context
- [ ] **NO** technical details like programming languages, frameworks, or databases.
- [ ] Only shows "Software Systems" and "Persons".
- [ ] The System Under Design is central and prominent.
- [ ] External Systems are clearly distinguished.

## 3. Level 2: Container
- [ ] The system boundary is clearly shown.
- [ ] "Containers" are separately runnable/deployable units (Web App, API, DB).
- [ ] Major technologies are specified for each container (e.g., React, Java, PostgreSQL).
- [ ] Relationships across the system boundary (with external systems/persons) are preserved from Level 1.

## 4. Level 3: Component
- [ ] Only shows significant components within a container.
- [ ] Avoid over-detailing if it doesn't help understand the structure.
- [ ] Ensure clear Separation of Concerns between components.

## 5. Common Pitfalls
- **Pitfall 1: Missing descriptions.** A box without a description (e.g., just "Web App" without saying what it does) loses C4's value.
- **Pitfall 2: Vague relationships.** Avoid labels like "Uses" or "Connects". Use specific verbs like "Sends payment request via", "Fetches order info from".
- **Pitfall 3: Mixing Levels.** Do not draw Containers (Level 2) directly inside a System Context diagram (Level 1).
- **Pitfall 4: Overloaded diagrams.** If a diagram is too complex, split it up or focus on a specific scenario.
