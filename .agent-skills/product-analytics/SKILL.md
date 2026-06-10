---
name: product-analytics
description: Product analytics and experimentation frameworks. Use for defining metrics, designing A/B tests, analyzing funnels and cohorts, measuring feature impact, and setting up analytics infrastructure.
metadata:
  tags: ["product-analytics", "metrics", "ab-testing", "experimentation", "funnel", "cohort", "statistics"]
---

# Product Analytics

Data-driven product decisions through metrics, experimentation, and behavioral analysis.

> "In God we trust, all others bring data." — W. Edwards Deming

---

## 1. Metrics Framework

### North Star Metric (NSM)

The single metric that best captures the core value your product delivers.

**Characteristics:**
- Measures customer value (not revenue)
- Reflects the core JTBD outcome
- Leading indicator of sustainable growth
- Actionable by product teams

**Examples:**
| Product | NSM | Why |
|---|---|---|
| Airbnb | Nights booked | Core value exchange |
| Spotify | Time spent listening | Content engagement |
| Slack | Messages sent | Communication value |
| Notion | Weekly active docs | Organized work |
| Duolingo | Lessons completed | Learning progress |

**Anti-patterns:**
- Revenue as NSM → optimizes for extraction, not value
- Downloads as NSM → optimizes for vanity, not retention
- Page views as NSM → optimizes for engagement, not outcomes

### Input → NSM → Output

```
Input Metrics (leading, actionable)
  ├─ Acquisition: Sign-up rate, activation rate
  ├─ Engagement: Feature adoption, session frequency
  └─ Quality: NPS, support ticket rate
           ↓
    North Star Metric (health indicator)
           ↓
Output Metrics (lagging, business)
  ├─ Revenue: ARR, MRR, LTV
  ├─ Retention: Logo retention, revenue retention
  └─ Efficiency: CAC, payback period
```

### The AARRR Framework (Pirate Metrics)

```
Acquisition  → Activation  → Retention  → Revenue  → Referral
   (A)           (A)          (R)         (R)         (R)

Acquisition: Users find you (SEO, ads, content, viral)
Activation: Users experience core value (first "aha" moment)
Retention: Users come back (Day-1, Day-7, Day-30)
Revenue: Users pay (conversion, expansion, upsell)
Referral: Users invite others (viral coefficient, NPS)
```

**Key ratios:**
- Activation rate: % of sign-ups who reach "aha" moment
- Retention rate: % of activated users who return
- Conversion rate: % of retained users who pay
- Viral coefficient (K): avg referrals per user; K > 1 = exponential growth

---

## 2. Funnel Analysis

### Building a Funnel

```
Step 1: Define the critical path
  "What are the minimum steps a user must take to get value?"

Step 2: Measure conversion at each step
  Step          Users    Conversion    Drop-off
  ─────────────────────────────────────────────
  Landing       10,000   100%          —
  Sign-up        3,000   30%           70% ← Biggest drop
  Onboarding     1,500   50%           50%
  First Value      750   50%           50%
  Day-7 Return   375    50%           50%
  Paid            75     20%           80%
```

**Analysis:**
- Focus on the biggest drop-off first
- A 10% improvement at a 70% drop-off beats a 50% improvement at a 10% drop-off
- Segment funnel by channel, persona, or cohort

### Funnel Segmentation

```
Funnel by Channel:

Channel     Landing  Sign-up  Activation  Retention
─────────────────────────────────────────────────────
Organic       5,000    1,500      750        375
Paid          4,000      800      240         72
Referral      1,000      700      490        343

Insight: Referral has highest quality (49% activation vs 16% paid)
Action: Shift budget from paid to referral program
```

---

## 3. Cohort Analysis

### Cohort Retention Table

```
Cohort Sign-up    Week 0   Week 1   Week 2   Week 3   Week 4   Week 8
─────────────────────────────────────────────────────────────────────
2026-01-01        100%     45%      38%      35%      33%      30%
2026-01-08        100%     48%      41%      37%      35%      —
2026-01-15        100%     50%      43%      39%      —        —
2026-01-22        100%     52%      45%      —        —        —
2026-01-29        100%     55%      —        —        —        —
```

