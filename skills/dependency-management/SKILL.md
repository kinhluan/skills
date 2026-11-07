---
name: dependency-management
description: Keep libraries, frameworks, and runtimes current and free of exploitable vulnerabilities. Use when inventorying dependencies or generating an SBOM, checking end-of-life status, planning a framework or runtime upgrade (Java, Quarkus, Vert.x, Spring, Node, Python, Go), configuring Renovate or Dependabot, triaging a CVE or scanner report, writing a VEX statement, or deciding whether a vulnerable dependency is actually exploitable.
metadata:
  tags: ["dependencies", "sbom", "cve", "vulnerability-management", "upgrades", "end-of-life", "supply-chain", "renovate"]
---

# Dependency Management

Every dependency is code you ship but did not write. Manage it as a portfolio: know what you run, keep it on supported versions, and fix the vulnerabilities that can actually hurt you first. Version and support dates change monthly, so verify every lifecycle claim against the vendor page or `endoflife.date` on the day you use it.

## 1. Inventory

You cannot patch what you cannot list.

1. Commit lockfiles: `package-lock.json`/`pnpm-lock.yaml`, `uv.lock`/`poetry.lock`, `go.sum`, Gradle lockfiles, the Bazel `maven_install.json`. For Maven, pin plugin and dependency versions and use a BOM.
2. Generate an **SBOM** per deployable artifact, in CycloneDX or SPDX. Generate it from the built artifact or image as well as from source, since the image adds OS packages.
3. Record the **runtime** too: JDK vendor and version, Node, Python, the base image, and the database and broker versions.
4. Separate runtime, build-only, and test-only dependencies. A test-only CVE rarely ships.

Commands for each ecosystem are in [ecosystems](references/ecosystems.md).

## 2. Lifecycle and Upgrade Policy

| Rule | Why |
|---|---|
| Stay on a **supported line**, preferring LTS, with at least 6 months of support left | Security fixes stop at end of life, often without notice |
| Upgrade continuously in small steps (patch weekly, minor monthly) | Large jumps hide breakage and stall forever |
| Track major upgrades as roadmap items with an owner and a date | Majors need code changes, not just a version bump |
| Know the licence of the runtime build you ship | Some vendor JDK builds change licence terms by update |
| Remove unused dependencies before upgrading them | Each one removed is attack surface and upgrade work eliminated |

Framework migration paths (Java LTS, Quarkus LTS, Vert.x 4 → 5, Spring Boot, OpenRewrite automation) are in [jvm-upgrades](references/jvm-upgrades.md).

### Automated updates

- Use **Renovate** or **Dependabot** with **grouping**: framework families together (`io.quarkus*`, `io.vertx*`, `@angular/*`), and patch and minor updates grouped weekly.
- Auto-merge patch updates only when CI has real tests, the package is mature, and a short **minimum release age** (for example 3 days) has passed. The wait lets yanked or malicious releases surface first.
- Majors get a separate PR, never auto-merge, and need a migration note.
- Pin GitHub Actions and container base images by **digest/SHA**, and let the bot update the pin. Moved tags have shipped malware, as in the 2026 `trivy-action` tag compromise (CVE-2026-33634).

## 3. Vulnerability Triage

A scanner report is a lead list, not a backlog. For each finding, answer in this order:

1. **Is it in what we ship?** Runtime classpath, the image, or the bundle, rather than test or build tooling only.
2. **Is the vulnerable code reachable?** Do we call the affected function, enable the affected feature, or parse untrusted input with it? Reachability tools include `govulncheck`, and some SCA products support Java and JavaScript.
3. **Is it being exploited?** Check **CISA KEV**, which lists known exploited vulnerabilities, and the **EPSS** probability score from FIRST. CVSS measures severity, not likelihood.
4. **What is the exposure?** An internet-facing service handling untrusted input outranks an internal batch job.
5. **What is the fix path?** A patch release, a backport, a configuration mitigation, or replacing the library.

| Signal | Action |
|---|---|
| In CISA KEV, reachable, and exposed | Emergency: patch or mitigate now; check for compromise |
| High EPSS or a public exploit, and reachable | Next release, within days |
| Reachable, low EPSS, not in KEV | Normal upgrade cadence |
| Not reachable, or not shipped | Record a **VEX** `not_affected` statement with its justification; upgrade on cadence |
| No fix available | Mitigate (configuration, WAF rule, input validation, isolation), record a time-limited exception, and watch for a release |

Data sources: OSV.dev (aggregates GHSA, PyPA, Go, RustSec, and more), GitHub Advisories, the NVD (its analysis backlog means some CVEs have no CPE or score for weeks), vendor advisories, and the CISA KEV catalog. Prefer OSV or GHSA to NVD-only matching for libraries, because CPE matching produces false positives and misses.

### Write it down

- **VEX** (OpenVEX, CycloneDX VEX, or CSAF) for each `not_affected` decision: product, CVE, status, justification, and author.
- **Exceptions** carry an owner, a reason, a compensating control, and an **expiry date**. An exception without an expiry becomes permanent.
- After an emergency, add a regression check: a pinned minimum version in the build, or a policy rule.

## 4. Supply Chain Hygiene

- Resolve packages only from trusted registries. Use a proxy or mirror, such as Nexus or Artifactory, with **namespace scoping** to prevent dependency confusion with internal package names.
- Verify integrity: lockfile hashes, `npm ci`, `pip install --require-hashes`, Maven checksum policy, and Sigstore or cosign for images and artifacts where available.
- Review new direct dependencies: maintenance, maintainers, install scripts, transitive size, and licence.
- Disable install scripts by default in CI where the ecosystem allows it.

## Output

For an assessment, return:

1. **Inventory**: artifacts, runtimes, and their SBOM location.
2. **Lifecycle table**: component, current version, supported line, end-of-life date (with source and date checked), and target version.
3. **Vulnerability decisions**: CVE, component, reachable (yes/no/unknown), KEV, EPSS, exposure, decision, and owner.
4. **Upgrade plan**: ordered steps, the migration risk for each, and the tests that prove it.
5. **Policy gaps**: missing lockfiles, unpinned actions, no automated updates, exceptions without expiry.

## Related Skills

- [security-analysis](../security-analysis/SKILL.md) for code-level vulnerabilities and the security tooling pipeline.
- [container-security](../container-security/SKILL.md) for base images and image scanning.
- [code-quality-gate](../code-quality-gate/SKILL.md) for wiring scans into CI as gates.
- [evolutionary-architecture](../evolutionary-architecture/SKILL.md) for fitness functions that enforce version policy.
