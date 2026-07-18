---
name: container-security
description: Review or harden container images, runtimes, Kubernetes workloads, clusters, registries, and software supply chains. Use for Docker/Kubernetes security, image scanning, provenance, admission policy, RBAC, secrets, network policy, or runtime detection.
metadata:
  tags: ["container-security", "kubernetes-security", "supply-chain", "runtime", "hardening"]
---

# Container Security

Trace trust from source and build identity to artifact, deployment policy, runtime privileges, network/data access, and detection. A clean vulnerability scan is not proof of a secure workload.

## Workflow

1. Define cluster/workload scope, data sensitivity, tenants, threat actors, and availability constraints.
2. Inventory source, builder, base image, registry, digest, SBOM, signature/provenance, deployment, service account, and runtime.
3. Review build and dependency integrity.
4. Review image content and configuration.
5. Review workload identity, privileges, filesystem, resources, secrets, and network.
6. Review cluster RBAC, admission, tenancy, control-plane/node posture, and audit.
7. Correlate vulnerability reachability and exploitability with runtime exposure.
8. apply the smallest safe remediation and verify deployment/recovery.

## Image and Supply Chain

- pin base images and deployment artifacts by digest where reproducibility requires it;
- use maintained minimal bases appropriate to debugging/operations;
- build in isolated, least-privileged builders;
- keep credentials out of layers, history, build args, and logs;
- produce an SBOM and verifiable provenance;
- sign/attest artifacts and enforce trusted identities at admission;
- rebuild regularly rather than patching running containers;
- define policy for severity, reachability, fix availability, exceptions, and expiry.

## Workload

- run as a non-root UID/GID and disallow privilege escalation;
- drop capabilities and add only those proven necessary;
- use read-only root filesystem and explicit writable mounts when feasible;
- avoid privileged mode, host namespaces, host paths, device access, and Docker/container runtime sockets;
- set CPU/memory/ephemeral-storage requests and limits based on workload behavior;
- use dedicated service accounts with narrow RBAC;
- mount short-lived secrets only where needed and prevent log/env leakage;
- restrict ingress and egress from observed communication needs;
- use seccomp/AppArmor/SELinux or platform-equivalent controls.

## Cluster and Runtime

Enforce current Kubernetes Pod Security Standards or a stronger organization policy. Separate tenant boundaries, protect admission/control-plane access, encrypt sensitive cluster data with managed key controls, log privileged/API actions, and detect drift or suspicious runtime behavior.

Do not paste generic hardening YAML over a workload without checking its platform/version and operational requirements. Test startup, probes, scaling, upgrades, debugging, and rollback after hardening.

## Output

Return scope/threats, artifact chain, confirmed findings, policy gaps, prioritized remediation, deployment verification, exception owners/expiry, and residual risk.

Read [references/detailed-guide.md](references/detailed-guide.md) only for relevant examples. Verify commands and API versions against current Docker, Kubernetes, cloud, and tool documentation.
