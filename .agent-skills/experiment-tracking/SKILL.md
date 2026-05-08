---
name: experiment-tracking
description: Track, log, compare, and reproduce experiments. Use when running experiments, recording results, comparing baselines, debugging poor performance, analyzing results, or preparing results tables for a paper.
metadata:
  tags: ["research", "phd", "experiment", "tracking", "results", "reproducibility"]
  version: 1.0.0
  triggers:
    - "Log experiment results"
    - "Compare baselines"
    - "Track my experiments"
    - "Results table"
    - "My experiment is not converging"
    - "Reproduce results"
    - "Analyze experiment"
---

# Experiment Tracking

Systematic logging and analysis of experiments. Prevents re-running the same failed experiment twice.

## Experiment Log Entry

For every experiment run, record:

```yaml
# experiments/exp_<ID>_<YYYYMMDD>.yaml
id: exp_042
date: 2026-05-08
status: completed  # running / completed / failed / abandoned

hypothesis: "Adding momentum to aggregation reduces communication rounds"
method: FedMomentum
variant: full  # or ablation variant name

config:
  dataset: MNIST-FL
  clients: 100
  rounds: 200
  local_epochs: 5
  lr: 0.01
  momentum: 0.9
  seed: 42

results:
  accuracy: 94.3 ± 0.4
  comm_rounds_to_95: 87
  total_comm_mb: 1240
  wall_time_min: 43

baseline_comparison:
  FedAvg: 92.1 ± 0.6 (comm_rounds=134)
  delta_accuracy: +2.2%
  delta_efficiency: -35% rounds

observations: "Convergence faster but last 5% accuracy harder to reach"
next_step: "Try momentum=0.95, check if plateau earlier"
```

## Results Table (paper-ready)

| Method | Accuracy (%) | Comm Rounds | Comm Cost (MB) | Time (min) |
|--------|-------------|-------------|----------------|------------|
| FedAvg [1] | 92.1 ± 0.6 | 134 | 1890 | 67 |
| FedProx [2] | 93.0 ± 0.5 | 118 | 1650 | 61 |
| **Ours** | **94.3 ± 0.4** | **87** | **1240** | **43** |

Format: **bold** = best. Report mean ± std over ≥5 seeds.

## Debugging Poor Results

Follow this diagnostic sequence:

```
1. Sanity check: does method work on tiny dataset / 2 clients?
   → No: implementation bug. Check data loading, loss computation.
   → Yes: continue.

2. Overfit check: train loss ↓ but val loss flat/↑?
   → Regularization needed. Check learning rate, dropout, weight decay.

3. Baseline match: can you reproduce a published baseline?
   → No: your eval setup is wrong. Check metric computation, split.
   → Yes: your method is the problem.

4. Hyperparameter sensitivity: sweep lr, rounds, batch size.
   → Use grid search on small scale first.

5. Convergence plot: is loss still decreasing at end of training?
   → Yes: train longer.
   → No, oscillating: lr too high.
   → No, flat early: stuck in local minimum, try different init.
```

## Comparison Workflow

When comparing against baselines:

1. **Same compute budget** — not "same epochs", but same wall-clock or same FLOPs
2. **Same data split** — identical train/val/test, same preprocessing
3. **Fair hyperparameter tuning** — either tune all methods equally or use published best
4. **Statistical test** — don't claim better if p > 0.05

```python
from scipy import stats
results_ours = [94.1, 94.3, 94.5, 94.2, 94.4]
results_baseline = [92.0, 92.3, 91.8, 92.1, 92.2]
stat, p = stats.wilcoxon(results_ours, results_baseline)
print(f"p={p:.4f}, significant: {p < 0.05}")
```

## Reproduce Another Paper's Results

```
1. Find official code (check paper → GitHub → PapersWithCode)
2. Record exact env: Python version, library versions, hardware
3. Run with published hyperparameters first
4. If mismatch >2%: check random seed, data version, metric definition
5. Document: "We reproduced X achieving Y% (paper reports Z%)"
```

## Experiment Index

Maintain `experiments/README.md`:
```markdown
| ID | Date | Method | Dataset | Key Result | Status |
|----|------|--------|---------|------------|--------|
| exp_042 | 2026-05-08 | FedMomentum | MNIST-FL | 94.3% | ✅ |
| exp_041 | 2026-05-07 | FedMomentum | MNIST-FL | 93.1% (lr=0.001) | ✅ |
```

## Links to Other Skills
- Requires → `research-design` (protocol defines what to track)
- Feeds into → `paper-writing` (Results + Experiments sections)
- Iterates with → `sota-survey` (discover new baselines mid-experiment)
