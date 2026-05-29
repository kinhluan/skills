---
name: journal-q1-polish
description: Polish paper for Q1 journal submission (ISI/Scopus). Use after paper draft is complete — handles notation sync with thesis, De-AI/De-translation protocol, and Q1 results table standards.
metadata:
  tags: ["research", "phd", "journal", "q1", "polish", "submission", "academic"]
  version: 1.0.0
  triggers:
    - "polish paper for journal"
    - "q1 submission"
    - "isi scopus polish"
    - "de-ai"
    - "de-translation"
    - "notation sync"
    - "results table std"
    - "ablation standard deviation"
    - "chuẩn hóa bài báo"
    - "đồng bộ ký hiệu"
    - "sửa văn phong q1"
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

### 1.3 Abstract ↔ Section 3.3 Complexity Sync

**Critical for Q1:** Complexity stated in abstract must exactly match the analysis in Section 3.3 (or equivalent methodology section). Mismatches are a common reviewer complaint.

**Audit template:**
```
Abstract claims: "O(T · N · d) time, O(N · d) space"
Section 3.3 states: "O(T · N · d) time, O(N · d) space"
Status: ✅ Match / ❌ Mismatch → fix: ___
```

**Common mismatch patterns:**
- Abstract says "linear time" but Section 3.3 shows O(N²)
- Abstract omits a factor (e.g., forgets communication rounds T)
- Abstract uses different variable names than Section 3.3

### 1.4 Sampling Ratio Notation Sync

When paper and thesis use different notation for the same concept, create explicit mapping:

| Concept | Paper | Thesis | Unified Form |
|---------|-------|--------|-------------|
| Effective sampling ratio | `\min(C.ratio, 75/N)` | `\min(s_{\text{config}}, T/N)` | `\min(r_{\text{max}}, S/N)` |

**Rule:** Pick one form (prefer thesis notation if already established) and use consistently. Add a footnote in paper: *"We use the notation from [thesis citation] for consistency."*

### 1.5 Cross-Reference Audit

- [ ] Every equation in paper has matching equation in thesis (or explicit note why different)
- [ ] Algorithm pseudocode matches thesis Algorithm chapter
- [ ] Complexity claims in paper abstract = complexity in thesis Chapter 3
- [ ] Sampling ratio notation unified between paper and thesis

---

## Step 2 — De-AI / De-translation Protocol

Q1 reviewers increasingly reject papers with AI-generated or machine-translated language. This step strips telltale signs.

### 2.1 AI Smell Detection (0-5 Score)

**Audit your paper for these AI-generated patterns:**

| Signal | Description | Example | Fix |
|--------|-------------|---------|-----|
| **Symmetrical structure** | All bullets/paragraphs start with same word pattern | "Enhance X...", "Enhance Y...", "Enhance Z..." | Vary sentence openings |
| **Abstract noun stacking** | Chaining abstract nouns | "utilization of optimization strategies" | "using optimization" |
| **Generic intro/outro** | Vague opening/closing | "In today's rapidly evolving world..." | Start with specific problem |
| **Excessive hedging** | Too many qualifiers | "It could potentially be argued that..." | State directly: "X shows..." |
| **Repetitive paraphrasing** | Same idea restated differently | "This is important. This matters. This is significant." | State once, move on |
| **Triple adjective stacking** | 3+ adjectives before noun | "novel comprehensive robust framework" | Pick one: "robust framework" |
| **Passive voice overuse** | >50% passive sentences | "It was found that..." | "We found..." |
| **Connector overuse** | furthermore, moreover, additionally every paragraph | "Furthermore, ... Moreover, ..." | Vary or restructure |

**Scoring:**
```
0/5 — Natural human writing
1/5 — Minor AI痕迹, light edit needed
2/5 — Noticeable patterns, targeted fixes
3/5 — Multiple signals, significant revision
4/5 — Heavy AI smell, major rewrite
5/5 — Obviously AI-generated, total rewrite
```

**Target: 0-1/5 for Q1 submission.**

### 2.2 Hype Words Blacklist

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

### 2.4 Quantify Hype with Experimental Data

**Rule:** When encountering hype words, replace with specific numbers from your results.

| Hype phrase | Bad (vague) | Good (data-driven) |
|-------------|-------------|-------------------|
| "extremely fast" | "The method is extremely fast" | "The method converges in 43 rounds vs. 67 for FedAvg (35.8% reduction)" |
| "significantly better" | "Our method performs significantly better" | "Our method achieves 94.3% accuracy, outperforming the best baseline by 2.2 percentage points (p < 0.001)" |
| "absolutely robust" | "The approach is absolutely robust to noise" | "Accuracy degrades by only 0.8% when noise increases from 0% to 30%" |
| "vastly superior" | "Our framework is vastly superior" | "Our framework reduces communication cost by 35% while maintaining comparable accuracy" |
| "extremely efficient" | "The algorithm is extremely efficient" | "The algorithm runs in O(N log N) time, 2.3× faster than the O(N²) baseline" |

**Workflow:**
1. Search document for: *extremely, vastly, absolutely, incredibly, remarkably, substantially, considerably*
2. For each hit, locate the corresponding result in your experiments
3. Replace with: **metric + value + comparison/baseline**

### 2.5 De-translation Patterns

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

### 2.6 Sentence Length Audit

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

### 3.2 Ablation Study Format

**⚠️ CRITICAL:** Every cell in an ablation table must include mean ± standard deviation. No exceptions.

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

**Rule:** If a result cell shows only a single number (e.g., `85.2`), it is incomplete. Every value must be `mean ± std` format.

### 3.3 Seed Count Justification

Include in experimental setup:

```
We report mean ± standard deviation over N independent runs with
different random seeds. We use [5/10/30] seeds to ensure reliable
statistical inference and reproducibility of our results.
```

**Seed count guidelines:**

| Domain | Minimum Seeds | Justification |
|--------|---------------|---------------|
| Deep Learning (deterministic) | 3-5 | Low variance, GPU determinism |
| Deep Learning (stochastic) | 5-10 | Moderate variance |
| Federated Learning | 5-10 | Client sampling variance |
| Metaheuristic / Evolutionary | 30 | Central Limit Theorem (n ≥ 30 for normality) |
| Reinforcement Learning | 10-30 | High variance, environment stochasticity |

**Why CLT matters for n ≥ 30:**
- Sampling distribution of mean approximates normality regardless of population distribution
- Enables parametric tests (t-test, ANOVA) even for non-normal results
- Standard expectation in empirical research methodology

**Template:**
```
We report mean ± standard deviation over [N] independent runs
(seed ∈ {42, 123, 456, ...}). [N] seeds ensure [reliable statistical
inference / CLT normality / reproducibility] per standard empirical
methodology.
```

### 3.4 Statistical Tests

| Claim | Required Test |
|-------|---------------|
| "outperforms" / "better than" | Paired t-test or Wilcoxon signed-rank |
| "comparable" / "similar" | Equivalence test or confidence interval overlap |
| "robust to hyperparameter" | Sensitivity analysis table |

### 3.5 Results Table Checklist

- [ ] **All cells** in ablation study show `mean ± std` (not just main results table)
- [ ] Seed count stated for each experiment (minimum 30 for metaheuristics per Đurasević & Jakobović [2023])
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
