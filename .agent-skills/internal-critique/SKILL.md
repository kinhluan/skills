---
name: internal-critique
description: Self-review a paper or thesis chapter before sharing with advisor or submitting. Simulates tough reviewer feedback to identify weaknesses before external review. Use when finishing a draft, preparing for advisor meeting, or doing pre-submission sanity check.
metadata:
  tags: ["research", "phd", "review", "critique", "self-review", "submission"]
  version: 1.0.0
  triggers:
    - "Review my paper"
    - "Critique this draft"
    - "Find weaknesses in my paper"
    - "Pre-submission check"
    - "Simulate reviewer"
    - "Is my paper ready"
    - "Advisor meeting prep"
---

# Internal Critique

Simulate a tough-but-fair reviewer before anyone else sees your work.

## Reviewer Mindset

Top conference reviewers ask:
1. Is this problem important and unsolved?
2. Is the proposed method novel?
3. Are experiments convincing and fair?
4. Are claims supported by evidence?
5. Is the writing clear enough to follow?

## Critique Protocol

### Level 1 — Fatal Flaws (reject if any present)

Check each. If yes → fix before any sharing.

- [ ] **Contribution unclear**: Can't state in 2 sentences what is new
- [ ] **Baselines unfair**: Missing key baselines, or baselines disadvantaged
- [ ] **No statistical significance**: Single-run results with no std dev
- [ ] **Claims unsupported**: Results table doesn't support abstract claims
- [ ] **Reproducibility impossible**: Hyperparameters missing, no code planned
- [ ] **Overclaiming**: "state-of-the-art" without comprehensive comparison

### Level 2 — Major Weaknesses (major revision territory)

- [ ] **Ablation missing**: Don't know which component causes improvement
- [ ] **Dataset too small/narrow**: Only 1 dataset, too easy, not standard
- [ ] **Hyperparameter sensitivity unknown**: Did you tune on test set?
- [ ] **Limitations not discussed**: Honest papers discuss failure cases
- [ ] **Related work gaps**: Missing the 2-3 most relevant papers

### Level 3 — Minor Issues (polish)

- [ ] Notation inconsistency
- [ ] Figures unclear (missing axis labels, legend, caption)
- [ ] Paragraph without clear main point
- [ ] Abstract doesn't match paper content
- [ ] Future work too vague

## Section-Specific Review

### Introduction
- Hook motivates real problem?
- Gap is specific, not "performance is important"?
- Contributions are concrete (numbers, not adjectives)?

### Related Work
- Papers organized by theme, not dump of citations?
- Each cluster clearly differentiated from yours?
- Most recent papers included (within 2 years)?

### Methodology
- Problem formally defined (notation, objective)?
- Algorithm reproducible from text alone?
- Assumptions stated explicitly?

### Experiments
- Baselines are current SOTA?
- Same compute budget for all methods?
- Results table complete (all methods × all metrics)?
- Ablation covers all key design choices?
- At least 1 analysis beyond main table?

### Writing
- Abstract ≤ 250 words?
- No paragraph > 8 sentences?
- No hedging words (very, clearly, obviously)?
- Every claim has citation or experimental support?

## Output Format

Produce a structured critique report:

```markdown
## Internal Critique: [Paper Title]

### Fatal Flaws
- [ ] [issue or ✅ clear]

### Major Weaknesses
1. [Section]: [specific problem] → [suggested fix]
2. ...

### Minor Issues
- [location]: [issue]

### Strongest Points
- [what works well — helps identify what to protect in revisions]

### Overall Assessment
- Ready for: advisor / workshop / top venue / needs more work
- Estimated revision time: [X hours/days]
- Priority fixes: [top 3 actions]
```

## Simulated Reviewer Comments

For each weakness, write in reviewer voice:
> *"The authors claim X but only demonstrate Y. The baseline Z is missing, which is the strongest published method on this task. Without this comparison, the improvement claim is not convincing."*

Then write your rebuttal response:
> *"We thank the reviewer. We will add Z as baseline. Preliminary results show our method still outperforms (Table attached). We will include in final version."*

This prepares you for actual rebuttal if the paper gets reviewed.

## Links to Other Skills
- Requires → `paper-writing` (draft to review)
- Feeds into → `publication-strategy` (after critique, choose venue)
- Can iterate back to → `experiment-tracking` (if more experiments needed)
