---
name: threat-modeling
description: Security threat modeling and risk assessment using STRIDE, Attack Trees, and DREAD scoring. Use when designing secure architecture, conducting security design reviews, assessing risks, or creating threat models for applications, systems, or cloud infrastructure.
metadata:
  tags:
  - security
  - threat-modeling
  - stride
  - risk-assessment
  version: 1.0.0
---

# Threat Modeling

Systematic approach to identifying, quantifying, and addressing security threats in software architecture and system design.

> "Threat modeling is the key to a secure design." — Adam Shostack

---

## 🎯 When to Use

- Designing new systems or architecture
- Conducting security design reviews
- Assessing risks before implementation
- Reviewing third-party integrations
- Cloud migration security planning
- Compliance and audit preparation

---

## 🔧 Core Methodologies

### STRIDE

| Threat Category | Description | Example |
|-----------------|-------------|---------|
| **S**poofing | Pretending to be someone else | Fake JWT token, stolen credentials |
| **T**ampering | Modifying data or code | Man-in-the-middle, code injection |
| **R**epudiation | Denying an action | Missing audit logs, no transaction records |
| **I**nformation Disclosure | Exposing sensitive data | SQL injection, verbose error messages |
| **D**enial of Service | Making system unavailable | DDoS, resource exhaustion |
| **E**levation of Privilege | Gaining unauthorized access | Privilege escalation, IDOR |

### DREAD Scoring

| Factor | Question | Score (1-10) |
|--------|----------|--------------|
| **D**amage | How bad is the damage? | 1=Minimal, 10=Total compromise |
| **R**eproducibility | How easy to reproduce? | 1=Very hard, 10=Always works |
| **E**xploitability | How easy to exploit? | 1=Expert only, 10=Script kiddie |
| **A**ffected Users | How many users affected? | 1=None, 10=All users |
| **D**iscoverability | How easy to discover? | 1=Very hard, 10=Obvious |

**Risk Score = (D + R + E + A + D) / 5**

| Risk Level | Score Range |
|------------|-------------|
| Critical | 9.0-10.0 |
| High | 7.0-8.9 |
| Medium | 4.0-6.9 |
| Low | 0.1-3.9 |

---

## 🏗️ Threat Modeling Process

### Step 1: Define Scope & Assets

```
Identify:
├─ What are we building? (system, feature, API)
├─ What data flows through it?
├─ Who are the users/actors?
├─ What are the trust boundaries?
└─ What are the high-value assets?
```

### Step 2: Create Data Flow Diagram (DFD)

```
Elements:
├─ External Entity (rectangle) — User, third-party service
├─ Process (circle) — Application, microservice
├─ Data Store (two horizontal lines) — Database, cache
├─ Data Flow (arrow) — HTTP request, message queue
└─ Trust Boundary (dashed line) — Network perimeter, tenant boundary

Example: E-commerce Checkout

[User] --HTTPS--> [Web App] --SQL--> [Database]
    |                  |
    |                  | --API--> [Payment Gateway]
    |                  |
Trust Boundary 1   Trust Boundary 2
```

### Step 3: Identify Threats (STRIDE-per-Element)

```
For each element in DFD, apply STRIDE:

External Entity:
  ├─ Spoofing: Can someone impersonate this user?
  └─ Repudiation: Can the user deny their actions?

Process:
  ├─ Spoofing: Can someone fake the process identity?
  ├─ Tampering: Can the process code be modified?
  ├─ Repudiation: Are actions logged?
  ├─ Information Disclosure: Does the process leak data?
  ├─ Denial of Service: Can the process be overwhelmed?
  └─ Elevation of Privilege: Can the process gain more rights?

Data Store:
  ├─ Tampering: Can stored data be modified?
  ├─ Information Disclosure: Can unauthorized access occur?
  └─ Denial of Service: Can the store be made unavailable?

Data Flow:
  ├─ Tampering: Can data in transit be modified?
  ├─ Information Disclosure: Can data be intercepted?
  └─ Denial of Service: Can the flow be blocked?
```

### Step 4: Score & Prioritize (DREAD)

