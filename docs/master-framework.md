# Product-Led Engineering: The Master Framework

This master guide integrates **Business Strategy** with **Technical Architecture** to create a seamless flow from market discovery to high-velocity code delivery.

## 1. The End-to-End Unified Flow

This diagram shows how all the components in this repository work together.

```mermaid
graph TD
    %% Business & Strategy Layer
    subgraph Layer_1_Strategy [1. Business & Strategy]
        LMR[Market Research] --> Gap[Market Gap]
        Gap --> JTBD[Jobs-To-Be-Done]
    end

    %% Architecture Layer
    subgraph Layer_2_Architecture [2. Technical Architecture]
        JTBD --> Strategic_DDD[Strategic DDD: Bounded Contexts]
        Strategic_DDD --> C4_L1[C4 Level 1: System Context]
        C4_L1 --> C4_L2[C4 Level 2: Containers]
        C4_L2 --> Tactical_DDD[Tactical DDD: Aggregates]
        Tactical_DDD --> C4_L3[C4 Level 3: Components]
    end

    %% Execution Layer
    subgraph Layer_3_Execution [3. Lean Execution]
        C4_L3 --> Ship[Technical Shipping: CI/CD/Flags]
        Ship --> Feedback{User Feedback}
        Feedback -->|Pivot/Refine| LMR
        Feedback -->|Release| Market[Full Market Release]
    end

    %% Styles
    style Layer_1_Strategy fill:#dfd,stroke:#333
    style Layer_2_Architecture fill:#bbf,stroke:#333
    style Layer_3_Execution fill:#f9f,stroke:#333
```

## 2. Integrated Workflow Reference

| Phase | Methodology | Goal | Reference Guide |
| :--- | :--- | :--- | :--- |
| **Discovery** | LMR & JTBD | Validate Market Demand | [Business Leadership](./business-product-leadership.md) |
| **Scoping** | Strategic DDD & C4 L1 | Define Boundaries & Ecosystem | [C4 & DDD Mapping](./ddd-c4-mapping.md) |
| **Design** | Tactical DDD & C4 L2/3 | Design Internal Domain Logic | [C4 & DDD Mapping](./ddd-c4-mapping.md) |
| **Delivery** | Ship != Release | Decouple Tech vs Business Risk | [Business Leadership](./business-product-leadership.md) |

## 3. The Continuous Alignment Loop

1.  **Business to Tech:** JTBD defines the **Core Domain**. If it's not core to the job, don't over-engineer it.
2.  **Tech to Business:** C4 Level 2 diagrams identify **Independent Ship Units**. Use this to plan your MVP release phases.
3.  **Market to Design:** User feedback from a "Ship" (behind flags) should immediately inform the next iteration of **Event Storming** and **Aggregate** design.

---

## 🚀 How to use this Repository

1.  **For Founders/PMs:** Start with the [Business & Product Leadership Guide](./business-product-leadership.md).
2.  **For Architects:** Start with the [C4 Model & DDD Mapping Guide](./ddd-c4-mapping.md).
3.  **For Teams:** Use the **Master Flow** above to ensure everyone speaks the same **Ubiquitous Language**.
