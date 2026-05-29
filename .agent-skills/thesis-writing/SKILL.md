---
name: thesis-writing
description: Write PhD/Master's thesis — full chapter structure, literature review chapter, methodology chapter, results chapter, discussion chapter, and conclusion. Use when drafting thesis chapters, organizing thesis structure, or converting papers into thesis format.
metadata:
  tags: ["research", "phd", "thesis", "writing", "academic", "chapter", "literature-review", "methodology"]
  version: 1.0.0
  triggers:
    - "write thesis"
    - "thesis chapter"
    - "literature review chapter"
    - "methodology chapter"
    - "results chapter"
    - "discussion chapter"
    - "viết luận văn"
    - "chương luận văn"
    - "tổng quan tài liệu"
---

# Thesis Writing

**Purpose:** Guide for writing PhD/Master's thesis — the most comprehensive document in a researcher's career.

**When to use:**
- Writing individual thesis chapters
- Converting papers into thesis format
- Organizing thesis structure
- Writing literature review chapter
- Writing methodology chapter

**Links to:**
- `paper-writing` — section-level writing skills
- `sota-survey` — literature review foundation
- `research-design` — methodology chapter content
- `experiment-tracking` — results chapter data
- `technical-english-cs` — academic English
- `vietnamese-writing-standard` — Vietnamese thesis writing

---

## Thesis Structure (Standard PhD)

```
Front Matter
├── Title Page
├── Abstract (Vietnamese + English)
├── Acknowledgments
├── Table of Contents
├── List of Figures
├── List of Tables
├── List of Abbreviations
└── List of Symbols

Chapters
├── Chapter 1: Introduction (10-15 pages)
│   ├── 1.1 Background & Motivation
│   ├── 1.2 Problem Statement
│   ├── 1.3 Research Objectives
│   ├── 1.4 Research Questions
│   ├── 1.5 Contributions
│   ├── 1.6 Scope & Limitations
│   └── 1.7 Thesis Organization
│
├── Chapter 2: Literature Review (20-30 pages)
│   ├── 2.1 Overview of Research Area
│   ├── 2.2 Theoretical Foundations
│   ├── 2.3 Related Work Taxonomy
│   ├── 2.4 Detailed Analysis of Key Works
│   ├── 2.5 Comparison Table
│   └── 2.6 Research Gaps
│
├── Chapter 3: Methodology (15-25 pages)
│   ├── 3.1 Problem Formulation
│   ├── 3.2 System Overview
│   ├── 3.3 Component 1 (your method)
│   ├── 3.4 Component 2 (your method)
│   ├── 3.5 Theoretical Analysis
│   └── 3.6 Complexity Analysis
│
├── Chapter 4: Experiments (15-20 pages)
│   ├── 4.1 Experimental Setup
│   ├── 4.2 Datasets
│   ├── 4.3 Baselines
│   ├── 4.4 Main Results
│   ├── 4.5 Ablation Studies
│   ├── 4.6 Sensitivity Analysis
│   └── 4.7 Discussion of Results
│
├── Chapter 5: Discussion (5-10 pages)
│   ├── 5.1 Interpretation of Results
│   ├── 5.2 Implications
│   ├── 5.3 Limitations
│   └── 5.4 Threats to Validity
│
└── Chapter 6: Conclusion (3-5 pages)
    ├── 6.1 Summary of Contributions
    ├── 6.2 Answers to Research Questions
    ├── 6.3 Future Work
    └── 6.4 Final Remarks

Back Matter
├── References
├── Appendices
│   ├── Appendix A: Proofs
│   ├── Appendix B: Additional Experiments
│   └── Appendix C: Code/Data Availability
└── Publications During PhD
```

---

## Chapter-by-Chapter Guide

### Chapter 1: Introduction

**Purpose:** Set the stage — why this research matters.

