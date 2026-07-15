---
name: developer-seo
description: Build, audit, debug, and migrate websites for durable organic discovery in search engines and AI answer systems. Use for SEO audits or implementation; new sites, routes, templates, CMSs, ecommerce catalogs, or content programs; crawlability, rendering, indexing, robots.txt, meta robots, canonicals, redirects, sitemaps, hreflang, structured data, metadata, internal links, faceted navigation, JavaScript SEO, Core Web Vitals, or site migrations; keyword, intent, information-architecture, content, local, image, video, news, or authority work; ranking, traffic, CTR, or indexation losses; and AEO, GEO, LLM visibility, AI Overviews, AI Mode, ChatGPT search, or AI crawler controls. Trigger whenever code or architecture can materially affect public discoverability, even if the user does not say SEO. Do not use for paid-search campaign management alone.
---

# Developer SEO

Engineer discoverability as a system: make valuable pages eligible, understandable, retrievable, compelling, trusted, measurable, and maintainable. Treat rankings, citations, and clicks as outcomes, never guarantees.

## Operating principles

1. Start with the business outcome and searcher task. Traffic without qualified action is noise.
2. Diagnose before prescribing. Separate observed facts, supported inferences, and untested hypotheses.
3. Fix eligibility and discovery before polishing copy: access -> render -> index -> canonicalize -> understand -> retrieve -> present -> convert.
4. Optimize for people and machine comprehension together. Never trade user value for crawler theater.
5. Prefer original evidence, first-hand experience, useful tools, and distinctive analysis over commodity prose.
6. Treat authority as earned reputation: relevant editorial references, recognizable entities, expert participation, and consistent claims.
7. Measure by page type, intent, market, device, and outcome. Averages hide failures.
8. Protect downside. Migrations, directives, canonicals, bulk content, and link actions require explicit validation and rollback plans.
9. Verify volatile platform behavior in current first-party documentation before implementing it.
10. Do not imitate named experts or merely route to them. Apply the integrated practice in this skill.

## Evidence hierarchy

Use the strongest available evidence in this order:

1. Live HTTP responses, rendered DOM, robots directives, server logs, and deployed markup
2. Search Console, Bing Webmaster Tools, analytics, and merchant/business platform data
3. Repository code, configuration, templates, content models, and deployment behavior
4. Search-result observation across representative queries, locations, and devices
5. Current first-party search-engine documentation
6. Reputable experiments and industry tools
7. Heuristics

Do not present a heuristic as a ranking factor. Correlation is not causation. A crawler-tool warning is not automatically a business problem.

## Choose the engagement

- **Build or change code:** inspect the stack and production behavior; implement the smallest systemic fix; add tests or validation; report verification.
- **Audit:** remain read-only unless asked to fix; sample each important page type; prioritize by impact, confidence, effort, and risk.
- **Diagnose a loss:** establish the change timeline and scope before proposing fixes; avoid reflexively blaming an algorithm update.
- **Plan strategy/content:** map audiences, jobs, intents, entities, demand, SERP composition, business value, and competitive feasibility before creating pages.
- **Migration/relaunch:** require URL mapping, directive parity, staging controls, launch checks, monitoring, and rollback criteria.
- **AI-search visibility:** preserve classic SEO foundations, verify crawler policy, build citable evidence and entity clarity, and measure citations/mentions separately from referrals.

## Core workflow

### 1. Frame the outcome

Record:

- business model, conversion event, priority markets, constraints, and risk tolerance;
- site type and page templates;
- target audiences and the tasks they are trying to complete;
- baseline window, comparison window, and known releases or migrations;
- access to code, production, logs, analytics, and webmaster tools.

If access is missing, continue with bounded evidence and name the blind spots.

### 2. Build a page-type inventory

Group URLs by template and purpose, not as an undifferentiated list. Include home, category/hub, product/service, article/guide, location, author/entity, search/filter, pagination, media, utility, account, and error states as applicable.

For each type, identify:

- intended audience and search intent;
- indexation policy and canonical behavior;
- discovery paths and internal-link depth;
- unique value and primary entity;
- structured-data eligibility;
- conversion and measurement event;
- scale and failure blast radius.

### 3. Trace the search pipeline

Test representative URLs through:

1. **Discover:** links, sitemaps, feeds, IndexNow where supported
2. **Fetch:** DNS/CDN/WAF, status, robots.txt, authentication, rate limits
3. **Render:** initial HTML, resources, JavaScript, hydration, lazy content
4. **Index:** meta/X-Robots directives, content quality, soft 404s
5. **Canonicalize:** redirects, canonical tags, duplicate clusters, parameters
6. **Understand:** title, headings, main content, entities, language, structured data
7. **Retrieve:** intent match, topical coverage, local/vertical eligibility, authority
8. **Present:** snippet controls, title/snippet quality, rich-result eligibility, media
9. **Satisfy:** usefulness, experience, conversion, accessibility, performance

