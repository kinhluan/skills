---
name: security-analysis
description: Security vulnerability analysis and auditing procedures. Use this skill for code security reviews, implementing DevSecOps pipelines, OWASP Top 10 mitigation, and secrets management.
metadata:
  tags: ["security", "sast", "dast", "vulnerability", "audit", "owasp", "devsecops"]
---

# Security Analysis

Comprehensive security vulnerability analysis, secure code review, and DevSecOps integration. Covers OWASP Top 10 2021, automated scanning (SAST/DAST/SCA), secrets management, and threat modeling.

> "Security is not a product, but a process." — Bruce Schneier

---

## 🎯 When to Use

- Reviewing code for security vulnerabilities before merge
- Designing secure architecture (threat modeling)
- Implementing DevSecOps CI/CD pipelines
- Conducting security audits or penetration testing preparation
- Responding to security incidents

---

## 🔒 Core Security Principles

| Principle | Meaning | In Practice |
|-----------|---------|-------------|
| **Assume Breach** | Design as if attacker is already inside | Defense in depth, least privilege |
| **Least Privilege** | Minimum permissions necessary | RBAC, service accounts, no root |
| **Fail Securely** | Errors don't expose sensitive data | Generic error messages, no stack traces in prod |
| **Defense in Depth** | Multiple independent controls | WAF + input validation + parameterized queries |
| **Zero Trust** | Never trust, always verify | MFA, mTLS, continuous validation |
| **Shift Left** | Security as early as possible | SAST in IDE, pre-commit hooks |

---

## 🛡️ OWASP Top 10 2021

### A01: Broken Access Control

**What:** Users can access resources they shouldn't.

**Vulnerable Code:**
```python
# VULNERABLE: No authorization check
@app.get("/api/orders/{order_id}")
def get_order(order_id: str):
    return db.query(f"SELECT * FROM orders WHERE id = '{order_id}'")

# VULNERABLE: Client-controlled user ID
@app.get("/api/orders")
def get_orders(user_id: str = Query(...)):  # attacker changes user_id
    return db.query(f"SELECT * FROM orders WHERE user_id = '{user_id}'")
```

**Secure Code:**
```python
from fastapi import Depends, HTTPException

@app.get("/api/orders/{order_id}")
def get_order(
    order_id: str,
    current_user: User = Depends(get_current_user)
):
    order = db.get_order(order_id)
    # Authorize: user can only access their own orders
    if order.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Access denied")
    return order
```

**Checklist:**
- [ ] Deny by default — allowlist, not blocklist
- [ ] Access control enforced server-side, never client-side
- [ ] CORS configured correctly (not `*` in production)
- [ ] Rate limiting on auth endpoints
- [ ] Admin functions on separate route/API

---

### A02: Cryptographic Failures

**What:** Sensitive data exposed due to weak or missing cryptography.

**Vulnerable Code:**
```python
# VULNERABLE: MD5 for passwords
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()

# VULNERABLE: Hardcoded key
SECRET_KEY = "my-secret-key-123"
```

**Secure Code:**
```python
# Python: bcrypt for passwords
import bcrypt

# Hash
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

# Verify
bcrypt.checkpw(password.encode(), password_hash)

# AES-GCM encryption
from cryptography.fernet import Fernet
key = Fernet.generate_key()  # Store in vault, not code!
cipher = Fernet(key)
token = cipher.encrypt(b"sensitive data")
```

```go
// Go: bcrypt + argon2
import "golang.org/x/crypto/bcrypt"

// Hash
hash, _ := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

// Verify
bcrypt.CompareHashAndPassword(hash, []byte(password))
```

**Checklist:**
- [ ] Passwords: bcrypt/argon2/scrypt (NOT MD5/SHA1)
- [ ] Data at rest: AES-256-GCM
- [ ] Data in transit: TLS 1.3 (disable TLS 1.0/1.1)
- [ ] Keys: stored in vault (HashiCorp Vault, AWS KMS, etc.)
- [ ] No hardcoded secrets (use environment variables + vault)

---

### A03: Injection

**What:** Untrusted data sent to interpreter (SQL, NoSQL, OS, LDAP).

**Vulnerable Code:**
```python
# VULNERABLE: SQL Injection
query = f"SELECT * FROM users WHERE id = '{user_id}'"
cursor.execute(query)

# VULNERABLE: Command Injection
import os
os.system(f"convert {user_input} output.png")
```

**Secure Code:**
```python
# SECURE: Parameterized query
query = "SELECT * FROM users WHERE id = %s"
cursor.execute(query, (user_id,))

# SECURE: ORM (Django/SQLAlchemy)
User.objects.filter(id=user_id)  # automatically parameterized

# SECURE: No shell execution
import subprocess
subprocess.run(["convert", user_input, "output.png"], check=True)
# List form prevents shell injection
```

```go
// SECURE: Go database/sql
db.Query("SELECT * FROM users WHERE id = ?", userID)

// SECURE: Go with squirrel query builder
squirrel.Select("*").From("users").Where(squirrel.Eq{"id": userID})
```

