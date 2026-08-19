---
name: web-endpoint-documenter
description: "Explore an authorized URL with headless Chrome DevTools/CDP, build a bounded SPA state-and-action graph, capture and classify browser traffic, optionally harvest browser-loaded static evidence, and run a guarded security-assessment mode with test principals and synthetic data. Produce evidence-aware Markdown, OpenAPI, or GraphQL endpoint documentation for REST, GraphQL, RPC, streaming, form, pagination, authentication, authorization, and request/response behavior without native GUI automation or direct HTTP crawling."
---

# Web Endpoint Documenter

Turn a user-authorized URL into a reproducible, evidence-backed Markdown description of the network contracts observable from the page.

## Boundaries

- Use headless Chrome DevTools/CDP tools only. Do not use native GUI automation, direct HTTP crawling, filesystem source downloads, or alternate browser automation unless the user explicitly changes the constraint.
- Keep the default mode `observe`: capture browser behavior without active probing or mutation. Allow `harvest` only for browser-mediated inspection of resources the page actually loads. Allow `probe` only after explicit authorization for a safe, read-only target or test environment. Allow `assess` only with explicit authorization, a defined target scope, test principals, synthetic canary data, and an allowlisted probe plan.
- Inspect only targets the user is authorized to analyze. Never bypass authentication, bot controls, paywalls, rate limits, origin policy, or access controls.
- Treat `GET`, `HEAD`, and `OPTIONS` as safe to observe. Do not submit forms or invoke `POST`, `PUT`, `PATCH`, `DELETE`, payments, account changes, uploads, or other mutations unless the user explicitly authorizes that action and it is clearly safe in the target environment.
- Redact cookies, authorization values, API keys, CSRF tokens, personal data, and secret-looking query/body values. Preserve header names and explain authentication requirements without emitting credentials.
- Never bypass authentication, authorization, anti-bot controls, or frontend guards. Never downgrade or strip live credentials, inject privileged fields into real records, or probe production state-changing endpoints by default.
- Do not claim backend completeness. Report the explored state/action surface, observed requests, static candidates, excluded actions, blocked paths, and remaining unknowns.

## Evidence modes

Record the selected mode in the report:

- **Observe**: default. Capture navigation, visible non-destructive interactions, request/response events, console errors, and stream messages.
- **Harvest**: opt-in. Inspect only browser-loaded script, module, manifest, and source-map resources through the browser/CDP layer when the tool exposes their bodies. Treat route strings, client code, and schemas as `static-candidate` evidence until dynamically confirmed.
- **Probe**: explicit opt-in. Perform narrowly bounded, authorized read-only probes such as GraphQL introspection or controlled header-necessity tests. Do not probe live mutations, credentials, access controls, or anti-bot defenses.
- **Assess**: explicit security-assurance mode. Require an authorized test/staging target, test principals and expected policy matrix, synthetic canary objects, a request/parameter allowlist, rate limits, and stop conditions. Compare server behavior across principals and controlled inputs; do not claim a vulnerability from a single response difference.

Never use a static candidate or an inferred template as proof that an endpoint is callable. Never call a generated specification production-ready solely because it was derived from browser evidence.

## Establish the exploration contract

Before browsing, resolve or state defaults for:

1. Starting URL and whether redirects may be followed.
2. Allowed origins: same-origin by default; label first-party subdomains and third-party traffic separately.
3. Authentication state: public session or an already-authorized browser profile. Never request secrets in chat.
4. Interaction budget: default to the initial load plus visible, non-destructive controls, with bounded depth, actions, and wait time.
5. Evidence mode: default `observe`; require explicit authorization for `harvest`, `probe`, or `assess`.
6. Mutation policy: default `observe-only`; require explicit opt-in for safe test mutations.
7. Output path and report name. Use a Markdown file unless the user requests another format.
8. For `assess`, record authorization, environment, principals, tenants, synthetic objects, expected authorization matrix, allowlisted probes, request budget, and stop conditions before browsing.

If a missing choice materially changes safety or coverage, ask one focused question before acting. Otherwise use the defaults above and record them in the report.

