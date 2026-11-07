# Payment Security and Compliance

Status checked 2026-11-07. PCI DSS v4.0.1 is the current standard; PCI SSC opened feedback on the next version in June 2026. Verify the current version, the SAQ you qualify for, and your acquirer's and local regulator's rules with your QSA or compliance team.

## Card Data and PCI DSS Scope

The cheapest PCI control is never touching card data.

| Integration | Card data reaches your servers? | Typical validation |
|---|---|---|
| Redirect to a hosted payment page | No | SAQ A (merchant) |
| Provider iframe or hosted fields | No, but your page hosts the iframe | SAQ A, subject to its script-security eligibility criteria |
| Provider JavaScript that posts directly to the provider | No, but your page controls the script | SAQ A-EP |
| Your API receives the PAN | **Yes** | SAQ D or an onsite assessment (ROC) |

- **Payment page scripts.** Requirements 6.4.3 (inventory, authorise, and integrity-check every script on the payment page) and 11.6.1 (detect unauthorised changes to the page and its HTTP headers) were mandatory from 31 March 2025. For SAQ A, PCI SSC moved them into an eligibility criterion: the merchant must confirm the site is not susceptible to script attacks that could affect the payment page. Use a strict CSP, Subresource Integrity where scripts are static, an approved script inventory, and change monitoring, whatever SAQ applies.
- **If you must store a PAN:** render it unreadable (strong cryptography with managed keys, or tokenisation), mask it on display (at most the first 6 and last 4 digits), keep keys separate from data, and restrict and log access.
- **Never store** sensitive authentication data after authorisation (full track data, CVV2/CVC2, PIN or PIN block), even encrypted.
- Use **network tokens** or provider tokens for card-on-file. Tokens are scoped to a merchant, so a stolen token cannot be used elsewhere.
- Keep the **cardholder data environment** small and segmented. Logs, analytics, error trackers, and support tools are the usual leaks, so scrub PANs at ingestion with Luhn-aware detectors.

## Authentication and Authorisation

- Use **strong customer authentication** for payments and sensitive changes: 3-D Secure 2 for cards, and app-based or biometric confirmation for wallets.
- Require step-up re-authentication for risky operations: adding a payout destination, changing the phone number or e-mail, raising limits, first payment to a new payee, large amounts, or a new device.
- **Bind authorisation to the transaction.** The confirmation must cover the amount, currency, and payee that will execute, so that the user does not approve one thing while the system does another.
- Check object-level access on every resource (payment, refund, payout, statement): `payment.merchant_id == caller.merchant_id`. Broken object-level authorisation is the most common payment API flaw.
- Separate duties: whoever can create a payout cannot also approve it. Require two-person approval for manual ledger adjustments.

## Fraud and Abuse Controls

- Apply velocity and amount limits per user, device, card or instrument, IP, payee, and merchant, over several windows.
- Enforce limits server-side, inside the same transaction as the spend, because a client-side or cache-only check races.
- Watch for promotion and referral abuse, refund abuse, card testing (many small authorisations), account takeover, and mule accounts.
- Score risk before money moves. Decide approve, step-up, review, or decline, and log the decision with its reasons.
- Run AML/KYC screening and reporting hooks according to licence and jurisdiction, owned by compliance.

## Integrity of Messages and Keys

- Sign outbound requests and verify inbound ones as each provider specifies: HMAC, RSA or ECDSA signatures, or mTLS. Verify over the raw bytes, compare in constant time, and enforce timestamp and nonce windows against replay.
- Keep signing and encryption keys in an HSM or cloud KMS. Rotate them on schedule and immediately on suspicion. Never put them in configuration repos or images.
- Pin provider endpoints and certificates as the provider documents. Do not disable TLS verification in any environment that can reach production data.

## Audit and Operations

- Keep an append-only audit trail of who did what, when, from where, on which resource, and with what before and after state. Cover admin actions, manual adjustments, limit changes, and key operations.
- Make it tamper-evident: write-once storage, hash chaining, or a separate account and team.
- Alert on `UNKNOWN` backlog, reconciliation breaks, refund spikes, failed signature checks, authorisation failures by merchant, and ledger invariant violations.
- Run incident runbooks for provider outages (switch or queue), double-charge reports (find by `provider_ref`, compensate through a journal), and suspected key compromise.

## Threats to Model

Run [threat-modeling](../../threat-modeling/SKILL.md) on each money flow. Cover at least:

- replayed or forged webhooks and requests
- races between concurrent spends, refunds, and payouts
- amount or currency tampering between quote and confirm
- payee substitution
- negative or zero amounts and integer overflow
- rounding exploitation over many small transactions
- insider manual adjustments
- leaks of card data or tokens through logs
