# Java and JVM Security Review (Quarkus, Vert.x, Spring)

The XML, deserialization, and Jackson examples below were run on JDK 21.0.6 with jackson-databind 2.20.1.

## Deserialization

**Native Java serialization** (`ObjectInputStream`) of untrusted bytes is remote code execution through gadget chains in the classpath. Replace it with a data format (JSON or Protobuf) bound to explicit types. If it cannot be removed yet, install an allow-list filter (JEP 290 / JEP 415):

```java
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.example.dto.*;java.lang.String;maxdepth=5;maxrefs=1000;maxbytes=100000;!*");
ois.setObjectInputFilter(filter);   // or JVM-wide: -Djdk.serialFilter=...
```

Look for `ObjectInputStream`, `XMLDecoder`, XStream without an allow list, SnakeYAML `new Yaml()` on untrusted input (use `SafeConstructor`; SnakeYAML 2.x is safe by default), Kryo or Hessian with registration disabled, and Java serialization over JMX, RMI, or caches and session replication.

**Jackson polymorphic typing** turns JSON into an object-instantiation primitive:

```java
// UNSAFE: any class name in the JSON is instantiated
mapper.activateDefaultTyping(mapper.getPolymorphicTypeValidator(), DefaultTyping.JAVA_LANG_OBJECT);
mapper.enableDefaultTyping();                 // deprecated, same problem
@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)    // on a field typed Object or Serializable

// SAFE: explicit subtypes, or a validator that allow-lists them
@JsonTypeInfo(use = JsonTypeInfo.Id.NAME) @JsonSubTypes({@Type(value = Card.class, name = "card")})
mapper.activateDefaultTyping(
    BasicPolymorphicTypeValidator.builder().allowIfSubType(PaymentMethod.class).build(),
    DefaultTyping.NON_FINAL);
```

Also keep `FAIL_ON_UNKNOWN_PROPERTIES` enabled at trust boundaries; it is the default, and it catches mass assignment. Use separate request DTOs instead of binding JSON directly onto entities.

## XML: XXE and Entity Expansion

The JDK's default `DocumentBuilderFactory` **resolves external entities**. In the test, a `file://` entity leaked a local file. Harden every factory: `DocumentBuilderFactory`, `SAXParserFactory`, `XMLInputFactory`, `TransformerFactory`, `SchemaFactory`, and `XMLReader`.

```java
DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
f.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);  // strongest: reject DOCTYPE
f.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
f.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
f.setAttribute(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");
f.setXIncludeAware(false);
f.setExpandEntityReferences(false);

XMLInputFactory x = XMLInputFactory.newFactory();                 // StAX
x.setProperty(XMLInputFactory.SUPPORT_DTD, false);
x.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
```

Check SOAP clients, SAML libraries, document converters, and `jackson-dataformat-xml` (Woodstox) configuration as well.

## Injection Sinks

| Sink | Unsafe | Safe |
|---|---|---|
| JDBC | `"... WHERE id = " + id` | `PreparedStatement` with `?`; identifiers through an allow list |
| JPA / Hibernate | String-built HQL/JPQL, `createNativeQuery(concat)` | Named parameters `:id`, Criteria API, Panache `find("email", email)` |
| Vert.x SQL client | `client.query("..." + x)` | `client.preparedQuery("... WHERE id = $1").execute(Tuple.of(id))` (`?` on MySQL) |
| Expression languages | SpEL, OGNL, MVEL, JEXL, or EL evaluated on user input | Never evaluate user input; use a `SimpleEvaluationContext` for SpEL if unavoidable |
| JNDI | `ctx.lookup(userInput)` | Never look up user-controlled names; keep Log4j 2 at least 2.17.1 (Log4Shell, CVE-2021-44228) |
| Templates | User-controlled template source (Freemarker, Velocity, Qute) | Only fixed templates; restrict Freemarker `?api` and `new` built-ins |
| OS commands | `Runtime.exec(String)` with concatenation | `ProcessBuilder(List.of(...))` with a fixed binary and validated arguments |
| Paths | `new File(base, userName)` | Normalise, then `resolved.startsWith(base)` with `toRealPath()`; reject `..` |
| Logs | Logging raw user input | Structured logging; strip CR/LF; never log secrets, tokens, or PANs |

## Quarkus

