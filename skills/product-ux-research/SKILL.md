---
name: product-ux-research
description: User research methods for product teams. Use for creating personas, journey mapping, usability testing, card sorting, and heuristic evaluation to build user-centered products.
metadata:
  tags: ["ux-research", "user-research", "usability", "persona", "journey-mapping", "testing"]
---

# Product UX Research

User-centered research methods to understand needs, validate designs, and measure usability.

> "Design is not just what it looks like and feels like. Design is how it works." — Steve Jobs

---

## 1. User Personas

### Persona Template

```markdown
## Persona: [Name] — [Role/Identity]

### Demographics
- Age, location, income, education
- Job title, company size, industry

### Goals
- What are they trying to achieve?
- What does success look like for them?

### Pains & Frustrations
- What blocks them from achieving goals?
- What workarounds do they currently use?

### Behaviors
- Daily routines related to the problem
- Tools they currently use
- How they make decisions

### JTBD
"When [situation], I want to [motivation], so I can [expected outcome]."

### Quote
"[Direct quote from interview that captures their mindset]"
```

### Persona Creation Process

```
1. Interview 8-12 target users
2. Identify patterns in goals, pains, behaviors
3. Group into 2-4 persona archetypes
4. Validate with quantitative data (survey)
5. Share with team and keep visible
```

**Rules:**
- Base on real data, not assumptions
- Focus on behaviors and goals, not demographics
- Keep to 2-4 personas (more = confusion)
- Update every 6-12 months

---

## 2. Journey Mapping

### Journey Map Template

```
Stage:       Awareness → Consideration → Onboarding → First Value → Regular Use → Advocacy
            ─────────────────────────────────────────────────────────────────────────────
User Action: Sees ad   → Reads reviews → Signs up   → Completes   → Uses core   → Refers
                                                  onboarding    feature       friend

Emotion:     😐 Curious → 😕 Skeptical → 😃 Excited → 😰 Confused → 😊 Satisfied → 🤩 Enthusiastic

Touchpoint:  Social    → Landing page → Email      → In-app      → Dashboard   → Share modal
             media       → Blog post    confirm      tutorial

Pain Point:  —         → "Is this     → Form too   → Can't find  → Missing     → No incentive
                            different?"  long         key feature   feature X

Opportunity: —         → Case study   → Social     → Interactive → Feature     → Referral
                            with ROI     login        guide         request       rewards
```

### Journey Map Analysis

**Identify:**
- **Peak moments:** Highest emotion → double down on these
- **Pain points:** Lowest emotion → prioritize fixing
- **Gaps:** Missing touchpoints → add communication
- **Handoffs:** Where user moves between channels → ensure continuity

---

## 3. Usability Testing

### Moderated Usability Test

```
Protocol:
1. Recruit 5 users (Nielsen: 5 finds 85% of issues)
2. Give tasks, not instructions
   ❌ "Click the blue button, then select Create"
   ✅ "Create a new project and invite your teammate"
3. Think-aloud: "Please say what you're thinking as you go"
4. Observe without helping (painful but necessary)
5. Measure: success rate, time-on-task, errors, SUS score
```

### System Usability Scale (SUS)

```
Rate 1-5 (Strongly Disagree → Strongly Agree):

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

Scoring:
- Odd items (1,3,5,7,9): score - 1
- Even items (2,4,6,8,10): 5 - score
- Total × 2.5 = SUS score (0-100)

Interpretation:
  > 80: Excellent
  70-80: Good
  50-70: OK (needs improvement)
  < 50: Poor
```

### Unmoderated Remote Testing

```
Tools: UserTesting.com, Maze, Lookback

Setup:
1. Define 3-5 tasks
2. Write scenario context ("Imagine you need to...")
3. Set success criteria for each task
4. Recruit 10-15 participants matching persona
5. Review recordings + heatmaps

Best for: Quick feedback, broad geographic reach
Limitation: Can't ask follow-up questions
```

### Usability Test Report

```markdown
## Usability Test: [Feature Name]
**Date:** YYYY-MM-DD
**Participants:** N=5
**Method:** Moderated, think-aloud

### Tasks & Results
| Task | Success Rate | Avg Time | Errors | Severity |
|------|-------------|----------|--------|----------|
| Create account | 5/5 (100%) | 2:30 | 0 | — |
| Set up project | 3/5 (60%) | 5:45 | 4 | High |
| Invite teammate | 4/5 (80%) | 1:20 | 1 | Low |

### Critical Issues (Fix Before Release)
1. **Project setup confusing** — 2 users couldn't find "Create Project" button
   → Make CTA more prominent, add empty state prompt

2. **Invite flow broken on mobile** — Users couldn't access invite modal
   → Fix responsive layout

### SUS Score: 72 (Good)

### Recommendations
- Fix critical issues before release
- Run follow-up test after fixes
```

---

## 4. Card Sorting

### Open Card Sort

```
Goal: Understand how users mentally organize information

Method:
1. Create 30-50 cards with content labels
   (features, topics, product categories)
2. Ask users to group cards into categories that make sense to them
3. Let users name their own categories
4. Analyze patterns across participants

Analysis:
- Dendrogram: Shows which cards are commonly grouped
- Similarity matrix: Heatmap of card pairings
- Category names: Most common labels users chose
```

### Closed Card Sort

