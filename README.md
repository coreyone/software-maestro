# Software Maestro

Capability orchestra for AI IDE agents. Conducts product strategy, design systems, engineering execution, data science & causal inference, growth, and negotiation from a single developer baton.

## Install

```bash
npx skills add coreyone/software-maestro
```
*(Alternative: clone directly to the target AI IDE config/skills directory. The shared Agent Skills format is intended to work across Claude Code, Gemini CLI, OpenAI Codex, and other compatible runtimes.)*

## Lifecycle Structure

*   **product/**: Strategy, Product Operations, Pod Orchestration & execution governance (michael-bolton-pod-conductor, product-marketing-narrative, continuous-product-loop, create-prd, product-pricing-strategy, product-management, product-management-press-memo, product-strategy-outcome-vision, proven-product-spec, ux-discovery-artifacts, how-might-we, michael-bolton-rule, swarm-rules, god-marduk, release-readiness-gtm, voc-insights-pipeline, portfolio-allocation-capitalization, decision-stack-governance, systems-retro-pruning, strategic-tradeoffs-constraint-matrix, incentive-design-metric-trees, platform-enablement-internal-leverage). Validates customer truth before roadmaps. Coordinates cross-functional product pods across 5 lifecycle movements, frames 3-tier PMM messaging hierarchies, connects financial decisions to product investments, gates cross-functional GTM releases, synthesizes multi-channel VoC, defines where NOT to play, structures metric trees, and prunes operational waste.
*   **design/**: Wayfinding, onboarding & visual systems (design-user-onboarding-ux, aesthetic-rules, responsive-rules, design-animation, design-system-rules, design-usability-rules, chart-communication, failure-states-empty-states). Structures for instant orientation (IA), cognitive friction-free onboarding, WCAG AA typography-first layout, and tactile microinteractions.
*   **engineering/**: Clean code, architecture, and governed improvement workflows (developer-development, code-review, improve-codebase, TDD, eval-driven development, system-architecture, resiliency, tech-stack). Isolates components, decouples modules, and improves probabilistic behavior through versioned baselines, calibrated evaluators, and regression datasets.
*   **data-and-api/**: Causal inference, KPI triage, semantic layers, contract-first endpoints & persistence schemas (data-science-causal-inference, product-data-metric-investigation-triage, data-warehouse-semantic-layer, api-design-guidelines, data-persistence-caching). Formulates quasi-experiments (CUPED, DiD, SCM, RDD), mathematically decomposes metric drops (Volume vs Rate vs Mix/Simpson's Paradox), builds dbt dimensional star schemas with enforced YAML data contracts and MetricFlow semantic layers.
*   **security/**: Identity & sandbox trust boundaries (developer-security, developer-web-security, auth-and-identity-rules). Isolates tokens (Keychain/HttpOnly cookies) and cryptographically validates JWTs.
*   **growth/**: Organic discovery, conversions, behavioral loops, experimentation & commercial negotiation (developer-seo, commerce-ux, cro-commerce-audit, design-forms, marketing-copy, elements-of-style, analytics-event-tracking, negotiation-maximizer, experimentation-hypothesis-engine, behavioral-loops-retention-modeling, marketing-lifecycle-crm-automation). Builds durable search visibility, automates multi-channel Push/Email/SMS lifecycle waterfalls, sizes A/B test hypotheses, uncovers predictive Aha moments, models habit loops, and flattens cohort retention decay.
*   **quality/**: Graceful degradation, APM telemetry, headless browser inspection, endpoint discovery, edge deployments, and reusable design/art-direction systems (a11y-debugging, web-performance, telemetry, web-deployment, peekaboo, chrome-devtools, web-endpoint-documenter, create-design-art-direction). Replaces loaders with layout-matching skeletons. Enforces zero-downtime database migrations (Expand/Contract).

## Taxonomy

```
├── product/          # Strategy, Pod Orchestration & governance (michael-bolton-pod-conductor, product-marketing-narrative, continuous-product-loop, create-prd, pricing, outcome-vision, proven-spec, ux-discovery, god-marduk, release-readiness-gtm, voc-insights-pipeline, portfolio-capitalization, decision-stack-governance, systems-retro-pruning, strategic-tradeoffs-constraint-matrix, incentive-design-metric-trees, platform-enablement-internal-leverage)
├── design/           # User onboarding & FTUX, aesthetic rules, responsive layout, motion, chart communication, skeletons, empty states
├── engineering/      # Code quality, audits, implementation planning, architecture, resiliency, TDD, eval-driven development
├── data-and-api/     # Causal inference, metric investigation triage, dbt dimensional semantic layers, REST/GraphQL API design, caching
├── security/         # Authentication protocols, identity keys, secure cookies, keychain
├── growth/           # SEO, lifecycle CRM automation, commerce UX, CRO, experimentation sizing, retention modeling, copywriting, analytics
└── quality/          # Performance debugging, telemetry observability, deployments, a11y audit, chrome automation, endpoint discovery, design/art direction
```

## Binary evals

High-contract skills include `evals/cases.json` suites with positive and negative trigger prompts, atomic pass/fail rules, and known-pass/known-fail fixtures. Validate every suite:

```bash
python scripts/check_binary_evals.py
```

Score a candidate response against one case:

```bash
python scripts/check_binary_evals.py path/to/skill --case case-id --response response.txt
```