**Checklist:**
- [ ] All queries parameterized (prepared statements)
- [ ] ORM used where possible
- [ ] No dynamic table/column names from user input
- [ ] Shell commands avoided; if necessary, use array form
- [ ] Input validation with allowlists

---

### A04: Insecure Design

**What:** Missing or ineffective security controls in design.

**Examples:**
- No rate limiting on password reset
- Business logic flaws (e.g., negative quantity in cart)
- Missing anti-CSRF tokens
- Insecure direct object references (IDOR)

**Secure Design Patterns:**
```python
# Rate limiting
from slowapi import Limiter

limiter = Limiter(key_func=lambda: request.client.host)

@app.post("/login")
@limiter.limit("5/minute")
def login(credentials: LoginRequest):
    ...

# Business logic validation
class OrderItem(BaseModel):
    product_id: str
    quantity: int

    @validator('quantity')
    def quantity_positive(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be positive')
        return v

# Anti-CSRF
def validate_csrf_token(request):
    token = request.headers.get('X-CSRF-Token')
    if not hmac.compare_digest(token, get_expected_token(request)):
        raise HTTPException(403, "Invalid CSRF token")
```

---

### A05: Security Misconfiguration

**What:** Default configs, verbose errors, unnecessary features enabled.

**Common Issues:**
```python
# VULNERABLE: Debug mode in production
app = FastAPI(debug=True)  # Exposes stack traces!

# VULNERABLE: CORS allows everything
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dangerous!
    allow_credentials=True,
)

# VULNERABLE: Verbose error messages
@app.exception_handler(Exception)
def handle_error(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc), "traceback": traceback.format_exc()}  # Leaks internals!
    )
```

**Secure Configuration:**
```python
# Production config
app = FastAPI(debug=False)  # Never True in production

# Restricted CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.example.com"],  # Explicit allowlist
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

# Generic error messages
@app.exception_handler(Exception)
def handle_error(request, exc):
    logger.error(f"Unhandled error: {exc}", exc_info=True)  # Log internally
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "request_id": request.state.request_id}
    )
```

**Security Headers (all responses):**
```python
# Add via middleware or reverse proxy
headers = {
    "Content-Security-Policy": "default-src 'self'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}
```

---

### A06: Vulnerable and Outdated Components

**What:** Using dependencies with known CVEs.

**Detection & Mitigation:**
```bash
# Python
pip install safety
safety check  # Scan requirements.txt

# Node.js
npm audit
npm audit fix

# Go
go list -json -m all | nancy sleuth

# Docker image scanning
trivy image myapp:latest

# GitHub Dependabot (automated)
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
```

---

### A07: Identification and Authentication Failures

**What:** Weak auth mechanisms, session management flaws.

**Secure Implementation:**
```python
# JWT with proper config
from jose import jwt

token = jwt.encode(
    {"sub": user_id, "iat": now, "exp": now + 3600},
    secret_key,
    algorithm="HS256"  # Use RS256 for asymmetric
)

# Session management
@app.post("/logout")
def logout(response: Response):
    response.delete_cookie("session_id")
    invalidate_session(session_id)

# MFA (TOTP)
import pyotp
totp = pyotp.TOTP(user.mfa_secret)
assert totp.verify(code)  # 6-digit code from authenticator app
```

**Checklist:**
- [ ] Strong password policy (NIST 800-63b)
- [ ] MFA enabled for sensitive accounts
- [ ] Session timeout (idle: 15min, absolute: 8h)
- [ ] Secure session cookies (HttpOnly, Secure, SameSite)
- [ ] Account lockout after failed attempts

---

### A08: Software and Data Integrity Failures

**What:** Insecure deserialization, untrusted dependencies, CI/CD tampering.

**Prevention:**
```python
# Never deserialize untrusted data with pickle!
# VULNERABLE:
# data = pickle.loads(untrusted_data)  # RCE!

# SECURE: Use JSON
import json
data = json.loads(untrusted_data)

# Verify software signatures
import gpg
verified = gpg.verify_file(signature_file, data_file)
assert verified.valid

# CI/CD: Signed commits
# Require signed commits in GitHub branch protection
# Use SLSA provenance for build artifacts
```

---

### A09: Security Logging and Monitoring Failures

**What:** Insufficient logging allows attacks to go undetected.

**What to Log:**
```python
# Security events (always log)
- Login attempts (success and failure)
- Privilege escalation
- Data access (sensitive resources)
- Configuration changes
- Authentication failures

# What NOT to log
- Passwords
- API keys
- PII (unless necessary, then masked)
- Session tokens
```

**Structured Logging:**
```python
import structlog

logger = structlog.get_logger()

# Good security log
logger.info(
    "login_attempt",
    user_id=user_id,
    ip_address=request.client.host,
    success=False,
    reason="invalid_password",
    user_agent=request.headers.get("user-agent"),
)

# Alert on anomalies
# - >5 failed logins from same IP in 1 minute
# - Access from unusual geolocation
# - Privilege escalation outside business hours
```

---

### A10: Server-Side Request Forgery (SSRF)

**What:** Server makes requests to attacker-controlled URLs.