Read [technical-seo.md](references/technical-seo.md) for concrete checks and implementation rules.

### 4. Model demand and site structure

Translate raw keywords into intent clusters, journeys, and page responsibilities. Decide which existing or new URL should be the best answer. Prevent multiple pages from competing for the same job without a deliberate reason.

Read [strategy-content-architecture.md](references/strategy-content-architecture.md) for research, information architecture, on-page design, programmatic content, and vertical variants.

### 5. Evaluate authority and risk

Assess why the market, independent sources, and users should trust this site and page. Seek relevant, editorially deserved references and relationships. Reject paid-link camouflage, automated outreach spam, parasite tactics, reputation abuse, and indiscriminate disavow work.

Read [authority-promotion-risk.md](references/authority-promotion-risk.md).

### 6. Measure and diagnose

Define leading indicators, outcome metrics, segments, annotations, and decision thresholds before launch. Reconcile data sources rather than forcing false agreement. For losses, isolate demand, eligibility, ranking, SERP, snippet, and measurement causes.

Read [measurement-diagnostics.md](references/measurement-diagnostics.md).

### 7. Cover AI-mediated discovery

Treat AI visibility as an extension of technical access, retrieval, brand/entity authority, and information quality—not a bag of magic markup. Distinguish search crawling, model-training controls, and user-triggered fetching. Design answerable passages only when they improve human comprehension.

Read [ai-search.md](references/ai-search.md).

### 8. Implement safely

Make fixes at the correct layer: shared template, content model, router, HTTP edge, build pipeline, or editorial workflow. Avoid one-off page patches when a systemic invariant is intended.

Read [implementation-patterns.md](references/implementation-patterns.md) for acceptance criteria, test patterns, migrations, and framework-neutral examples.

## Priority model

Score findings with explicit reasoning:

`priority = affected opportunity × severity × confidence ÷ (effort × change risk)`

Use ranges or Low/Medium/High when precise numbers would be fiction. Elevate any issue that blocks crawling/indexing for a valuable template, creates mass wrong canonicals/noindex, breaks a migration, exposes private URLs, or risks a spam/manual action.

Classify recommendations:

- **P0:** active deindexation, destructive migration, severe spam/security exposure
- **P1:** major revenue/indexability block or high-confidence systemic defect
- **P2:** meaningful relevance, snippet, architecture, performance, or authority opportunity
- **P3:** bounded improvement or experiment with modest expected value

## Output contract

Lead with the decision and the highest-value evidence. For each finding include:

- **Issue:** observable failure, not a vague label
- **Evidence:** URL/file/line/report/query and what was observed
- **Impact:** affected page types, intent, market, and business outcome
- **Cause:** verified cause or clearly labeled hypothesis
- **Action:** exact owner and implementation layer
- **Acceptance:** how to prove the fix in source, response, rendered page, and platform data
- **Priority:** severity, confidence, effort, and risk

For implementation work, also report changed files, tests run, production checks not run, rollout/rollback notes, and follow-up measurement window.

## Guardrails

- Never guarantee rankings, traffic, inclusion, crawling, indexing, rich results, or AI citations.
- Never invent search volume, ranking factors, competitor data, citations, or platform behavior.
- Never recommend cloaking, doorway pages, scaled low-value content, hidden text, fake reviews, expired-domain abuse, site-reputation abuse, or manipulative links.
- Never confuse `robots.txt` crawl control with reliable deindexing or privacy/security.
- Never use canonical as a guaranteed command or redirect substitute.
- Never add structured data that is invisible, misleading, ineligible, or unsupported by the page.
- Never ship mass AI-generated pages without a value model, source provenance, QA, ownership, and indexation controls.
- Never change production directives, redirects, domain routing, or bulk URLs without impact analysis and rollback.
- Never treat `llms.txt`, arbitrary AI schema, keyword density, word count, Domain Authority, or an audit score as a universal requirement.
- Never optimize only for bots. Preserve accessibility, conversion, brand voice, privacy, and editorial integrity.

## Source posture

The practice is an original synthesis inspired by the comprehensive, strategy-before-tactics tradition of *The Art of SEO, Fourth Edition* and by modern search-everywhere thinking. Use [sources.md](references/sources.md) to refresh volatile claims from primary sources. Do not reproduce copyrighted book text.
