---
name: business-product-leadership
description: Strategic frameworks for Product/Business Owners. Use this skill for Product Market Research, defining Jobs-To-Be-Done (JTBD), understanding Diffusion of Innovations, planning MVPs, and separating deployment (Ship) from business launch (Release).
metadata:
  tags: ["product-management", "business-strategy", "jtbd", "mvp", "agile-delivery", "diffusion-of-innovations"]
---

# Business & Product Leadership

This skill bridges the gap between Business Strategy and Technical Execution. It is designed for Product Owners and Founders who manage both the business viability and the product delivery.

## 📈 1. Business Strategy & Discovery

### Product Market Research & Market Fit
Before building anything, validate market demand for the *product* you intend to create.
- **Identify the Problem:** What specific pain point or unmet need does your product solve?
- **Competitor Analysis:** Who else is solving this problem? How can you differentiate (Price, Speed, Quality, UX)?
- **Target Segment:** Who is your ideal early user, and what triggers them to seek a solution?
- **Validation Methods:** Customer interviews, landing page tests, smoke tests — validate *demand* before writing production code.

### Jobs-To-Be-Done (JTBD) Framework
People don't buy products; they "hire" them to get a job done.
- **The JTBD Statement:** *"When [Situation], I want to [Motivation], so I can [Expected Outcome]."*
- **Example:** *"When I am commuting, I want to listen to educational content easily, so I can feel productive."*
- **Focus:** Build features that directly solve the core *Job*, not just what users *say* they want.

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

## 🏗 2. Product Architecture (DDD Integration)

Connect your business findings to technical design using **Domain-Driven Design (DDD)**.
- **Core Domain:** Map the core *Job-To-Be-Done* directly to your DDD **Core Domain**. This is where you invest the most engineering effort.
- **Generic Subdomains:** If a feature doesn't directly serve the unique JTBD (e.g., User Authentication), treat it as a Generic Subdomain. **Buy or use SaaS; do not build from scratch.**
- **Event Storming:** Use the JTBD outcomes to define the key **Domain Events** in your system.

## 🚀 3. Agile Delivery: Ship != Release

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

## 🎯 The MVP Playbook
1. Define the primary **JTBD**.
2. Identify the **Core Domain** required to solve that JTBD.
3. Design the architecture using **C4 Level 1 & 2**, mocking or buying Generic Subdomains.
4. **Ship** the core feature behind a flag.
5. **Release** to a small Early Adopter cohort to validate the market hypothesis and gather adoption signal before crossing the Chasm.
