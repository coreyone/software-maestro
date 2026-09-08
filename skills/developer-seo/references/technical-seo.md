# Technical SEO

Use this reference for crawling, rendering, indexing, canonicalization, structured data, internationalization, performance, and migrations.

## Contents

1. Diagnostic sequence
2. HTTP and access
3. Directives and canonicalization
4. Discovery and crawl efficiency
5. Rendering and JavaScript
6. Structured data and media
7. International and local variants
8. Page experience
9. Migrations

## 1. Diagnostic sequence

For each representative URL capture four views:

- requested URL and redirect chain;
- raw HTTP status, headers, and HTML;
- rendered DOM plus failed resources and console/network errors;
- search-engine-reported canonical, index state, and last crawl when available.

Compare desktop/mobile only where behavior differs. Test logged out, clean cookies, and a neutral location when personalization could alter output.

Trace failures in order. A missing page cannot rank; an inaccessible page cannot render; a non-indexable page cannot be canonical; a canonicalized-away page cannot own a query.

## 2. HTTP and access

### Status codes

- Return `200` only for a real, useful page.
- Use `301` or `308` for durable moves and `302` or `307` for genuinely temporary routing. Preserve method semantics where relevant.
- Return `404` or `410` for gone resources. A pretty error page with `200` is a soft 404 risk.
- Investigate intermittent `5xx`, `429`, CDN challenges, geo blocks, bot blocks, and timeouts from logs—not one fetch alone.
- Avoid redirect chains, loops, mass redirects to irrelevant destinations, and redirecting every removed URL to the home page.

### Access controls

- Ensure public pages and their critical CSS, JS, images, and APIs are fetchable by intended crawlers.
- Do not expose private content to solve SEO. Authentication and authorization are security boundaries; robots.txt is not.
- Confirm WAF and rate-limit rules distinguish verified crawlers safely. Do not trust user-agent strings alone when IP verification is required.
- Check staging cannot be indexed. Prefer authentication; add `noindex` as defense in depth, and never rely on robots.txt alone to hide indexed URLs.

## 3. Directives and canonicalization

### robots.txt

- Use it to control crawling, not to remove an already known URL from an index.
- Keep syntax simple; test precedence; reference sitemap indexes where useful.
- Do not block a URL that must be crawled to observe its `noindex`.
- Audit bot-specific rules and CDN copies. Record the business decision behind AI crawler rules.

### Meta robots and X-Robots-Tag

- Use HTML meta for pages and `X-Robots-Tag` for files or HTTP-level control.
- Treat `noindex`, snippet, cache, image, and follow controls as independent decisions.
- Ensure production templates cannot inherit staging `noindex`.
- Check header and HTML directives for conflicts; the more restrictive result may win.

### Canonicals

- Pick a canonical URL that returns `200`, is indexable, and contains equivalent primary content.
- Align redirect targets, internal links, sitemaps, hreflang, and structured-data URLs with the preferred canonical.
- Use self-referential canonicals on indexable templates when the platform can emit them consistently.
- Normalize protocol, host, casing policy, trailing slash, default ports, index files, and tracking parameters.
- Do not canonicalize paginated, localized, or substantively different pages to a generic parent merely to shrink the index.
- Treat canonical tags as hints. Diagnose conflicting signals when the engine selects another URL.

### Duplicate and parameter URLs

Classify parameters as sorting, filtering, tracking, pagination, session, or content-defining. Decide crawl/index/canonical behavior by class. Ensure navigation does not create unbounded URL spaces through arbitrary combinations, calendars, internal searches, or session IDs.

## 4. Discovery and crawl efficiency

### Internal links

- Emit crawlable `<a href>` links for important navigation and contextual relationships.
- Make valuable pages reachable without site search, form submission, hover-only UI, or client-only event handlers.
- Link from relevant high-visibility hubs with descriptive, natural anchors.
- Detect orphaned pages, excessive depth, broken links, and links to redirects/noncanonical URLs.
- Use breadcrumbs and related-content modules when they reflect genuine hierarchy or association.

### XML sitemaps

- Include only canonical, indexable, `200` URLs the site wants discovered.
- Split by page type or market when it improves diagnosis; use sitemap indexes at scale.
- Emit accurate absolute URLs and meaningful `lastmod` values based on substantive changes.
- Do not treat sitemap submission as a substitute for internal linking or quality.
- Compare submitted, discovered, crawled, canonicalized, and indexed counts by template.

### Crawl-budget work

