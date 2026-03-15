# Personal Research Implementation: FL + DQN + MLFQ

This document contains the core logic and code snippets developed for the PhD research on healthcare scheduling.

## 1. Federated Learning (FedAvg) Logic

```python
# Server-side averaging
def federated_averaging(models, weights):
    total = sum(weights)
    averaged = {}
    for key in models[0].state_dict():
        averaged[key] = sum(
            w * model.state_dict()[key] 
            for model, w in zip(models, weights)
        ) / total
    return averaged

# Training Round logic
for round in range(num_rounds):
    clients = select_clients()
    models, weights = [], []
    for client in clients:
        model, weight = client.train(local_epochs)
        models.append(model)
        weights.append(weight)
    global_model.load_state_dict(federated_averaging(models, weights))
```

## 2. Deep Q-Network (DQN) Architecture

```python
import torch.nn as nn

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
            nn.Linear(256, action_dim)
        )
    
    def forward(self, x):
        return self.net(x)
```

## 3. MLFQ Scheduler Integration

```python
class MLFQScheduler:
    def __init__(self, num_queues=3):
        self.queues = [[] for _ in range(num_queues)]
        self.priority_boost = 10
        
    def add_patient(self, patient, priority):
        queue_idx = min(priority, len(self.queues) - 1)
        self.queues[queue_idx].append(patient)
    
    def get_next_patient(self):
        # DQN selects which queue to serve
        queue_state = self.get_queue_state()
        action = dqn_agent.select_action(queue_state)
        
        # Boost priority of waiting patients
        self.boost_priorities()
        
        return self.queues[action].pop(0) if self.queues[action] else None
```

## 4. Healthcare Use Case Definitions

### State Representation
- `queue_lengths`: [len(q) for q in queues]
- `patient_acuity`: average_acuity_per_queue
- `resource_availability`: [beds, staff, equipment]

### Reward Function
```python
def calculate_reward(state, action, next_state):
    reward = 0
    # Minimize wait time (weighted by acuity)
    reward -= sum(patient.wait_time * patient.acuity for patient in all_patients)
    # Penalize queue imbalance
    reward -= variance(queue_lengths) * 10
    # Reward completing high-acuity cases
    reward += completed_high_acuity * 50
    return reward
```

## 5. Differential Privacy Noise

```python
def add_dp_noise(gradients, epsilon, delta, sensitivity):
    sigma = sensitivity * np.sqrt(2 * np.log(1.25 / delta)) / epsilon
    noise = torch.randn_like(gradients) * sigma
    return gradients + noise
```