## Explore with Chrome DevTools

Use the `chrome-devtools` workflow:

1. List and select the target page, navigate to the URL, and wait for load/settling signals.
2. Capture an initial accessibility snapshot. Record title, final URL, visible routes, forms, controls, pagination, dialogs, tabs, and stateful UI.
3. Build a state-and-action graph. Give each state a stable hash from URL/history, accessibility structure, relevant route/DOM state, and selected controls. Give each action an ID, source state, target state, and request window.
4. Discover candidate actions from fresh snapshots, DOM-observable links/forms/buttons/tabs, route changes, and resource entries. Queue them with bounded breadth/depth and stop revisiting equivalent state/action fingerprints.
5. Start network observation before each meaningful interaction. Associate requests, responses, WebSocket frames, SSE messages, console errors, and blocked requests with the triggering action and page state when the tools expose them.
6. Exercise visible, non-destructive paths systematically: navigation, tabs, accordions, search/filter controls, pagination, sorting, dialogs, login-state branches already available, and bounded scrolling/infinite lists.
7. Refresh or revisit a state when needed to distinguish initial-load traffic from interaction traffic. Avoid duplicate actions once their request behavior is established.
8. Use `evaluate_script` only for page-observable data needed to understand behavior, such as form values, route state, resource entries, or embedded configuration. Treat page JavaScript as evidence, not proof of a callable endpoint.
9. In `harvest` mode, inspect only resources observed as loaded by the page. Record resource URL, origin, hash, timestamp, and evidence location. Do not fetch arbitrary guessed assets or read source outside the browser boundary.
10. In `probe` mode, record the exact authorization, target environment, probe request, expected safety property, and result. Stop on an unexpected status, side effect, auth challenge, rate limit, or ambiguity.
11. In `assess` mode, execute only the predeclared allowlist. Capture the control request, test variant, principal/object context, response differential, and a fresh server-side state check. Stop on an unexpected side effect, real-user data, privilege change, rate limit, auth anomaly, or scope violation.

When a tool cannot expose a required request or response detail, mark it `unknown` and explain the limitation. Do not fill gaps from guesses or undocumented assumptions.

## Normalize and classify traffic

Deduplicate requests by:

```text
method + normalized URL + content type + normalized request shape
```

Normalize volatile path IDs, timestamps, cursors, cache busters, and opaque tokens only when the substitution is supported by repeated observations. Preserve one concrete redacted example and show the normalized template separately.

Classify each observed request as one of:

- document/navigation
- REST/resource endpoint
- GraphQL operation
- RPC/action endpoint
- form submission
- pagination/search/filter/sort request
- upload/download
- WebSocket or Server-Sent Events channel
- preflight or redirect
- static asset
- telemetry/advertising/third-party support traffic

Assign an evidence class to every candidate:

- `observed-dynamic`: captured during page navigation or an interaction;
- `observed-stream`: captured from a WebSocket or Server-Sent Events channel;
- `observed-error`: captured as an error response or browser failure;
- `static-candidate`: found in a browser-loaded resource but not confirmed by traffic;
- `inferred-template`: normalized from repeated observations with supporting evidence;
- `actively-probed`: confirmed or rejected by an explicitly authorized probe;
- `assess-signal`: a security-relevant behavioral differential found during an authorized assessment;
- `third-party`: outside the allowed first-party origin set;
- `blocked-or-unknown`: not exposed, not exercised, or ambiguous.

Keep static candidates and inferred templates out of the primary usable-endpoint count unless the report explicitly labels the count as broader discovery coverage.

Document the distinction between an endpoint observed in the browser and an endpoint demonstrated as safely replayable. A request that requires browser state, a signed URL, a short-lived token, or an opaque generated value is not automatically a generally usable API.

## Apply API contract analysis

For each substantive first-party endpoint, document:

