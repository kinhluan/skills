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

## PMR Output → JTBD Validation

After running the multi-signal discovery framework, map findings to JTBD components. This is the bridge from VALIDATE to WHAT layer.

### JTBD Validation Matrix

| JTBD Component | PMR Input | Validated? | If Not Validated |
|---|---|---|---|
| **Situation** (context/frequency) | Interview: "How often does this happen?" | ≥ 3x/week | Problem is too infrequent — pivot or abandon |
| **Motivation** (pain severity) | Survey: Pain rating 1-10 | ≥ 40% rate 7+ | Pain is too mild — not worth solving |
| **Expected Outcome** (value) | Landing page conversion | ≥ 5% cold traffic | Value proposition not compelling — rewrite |
| **Willingness to Pay** | Van Westendorp pricing | Clear acceptable range | No monetization path — freemium or abandon |

### From Problem Statement to JTBD

```
Problem Statement:
"[Segment] struggles with [Problem] because [Root cause],
 costing them [Quantified cost] per [Time period]."

        ↓  Convert to JTBD

JTBD Statement:
"When [Situation from Problem context], I want to [Motivation from Root cause],
 so I can [Expected Outcome that eliminates Quantified cost]."
```

**Example:**

```
Problem: "Engineering managers at 50-200 person startups spend 4+ hours/week
          compiling status updates because their tools don't surface blockers
          automatically."

JTBD: "When I'm planning the week, I want to see team blockers at a glance,
       so I can remove obstacles before they derail sprint goals."
```

### JTBD Quality Checklist

Before proceeding to MVP scope, ensure each JTBD is:

- [ ] **Specific:** Not "I want to be more productive" but "I want to see blockers at a glance"
- [ ] **Situation-based:** Starts with "When..." — tied to real context
- [ ] **Motivation-focused:** Describes what the user wants to achieve, not what the product does
- [ ] **Outcome-oriented:** Ends with "so I can..." — measurable benefit
- [ ] **Validated by PMR:** At least 2 signals confirm this JTBD is real

### Go/No-Go Per JTBD

```
For each JTBD derived from the Problem Statement:

✅ GO — All components validated:
   • Situation: confirmed by interviews
   • Motivation: pain severity ≥ 7/10 for ≥ 40%
   • Outcome: landing page or survey confirms value
   → Include in MVP Core Domain

⚠️ DEFER — Partially validated:
   • 1-2 components confirmed, others unclear
   → Add to roadmap, not MVP

❌ NO-GO — Not validated:
   • < 2 signals confirm
   • Pain severity < 5/10
   • No willingness to pay
   → Drop from scope, revisit in future iteration
```

---

## Quantitative Signal Methods

### Signal 5 — Structured Survey (Quantitative Validation)

Use surveys to validate patterns found in interviews at scale.

**When to use:**
- You have hypotheses from interviews that need scale validation
- You need to segment the market by pain severity
- You want to quantify willingness-to-pay

**Survey Design:**
```
Section 1: Screening (2-3 questions)
  - Confirm respondent is in target segment
  - Filter out non-target respondents early

Section 2: Problem Frequency & Severity (5-7 questions)
  - "How often do you experience [problem]?" (Never/Rarely/Sometimes/Often/Always)
  - "How painful is this problem?" (1-10 scale)
  - "What is the business impact?" (Lost time, lost revenue, missed opportunity)

Section 3: Current Solutions (3-4 questions)
  - "How do you currently solve this?"
  - "How satisfied are you with current solutions?" (1-10)
  - "What would an ideal solution look like?"

Section 4: Willingness-to-Pay (2 questions)
  - Van Westendorp Price Sensitivity Meter:
    "At what price would this be too expensive?"
    "At what price would this be so cheap you'd question quality?"
    "At what price would this start to feel expensive?"
    "At what price would this be a bargain?"
```

**Sample Size:**
- Minimum: 100 responses for directional signal
- Recommended: 200-300 for statistical significance
- Segment analysis: 50+ per segment

**Analysis:**
- Problem severity distribution (look for ≥40% rating 7+ out of 10)
- Correlation: frequent + severe = high-priority problem
- Gap analysis: high pain + low satisfaction with current solutions = opportunity

### Signal 6 — Market Sizing (TAM/SAM/SOM)

Quantify the market to assess opportunity size.

```
TAM (Total Addressable Market): Everyone who could use this
  → Calculation: Total potential customers × average contract value
  → Example: 10M small businesses × $100/month = $12B/year TAM

SAM (Serviceable Addressable Market): Who you can realistically reach
  → Calculation: TAM × geographic/vertical constraints
  → Example: $12B × 20% (English-speaking, tech-savvy) = $2.4B SAM

SOM (Serviceable Obtainable Market): Who you can capture in 3-5 years
  → Calculation: SAM × realistic market share
  → Example: $2.4B × 2% = $48M SOM
```

**Sources:**
- Industry reports (Gartner, IDC, Forrester)
- Government statistics (census, labor data)
- Bottom-up: Count actual potential customers
- Top-down: Start from industry total and narrow

**Validation rule:** SOM should be ≥$10M for VC-backed, ≥$1M for bootstrapped

### Signal 7 — Behavioral Data Analysis

Analyze existing data to find evidence of the problem.

**Sources:**
- **Web analytics:** High bounce rate on key pages, abandoned flows, search queries
- **Support tickets:** Recurring themes, frequency trends
- **App reviews:** Common complaints, feature requests
- **Social media:** Complaints about current solutions, "wish someone would build..."
- **Job board data:** Skills gaps, hiring volume (LMR signal)

**Analysis framework:**
```
1. Collect all mentions of the problem domain
2. Categorize by: frequency, severity, sentiment
3. Trend analysis: Is this problem growing or shrinking?
4. Segment by: user type, company size, industry
```

---

## Ecosystem Connections

- **Requires upstream →** `why-strategic-rationale`: WHY Statement gives the strategic hypothesis that problem-discovery validates empirically
- **Feeds downstream →** `business-product-leadership`: Problem Statement → JTBD definition → Core Domain mapping → MVP scope
- **Feeds downstream →** `diffusion-release-tracking`: Segment identification → beachhead for Innovator/Early Adopter gates
- **Feeds downstream →** `ddd-core`: Problem scope → Core Domain boundary
- **Feeds downstream →** `product-analytics`: Survey data → persona segmentation → metric baselines

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
