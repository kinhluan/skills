---
name: why-strategic-rationale
description: >
  Establish the strategic rationale for a product or feature before building.
  Use this skill when evaluating a new product idea, justifying an initiative to
  stakeholders, validating whether a feature is worth building, or preparing a
  pitch document. Combines Value Proposition Canvas (structured analysis) with
  Amazon's Working Backwards PR/FAQ (narrative synthesis) in a 2-phase workflow.
metadata:
  tags: ["strategy", "value-proposition", "working-backwards", "pr-faq", "jtbd", "product-validation", "why"]
---

# WHY: Strategic Rationale

**"People don't buy what you do; they buy why you do it."** — Simon Sinek

Before WHAT (JTBD), WHEN (Rogers), HOW FAST (DORA), or HOW DESIGN (C4/DDD), answer one question: **Why should this exist?**

This skill produces the strategic foundation that every downstream decision builds on. If the WHY is weak, everything downstream is waste.

---

## The 2-Phase WHY Workflow

```
Phase 1: VALUE PROPOSITION CANVAS        Phase 2: WORKING BACKWARDS (PR/FAQ)
(Structured Analysis)                    (Narrative Synthesis)

┌──────────────────────┐                 ┌──────────────────────┐
│  Customer Profile    │                 │  Press Release       │
│  ┌────────────────┐  │    feeds into   │  ┌────────────────┐  │
│  │ Jobs           │──┼────────────────▶│  │ Headline       │  │
│  │ Pains          │  │                 │  │ Problem        │  │
│  │ Gains          │  │                 │  │ Solution       │  │
│  └────────────────┘  │                 │  │ Benefit        │  │
│  Value Map           │                 │  │ Quote          │  │
│  ┌────────────────┐  │                 │  └────────────────┘  │
│  │ Pain Relievers │──┼────────────────▶│  FAQ               │  │
│  │ Gain Creators  │  │                 │  ┌────────────────┐  │
│  │ Products/Svcs  │  │                 │  │ Why now?       │  │
│  └────────────────┘  │                 │  │ Why us?        │  │
└──────────────────────┘                 │  │ Why not X?     │  │
                                         │  │ What if fail?  │  │
         ↓                               │  └────────────────┘  │
   Structured understanding              └──────────────────────┘
   of customer value                                ↓
                                          Persuasive narrative
                                          + objection handling
                                                  ↓
                                          Output → JTBD (WHAT layer)
```

---

## Phase 1: Value Proposition Canvas (VPC)

The VPC maps **Customer Jobs, Pains, and Gains** to your **Value Map** (Pain Relievers, Gain Creators, Products & Services).

### Step 1: Customer Profile (Right Side)

Ask the user these questions. Probe deeply — surface-level answers produce weak strategies.

**Customer Jobs** — What is the customer trying to get done?
- Functional jobs: tasks, problems to solve, needs to meet
- Social jobs: how they want to be perceived, status, relationships
- Emotional jobs: how they want to feel, security, confidence
- Supporting jobs: jobs in the context of purchasing, using, disposing

**Pains** — What annoys, risks, or blocks the customer?
- Undesired outcomes: "This doesn't work the way I need"
- Obstacles: "I can't do this because..."
- Risks: "I'm afraid that..."
- Anxieties: "What if..."

**Gains** — What outcomes does the customer want beyond relief?
- Required gains: baseline expectations (table stakes)
- Expected gains: assumed improvements
- Desired gains: what they wish for
- Unexpected gains: things they haven't thought of

### Step 2: Value Map (Left Side)

**Products & Services** — What are you offering?
- List all products, services, and features

**Pain Relievers** — How do you eliminate customer pains?
- Map each Pain to a specific Pain Reliever
- Be explicit: "Pain X is relieved by Feature Y because..."

**Gain Creators** — How do you create customer gains?
- Map each Gain to a specific Gain Creator
- Be explicit: "Gain A is created by Feature B because..."

### Step 3: Fit Assessment

| Fit Level | Criteria | Verdict |
|---|---|---|
| **Problem-Solution Fit** | Pain Relievers address top 3 pains | ✅ Proceed to Phase 2 |
| **Partial Fit** | Some pains addressed, others ignored | ⚠️ Identify gaps, iterate |
| **No Fit** | Pains and Value Map don't align | ❌ Pivot or abandon |

**Critical rule:** If there is no Problem-Solution Fit, do NOT proceed to Phase 2. Go back to Customer Profile and re-validate.

---

## Phase 2: Working Backwards (PR/FAQ)

Transform the VPC analysis into a narrative document that answers: **Why this product? Why now? Why us?**

### The Press Release

Write a mock press release as if the product/feature has just launched. Date it 1–2 years in the future.

**Structure:**

```
HEADLINE: [Product Name] Helps [Customer Segment] [Achieve Key Gain]
          by [Core Value Proposition]

SUBHEAD: [One sentence expanding on the headline — the "so what?"]

[CITY], [DATE] — [Company/Team] today announced [Product Name], a
[category] that [primary benefit]. [Product Name] [key differentiator
vs. status quo].

"Quote from a hypothetical customer describing the transformation
they experienced." — [Name], [Role], [Company]

THE PROBLEM: [2-3 sentences describing the customer pain from VPC
Phase 1. Be specific — use the exact pains identified.]

THE SOLUTION: [2-3 sentences describing how the product addresses
those pains. Map directly to Pain Relievers from VPC.]

THE IMPACT: [2-3 sentences on the gains delivered. Use quantified
metrics where possible — time saved, cost reduced, revenue gained.]

AVAILABILITY: [When will this be available? What's the rollout plan?]
```

