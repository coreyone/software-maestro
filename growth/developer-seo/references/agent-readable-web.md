# Agent-Readable Web Representations and Actions

Use this reference when a website should be easier for LLMs or browser agents to retrieve, parse, cite, or operate. Keep retrieval, search visibility, and action execution as separate capabilities with separate success measures.

## Contents

1. Decision model
2. HTTP content negotiation
3. One source and semantic parity
4. Markdown representation contract
5. Discovery
6. Cache correctness
7. Failure and security behavior
8. Observability and rollout
9. `llms.txt` and generated indexes
10. Agent actions and WebMCP
11. Test matrix
12. Definition of done

## 1. Decision model

Implement negotiated Markdown when at least one of these is true:

- request logs show clients asking for `text/markdown`;
- developer documentation, support knowledge, research, catalogs, or other content-heavy pages have meaningful agent use;
- a named consumer documents support;
- controlled tests show cleaner extraction, lower payload/token cost, or faster retrieval;
- the feature can be generated from the canonical content without a second editorial workflow.

Treat it as a retrieval and usability optimization, not a ranking factor or universal SEO requirement. As of July 2026, Google states that Markdown and `llms.txt` are not required and do not improve visibility in Google Search. Other agent products and infrastructure providers do request or serve negotiated Markdown.

Default to HTML when evidence is absent, generation is unreliable, or cache/security controls are not ready. Pilot on high-value page types before enabling sitewide.

Use three distinct layers:

1. **Discovery:** crawlers and agents can find the resource.
2. **Representation:** clients can retrieve useful HTML or Markdown.
3. **Action:** authorized agents can safely perform supported tasks.

Passing one layer does not prove the next.

## 2. HTTP content negotiation

Serve the same resource in different representations at one canonical URL when the application and CDN can do so correctly.

When Markdown is selected, return:

```http
HTTP/1.1 200 OK
Content-Type: text/markdown; charset=utf-8
Vary: Accept
```

Keep the browser/default response as `text/html; charset=utf-8`. Do not redirect solely because a client requests Markdown. Internal rewrites are fine if the public URL and semantics remain stable.

### Parse `Accept` correctly

Use an RFC-aware media-type negotiator. Do not test only whether the raw header contains `text/markdown`.

- Honor quality weights (`q`). A media range with `q=0` is unacceptable.
- Prefer Markdown only when `text/markdown` is acceptable and wins the server's documented selection policy.
- Support lists such as `text/markdown, text/html;q=0.8, */*;q=0.1`.
- Treat an absent `Accept` header as no stated preference and normally serve HTML.
- Decide and test how ties, `text/*`, and `*/*` resolve; defaulting to HTML minimizes browser surprises.
- If no available representation is acceptable, either return `406 Not Acceptable` or deliberately disregard negotiation as permitted by HTTP. A fallback must declare its true `Content-Type`.

Apply the same authorization, locale, personalization, status code, and canonical resource semantics to both representations. Content negotiation must not become a crawler-only access bypass or cloaking mechanism.

## 3. One source and semantic parity

Generate HTML and Markdown from the same structured content, CMS record, document AST, or validated domain model. Acceptable pipelines include:

- source/AST -> HTML renderer + Markdown renderer;
- structured CMS content -> HTML + Markdown serializers;
- canonical server-rendered content region -> deterministic HTML-to-Markdown conversion.

Do not maintain independent `.html` and `.md` copy. If a stable `.md` URL exists, generate it through the same pipeline and invalidation event.

Define parity semantically, not byte-for-byte. Both representations must preserve:

- claims, facts, qualifications, units, and examples;
- page title, summary, heading hierarchy, and primary content;
- meaningful links and their destinations;
- ordered/unordered lists, genuinely tabular data, and code examples;
- author/source identity and substantive update timestamp;
- legally or operationally important notices;
- the same access and publication state.

Format-specific differences are valid: HTML navigation, controls, styling, structured data, and visual layout need not appear verbatim in Markdown. Test the meaning users rely on.

Build parity tests around the shared source or normalized semantic model. Compare extracted headings, facts/fields, links, tables, code blocks, and timestamps. Fail publication or alert the owner when required elements diverge.

## 4. Markdown representation contract

Prefer a conservative CommonMark-compatible subset unless a known consumer supports more.

### Include

- optional machine-readable metadata when supported: title, concise description, canonical URL, Markdown URL if stable, language, author, and ISO 8601 `last_updated` in UTC;
- one `#` page title;
- logical `##` and `###` sections without skipped levels where practical;
- the complete primary content and important caveats;
- descriptive absolute links when the response may be consumed out of site context;
- lists, block quotes, and tables only when they preserve actual structure;
- fenced code blocks with an accurate language identifier;
- concise image descriptions and source URLs when the image carries meaning;
- provenance/citation links needed to verify material claims.

