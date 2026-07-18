---
name: api-security
description: Design, review, test, or harden REST, GraphQL, RPC, webhook, OAuth, and gateway security. Use for API authentication, object/function/property authorization, schemas, abuse controls, SSRF, inventory, rate limits, tokens, or OWASP API risk review.
metadata:
  tags: ["api-security", "authorization", "oauth", "graphql", "abuse-prevention"]
---

# API Security

Secure the API as a set of business operations and data boundaries, not only endpoints. Confirm the actual protocol, identity provider, clients, trust zones, and deployment before selecting controls.

## Workflow

1. Inventory hosts, versions, routes/operations, methods, schemas, clients, owners, and data classifications.
2. Map authentication and authorization from actor to object, function, and returned properties.
3. Validate request parsing, content types, size, recursion/depth, and response serialization.
4. Trace outbound URLs, webhooks, redirects, file fetches, and internal network reachability.
5. Model abuse: enumeration, scraping, credential stuffing, expensive operations, workflow bypass, and resource exhaustion.
6. Review token/key lifecycle, storage, audience/issuer, rotation, revocation, and logging.
7. Verify findings with designated test identities and synthetic data.
8. Add regression tests, telemetry, and incident/recovery controls.

## Control Checklist

- deny by default at every object/function/property boundary;
- re-authorize each request server-side; never trust a client-supplied role/tenant;
- validate input against a bounded schema and reject unexpected fields where appropriate;
- return only explicitly allowed fields;
- use parameterized data access and contextual output encoding;
- bound pagination, filters, uploads, batch size, query complexity, time, and concurrency;
- apply abuse controls by identity, operation cost, and business risk, not IP alone;
- restrict outbound destinations and protect cloud/link-local metadata paths;
- verify webhook signatures, timestamp/replay window, and idempotency;
- avoid sensitive values in URLs, errors, metrics, traces, and logs;
- maintain version/inventory ownership and a retirement plan;
- make security failures observable without leaking policy details.

## OAuth and Tokens

Use current standards and provider guidance. Validate signature/algorithm, issuer, audience, expiry, and intended token type. Prefer short-lived, narrowly scoped credentials and supported authorization flows. Do not build custom cryptography or place bearer tokens in insecure browser storage.

## GraphQL/RPC

Authorization belongs in resolved business operations, not only the top-level route. Bound depth, aliases, batching, input size, and resolver cost. Prevent introspection changes from being mistaken for authorization.

## Output

Return the API inventory/boundaries, confirmed findings with evidence, missing controls, abuse cases, prioritized remediation, regression tests, telemetry, and coverage limits.

Read [references/detailed-guide.md](references/detailed-guide.md) only for relevant examples. Verify current categories and controls against the [OWASP API Security Project](https://owasp.org/www-project-api-security/) and protocol/provider specifications.
