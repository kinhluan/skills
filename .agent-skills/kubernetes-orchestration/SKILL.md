---
name: kubernetes-orchestration
description: Kubernetes deployment and orchestration patterns
metadata:
  tags: ["kubernetes", "k8s", "orchestration", "devops", "cloud", "deployment"]
---

# Kubernetes Orchestration

Best practices for Kubernetes deployments and operations.

## When to Use

- Deploying applications to Kubernetes
- Writing or reviewing K8s manifests
- Setting up clusters and workloads

## Core Concepts

### Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:1.0.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
```

### Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP
```

### ConfigMap & Secrets

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  LOG_LEVEL: "info"
  MAX_CONNECTIONS: "100"
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  DATABASE_URL: "postgresql://user:pass@db:5432/app"
```

## Best Practices

- Use labels consistently
- Set resource requests and limits
- Implement health checks (liveness, readiness, startup probes)
- Use ConfigMaps and Secrets for configuration
- Implement horizontal pod autoscaling (HPA)
- Use namespaces for environment separation

## Resources

- [Kubernetes Docs](https://kubernetes.io/docs/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
