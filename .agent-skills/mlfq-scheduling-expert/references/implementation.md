# Personal Implementation: MLFQ for ESI Triage

This document contains the Python logic for a 5-level MLFQ scheduler mapped to the Emergency Severity Index (ESI).

## 🏥 ESI to Queue Mapping ($K=5$)

| Queue Index | ESI Level | Category | Time Quantum ($Q_i$) |
| :--- | :--- | :--- | :--- |
| **Q0** | ESI 1 | Resuscitation (Immediate) | Shortest / Highest Priority |
| **Q1** | ESI 2 | Emergent (High Risk) | Short |
| **Q2** | ESI 3 | Urgent | Medium |
| **Q3** | ESI 4 | Less Urgent | Long |
| **Q4** | ESI 5 | Non-Urgent | Longest / Lowest Priority |

## 🧱 MLFQ Logic with Aging Mechanism

```python
class HealthcareMLFQScheduler:
    def __init__(self, aging_threshold=30):
        self.K = 5
        self.queues = [[] for _ in range(self.K)]
        self.aging_threshold = aging_threshold # in minutes/steps
        
    def triage_patient(self, patient):
        """Initial mapping based on ESI Level (1-5)."""
        queue_idx = patient.esi_level - 1
        self.queues[queue_idx].append(patient)
    
    def apply_aging(self):
        """
        Aging Mechanism: Moves long-waiting patients to higher priority 
        to prevent starvation in ESI 4 & 5.
        """
        for i in range(1, self.K): # From Q1 down to Q4
            for patient in self.queues[i][:]:
                if patient.wait_time > self.aging_threshold:
                    self.queues[i-1].append(patient)
                    self.queues[i].remove(patient)
                    patient.wait_time = 0 # Reset wait after boost
```

## 🤖 RL/DQN Action Space: Resource Allocation
The DQN agent decides how to allocate resources (Doctors/Beds) to these 5 queues:
- **Action:** `[Alloc_Q0, Alloc_Q1, Alloc_Q2, Alloc_Q3, Alloc_Q4]`
- **Goal:** Balance the load across ESI levels while prioritizing high-acuity cases.
