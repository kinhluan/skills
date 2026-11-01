# GitHub Labeling Standards (Consolidated Pattern)

Use these labels to categorize Issues and Pull Requests for better filtering and project management.

## 🏆 Milestones (Release Targets)
*   Format: `[vX.X]` or `[Sprint Name]`
*   Style: Dull, neutral colors to avoid distraction.

## 🏃 Status (Actionable)
*   `status:WIP`: Work in progress.
*   `status:needs-review`: Waiting for initial review.
*   `status:in-review`: Currently being reviewed.
*   `status:fixing`: Feedback received, currently applying fixes.
*   `status:done`: Merged and verified.
*   `status:blocked`: Task is waiting on another task or external dependency.

## 🏷 Type (Indicator)
*   `type:feature`: New functionality.
*   `type:bug`: Error or unexpected behavior.
*   `type:security`: Security vulnerability or audit.
*   `type:refactor`: Code restructuring without behavior change.
*   `type:infrastructure`: CI/CD, Docker, Kubernetes, etc.
*   `type:breaking-change`: Updates that break compatibility.
*   `type:docs`: Documentation updates.

## 🚀 Management (Deployment Status)
*   `env:staging`: Code has been deployed to the staging environment.
*   `env:production`: Code is live in production.
*   `env:qa-needed`: Quality Assurance review is required.

## ⚖️ Priority (Management)
*   `priority:high`: Immediate attention required.
*   `priority:medium`: Standard task.
*   `priority:low`: Non-urgent.

## 🧩 Context
*   `context:frontend`: UI/UX related.
*   `context:backend`: Server/Database related.
*   `context:api`: Interface/Protocol related.
*   `context:core`: Fundamental logic.
