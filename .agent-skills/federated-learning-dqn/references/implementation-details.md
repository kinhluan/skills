# Personal Implementation: Federated Service Time Prediction

This document details the FL + DQN architecture for cross-hospital service time prediction and resource optimization.

## 🔮 FL Task: Service Time Prediction
The goal is to predict $T_{service}$ for each ESI triage level without sharing patient data.

```python
# Model predicts service time based on ESI, Age, Comorbidities
class ServiceTimePredictor(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1) # Output: Predicted Time
        )

# Federated Aggregation (FedAvg) 
# aggregates local Hospital models into a global Service Time Predictor
```

## 🤖 DQN Task: Real-time Resource Allocation
The DQN agent optimizes the allocation of hospital resources across the 5 ESI queues.

| Component | Description |
| :--- | :--- |
| **State** | `[Predicted_Service_Times, Current_Queue_Lengths, Available_Staff]` |
| **Action** | Re-allocation of staff to specific ESI queues. |
| **Reward** | $- (\sum wait\_time) - (\alpha \times overutilization)$ |

## 🛡️ Privacy Logic (Opacus)
Ensuring that model updates during "Service Time Prediction" training are differentially private.