- method, normalized URL, origin, protocol/classification, and trigger;
- observed status codes, content types, and redirect behavior;
- path, query, header, cookie, and body fields, with required/optional/unknown status;
- representative redacted request and response examples, bounded in size;
- response shape, entities, nullable fields, enums, links, and pagination metadata;
- filtering and sorting parameters, including defaults and stable ordering when observed;
- authentication, CSRF, permission, idempotency, cache, and rate-limit signals when observed;
- success, validation, authorization, not-found, conflict, throttling, and server-error behavior;
- replay notes, prerequisites, side effects, and confidence level.

Use HTTP semantics accurately: distinguish safe/idempotent methods from observed behavior, record `Location`, `Retry-After`, cache validators, rate-limit headers, and problem details when present. If an error resembles RFC 7807, identify `type`, `title`, `status`, `detail`, and `instance`; do not label a payload RFC 7807-compliant unless the evidence supports it. For list endpoints, document cursor/limit or offset/limit behavior plus explicit filter and sort fields when observed. Never invent pagination, versioning, HATEOAS, or idempotency guarantees.

For GraphQL, record endpoint URL, operation name, operation type, variables shape, selected fields, response envelope, error array, and whether persisted queries or batching were observed. For WebSockets/SSE, document the handshake/channel URL and only the message shapes actually observed; distinguish transport from application operations.

## Build the evidence corpus and infer schemas

Aggregate observations by:

```text
method + normalized route + operation identity + request shape + response status/content type
```

Merge repeated payloads conservatively. Record required/optional, nullable, enum, array, nested-object, and status-specific variants only when supported by multiple observations or an explicit probe. Preserve field-level evidence IDs so a schema can be audited back to an action and response.

For list endpoints, combine observed examples to identify cursor/limit or offset/limit behavior, explicit filters, sort fields, defaults, and stable ordering. Do not invent pagination or retry guarantees. For errors, preserve the actual envelope and identify RFC 7807 fields only when present; note deviations.

## Generate optional evidence-aware artifacts

Keep Markdown as the canonical report. When requested, generate OpenAPI 3.1 or GraphQL SDL sidecars from the evidence corpus, never as replacements for the evidence report.

Annotate generated operations and schemas with evidence extensions such as:

```yaml
x-evidence-status: observed
x-evidence-ids: [action-07-request-003]
x-replayability: browser-session-required
x-side-effect: unknown
x-confidence: medium
```

Use `observed-contract` or `inferred-candidate` language rather than `production-ready` unless the user separately validates the artifact against the service. GraphQL SDL must distinguish observed operation shapes from a full introspected schema.

## Analyze authentication and replayability safely

Describe browser state, cookies, CSRF, authorization, signatures, timestamps, idempotency keys, and short-lived values without emitting their values. By default, infer header importance from repeated browser observations and response behavior; do not strip or replay live credentials.

In `probe` mode only, a header-necessity matrix may test non-sensitive browser hints in an authorized read-only environment. Record each variant and result. Classify a requirement as `required`, `not demonstrated`, `sensitive`, or `unknown`; never recommend retries or header removal for an unknown mutation.

## Run an authorized security assessment

Use `assess` only when the exploration contract includes explicit authorization, a safe environment, test principals, synthetic data, an expected policy matrix, an allowlist, and bounded stop conditions. Keep all activity headless and browser-mediated.

- **Hidden surfaces**: inspect browser-loaded chunks, manifests, source maps, route strings, feature flags, and client guards for `/admin/`, `/debug/`, `/metrics/`, export, or unlinked capabilities. Record these as `static-candidate`; do not auto-visit, bypass a guard, or infer authorization from frontend code.
- **Method/content variants**: use safe read-only controls first. Test alternate `Accept` or request content types only on allowlisted read endpoints. Do not send alternate verbs or state-changing bodies to live endpoints unless the user has explicitly authorized that exact test fixture.
- **BOLA/BFLA differentials**: require at least two test principals and an expected matrix covering principal, tenant, object, operation, and expected result. Compare status, body shape, sensitive keys, and timing only as signals; confirm with a fresh server-side read or state check. Label results `candidate`, `confirmed-in-fixture`, `inconclusive`, `rejected`, or `blocked`.
- **Authentication enforcement**: never strip or downgrade live credentials and never request tokens in chat. In a synthetic fixture only, compare control and malformed/absent-auth variants against an expected reject policy, recording whether the server—not only the frontend router—enforces it.
- **Mass assignment**: identify protected-looking fields such as role, admin, verification, tenant, or balance from observed schemas, then use harmless synthetic canary fields and isolated records. Verify before/after state; never inject privilege fields into real user or financial records.
- **Blind parameters**: apply a small, documented parameter corpus only to allowlisted read-only endpoints or fixtures. Treat changes in status, response length, JSON keys, timing, or content type as leads requiring confirmation, not findings.

