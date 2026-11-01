---
name: milestone-tracker
description: Track PhD/Master's milestones, deadlines, committee meetings, and research timeline. Use when planning PhD schedule, checking progress, preparing for committee meetings, managing submission deadlines, or when behind on timeline.
metadata:
  tags: ["research", "phd", "milestone", "timeline", "planning", "deadline"]
  version: 1.0.0
  triggers:
    - "PhD milestones"
    - "Track my progress"
    - "Am I on track"
    - "Committee meeting"
    - "Research timeline"
    - "When should I submit"
    - "PhD schedule"
    - "Behind on timeline"
---

# Milestone Tracker

Plan and track your PhD/Master's journey from start to defense.

## Master's Thesis Timeline (2 years)

```
Year 1, Semester 1 (Months 1-6)
├── Month 1-2: Literature review + SOTA survey
├── Month 2-3: Research question formulation
├── Month 3-4: Proposal writing + advisor alignment
├── Month 4:   Proposal defense / committee approval ← GATE 1
├── Month 4-6: Research design + preliminary experiments
└── Month 6:   Progress report to committee

Year 1, Semester 2 (Months 7-12)
├── Month 7-9: Main experiments
├── Month 9-10: Paper writing (conference target)
├── Month 10:  Submit to conference ← GATE 2 (optional)
├── Month 10-12: Refine results, start thesis
└── Month 12:  End-of-year committee review

Year 2, Semester 1 (Months 13-18)
├── Month 13-15: Complete all experiments
├── Month 15-17: Write thesis chapters
├── Month 17:  Submit thesis draft to advisor ← GATE 3
└── Month 18:  Incorporate advisor feedback

Year 2, Semester 2 (Months 19-24)
├── Month 19-21: Revise thesis
├── Month 21:  Submit to committee (4-6 weeks before defense)
├── Month 22:  Defense preparation
├── Month 23:  THESIS DEFENSE ← GATE 4
└── Month 24:  Post-defense corrections + submission
```

## PhD Timeline (3-5 years, CS)

```
Year 1: Coursework + Literature
Year 2: Research design + first paper
Year 3: Main contributions + 2-3 papers
Year 4: Thesis writing + additional papers (if needed)
Year 5: Defense + job market
```

## Current Status Check

When asked "am I on track?", run this assessment:

```markdown
## PhD Progress Check — [Date]

**Program:** [Master's / PhD]
**Start date:** [date]
**Expected end:** [date]
**Current month:** [N of total]

### Milestones Status
| Milestone | Target date | Status | Notes |
|-----------|-------------|--------|-------|
| Proposal approved | Month 4 | ✅/⏳/❌ | |
| First paper submitted | Month 10 | ✅/⏳/❌ | |
| All experiments complete | Month 15 | ✅/⏳/❌ | |
| Thesis draft to advisor | Month 17 | ✅/⏳/❌ | |
| Defense | Month 23 | ✅/⏳/❌ | |

### Current Blockers
1. [What is blocking progress?]
2. ...

### Risk Assessment
- On track / Slightly behind (1-2 months) / Significantly behind (3+ months)
- Mitigation: [specific action]
```

## Publication Deadline Calendar

Build this at start of Year 1:

```markdown
## 2026 Submission Calendar

| Venue | Deadline | Notification | Status |
|-------|----------|--------------|--------|
| ICLR 2027 | Oct 2026 | Jan 2027 | Planning |
| NeurIPS 2026 | May 2026 | Sep 2026 | Target |
| ICML 2026 | Feb 2026 | Jun 2026 | Missed |
```

## Committee Meeting Prep

Before each committee meeting, prepare 1-page update:

```markdown
## Committee Update — [Date]

**Since last meeting ([date]):**
- Completed: [list]
- Submitted/published: [list]

**Current work:**
- [What I'm working on now]

**Results so far:**
- [Key numbers, figures]

**Challenges:**
- [What's hard, where I need guidance]

**Plan until next meeting:**
- [Concrete deliverables with dates]

**Questions for committee:**
1. [Decision needed from them]
2. ...
```

## When Behind Schedule

Red flags and responses:

| Situation | Response |
|-----------|----------|
| No results after 3 months of experiments | Talk to advisor immediately. Pivot or simplify. |
| Paper rejected twice | Assess: is the problem or execution? Consider journal. |
| Writing blocked | Time-box: 2 hours/day, any output. Show advisor weekly. |
| Advisor unavailable | Email with specific questions. Keep paper trail. |
| Lost motivation | Normal. Talk to peers, counselor. Take 1 real week off. |

## Gantt Template

```
Task                    | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | ... 
Literature review       | ██ | ██ |    |    |    |    |    |    |
RQ formulation          |    | ██ | ██ |    |    |    |    |    |
Proposal writing        |    |    | ██ | ██ |    |    |    |    |
Proposal defense        |    |    |    | ◆  |    |    |    |    |
Research design         |    |    |    | ██ | ██ |    |    |    |
Experiments             |    |    |    |    | ██ | ██ | ██ | ██ |
Paper writing           |    |    |    |    |    |    | ██ | ██ |
```

## Links to Other Skills
- Integrates with → all other research skills (timeline for each)
- Feeds into → `defense-prep` (schedules defense prep window)
- Feeds into → `publication-strategy` (tracks submission deadlines)