```markdown
## 1.1 Background & Motivation
[2-3 paragraphs]
- Broad context of the research area
- Real-world problem or application
- Why this problem is important

## 1.2 Problem Statement
[1-2 paragraphs]
- Specific gap in existing knowledge
- Limitations of current approaches
- "However, [limitation] remains unsolved..."

## 1.3 Research Objectives
[Bulleted list]
- Primary: [Main objective]
- Secondary: [Supporting objectives]

## 1.4 Research Questions
[Numbered list]
- RQ1: [Primary research question]
- RQ2: [Secondary research question]
- RQ3: [Optional tertiary question]

## 1.5 Contributions
[Numbered list, be specific]
1. We propose [method name] that [what it does]
2. We demonstrate [finding] through [experiments]
3. We release [artifact] for reproducibility

## 1.6 Scope & Limitations
- What this thesis covers
- What this thesis does NOT cover
- Assumptions made

## 1.7 Thesis Organization
"The remainder of this thesis is organized as follows.
Chapter 2 reviews... Chapter 3 describes... Chapter 4 presents...
Chapter 5 discusses... Chapter 6 concludes..."
```

### Chapter 2: Literature Review

**Purpose:** Comprehensive survey — position your work in the field.

**Structure:**
```markdown
## 2.1 Overview of Research Area
[2-3 pages]
- History and evolution
- Current state of the art
- Key milestones

## 2.2 Theoretical Foundations
[3-5 pages]
- Core concepts and definitions
- Mathematical foundations
- Key theorems/properties

## 2.3 Related Work Taxonomy
[2-3 pages]
- Group A: [Approach name] — papers [1,3,5]
- Group B: [Approach name] — papers [2,4]
- Group C: [Approach name] — papers [6,7]

## 2.4 Detailed Analysis of Key Works
[8-12 pages]
For each important paper:
- Problem addressed
- Method proposed
- Strengths
- Limitations
- How our work differs

## 2.5 Comparison Table
| Paper | Year | Problem | Method | Dataset | Result | Limitation |
|-------|------|---------|--------|---------|--------|------------|
| ...   | ...  | ...     | ...    | ...     | ...    | ...        |

## 2.6 Research Gaps
[1-2 pages]
- Gap 1: [Description] → addressed by RQ1
- Gap 2: [Description] → addressed by RQ2
- Gap 3: [Description] → addressed by RQ3
```

**Key rules:**
- Synthesize, don't just list papers
- Organize by theme, not chronology
- Each paragraph ends with: "Unlike [them], we [difference]"
- Include 50-100+ references (depending on field)

### Chapter 3: Methodology

**Purpose:** Describe your approach in enough detail for reproduction.

```markdown
## 3.1 Problem Formulation
- Formal notation (variables, sets, functions)
- Objective function
- Constraints
- Assumptions (state explicitly)

## 3.2 System Overview
[2-3 pages]
- High-level architecture diagram
- Component relationships
- Data flow

## 3.3 Component 1: [Name]
[4-6 pages]
- Motivation
- Algorithm description
- Pseudocode (use algorithm environment)
- Mathematical formulation
- Complexity: O(...)

## 3.4 Component 2: [Name]
[4-6 pages]
- Same structure as 3.3

## 3.5 Theoretical Analysis
[2-3 pages]
- Convergence properties
- Optimality bounds
- Proofs (or reference to Appendix A)

## 3.6 Complexity Analysis
| Operation | Time | Space |
|-----------|------|-------|
| Training  | O()  | O()   |
| Inference | O()  | O()   |
| Total     | O()  | O()   |
```

### Chapter 4: Experiments

**Purpose:** Empirical validation of your claims.

```markdown
## 4.1 Experimental Setup
- Hardware: GPU type, RAM, storage
- Software: Framework versions, libraries
- Hyperparameters: Search ranges and final values

## 4.2 Datasets
| Dataset | Domain | Size | Train/Val/Test | Source |
|---------|--------|------|----------------|--------|
| ...     | ...    | ...  | ...            | ...    |

## 4.3 Baselines
| Method | Year | Type | Citation |
|--------|------|------|----------|
| ...    | ...  | SOTA | ...      |

## 4.4 Main Results
| Method | Metric1 | Metric2 | Metric3 |
|--------|---------|---------|---------|
| ...    | XX.X    | XX.X    | XX.X    |
| Ours   | **XX.X**| **XX.X**| **XX.X**|

Analysis: "Our method achieves X on Y, outperforming best baseline by Z%"

## 4.5 Ablation Studies
| Configuration | Metric1 | Metric2 |
|---------------|---------|---------|
| Full model    | XX.X    | XX.X    |
| w/o Component1| XX.X    | XX.X    |
| w/o Component2| XX.X    | XX.X    |

## 4.6 Sensitivity Analysis
- Hyperparameter sensitivity plots
- Convergence curves
- Scalability experiments

## 4.7 Discussion of Results
- Answer RQ1: [with evidence]
- Answer RQ2: [with evidence]
- Answer RQ3: [with evidence]
```