Do not label a security issue confirmed unless the result is reproducible within the authorized scope and supported by the expected-policy matrix and state evidence. Do not infer absence of a vulnerability from a blocked or untested case.

## Produce the Markdown report

Write a single report with this structure:

```markdown
# Web Endpoint Map: <title>

## Scope and evidence
- Target, final URL, timestamp, browser/session assumptions
- Allowed origins and mutation policy
- Mode: observe / harvest / probe / assess and authorization basis
- Coverage summary: states/actions discovered and explored, requests observed, endpoints deduplicated
- Evidence labels: Observed / Inferred / Unknown

## Executive summary
<what the page appears to use and what is safe or unsafe to reuse>

## Endpoint index
| ID | Evidence class | Method/channel | Normalized URL | Trigger | Classification | Auth | Side effect | Confidence |

## Endpoint details
### <ID> <METHOD> <normalized URL>
<contract fields, redacted examples, schemas, errors, pagination, replay notes>

## Interaction coverage
| State/action | Result | Requests | Status |

## Security assessment scope
<authorization, environment, principals, tenants, synthetic objects, allowlist, budgets, and stop conditions; omit when not using assess mode>

## Authorization matrix and assessment results
| Principal/object/operation | Expected | Observed | State check | Result | Evidence |

## Static candidates and unconfirmed routes
| Candidate | Evidence resource | Why it is a candidate | Confirmation status |

## Traffic excluded from the API map
<assets, telemetry, ads, third parties, preflights, blocked mutations>

## Security and privacy notes
<redactions, credentials, sensitive data, replay hazards>

## Gaps and next tests
<blocked paths, unobserved states, required authorization, and smallest safe next test>

## Optional generated artifacts
<paths to OpenAPI, GraphQL SDL, or collection sidecars, each labeled with evidence scope>
```

Keep raw payloads bounded and readable. Prefer compact schemas and representative examples over dumping every response. Link every endpoint claim to an exploration action or captured evidence. Use stable endpoint IDs so later reports can be diffed.

For a final quality pass, read [references/reporting-rubric.md](references/reporting-rubric.md) and revise any entry that confuses observation with inference, exposes secrets, or overstates replayability or coverage.

## Completion gate

Before reporting completion, verify:

- the page was navigated and settled in headless Chrome;
- the selected evidence mode, authorization basis, budgets, and initial snapshot are recorded;
- `assess` runs include explicit scope, test principals, synthetic data, expected policy matrix, allowlist, and stop conditions;
- discovered and explored interaction states are recorded with stable state/action IDs and loop-bounded coverage;
- every documented endpoint has a trigger, classification, normalized identity, evidence class, and confidence;
- every `assess-signal` has a control case, test variant, expected result, observed result, and state evidence;
- static candidates and inferred templates are separated from observed usable endpoints;
- secrets and personal data are redacted;
- safe and mutating methods are distinguished;
- observed error payloads, pagination/filter/sort behavior, auth signals, and replay limits are documented;
- generated OpenAPI/GraphQL artifacts, if any, carry evidence scope and replayability limitations;
- third-party and non-API traffic is separated;
- blocked, untested, and unknown behavior is explicit;
- security results are labeled candidate, confirmed-in-fixture, inconclusive, rejected, or blocked, never overstated as production vulnerabilities;
- the Markdown file exists at the requested output path and is internally consistent.

The final response should link the Markdown report and summarize coverage, major endpoint families, safety restrictions, and unresolved gaps.
