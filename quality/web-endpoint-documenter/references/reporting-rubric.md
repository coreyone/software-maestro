# Reporting rubric

Use this rubric while reviewing a report. It is deliberately separate from the execution workflow so it can be loaded for quality review without adding exploration instructions to every run.

## Mode discipline

The report must state whether it used `observe`, `harvest`, `probe`, or `assess` mode. `observe` is the default. `harvest` may only describe browser-loaded resources. `probe` must include explicit authorization, target safety assumptions, and the exact bounded probe. `assess` additionally requires an authorized safe environment, test principals, synthetic canary data, an expected policy matrix, an allowlist, and stop conditions. Do not treat a higher mode as better evidence automatically.

## Exploration coverage

Check that the report records a state-and-action graph rather than only a request list. Each explored action should have a stable ID, source state, result state or failure, request window, and deduplication fingerprint. Coverage should name discovered-but-unexplored states and explain the stopping rule.

## Endpoint identity

An endpoint entry should be stable enough to compare across runs while retaining a concrete redacted observation. Include method, normalized URL, content type, and normalized request shape. Do not merge requests merely because their paths match when their operations, bodies, or response contracts differ.

## Evidence levels

- **Observed**: directly captured from a browser request, response, page state, or console event.
- **Inferred**: a cautious interpretation supported by repeated observations, such as a path parameter or cursor template.
- **Unknown**: not exposed, not exercised, blocked, or ambiguous.

Every field in a detailed endpoint entry should use one of these levels when it is not self-evident from the capture.

Static bundle strings, source-map interfaces, embedded routes, enumerated origins, and inferred path templates are candidates unless browser traffic or an authorized probe confirms them. Keep them out of the observed usable-endpoint count.

## Security assessment validity

For BOLA/BFLA claims, require a control case, at least one contrasting test principal or object, an expected authorization policy, and a fresh server-side state check. Status, response length, timing, or JSON-key differences alone are differential signals, not proof.

For authentication, method/content negotiation, mass-assignment, and parameter tests, verify that the target and data were explicitly allowlisted and synthetic or disposable. Never treat a blocked, untested, or production-inappropriate probe as evidence of either presence or absence of a vulnerability.

## Contract quality

Check that the report answers:

1. What action caused the request?
2. What must a caller provide?
3. What does the response contain?
4. How do success and failure differ?
5. Does the request read or mutate state?
6. What authentication, browser state, or short-lived values are required?
7. Can it be replayed safely, and what prevents that conclusion?
8. What pagination, filtering, sorting, versioning, caching, or rate-limit behavior was actually observed?

If a schema or generated artifact is present, verify that fields and variants retain evidence IDs, status/content-type partitions, and replayability limitations.

## API-design interpretation

Use API design concepts as an analysis lens, not as a reason to retrofit an undocumented contract:

- recognize HTTP method and status semantics without assuming the server follows them;
- identify RFC 7807 fields only when present and note deviations;
- describe cursor pagination, explicit filtering, and stable sorting when observed;
- record idempotency and retry signals rather than recommending retries for unknown mutations;
- preserve the target’s existing protocol and conventions;
- identify compatibility risks such as volatile fields, generated signatures, undocumented defaults, and schema drift.

## Safety review

Reject or revise a report that exposes credentials, claims unobserved endpoints are complete, provides unsafe mutation recipes without authorization, performs introspection, token tampering, header stripping, verb testing, or mass-assignment testing without assess authorization, confuses telemetry with a reusable API, presents inferred schemas as verified facts, or calls an observation-derived spec production-ready without separate validation.
