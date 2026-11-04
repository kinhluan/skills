# Detailed Security Analysis Guide

> Reference status: illustrative patterns, not drop-in policy. Verify current standards, tool versions, action revisions, cipher policy, and vulnerability status against primary documentation before use. The top-level `SKILL.md` is authoritative when guidance conflicts.

Organized by the OWASP Top 10:2025. Each section shows a vulnerable pattern, a safer pattern, and review checks.

---

## Core Principles

| Principle | Meaning | In Practice |
|-----------|---------|-------------|
| **Assume Breach** | Design as if an attacker is already inside | Defense in depth, least privilege |
| **Least Privilege** | Minimum permissions necessary | Scoped tokens, service accounts, no root |
| **Fail Closed** | Errors deny access and expose nothing | Deny on exception, generic error responses |
| **Defense in Depth** | Multiple independent controls | Egress proxy + URL validation + network policy |
| **Zero Trust** | Authenticate and authorize every request | MFA, mTLS, per-request authorization |
| **Shift Left** | Catch issues before merge | SAST, secret scanning, pre-commit hooks |

---

## OWASP Top 10:2025

| 2025 | Category | Note |
|------|----------|------|
| A01 | Broken Access Control | Now includes SSRF |
| A02 | Security Misconfiguration | |
| A03 | Software Supply Chain Failures | Expands 2021 "Vulnerable and Outdated Components" |
| A04 | Cryptographic Failures | |
| A05 | Injection | |
| A06 | Insecure Design | |
| A07 | Authentication Failures | Renamed |
| A08 | Software or Data Integrity Failures | |
| A09 | Security Logging & Alerting Failures | Renamed |
| A10 | Mishandling of Exceptional Conditions | New |

### A01: Broken Access Control

**Vulnerable:**
```python
# No authorization check, and a client-controlled owner ID
@app.get("/api/orders")
def get_orders(user_id: str = Query(...)):  # attacker changes user_id
    return db.orders_for(user_id)
```

**Safer:**
```python
from fastapi import Depends, HTTPException

@app.get("/api/orders/{order_id}")
def get_order(order_id: str, current_user: User = Depends(get_current_user)):
    order = db.get_order(order_id)
    # Same response for "missing" and "not yours" avoids an existence oracle.
    if order is None or (order.user_id != current_user.id and not current_user.is_admin):
        raise HTTPException(status_code=404)
    return order
```

**Checks:**
- [ ] Deny by default; authorization enforced server-side on every request
- [ ] Object-, function-, and property-level checks (not just "logged in")
- [ ] CORS origins are an explicit allowlist when credentials are allowed
- [ ] Admin functions separated and separately authorized

#### SSRF (part of A01 in 2025)

**Vulnerable:**
```python
url = request.json["webhook_url"]
requests.get(url)  # can reach 169.254.169.254, localhost, internal services
```

A hostname blocklist or a "resolve, check, then `requests.get(url)`" check is **not** sufficient:

- DNS rebinding: the check resolves to a public IP, the request resolves again to an internal IP.
- Redirects: `requests` follows 3xx by default, so a public URL can redirect inward.
- Alternate encodings and families: IPv6, IPv4-mapped IPv6, decimal/hex IPv4, CGNAT and link-local ranges.

**Preferred control:** send outbound requests through an egress proxy or network policy that only allows approved destinations. If the application must fetch arbitrary URLs, resolve once, reject unless **every** address is public, connect to the checked address, and do not follow redirects:

```python
import ipaddress
import socket
from urllib.parse import SplitResult, urlsplit

import urllib3

DEFAULT_PORTS = {"http": 80, "https": 443}


class UnsafeURL(ValueError):
    pass


def resolve_public(url: str) -> tuple[SplitResult, str, int, str]:
    parts = urlsplit(url)
    hostname = parts.hostname
    if parts.scheme not in DEFAULT_PORTS or not hostname:
        raise UnsafeURL("only absolute http(s) URLs are allowed")
    if parts.username or parts.password:
        raise UnsafeURL("credentials in URLs are not allowed")
    port = parts.port or DEFAULT_PORTS[parts.scheme]

    # Resolve once, check every address, then connect to a checked address.
    infos = socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
    addresses: list[str] = []
    for info in infos:
        ip = ipaddress.ip_address(str(info[4][0]).split("%", 1)[0])
        if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped:
            ip = ip.ipv4_mapped
        if not ip.is_global or ip.is_multicast:
            raise UnsafeURL(f"{hostname} resolves to non-public {ip}")
        addresses.append(str(ip))
    return parts, hostname, port, addresses[0]


def safe_get(url: str, timeout: float = 5.0, max_bytes: int = 1_000_000) -> bytes:
    parts, hostname, port, ip = resolve_public(url)
    host = f"[{hostname}]" if ":" in hostname else hostname
    host_header = host if port == DEFAULT_PORTS[parts.scheme] else f"{host}:{port}"
    path = (parts.path or "/") + (f"?{parts.query}" if parts.query else "")

    pool: urllib3.HTTPConnectionPool
    if parts.scheme == "https":
        # Connect to the pinned IP; SNI and certificate checks use the hostname.
        pool = urllib3.HTTPSConnectionPool(
            ip, port, server_hostname=hostname, assert_hostname=hostname,
            timeout=timeout, retries=False,
        )
    else:
        pool = urllib3.HTTPConnectionPool(ip, port, timeout=timeout, retries=False)

    # retries=False also disables redirects: a 3xx is returned, never followed.
    response = pool.request(
        "GET", path, headers={"Host": host_header}, redirect=False, preload_content=False
    )
    try:
        body = response.read(max_bytes + 1)
    finally:
        response.release_conn()
    if len(body) > max_bytes:
        raise UnsafeURL("response too large")
    return body
```