YAML frontmatter is a convention, not core Markdown. Use it only when the delivery platform or intended consumers support it; escape values and delimiters safely. Otherwise expose metadata as a short Markdown section or response headers.

### Remove

- global navigation, cookie/consent chrome, decorative controls, and repeated footers;
- CSS, scripts, hydration/application state, tracking payloads, and source maps;
- ads, promotional modules, unrelated recommendations, and duplicated calls to action;
- hidden layout text, duplicated accessibility labels, icon names, and screen-reader-only UI instructions that do not help understand the content;
- modal/drawer text that is unrelated to the requested page state.

Do not remove semantic labels needed to understand a form, control, diagram, or accessible alternative. Clean output means less chrome, not less meaning.

### Serialize safely

- Escape Markdown control characters where content is data rather than authored markup.
- Choose a code-fence length that cannot be closed by the example content.
- Escape table pipes and use lists when cells contain complex or multiline content.
- Preserve Unicode and declare UTF-8.
- Sanitize unsafe URLs and never resolve private/internal links into public output.
- Do not include secrets, session state, unpublished fields, internal IDs, or hidden personalization.

Markdown should normally be smaller and easier to parse than HTML, but never delete required facts merely to reduce tokens.

## 5. Discovery

Content negotiation at the canonical URL requires no alternate URL discovery. If a stable generated Markdown URL also exists, advertise it in HTML:

```html
<link rel="alternate" type="text/markdown" href="https://example.com/path.md">
```

The alternate must return current content from the same source and must not create a second canonical page or editorial workflow. Use an absolute URL in reusable templates when origin configuration is trustworthy.

An HTTP `Link` header may advertise the alternate for non-HTML clients when the platform supports it. Do not assume either signal is universally consumed or provides a ranking benefit.

Keep standard HTML pages, internal links, XML sitemaps, and search-engine eligibility intact. A Markdown alternate or Markdown sitemap is an optional agent navigation aid, not a substitute for standard discovery.

## 6. Cache correctness

Whenever representation selection depends on `Accept`, include `Accept` in `Vary` for every affected cacheable response, including errors when their representation varies. Preserve existing `Vary` dimensions rather than overwriting them.

Configure application, reverse proxy, and CDN caches to separate HTML and Markdown variants. Where supported, normalize the cache key to the selected representation instead of every raw `Accept` permutation, while preserving HTTP-correct behavior.

Generate representation-specific validators:

- distinct strong `ETag` values for different bodies; or
- correctly scoped weak validators; or
- omit validators when an edge conversion layer cannot honor conditional requests safely.

Test for cross-format cache poisoning:

1. request HTML, then Markdown, then HTML again;
2. reverse the order;
3. test cold and warm caches at origin and CDN;
4. verify `Content-Type`, body format, `Age`/cache headers, validators, and status each time;
5. test purge/revalidation after a source update.

Do not assume emitting `Vary: Accept` alone proves a CDN uses the right cache key. Verify deployed behavior.

## 7. Failure and security behavior

On Markdown generation failure:

- return an honest `5xx` or other appropriate status when the requested representation cannot be produced; or
- deliberately fall back to HTML only when policy allows it, declaring `Content-Type: text/html` and retaining correct `Vary` behavior.

Never label HTML as Markdown. Never serve a previously generated stale representation silently after the canonical source has changed unless an explicit stale-while-revalidate policy applies equally and its age is observable.

Preserve authentication, authorization, robots controls, privacy rules, rate limits, embargoes, paywalls, legal notices, and content-use policy across representations. A cleaner representation increases extraction efficiency and therefore the blast radius of accidental disclosure.

Treat request headers and user-agent strings as untrusted. Avoid automatic user-agent rewriting by default; prefer explicit `Accept`. If a verified or signed agent mechanism is adopted, validate it according to current first-party documentation and include it in the cache key and threat model.

Review conversion for prompt injection and data-boundary confusion. Clearly delimit untrusted user-generated or third-party content. Do not let page content alter server behavior or expose internal instructions.

## 8. Observability and rollout

Log the selected representation, not only the raw request. Record in UTC:

- requested URL or route template;
- normalized requested media types and selected format;
- user agent as an untrusted string;
- response status, size, generation latency, and cache outcome;
- source revision/update timestamp;
- failures and fallback reason.

Minimize personal data, credentials, query values, and retention. Sample high-volume traffic where appropriate. Do not infer a verified agent identity from the user-agent header alone.

Measure by page type:

- Markdown request volume and unique requesting client patterns;
- HTML versus Markdown bytes and estimated parser/token overhead;
- generation and retrieval latency;
- cache hit rate and variant errors;
- parser/validation failures, broken links, and stale-content incidents;
- downstream citations, referrals, tool success, or support deflection when observable.