### Chapter 5: Discussion

**Purpose:** Interpret results, acknowledge limitations.

```markdown
## 5.1 Interpretation of Results
- Why does your method work?
- What patterns emerged?
- Unexpected findings

## 5.2 Implications
- Theoretical contributions
- Practical applications
- Impact on the field

## 5.3 Limitations
- Dataset limitations
- Method assumptions
- Computational constraints
- Generalizability concerns

## 5.4 Threats to Validity
- Internal validity
- External validity
- Construct validity
- Conclusion validity
```

### Chapter 6: Conclusion

**Purpose:** Wrap up — summarize and look forward.

```markdown
## 6.1 Summary of Contributions
[Numbered list matching Chapter 1 contributions]

## 6.2 Answers to Research Questions
- RQ1: [Answer with key evidence]
- RQ2: [Answer with key evidence]
- RQ3: [Answer with key evidence]

## 6.3 Future Work
1. [Short-term: next experiments]
2. [Medium-term: extensions]
3. [Long-term: broader applications]

## 6.4 Final Remarks
[1-2 paragraphs: significance, impact, personal reflection]
```

---

## Converting Papers to Thesis

### Paper → Chapter Mapping

| Paper Section | Thesis Chapter | Adjustments |
|---------------|----------------|-------------|
| Abstract | Chapter 1 intro | Expand motivation |
| Introduction | Chapter 1 | Add more background |
| Related Work | Chapter 2 | Expand significantly (3-5x) |
| Method | Chapter 3 | Add more detail, proofs |
| Experiments | Chapter 4 | Add more analysis |
| Discussion | Chapter 5 | Expand limitations |
| Conclusion | Chapter 6 | Add future work |

### Key Differences

| Aspect | Paper | Thesis |
|--------|-------|--------|
| Length | 8-12 pages | 150-250 pages |
| References | 30-50 | 100-200 |
| Related Work | 1-2 pages | 20-30 pages |
| Method detail | Concise | Exhaustive |
| Proofs | Sketch | Full (appendix) |
| Audience | Experts | Committee (broader) |

---

## Vietnamese Thesis Format

### Abstract Structure (Vietnamese)
```
Tóm tắt
[1 đoạn: Bối cảnh và động lực]
[1 đoạn: Vấn đề nghiên cứu]
[1 đoạn: Phương pháp đề xuất]
[1 đoạn: Kết quả chính]
[1 đoạn: Đóng góp]
```

### Chapter Titles (Vietnamese)
```
Chương 1: Giới thiệu
Chương 2: Tổng quan tài liệu
Chương 3: Phương pháp
Chương 4: Thực nghiệm và kết quả
Chương 5: Thảo luận
Chương 6: Kết luận
```

---

## LaTeX Tips for Thesis

### Document Class
```latex
\documentclass[12pt,a4paper]{report}
\usepackage[utf8]{vietnam}
```

### Chapter Formatting
```latex
\chapter{Giới thiệu}
\section{Bối cảnh và động lực}
\subsection{Tầm quan trọng của vấn đề}
```

### Cross-References
```latex
Như đã trình bày trong Chương~\ref{ch:literature}...
Kết quả của Thực nghiệm~\ref{exp:main} cho thấy...
```

### Bibliography
```latex
% Use BibTeX with thesis style
\bibliographystyle{plain}
\bibliography{references}
```

---

## Integration Flow

```
sota-survey (literature review)
    ↓
research-question (RQs)
    ↓
research-design (methodology)
    ↓
thesis-writing (this skill)
    ├── Chapter 1: Introduction
    ├── Chapter 2: Literature Review ← sota-survey
    ├── Chapter 3: Methodology ← research-design
    ├── Chapter 4: Experiments ← experiment-tracking
    ├── Chapter 5: Discussion
    └── Chapter 6: Conclusion
    ↓
paper-writing (extract papers from thesis)
    ↓
journal-q1-polish (polish for Q1)
    ↓
publication-strategy (where to submit)
    ↓
conference-paper (present at conference)
    ↓
progress-report (report to advisor)
    ↓
defense-prep (prepare for defense)
```