**Vulnerable Code:**
```python
# VULNERABLE: User controls URL
url = request.json["webhook_url"]
response = requests.get(url)  # Can access internal services!
```

**Secure Code:**
```python
import urllib.parse

def validate_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    # Block internal IPs, localhost, file://
    blocked_hosts = {"localhost", "127.0.0.1", "0.0.0.0", "::1"}
    if parsed.hostname in blocked_hosts:
        return False
    # Resolve and check IP isn't private
    ip = socket.gethostbyname(parsed.hostname)
    if ipaddress.ip_address(ip).is_private:
        return False
    return parsed.scheme in {"http", "https"}

if not validate_url(url):
    raise HTTPException(400, "Invalid URL")
response = requests.get(url, timeout=5)
```

---

## 🔬 DevSecOps: Automated Security Testing

### SAST (Static Application Security Testing)

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # Python
      - name: Bandit (Python SAST)
        run: |
          pip install bandit
          bandit -r src/ -f json -o bandit-report.json || true

      # JavaScript/TypeScript
      - name: ESLint Security
        run: |
          npm install eslint-plugin-security
          npx eslint . --ext .js,.ts

      # Go
      - name: Gosec (Go SAST)
        run: |
          go install github.com/securego/gosec/v2/cmd/gosec@latest
          gosec ./...

      # Multi-language
      - name: Semgrep
        run: |
          pip install semgrep
          semgrep --config=auto --json --output=semgrep.json src/
```

### DAST (Dynamic Application Security Testing)

```yaml
  dast:
    runs-on: ubuntu-latest
    needs: deploy-staging
    steps:
      - name: OWASP ZAP Scan
        uses: zaproxy/action-full-scan@v0.9.0
        with:
          target: 'https://staging.example.com'
          rules_file_name: '.zap/rules.tsv'
```

### SCA (Software Composition Analysis)

```yaml
  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
```

### Secrets Scanning

```yaml
  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # full history for trufflehog

      - name: TruffleHog
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: main
          head: HEAD
```

---

## 🔐 Secrets Management

### Never Do This
```python
# ❌ HARDCODED SECRETS
API_KEY = "sk-live-abc123"
DATABASE_URL = "postgres://admin:password@db:5432/app"
```

### Do This Instead
```python
# ✅ Environment variables
import os
API_KEY = os.environ["API_KEY"]

# ✅ Secrets manager (AWS)
import boto3
client = boto3.client('secretsmanager')
secret = client.get_secret_value(SecretId="prod/api-key")

# ✅ HashiCorp Vault
import hvac
client = hvac.Client(url='https://vault.example.com')
client.token = os.environ['VAULT_TOKEN']
secret = client.secrets.kv.v2.read_secret_version(path='api-key')

# ✅ Kubernetes secrets
# Mount as file, not env var (prevents /proc exposure)
with open('/var/run/secrets/api-key') as f:
    api_key = f.read().strip()
```

### Pre-commit Hook (prevent secrets in git)
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks:
      - id: detect-private-key

  - repo: https://github.com/Yelp/detect-secrets
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']

  - repo: https://github.com/trufflesecurity/trufflehog
    hooks:
      - id: trufflehog
        args: ["filesystem", "--only-verified", "."]
```

---

## 🎯 Secure Code Review Checklist

### Input Validation
- [ ] All user input validated (type, length, format, range)
- [ ] Allowlist validation preferred over blocklist
- [ ] File uploads: validate type, size, scan for malware
- [ ] URL parameters: no sensitive data exposed

### Authentication & Authorization
- [ ] Auth checks on every protected endpoint
- [ ] Principle of least privilege enforced
- [ ] Session management secure (timeout, invalidation)
- [ ] No sensitive operations without re-authentication

### Data Protection
- [ ] Passwords hashed with bcrypt/argon2
- [ ] Sensitive data encrypted at rest (AES-256)
- [ ] TLS 1.3 for all communications
- [ ] PII masked in logs

### Output Encoding
- [ ] HTML output escaped (prevent XSS)
- [ ] JSON properly serialized
- [ ] Content-Type headers set correctly
- [ ] Download filenames sanitized

### Error Handling
- [ ] Generic error messages to users
- [ ] Detailed errors logged internally
- [ ] No stack traces in production responses
- [ ] Fail securely (deny access on error)

### Dependencies
- [ ] No known CVEs in dependencies
- [ ] Dependencies pinned (lock files)
- [ ] Minimal dependencies principle
- [ ] Regular dependency updates

---

## 📊 Severity Assessment

| Severity | CVSS | Example | Response Time |
|----------|------|---------|---------------|
| **Critical** | 9.0-10.0 | RCE, SQLi with data exfiltration | 24 hours |
| **High** | 7.0-8.9 | Auth bypass, IDOR on sensitive data | 72 hours |
| **Medium** | 4.0-6.9 | XSS, CSRF, information disclosure | 1 week |
| **Low** | 0.1-3.9 | Verbose errors, missing headers | 1 month |

---

## 📚 References

- [OWASP Top 10:2021](https://owasp.org/Top10/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [SLSA (Supply-chain Levels for Software Artifacts)](https://slsa.dev/)
