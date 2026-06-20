---
name: container-security
description: Container and Kubernetes security hardening, image scanning, runtime protection, and supply chain security. Use when securing Docker containers, Kubernetes clusters, scanning images for vulnerabilities, or implementing runtime security controls.
metadata:
  tags:
  - security
  - containers
  - kubernetes
  - docker
  - falco
  version: 1.0.0
---

# Container Security

Comprehensive container and Kubernetes security: image hardening, runtime protection, supply chain security, and cluster hardening.

> "Containers are only as secure as the images they run and the clusters that orchestrate them."

---

## 🎯 When to Use

- Securing Docker containers and images
- Hardening Kubernetes clusters
- Scanning container images for vulnerabilities
- Implementing runtime security (Falco, Sysdig)
- Supply chain security (Sigstore, SLSA)
- Pod Security Standards enforcement
- Network policies for microservices

---

## 🐳 Docker Security

### Image Hardening

```dockerfile
# Multi-stage build for minimal attack surface
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

# Distroless final image
FROM gcr.io/distroless/static:nonroot
COPY --from=builder /app/main /main
USER nonroot:nonroot
EXPOSE 8080
ENTRYPOINT ["/main"]
```

```dockerfile
# Security best practices
FROM node:20-alpine

# Run as non-root
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Install only production dependencies
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Copy application with correct ownership
COPY --chown=nodejs:nodejs . /app
WORKDIR /app
USER nodejs

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node healthcheck.js || exit 1

EXPOSE 3000
CMD ["node", "server.js"]
```

### Docker Security Options

```bash
# Run with security options
docker run \
    --read-only \
    --security-opt=no-new-privileges:true \
    --cap-drop=ALL \
    --cap-add=NET_BIND_SERVICE \
    --memory=512m \
    --memory-swap=512m \
    --cpus=1.0 \
    --pids-limit=100 \
    --user 1000:1000 \
    myapp:latest

# Disable inter-container communication
docker network create --internal --subnet 172.18.0.0/16 isolated-network
```

### Image Scanning

```bash
# Trivy
trivy image myapp:latest
trivy image --severity HIGH,CRITICAL myapp:latest
trivy image --format sarif -o report.sarif myapp:latest

# Snyk
snyk container test myapp:latest
snyk container test --severity-threshold=high myapp:latest

# Clair
clairctl report myapp:latest

# Grype
grype myapp:latest
grype myapp:latest -o sarif > grype-report.sarif
```

### Dockerfile Security Audit

```bash
# Check for common issues
dockerfilelint Dockerfile

# Hadolint
hadolint Dockerfile

# Checkov for Docker
checkov -f Dockerfile --framework dockerfile
```

---

## ☸️ Kubernetes Security

### RBAC Configuration

```yaml
# Least-privilege ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: production
automountServiceAccountToken: false
---
# Role with minimal permissions
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-role
  namespace: production
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get"]
  resourceNames: ["app-config"]
---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-rolebinding
  namespace: production
subjects:
- kind: ServiceAccount
  name: app-sa
  namespace: production
roleRef:
  kind: Role
  name: app-role
  apiGroup: rbac.authorization.k8s.io
```

### Pod Security Standards

```yaml
# Restricted Pod Security Standard
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
  namespace: production
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    resources:
      limits:
        memory: "256Mi"
        cpu: "500m"
      requests:
        memory: "128Mi"
        cpu: "250m"
    volumeMounts:
    - name: tmp
      mountPath: /tmp
    - name: cache
      mountPath: /cache
  volumes:
  - name: tmp
    emptyDir: {}
  - name: cache
    emptyDir: {}
```

### Network Policies

```yaml
# Deny all by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
---
# Allow frontend to backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
---
# Allow backend to database only
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-to-db
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: backend
    ports:
    - protocol: TCP
      port: 5432
```

### Secrets Management

```yaml
# External Secrets Operator (recommended)
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: ClusterSecretStore
    name: aws-secrets-manager
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
  - secretKey: DATABASE_URL
    remoteRef:
      key: production/app
      property: database_url
  - secretKey: API_KEY
    remoteRef:
      key: production/app
      property: api_key
```

```bash
# Never store secrets in plain text
# Check for secrets in manifests
grep -r "password:" ./k8s/
grep -r "secret:" ./k8s/
grep -r "token:" ./k8s/

# Use sealed secrets for GitOps
kubeseal --format=yaml < secret.yaml > sealed-secret.yaml
```

---

## 🔒 Supply Chain Security

### Image Signing & Verification

```bash
# Cosign (Sigstore)
cosign generate-key-pair
cosign sign --key cosign.key myregistry/myapp:latest
cosign verify --key cosign.pub myregistry/myapp:latest

# SLSA provenance
cosign attest --predicate slsa-provenance.json --type slsaprovenance myregistry/myapp:latest

# Verify SLSA
slsa-verifier verify-image myregistry/myapp:latest \
    --source-uri github.com/myorg/myrepo \
    --print-provenance
```

