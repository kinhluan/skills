---
name: business-product-leadership
description: Strategic frameworks for Product/Business Owners. Use this skill for Labor Market Research (LMR), defining Jobs-To-Be-Done (JTBD), planning MVPs, and separating deployment (Ship) from business launch (Release).
metadata:
  tags: ["product-management", "business-strategy", "jtbd", "mvp", "agile-delivery"]
---

# Business & Product Leadership

This skill bridges the gap between Business Strategy and Technical Execution. It is designed for Product Owners and Founders who manage both the business viability and the product delivery.

## 📈 1. Business Strategy & Discovery

### Labor Market Research (LMR) & Market Fit
Before building anything, validate the market demand.
- **Identify the Gap:** What specific skills or solutions are currently under-supplied in the market?
- **Competitor Analysis:** Who else is solving this problem? How can we differentiate (Price, Speed, Quality)?
- **Target Audience:** Who is the exact buyer, and what is their budget?

### Jobs-To-Be-Done (JTBD) Framework
People don't buy products; they "hire" them to get a job done.
- **The JTBD Statement:** *"When [Situation], I want to [Motivation], so I can [Expected Outcome]."*
- **Example:** *"When I am commuting, I want to listen to educational content easily, so I can feel productive."*
- **Focus:** Build features that directly solve the core *Job*, not just what users *say* they want.

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
5. **Release** to a small cohort to validate the LMR hypothesis.