Regression tests should cover `127.0.0.1`, `localhost`, `169.254.169.254`, `10.0.0.0/8`, `[::1]`, `[::ffff:127.0.0.1]`, `0.0.0.0`, `100.64.0.0/10`, decimal and hex IPv4, non-HTTP schemes, a DNS answer mixing public and private records, and a 3xx response pointing inward.

---

### A02: Security Misconfiguration

**Vulnerable:**
```python
app = FastAPI(debug=True)  # stack traces in responses

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True)

@app.exception_handler(Exception)
def handle_error(request, exc):
    return JSONResponse(status_code=500, content={"error": str(exc), "traceback": traceback.format_exc()})
```

**Safer:**
```python
app = FastAPI(debug=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

@app.exception_handler(Exception)
def handle_error(request, exc):
    logger.error("unhandled_error", exc_info=True)  # details stay internal
    return JSONResponse(status_code=500, content={"error": "Internal server error", "request_id": request.state.request_id})
```

**Security headers** (tune CSP to the application):
```python
headers = {
    "Content-Security-Policy": "default-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}
# Do not add X-XSS-Protection: it is obsolete and the legacy filter caused issues. Rely on CSP.
```

---

### A03: Software Supply Chain Failures

Covers dependencies, build systems, CI/CD, artifact registries, and update channels.

**Dependency scanning:**
```bash
pip-audit -r requirements.txt     # Python (PyPA)
npm audit --omit=dev              # Node: runtime deps; review dev deps separately
govulncheck ./...                 # Go: reports only vulnerabilities reachable from your code
osv-scanner scan source -r .      # Multi-ecosystem, OSV database
trivy image myapp@sha256:<digest> # Container images, scanned by digest
```

**Checks:**
- [ ] Lockfiles committed; installs reproducible (`npm ci`, `pip install --require-hashes`)
- [ ] Dependency alerts triaged by exposure, reachability, EPSS, and CISA KEV (see `SKILL.md`)
- [ ] CI actions pinned to full commit SHAs, not `@main`, `@master`, or moving tags
- [ ] `GITHUB_TOKEN` permissions set explicitly and minimally per job
- [ ] No `pull_request_target` workflow that checks out and runs untrusted PR code
- [ ] Private package names protected from dependency confusion (scoped or reserved names, registry pinning)
- [ ] New or renamed packages reviewed for typosquatting before adoption
- [ ] SBOM generated for releases; provenance (for example SLSA) attached to artifacts
- [ ] Agent extensions (skills, plugins, MCP servers, hooks) reviewed and version-pinned like any dependency

---

### A04: Cryptographic Failures

**Vulnerable:**
```python
password_hash = hashlib.md5(password.encode()).hexdigest()  # fast, unsalted
SECRET_KEY = "my-secret-key-123"                              # hardcoded key
```

**Safer password storage** (OWASP Password Storage Cheat Sheet prefers Argon2id):
```python
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()  # Argon2id with library defaults; tune to your hardware
stored = ph.hash(password)

try:
    ph.verify(stored, candidate)
    if ph.check_needs_rehash(stored):
        stored = ph.hash(candidate)  # upgrade parameters on login
except VerifyMismatchError:
    raise InvalidCredentials()
```

**Authenticated encryption:**
```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = load_key_from_kms()          # never generate-and-forget or hardcode
nonce = os.urandom(12)             # unique per encryption under the same key
ciphertext = AESGCM(key).encrypt(nonce, plaintext, associated_data)
# Store nonce alongside ciphertext. Fernet is a simpler alternative (AES-128-CBC + HMAC-SHA256).
```

