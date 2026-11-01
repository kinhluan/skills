# Research Design Templates

## Experiment Protocol Template

```markdown
## Experiment Protocol

### Research Questions
- RQ1: [Primary question]
- RQ2: [Secondary question]

### Hypotheses
- H1: [Null hypothesis for RQ1]
- H2: [Alternative hypothesis for RQ1]

### Variables
- Independent: [What we manipulate]
- Dependent: [What we measure]
- Controlled: [What we keep constant]

### Datasets
| Dataset | Size | Source | Preprocessing |
|---------|------|--------|---------------|
| [name] | [N samples] | [URL/citation] | [steps] |

### Baselines
| Method | Type | Citation | Why included |
|--------|------|----------|--------------|
| [name] | [SOTA/Classic/Ablation] | [ref] | [reason] |

### Metrics
| Metric | Formula | Range | Interpretation |
|--------|---------|-------|----------------|
| [name] | [equation] | [min-max] | [higher/lower is better] |

### Hyperparameters
| Parameter | Search Range | Final Value | Selection Method |
|-----------|--------------|-------------|------------------|
| learning_rate | [1e-4, 1e-2] | 1e-3 | grid search |
| batch_size | [16, 32, 64, 128] | 64 | validation loss |

### Statistical Tests
- Comparison type: [paired/unpaired]
- Test: [t-test/Wilcoxon/Mann-Whitney]
- Significance level: α = 0.05
- Multiple comparison correction: [Bonferroni/FDR if needed]

### Reproducibility
- Seeds: [42, 123, 456, 789, 1024]
- Hardware: [GPU type, RAM]
- Software: [framework versions]
- Code release: [URL or "upon acceptance"]
```

## Ablation Study Template

```markdown
## Ablation Study Design

### Components to Ablate
1. [Component A] - tests [hypothesis about A]
2. [Component B] - tests [hypothesis about B]
3. [Component C] - tests [hypothesis about C]

### Ablation Configurations
| Config | Comp A | Comp B | Comp C | Purpose |
|--------|--------|--------|--------|---------|
| Full | ✓ | ✓ | ✓ | Complete model |
| w/o A | ✗ | ✓ | ✓ | A's contribution |
| w/o B | ✓ | ✗ | ✓ | B's contribution |
| w/o C | ✓ | ✓ | ✗ | C's contribution |
| Minimal | ✗ | ✗ | ✗ | Baseline |

### Expected Outcomes
- If removing A causes X% drop → A is critical for [function]
- If removing B causes Y% drop → B contributes to [function]
- If removing C has minimal effect → C is optional

### Reporting Format
| Configuration | Metric1 (mean ± std) | Metric2 (mean ± std) | # Seeds |
|---------------|---------------------|---------------------|---------|
| Full | XX.X ± X.X | XX.X ± X.X | 5 |
| w/o A | XX.X ± X.X | XX.X ± X.X | 5 |
```

## Pilot Study Template

```markdown
## Pilot Study Plan

### Purpose
Validate experimental setup before full run.

### Scope
- N samples: [small subset, e.g., 10% of full dataset]
- Seeds: [1-2 seeds only]
- Baselines: [1-2 key baselines]

### Checklist
- [ ] Pipeline runs end-to-end without errors
- [ ] Metrics are computed correctly
- [ ] Results are reasonable (not random)
- [ ] Runtime estimate for full experiment
- [ ] Resource requirements (GPU memory, disk)

### Go/No-Go Decision
- ✓ Pipeline stable → proceed to full experiment
- ✗ Issues found → fix and re-pilot
```
