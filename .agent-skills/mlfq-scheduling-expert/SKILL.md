---
name: mlfq-scheduling-expert
description: Expert-level Multi-Level Feedback Queue (MLFQ) Scheduling. Use this skill for designing complex task schedulers, optimizing time-quantums, and implementing dynamic priority boosting.
metadata:
  tags: ["os-scheduling", "mlfq", "performance-optimization", "resource-management"]
---

# MLFQ Scheduling Expert

Multi-Level Feedback Queue (MLFQ) is a sophisticated scheduling algorithm that balances response time and throughput by dynamically adjusting task priorities.

## ⚙️ Core Mechanisms

1.  **Multiple Queues:** Tasks are organized into $N$ queues with varying priority levels.
2.  **Time Quantum ($Q_i$):** Higher priority queues have shorter time quantums (e.g., $Q_0 = 4ms$, $Q_1 = 8ms$).
3.  **Dynamic Downgrade:** If a task uses its entire time slice without blocking, it is moved to a lower priority queue.
4.  **Priority Boost:** To avoid starvation, all tasks are periodically moved to the highest priority queue (Queue 0).

## 🧪 Optimization Parameters (PhD Focus)

- **$S$ (Boost Interval):** How often to perform a priority boost. Too small increases overhead; too large causes starvation.
- **$Q$ Scaling:** Linear vs. Exponential scaling of time quantums across queues.
- **Feedback Loop:** Using AI (e.g., DQN) to adjust $S$ and $Q$ based on real-time workload statistics.

## 📊 Evaluation Metrics

| Metric | Goal | Description |
| :--- | :--- | :--- |
| **Turnaround Time** | Minimize | Total time from arrival to completion. |
| **Response Time** | Minimize | Time from arrival to first execution (critical for I/O tasks). |
| **Throughput** | Maximize | Number of tasks completed per time unit. |

## 🧠 Implementation Details
For the core Python implementation including queue management and priority boosting logic, see [implementation.md](./references/implementation.md).