**Quality checks:**
- [ ] Headline mentions the customer, not the technology
- [ ] Problem section uses language from VPC Customer Profile
- [ ] Solution maps directly to VPC Pain Relievers + Gain Creators
- [ ] Impact section has at least one quantified metric
- [ ] A non-technical person can understand the entire PR

### The FAQ (Anticipated Objections)

Write 8–12 questions a skeptical stakeholder, investor, or customer would ask. Answer each honestly.

**Categories:**

**Why This? (Strategic Rationale)**
- Q: Why is this worth building?
  → Answer using VPC Pain/Gain analysis. Reference the top 3 pains.
- Q: What's the competitive advantage?
  → Compare to alternatives. What's different about this approach?

**Why Now? (Timing)**
- Q: Why not wait 6 months?
  → Reference market signals, competitor moves, customer urgency
- Q: What's the cost of NOT doing this?
  → Quantify: lost revenue, churn risk, competitive disadvantage

**Why Us? (Capability)**
- Q: Why is this team the right one to build this?
  → Domain expertise, existing assets, unique data, network effects
- Q: What's the unfair advantage?
  → Moats: data, distribution, brand, switching costs, network effects

**What If We Fail? (Risk)**
- Q: What's the biggest risk?
  → Identify the #1 assumption that could be wrong
- Q: How will we know if this is failing?
  → Define kill criteria: what signal means "stop"?
- Q: What's the minimum experiment to validate?
  → Smallest possible test of the riskiest assumption

**Scope & Constraints**
- Q: What's explicitly NOT in scope?
  → Boundaries prevent scope creep
- Q: What dependencies does this have?
  → External APIs, team availability, data access, compliance

---

## Output: WHY Statement

After completing both phases, produce a single **WHY Statement** that serves as the strategic anchor for all downstream work.

```
## WHY Statement — [Product/Feature Name]

**Date:** YYYY-MM-DD
**Author:** [Name/Team]

### The Customer
[1-2 sentences: who they are, what they care about — from VPC Profile]

### The Problem
[1-2 sentences: the #1 pain that justifies this initiative — from VPC Pains]

### The Opportunity
[1-2 sentences: the gain that makes this worth pursuing — from VPC Gains]

### The Thesis
[1 sentence: "We believe that [action] for [customer] will result in
[outcome] because [reason]."]

### Kill Criteria
- [ ] [Condition that means "stop building this"]
- [ ] [Condition that means "pivot to a different approach"]

### Confidence Level
| Assumption | Confidence (H/M/L) | Validation Method |
|---|---|---|
| [Key assumption 1] | H/M/L | [How to verify] |
| [Key assumption 2] | H/M/L | [How to verify] |
| [Key assumption 3] | H/M/L | [How to verify] |
```

---

## Connecting to the Ecosystem

### → `business-product-leadership` (WHAT)

The WHY Statement feeds directly into JTBD definition:

| WHY Output | JTBD Input |
|---|---|
| VPC Customer Jobs | → JTBD Situation + Motivation |
| VPC Gains | → JTBD Expected Outcome |
| PR/FAQ Problem section | → LMR validation evidence |
| WHY Thesis | → MVP scope boundary |

**Flow:** WHY (VPC) → WHAT (JTBD/LMR/MVP)

### → `diffusion-release-tracking` (WHEN)

The PR/FAQ's "Availability" section and FAQ's "Why Now?" inform Rogers gate planning:

| WHY Signal | WHEN Decision |
|---|---|
| Strong "Why Now?" (urgency, market window) | → Faster gate cadence |
| Weak "Why Now?" (nice-to-have) | → Slower validation, longer Innovator gate |
| Kill criteria defined | → Gate failure = execute kill criteria |

### → `dora-core` (HOW FAST/SAFE)

The FAQ's "What's the minimum experiment?" answer maps to DORA delivery capability:

| WHY Signal | DORA Implication |
|---|---|
| Need for rapid experimentation | → Requires Elite/High Deployment Frequency |
| Kill criteria are time-sensitive | → Requires fast Lead Time + low MTTR |
| High-confidence thesis | → Can tolerate Medium DORA tier |

### → `c4-model` + `ddd-core` (HOW DESIGN)

The VPC Value Map directly informs DDD domain modeling:

| WHY Output | HOW DESIGN Input |
|---|---|
| VPC Products & Services | → C4 L2 Container candidates |
| VPC Pain Relievers | → DDD Core Domain responsibilities |
| VPC Gain Creators | → DDD Supporting Subdomain features |
| FAQ "What's NOT in scope" | → DDD Generic Subdomain (buy/SaaS) |

---

## Anti-Patterns

- **Building the WHY after the code:** If you're writing the PR/FAQ to justify something already built, you're rationalizing, not validating. WHY comes first.
- **Confusing WHAT with WHY:** "We need a dashboard" is WHAT. "Operators waste 2 hours/day compiling data manually" is WHY.
- **Skipping the VPC:** Jumping straight to PR/FAQ without structured analysis produces persuasive but unfounded narratives. Garbage in, garbage out.
- **No kill criteria:** A WHY without kill criteria is a wish, not a strategy. Every thesis must have a falsification condition.
- **One-sided FAQ:** If every FAQ answer is positive, you're writing marketing, not strategy. Include genuine risks and honest limitations.
- **Ignoring emotional/social jobs:** Functional jobs alone produce commodity products. The VPC Customer Profile must include social and emotional dimensions.
