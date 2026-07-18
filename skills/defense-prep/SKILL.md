---
name: defense-prep
description: Prepare for PhD or Master's thesis defense. Use when preparing defense presentation, anticipating committee questions, practicing oral defense, or structuring defense slides.
metadata:
  tags: ["research", "phd", "defense", "thesis", "presentation", "committee"]
  version: 1.0.0
  triggers:
    - "Prepare for defense"
    - "PhD defense"
    - "Master defense"
    - "Thesis defense"
    - "Defense presentation"
    - "Committee questions"
    - "Practice defense"
    - "Defense slides"
---

# Defense Preparation

Prepare a confident, rigorous oral defense of your thesis work.

## Defense Timeline

```
T-8 weeks: Draft complete slides, share with advisor
T-6 weeks: Practice talk #1 with advisor (full run)
T-4 weeks: Incorporate feedback, practice with lab group
T-2 weeks: Practice with mock committee (optional but recommended)
T-1 week: Final slide polish, print backup PDF, know venue
T-1 day: Rest. Eat well. Check AV setup.
T-0: Arrive 30min early. Water bottle. Backup on USB.
```

## Slide Structure (60-min defense = ~40 slides)

```
Cover slide             (1) — title, your name, advisor, date
Outline                 (1) — roadmap of talk
Motivation              (2-3) — why this problem matters
Research Questions      (1) — what you set out to answer
Background              (3-4) — what audience needs to know
Related Work            (2-3) — where you fit in literature
Methodology             (8-10) — your main contribution
Results                 (6-8) — experiments + key findings
Discussion              (2-3) — implications, limitations
Conclusion              (2) — answer your RQs, contributions
Future Work             (1-2)
Thank You + Q&A         (1)
Backup slides           (5-10) — for expected hard questions
```

## Slide Design Principles

- **1 idea per slide** — title is the takeaway, body is the evidence
- **Figures over text** — if explainable with a diagram, use one
- **Build animations sparingly** — only to guide attention, not show off
- **Results: always compare** — isolated numbers mean nothing
- **Font ≥ 24pt** — smallest text readable from back of room

## Anticipated Question Categories

### Category 1 — Methodology Deep Dives
*"Why did you choose [method X] over [method Y]?"*
→ Prepare: justification from research-design + comparison data

*"What happens if assumption [A] doesn't hold?"*
→ Prepare: robustness experiment or honest limitation statement

*"How does your method scale to [larger/different] setting?"*
→ Prepare: complexity analysis + any scaling experiments

### Category 2 — Experimental Validity
*"Why didn't you compare to [paper Z]?"*
→ Prepare: why it's not a fair baseline OR add it

*"Could your results be explained by [confound]?"*
→ Prepare: controlled experiment that rules it out

*"Is the improvement statistically significant?"*
→ Prepare: p-values, effect sizes, number of seeds

### Category 3 — Contribution Scope
*"How is this different from [prior work X]?"*
→ Prepare: explicit differentiation table

*"What is your key insight / novelty?"*
→ One crisp sentence. Practice this until fluent.

*"What would you do differently if starting over?"*
→ Honest answer. Shows maturity. Not a trap.

### Category 4 — Future Directions
*"What are the next steps?"*
→ Have 2-3 concrete, specific directions (not vague "more datasets")

### Category 5 — Basics (common in Master's)
*"Explain [fundamental concept] in your work"*
→ Never assume they know your domain. Prepare Feynman-style explanation.

## Practice Scoring Rubric

Use this when practicing with peers/advisor:

| Dimension | 1-Poor | 3-OK | 5-Excellent |
|-----------|--------|------|-------------|
| Motivation clarity | Unclear why | Somewhat clear | Crystal clear, real stakes |
| Technical depth | Skips details | Some details | Rigorous but accessible |
| Results explanation | Just shows numbers | Explains trends | Insights + implications |
| Question handling | Defensive | Addresses question | Engages, builds on question |
| Time management | Over/under by >5min | ±3min | Hits target exactly |
| Confidence | Nervous, hesitant | Competent | Authoritative |

## On the Day

**Opening** (memorize this):
> "Good [morning/afternoon]. Thank you for coming. My thesis is titled [X]. The central question I've been investigating is [RQ in plain language]. Today I'll walk you through what I found and why I believe it matters."

**Handling unknown questions:**
> "That's a great question. I haven't specifically tested for that, but based on [reasoning], I would expect [answer]. This is actually a good direction for future work."

Never say "I don't know" alone — say "I don't know, but here's how I would think about it."

**Time control:**
- Practice 3 times minimum. Know your pace.
- Every slide: estimate seconds. Cut if needed.
- Don't rush Q&A by running over.

## Backup Slide Topics (prepare these)

- Detailed algorithm pseudocode
- Full hyperparameter tables
- Additional ablation results
- Proofs or derivations referenced but not shown
- Failure cases / limitations in detail
- Comparison with [most likely missing baseline]

## Links to Other Skills
- Requires → `paper-writing` (thesis must be written first)
- Requires → `milestone-tracker` (defense date in timeline)
- Pairs with → `internal-critique` (critique your slides like a reviewer)
