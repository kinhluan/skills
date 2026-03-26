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

... (unchanged) ...

## 🧠 4. Grounded Reasoning: NotebookLM Integration

To ensure technical execution stays aligned with high-level strategy, this skill follows a **Grounded Reasoning** approach when working alongside [NotebookLM](https://notebooklm.google.com/).

### Workflow with NotebookLM
1.  **Context Request:** Before major technical decisions, the AI should prompt the user: *"Please provide the latest strategic context or JTBD summary from your NotebookLM for this feature."*
2.  **Synthesis:** The user provides the context (via copy-paste or summary).
3.  **Validation:** The AI evaluates the current C4/DDD design against this provided business evidence.

### Integration Rule
**MANDATORY:** Always prioritize the business constraints and "Jobs" provided by the user from their research notebooks over generic assumptions. If a technical design conflicts with the user's provided strategy, flag it as a **Strategic Risk**.
