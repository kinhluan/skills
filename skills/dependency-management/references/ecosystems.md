# Commands by Ecosystem

Check tool versions before relying on flags; these were verified in November 2026 (Maven 3.10, versions-maven-plugin 2.18.0, cyclonedx-maven-plugin 2.9.1). Pin plugin versions in CI instead of resolving `LATEST`.

## Cross-Ecosystem

| Task | Command |
|---|---|
| Scan a repo for known vulnerabilities | `osv-scanner scan source -r .` |
| Scan a container image | `osv-scanner scan image <image>` or `grype <image>` |
| SBOM from an image or directory | `syft <image-or-dir> -o cyclonedx-json > sbom.json` |
| Scan an existing SBOM | `grype sbom:./sbom.json`, or `osv-scanner scan source -L bom.cdx.json` (OSV-Scanner recognises SBOMs by name, such as `*.cdx.json` or `*.spdx.json`) |
| One package, from a script | `curl -s https://api.osv.dev/v1/query -d '{"package":{"purl":"pkg:maven/io.vertx/vertx-core@4.4.0"}}'` |
| Exploit probability | `curl -s "https://api.first.org/data/v1/epss?cve=CVE-2021-44228"` |
| Known exploited? | Search the CISA KEV feed `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` for the `cveID` |
| End-of-life dates | `curl -s https://endoflife.date/api/v1/products/<product>` (e.g. `quarkus-framework`, `spring-boot`, `eclipse-temurin`, `nodejs`, `python`) |

Query OSV by **purl** (`pkg:<type>/<namespace>/<name>@<version>`). It avoids ecosystem and name-format mistakes that silently return zero results.

## Maven

```bash
mvn -B dependency:tree -Dscope=runtime                      # what actually ships
mvn -B org.codehaus.mojo:versions-maven-plugin:2.18.0:display-dependency-updates
mvn -B org.codehaus.mojo:versions-maven-plugin:2.18.0:display-plugin-updates
mvn -B org.cyclonedx:cyclonedx-maven-plugin:2.9.1:makeAggregateBom -DoutputFormat=json   # target/bom.json
mvn -B org.owasp:dependency-check-maven:check -DnvdApiKey="$NVD_API_KEY"
```

- Use `-DprocessDependencyManagement=false` on `display-dependency-updates` to hide BOM-managed noise.
- Import the framework BOM (`quarkus-bom`, `vertx-stack-depchain`, `spring-boot-dependencies`) and override a transitive version only in `<dependencyManagement>`, with a comment that links the CVE and a removal condition.
- Fail the build on banned versions with `maven-enforcer-plugin` `bannedDependencies` (for example `log4j-core:[,2.17.1)`).
- OWASP Dependency-Check works without an NVD API key, but updates are very slow; request a free key and cache the data directory in CI.

## Gradle

```bash
./gradlew dependencies --configuration runtimeClasspath
./gradlew dependencyInsight --dependency jackson-databind --configuration runtimeClasspath
./gradlew dependencyUpdates          # com.github.ben-manes.versions plugin
./gradlew cyclonedxBom               # org.cyclonedx.bom plugin
```

Enable `dependencyLocking { lockAllConfigurations() }` and commit the lockfiles. Use version catalogs (`libs.versions.toml`) so the bot updates one place.

## Bazel (`rules_jvm_external`)

```bash
bazel run @maven//:outdated                          # replace `maven` with your repository name
RULES_JVM_EXTERNAL_REPIN=1 bazel run @maven//:pin    # re-pin after changing artifacts
bazel query 'deps(//service:app)' --output=label | grep '@maven//'
```

The pinned `maven_install.json` is the lockfile. Scan it with OSV-Scanner, or generate an SBOM from the built deploy JAR or image, since Bazel graphs can differ from the Maven coordinates you declared.

## Node.js (npm or pnpm)

```bash
npm ci                                   # lockfile-exact install
npm outdated
npm audit --omit=dev                     # runtime dependencies only
npm sbom --sbom-format cyclonedx > sbom.json
pnpm outdated -r && pnpm audit --prod
```

Use `overrides` (npm) or `pnpm.overrides` for a transitive fix, with a comment linking the advisory. Set `ignore-scripts=true` in CI `.npmrc` and allow specific packages that need build scripts.

## Python

```bash
uv lock --upgrade-package <name>        # targeted upgrade
uv tree --outdated
uvx pip-audit                           # or: pip-audit -r requirements.txt
```

Use `--require-hashes` for `pip install` from requirements files in production builds.

## Go

```bash
go list -m -u all                      # available updates
govulncheck ./...                      # reachability-aware: reports only called vulnerable symbols
go mod tidy && go mod verify
```

`govulncheck` is the reference example of reachability analysis: a module-level hit with no call path is reported separately as informational.

## Containers and OS Packages

- Rebuild images on a schedule even without code changes, so base-image patches land.
- Pin base images by digest (`FROM eclipse-temurin:25-jre@sha256:...`) and let Renovate bump the digest.
- Prefer minimal or distroless runtime images; fewer packages means fewer findings to triage.
