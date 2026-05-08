---
name: publication-strategy
description: Choose publication venue, prepare submission, write rebuttals, and manage revision cycles. Use when deciding where to submit a paper, preparing camera-ready, writing a rebuttal to reviewers, or planning a revision.
metadata:
  tags: ["research", "phd", "publication", "venue", "rebuttal", "submission"]
  version: 1.0.0
  triggers:
    - "Where to submit my paper"
    - "Publication strategy"
    - "Write rebuttal"
    - "Revision plan"
    - "Conference deadline"
    - "Journal vs conference"
    - "Prepare camera-ready"
---

# Publication Strategy

Get your work published efficiently without wasted submissions.

## Venue Selection

### AI/ML Top Venues (Tier 1)
| Venue | Type | Deadline pattern | Acceptance rate |
|-------|------|-----------------|-----------------|
| NeurIPS | Conference | May | ~25% |
| ICML | Conference | Jan | ~27% |
| ICLR | Conference | Oct | ~30% |
| CVPR | Conference | Nov | ~25% |
| ACL/EMNLP | Conference | Feb/Jun | ~25% |
| AAAI | Conference | Aug | ~23% |

### Systems / Distributed Computing
| Venue | Type | Focus |
|-------|------|-------|
| MLSys | Conference | ML systems, FL efficiency |
| EuroSys | Conference | Systems |
| IEEE TPDS | Journal | Parallel/distributed |
| IEEE IoT Journal | Journal | IoT applications |

### Choosing Your Venue

Answer these:
1. **Contribution type**: algorithm → ML venue; system → systems venue; application → domain venue
2. **Novelty level**: incremental → workshop or journal; significant → top conference
3. **Timeline**: PhD submission date → work backwards from deadlines
4. **Audience**: who needs to read this? → they attend which venue?

**Strategy for PhD students:**
```
First paper → workshop at top venue (NeurIPS/ICML workshop) — lower bar, builds CV
Second paper → Tier 2 conference (ECML, ICDM, LoD)
Third paper → Tier 1 attempt (NeurIPS, ICML, ICLR)
Thesis compilation → journal version (IEEE TPDS, JMLR)
```

## Submission Checklist

- [ ] Paper within page limit (main + appendix)
- [ ] All author information removed (double-blind venues)
- [ ] Code anonymized (no usernames in comments, no personal paths)
- [ ] All figures are vector (PDF) or ≥300 DPI
- [ ] References formatted per venue style
- [ ] Supplementary material within size limit
- [ ] Ethics statement if required (NeurIPS mandates it)
- [ ] License statement if releasing dataset/code

## Rebuttal Writing

Most top conferences have 72-96h rebuttal window. Structure:

```markdown
We thank all reviewers for their detailed feedback. We address the main concerns:

**[R1, R2] Missing baseline [Method X]:**
We ran [X] under identical conditions. Our method achieves Y% vs X's Z%
(see attached Table). We will include this in the final version.

**[R3] Concern about dataset diversity:**
We acknowledge this limitation. We plan experiments on [Dataset B] 
which we can include in revision. Preliminary results show [outcome].

**[R1] Unclear notation in Section 3:**
We will revise Section 3.1 to clarify [specific point]. The key insight is [explanation].

Minor issues raised by all reviewers will be addressed in revision.
```

**Rebuttal rules:**
- Don't be defensive — acknowledge valid concerns
- Promise only what you can deliver in revision timeline
- Focus on fatal flaws, not nitpicks
- Keep it concise — reviewers are busy

## Revision Plan

After receiving "Major Revision" decision:

```markdown
## Revision Plan for [Venue] [Year]

**Deadline:** [date]
**Review decision:** Major / Minor revision

| Reviewer | Concern | Action | Owner | Due |
|----------|---------|--------|-------|-----|
| R1 | Missing baseline X | Run experiments | Me | +2 weeks |
| R2 | Unclear Section 3 | Rewrite 3.1 | Me | +1 week |
| R3 | Needs ablation on Y | Design + run | Me | +3 weeks |

**New experiments needed:** [list]
**Sections requiring rewrite:** [list]
**Estimated revision time:** [X weeks]
```

## After Rejection

Rejection ≠ bad paper. NeurIPS accepts ~25%, reject = 75% of all submissions.

1. Read reviews carefully — identify legitimate weaknesses
2. Rate each review: valid / partially valid / wrong
3. Decide: fix + resubmit to same tier OR resubmit to next venue
4. Don't submit same paper to next deadline without addressing reviewers

Typical path: NeurIPS reject → fix → ICML (3 months later)

## Links to Other Skills
- Requires → `internal-critique` (paper must pass internal check first)
- Requires → `paper-writing` (clean draft)
- Feeds into → `milestone-tracker` (add submission deadlines)
