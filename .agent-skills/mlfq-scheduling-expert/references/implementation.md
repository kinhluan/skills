# Personal Implementation: MLFQ Scheduler

This document contains the Python implementation of the Multilevel Feedback Queue (MLFQ) scheduler logic.

## 🧱 Core Scheduler Class

```python
class MLFQScheduler:
    def __init__(self, num_queues=3, priority_boost_interval=10):
        self.queues = [[] for _ in range(num_queues)]
        self.priority_boost = priority_boost_interval
        
    def add_task(self, task, initial_priority=0):
        """Adds a task to the specified queue."""
        queue_idx = min(initial_priority, len(self.queues) - 1)
        self.queues[queue_idx].append(task)
    
    def get_next_task(self, selection_strategy="fcfs"):
        """
        Retrieves the next task to serve. 
        Can be integrated with AI (DQN) for strategic selection.
        """
        for i, queue in enumerate(self.queues):
            if queue:
                return queue.pop(0)
        return None
    
    def boost_priorities(self):
        """Moves all tasks to the highest priority queue to avoid starvation."""
        all_tasks = []
        for queue in self.queues:
            all_tasks.extend(queue)
            queue.clear()
        self.queues[0] = all_tasks

    def handle_time_slice_expiry(self, task, current_queue_idx):
        """Downgrades task priority if time slice is fully consumed."""
        new_priority = min(current_queue_idx + 1, len(self.queues) - 1)
        self.queues[new_priority].append(task)
```

## 🤖 AI Integration (Conceptual)

In your PhD research, the `selection_strategy` or the `priority_boost` timing can be determined by a **DQN Agent**:

- **State:** `[len(q0), len(q1), len(q2), mean_wait_time, cpu_utilization]`
- **Action:** `[Serve Q0, Serve Q1, Serve Q2, Boost Now, Do Nothing]`
- **Reward:** `- (total_wait_time) + completion_bonus`
