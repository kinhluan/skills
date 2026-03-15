---
name: mlfq-scheduling-expert
description: Healthcare-grade MLFQ Scheduling. Specifically for ESI 1-5 triage levels ($K=5$ queues) with dynamic aging mechanisms to prevent patient starvation in low-priority queues.
metadata:
  tags: ["healthcare-it", "mlfq", "triage-scheduling", "esi-levels"]
---

# MLFQ Scheduling Expert (Healthcare Focus)

This skill specializes in Multilevel Feedback Queue scheduling tailored for Emergency Departments using the **Emergency Severity Index (ESI)**.

## 🏥 Triage-to-Queue Mapping ($K=5$)
- **Queue 0 (ESI 1):** Immediate resuscitation cases. Highest priority.
- **Queue 1 (ESI 2):** High-risk/emergent cases.
- **Queue 2 (ESI 3):** Urgent cases.
- **Queue 3 (ESI 4):** Less urgent.
- **Queue 4 (ESI 5):** Non-urgent cases. Lowest priority.

## ⚙️ Aging Mechanism (Starvation Prevention)
To ensure ESI 4 & 5 patients are eventually seen, implement a **wait-time based priority boost**:
- **Rule:** If `wait_time > T_threshold`, move the patient to the next higher priority queue.

## 📊 Performance Optimization
Use this skill to optimize:
- **Time Quantums** per ESI level.
- **Aging Thresholds** ($T$) based on hospital occupancy.
- **Resource Allocation** across the 5 queues using AI models.

## 🧠 Implementation Details
For the Python logic of the ESI-mapped MLFQ and Aging mechanism, see [implementation.md](./references/implementation.md).
