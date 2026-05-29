# PhD Research Workflow — Full Integration Map

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PhD Research Workflow (Full Integration)                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: PREPARATION (Year 1)                                              │
│  ═══════════════════════════════                                            │
│                                                                             │
│  sota-survey ──────→ research-question ──────→ research-design              │
│       │                    │                        │                       │
│       └────────────────────┼────────────────────────┘                       │
│                            ↓                                                │
│                      phd-proposal                                           │
│                            │                                                │
│                            ↓                                                │
│                    proposal-defense                                          │
│                            │                                                │
│                            ↓                                                │
│                   ✅ PROPOSAL APPROVED                                      │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 2: RESEARCH & WRITING (Year 2-3)                                     │
│  ════════════════════════════════════════                                    │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    RESEARCH LOOP                                     │   │
│  │                                                                     │   │
│  │  research-design ──→ experiment-tracking ──→ technical-report       │   │
│  │       │                    │                      │                 │   │
│  │       └────────────────────┼──────────────────────┘                 │   │
│  │                            ↓                                        │   │
│  │                    internal-critique                                │   │
│  │                            │                                        │   │
│  │                            ↓                                        │   │
│  │                    conference-paper                                 │   │
│  │                            │                                        │   │
│  │                            ↓                                        │   │
│  │                    publication-strategy                             │   │
│  │                            │                                        │   │
│  │                            ↓                                        │   │
│  │                    journal-q1-polish                                │   │
│  │                            │                                        │   │
│  │                            ↓                                        │   │
│  │                    ✅ PAPER PUBLISHED                               │   │
│  │                            │                                        │   │
│  │                            └────────────────────────────────────┐   │   │
│  │                                                                 │   │   │
│  └─────────────────────────────────────────────────────────────────┘   │   │
│                            ↑                                            │   │
│                            │ (iterate)                                  │   │
│                            │                                            │   │
│  ┌─────────────────────────┴───────────────────────────────────────┐   │   │
│  │                    THESIS WRITING                                │   │   │
│  │                                                                 │   │   │
│  │  thesis-writing                                                 │   │   │
│  │  ├── Chapter 1: Introduction                                    │   │   │
│  │  ├── Chapter 2: Literature Review ← sota-survey                 │   │   │
│  │  ├── Chapter 3: Methodology ← research-design                   │   │   │
│  │  ├── Chapter 4: Experiments ← experiment-tracking               │   │   │
│  │  ├── Chapter 5: Discussion ← technical-report                   │   │   │
│  │  └── Chapter 6: Conclusion                                      │   │   │
│  │                                                                 │   │   │
│  └─────────────────────────────────────────────────────────────────┘   │   │
│                            │                                            │   │
│                            ↓                                            │   │
│  ┌─────────────────────────────────────────────────────────────────┐   │   │
│  │                    PROGRESS REPORTS                              │   │   │
│  │                                                                 │   │   │
│  │  progress-report                                                │   │   │
│  │  ├── Monthly Report → advisor                                   │   │   │
│  │  ├── Committee Report → committee                               │   │   │
│  │  ├── Annual Report → department                                 │   │   │
│  │  └── Funding Report → agency                                    │   │   │
│  │                                                                 │   │   │
│  └─────────────────────────────────────────────────────────────────┘   │   │
│                            │                                            │   │
│                            ↓                                            │   │
│                   ✅ THESIS DRAFT COMPLETE                               │   │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 3: DEFENSE (Year 3-4)                                                │
│  ════════════════════════════                                               │
│                                                                             │
│  defense-prep ──────→ ✅ THESIS DEFENSE                                    │
│       │                                                                     │
│       ↓                                                                     │
│  ✅ PhD COMPLETED                                                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SUPPORTING SKILLS (Throughout)                                             │
│  ════════════════════════════════                                           │
│                                                                             │
│  ├── technical-english-cs (writing quality)                                │
│  ├── vietnamese-cs-terminology (Vietnamese terms)                          │
│  ├── vietnamese-writing-standard (Vietnamese writing)                      │
│  ├── milestone-tracker (timeline management)                               │
│  └── research-workspace-standard (file organization)                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Skill Cross-References

| Skill | Links TO | Links FROM |
|-------|----------|------------|
| sota-survey | research-question | thesis-writing, conference-paper |
| research-question | research-design | sota-survey, proposal-defense |
| research-design | experiment-tracking | research-question, thesis-writing |
| phd-proposal | proposal-defense | research-question, research-design |
| proposal-defense | thesis-writing | phd-proposal, defense-prep |
| thesis-writing | paper-writing, conference-paper | proposal-defense, progress-report |
| experiment-tracking | technical-report, thesis-writing | research-design |
| technical-report | thesis-writing, conference-paper | experiment-tracking |
| conference-paper | publication-strategy | thesis-writing, paper-writing |
| journal-q1-polish | publication-strategy | paper-writing, conference-paper |
| publication-strategy | — | conference-paper, journal-q1-polish |
| progress-report | — | thesis-writing, experiment-tracking |
| internal-critique | — | paper-writing, conference-paper |
| defense-prep | — | proposal-defense |
| paper-writing | journal-q1-polish | thesis-writing |
| milestone-tracker | — | All skills |
| research-workspace-standard | — | All skills |

## Recommended Workflow Order

```
1. sota-survey (literature)
2. research-question (RQs)
3. research-design (methodology)
4. phd-proposal (proposal document)
5. proposal-defense (defend proposal)
   ─── PROPOSAL APPROVED ───
6. research-design (refine)
7. experiment-tracking (run experiments)
8. technical-report (document results)
9. conference-paper (publish findings)
10. publication-strategy (choose venue)
11. internal-critique (self-review)
12. journal-q1-polish (polish for Q1)
    ─── PAPER PUBLISHED ───
13. thesis-writing (write chapters)
14. progress-report (report to advisor)
    ─── THESIS COMPLETE ───
15. defense-prep (prepare defense)
    ─── PhD COMPLETE ───
```

## Timeline Integration with milestone-tracker

```
Year 1:
├── Q1-Q2: sota-survey, research-question
├── Q3: research-design, phd-proposal
└── Q4: proposal-defense ✅

Year 2:
├── Q1-Q2: research-design (refine), experiment-tracking
├── Q3: technical-report, conference-paper
└── Q4: publication-strategy, journal-q1-polish

Year 3:
├── Q1-Q2: thesis-writing (chapters 2-4)
├── Q3: thesis-writing (chapters 5-6), progress-report
└── Q4: defense-prep, thesis defense ✅
```