- **Deny by default:** `quarkus.security.jaxrs.deny-unannotated-endpoints=true`, which defaults to false. Every resource then needs `@RolesAllowed`, `@PermitAll`, or `@Authenticated`.
- Path policies (`quarkus.http.auth.permission.<name>.paths/policy/methods`) are evaluated **before** annotations, so `@PermitAll` cannot open a path that a policy denies. Review both together.
- OIDC and JWT (`quarkus-oidc`, `smallrye-jwt`): verify the issuer and audience (`mp.jwt.verify.issuer`, `mp.jwt.verify.audiences`). Never disable token verification in a production profile.
- Check `%prod` profile values for `quarkus.http.cors.origins` (no `*` with credentials), the Dev UI and dev services, Swagger UI (`quarkus.swagger-ui.always-include`), management endpoint exposure, and secrets in `application.properties` committed to git.
- `@Blocking` and `@NonBlocking` misuse can starve the event loop, which becomes a denial of service under load.

## Vert.x

- **Body size:** always add `BodyHandler.create().setBodyLimit(<bytes>)` sized for the route. Set upload directory permissions and `setDeleteUploadedFilesOnEnd(true)`.
- **Never block the event loop** (JDBC, file I/O, crypto, or `Thread.sleep` in a handler). Use `executeBlocking`, worker verticles, or virtual threads. One blocked loop stalls every connection on it.
- **Authorization:** routes are open unless a handler protects them. Mount `AuthenticationHandler` and `AuthorizationHandler` before business handlers, and check object ownership inside the handler.
- **CORS** with an explicit origin list (`CorsHandler.create().addOrigin(...)`); avoid `*` with credentials. Use `CSRFHandler` for cookie sessions; `SessionHandler` with secure, HttpOnly, SameSite cookies; and `HSTSHandler`.
- **Event bus:** messages from bridged clients (SockJS bridge) are untrusted. Configure `inboundPermitteds` and `outboundPermitteds` narrowly, and never bridge internal addresses.
- `StaticHandler`: do not serve from a directory containing configuration or keys; in Vert.x 5, configure the root at creation.

## Spring

- Actuator: expose only `health` and `info` publicly; protect `env`, `heapdump`, `configprops`, `mappings`, and `loggers` (they leak secrets or allow reconfiguration).
- Spring Security: `authorizeHttpRequests` rules are ordered, so put the most specific first and end with `.anyRequest().authenticated()`. Method security uses `@PreAuthorize`.
- Data binding on entities (`@ModelAttribute`) allows mass assignment; use DTOs or `@InitBinder` allowed fields.
- SpEL in `@Value`, `@PreAuthorize`, or Spring Cloud routing must never include user input.

## Crypto and Randomness

- `SecureRandom` for tokens, ids, and nonces, never `java.util.Random` or `Math.random()`.
- `Cipher.getInstance("AES/GCM/NoPadding")` with a unique 12-byte IV per message; never `"AES"` alone (which means ECB) or a static IV.
- Passwords: Argon2id or bcrypt (Spring Security `Argon2PasswordEncoder`/`BCryptPasswordEncoder`, or `de.mkammerer:argon2-jvm`), never a plain SHA-256.
- Compare MACs and tokens with `MessageDigest.isEqual`, which is constant-time, not `equals`.
- Never install a trust-all `TrustManager` or `HostnameVerifier`, including "temporarily" in non-production code that can be promoted.

## Search Patterns

```bash
rg -n 'ObjectInputStream|XMLDecoder|enableDefaultTyping|activateDefaultTyping|Id\.CLASS' --type java
rg -n 'DocumentBuilderFactory|SAXParserFactory|XMLInputFactory|TransformerFactory' --type java
rg -n 'createQuery\(.*\+|createNativeQuery\(.*\+|\.query\(".*\+' --type java
rg -n 'Runtime\.getRuntime\(\)\.exec|new ProcessBuilder' --type java
rg -n 'X509TrustManager|HostnameVerifier|setHostnameVerifier|TrustAll' --type java
rg -n 'new Random\(|Math\.random' --type java
rg -n 'deny-unannotated-endpoints|cors\.origins|swagger-ui\.always-include' -g '*.properties' -g '*.yaml'
```

These patterns find candidates; confirm each with data-flow reasoning or a SAST rule before reporting it.
