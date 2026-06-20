---
name: api-security
description: API security best practices, OWASP API Security Top 10 2023, authentication, authorization, rate limiting, and API gateway security. Use when securing REST APIs, GraphQL, OAuth 2.0 implementations, or API gateway configurations.
metadata:
  tags:
  - security
  - api
  - oauth
  - jwt
  - graphql
  version: 1.0.0
---

# API Security

Comprehensive API security guidance covering OWASP API Security Top 10 2023, authentication, authorization, rate limiting, and secure API design.

> "APIs are the new perimeter. Secure them like your front door."

---

## 🎯 When to Use

- Securing REST/GraphQL APIs
- Implementing OAuth 2.0 / JWT authentication
- Configuring API gateways (Kong, AWS API Gateway, Azure API Management)
- Designing secure API architectures
- Rate limiting and throttling
- API vulnerability assessment
- API documentation security review

---

## 🛡️ OWASP API Security Top 10 2023

### API1:2023 — Broken Object Level Authorization (BOLA)

**What:** Users can access objects they shouldn't by manipulating IDs in API requests.

**Vulnerable:**
```http
GET /api/orders/12345
# No check if current user owns order 12345
```

**Secure:**
```python
from fastapi import Depends, HTTPException

@app.get("/api/orders/{order_id}")
def get_order(
    order_id: str,
    current_user: User = Depends(get_current_user)
):
    order = db.get_order(order_id)
    if order.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(403, "Access denied")
    return order
```

**Checklist:**
- [ ] Validate object ownership on every request
- [ ] Use random UUIDs instead of sequential IDs
- [ ] Implement authorization middleware
- [ ] Test with different user contexts

---

### API2:2023 — Broken Authentication

**What:** Weak authentication mechanisms allow attackers to impersonate users.

**Secure JWT Implementation:**
```python
import jwt
from datetime import datetime, timedelta

# Token generation
def create_access_token(user_id: str, secret: str) -> str:
    payload = {
        "sub": user_id,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=15),
        "type": "access"
    }
    return jwt.encode(payload, secret, algorithm="HS256")

# Token verification
def verify_token(token: str, secret: str) -> dict:
    try:
        payload = jwt.decode(
            token, secret,
            algorithms=["HS256"],
            options={"require": ["exp", "sub"]}
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")
```

**Secure Session Management:**
```python
# Refresh token rotation
def refresh_access_token(refresh_token: str) -> tuple:
    payload = verify_token(refresh_token, REFRESH_SECRET)
    # Invalidate old refresh token
    token_store.revoke(payload["jti"])
    # Issue new pair
    new_access = create_access_token(payload["sub"], ACCESS_SECRET)
    new_refresh = create_refresh_token(payload["sub"])
    return new_access, new_refresh
```

**Checklist:**
- [ ] Short-lived access tokens (15 min)
- [ ] Refresh token rotation
- [ ] Secure token storage (HttpOnly cookies)
- [ ] MFA for sensitive operations
- [ ] Account lockout after failed attempts
- [ ] Strong password policy (NIST 800-63b)

---

### API3:2023 — Broken Object Property Level Authorization

**What:** Exposing sensitive fields or allowing mass assignment.

**Vulnerable:**
```python
# Returns ALL user fields including password_hash
@app.get("/api/users/{user_id}")
def get_user(user_id: str):
    return db.users.find_one({"_id": user_id})
```

**Secure:**
```python
from pydantic import BaseModel

class UserPublic(BaseModel):
    id: str
    username: str
    display_name: str
    created_at: datetime
    # password_hash is NOT included

@app.get("/api/users/{user_id}", response_model=UserPublic)
def get_user(user_id: str):
    user = db.users.find_one({"_id": user_id})
    return UserPublic(**user)

# Prevent mass assignment
class UserUpdate(BaseModel):
    display_name: str | None = None
    email: str | None = None
    # role is NOT included — cannot be changed via API
```

---

### API4:2023 — Unrestricted Resource Consumption

**What:** No rate limiting allows DoS via resource exhaustion.

**Rate Limiting Implementation:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/login")
@limiter.limit("5/minute")
def login(credentials: LoginRequest):
    ...

@app.get("/api/data")
@limiter.limit("100/minute")
def get_data():
    ...

# Per-user rate limiting
@app.get("/api/expensive")
@limiter.limit("10/hour", per_method=True, key_func=lambda: current_user.id)
def expensive_operation():
    ...
```

**API Gateway Rate Limiting (Kong):**
```yaml
plugins:
  - name: rate-limiting
    config:
      minute: 100
      policy: redis
      redis_host: redis
      fault_tolerant: true
      hide_client_headers: false
```

---

### API5:2023 — Broken Function Level Authorization

**What:** Missing authorization checks on administrative functions.

**Secure:**
```python
from functools import wraps

