---
name: conference-paper
description: Write conference papers (4-6 pages), poster abstracts, and prepare oral/poster presentations. Use when targeting conferences like NeurIPS, ICML, CVPR, ACL, IEEE venues, or preparing conference presentations.
metadata:
  tags: ["research", "phd", "conference", "paper", "presentation", "poster", "oral"]
  version: 1.0.0
  triggers:
    - "conference paper"
    - "poster abstract"
    - "conference presentation"
    - "oral presentation"
    - "poster presentation"
    - "báo cáo hội nghị"
    - "poster hội nghị"
---

# Conference Paper

**Purpose:** Write and present research at academic conferences — the primary publication venue in CS.

**When to use:**
- Writing conference paper (4-6 pages)
- Preparing poster abstract
- Creating oral/poster presentation
- Preparing camera-ready version

**Links to:**
- `paper-writing` — general writing skills
- `journal-q1-polish` — polish for top venues
- `publication-strategy` — venue selection
- `technical-english-cs` — academic English
- `defense-prep` — presentation skills

---

## Conference Paper vs Journal Paper

| Aspect | Conference | Journal |
|--------|-----------|---------|
| Length | 4-6 pages (double-column) | 8-12 pages (single/double) |
| Review time | 2-3 months | 3-12 months |
| Acceptance rate | 20-30% (top: 15-25%) | 20-40% |
| Novelty emphasis | High (new ideas) | Moderate (thoroughness) |
| Experiments | Key results | Comprehensive |
| Related work | Concise | Extensive |
| Presentation | Required | Optional |
| Proceedings | Yes (archival) | Yes |
| Impact | Immediate | Long-term |

---

## Conference Paper Structure (4-6 pages)

```
Title
Abstract (150-200 words)

1. Introduction (0.5-1 page)
   - Problem + motivation (2 paragraphs)
   - Gap (1 paragraph)
   - Contributions (bulleted list)

2. Related Work (0.5-1 page)
   - 2-3 paragraphs grouping related approaches
   - End each: "Unlike [X], we [difference]"

3. Method (1.5-2 pages)
   - Problem formulation
   - System overview (1 figure)
   - Key components (algorithm + explanation)
   - Complexity: O(...)

4. Experiments (1-1.5 pages)
   - Setup: datasets, baselines, metrics
   - Main results (1 table)
   - Ablation (1 table)
   - Analysis (1 figure optional)

5. Conclusion (0.25 page)
   - Summary + future work

References (≤1 page)
```

### Page Budget

| Section | Pages | Notes |
|---------|-------|-------|
| Abstract | 0.2 | 150-200 words |
| Introduction | 0.75 | Funnel structure |
| Related Work | 0.75 | 2-3 paragraphs |
| Method | 1.5 | Core contribution |
| Experiments | 1.25 | Key results only |
| Conclusion | 0.25 | Brief |
| References | 0.5 | 20-30 refs |
| **Total** | **5** | ±0.5 for 4-6 page limit |

---

## Poster Abstract (1 page)

```markdown
# [Title]

**Authors:** [Names]
**Affiliation:** [University]

## Abstract
[250-300 words]
- Problem (2 sentences)
- Gap (1 sentence)
- Method (3-4 sentences)
- Results (2-3 sentences)
- Impact (1 sentence)

## Key Figure
[1 main figure showing concept or results]

## References
[3-5 key references]
```

---

## Poster Design

### Layout (A0 portrait: 841 × 1189 mm)

```
┌─────────────────────────────────────────────┐
│                 TITLE                        │
│            Authors & Affiliation             │
├──────────────┬──────────────┬───────────────┤
│ Introduction │   Method     │  Related Work │
│ + Motivation │   (Figure)   │               │
├──────────────┼──────────────┼───────────────┤
│   Results    │   Results    │  Conclusion   │
│   (Table)    │   (Figure)   │  + Future     │
├──────────────┴──────────────┴───────────────┤
│          References & Contact               │
└─────────────────────────────────────────────┘
```

### Poster Checklist
- [ ] Title readable from 3m distance
- [ ] Figures readable from 1.5m distance
- [ ] Text readable from 1m distance
- [ ] QR code to paper/code
- [ ] Contact email visible
- [ ] Color-blind friendly palette
- [ ] Minimal text (figures > text)

---

## Oral Presentation (15-20 min)

### Slide Structure

```
Slide 1: Title + Authors (30 sec)
Slide 2: Outline (15 sec)
Slide 3-4: Problem & Motivation (2 min)
Slide 5: Related Work (1 min)
Slide 6-8: Method (5 min)
  - Overview (1 slide)
  - Key component 1 (1 slide)
  - Key component 2 (1 slide)
Slide 9-11: Experiments (4 min)
  - Setup (1 slide)
  - Main results (1 slide)
  - Ablation/Analysis (1 slide)
Slide 12: Conclusion & Future Work (1 min)
Slide 13: Q&A (30 sec)
```

### Timing Guide
| Section | Time | Slides |
|---------|------|--------|
| Intro + Problem | 2 min | 2-3 |
| Related Work | 1 min | 1 |
| Method | 5 min | 3-4 |
| Experiments | 4 min | 2-3 |
| Conclusion | 1 min | 1 |
| Buffer | 2 min | — |
| **Total** | **15 min** | **10-12** |

### Presentation Tips
- Practice 3 times minimum
- Time yourself (strict 15 min)
- Prepare for common questions
- Have backup slides for deep-dive
- Speak slowly (120-150 words/min)

---

## Camera-Ready Preparation

### Checklist
- [ ] Address all reviewer comments
- [ ] Update results if improved
- [ ] Fix all typos/formatting
- [ ] Check figure quality (300 DPI)
- [ ] Verify references complete
- [ ] Add acknowledgments
- [ ] Check page limits
- [ ] Submit source files + PDF
- [ ] Sign copyright form
- [ ] Register for conference

### Response to Reviews (for revision)

```markdown
# Response to Reviewers

## Summary of Changes
[Bulleted list of major changes]

## Reviewer 1
### Comment 1: "[quote]"
**Response:** [explanation]
**Changes:** [what was changed, page/line]

### Comment 2: "[quote]"
...

## Reviewer 2
...
```

---

## Conference-Specific Formats

### NeurIPS/ICML/ICLR
- 4 pages main + unlimited appendix
- Double-blind review
- NeurIPS LaTeX template
- Broader Impact statement (NeurIPS)

### CVPR/ICCV/ECCV
- 8 pages (excluding references)
- Double-blind review
- IEEE template
- Supplementary material

### ACL/EMNLP/NAACL
- 8 pages (long) / 4 pages (short)
- Double-blind review
- ACL template
- Ethics statement

### IEEE Conferences (custom)
- 4-6 pages
- IEEE double-column template
- IEEE PDF eXpress compliance

---

## Integration Flow

```
sota-survey (find venues)
    ↓
publication-strategy (choose venue)
    ↓
paper-writing (draft)
    ↓
conference-paper (this skill)
    ├── Write paper (4-6 pages)
    ├── Prepare poster
    ├── Prepare oral slides
    └── Camera-ready
    ↓
journal-q1-polish (if extending to journal)
    ↓
internal-critique (self-review)
    ↓
progress-report (report to advisor)
    ↓
thesis-writing (integrate into thesis)
```
