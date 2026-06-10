---
name: business-product-leadership
description: Strategic frameworks for Product/Business Owners. Use this skill for Product Market Research, defining Jobs-To-Be-Done (JTBD), understanding Diffusion of Innovations, planning MVPs, separating deployment (Ship) from business launch (Release), product metrics, A/B testing, pricing, and go-to-market strategy.
metadata:
  tags: ["product-management", "business-strategy", "jtbd", "mvp", "agile-delivery", "diffusion-of-innovations", "metrics", "analytics", "pricing", "go-to-market"]
---

# Business & Product Leadership

This skill bridges the gap between Business Strategy and Technical Execution. It is designed for Product Owners and Founders who manage both the business viability and the product delivery.

## 📈 1. Business Strategy & Discovery

### The JTBD → Value Prop → PMR Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│   WHY Layer     │────→│    WHAT Layer    │────→│   VALIDATE Layer    │
│                 │     │                  │     │                     │
│ VPC Customer    │     │ JTBD Statement   │     │ Product Market      │
│ Jobs/Pains/Gains│────→│ "When [S], I     │────→│ Research (PMR)      │
│                 │     │  want [M], so    │     │                     │
│ Value Prop      │     │  I can [O]"      │     │ • Interviews        │
│ Statement       │     │                  │     │ • Surveys           │
│                 │     │ 1 Value Prop     │     │ • Landing page      │
│ "[Product] helps│     │ → 1-3 JTBDs      │     │ • Behavioral data   │
│  [Customer]     │     │                  │     │                     │
│  [solve Problem]│     │ JTBD defines     │     │ PMR validates/      │
│  by [Approach]" │     │ WHAT to build    │     │ invalidates JTBD    │
└─────────────────┘     └──────────────────┘     └─────────────────────┘
         │                       │                        │
         └───────────────────────┴────────────────────────┘
                                 ↓
                    ┌─────────────────────┐
                    │   MVP Scope         │
                    │ • Core Domain       │
                    │ • Beachhead segment │
                    │ • Kill criteria     │
                    └─────────────────────┘
```

### Jobs-To-Be-Done (JTBD) Framework

People don't buy products; they "hire" them to get a job done.

**The JTBD Statement:** *"When [Situation], I want to [Motivation], so I can [Expected Outcome]."*

**Example:** *"When I am commuting, I want to listen to educational content easily, so I can feel productive."*

**Focus:** Build features that directly solve the core *Job*, not just what users *say* they want.

### Value Proposition Statement

The strategic narrative that connects your product to customer value. Derived from WHY layer (VPC).

```
"[Product] helps [Customer Segment] [solve Core Problem]
 by [Unique Approach], resulting in [Measurable Gain]."
```

**Relationship: 1 Value Prop → 1-3 JTBDs**

| Value Prop Component | JTBD Element | Example |
|---|---|---|
| Customer Segment | → Situation | "knowledge workers" → "When I'm planning my week" |
| Core Problem | → Motivation | "disorganized work" → "I want to see everything in one place" |
| Measurable Gain | → Expected Outcome | "save 2+ hours/week" → "so I can stay organized without switching apps" |

### Product Market Research (PMR)

Validate the JTBD assumptions before building. PMR answers: *"Does the market actually want this job done?"*

**PMR validates each JTBD component:**

| JTBD Component | PMR Validation Method | Pass Criteria |
|---|---|---|
| **Situation** (frequency) | Interviews: "How often does this happen?" | ≥ 3x per week |
| **Motivation** (pain severity) | Survey: "Rate pain (1-10)" | ≥ 40% rate 7+ |
| **Expected Outcome** (value) | Landing page conversion | ≥ 5% cold traffic |
| **Willingness to pay** | Van Westendorp pricing | Clear acceptable price range |

**PMR Action Flow:**
```
Step 1: Desk Research (1-2 weeks)
  → Market sizing (TAM/SAM/SOM)
  → Competitor landscape
  → Industry trends

Step 2: Qualitative Research (2-3 weeks)
  → 5-10 customer interviews
  → Validate Jobs, Pains, Gains from VPC
  → Discover current workarounds