Use the evidence to expand, revise, or remove support. More generated files are not evidence of more value.

## 9. `llms.txt` and generated indexes

Do not hand-maintain `llms.txt` or treat it as a Search requirement. Implement `llms.txt`, `llms-full.txt`, `sitemap.md`, or similar indexes only when:

- a named consumer uses the format or logs show meaningful requests;
- it is generated automatically from the canonical inventory;
- every URL is current, public, authorized, and useful;
- generation and invalidation share the content pipeline;
- ownership and monitoring exist;
- it creates no separate editorial workflow.

Do not let an auxiliary index replace clean page-level retrieval, standard internal links, XML sitemaps, robots policy, or normal search eligibility. Remove it when no consumer value can be demonstrated.

## 10. Agent actions and WebMCP

Markdown makes a page easier to read; it does not make interactive tasks safe or reliable. For agent actions, start with semantic HTML, accessible names, standard forms, stable URLs, clear error states, and server-side validation.

As of July 2026, WebMCP is a proposed web standard in a Chrome origin trial, not a baseline cross-browser capability. Consider it only as progressive enhancement for valuable tasks, with feature detection and a normal human workflow fallback.

When piloting WebMCP:

- use current `document.modelContext` APIs; verify the proposal and Chrome status before coding;
- expose a small task-oriented tool surface rather than mirroring every UI control;
- reuse the same domain service, authorization, validation, CSRF protection, rate limits, idempotency, and audit logging as the human/API path;
- mark read-only behavior with `readOnlyHint` and untrusted results with `untrustedContentHint` where supported;
- limit cross-origin exposure to explicitly trusted secure origins;
- unregister route/state-specific tools with the supported lifecycle mechanism;
- require explicit user review/confirmation for purchases, messages, publishing, deletion, permissions, and other consequential actions;
- return structured, bounded results and distinguish untrusted content from instructions;
- test prompt injection, confused-deputy behavior, replay, duplicate submission, cancellation, navigation, and stale state;
- measure task completion, correction rate, confirmations, failures, and security events.

Do not claim WebMCP affects search rankings. Keep experimental APIs behind a reversible rollout and current compatibility check.

## 11. Test matrix

### Negotiation

```bash
curl -sS -D - https://example.com/page -o /tmp/page.html
curl -sS -D - -H 'Accept: text/markdown' https://example.com/page -o /tmp/page.md
curl -sS -D - -H 'Accept: text/markdown, text/html;q=0.8' https://example.com/page -o /tmp/page-preferred.md
curl -sS -D - -H 'Accept: text/markdown;q=0, text/html;q=1' https://example.com/page -o /tmp/page-rejected.html
```

Assert:

- expected status and exact media type;
- `Vary` contains `Accept` without losing other dimensions;
- absent/tied/wildcard/weighted headers follow documented policy;
- `q=0` never selects Markdown;
- HEAD and conditional requests match GET semantics where supported;
- redirects and errors preserve honest representation metadata.

### Content

- parse Markdown with the project's target parser in strict mode;
- compare normalized facts/fields, headings, links, lists, tables, code, and timestamps with the canonical source and rendered HTML;
- scan for broken links, private URLs, scripts/styles/state, navigation chrome, duplicated boilerplate, and leaked fields;
- verify Unicode, escaping, code fences, tables, images, and empty/long content;
- update the source and prove HTML and Markdown invalidate together.

### Cache and operations

- run both request orders through origin and CDN cold/warm caches;
- verify format-specific validators and purge/revalidation;
- simulate generator failure, timeout, stale cache, and partial CMS data;
- confirm logs capture selection, size, latency, cache outcome, and failure without sensitive data;
- load-test generation and bound CPU/memory/time.

### Agent actions

- test feature detection and human fallback;
- test authorization and confirmation parity;
- test read/write boundaries, prompt injection, untrusted output, replay, cancellation, and duplicate execution;
- confirm unsupported browsers ignore enhancements without breaking the page.

## 12. Definition of done

- `Accept: text/markdown` selects clean Markdown under the documented negotiation policy.
- Markdown returns `Content-Type: text/markdown; charset=utf-8` and responses vary correctly on `Accept`.
- HTML and Markdown are generated from one canonical source and preserve all material information.
- Deployed CDN and application caches cannot cross-serve formats.
- Markdown is structurally valid, meaningfully cleaner, and free of private or irrelevant UI data.
- Source updates invalidate every representation together; stale behavior is explicit and tested.
- Logs measure real usage, format, size, latency, cache behavior, and failures with privacy controls.
- No manually maintained `llms.txt` or Markdown copy exists.
- Failures return honest statuses and content types.
- Any agent action layer is progressive, authorized, confirmed where consequential, and tested against prompt injection and replay.
- Documentation states that agent representations and action protocols are not guaranteed ranking signals.
