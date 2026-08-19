# Reporting rubric

Use this rubric while reviewing a report. It is deliberately separate from the execution workflow so it can be loaded for quality review without adding exploration instructions to every run.

## Endpoint identity

An endpoint entry should be stable enough to compare across runs while retaining a concrete redacted observation. Include method, normalized URL, content type, and normalized request shape. Do not merge requests merely because their paths match when their operations, bodies, or response contracts differ.

## Evidence levels

- **Observed**: directly captured from a browser request, response, page state, or console event.
- **Inferred**: a cautious interpretation supported by repeated observations, such as a path parameter or cursor template.
- **Unknown**: not exposed, not exercised, blocked, or ambiguous.

Every field in a detailed endpoint entry should use one of these levels when it is not self-evident from the capture.

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

## API-design interpretation

Use API design concepts as an analysis lens, not as a reason to retrofit an undocumented contract:

- recognize HTTP method and status semantics without assuming the server follows them;
- identify RFC 7807 fields only when present and note deviations;
- describe cursor pagination, explicit filtering, and stable sorting when observed;
- record idempotency and retry signals rather than recommending retries for unknown mutations;
- preserve the target’s existing protocol and conventions;
- identify compatibility risks such as volatile fields, generated signatures, undocumented defaults, and schema drift.

## Safety review

Reject or revise a report that exposes credentials, claims unobserved endpoints are complete, provides unsafe mutation recipes without authorization, confuses telemetry with a reusable API, or presents inferred schemas as verified facts.
