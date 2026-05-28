---
name: journal-q1-polish
description: Polish paper for Q1 journal submission (ISI/Scopus). Use after paper draft is complete — handles notation sync with thesis, De-AI/De-translation protocol, and Q1 results table standards.
metadata:
  tags: ["research", "phd", "journal", "q1", "polish", "submission", "academic"]
  version: 1.0.0
  links:
    - paper-writing
    - technical-english-cs
    - experiment-tracking
    - internal-critique
    - publication-strategy
---

# Journal Q1 Polish

**Purpose:** Final polish pass before submitting to Q1 journals (ISI/Scopus indexed). Ensures paper meets top-tier standards for notation consistency, language quality, and experimental rigor.

**When to use:** After paper draft is complete, before submission. NOT for initial writing — use `paper-writing` for that.

**Links to:**
- `paper-writing` — structure, sections, flow
- `technical-english-cs` — diction, terminology, IEEE/ACM style
- `experiment-tracking` — results tables, metrics format
- `internal-critique` — self-review checklist
- `publication-strategy` — venue selection, submission prep

---

## Step 1 — Notation & Complexity Sync (Paper ↔ Thesis)

Paper phải dùng notation và complexity format giống thesis để tránh mâu thuẫn khi defend.

### 1.1 Notation Table

Tạo bảng notation mapping giữa paper và thesis:

| Symbol | Paper | Thesis | Status |
|--------|-------|--------|--------|
| Learning rate | $\eta$ | $\eta$ | ✅ Match |
| Batch size | $B$ | $B$ | ✅ Match |
| Model params | $\theta$ | $\theta$ | ✅ Match |

**Checklist:**
- [ ] Tất cả biến trong paper xuất hiện trong thesis notation table
- [ ] Không có symbol conflict (cùng symbol, khác meaning)
- [ ] Greek vs Latin letters consistent
- [ ] Subscript/superscript convention thống nhất

### 1.2 Complexity Notation

Q1 journals expect O(·) notation with explicit assumptions:

```
Time Complexity: O(T · N · d)
  T = number of rounds
  N = number of clients
  d = model dimension
  
Space Complexity: O(N · d)
  Per-client model storage
```

**Rules:**
- Always state what each variable represents
- Include amortized complexity if relevant
- Compare with baseline complexity in the same format

### 1.3 Cross-Reference Audit

- [ ] Every equation in paper has matching equation in thesis (or explicit note why different)
- [ ] Algorithm pseudocode matches thesis Algorithm chapter
- [ ] Complexity claims in paper abstract = complexity in thesis Chapter 3

---

## Step 2 — De-AI / De-translation Protocol

Q1 reviewers increasingly reject papers with AI-generated or machine-translated language. This step strips telltale signs.

### 2.1 Hype Words Blacklist

**BAN these words/phrases entirely:**