**Signals:**
- **Flattening curve** (horizontal at Week 4+): Product-Market Fit signal
- **Improving cohorts** (each row better than last): Product improving
- **Declining cohorts**: Product degrading or market shifting
- **Benchmarks:**
  - Consumer SaaS: 20-25% Week-4 retention = good, 30%+ = excellent
  - B2B SaaS: 40-50% Week-4 retention = good, 60%+ = excellent
  - Mobile apps: 15-20% Day-30 retention = good

### Cohort Analysis by Feature

```
Cohort that used Feature X vs didn't:

                Week 1   Week 2   Week 4
─────────────────────────────────────────
Used Feature X    60%      55%      50%
Didn't use        35%      25%      15%
Lift              +71%    +120%    +233%

Insight: Feature X is strongly correlated with retention
Action: Prioritize onboarding users to Feature X
```

---

## 4. A/B Testing & Experimentation

### Experiment Design

```
1. Hypothesis
   "We believe [change] will [impact metric] by [amount] because [reason]"

2. Success Criteria
   Primary metric: The one metric that determines go/no-go
   Secondary metrics: Guardrails (don't hurt X while improving Y)
   Guardrail metrics: Must not degrade (e.g., page load time)

3. Randomization
   - Truly random assignment (check for bias post-hoc)
   - Stable (same user always sees same variant)
   - Consistent across devices

4. Duration
   - Minimum: 1 full business cycle (7 days for weekly patterns)
   - Typical: 2 weeks
   - Maximum: Set before starting; don't run indefinitely
```

### Sample Size Calculation

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Baseline conversion and Minimum Detectable Effect
baseline = 0.20      # 20% current conversion
mde = 0.03           # Want to detect +3% (to 23%)
alpha = 0.05         # 5% false positive rate
power = 0.80         # 80% chance of detecting true effect

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

**Quick reference:**
| Baseline | MDE | Sample/variant |
|---|---|---|
| 10% | +2% | ~7,000 |
| 20% | +3% | ~3,500 |
| 30% | +5% | ~1,800 |
| 50% | +5% | ~1,600 |

### Statistical Analysis

```python
from scipy import stats

# Two-proportion z-test
control_visitors = 3500
control_conversions = 700      # 20%
variant_visitors = 3500
variant_conversions = 875      # 25%

z_stat, p_value = stats.proportions_ztest(
    [control_conversions, variant_conversions],
    [control_visitors, variant_visitors]
)

# Confidence interval
lift = (variant_conversions/variant_visitors - control_conversions/control_visitors)
# p < 0.05 AND practical significance → implement
```

**Decision framework:**
| p-value | Practical Significance | Decision |
|---|---|---|
| < 0.05 | Yes (lift > MDE) | ✅ Implement |
| < 0.05 | No (lift < MDE) | ⚠️ Monitor, not implement |
| > 0.05 | Yes | ⚠️ Run longer or accept risk |
| > 0.05 | No | ❌ No effect, don't implement |

### Early Stopping & Peeking

**The Problem:** Peeking at results and stopping when p < 0.05 inflates false positive rate from 5% to ~30%.

**Solutions:**
1. **Fixed duration:** Set end date before starting, don't look until then
2. **Sequential testing:** Use proper sequential boundaries (more complex)
3. **Accept uncertainty:** Some experiments need to run longer

### Experiment Checklist

- [ ] Hypothesis is specific and falsifiable
- [ ] Primary metric defined before launch
- [ ] Sample size calculated and feasible
- [ ] Duration set (min 1 business cycle)
- [ ] Randomization checked for bias
- [ ] No other changes during experiment
- [ ] Results analyzed with both statistical and practical significance
- [ ] Losers are documented (prevents re-testing same idea)

---

## 5. Feature Impact Measurement

### Before/After Analysis

```
Feature Launch Impact:

Metric          Before    After    Δ       Significant?
────────────────────────────────────────────────────────
Activation      25%       28%      +3pp    Yes (p=0.02)
Day-7 Retention  18%       19%      +1pp    No (p=0.18)
Revenue/user    $12       $14      +$2     Yes (p=0.01)

Interpretation: Feature improved activation and revenue but not retention.
Next step: Investigate why retention didn't improve.
```

### Holdout Groups

Reserve a small % of users (5-10%) who never see the new feature:

