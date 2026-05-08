---
name: research-design
description: Design a rigorous experiment protocol including methodology choice, baselines, metrics, ablation studies, and reproducibility plan. Use before running any experiment, when designing evaluation strategy, or when reviewing experimental validity.
metadata:
  tags: ["research", "phd", "experiment", "methodology", "reproducibility", "ablation"]
  version: 1.0.0
  triggers:
    - "Design experiment"
    - "Choose baselines"
    - "Define evaluation metrics"
    - "Ablation study"
    - "Experimental protocol"
    - "How to evaluate my method"
    - "Reproducibility checklist"
---

# Research Design

Design experiments before running them. Bad design wastes months.

## Workflow

### Step 1 — Methodology Paradigm

**Choose one and justify:**

| Paradigm | When to use |
|----------|-------------|
| **Simulation** | Can't control real environment; FL, scheduling, network protocols |
| **Controlled experiment** | Can manipulate variables; lab conditions |
| **Real-world dataset** | Benchmark comparison; image/NLP tasks |
| **User study** | Measuring human factors |
| **Theoretical analysis** | Proving bounds, convergence, complexity |
| **Design Science Research (DSR)** | Build + evaluate artifact in real context |

### Step 2 — Variables

```
Independent variables (you manipulate):
  - [var1]: values [a, b, c]
  - [var2]: values [x, y]

Dependent variables (you measure):
  - [metric1]: [how measured]
  - [metric2]: [how measured]

Controlled variables (you fix):
  - [setting1]: value [X]
  - [setting2]: value [Y]

Confounding variables (potential threats):
  - [threat1]: [how mitigated]
```

### Step 3 — Baselines Selection

Rule: choose baselines that represent **each major paradigm** in your SOTA taxonomy.

| Baseline | Paper | Why included | Code available? |
|----------|-------|--------------|-----------------|
| [Method A] | Author et al. (year) | Best published result on [metric] | ✅ github.com/... |
| [Method B] | Author et al. (year) | Representative of [approach class] | ✅ |
| [Naive/Oracle] | N/A | Lower/upper bound | trivial |

**Avoid**: cherry-picked weak baselines, baselines without code, outdated methods unless they're the canonical comparison.

### Step 4 — Metrics

**Primary metric** (1): drives all main comparisons — must directly measure what your RQ claims to improve.

**Secondary metrics** (2-4): provide context — efficiency, robustness, scalability.

**Metric formulas** — write them explicitly:
```
Accuracy = (TP+TN) / (TP+TN+FP+FN)
Communication cost = Σ(rounds × message_size_MB)
Convergence speed = rounds_to_reach_target_accuracy
```

**Statistical significance**:
- Run ≥5 seeds, report mean ± std
- Use Wilcoxon signed-rank test (non-parametric) or paired t-test
- Report effect size (Cohen's d)

### Step 5 — Ablation Study Design

Identify your method's key components. Test each one by removing/replacing it:

| Variant | Description | Expected effect |
|---------|-------------|-----------------|
| Full model | All components | Best |
| w/o [component A] | Remove A | Shows A's contribution |
| w/o [component B] | Remove B | Shows B's contribution |
| [component A] replaced with [baseline] | Shows your design choice matters |

### Step 6 — Dataset / Environment

```yaml
dataset:
  name: [dataset name]
  source: [URL or paper]
  size: [N samples / N clients / N episodes]
  split: train/val/test = X%/Y%/Z%
  preprocessing: [steps]
  why_chosen: [relevance + availability + used by baselines]

hardware:
  GPU: [model, VRAM]
  CPU: [cores]
  RAM: [GB]
  estimated_runtime: [per experiment]
```

### Step 7 — Reproducibility Checklist

- [ ] Fixed random seeds for all experiments
- [ ] All hyperparameters documented in one config file
- [ ] Dataset preprocessing steps scripted (not manual)
- [ ] All baselines run with same compute budget
- [ ] Environment: `requirements.txt` or `environment.yml` or `Dockerfile`
- [ ] Results logged to file (not just stdout)
- [ ] Code pushed to version control before experiments

## Output Format

```markdown
## Experiment Design: [Your Method Name]

**Paradigm:** [choice + 1-line justification]

**RQ being tested:** [paste from research-question]

### Variables
- Independent: ...
- Dependent: ...
- Controlled: ...

### Baselines
| Baseline | Source | Role |
...

### Metrics
- Primary: [metric] — measures [what]
- Secondary: [metric1, metric2]

### Ablation Plan
| Variant | Removes | Tests |
...

### Datasets/Environments
...

### Statistical Analysis
- N runs: [≥5]
- Significance test: [which test]
- Reporting: mean ± std
```

## Links to Other Skills
- Requires → `research-question` (RQ defines what you measure)
- Requires → `sota-survey` (baselines come from here)
- Feeds into → `experiment-tracking` (run the protocol)
- Feeds into → `paper-writing` (Methodology section)
