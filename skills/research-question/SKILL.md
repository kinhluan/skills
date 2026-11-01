---
name: research-question
description: Formulate research questions, hypotheses, and contribution statements from identified literature gaps. Use when defining a research problem, framing a thesis topic, identifying novelty, or writing the "contribution" section of a proposal or paper.
metadata:
  tags: ["research", "phd", "rq", "hypothesis", "contribution", "gap"]
  version: 1.0.0
  triggers:
    - "Formulate research question"
    - "Define my research problem"
    - "What is my contribution"
    - "Research gap to hypothesis"
    - "Identify novelty"
    - "Frame my thesis topic"
---

# Research Question Formulation

Bridge the gap between what exists (SOTA) and what you'll contribute.

## Prerequisite
Run `sota-survey` first. You need a gap table before formulating RQ.

## Workflow

### Step 1 — Gap → Problem Statement
For each gap from SOTA survey, apply this template:

```
Despite [what exists], [limitation/gap] remains unsolved because [root cause].
This causes [concrete consequence] in [application domain].
```

Example:
> Despite federated learning achieving competitive accuracy, communication efficiency in heterogeneous IoT networks remains unsolved because existing methods assume uniform client capabilities. This causes excessive energy drain in resource-constrained healthcare devices.

### Step 2 — Formulate Research Questions

**Main RQ (1 sentence):**
```
How can [method/approach] be designed to [achieve goal] in [context/constraint]?
```

**Sub-questions (2-4, each answerable in ~1 paper/chapter):**
- RQ1: [measurable, specific]
- RQ2: [builds on RQ1]
- RQ3: [validates or extends]

**RQ Quality Check:**
- [ ] Specific — not "improve performance" but "reduce communication rounds by X%"
- [ ] Feasible — answerable in your timeline with your resources
- [ ] Novel — not already answered in literature
- [ ] Significant — matters to the field
- [ ] Ethical — no harm, IRB if needed

### Step 3 — Hypothesis (if experimental)

```
H0 (null): [Method A] performs no better than [baseline] on [metric] in [setting]
H1 (alternative): [Method A] achieves [≥X% improvement] over [baseline] on [metric]
```

### Step 4 — Contribution Statement

Structure for proposal and paper Introduction:

```markdown
## Contributions

This work makes the following contributions:

1. **[Type: Algorithm/Framework/Dataset/Analysis]**: We propose [name], which [what it does] to address [gap].
2. **[Type]**: We demonstrate [empirical result] on [benchmark], showing [magnitude] improvement over [baseline].
3. **[Type]** (optional): We release [artifact] for reproducibility.
```

Contribution types: Algorithm, Framework, Dataset, Benchmark, Analysis, Survey, System, Theorem.

### Step 5 — Scope Boundary

Explicitly state what you will NOT do (saves you from committee scope creep):
```
Out of scope:
- [Related problem you won't solve and why]
- [Assumption you're making]
- [Limitation you accept]
```

## Output Format

```markdown
## Research Problem Definition

**Problem:** [1-2 sentence problem statement]

**Main RQ:** [Single question]

**Sub-questions:**
- RQ1: ...
- RQ2: ...

**Hypothesis:**
- H0: ...
- H1: ...

**Contributions:**
1. ...
2. ...

**Out of scope:** ...
```

## Links to Other Skills
- Requires → `sota-survey` (gap table as input)
- Feeds into → `phd-proposal` (problem statement section)
- Feeds into → `paper-writing` (Introduction + Contribution sections)