```
Benefits:
- Measure long-term impact (some features have delayed effects)
- Detect negative interactions between features
- Provide clean baseline for future experiments

Trade-off: Slower to detect impact (smaller sample)
```

### Incrementality Testing

For marketing or growth features, measure true incremental impact:

```
Method: Randomized controlled trial

Group A (90%): See the new growth feature
Group B (10%): Don't see it (control)

Measure: Difference in conversion between A and B

If A converts at 15% and B at 12%:
Incremental lift = 3 percentage points (25% relative)
```

---

## 6. Analytics Infrastructure

### Event Tracking Schema

```json
{
  "event": "purchase_completed",
  "timestamp": "2026-06-10T09:23:15Z",
  "user_id": "usr_12345",
  "session_id": "sess_67890",
  "properties": {
    "product_id": "prod_001",
    "price": 49.99,
    "currency": "USD",
    "payment_method": "credit_card",
    "coupon_applied": false
  },
  "context": {
    "page_url": "/checkout",
    "device": "mobile",
    "os": "iOS 17",
    "referrer": "email_campaign_summer"
  }
}
```

**Required events for every product:**
| Event | When | Properties |
|---|---|---|
| `user_signed_up` | Account creation | channel, referrer, device |
| `user_activated` | First value moment | time_to_activate, feature_used |
| `session_started` | App open / page load | referrer, device, os |
| `feature_used` | Core feature interaction | feature_name, duration |
| `subscription_started` | First payment | plan, amount, coupon |
| `subscription_cancelled` | Churn | reason, tenure, LTV |

### Tool Comparison

| Tool | Best For | Pricing |
|---|---|---|
| **Amplitude** | Product analytics, funnels, cohorts | Free tier generous |
| **Mixpanel** | Event tracking, user journeys | Free tier available |
| **PostHog** | Open-source, self-hosted option | Free + paid cloud |
| **Heap** | Auto-capture (no manual event setup) | Premium pricing |
| **Google Analytics 4** | Web traffic, acquisition | Free |
| **LaunchDarkly** | Feature flags + experimentation | Paid |
| **Statsig** | Full-stack experimentation | Free tier available |

### Dashboard Design

```
Executive Dashboard (weekly review):
┌─────────────────┬─────────────────┬─────────────────┐
│   NSM (WAU)     │   Revenue (MRR) │   Retention D7  │
│     45,200      │    $128,000     │      28%        │
│    ↑ 5% WoW     │    ↑ 8% WoW     │    → flat       │
└─────────────────┴─────────────────┴─────────────────┘
┌─────────────────┬─────────────────┬─────────────────┐
│  Activation     │   Conversion    │   NPS Score     │
│      32%        │      4.2%       │      42         │
│    ↑ 2pp MoM    │    ↑ 0.3pp      │    ↑ 3 pts      │
└─────────────────┴─────────────────┴─────────────────┘

Product Team Dashboard (daily):
- Funnel: Sign-up → Onboarding → Activation (last 7 days)
- Cohort: Week-1 retention by sign-up week
- Experiments: Active experiments + results
- Feature adoption: Top 10 features by usage
```

---

## 7. Common Analytics Pitfalls

| Pitfall | Why It Hurts | Fix |
|---|---|---|
| **Vanity metrics** | Downloads, page views don't correlate with value | Focus on NSM and retention |
| **Survivorship bias** | Only analyzing users who stayed | Include churned users in cohorts |
| **Correlation = causation** | Feature users retain more → feature causes retention? | Run experiments to prove causality |
| **P-hacking** | Testing many metrics until one is significant | Pre-register primary metric |
| **Small sample sizes** | Concluding from 100 users | Calculate sample size upfront |
| **Ignoring seasonality** | Comparing December to January | Use YoY or same-period comparisons |
| **Segment-level effects** | Overall metric flat but segment improving | Always segment by persona/channel |

---

## Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| Metrics definition | `business-product-leadership` | JTBD → NSM mapping |
| Experiment design | `business-product-leadership` | A/B testing framework |
| Funnel/cohort analysis | `business-product-leadership` | Product health measurement |
| Statistical methods | `research-design` | Rigorous experimental protocol |
| Feature flags | `collaborative-engineering-agent` | Ship behind flags |
| Release tracking | `diffusion-release-tracking` | Gate advancement decisions |
| User research | `product-ux-research` | Qualitative insights |