| Banned | Replace with |
|--------|--------------|
| delve into | examine, investigate, explore |
| leverage | use, apply, employ |
| robust | reliable, stable, consistent |
| cutting-edge | current, recent, state-of-the-art |
| novel | *(just delete — let the work speak)* |
| groundbreaking | *(delete)* |
| paradigm | approach, framework, method |
| landscape | field, domain, area |
| tapestry | *(delete)* |
| meticulous | careful, thorough |
| furthermore | *(use "Additionally" or restructure sentence)* |
| moreover | *(same)* |
| in conclusion | *(delete — just end the section)* |
| it is worth noting | *(delete — if worth noting, just state it)* |
| comprehensive | complete, full, extensive |
| innovative | *(delete or specify what's new)* |
| significant improvement | improvement of X% (be specific) |
| state-of-the-art | current best, recent methods (cite them) |
| demonstrates | shows, indicates, confirms |
| facilitates | enables, allows, supports |
| enhances | improves, increases |
| utilizing | using |
| aforementioned | *(delete — restructure)* |
| subsequently | then, next, after |
| preliminary | initial, early |

### 2.2 Passive → Active Voice

Q1 journals prefer active voice. Scan for passive patterns:

**Passive (bad):**
```
The model was trained on the dataset.
Experiments were conducted to evaluate performance.
It was found that the method outperforms baselines.
```

**Active (good):**
```
We trained the model on the dataset.
We evaluated performance through experiments.
The method outperforms baselines.
```

**Exception:** Methods section can use passive for standard procedures ("The dataset was split into 80/20 train/test").

### 2.3 De-translation Patterns

If paper was translated from Vietnamese:

| Vietnamese structure | English fix |
|---------------------|-------------|
| "The method has the ability to..." | "The method can..." |
| "In order to..." | "To..." |
| "Due to the fact that..." | "Because..." |
| "At the present time" | "Currently" / "Now" |
| "In the event that" | "If" |
| "Despite the fact that" | "Although" / "Despite" |
| "On a daily basis" | "Daily" |
| "Has the potential to" | "Can" / "May" |

### 2.4 Sentence Length Audit

- Target: 15-25 words per sentence
- Hard max: 35 words (split if longer)
- Check: any paragraph with 3+ consecutive sentences > 25 words → rewrite

---

## Step 3 — Q1 Results Table Standard

Q1 journals expect rigorous experimental reporting. This is the #1 rejection reason for ML/AI papers.

### 3.1 Mandatory Columns

| Column | Required | Notes |
|--------|----------|-------|
| Method | ✅ | Full name + citation |
| Metric(s) | ✅ | Primary metric bolded |
| Mean | ✅ | Arithmetic mean |
| Std Dev | ✅ | **MANDATORY for ablation studies** |
| # Seeds | ✅ | Minimum 3, recommend 5 |
| p-value | ⚠️ | Required if claiming "significant improvement" |

### 3.2 Alation Study Format

**WRONG (rejection risk):**
```
| Method    | Accuracy |
|-----------|----------|
| Baseline  | 85.2     |
| + Module A| 87.1     |
| + Module B| 88.3     |
```

**RIGHT (Q1 standard):**
```
| Method     | Accuracy       | # Seeds | p-value  |
|------------|----------------|---------|----------|
| Baseline   | 85.2 ± 0.3     | 5       | —        |
| + Module A | 87.1 ± 0.4     | 5       | 0.002*   |
| + Module B | 88.3 ± 0.2     | 5       | <0.001*  |

* Statistically significant (paired t-test, α=0.05)
```

### 3.3 Seed Count Justification

Include in experimental setup:

```
We report mean ± standard deviation over 5 independent runs with 
different random seeds (seed ∈ {42, 123, 456, 789, 1024}). We use 
5 seeds following [citation to methodology paper] to ensure 
reproducible results while maintaining computational feasibility.
```

### 3.4 Statistical Tests

| Claim | Required Test |
|-------|---------------|
| "outperforms" / "better than" | Paired t-test or Wilcoxon signed-rank |
| "comparable" / "similar" | Equivalence test or confidence interval overlap |
| "robust to hyperparameter" | Sensitivity analysis table |

### 3.5 Results Table Checklist

- [ ] All ablation results include mean ± std
- [ ] Seed count stated for each experiment
- [ ] Statistical significance marked with asterisk + footnote
- [ ] Best result **bolded**, second-best *underlined*
- [ ] Baseline results from original paper cited, not re-implemented (unless stated)
- [ ] Hardware spec mentioned (GPU type, RAM) for reproducibility
- [ ] Runtime/latency comparison if claiming efficiency

---

## Final Polish Checklist

### From `internal-critique`
- [ ] Self-review using internal-critique checklist
- [ ] Address all "fatal flaw" items before submission

### From `technical-english-cs`
- [ ] Diction matches IEEE/ACM standards
- [ ] No Vietnamese-English translation artifacts

### From `paper-writing`
- [ ] Section structure follows target venue template
- [ ] Abstract within word limit
- [ ] References formatted correctly

### From `publication-strategy`
- [ ] Selected venue matches paper scope
- [ ] Checked recent acceptance rate
- [ ] Reviewed 2-3 recent papers from target venue for style

---

## Integration Flow

```
paper-writing (draft complete)
    ↓
journal-q1-polish (this skill)
    ├── Step 1: notation-sync
    ├── Step 2: de-ai-protocol
    └── Step 3: q1-results-standard
    ↓
internal-critique (final review)
    ↓
publication-strategy (venue selection + submission)
```
