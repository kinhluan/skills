---
name: security-analysis
description: Security vulnerability analysis and auditing procedures
metadata:
  tags: ["security", "sast", "vulnerability", "audit", "owasp"]
---

# Security Analysis

Procedures for security vulnerability analysis and code auditing.

## When to Use

- Reviewing code for security vulnerabilities
- Conducting security audits
- Implementing security best practices

## Core Principles

1. **Assume All External Input is Malicious** - Validate and sanitize all user input
2. **Principle of Least Privilege** - Only grant necessary permissions
3. **Fail Securely** - Never expose sensitive information in errors

## Vulnerability Categories

### Injection (OWASP A03)

**Look for:**
- SQL queries with string concatenation
- Shell commands with user input
- Template injection vulnerabilities

```python
# VULNERABLE
query = f"SELECT * FROM users WHERE id = {user_id}"

# SECURE
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))
```

### Broken Authentication (OWASP A07)

**Check for:**
- Weak session token generation
- Missing rate limiting on auth endpoints
- Insecure password reset flows

### Sensitive Data Exposure (OWASP A02)

**Check for:**
- Hardcoded secrets in code
- PII in logs
- Unencrypted sensitive data storage

```python
# VULNERABLE - PII in logs
logger.info(f"Processing payment for {user_email}: ${amount}")

# SECURE
logger.info(f"Processing payment for user_id={user_id}: ${amount}")
```

### Security Misconfiguration (OWASP A05)

**Check for:**
- Debug mode enabled in production
- Verbose error messages
- Unnecessary services/ports exposed

## Analysis Procedure

1. **Identify Privacy Sources** - User input, API parameters, files
2. **Trace to Privacy Sinks** - Logs, external APIs, responses
3. **Check for Sanitization** - Validation, encoding, parameterization
4. **Assess Severity** - Critical, High, Medium, Low

## Severity Levels

| Level | Impact | Example |
|-------|--------|---------|
| Critical | RCE, full compromise | SQL injection with RCE |
| High | Data breach, auth bypass | IDOR on sensitive data |
| Medium | Limited data access | Reflected XSS |
| Low | Minor info disclosure | Verbose errors |

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