```
Example: SQL Injection in Checkout API

Damage: 9 (Full database access, customer data exposed)
Reproducibility: 8 (Always reproducible with crafted input)
Exploitability: 7 (Basic SQL knowledge needed)
Affected Users: 9 (All customers)
Discoverability: 6 (Requires some probing)

Risk Score = (9 + 8 + 7 + 9 + 6) / 5 = 7.8 → HIGH
```

### Step 5: Mitigate & Validate

```
Mitigation Strategies:
├─ Eliminate: Remove the threat entirely
├─ Reduce: Lower likelihood or impact
├─ Transfer: Move risk to another party (insurance)
└─ Accept: Document and monitor

For each threat, define:
├─ Mitigation technique
├─ Implementation owner
├─ Validation method
└─ Timeline
```

---

## 🌳 Attack Trees

### Structure

```
Goal: Steal customer credit card data
│
├─ AND: Gain database access
│   ├─ Exploit SQL injection
│   │   └─ Find vulnerable endpoint
│   │   └─ Craft payload
│   ├─ Compromise application server
│   │   └─ Exploit RCE
│   │   └─ Use stolen credentials
│   └─ Social engineer DBA
│
├─ OR: Intercept payment data
│   ├─ Man-in-the-middle attack
│   │   └─ Compromise network infrastructure
│   ├─ Compromise payment gateway
│   │   └─ Exploit API vulnerability
│   └─ Insider threat
│       └─ Bribe employee
│
└─ AND: Exfiltrate data
    ├─ Establish covert channel
    └─ Bypass DLP controls
```

### Attack Tree Analysis

```
For each node, calculate:
├─ Cost (effort/resources needed)
├─ Time (how long to execute)
├─ Skill (expertise required)
└─ Detection (likelihood of being caught)

Leaf nodes with lowest cost + time + skill = highest risk paths
```

---

## ☁️ Cloud-Specific Threat Modeling

### AWS Threat Model Template

```
Assets:
├─ S3 buckets (customer data, backups)
├─ RDS databases (transaction records)
├─ Lambda functions (business logic)
├─ IAM roles (privilege escalation vectors)
└─ VPC (network segmentation)

Trust Boundaries:
├─ Internet → CloudFront/WAF
├─ CloudFront → ALB
├─ ALB → ECS/EKS (container workloads)
├─ ECS → RDS (database tier)
└─ Cross-account boundaries

Key Threats:
├─ S3 bucket misconfiguration (public access)
├─ IAM over-permission (wildcard policies)
├─ Lambda injection (event source poisoning)
├─ VPC peering exposure
└─ Secrets in CloudWatch logs
```

### Kubernetes Threat Model

```
Assets:
├─ etcd (cluster state, secrets)
├─ API Server (control plane)
├─ kubelet (node agent)
├─ Container images
└─ Network policies

Threats:
├─ etcd unauthorized access → cluster compromise
├─ API Server exposed → entire cluster at risk
├─ Privileged containers → host escape
├─ Weak network policies → lateral movement
└─ Malicious images → supply chain attack
```

---

## 📋 Threat Modeling Checklist

### Pre-Modeling
- [ ] System architecture documented
- [ ] Data classification completed
- [ ] User roles and permissions defined
- [ ] Third-party integrations identified
- [ ] Compliance requirements known

### During Modeling
- [ ] DFD created with trust boundaries
- [ ] STRIDE applied to all elements
- [ ] Attack trees for critical assets
- [ ] DREAD scoring for all threats
- [ ] Mitigations identified per threat

### Post-Modeling
- [ ] Threats prioritized by risk score
- [ ] Mitigation roadmap created
- [ ] Validation tests defined
- [ ] Review scheduled (quarterly)
- [ ] Documentation updated

---

## 🛠️ Tools

| Tool | Purpose |
|------|---------|
| **Microsoft Threat Modeling Tool** | DFD creation, STRIDE analysis |
| **OWASP Threat Dragon** | Open-source threat modeling |
| **pytm** | Python threat modeling framework |
| **ThreatSpec** | Threat modeling as code |
| **IriusRisk** | Enterprise threat modeling platform |

---

## 📚 References

- [STRIDE by Microsoft](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [Threat Modeling: Designing for Security](https://www.amazon.com/Threat-Modeling-Designing-Adam-Shostack/dp/1118809998) — Adam Shostack
- [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/)
