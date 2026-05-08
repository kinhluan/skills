---
name: phd-proposal
description: Write, structure, or review a PhD/Master's research proposal. Use when drafting a research proposal, preparing for committee review, writing a thesis outline, or aligning methodology with academic requirements.
metadata:
  tags: ["research", "phd", "proposal", "methodology", "committee"]
  version: 1.0.0
  triggers:
    - "Write research proposal"
    - "PhD proposal"
    - "Thesis proposal"
    - "Help me write my proposal"
    - "Proposal structure"
    - "Committee review preparation"
---

# PhD/Master's Research Proposal

Structure and write a rigorous research proposal that satisfies committee requirements.

## Standard Proposal Structure (IEEE/ACM CS)

```
1. Title & Abstract          (~200 words)
2. Introduction              (~500 words)
3. Related Work              (~800 words)
4. Research Questions        (~200 words)
5. Methodology               (~1000 words) ← most important
6. Preliminary Results       (~500 words, if any)
7. Timeline & Milestones     (table/Gantt)
8. Expected Contributions    (~300 words)
9. References                (BibTeX)
```

## Section-by-Section Guidance

### 1. Title
Formula: `[Method/Approach] for [Problem] in [Domain/Context]`
Example: *"Federated Multi-Level Feedback Queue Scheduling for Resource-Constrained Healthcare IoT Networks"*

### 2. Abstract (structured)
```
[Context]: In [domain], [background challenge].
[Gap]: However, [specific gap from literature].
[Approach]: We propose [method name], which [key idea].
[Validation]: We evaluate on [datasets/benchmarks] using [metrics].
[Impact]: Results show [expected outcome], enabling [application].
```

### 3. Introduction
- Hook: real-world motivation (1 paragraph)
- Background: what exists (1 paragraph)
- Problem: specific gap (1 paragraph)
- Solution sketch: your approach (1 paragraph)
- Contributions: bulleted list (use `research-question` output)
- Paper/thesis structure: "Chapter 2 covers..."

### 4. Related Work
Organize by taxonomy (not chronologically):
```
4.1 [Approach A] — summarize 3-5 papers, explain why insufficient
4.2 [Approach B] — same
4.3 [Your positioning] — "Unlike X, we address Y by Z"
```

### 5. Methodology (Most Critical)

**5.1 Research Paradigm**
Choose and justify:
- Quantitative / Qualitative / Mixed
- Paradigm: Design Science Research (DSR) / Experimental / Simulation

**5.2 System/Model Design**
```
Input: [what]
Processing: [how — algorithm, model, framework]
Output: [what]
Assumption: [what you assume]
```

**5.3 Experimental Protocol**
```
Datasets: [name, size, source, why chosen]
Baselines: [method1, method2 — why these are fair comparisons]
Metrics: [primary metric] + [secondary metrics]
Evaluation protocol: [k-fold CV / train-val-test split / simulation rounds]
Statistical tests: [t-test / Wilcoxon / effect size — for significance]
```

**5.4 Reproducibility Plan**
- Code: GitHub repo (public after publication)
- Environment: Docker / conda environment file
- Seeds: fixed random seeds
- Hardware: specify GPU/CPU specs

### 6. Timeline

| Phase | Activity | Duration | Milestone |
|-------|----------|----------|-----------|
| 1 | Literature review | Month 1-2 | Gap matrix complete |
| 2 | Method design | Month 2-4 | Architecture finalized |
| 3 | Implementation | Month 3-6 | Working prototype |
| 4 | Experiments | Month 5-8 | Results table complete |
| 5 | Writing | Month 7-10 | Draft thesis/paper |
| 6 | Revision | Month 9-11 | Submission ready |
| 7 | Defense | Month 12 | Defended ✓ |

### 7. Expected Contributions
Restate from `research-question` skill, add:
- Theoretical contribution (if any)
- Practical contribution (system, dataset, tool)
- Publication targets (venues + tier)

## Committee Checklist

Before submitting proposal for committee review:
- [ ] Problem is clearly stated in 1-2 sentences
- [ ] Gap is supported by ≥3 recent papers
- [ ] RQ is specific and measurable
- [ ] Methodology is detailed enough to replicate
- [ ] Baselines are state-of-the-art, fairly chosen
- [ ] Timeline is realistic (pad 20% for delays)
- [ ] Limitations are acknowledged
- [ ] Ethical considerations addressed (IRB, data privacy)

## Output Format

Produce a structured Markdown document following the section order above. Export to LaTeX or Word using the `paper-writing` skill templates.

## Links to Other Skills
- Requires → `sota-survey` + `research-question`
- Feeds into → `research-design` (methodology details)
- Feeds into → `milestone-tracker` (timeline)
- Feeds into → `paper-writing` (proposal becomes thesis chapters)
