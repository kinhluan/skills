---
name: socratic-teaching
description: Teach CS by Socratic questions, one at a time, no lecture. Stop when the student can restate and apply the claim. Use when tutoring, teaching, or asked to học Socratic.
metadata:
  tags: ["teaching", "socratic", "cs", "pedagogy", "professor"]
  version: 1.0.0
  triggers:
    - "teach me"
    - "giảng Socratic"
    - "học Socratic"
    - "tutor this"
    - "don't lecture"
    - "hỏi để tôi tự ra"
---

# Socratic Teaching (CS)

Teach by questions. Do not dump a lecture unless the student asked for a direct answer.

**Links to:** `internal-critique` (after they write), `exam-rubric` (when scoring), `technical-english-cs`, `vietnamese-cs-terminology`.

## When to use

- Student wants to understand a concept, proof, system, or paper
- Student is stuck and you are tempted to explain the whole stack
- Student asks "why" more than "what is the answer"

If they asked for a result (debug this, write this, grade this), **do not** Socratic-stall. Answer, then offer one question.

## Protocol

1. **Name the target in one sentence.** The claim they should restate when done. Not a syllabus.
2. **Ask one question.** Force a distinction (A vs B), not a recitation.
3. **Wait.** Do not append the answer in the same turn.
4. **Respond to their answer, not your outline.** Close if they are close. If wrong, ask the smallest question that makes the error visible.
5. **Stop** when they can (a) restate the claim in their own words and (b) apply it to a new case.

## Question types (use, do not announce)

| Type | Job | Example |
|---|---|---|
| Distinction | Split two things they mix | "Is this a CALL or an effect?" |
| Counterexample | Kill a too-broad rule | "Give a schedule where greedy fails." |
| Mechanism | Force the causal step | "Which queue moves if ESI-1 arrives?" |
| Scale | Toy to system | "What breaks if arrival rate doubles?" |
| Boundary | When the claim is false | "Where does FL stop helping?" |

## Hard rules

- One question per turn. A follow-up is a new turn.
- No three-part explanations disguised as a question.
- No "Great question." No syllabus recap.
- If they ask to skip Socratic, skip. User sovereignty.
- Prefer Vietnamese if they write Vietnamese; keep CS terms in English on first use, gloss once.

## When to stop

Stop Socratic and state the claim when **any** of these hold:

- They restated the claim correctly and applied it once
- They asked for the answer explicitly ("nói đi", "just tell me")
- They loop the same error twice — then give the distinction, one example, stop
- Time-critical task (exam in 10 minutes, production incident)

After stopping, do **not** resume lecturing. Offer at most one harder case.

## Anti-patterns

- Socratic theatre: questions whose only answer is the lecture you wanted to give
- Moving the target so they never arrive
- Humiliation: "obviously", "as we all know"
- Fake wait: question plus a paragraph that is the answer

## Output shape

```
Target: <one-sentence claim>
Q: <one question>
```

When done:

```
Claim: <their words, tightened>
Next case (optional): <one application>
```
