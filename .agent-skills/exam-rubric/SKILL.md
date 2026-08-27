---
name: exam-rubric
description: Grade CS work with an explicit rubric. Separate collaboration from plagiarism. Use when scoring exams, assignments, orals, lab reports, or suspected copied code.
metadata:
  tags: ["teaching", "exam", "rubric", "plagiarism", "cs", "pedagogy"]
  version: 1.0.0
  triggers:
    - "grade this"
    - "chấm bài"
    - "rubric"
    - "plagiarism or collaboration"
    - "score this exam"
    - "chấm đồ án"
---

# Exam Rubric (CS)

Score against a published rubric. Never invent a grade from vibe. Separate **collaboration** (allowed process) from **plagiarism** (stolen product).

**Links to:** `socratic-teaching` (feedback after the score), `internal-critique` (paper-shaped work), `code-review-pr` (code quality, not integrity).

## When to use

- Scoring an exam, assignment, oral, lab, or thesis chapter
- Student asks "is this copy?" or "được làm nhóm không?"
- Need a grade that would survive a regrade petition

If they asked you to *write* the solution, do not grade it as if it were theirs.

## Build the rubric first

Before scoring, write four things. If the instructor already has them, use theirs.

1. **Learning targets** (3–6). What the student must show, not what the prompt mentioned.
2. **Levels** for each target: Missing / Partial / Meets / Exceeds (or 0 / 1 / 2).
3. **Evidence** each level requires (a named artifact: proof step, plot, complexity, test).
4. **Weights** that sum to 100.

Do not add hidden criteria after seeing the answer.

## Default CS dimensions (adapt, do not cargo-cult)

| Dimension | Missing | Partial | Meets | Exceeds |
|---|---|---|---|---|
| Problem statement | Wrong problem | Right problem, wrong constraints | Constraints named | States what is *not* claimed |
| Method | No method | Method named, not applied | Applied to the given instance | Notes when the method fails |
| Correctness | Broken / no invariant | Some cases work | Stated invariant or test that can fail | Edge cases + counterexample to a wrong algorithm |
| Complexity / systems | None | Asymptotic name only | Time/space or bottleneck named | Bottleneck + what happens at 10× |
| Communication | Unreadable | Readable but terms mixed | Terms consistent (EN + one VN gloss) | Claim in first sentence |

Oral: replace Communication with "can restate under a new input."

## Scoring protocol

1. Read the rubric, then the work, then the rubric again.
2. Score each dimension independently. A brilliant method does not rescue a false claim.
3. Quote **one** piece of evidence per dimension (line, figure, sentence).
4. Total = weighted sum. Round at the end, not per cell.
5. Write three lines of feedback: keep / fix / next practice. No moral lecture.

## Collaboration vs plagiarism

These are different findings. Do not collapse them.

| | Collaboration | Plagiarism |
|---|---|---|
| What moved | Process (discussion, pair-debug, shared test idea) | Product (text, proof, code, figure) presented as own |
| Typical evidence | Similar approach, different bugs/names, student can explain | Near-verbatim blocks, identical odd mistakes, cannot explain a line |
| Academic response | Allowed if the spec allows it; still must disclose | Integrity case; score as unverifiable; do not split the difference |

**Code:** identical AST + identical unique comments → plagiarism until proven otherwise. Shared algorithm + different tests/names → collaboration if the spec allows.

**Text:** uncited sentences from a paper, blog, or model output → plagiarism. Cited paraphrase → not.

**Models:** LLM use is collaboration with a tool if the spec allows and the student can defend every line. Submitting model output they cannot explain is ghostwriting (integrity), even if "original" to the model.

If integrity is uncertain: **do not guess a penalty**. Flag, quote the overlap, ask the student to explain the flagged span. Grade only what they can defend.

## Integrity flags (not a verdict)

- Long identical spans (code or prose) with no citation
- Citation that does not contain the claimed result
- Numbers that do not match the table they cite
- Cannot explain a line they "wrote"
- Sudden register shift (one paragraph native, next academic-perfect)

A flag is a question, not a conviction.

## Anti-patterns

- Holistic "feels like a 7"
- Punishing allowed collaboration
- Extra credit for length
- Mixing Vietnamese and English criteria mid-rubric
- Scoring effort instead of evidence

## Output shape

```
Targets: <list>
Rubric: <dimension × level, weights>
Scores: <table with one evidence quote each>
Total: <number / 100>
Integrity: clean | collaboration-disclosed | flag (quote span, not verdict)
Feedback: keep / fix / next
```
