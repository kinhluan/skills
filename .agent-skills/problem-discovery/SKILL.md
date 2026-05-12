---
name: problem-discovery
description: Use when validating that a real-world problem exists before defining JTBD or writing code. Triggers on "is there demand for this?", "how do I validate this idea?", "should we build this?", or before any MVP scope decision. Combines multiple signal sources to produce a Problem Statement with confidence level.
metadata:
  tags: ["product", "discovery", "validation", "lmr", "jtbd", "mvp", "market-research", "problem-solution-fit"]
---

# Problem Discovery

**Validate the problem exists before defining the solution.**

This skill sits between strategic rationale (`why-strategic-rationale`) and solution definition (`business-product-leadership`). It answers: **"Is this problem real, specific, and painful enough to solve?"**

---

## Position in the Product R&D Flow

```
why-strategic-rationale  →  problem-discovery  →  business-product-leadership
      (WHY layer)              (VALIDATE layer)         (WHAT layer: JTBD + MVP)
```

---

## The Multi-Signal Discovery Framework

Use ≥ 2 signals. Confidence accumulates across signals — no single method is sufficient.

### Signal 1 — Customer Interviews (Always Required)

Ground truth. Everything else is proxy data.

**Protocol:**
- Talk to 5–10 people who represent the target segment
- Ask about past behavior, not hypothetical future intent
- Key questions:
  - "Tell me about the last time you experienced [problem area]."
  - "How did you solve it? What was frustrating about that?"
  - "How much time/money does this cost you?"
- **Red flag:** "I would use that" — this is intent, not evidence
- **Green flag:** "I spent 3 hours last week doing X manually" — specific, quantified past pain

**Output:** Verbatim quotes + frequency count of recurring pain themes

---

### Signal 2 — Labor Market Research (LMR)

Best for B2B / developer tools. Job postings reveal what companies are actively paying to solve.

**Protocol:**
1. Search job boards (LinkedIn, Indeed, specialized boards) for roles related to the problem domain
2. Identify recurring skill requirements → these are manual tasks ripe for automation
3. Check hiring volume trend (growing demand = problem getting worse, not better)
4. Validate compensation bands → high pay for scarce skill = strong demand signal

**Example:** 500+ job postings for "data pipeline engineer" with manual ETL skills = demand for automation tooling.

**Limitations:** Only works when the problem is currently solved by human labor. Not valid for consumer products or novel problem categories.

**Output:** Hiring volume + skill gap + estimated market size

---

### Signal 3 — Landing Page / Smoke Test

Measures behavioral intent, not stated preference.

**Protocol:**
- Build a landing page describing the product (1–2 days max, no actual product)
- Drive traffic via relevant communities (Reddit, HN, Slack groups, LinkedIn)
- Measure: sign-up rate, email capture, waitlist conversion
- **Threshold:** >5% conversion on cold traffic = strong signal

**Smoke test variant (Wizard of Oz):** Fake the product entirely. Take orders manually. See if anyone tries to use it before you build.

**Output:** Conversion rate + qualitative feedback from sign-ups

---

### Signal 4 — Competitor & Proxy Revenue Analysis

If others are solving the adjacent problem and making money, the problem is real.

**Protocol:**
- Find closest competitor or substitute solution
- Check: App Store ratings (high ratings + "wish it did X" reviews = gap), G2/Trustpilot reviews, job postings at competitor companies
- Estimate competitor revenue via SimilarWeb traffic × industry conversion rates
- Look for underserved segments: competitors with 3-star average in one niche

**Output:** Competitor landscape + underserved segment identification

---

## Confidence Assessment

After running ≥ 2 signals, assess overall confidence:

| Level | Criteria | Next Step |
|-------|----------|-----------|
| **High** | 2+ signals agree, verbatim quotes quantify pain, competitors exist and are profitable | Proceed to JTBD definition |
| **Medium** | 1 strong signal + 1 weak, pain is real but scope unclear | Run 1 more signal before JTBD |
| **Low** | Signals conflict or are weak, pain is theoretical | Do not proceed — pivot problem statement or abandon |

---

## Output: Problem Statement

```markdown
## Problem Statement — [Domain/Initiative Name]

**Date:** YYYY-MM-DD
**Confidence:** High / Medium / Low

### The Problem
[1 sentence: who has the problem, what it is, what it costs them]

### Evidence
| Signal | Finding | Strength |
|--------|---------|----------|
| Customer interviews (N=X) | [Key quote or pattern] | Strong / Weak |
| LMR | [Job volume, skill gap] | Strong / Weak |
| Landing page | [Conversion rate] | Strong / Weak |
| Competitor analysis | [Gap found] | Strong / Weak |

### The Segment
[Who specifically has this problem most acutely? This becomes the beachhead.]

### Kill Criteria
- [ ] [Condition that means "this problem isn't real enough to solve"]

### Open Questions
- [Assumption still unvalidated that could change direction]
```

---

## Ecosystem Connections

- **Requires upstream →** `why-strategic-rationale`: WHY Statement gives the strategic hypothesis that problem-discovery validates empirically
- **Feeds downstream →** `business-product-leadership`: Problem Statement → JTBD definition → Core Domain mapping → MVP scope
- **Feeds downstream →** `diffusion-release-tracking`: Segment identification → beachhead for Innovator/Early Adopter gates
- **Feeds downstream →** `ddd-core`: Problem scope → Core Domain boundary

---

## Anti-Patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Interviews only | Confirmation bias — people tell you what you want to hear | Combine with behavioral signal (landing page or LMR) |
| LMR only | Measures yesterday's problem, not tomorrow's opportunity | Validate with interviews to confirm pain is acute today |
| Survey instead of interview | Surveys answer "what", not "why" | Replace with open-ended 30-min conversations |
| Building before any signal | Sunk cost blinds you to negative evidence | Min 2 signals before writing production code |
| "Everyone I talked to loved it" | Selection bias — you talked to friends | Recruit strangers from target segment |
| Skipping Low-confidence problems | Feels like wasted time | A clear NO saves months of building the wrong thing |