def require_admin(f):
    @wraps(f)
    async def wrapper(*args, **kwargs):
        user = await get_current_user()
        if not user.is_admin:
            raise HTTPException(403, "Admin access required")
        return await f(*args, **kwargs)
    return wrapper

@app.delete("/api/users/{user_id}")
@require_admin
def delete_user(user_id: str):
    db.users.delete_one({"_id": user_id})
```

---

### API6:2023 — Unrestricted Access to Sensitive Business Flows

**What:** Automated abuse of business logic (e.g., ticket scalping, vote manipulation).

**Mitigations:**
```python
# CAPTCHA for high-risk operations
@app.post("/api/purchase")
@require_captcha
def purchase_ticket(request: PurchaseRequest):
    ...

# Device fingerprinting
@app.post("/api/vote")
def cast_vote(request: VoteRequest):
    fingerprint = generate_device_fingerprint(request)
    if vote_store.has_voted_today(request.poll_id, fingerprint):
        raise HTTPException(429, "Already voted today")
    ...

# Progressive delays
@app.post("/api/resend-verification")
def resend_verification(email: str):
    count = verification_store.get_count(email)
    delay = min(2 ** count, 3600)  # Exponential backoff, max 1 hour
    time.sleep(delay)
    ...
```

---

### API7:2023 — Server Side Request Forgery (SSRF)

**What:** Server makes requests to attacker-controlled URLs.

**Secure:**
```python
import urllib.parse
import ipaddress

def validate_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    
    # Whitelist schemes
    if parsed.scheme not in {"http", "https"}:
        return False
    
    # Block internal IPs
    blocked_hosts = {
        "localhost", "127.0.0.1", "0.0.0.0", "::1",
        "169.254.169.254"  # AWS metadata
    }
    if parsed.hostname in blocked_hosts:
        return False
    
    # Resolve and check IP
    try:
        ip = socket.getaddrinfo(parsed.hostname, None)[0][4][0]
        if ipaddress.ip_address(ip).is_private:
            return False
    except:
        return False
    
    return True

@app.post("/api/webhook")
def set_webhook(request: WebhookRequest):
    if not validate_url(request.url):
        raise HTTPException(400, "Invalid URL")
    # ...
```

---

### API8:2023 — Security Misconfiguration

**What:** Default configs, verbose errors, unnecessary features.

**Secure Configuration:**
```python
# FastAPI production config
app = FastAPI(
    debug=False,
    docs_url=None,      # Disable Swagger in production
    redoc_url=None,     # Disable ReDoc in production
    openapi_url=None    # Disable OpenAPI schema
)

# Security headers
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

# Generic error messages
@app.exception_handler(Exception)
async def handle_error(request, exc):
    logger.error(f"Error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "request_id": request.state.request_id}
    )
```

---

### API9:2023 — Improper Inventory Management

**What:** Shadow APIs, deprecated versions, and undocumented endpoints.

**Mitigations:**
```yaml
# API versioning strategy
/api/v1/users      # Current stable
/api/v2/users      # Latest (may have breaking changes)
/api/v1/deprecated # Marked for removal

# Sunset headers
Sunset: Sat, 31 Dec 2024 23:59:59 GMT
Deprecation: true
```

```python
# API discovery and documentation
@app.get("/api/versions")
def list_versions():
    return {
        "current": "v2",
        "supported": ["v1", "v2"],
        "deprecated": ["v0"],
        "sunset_dates": {"v1": "2024-12-31"}
    }

# API inventory scanning
# Use tools like: OWASP ZAP, Burp Suite, Postman
```

---

### API10:2023 — Unsafe Consumption of APIs

**What:** Trusting data from third-party APIs without validation.

**Secure:**
```python
import requests
from pydantic import BaseModel, ValidationError

class ThirdPartyUser(BaseModel):
    id: str
    email: str
    name: str

@app.get("/api/external-user/{user_id}")
def get_external_user(user_id: str):
    # Validate input
    if not user_id.isalnum():
        raise HTTPException(400, "Invalid user ID")
    
    # Call third-party API
    try:
        response = requests.get(
            f"https://api.thirdparty.com/users/{user_id}",
            timeout=5,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(502, "External service unavailable")
    
    # Validate response
    try:
        user = ThirdPartyUser(**response.json())
    except ValidationError:
        raise HTTPException(502, "Invalid response from external service")
    
    return user
```

---

## 🔐 OAuth 2.0 & JWT Security

### OAuth 2.0 Flow Selection

```
┌─────────────────────────────────────────────────────────────┐
│                    OAuth 2.0 Flows                          │
├─────────────────────────────────────────────────────────────┤
│ Authorization Code + PKCE    │ Mobile/SPAs (recommended)    │
│ Authorization Code           │ Web apps with backend        │
│ Client Credentials           │ Server-to-server             │
│ Device Code                  │ Input-constrained devices    │
│ Implicit                     │ ❌ DEPRECATED, do not use    │
│ Password                     │ ❌ DEPRECATED, do not use    │
└─────────────────────────────────────────────────────────────┘
```

### PKCE Implementation

```python
import secrets
import hashlib
import base64

# Step 1: Generate code verifier and challenge
code_verifier = base64.urlsafe_b64encode(
    secrets.token_bytes(32)
).rstrip(b'=').decode('ascii')

code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).rstrip(b'=').decode('ascii')

