# AI Search and Answer Visibility

Use this reference for AI Overviews, AI Mode, ChatGPT search, Copilot, answer engines, generative engine optimization, and AI crawler policy.

## 1. Model the surfaces separately

Do not treat all AI systems as one index or ranking system. Distinguish:

- generative features inside traditional search;
- standalone answer products with web retrieval;
- training crawlers;
- search/retrieval crawlers;
- user-triggered fetchers or browser agents;
- model knowledge without live retrieval;
- merchant, local, news, video, and other vertical feeds.

Controls, freshness, attribution, and measurement differ by surface.

## 2. Preserve the foundation

AI visibility usually depends on the same durable prerequisites:

- public crawl access for the intended retrieval bot;
- indexable, canonical, stable URLs;
- important information available as text;
- clear entities and relationships;
- original, accurate, current, source-backed content;
- strong internal discovery and external recognition;
- structured data consistent with visible claims;
- good user experience and accessible media;
- current merchant, business, or publisher feeds where relevant.

Do not replace these with speculative AEO/GEO hacks.

Negotiated Markdown can make retrieval smaller and cleaner for clients that request it, but it is not required for Google Search visibility and is not a substitute for an accessible, indexable HTML page. Use it only from the canonical source with correct negotiation, caching, parity, and measurement. Treat emerging browser-agent action protocols as a separate progressive-enhancement decision.

## 3. Crawler policy

Create a policy matrix before editing robots.txt:

| Agent | Purpose | Desired access | Business rationale | Verified source/date |
|---|---|---|---|---|
| Search crawler | retrieval/search inclusion | allow/block | discoverability choice | first-party docs |
| Training crawler | model training | allow/block | rights/strategy choice | first-party docs |
| User fetcher | user-triggered access | contextual | utility/security choice | first-party docs |

For OpenAI, OAI-SearchBot and GPTBot represent independent search and training choices; ChatGPT-User is user-triggered and may not behave like an automatic crawler. Verify current names, IP guidance, and semantics before changing production policy.

For Google Search AI features, current Google guidance says normal Search eligibility and snippet controls apply and special AI markup is not required. Verify this remains current.

Never frame crawler access as consent to every possible downstream use. Coordinate with legal/privacy/product owners when policy is material.

## 4. Create citable information

Improve the probability that a system can retrieve, understand, and accurately cite the page:

- state the page's subject and answer plainly;
- define terms and disambiguate entities;
- use descriptive headings and coherent sections;
- support claims with primary evidence, dates, units, methods, and limitations;
- expose original tables, examples, statistics, and comparisons in accessible text/HTML;
- keep author, organization, product, and source identities consistent;
- update materially changed information and retain provenance;
- provide stable anchors/URLs when useful to humans;
- align text, images, video, feeds, and structured data.

Do not mechanically “chunk” every paragraph, manufacture quotations, or add an FAQ solely for bots. Extractability is a byproduct of clear information design.

## 5. Search-everywhere strategy

Map where the audience actually discovers and validates answers:

- web search and AI answers;
- YouTube/video and image search;
- maps/local platforms;
- marketplaces and merchant surfaces;
- forums, communities, review sites, and industry publications;
- social platforms and podcasts;
- knowledge bases, documentation, repositories, and app ecosystems.

Optimize the native asset and the owned landing experience. Build recognizable entity consistency across credible surfaces. Seek mentions because they reach and persuade the audience, not merely to seed models.

## 6. AI-assisted research and production

Use AI for:

- query fan-out and subtopic hypothesis generation;
- source discovery and competitive gap organization;
- entity/claim inventories;
- transcript, schema, and metadata drafts;
- log/report summarization;
- QA checklists and test generation.

Require source verification for facts and current platform behavior. Keep prompts and outputs out of publication when they contain confidential, personal, licensed, or unverified material. An LLM-generated competitor/content gap is a lead for research, not evidence.

## 7. Measurement

Track separately:

- citations and cited URLs where platform reporting exists;
- brand/product mentions for a controlled prompt/query set;
- accuracy, sentiment, and competitor inclusion;
- AI referrals using documented source/medium rules;
- branded search lift and direct traffic as weak, confounded supporting signals;
- conversions and assisted outcomes from identifiable AI traffic;
- classic search impressions/clicks for queries affected by AI features.

Version the prompt set, model/product, login/location, date, and methodology. Outputs are probabilistic and personalized; one screenshot is anecdotal.

Do not equate mention share with revenue or citation count with authority. Use repeated measurements and business outcomes.

## 8. Myths and anti-patterns

- `llms.txt` and Markdown are not Google Search inclusion or ranking requirements. Implement negotiated Markdown or generated agent indexes only for a defined consumer/use case and never instead of crawl/index fundamentals.
- There is no universal “AI schema.” Use supported schema that truthfully describes visible content.
- Keyword stuffing for embeddings harms clarity and trust.
- Publishing generic AI summaries adds little retrievable value.
- Fake mentions, synthetic reviews, purchased citations, and coordinated spam create policy and reputation risk.
- Blocking training does not necessarily block search inclusion; blocking one bot does not define every product's behavior.
- AI answer visibility does not guarantee a click. Design brand memory, useful next actions, tools, subscriptions, and conversion paths accordingly.

## 9. Answer-surface audit

For priority tasks:

1. Define a stable, representative query/prompt set.
2. Observe which surfaces appear and what sources/entities they use.
3. Check whether the owned site is technically eligible and fresh.
4. Compare cited competitors on unique evidence, entity clarity, structure, format, and recognition.
5. Correct inaccurate or ambiguous owned information at the source.
6. Build the missing primary evidence or utility.
7. Promote it to relevant people and platforms.
8. Re-measure with the same method and record uncertainty.
