# Research / PhD Skills Group — Design Spec
Date: 2026-05-08

## Overview

10 self-contained skills for PhD/research workflows. Each skill works standalone (A+B hybrid approach) but together follows the standard PhD lifecycle validated against Creswell, Design Science Research (DSR), and IEEE CS methodology.

## Lifecycle Flow

```
sota-survey ──────────────────────────────────────────────┐
    ↓                                                      │ iterative
research-question (RQ + gap + contribution framing)        │
    ↓                                                      │
phd-proposal (methodology, scope, committee alignment)     │
    ↓                                                      │
research-design (protocol, baselines, metrics, ablation)  │
    ↓                                                      │
experiment-tracking (run, log, compare, reproduce)        ─┘
    ↓
paper-writing (chapter/paper drafting + structure)
    ↓
internal-critique (self-review before submit)
    ↓
publication-strategy (venue selection, revision, rebuttal)
    ↓
defense-prep
    ↑
milestone-tracker (cross-cutting — deadlines, committee)
```

## Skills

| Skill | Purpose | Key Actions |
|-------|---------|-------------|
| `sota-survey` | Search, read, synthesize literature | arXiv/Scholar search, gap matrix, citation graph |
| `research-question` | Formulate RQ, hypothesis, contribution | RQ template, gap-to-contribution bridge |
| `phd-proposal` | Structure proposal document | Problem, methodology, scope, timeline, committee |
| `research-design` | Protocol, metrics, baselines, ablation | Experiment design, reproducibility checklist |
| `experiment-tracking` | Run, log, compare experiments | Results table, baseline comparison, reproduce |
| `paper-writing` | Draft thesis chapters or conference papers | Section-by-section guidance, LaTeX structure |
| `internal-critique` | Self-review before submission | Weakness analysis, reviewer simulation |
| `publication-strategy` | Venue selection, rebuttal, revision cycles | Venue ranking, rebuttal writing, revision plan |
| `defense-prep` | Oral defense preparation | Committee Q&A simulation, slide structure |
| `milestone-tracker` | PhD timeline, deadlines, committee meetings | Gantt-style tracking, milestone checklist |

## Approach

- **Self-contained core**: Full workflow logic in SKILL.md — no external tools required
- **Optional tool integration**: arXiv API, Semantic Scholar, HuggingFace Papers when available
- **Namespace**: `kinhluan/skills` (consistent with `skills.json` registry)
- **Format**: YAML frontmatter + markdown workflow, same as `ddd-core`, `c4-model` etc.

## Target Users

- Primary: PhD/Master students (CS, AI, Engineering)
- Secondary: General researchers needing structured workflows

## What Each Skill Must Include

1. Trigger phrases (when Claude invokes it)
2. Step-by-step workflow (not just checklist)
3. Concrete output format (templates, tables, structures)
4. Optional tool integration hints
5. Cross-links to related skills in the group
