# PhD Research Framework

**From literature gap to defended thesis — a rigorous, reproducible workflow.**

This framework guides doctoral and master's research from initial curiosity through to thesis defense. It mirrors the scientific method: observe → hypothesize → experiment → analyze → publish → defend.

> "Research is what I'm doing when I don't know what I'm doing." — Wernher von Braun

---

## 1. The PhD Research Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 0 — FOUNDATION                                     │
│                                                                                 │
│   📚 SOTA Survey ──→ 🔬 Research Question ──→ 🧪 Research Design               │
│   (sota-survey)      (research-question)      (research-design)                │
│                                                                                 │
│   • Literature matrix    • Gap identification    • Methodology choice          │
│   • Citation network     • Hypothesis            • Baselines & metrics         │
│   • Trend analysis       • Contribution stmt     • Reproducibility plan        │
│                                                                                 │
│   Output: Literature Matrix + Gap Analysis + Research Proposal                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ (Committee Review / Proposal Defense)
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 1 — EXPERIMENTATION                                │
│                                                                                 │
│   🧬 Experiments ──→ 📊 Results ──→ 🔍 Analysis                                │
│   (experiment-tracking)                                                          │
│                                                                                 │
│   • Implementation       • Metrics collection      • Statistical tests         │
│   • Ablation studies     • Visualization           • Comparison vs baselines   │
│   • Hyperparameter tuning • Raw data logging        • Significance testing     │
│                                                                                 │
│   Output: Experiment Logs + Results Tables + Analysis Report                   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ (Internal Review / Advisor Meeting)
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 2 — PUBLICATION                                    │
│                                                                                 │
│   📝 Paper Writing ──→ ✨ Q1 Polish ──→ 📰 Publication Strategy                │
│   (paper-writing)      (journal-q1-polish)      (publication-strategy)         │
│                                                                                 │
│   • Structure & outline  • De-AI protocol          • Venue selection           │
│   • Academic tone        • Notation sync           • Rebuttal writing          │
│   • LaTeX formatting     • Results table std       • Revision cycles           │
│                                                                                 │
│   Output: Submitted Paper + Camera-Ready Version                               │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ (Acceptance / Major Revision / Rejection)
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 3 — THESIS COMPOSITION                             │
│                                                                                 │
│   📖 Thesis Writing ──→ 🛡️ Defense Prep                                        │
│   (thesis-writing)      (defense-prep)                                         │
│                                                                                 │
│   • Chapter structure    • Slide design            • Committee Q&A sim         │
│   • Literature review    • Key contribution map    • Anticipate weaknesses     │
│   • Methodology chapter  • Demo preparation        • Mock defense              │
│   • Results & discussion                                                          │
│                                                                                 │
│   Output: Complete Thesis + Defense Slides + Q&A Preparation                   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼ (Defense Day)
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         PHASE 4 — REFLECTION                                     │
│                                                                                 │
│   🧠 Second Brain Reflection                                                     │
│   (second-brain-reflection)                                                     │
│                                                                                 │
│   • Compress lessons learned                                                     │
│   • Extract reusable rules                                                       │
│   • Archive artifacts                                                            │
│   • Plan next research direction                                                 │
│                                                                                 │
│   Output: Compressed Knowledge + Rules for Future Research                     │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The 5-Phase Stack

| Phase | Question | Skill | Output |
|:---|:---|:---|:---|
| **0. Foundation** | What do we know? What don't we know? | `sota-survey` + `research-question` + `research-design` | Literature Matrix + Gap Analysis + Research Proposal |
| **1. Experiment** | How do we test our hypothesis? | `experiment-tracking` | Experiment Logs + Results + Analysis |
| **2. Publish** | How do we communicate findings? | `paper-writing` + `journal-q1-polish` + `publication-strategy` | Submitted Paper |
| **3. Thesis** | How do we synthesize everything? | `thesis-writing` + `defense-prep` | Complete Thesis + Defense |
| **3.5 Visuals** | How do we communicate visually? | `ai-figure-generation` + `slide-automation` | Figures + Presentation Deck |
| **4. Reflect** | What did we learn? | `second-brain-reflection` | Compressed Rules & Lessons |

---

## 3. Continuous Support Skills

These skills run across all phases:

| Skill | When to Use | Phase |
|:---|:---|:---|
| `milestone-tracker` | Planning timeline, tracking deadlines, committee meetings | All |
| `progress-report` | Monthly/quarterly reports to advisor | 0, 1, 2 |
| `internal-critique` | Self-review before sharing with advisor (severity-graded) | 1, 2, 3 |
| `paper-audit` | Verify paper claims against code (reproducibility check) | 1, 2 |
| `research-watch` | Monitor field for new papers and trends | All |
| `technical-english-cs` | Writing, reviewing, polishing academic text | 2, 3 |
| `vietnamese-cs-terminology` | Translating CS terms to Vietnamese (HUST/VNU) | 2, 3 |
| `vietnamese-writing-standard` | Vietnamese orthography & tone correction | 2, 3 |

---

## 4. Key Integration Points

### SOTA → Research Question → Research Design

```
Literature Matrix (sota-survey)
    ↓
Identify Gap: "No existing work addresses [X] under [Y] conditions"
    ↓
Research Question (research-question):
  "How does [X] perform under [Y] compared to [Z]?"
    ↓
Research Design (research-design):
  • Methodology: [approach]
  • Baselines: [list]
  • Metrics: [list]
  • Reproducibility: [code + data + config]
```

### Experiment → Paper

```
Experiment Results (experiment-tracking)
    ↓
Select key findings (3-5 main results)
    ↓
Paper Structure (paper-writing):
  • Abstract: Problem → Method → Key Result → Significance
  • Introduction: Motivation + Gap + Contribution
  • Related Work: Position vs SOTA
  • Methodology: Reproducible description
  • Experiments: Results tables + significance tests
  • Conclusion: Summary + Future work
    ↓
Q1 Polish (journal-q1-polish):
  • De-AI protocol
  • Notation sync with thesis
  • IEEE/ACM formatting
```

### Paper → Thesis

```
Published Papers (publication-strategy)
    ↓
Thesis Structure (thesis-writing):
  • Introduction (synthesized from all papers)
  • Literature Review (expanded SOTA)
  • Methodology (unified framework)
  • Results (compiled experiments)
  • Discussion (broader implications)
  • Conclusion
    ↓
Defense Prep (defense-prep):
  • 20-min presentation
  • Committee Q&A simulation
  • Anticipate "so what?" questions
    ↓
Visual Communication (ai-figure-generation + slide-automation):
  • AI-generated conceptual figures
  • Automated slide deck from thesis content
  • Publication-ready visualizations
```

---

## 5. Quality Gates

| Gate | Checkpoint | Skill | Pass Criteria |
|:---|:---|:---|:---|
| **G0** | Proposal Defense | `phd-proposal` | Committee approves research direction |
| **G0** | Proposal Defense | `phd-proposal` | Committee approves research direction |
| **G0.5** | SOTA Verification | `paper-audit` | Key baselines verified against code |
| **G1** | First Experiment | `experiment-tracking` | Baseline reproduced, new method implemented |
| **G2** | First Paper | `paper-writing` + `internal-critique` | Advisor approves draft; no critical issues |
| **G3** | Major Revision | `publication-strategy` | Paper accepted with revisions |
| **G4** | Thesis Draft | `thesis-writing` | Advisor approves complete draft |
| **G4.5** | Presentation Ready | `ai-figure-generation` + `slide-automation` | Slides complete with figures |
| **G5** | Defense | `defense-prep` | Committee approves thesis |

---

## 6. How to Use This Repository

| Stage | Start Here |
|:---|:---|
| **Just starting PhD** | `sota-survey` → `research-question` → `phd-proposal` |
| **Have a research idea** | `research-design` → `experiment-tracking` |
| **Experiments done** | `paper-writing` → `internal-critique` → `journal-q1-polish` → `publication-strategy` |
| **Papers published** | `thesis-writing` → `defense-prep` |
| **Need presentation** | `ai-figure-generation` → `slide-automation` |
| **Staying current** | `research-watch` → `paper-audit` (for key papers) |
| **Writing in Vietnamese** | `vietnamese-cs-terminology` + `vietnamese-writing-standard` |
| **Need to report progress** | `progress-report` + `milestone-tracker` |

---

## 7. Integration with Product-Led Engineering

PhD research and product development share the same rigor:

| PhD | Product-Led | Shared Principle |
|:---|:---|:---|
| SOTA Survey | Problem Discovery | Evidence before building |
| Research Question | WHY Statement | Clear articulation of value |
| Experiments | PMR / A/B Testing | Validate hypothesis with data |
| Paper | MVP Ship | Communicate results |
| Thesis | Product Metrics | Synthesize learnings |
| Defense | Release | Face scrutiny, prove value |

> Both require **rigor**, **reproducibility**, and **clear communication of value**.

---

## References

- [Master Framework](./master-framework.md) — Product-Led Engineering workflow
- [PhD Workflow Integration](./phd-workflow-integration.md) — Detailed integration guide