**Checks:**
- [ ] Passwords: Argon2id (or scrypt/bcrypt where mandated), never MD5/SHA-1/plain SHA-2
- [ ] Data at rest: approved authenticated encryption with managed key lifecycle
- [ ] Data in transit: TLS 1.2+ (prefer 1.3); TLS 1.0/1.1 disabled
- [ ] Keys and secrets in a KMS or secret manager, rotated, never in source

---

### A05: Injection

**Vulnerable:**
```python
cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
os.system(f"convert {user_input} output.png")
```

**Safer:**
```python
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
User.objects.filter(id=user_id)  # ORM parameterizes

# No shell; "--" stops a leading "-" in user input from being parsed as an option.
subprocess.run(["convert", "--", user_input, "output.png"], check=True)
```

```go
db.QueryContext(ctx, "SELECT * FROM users WHERE id = ?", userID)
```

**Checks:**
- [ ] All queries parameterized; dynamic identifiers mapped from an allowlist
- [ ] No shell invocation with user data; argument arrays only
- [ ] Output encoded for its context (HTML, attribute, URL, JS)
- [ ] LLM output treated as untrusted input when it reaches any interpreter

---

### A06: Insecure Design

Missing controls that no amount of correct code can add later: rate limits, business invariants, anti-automation, CSRF protection.

```python
from fastapi import Request
from pydantic import BaseModel, Field
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)  # behind a proxy, derive client IP from trusted headers only

@app.post("/login")
@limiter.limit("5/minute")
def login(request: Request, credentials: LoginRequest):
    ...

class OrderItem(BaseModel):
    product_id: str
    quantity: int = Field(gt=0, le=100)  # business invariant in the type

def validate_csrf_token(request: Request) -> None:
    token = request.headers.get("X-CSRF-Token") or ""
    if not hmac.compare_digest(token, get_expected_token(request)):
        raise HTTPException(403, "Invalid CSRF token")
```

Use `threat-modeling` to find design gaps before implementation.

---

### A07: Authentication Failures

**JWT verification** (the decode side is where most bugs live):
```python
import jwt  # PyJWT

claims = jwt.decode(
    token,
    public_key,
    algorithms=["RS256"],              # pin; never derive from the token header
    audience="api://orders",
    issuer="https://idp.example.com",
    options={"require": ["exp", "iat", "sub"]},
)
```

**MFA:**
```python
import pyotp

totp = pyotp.TOTP(user.mfa_secret)
if not totp.verify(code, valid_window=1):  # never `assert`: asserts vanish under python -O
    raise InvalidCredentials()
# Also reject reuse of an accepted code within its time step.
```

**Logout:**
```python
@app.post("/logout")
def logout(request: Request, response: Response):
    invalidate_session(request.cookies.get("session_id"))  # server-side first
    response.delete_cookie("session_id")
```

**Checks:**
- [ ] Password policy per NIST SP 800-63B (length, breached-password screening, no forced rotation)
- [ ] MFA for privileged and sensitive accounts; phishing-resistant where possible
- [ ] Online guessing throttled (rate limit, backoff) without enabling lockout-based DoS
- [ ] Session IDs rotated on login; idle and absolute timeouts per policy
- [ ] Cookies `HttpOnly`, `Secure`, `SameSite`

---

### A08: Software or Data Integrity Failures

```python
# Vulnerable: pickle.loads(untrusted)  -> arbitrary code execution
data = json.loads(untrusted)  # safer: a data-only format, then schema validation
```

```bash
# Verify artifacts before use (Sigstore)
cosign verify-blob --bundle artifact.sigstore.json \
  --certificate-identity <expected-identity> \
  --certificate-oidc-issuer <expected-issuer> artifact.tar.gz
```

**Checks:**
- [ ] No native deserialization (`pickle`, Java serialization, unsafe YAML loaders) of untrusted data
- [ ] Update and plugin channels verify signatures before install
- [ ] Protected branches require review; release builds run from trusted, isolated runners

---

### A09: Security Logging & Alerting Failures

**Log:** authentication outcomes, authorization denials, privilege changes, access to sensitive resources, configuration changes.
**Never log:** passwords, tokens, API keys, session IDs, full payment data; mask PII.

```python
logger.info(
    "login_attempt",
    user_id=user_id,
    ip_address=client_ip,
    success=False,
    reason="invalid_password",
)
```

Logging without alerting is a 2025 failure mode: define who is paged for repeated failures, impossible travel, or privilege changes, and test that the alert fires.

---

### A10: Mishandling of Exceptional Conditions

**Vulnerable (fails open):**
```python
try:
    allowed = authz.check(user, "orders:read", order_id)
except AuthzUnavailable:
    allowed = True  # outage becomes an authorization bypass
```