```
Goal: Validate an existing information architecture

Method:
1. Pre-define categories (e.g., navigation menu items)
2. Ask users to place cards into these categories
3. Measure: % of cards placed in "expected" category

Analysis:
- Placement matrix: Where each card was placed
- Confusion: Cards placed across many categories
- Consensus: Cards consistently placed in one category
```

**Tools:** Optimal Workshop, UserZoom, Maze, physical cards

---

## 5. Tree Testing

```
Goal: Test information architecture without visual design

Method:
1. Create text-only tree of your site/app structure
2. Give users tasks: "Where would you find X?"
3. Users navigate the tree to find the answer
4. Measure: success rate, time, directness

Metrics:
- Success rate: % finding correct location
- Directness: % going straight to answer (no backtracking)
- Time: How long to find

Example:
Task: "Where would you update your payment method?"
Tree:
  Account
    ├── Profile
    ├── Settings
    │   ├── Notifications
    │   └── Billing ← Correct
    └── Security

Result: 70% found it, 40% direct path
Issue: 30% looked under Profile first
Fix: Add "Payment" link in Profile or rename Billing
```

---

## 6. Diary Studies

```
Goal: Understand user behavior over time

Method:
1. Recruit 8-12 participants
2. Ask them to complete tasks/record experiences daily for 1-2 weeks
3. Prompt with specific questions each day
4. Collect: photos, screen recordings, written responses

Best for:
- Habits and routines
- Long-term product usage
- Emotional responses over time
- Real-world context (not lab)

Analysis:
- Timeline of experiences
- Emotional journey
- Pain point frequency
- Feature usage patterns
```

---

## 7. Heuristic Evaluation

### Nielsen's 10 Usability Heuristics

```
1. Visibility of System Status
   → Keep users informed (progress bars, loading states)

2. Match Between System and Real World
   → Use familiar language and concepts

3. User Control and Freedom
   → Support undo, escape hatches, confirmations

4. Consistency and Standards
   → Same words/actions mean same things everywhere

5. Error Prevention
   → Design to prevent mistakes, not just recover from them

6. Recognition Rather Than Recall
   → Show options, don't make users remember

7. Flexibility and Efficiency of Use
   → Accelerators for experts, guidance for novices

8. Aesthetic and Minimalist Design
   → No irrelevant information

9. Help Users Recognize, Diagnose, and Recover from Errors
   → Clear error messages with solutions

10. Help and Documentation
    → Easy to search, focused on tasks, concrete steps
```

### Evaluation Process

```
1. Assemble 3-5 evaluators (mix of UX experts and domain experts)
2. Each evaluator independently reviews interface against heuristics
3. Record: heuristic violated, severity (0-4), location, recommendation
4. Aggregate findings across evaluators
5. Prioritize by severity and frequency

Severity Scale:
0 = Not a usability problem
1 = Cosmetic (fix if time)
2 = Minor (low priority)
3 = Major (high priority, fix before release)
4 = Catastrophic (must fix immediately)
```

---

## 8. Research Method Selection

| Question | Method | Sample Size | Timeline |
|---|---|---|---|
| Who are our users? | Persona research | 8-12 interviews | 2-3 weeks |
| How do users currently solve this? | Contextual inquiry | 5-8 observations | 1-2 weeks |
| Can users complete core tasks? | Usability testing | 5 users | 3-5 days |
| How do users organize information? | Card sorting | 15-20 users | 1 week |
| Can users find things in our IA? | Tree testing | 30-50 users | 3-5 days |
| What do users think over time? | Diary study | 8-12 users | 2-4 weeks |
| What usability issues exist? | Heuristic evaluation | 3-5 experts | 2-3 days |
| Which design is better? | A/B testing | Calculated | 1-2 weeks |

---

## 9. Research Ops

### Research Repository

```markdown
# Research Repository

## Personas
- [Busy Manager Maria](personas/maria.md)
- [Startup Founder Frank](personas/frank.md)

## Studies
| Date | Method | Topic | Key Finding | Link |
|------|--------|-------|-------------|------|
| 2026-05 | Usability test | Onboarding v2 | 60% success, SUS 72 | [Report](studies/onboarding-may.md) |
| 2026-04 | Card sort | Navigation IA | Users grouped Pricing under Account | [Report](studies/navigation-apr.md) |

## Insights
- [Onboarding confusion](insights/onboarding.md): Users miss "Create Project" CTA
- [Mobile invite broken](insights/mobile-invite.md): Modal not accessible on small screens

## Raw Data
- [Interview transcripts](raw/interviews/)
- [Usability recordings](raw/usability/)
```

### Research Cadence

```
Continuous (weekly):
- Usability tests (2-3 users/week)
- Support ticket analysis
- Analytics review

Quarterly:
- Persona validation (survey)
- Journey map update
- Competitive UX audit

Annually:
- Full persona refresh
- Comprehensive IA review
- Strategic user research (new markets)
```

---

## Integration with Other Skills

| This skill provides | Related skill | For deeper dive |
|---|---|---|
| User insights | `business-product-leadership` | JTBD definition, MVP scope |
| Usability validation | `product-analytics` | Quantify UX impact |
| Persona creation | `problem-discovery` | Interview protocols |
| Design validation | `c4-level3-component` | Component usability |
| Research synthesis | `second-brain-reflection` | Compress insights into rules |
