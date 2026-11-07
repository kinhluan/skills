# JVM Runtime and Framework Upgrades

**Status checked 2026-11-07.** These dates change; re-verify before planning.

| Source | URL |
|---|---|
| Oracle Java SE roadmap | https://www.oracle.com/java/technologies/java-se-support-roadmap.html |
| Adoptium (Temurin) | https://adoptium.net/support |
| Quarkus releases | https://quarkus.io/releases |
| Vert.x 5 migration guide | https://vertx.io/docs/guides/vertx-5-migration-guide/ |
| Any product | `curl -s https://endoflife.date/api/v1/products/<name>` |

## Java

| LTS | Status in Nov 2026 |
|---|---|
| 8, 11 | Legacy. Vendor extended support only; plan exit |
| 17 | Oracle Premier Support ended Sep 2026; OpenJDK vendor builds still updated |
| 21 | Supported. Temurin at least to Dec 2029. Oracle JDK 21 updates released after Sep 2026 are under the OTN licence, which is not free for production |
| 25 | Current LTS (Sep 2025). Temurin at least to Sep 2031; Oracle Premier to Sep 2030 |
| 29 | Next planned LTS, Sep 2027 |

- Ship an **OpenJDK build** (Temurin, Corretto, Red Hat, Zulu) unless you have an Oracle licence. Record the vendor in the SBOM.
- Upgrade one LTS at a time: compile and test on the target JDK in CI *before* changing the production runtime.
- Common breakages:
  - Strong encapsulation of JDK internals (JDK 17): look for `--add-opens` in old start scripts.
  - Security Manager deprecated (JDK 17) and permanently disabled (JDK 24).
  - Warnings for `sun.misc.Unsafe` memory-access methods (JDK 24).
  - Dynamic agent loading warnings (JDK 21+).
  - Libraries that read the Java version with brittle parsing.
- Upgrade bytecode tools before the JDK: ByteBuddy, ASM, Mockito, Lombok, Jacoco, Error Prone, and the build plugins.

Automate source changes with OpenRewrite:

```bash
mvn -U org.openrewrite.maven:rewrite-maven-plugin:run \
  -Drewrite.recipeArtifactCoordinates=org.openrewrite.recipe:rewrite-migrate-java:RELEASE \
  -Drewrite.activeRecipes=org.openrewrite.java.migrate.UpgradeToJava21   # or UpgradeToJava25
```

Review the diff like any other PR. Recipes handle mechanical changes, not behaviour.

## Quarkus

LTS releases come every 6 months, each with 12 months of community maintenance. Non-LTS minors ship every 4–6 weeks.

| LTS | Released | Community maintenance ends |
|---|---|---|
| 3.40 | 2026-09-30 | 2027-09-30 (current recommended) |
| 3.33 | 2026-03-25 | 2027-03-25 |
| 3.27 | 2025-09-24 | **Ended** 2026-09-24 (Red Hat/IBM enterprise to 2027-12-31) |
| 3.20 | 2025-03-26 | **Ended** 2026-03-28 |
| 3.15 | 2024-09-25 | **Ended** 2025-09-25 |

Quarkus 4.0 was planned for 2026-11-25. Expect a major migration; wait for the first 4.x LTS unless you need a 4.0 feature.

Upgrade path:

1. Move to the newest **3.x LTS** first. Jumping LTS to LTS is supported by the update tool:
   ```bash
   quarkus update --stream=3.40          # Quarkus CLI
   ./mvnw io.quarkus.platform:quarkus-maven-plugin:3.40.1.1:update -N -Dstream=3.40   # Maven, no CLI needed
   ```
   `quarkus update` applies OpenRewrite recipes for the versions crossed.
2. Read the migration guide for every minor crossed (on the Quarkus GitHub wiki), especially for configuration renames and extension splits.
3. Run the full test suite in JVM *and* native mode if you ship native images.
4. Keep the Quarkus BOM as the single source of extension versions; do not pin Quarkus-managed libraries separately unless you are applying a documented CVE override.

## Vert.x

- **4.x:** only the **4.5** line is maintained. 4.4 ended at 4.4.9, so any 4.4.x is unpatched; move to the latest 4.5.x at once (low risk). The Vert.x project says 4.x gets bug-fix releases officially until **April 2027**.
- **5.x:** current (5.2.x in Nov 2026). The minimum JDK is 11; run it on 21 or 25.

Migration 4 → 5, in order:

1. Upgrade to the latest **4.5.x** and compile with deprecation warnings on. Many 5.x APIs exist in 4.5 as deprecated bridges; fix those warnings first.
2. Replace **callbacks with futures** everywhere. Vert.x 5 removed callback overloads, and they were *not* deprecated in 4.x, so search for `Handler<AsyncResult<` parameters. `executeBlocking` takes a `Callable`.
3. Replace removed modules:

   | Removed | Replacement |
   |---|---|
   | Vert.x Sync | Virtual threads (`ThreadingModel.VIRTUAL_THREAD`) |
   | Service Factories | Explicit deployment |
   | Vert.x Web OpenAPI | Web OpenAPI Router |

   Plan replacements for components sunsetting in 6:

   | Sunsetting | Replacement |
   |---|---|
   | RxJava 2 | Mutiny or RxJava 3 |
   | OpenTracing | OpenTelemetry |
   | gRPC Netty | Vert.x gRPC |
   | JDBC API | SQL client for JDBC |
   | Service Discovery | Service Resolver |
   | Vert.x Unit | Vert.x JUnit 5 |
4. Adapt builders and options:
   - `Vertx.builder()…buildClustered()`
   - `PoolOptions` for HTTP client pools
   - `setIdleTimeout` instead of `setTimeout`
   - SQL `PgBuilder.pool()…` / `MySQLBuilder.pool()…`
   - `DeploymentOptions#setThreadingModel` instead of `setWorker`
5. Rewrite against new APIs where clients changed substantially: the RabbitMQ client was rewritten, Redis no longer forwards subscriptions to the event bus, and the WebSocket client moved to `createWebSocketClient()`.
6. Re-baseline metrics dashboards, because several Micrometer tag names changed.

For a large codebase built on a custom base class (such as a shared `AbstractVerticle` subclass), migrate the base class and its helpers first behind the 4.5 deprecated bridges, then services in batches.

## Spring Boot and Others

Check `endoflife.date` for `spring-boot`, `spring-framework`, `hibernate`, `kafka`, `nodejs`, `python`, and your database. Apply the same pattern: newest patch first, then a supported minor, then majors with the official migration guide and OpenRewrite recipes where they exist.
