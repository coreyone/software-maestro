# Measurement and Diagnostics

Use this reference to define SEO measurement, investigate losses, and evaluate changes without false precision.

## 1. Measurement tree

Connect metrics to outcomes:

`eligible URLs -> discovered -> crawled -> indexed/canonical -> impressions/citations -> clicks/referrals -> engaged actions -> conversions -> value`

Each stage has different failure causes. Do not optimize downstream CTR while valuable pages are excluded upstream.

## 2. Baseline dimensions

Segment at minimum by:

- page type/template;
- query intent and brand/nonbrand;
- country/language and local market;
- device;
- search surface: web, image, video, news, local, shopping, AI where data exists;
- new versus established content;
- conversion type and value.

Annotate deployments, content releases, migrations, outages, tracking changes, campaigns, seasonality, and known platform updates in UTC; convert to local time only for presentation.

## 3. Source reconciliation

- Search Console measures search impressions/clicks under its definitions and privacy/aggregation limits.
- Analytics measures instrumented sessions/events and can lose data to consent, blockers, redirects, attribution, or broken tags.
- Logs measure server requests but include bots, caches, prefetches, and requests that never execute analytics.
- Rank trackers sample queries, locations, devices, and SERP states; they are not census data.
- Third-party traffic/link/volume estimates are modeled.

Expect differences. Reconcile direction and definitions before treating mismatch as failure.

## 4. KPI set

Choose a small set tied to the engagement:

- qualified organic conversions and value;
- nonbrand impressions/clicks for priority intent clusters;
- share of valuable canonical pages indexed;
- search demand captured by priority page types;
- snippet CTR conditional on query and position bands;
- crawl success/freshness for priority templates;
- referring domains/citations that are relevant and editorial;
- AI citations/mentions and assisted outcomes where observable;
- Core Web Vitals pass rate using field data;
- content accuracy/freshness SLA.

Avoid vanity reporting that celebrates total indexed URLs, raw sessions, keyword counts, or audit scores without business context.

## 5. Loss-diagnosis sequence

### A. Verify the data

- Did tags, consent, attribution, channel grouping, filters, properties, or reporting APIs change?
- Do Search Console, analytics, logs, revenue systems, and rank samples agree on direction?
- Is the comparison aligned for weekdays, seasonality, timezone, and partial days?

### B. Scope the loss

Find the first break by page type, query, market, device, directory, protocol/host, and search surface. Determine whether impressions, position, CTR, clicks, conversion rate, or tracking changed.

### C. Establish a timeline

Correlate the first sustained change with releases, redirects, content edits, inventory, outages, security events, migrations, manual actions, and external demand. Correlation creates a hypothesis, not proof.

### D. Test the pipeline

- Fetch and render affected and unaffected controls.
- Compare directives, canonical selection, content, internal links, status, performance, and structured data.
- Inspect sitemap and log patterns.
- Review query/SERP intent changes, new features, AI answers, and competitor displacement.

### E. Form falsifiable hypotheses

For each hypothesis state predicted evidence, a confirming test, a disconfirming test, scope, and corrective action. Prefer the explanation that fits timing and segmentation with the fewest unsupported assumptions.

## 6. Indexation diagnostics

Build a matrix by template:

| State | Meaning | Typical next test |
|---|---|---|
| Not discovered | no known path | internal links, sitemap, URL creation |
| Discovered, not crawled | low priority/capacity/duplication | logs, quality, URL space, response speed |
| Crawled, not indexed | content/duplication/quality/directive | rendered content, canonical, soft 404, value |
| Duplicate/canonicalized | another URL selected | signal alignment and equivalence |
| Indexed, no impressions | demand/relevance/market | intent map, query data, competition |
| Impressions, low clicks | snippet/SERP/intent | query-position CTR, title, result features |

Do not use a raw `site:` query as an exact index count.

## 7. Forecasting

Use scenarios, not promises. State assumptions for addressable demand, achievable visibility, CTR, conversion, value, ramp time, and cannibalization. Provide downside/base/upside ranges and sensitivity to the weakest assumptions.

For engineering work, quantify affected URL/template count and current business contribution before forecasting traffic.

## 8. Experiments

- Define the unit: URL, template, cluster, market, or time series.
- Select comparable treatment and control groups where possible.
- Predefine primary metric, guardrails, minimum duration, and stop conditions.
- Avoid changing titles, body, internal links, and rendering simultaneously if causal learning matters.
- Account for crawl/index lag, seasonality, query mix, and sitewide interference.
- Preserve variants and timestamps.

SEO tests are noisy. Report effect ranges and uncertainty. A non-significant result is not proof of no effect.

## 9. Change acceptance

Verify in layers:

1. source/config test;
2. build or template output;
3. local/staging HTTP and rendered DOM;
4. production response and representative crawl;
5. search-engine recrawl/index data;
6. query, click, conversion, and business outcomes over the stated window.

Do not call a code merge an SEO outcome. Report which layers are complete and which require time.