### SBOM Generation

```bash
# Syft
syft myapp:latest -o spdx-json > sbom.spdx.json
syft myapp:latest -o cyclonedx-json > sbom.cyclonedx.json

# Trivy SBOM
trivy image --format cyclonedx -o sbom.cyclonedx.json myapp:latest

# Grype SBOM
grype myapp:latest -o cyclonedx-json > sbom.cyclonedx.json
```

### Admission Controllers

```yaml
# Kyverno policy: require labels
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-labels
spec:
  validationFailureAction: enforce
  rules:
  - name: check-for-labels
    match:
      resources:
        kinds:
        - Pod
    validate:
      message: "All pods must have app and version labels"
      pattern:
        metadata:
          labels:
            app: "?*"
            version: "?*"
---
# OPA Gatekeeper: disallow privileged containers
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8spspprivilegedcontainer
spec:
  crd:
    spec:
      names:
        kind: K8sPSPPrivilegedContainer
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8spspprivilegedcontainer
        violation[{"msg": msg}] {
          c := input.review.object.spec.containers[_]
          c.securityContext.privileged
          msg := sprintf("Privileged container is not allowed: %v", [c.name])
        }
```

---

## 🛡️ Runtime Security

### Falco

```yaml
# Falco rule: detect shell in container
- rule: Terminal Shell in Container
  desc: Detect shell execution inside a container
  condition: spawned_process and container and shell_procs
  output: "Shell spawned in container (user=%user.name container=%container.name)"
  priority: WARNING

# Falco rule: detect privilege escalation
- rule: Privilege Escalation
  desc: Detect privilege escalation via setuid/setgid
  condition: spawned_process and (setuid or setgid)
  output: "Privilege escalation detected (user=%user.name command=%proc.cmdline)"
  priority: CRITICAL
```

```bash
# Install Falco
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm install falco falcosecurity/falco \
    --set driver.kind=modern_ebpf \
    --set tty=true

# Check Falco alerts
kubectl logs -l app=falco -n falco | grep "Warning\|Critical"
```

### Runtime Monitoring

```bash
# Sysdig
sysdig -p"%evt.time %proc.name %fd.name" evt.type=open

# Check for suspicious processes in containers
kubectl get pods --all-namespaces -o json | jq '.items[].spec.containers[].securityContext'

# Audit pod security contexts
kubectl get pods -o json | jq '.items[] | {name: .metadata.name, securityContext: .spec.securityContext, containers: [.spec.containers[] | {name: .name, securityContext: .securityContext}]}'
```

---

## 📋 Security Checklist

### Image Security
- [ ] Use minimal base images (distroless, alpine, scratch)
- [ ] Run as non-root user
- [ ] Scan images for CVEs before deployment
- [ ] Sign images with Cosign
- [ ] Generate and store SBOMs
- [ ] Use multi-stage builds
- [ ] Pin base image versions (no `latest`)
- [ ] Remove unnecessary packages and tools

### Kubernetes Security
- [ ] Enable Pod Security Standards (Restricted)
- [ ] Implement Network Policies (deny-all default)
- [ ] Use RBAC with least privilege
- [ ] Disable automountServiceAccountToken where not needed
- [ ] Enable audit logging
- [ ] Use external secrets management (not plain YAML)
- [ ] Enable admission controllers (Kyverno/OPA)
- [ ] Regular cluster security scanning (kube-bench, kube-hunter)

### Runtime Security
- [ ] Deploy Falco for runtime threat detection
- [ ] Monitor for privilege escalation
- [ ] Alert on unexpected network connections
- [ ] Track container drift (file changes)
- [ ] Monitor resource usage anomalies

---

## 🛠️ Tools Reference

| Tool | Purpose |
|------|---------|
| **Trivy** | Container image & filesystem scanning |
| **Grype** | Vulnerability scanner for containers |
| **Snyk** | Container & dependency scanning |
| **Clair** | Static vulnerability analysis |
| **Cosign** | Container image signing (Sigstore) |
| **Syft** | SBOM generation |
| **Falco** | Runtime threat detection |
| **Sysdig** | Container monitoring & forensics |
| **kube-bench** | CIS Kubernetes benchmark |
| **kube-hunter** | Kubernetes penetration testing |
| **Kyverno** | Kubernetes policy engine |
| **OPA Gatekeeper** | Policy enforcement |
| **Sealed Secrets** | Encrypt secrets for GitOps |
| **External Secrets Operator** | Sync secrets from external providers |

---

## 📚 References

- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes)
- [NIST Container Security Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
- [Kubernetes Security Best Practices](https://kubernetes.io/docs/concepts/security/)
- [Sigstore Documentation](https://docs.sigstore.dev/)