# Step 2: Authorization request
# GET /authorize?response_type=code&client_id=...&redirect_uri=...&code_challenge=...&code_challenge_method=S256

# Step 3: Token exchange
# POST /token
# grant_type=authorization_code&code=...&redirect_uri=...&client_id=...&code_verifier=...
```

### JWT Best Practices

```python
# Use RS256 for asymmetric signing (public key verification)
# Use HS256 only for internal service-to-service

# Key rotation
# Maintain multiple valid keys, rotate every 90 days

# Token binding
# Bind tokens to TLS session or device fingerprint

# Secure claims
"""
Required claims:
  - sub: subject (user ID)
  - iss: issuer
  - aud: audience
  - exp: expiration
  - iat: issued at
  - jti: unique token ID (for revocation)

Forbidden claims:
  - Never include passwords or secrets
  - Never include PII without encryption
"""
```

---

## 🌐 GraphQL Security

### Query Depth Limiting

```python
from graphql.validation import ValidationRule

class QueryDepthLimit(ValidationRule):
    def __init__(self, max_depth: int = 10):
        self.max_depth = max_depth
    
    def enter_selection_set(self, node, *args):
        depth = self._get_depth(node)
        if depth > self.max_depth:
            raise GraphQLError(f"Query exceeds maximum depth of {self.max_depth}")

# Apollo Server
const server = new ApolloServer({
    typeDefs,
    resolvers,
    validationRules: [createComplexityLimitRule(1000)],
    plugins: [queryDepthLimit(10)]
});
```

### Query Complexity Analysis

```python
# Calculate complexity score
def calculate_complexity(node, depth=0):
    score = 1
    for child in node.selections:
        score += calculate_complexity(child, depth + 1) * (depth + 1)
    return score

# Reject overly complex queries
MAX_COMPLEXITY = 1000

@app.post("/graphql")
def graphql_endpoint(query: GraphQLQuery):
    ast = parse(query)
    complexity = calculate_complexity(ast)
    if complexity > MAX_COMPLEXITY:
        raise HTTPException(400, f"Query complexity {complexity} exceeds limit {MAX_COMPLEXITY}")
```

---

## 📋 API Security Checklist

### Authentication
- [ ] Strong authentication (OAuth 2.0 + PKCE or mTLS)
- [ ] Short-lived tokens with rotation
- [ ] MFA for sensitive operations
- [ ] Secure token storage (HttpOnly, Secure, SameSite)

### Authorization
- [ ] Object-level authorization on every endpoint
- [ ] Function-level authorization for admin operations
- [ ] Principle of least privilege
- [ ] Regular access reviews

### Input Validation
- [ ] Strict schema validation (OpenAPI, JSON Schema)
- [ ] Parameterized queries (prevent injection)
- [ ] File upload restrictions (type, size, content)
- [ ] URL validation (prevent SSRF)

### Output Protection
- [ ] Response filtering (prevent data leakage)
- [ ] Error message sanitization
- [ ] CORS properly configured
- [ ] Security headers on all responses

### Rate Limiting
- [ ] Per-IP rate limiting
- [ ] Per-user rate limiting
- [ ] Per-endpoint rate limiting
- [ ] Progressive delays for repeated failures

### Monitoring
- [ ] API access logging
- [ ] Anomaly detection
- [ ] Failed authentication alerting
- [ ] Rate limit violation tracking

---

## 🛠️ Tools

| Tool | Purpose |
|------|---------|
| **OWASP ZAP** | API security scanning |
| **Burp Suite** | Web/API penetration testing |
| **Postman** | API testing & documentation |
| **Insomnia** | API testing |
| **Kong** | API gateway |
| **AWS API Gateway** | Cloud API gateway |
| **Azure API Management** | Cloud API gateway |
| **JWT.io** | JWT debugging |
| **OAuth.tools** | OAuth flow testing |

---

## 📚 References

- [OWASP API Security Top 10 2023](https://owasp.org/www-project-api-security/)
- [OWASP API Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/API_Security_Cheat_Sheet.html)
- [OAuth 2.0 Security Best Practices](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics)
- [JWT Best Practices](https://datatracker.ietf.org/doc/html/rfc8725)
- [GraphQL Security](https://graphql.org/learn/thinking-in-graphs/)
