# Implementation Patterns

Use this reference when changing application code, infrastructure, templates, or tests.

## 1. Define invariants

Express SEO behavior as testable page-type invariants:

- every indexable page returns `200` and has one stable canonical to itself;
- every nonindexable page has an intentional reason and owner;
- titles and primary headings are meaningful for real content;
- canonical URLs appear in internal links and sitemaps;
- removed resources return a correct error or one relevant redirect;
- localized alternates form valid reciprocal clusters;
- structured data matches visible page facts;
- important content and links exist in rendered HTML;
- staging requires authentication and cannot leak into production discovery.

Test invariants at the shared template/router/content-model layer.

## 2. Framework-neutral head model

Derive metadata from validated page data, not arbitrary UI state:

```text
SeoDocument {
  canonicalUrl
  title
  description?
  indexPolicy
  language
  alternates[]
  openGraph?
  structuredData[]
}
```

Rules:

- build canonical URLs from an explicit public origin and normalized route;
- reject or safely default missing production origin;
- avoid request query strings in canonicals unless the parameter defines canonical content;
- serialize JSON-LD safely; never interpolate untrusted strings into raw script markup;
- ensure server and client derive identical values;
- keep social metadata and SEO metadata consistent but not unnecessarily coupled.

## 3. robots.txt pattern

Generate or serve robots.txt from a small reviewed policy. Separate environment behavior:

```text
production: explicit crawler policy + sitemap URL
staging/preview: authentication; defensive noindex headers; no public sitemap
```

Do not infer the public origin from an untrusted request host. Test exact bytes/status at `/robots.txt` after CDN deployment.

## 4. Sitemap pattern

Generate entries from the same canonical inventory used by routing/content publication. Filter before serialization:

```text
published && public && indexable && canonical && statusExpected200
```

Use UTC timestamps and emit `lastmod` only for substantive public changes. Stream or shard at scale. Tests should reject duplicates, noncanonical hosts, query tracking parameters, and nonindexable routes.

## 5. Redirect pattern

Store migrations as reviewed source-to-destination mappings with reason and expiry/review date. Validate:

- every source is unique;
- destinations are absolute or normalized safely;
- no cycles or chains are introduced;
- destination intent is equivalent enough to help users;
- query preservation is intentional;
- wildcard rules cannot capture unrelated paths;
- old top URLs and backlinks have coverage.

Test at the deployed edge because framework, CDN, and host redirects can compose unexpectedly.

## 6. Status and empty states

- Missing entity: real `404`/`410`, not an empty `200` app shell.
- Temporarily unavailable item: keep `200` only if the page remains useful and truthfully describes status/alternatives.
- Empty category/filter: usually avoid indexability and unbounded crawl paths; preserve a useful user state.
- Internal search: normally not an indexable landing-page generator unless deliberately curated.
- Access denied: use correct authentication/authorization behavior; never expose content for bots.

## 7. Faceted navigation

Create a facet policy table:

| Facet class | Crawlable links | Indexable | Canonical | Sitemap |
|---|---:|---:|---|---:|
| Primary curated category | yes | yes | self | yes |
| Useful high-demand combination | deliberate | yes | self | yes |
| Sort/view/tracking | no or controlled | no | base or omitted by design | no |
| Arbitrary/empty combination | no | no | case-specific | no |

Do not deploy blanket canonicalization without checking whether crawlers still waste resources on the combinations. Control link generation and URL state at source.

## 8. Structured data pipeline

- Generate JSON-LD from typed, validated domain data.
- Keep eligibility decisions near page-type logic.
- Unit-test required properties and URLs.
- Snapshot representative output cautiously; add semantic assertions so snapshots do not approve false data.
- Run an external validator on deployed representative pages.
- Monitor rich-result/search-console reports after release.

Never copy schema from a competitor without verifying current support and page truth.

## 9. Rendering tests

For representative routes verify:

- raw HTML contains primary title/content/link/canonical where intended;
- rendered DOM preserves them after hydration;
- disabled JavaScript behavior remains usable enough for the chosen rendering architecture;
- slow/failed APIs produce accurate statuses and useful fallbacks;
- lazy content becomes available without unsupported interaction;
- bot-facing behavior matches normal anonymous users except legitimate localization/device adaptation.

Use CLI HTTP inspection before browser automation. Use a real browser when rendering, hydration, consent, or interaction is in question.

## 10. Performance budgets

Set budgets per template and device class for HTML/server time, critical JS/CSS, image weight, third parties, and field CWV. Gate major regressions in CI where the signal is stable; do not fail builds on noisy single-run lab scores alone.

## 11. Release checklist

Before merge:

- review affected templates and URL count;
- run unit/integration/build tests;
- crawl representative output;
- compare raw and rendered metadata/content;
- validate directives, canonical, structured data, links, status, and events;
- document production-only checks and rollback.

After deploy:

- fetch through the public CDN/WAF;
- inspect representative mobile render;
- validate analytics and conversion events;
- check logs for crawler blocks/errors;
- submit/inspect critical URLs only when useful;
- monitor template-level search and business metrics through the expected recrawl/index window.

## 12. Finding format for code reviews

```text
[P1] Canonical host derived from request Host
Evidence: file:line and deployed response
Impact: all product pages can emit attacker/proxy hosts
Cause: unvalidated public-origin construction
Fix: require configured public origin; normalize routes
Acceptance: unit tests + production sample show one correct canonical
```

Avoid generic “add SEO” recommendations. Name the broken invariant, blast radius, exact layer, and proof.
