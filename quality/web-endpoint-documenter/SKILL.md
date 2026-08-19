---
name: web-endpoint-documenter
description: "Explore a URL with headless Chrome DevTools/CDP, interact with its observable UI, capture and classify network traffic, and produce an evidence-backed Markdown map of usable web endpoints. Use when documenting a web page's REST, GraphQL, RPC, streaming, form, pagination, authentication, error, or request/response behavior from browser-observed traffic."
---

# Web Endpoint Documenter

Turn a user-authorized URL into a reproducible, evidence-backed Markdown description of the network contracts observable from the page.

## Boundaries

- Use headless Chrome DevTools/CDP tools only. Do not use native GUI automation, direct HTTP crawling, source downloads, or alternate browser automation unless the user explicitly changes the constraint.
- Inspect only targets the user is authorized to analyze. Never bypass authentication, bot controls, paywalls, rate limits, origin policy, or access controls.
- Treat `GET`, `HEAD`, and `OPTIONS` as safe to observe. Do not submit forms or invoke `POST`, `PUT`, `PATCH`, `DELETE`, payments, account changes, uploads, or other mutations unless the user explicitly authorizes that action and it is clearly safe in the target environment.
- Redact cookies, authorization values, API keys, CSRF tokens, personal data, and secret-looking query/body values. Preserve header names and explain authentication requirements without emitting credentials.
- Do not claim completeness. Report the explored surface, observed requests, excluded actions, blocked paths, and remaining unknowns.

## Establish the exploration contract

Before browsing, resolve or state defaults for:

1. Starting URL and whether redirects may be followed.
2. Allowed origins: same-origin by default; label first-party subdomains and third-party traffic separately.
3. Authentication state: public session or an already-authorized browser profile. Never request secrets in chat.
4. Interaction budget: default to the initial load plus visible, non-destructive controls, with bounded depth, actions, and wait time.
5. Mutation policy: default `observe-only`; require explicit opt-in for safe test mutations.
6. Output path and report name. Use a Markdown file unless the user requests another format.

If a missing choice materially changes safety or coverage, ask one focused question before acting. Otherwise use the defaults above and record them in the report.

## Explore with Chrome DevTools

Use the `chrome-devtools` workflow:

1. List and select the target page, navigate to the URL, and wait for load/settling signals.
2. Capture an initial accessibility snapshot. Record title, final URL, visible routes, forms, controls, pagination, dialogs, tabs, and stateful UI.
3. Start network observation before each meaningful interaction. Associate requests with the triggering action and page state.
4. Exercise visible, non-destructive paths systematically: navigation, tabs, accordions, search/filter controls, pagination, sorting, dialogs, login-state branches already available, and bounded scrolling/infinite lists.
5. Refresh or revisit a state when needed to distinguish initial-load traffic from interaction traffic. Avoid duplicate actions once their request behavior is established.
6. Use `evaluate_script` only for page-observable data needed to understand behavior, such as form values, route state, or embedded configuration. Treat page JavaScript as evidence, not proof of a callable endpoint.
7. Capture console errors and blocked requests when they explain missing or degraded behavior.

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

## Produce the Markdown report

Write a single report with this structure:

```markdown
# Web Endpoint Map: <title>

## Scope and evidence
- Target, final URL, timestamp, browser/session assumptions
- Allowed origins and mutation policy
- Coverage summary: states/actions explored, requests observed, endpoints deduplicated
- Evidence labels: Observed / Inferred / Unknown

## Executive summary
<what the page appears to use and what is safe or unsafe to reuse>

## Endpoint index
| ID | Method/channel | Normalized URL | Trigger | Classification | Auth | Side effect | Confidence |

## Endpoint details
### <ID> <METHOD> <normalized URL>
<contract fields, redacted examples, schemas, errors, pagination, replay notes>

## Interaction coverage
| State/action | Result | Requests | Status |

## Traffic excluded from the API map
<assets, telemetry, ads, third parties, preflights, blocked mutations>

## Security and privacy notes
<redactions, credentials, sensitive data, replay hazards>

## Gaps and next tests
<blocked paths, unobserved states, required authorization, and smallest safe next test>
```

Keep raw payloads bounded and readable. Prefer compact schemas and representative examples over dumping every response. Link every endpoint claim to an exploration action or captured evidence. Use stable endpoint IDs so later reports can be diffed.

For a final quality pass, read [references/reporting-rubric.md](references/reporting-rubric.md) and revise any entry that confuses observation with inference, exposes secrets, or overstates replayability or coverage.

## Completion gate

Before reporting completion, verify:

- the page was navigated and settled in headless Chrome;
- the initial snapshot and all explored interaction states are recorded;
- every documented endpoint has a trigger, classification, normalized identity, evidence status, and confidence;
- secrets and personal data are redacted;
- safe and mutating methods are distinguished;
- observed error payloads, pagination/filter/sort behavior, auth signals, and replay limits are documented;
- third-party and non-API traffic is separated;
- blocked, untested, and unknown behavior is explicit;
- the Markdown file exists at the requested output path and is internally consistent.

The final response should link the Markdown report and summarize coverage, major endpoint families, safety restrictions, and unresolved gaps.