Step 3: Quantitative Validation (2-4 weeks)
  → Survey 100-300 respondents
  → Landing page / smoke test
  → Behavioral data analysis

Step 4: Synthesis
  → Map findings to each JTBD
  → Validate / invalidate / refine
  → Define beachhead segment
  → Go/No-Go decision
```

**Critical rule:** JTBD must be defined BEFORE PMR. You cannot validate what you haven't articulated.

### Product Market Research & Market Fit
Before building anything, validate market demand for the *product* you intend to create.
- **Identify the Problem:** What specific pain point or unmet need does your product solve?
- **Competitor Analysis:** Who else is solving this problem? How can you differentiate (Price, Speed, Quality, UX)?
- **Target Segment:** Who is your ideal early user, and what triggers them to seek a solution?
- **Validation Methods:** Customer interviews, landing page tests, smoke tests — validate *demand* before writing production code.

### Diffusion of Innovations (Rogers, 1962)
Understanding *how* your product spreads through the market determines your release and feature strategy.

```
Innovators   Early       Early        Late         Laggards
  2.5%      Adopters    Majority     Majority       16%
            13.5%        34%          34%
    |_________|___________|____________|______________|
              ^           ^
           Target       "The Chasm"
           for MVP      (Geoffrey Moore)
```

**Adopter Segments:**
| Segment | Mindset | What they need from you |
|---|---|---|
| **Innovators** | Risk-tolerant, tech-first | Access, raw capability |
| **Early Adopters** | Vision-driven, influential | Reference story, competitive edge |
| **Early Majority** | Pragmatic, wait-and-see | Proven ROI, whole product |
| **Late Majority** | Skeptical, price-sensitive | Standards, support, herd behavior |
| **Laggards** | Tradition-bound | Forced adoption or irrelevance |

**The Chasm** (Moore): Gap between Early Adopters and Early Majority is where most products die. Early Adopters accept rough edges; Early Majority demands a **complete solution**.

**Strategic Implications:**
- **MVP → target Early Adopters** first. They tolerate incomplete products if the core Job is solved.
- **Cross the Chasm** by dominating one niche vertical completely (beachhead strategy) before expanding.
- **Feature flags + phased Release** align directly with the adoption curve: Innovators → Early Adopters → controlled rollout to Majority.
- Do not build for Late Majority features until Early Majority is retained.
- For active release tracking and Go/No-Go decisions per rollout phase, use the `diffusion-release-tracking` skill.

---

## 2. Product Metrics & Analytics

### North Star Metric (NSM)
The single metric that best captures the core value your product delivers to customers.

**Characteristics of a good NSM:**
- Measures customer value (not revenue or growth)
- Reflects the JTBD core outcome
- Leading indicator of sustainable growth
- Actionable — teams can influence it

**Examples:**
| Product | North Star Metric | Why |
|---|---|---|
| Airbnb | Nights booked | Core value: finding a place to stay |
| Spotify | Time spent listening | Core value: music enjoyment |
| Slack | Messages sent | Core value: team communication |
| Notion | Weekly active docs | Core value: organized work |

**Input Metrics → NSM:**
```
Input: Sign-up rate, activation rate, feature adoption
        ↓
NSM:   Weekly Active Users (WAU)
        ↓
Output: Revenue, retention, LTV
```

### The Product Metrics Hierarchy

```
Level 1: Business Outcome (lagging)
  - Revenue, LTV, CAC, Market Share

Level 2: Product Health (leading)
  - Retention (Day-1, Day-7, Day-30)
  - Engagement (DAU/MAU ratio, session frequency)
  - Activation (% completing key action)

Level 3: Feature Performance (actionable)
  - Feature adoption rate
  - Feature retention (users returning to feature)
  - Time-to-value (time from sign-up to first success)
```

### Cohort Analysis

Track groups of users who started at the same time to understand retention patterns.

```
Cohort Retention Table:

Sign-up    Week 0   Week 1   Week 2   Week 3   Week 4
2026-01    100%     45%      38%      35%      33%
2026-02    100%     48%      40%      36%      —
2026-03    100%     50%      —        —        —
```

**Key signals:**
- Flattening retention curve = product-market fit signal
- Declining retention over cohorts = product degrading or market shifting
- Retention < 20% at Week 4 = serious PMF problem

### Funnel Analysis

Map the user journey and identify drop-off points.

```
Funnel: Sign-up → Onboarding → First Value → Retention → Revenue