**Safer:**
```python
try:
    allowed = authz.check(user, "orders:read", order_id)
except AuthzUnavailable:
    logger.warning("authz_unavailable", order_id=order_id)
    raise HTTPException(503)  # deny, and say the service is unavailable
```

**Checks:**
- [ ] Security decisions default to deny on error, timeout, or partial data
- [ ] Multi-step operations are atomic or compensated; no half-applied state
- [ ] Resources released on every path (context managers, `finally`)
- [ ] Error responses do not leak internals; unexpected errors are logged and alerted

---

## AI and Agent Security

Use with the OWASP Top 10 for LLM Applications.

| Risk | Review question |
|------|-----------------|
| Prompt injection | Can untrusted content (documents, web pages, issues, tool output) steer actions? |
| Sensitive information disclosure | Can context, retrieval, logs, or traces expose secrets or other tenants' data? |
| Supply chain | Are models, datasets, skills, plugins, and MCP servers from reviewed, pinned sources? |
| Improper output handling | Does model output reach a shell, SQL, HTML, path, URL fetch, or deserializer unchecked? |
| Excessive agency | Which tools and credentials can the model use, and which actions need human confirmation? |
| System prompt leakage | Does the system prompt contain secrets or authorization logic it should not? |
| Unbounded consumption | Can an attacker trigger runaway loops, recursion, or token and tool spend? |

Controls that hold up: least-privilege tool credentials, human confirmation for irreversible or outward actions, output encoding at every sink, per-tenant retrieval filtering enforced outside the model, and budgets on steps, tokens, and time.

---

## DevSecOps Pipeline

Pin every third-party action to a full commit SHA (shown as `<sha>`) and record the version in a comment. Set token permissions explicitly.

```yaml
# .github/workflows/security.yml
name: Security Scan
on: [pull_request]

permissions:
  contents: read

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<sha> # vX.Y.Z
      - name: Bandit (fails on high-severity findings)
        run: |
          pip install bandit
          bandit -r src/ -lll
      - name: Semgrep (fails on findings)
        run: |
          pip install semgrep
          semgrep scan --config p/default --error src/

  sca:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write   # only this job uploads SARIF
    steps:
      - uses: actions/checkout@<sha> # vX.Y.Z
      - name: Trivy filesystem scan
        uses: aquasecurity/trivy-action@<sha> # vX.Y.Z
        with:
          scan-type: fs
          format: sarif
          output: trivy-results.sarif
      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@<sha> # current major
        with:
          sarif_file: trivy-results.sarif

  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<sha> # vX.Y.Z
        with:
          fetch-depth: 0
      - name: TruffleHog
        uses: trufflesecurity/trufflehog@<sha> # vX.Y.Z
        with:
          extra_args: --only-verified
```

Never append `|| true` to a security step: it turns the gate into a report nobody reads. If a tool needs a baseline, commit the baseline and fail on new findings.

DAST runs against an environment you own and are authorized to scan (for example staging), never production without explicit approval. Route active testing to `penetration-testing`.

---

## Secrets Management

```python
# Hardcoded: never
API_KEY = "sk-live-abc123"

# Environment variable injected by the platform
API_KEY = os.environ["API_KEY"]

# Secret manager
secret = boto3.client("secretsmanager").get_secret_value(SecretId="prod/api-key")

# Kubernetes: prefer a mounted file over an env var (env leaks via /proc, crash dumps, child processes)
api_key = Path("/var/run/secrets/app/api-key").read_text().strip()
```

**Pre-commit:**
```yaml
# .pre-commit-config.yaml (pin rev to a released tag or SHA)
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: <pinned>
    hooks:
      - id: detect-private-key
  - repo: https://github.com/Yelp/detect-secrets
    rev: <pinned>
    hooks:
      - id: detect-secrets
        args: ["--baseline", ".secrets.baseline"]
```

If a secret was committed, rotate it first: deleting it from history does not un-leak it.

---

## Severity

Score technical severity with a stated method, then adjust for business context and existing controls.

| Severity | CVSS (v3.1/v4.0 base) | Typical examples |
|----------|-----------------------|------------------|
| Critical | 9.0–10.0 | Unauthenticated RCE, SQL injection with data exfiltration |
| High | 7.0–8.9 | Authentication bypass, IDOR on sensitive data |
| Medium | 4.0–6.9 | Stored XSS with limited reach, CSRF on non-critical actions |
| Low | 0.1–3.9 | Verbose errors, missing hardening headers |

Raise priority for presence in CISA KEV or a high EPSS score; lower it for unreachable or dev-only code. Remediation deadlines come from the owner's policy, not from this table.

---

## References

- [OWASP Top 10:2025](https://top10.owasp.org/2025/)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [FIRST EPSS](https://www.first.org/epss/)
- [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [SLSA](https://slsa.dev/)