Prioritize it only for large or rapidly changing sites with evidence of discovery/freshness constraints. Reduce infinite spaces, duplicate fetches, slow responses, error loops, and stale URLs. Use server logs to measure bot demand and response quality.

## 5. Rendering and JavaScript

- Prefer meaningful primary content, titles, canonicals, robots directives, and links in the initial HTML when practical.
- Server rendering, static generation, or reliable pre-rendering reduces latency and dependency risk; choose by product constraints, not dogma.
- Ensure hydration does not replace useful HTML with errors, placeholders, or divergent content.
- Test lazy-loaded content without scroll/click requirements that crawlers may not perform.
- Avoid fragment-only routing for indexable states. Give each intended page a stable URL and meaningful status.
- Handle API errors as real errors. Do not return an empty `200` shell for missing products or articles.
- Keep canonical and robots signals stable between raw and rendered HTML.
- Verify content behind consent, geolocation, personalization, and client storage has an indexable default representation.
- Test rendered DOM, not only browser screenshots. A visible canvas or image may contain no indexable text.

## 6. Structured data and media

### Structured data

- Select types based on actual page purpose and current search-engine eligibility.
- Make JSON-LD entities consistent with visible content and canonical URLs.
- Use stable `@id` values to connect Organization, WebSite, WebPage, Person, Product, Article, BreadcrumbList, and other justified entities.
- Include required properties and accurate recommended properties; do not fabricate ratings, prices, availability, authors, or dates.
- Validate syntax and feature eligibility separately. Valid schema does not guarantee a rich result.
- Monitor template-wide warnings after releases.

### Images and video

- Use descriptive filenames where maintainable, useful alt text, surrounding context, accessible captions when needed, and indexable asset URLs.
- Do not stuff keywords into alt text; decorative images should normally use empty alt text.
- Preserve width/height or aspect ratio to limit layout shift. Serve responsive formats and sizes.
- For video-first pages, provide a stable watch page, descriptive title/context, thumbnail, and supported video markup/sitemap where appropriate.
- Keep critical media out of blocked scripts, expiring URLs, or inaccessible CDNs.

## 7. International and local variants

### International

- Localize language, currency, units, legal terms, and intent; do not merely translate keywords.
- Use stable locale URLs. Avoid mandatory IP redirects that hide alternatives from crawlers or users.
- Implement reciprocal, canonical-consistent hreflang with valid language/region codes; include `x-default` only for a real fallback.
- Each localized page generally canonicalizes to itself, not to another language.
- Validate clusters, not isolated tags. One broken return link can affect the set.

### Local

- Keep name, address, phone, hours, service area, categories, and landing-page claims accurate across owned profiles and site pages.
- Create location pages only when each represents a real location/service and provides locally useful, non-boilerplate information.
- Connect Organization/LocalBusiness entities consistently; manage reviews ethically; never fabricate location presence.

## 8. Page experience

- Optimize for real users and field data. Diagnose LCP, INP, and CLS at the page-type and device level.
- LCP: reduce server delay, prioritize the actual hero resource, avoid render-blocking work, and size/compress media.
- INP: reduce long main-thread tasks, excessive hydration, third-party work, and event-handler cost.
- CLS: reserve media/ad/embed space, control font swaps, and avoid inserting content above the viewport.
- Preserve content and conversion behavior while optimizing. A fast empty page is not success.
- Treat HTTPS, mobile usability, accessibility, intrusive interstitials, and stability as trust and usability requirements, not isolated ranking tricks.

## 9. Migrations

Before launch:

- inventory indexed/linked/trafficked URLs and classify keep, move, merge, or retire;
- create one-to-one redirect mappings where equivalent destinations exist;
- preserve content, metadata, canonicals, hreflang, structured data, internal links, and analytics unless change is intentional;
- crawl staging behind authentication and scan for accidental production URLs or `noindex` leakage;
- establish baselines by page type, query, market, device, backlinks, and conversions;
- define rollback conditions and owners.

At launch:

- deploy redirects atomically where possible;
- update internal links, canonicals, sitemaps, feeds, profiles, and critical external destinations;
- verify DNS/TLS/CDN, representative responses, rendered pages, robots.txt, analytics, and conversion events;
- submit new sitemaps and use supported change-of-address workflows when applicable.

After launch:

- monitor logs, crawl errors, indexed counts, canonical selection, rankings, clicks, conversions, and redirect misses daily at first;
- retain redirects long enough for users, crawlers, and external links to transition;
- fix patterns at source instead of accumulating redirect chains.
