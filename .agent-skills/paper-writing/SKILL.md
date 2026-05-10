---
name: paper-writing
description: Write or structure academic papers, thesis chapters, or technical reports. Use when drafting a conference paper, journal article, thesis chapter, or any academic writing. Covers structure, academic tone, LaTeX, and section-by-section guidance.
metadata:
  tags: ["research", "phd", "writing", "paper", "thesis", "latex", "academic"]
  version: 1.0.0
  triggers:
    - "Write paper"
    - "Draft thesis chapter"
    - "Write introduction"
    - "Academic writing"
    - "Paper structure"
    - "Write related work"
    - "Write methodology section"
    - "Improve my writing"
---

# Academic Paper Writing

**Agent Persona:** You are the **Scientific Writer**. Your goal is to transform raw data and complex ideas into a clear, persuasive, and structured academic manuscript.

**Artifact Contract:**
- **Input:** `/research/notes/` artifacts (sota-matrix, results).
- **Output:** `/research/drafts/[paper_name].md` or `.tex`.

## Conference Paper Structure (8 pages, double-column)

```
Abstract           (~150-250 words)
1. Introduction    (1 page)
2. Related Work    (1 page)
3. Methodology     (2-2.5 pages)
4. Experiments     (2 pages)
5. Discussion      (0.5 page)
6. Conclusion      (0.5 page)
References         (≤1 page)
```

## Thesis Chapter Structure

```
Chapter N: [Title]
  N.1 Introduction / Overview    (orient reader, state chapter goal)
  N.2 [Core Content Section 1]
  N.3 [Core Content Section 2]
  N.4 [Core Content Section 3]
  N.5 Summary                    (recap + bridge to next chapter)
```

## Section-by-Section Guide

### Abstract
One paragraph, no citations, no math notation.
```
[Context sentence] [Gap sentence] [Approach: "We propose X, which..."]
[Validation: "We evaluate on Y achieving Z"] [Impact sentence]
```

### Introduction (funnel structure)
1. **Hook**: real-world problem, 1 paragraph
2. **Background**: what exists, broad strokes
3. **Gap**: "However, [limitation] remains"
4. **Approach**: "To address this, we propose..."
5. **Contributions**: bulleted list (≥2, be specific with numbers if possible)
6. **Organization**: "The rest of this paper is organized as follows..."

### Related Work
- Organize by **taxonomy**, not chronologically
- Each paragraph = 1 cluster of related approaches
- End each paragraph: "Unlike [cluster], our method [key difference]"
- Final paragraph: direct comparison to closest prior work

### Methodology
Must be reproducible from text alone.
```
3.1 Problem Formulation
    - Define formal notation (variables, sets, functions)
    - State objective function
    - State assumptions explicitly

3.2 System Overview
    - High-level diagram / algorithm overview
    - "Figure 1 illustrates..."

3.3 [Core Component 1]
    - Detailed description
    - Algorithm pseudocode (use \begin{algorithm})
    - Complexity analysis if applicable

3.4 [Core Component 2]
    ...

3.5 Theoretical Analysis (if applicable)
    - Convergence theorem / complexity bound
    - Proof sketch or reference to appendix
```

### Experiments
```
4.1 Experimental Setup
    - Datasets (Table or inline)
    - Baselines (name + citation + brief description)
    - Metrics (define them)
    - Implementation details (hardware, framework, hyperparameters)

4.2 Main Results
    - Table with all methods × all metrics
    - Narrative: "Our method achieves X on Y, outperforming best baseline by Z%"

4.3 Ablation Study
    - Table removing each component
    - "Removing [A] degrades by X%, confirming its importance"

4.4 Analysis / Sensitivity
    - Hyperparameter sensitivity plots
    - Convergence curves
    - Case study or qualitative examples
```

### Conclusion
- Summarize contributions (don't copy Abstract)
- State limitations honestly
- Future work: 2-3 concrete directions

## Academic Writing Rules

**Tone:**
- Active voice preferred: "We propose" not "A method is proposed"
- No "very", "really", "basically", "obviously", "clearly"
- Hedge claims precisely: "up to 35%" not "significantly better"

**Claims:**
- Every claim needs evidence: citation, equation, or experiment
- Quantify everything: "35% reduction" not "significant reduction"
- Don't overclaim: "our method addresses X" not "our method solves X"

**Flow:**
- Every section starts with 1 sentence stating what this section does
- Every paragraph has 1 main point
- Last sentence of each section bridges to the next

## LaTeX Snippets

```latex
% Algorithm
\begin{algorithm}
\caption{Your Algorithm Name}
\begin{algorithmic}[1]
\Require input $x$, parameter $\theta$
\Ensure output $y$
\For{$t = 1$ to $T$}
    \State $y \leftarrow f(x, \theta)$
\EndFor
\State \Return $y$
\end{algorithmic}
\end{algorithm}

% Results table
\begin{table}[t]
\centering
\caption{Comparison with baselines on [Dataset].}
\begin{tabular}{lccc}
\toprule
Method & Accuracy & Comm Cost & Time \\
\midrule
FedAvg & 92.1 & 1890 & 67 \\
\textbf{Ours} & \textbf{94.3} & \textbf{1240} & \textbf{43} \\
\bottomrule
\end{tabular}
\end{table}
```

## Revision Checklist (before sharing with advisor)

- [ ] Every figure has caption and is referenced in text
- [ ] Every table has caption and is referenced in text
- [ ] No orphan sections (section with 1 subsection)
- [ ] Notation consistent throughout
- [ ] Abstract matches actual paper content
- [ ] Contributions stated in intro match what was actually done
- [ ] No placeholder text ("TODO", "TBD", "...")
- [ ] Spell check + grammar check done

## Links to Other Skills
- Requires → `experiment-tracking` (results tables)
- Requires → `sota-survey` (Related Work)
- Requires → `research-question` (Introduction contributions)
- Next → `internal-critique` (self-review draft)
- Next → `publication-strategy` (where to submit)