Example:
Sign-up:        1000 users (100%)
Onboarding:      700 users (70%)  ← Drop-off: 30% — onboarding too long?
First Value:     350 users (35%)  ← Drop-off: 50% — value not clear?
Day-7 Return:    175 users (17.5%) ← Drop-off: 50% — not sticky enough?
Paid Convert:     35 users (3.5%)
```

**Action:** Focus on the biggest drop-off first. A 10% improvement at the biggest bottleneck beats a 50% improvement at a small one.

---

## 3. A/B Testing & Experimentation

### Experiment Design Framework

```
1. Hypothesis: "We believe [change] will [impact] because [reason]"
   Example: "We believe simplifying onboarding from 5 to 3 steps will increase
   activation by 15% because users drop off most at step 4."

2. Primary Metric: The one metric that determines success/failure
3. Secondary Metrics: Guardrails (e.g., don't hurt retention while improving activation)
4. Sample Size: Calculate before running
5. Duration: Run for full business cycles (min 1 week, typically 2)
```

### Sample Size Calculation

```python
# Using statsmodels
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Example: Baseline conversion = 20%, want to detect +3% (to 23%)
baseline = 0.20
mde = 0.03  # Minimum Detectable Effect
alpha = 0.05
power = 0.80

effect_size = proportion_effectsize(baseline + mde, baseline)
analysis = NormalIndPower()
sample_size = analysis.solve_power(
    effect_size=effect_size,
    alpha=alpha,
    power=power,
    ratio=1
)
# Result: ~3,500 users per variant
```

**Rule of thumb:**
| Baseline | MDE | Sample per variant |
|---|---|---|
| 10% | +2% | ~7,000 |
| 20% | +3% | ~3,500 |
| 30% | +5% | ~1,800 |

### Statistical Significance

```python
from scipy import stats

# Two-proportion z-test
control = [1000, 200]      # 1000 visitors, 200 conversions
variant = [1000, 250]      # 1000 visitors, 250 conversions

z_stat, p_value = stats.proportions_ztest(
    [control[1], variant[1]],
    [control[0], variant[0]]
)

# p < 0.05 → statistically significant
# But also check practical significance: is +2.5% conversion worth the effort?
```

### Early Stopping & Peeking

**DON'T peek at results and stop early.** This inflates false positive rate dramatically.

**Solutions:**
- Set a fixed duration before starting (e.g., 2 weeks)
- Use sequential testing if you must peek (more complex, requires larger sample)
- Accept that some experiments will run longer than hoped

### Experiment Checklist

- [ ] Hypothesis is specific and falsifiable
- [ ] Primary metric defined before launch
- [ ] Sample size calculated
- [ ] Duration set (minimum 1 full business cycle)
- [ ] Randomization is truly random (check for bias)
- [ ] No other changes during experiment period
- [ ] Results analyzed with both statistical AND practical significance

---

## 4. Pricing & Monetization

### Pricing Strategy Framework

**1. Cost-Plus Pricing** ❌ (Don't use)
- Price = Cost + Margin
- Problem: ignores customer value, leaves money on table

**2. Competitor-Based Pricing** ⚠️ (Use as reference only)
- Price relative to competitors
- Problem: race to the bottom, commoditizes your product

**3. Value-Based Pricing** ✅ (Recommended)
- Price based on value delivered to customer
- Calculate: How much money/time does your product save/create?

```
Value-Based Pricing Calculation:

Customer's current cost of problem: $10,000/year (manual process)
Your product saves: 80% of that time = $8,000/year value
Price at 20-30% of value captured: $1,600 - $2,400/year
```

### Pricing Tiers

```
Freemium Structure:

Free:        Core JTBD, limited usage, basic support
  ↓  (convert ~2-5%)
Pro:         Unlimited usage, advanced features, priority support
  ↓  (convert ~10-20% of paid)
Enterprise:  Custom features, SLA, dedicated support, SSO
```

**Freemium rules:**
- Free tier must deliver core JTBD (otherwise users won't experience value)
- Limit by usage (not features) — users hit a natural ceiling
- Conversion trigger: when free user hits a pain point that Pro solves

### Unit Economics

```
LTV = Average Revenue Per User × Gross Margin × Average Customer Lifetime

CAC = Total Sales & Marketing Cost / Number of New Customers

LTV:CAC Ratio:
  < 1:1   → Unsustainable, losing money on every customer
  1:1-3:1 → Surviving but not thriving
  3:1-5:1 → Healthy SaaS business
  > 5:1   → Under-investing in growth

Payback Period: How many months to recover CAC
  < 12 months → Excellent
  12-18 months → Good
  > 18 months → Risky
```

---

## 5. User Research Deep Dive

### User Personas

```markdown
## Persona: "Busy Manager Maria"

**Demographics:**
- Role: Engineering Manager at mid-size tech company
- Age: 32, Urban, $120K+ income

**Goals:**
- Keep team productive without micromanaging
- Have visibility into blockers before they escalate

**Pains:**
- Status updates take 2+ hours/week to compile
- Team members don't proactively flag blockers
- Current tools are too complex for quick check-ins

**Behaviors:**
- Checks Slack on phone during commute
- Prefers async communication over meetings
- Uses 5+ tools daily (Jira, Slack, Calendar, Email, Docs)

**JTBD:** "When I'm planning the week, I want to see team blockers at a glance,
so I can remove obstacles before they derail sprint goals."
```

### Journey Mapping

```
Stage:          Awareness → Consideration → Onboarding → First Value → Regular Use → Advocacy
User Action:    Sees ad   → Reads blog   → Signs up   → Completes   → Uses daily  → Refers
                                                              onboarding   core feature
Emotion:        Curious   → Skeptical    → Excited    → Confused    → Satisfied   → Enthusiastic
Pain Point:     —         → "Is this     → Form too   → Can't find  → Missing     → No referral
                            different?"    long        core feature   feature X     incentive
Opportunity:    —         → Case study   → Social     → Interactive → Feature     → Referral
                            with ROI       login       tutorial       request       program
```

### Usability Testing Protocol

```
1. Recruit 5 users (Nielsen: 5 users find 85% of issues)
2. Give them a task, not instructions
   ❌ "Click the blue button, then select 'Create'"
   ✅ "Create a new project and invite your teammate"
3. Think-aloud protocol: "Please say what you're thinking as you go"
4. Observe, don't help (painful but necessary)
5. Measure: task success rate, time-on-task, error rate, satisfaction (SUS score)
```

---

## 6. Go-to-Market (GTM) Strategy

### Positioning Statement

```
For [target customer]
Who [statement of need or opportunity]
Our product is a [product category]
That [key benefit / compelling reason to buy]
Unlike [primary competitive alternative]
Our product [primary differentiation]
```

**Example:**
```
For engineering managers at growing startups
Who struggle to keep teams aligned without constant meetings
Our product is a daily async status tool
That surfaces blockers and wins in 2 minutes a day
Unlike daily standup meetings or complex project management tools
Our product respects everyone's time while maintaining full visibility
```

### Launch Playbook

```
Pre-Launch (4 weeks before):
  □ Beta cohort of 20-50 users actively using
  □ Case study with quantified ROI ready
  ░ Landing page with clear JTBD messaging
  □ Pricing page finalized
  □ Support docs and FAQ ready
  □ Onboarding flow tested with 5+ users

Launch Week:
  □ Product Hunt / Hacker News launch
  □ Email to waitlist
  □ Social media announcement
  □ Founder/team personal outreach to 20 key users
  □ Monitor metrics dashboard hourly

Post-Launch (2-4 weeks):
  □ Gather feedback from first 100 users
  □ Fix critical bugs within 24 hours
  □ Publish first case study
  □ Iterate on onboarding based on drop-off data
```

---

## 7. Product-Market Fit Measurement

### Sean Ellis Test

Ask users: **"How would you feel if you could no longer use this product?"**

| Response | % of Users |
|---|---|
| Very disappointed | — |
| Somewhat disappointed | — |
| Not disappointed | — |
| N/A — I no longer use it | — |

**PMF threshold: ≥ 40% "Very disappointed"**

**If < 40%:**
- Segment by user type — which segment is > 40%?
- Double down on that segment (beachhead)
- Ignore users who don't fit that segment for now

### Retention Curve Test

Plot % of users returning over time:

```
Retention %
    100% |\
         |  \
     50% |    \_______     ← Flattening = PMF signal
         |            \____
     20% |                 \_______  ← Still declining = no PMF
         |
      0% +----+----+----+----+----+→ Time (weeks)
         W1   W2   W3   W4   W8   W12
```

**PMF signal:** Curve flattens to a horizontal asymptote (users who stay, stay forever).
**No PMF:** Curve keeps declining toward zero.

### Superhuman PMF Survey

For B2B products, measure across 4 dimensions:

```
1. How disappointed would you be if this product no longer existed?
   (Very / Somewhat / Not disappointed)

2. What type of people do you think would most benefit from [product]?
   (Open-ended — use for persona refinement)

3. What is the main benefit you receive from [product]?
   (Open-ended — use for messaging)

4. How can we improve [product] for you?
   (Open-ended — use for roadmap)
```

**Analyze:** Group "Very disappointed" users by their answer to Q2 → that's your beachhead segment.

---

## 🏗 8. Product Architecture (DDD Integration)

Connect your business findings to technical design using **Domain-Driven Design (DDD)**.
- **Core Domain:** Map the core *Job-To-Be-Done* directly to your DDD **Core Domain**. This is where you invest the most engineering effort.
- **Generic Subdomains:** If a feature doesn't directly serve the unique JTBD (e.g., User Authentication), treat it as a Generic Subdomain. **Buy or use SaaS; do not build from scratch.**
- **Event Storming:** Use the JTBD outcomes to define the key **Domain Events** in your system.

---

## 🚀 9. Agile Delivery: Ship != Release

To achieve a fast time-to-market (MVP) and reduce risk, strictly separate technical deployment from business launch.

### "Ship" (Technical Action)
- Pushing code to the production environment.
- Code is hidden behind **Feature Flags** or available only to internal testers (Dark Launching).
- *Goal: Continuous Integration without business risk.*

### "Release" (Business Action)
- Turning on the Feature Flag for actual users.
- Can be phased (Canary release: 5% of users -> 20% -> 100%).
- Tied to marketing campaigns and business readiness.
- *Goal: Deliver value when the market is ready.*

---

## 🧠 10. Grounded Reasoning: NotebookLM Integration

To ensure technical execution stays aligned with high-level strategy, follow a **Grounded Reasoning** approach when working alongside [NotebookLM](https://notebooklm.google.com/).

### Workflow
1. **Context Request:** Before major technical decisions, prompt the user: *"Please provide the latest strategic context or JTBD summary from your NotebookLM for this feature."*
2. **Synthesis:** User provides context (via copy-paste or summary).
3. **Validation:** Evaluate the current C4/DDD design against the provided business evidence.

### Rule
**MANDATORY:** Always prioritize business constraints and Jobs provided by the user from their research notebooks over generic assumptions. If a technical design conflicts with the user's provided strategy, flag it as a **Strategic Risk**.

---

## 🎯 The MVP Playbook
1. Define the primary **JTBD**.
2. Identify the **Core Domain** required to solve that JTBD.
3. Design the architecture using **C4 Level 1 & 2**, mocking or buying Generic Subdomains.
4. **Ship** the core feature behind a flag.
5. **Release** to a small Early Adopter cohort to validate the market hypothesis and gather adoption signal before crossing the Chasm.

---

## Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| JTBD definition | `why-strategic-rationale` | WHY Statement feeds into JTBD |
| Problem validation | `problem-discovery` | Multi-signal framework |
| Release gates | `diffusion-release-tracking` | Go/No-Go per Rogers gate |
| Delivery speed | `dora-core` | Deployment Frequency prerequisite |
| Architecture mapping | `ddd-core` + `c4-model` | Bounded Contexts + C4 diagrams |
| A/B testing stats | `product-analytics` | Detailed experiment design |
| UX research | `product-ux-research` | Usability testing, personas |
| Code delivery | `collaborative-engineering-agent` | Atomic PRs, feature flags |
