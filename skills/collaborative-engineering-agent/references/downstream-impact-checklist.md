# Downstream Impact & API Stability Checklist

Use this checklist to identify potential risks to other services, API consumers, or data integrity before merging.

## 📡 API Contract (Breaking Changes)
- [ ] Have any public API endpoints been modified or deleted?
- [ ] Have required fields in request/response payloads been added/changed?
- [ ] Is there a new version (e.g., `/v2/`) or is the change backward compatible?

## 🗄 Database & Schema (Migrations)
- [ ] Does this change require a database migration?
- [ ] Is the migration "zero-downtime" friendly? (e.g., adding a column is usually safe, dropping one is not).
- [ ] Will large tables be locked during the migration?

## 🔗 Internal Dependencies (Microservices)
- [ ] Do other services consume the output of this component?
- [ ] Does this PR change the format of an event emitted to a message queue (Kafka/RabbitMQ)?
- [ ] Have you checked logs in staging for potential failures in downstream consumers?

## ⚙️ Environment & Configuration
- [ ] Are there new mandatory environment variables required?
- [ ] Does the deployment require a specific order? (e.g., "Migration first, then code").

## 🛡 Security & Permissions
- [ ] Does this change the way users are authenticated or authorized?
- [ ] Have new roles or permissions been added that need to be provisioned in IAM?
