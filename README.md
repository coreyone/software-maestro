# Software Maestro

Capability orchestra of 85 agent skills for AI IDE agents. Conducts product strategy, design systems, engineering execution, data science & causal inference, security, growth, and quality from a single developer baton.

## Install

```bash
npx skills add coreyone/software-maestro
```
*(Alternative: clone directly to the target AI IDE config/skills directory. The shared Agent Skills format is intended to work across Claude Code, Gemini CLI, OpenAI Codex, and other compatible runtimes.)*

## Lifecycle Structure

*   **product/** (26 skills): Strategy, Product Operations, Pod Orchestration & execution governance (product-zero-to-one, product-growth, product-optimizer-feature, product-marketplace, michael-bolton-pod-conductor, product-marketing-narrative, continuous-product-loop, create-prd, product-pricing-strategy, product-management, product-management-press-memo, product-strategy-outcome-vision, proven-product-spec, ux-discovery-artifacts, how-might-we, michael-bolton-rule, swarm-rules, god-marduk, release-readiness-gtm, voc-insights-pipeline, portfolio-allocation-capitalization, decision-stack-governance, systems-retro-pruning, strategic-tradeoffs-constraint-matrix, incentive-design-metric-trees, platform-enablement-internal-leverage). Validates customer truth before roadmaps. Coordinates cross-functional product pods across 5 lifecycle movements, frames 3-tier PMM messaging hierarchies, connects financial decisions to product investments, gates cross-functional GTM releases, synthesizes multi-channel VoC, defines where NOT to play, structures metric trees, and prunes operational waste.
*   **design/** (11 skills): Wayfinding, onboarding & visual systems (design-user-onboarding-ux, aesthetic-rules, aesthetic-science, design-responsive-rules, design-animation, design-system-rules, design-usability-rules, design-review-rules, design-information-architecture-rules, chart-communication, failure-states-empty-states). Structures for instant orientation (IA), cognitive friction-free onboarding, WCAG AA typography-first layout, perceptual physics, and tactile microinteractions.
*   **engineering/** (12 skills): Clean code, architecture, multi-cloud networking, and governed improvement workflows (developer-development-rules, developer-code-review-rules, improve-codebase, developer-test-driven-development, developer-eval-driven-development, system-architecture-rules, resiliency-circuit-breakers, tech-stack-preferences, hybrid-cloud-networking, multi-cloud-architecture, terraform-module-library, info-to-ink). Isolates components, decouples modules, provisions multi-cloud infrastructure, and improves probabilistic behavior through versioned baselines, calibrated evaluators, and regression datasets.
*   **data-and-api/** (5 skills): Causal inference, KPI triage, semantic layers, contract-first endpoints & persistence schemas (data-science-causal-inference, product-data-metric-investigation-triage, data-warehouse-semantic-layer, api-design-guidelines, data-persistence-caching). Formulates quasi-experiments (CUPED, DiD, SCM, RDD), mathematically decomposes metric drops (Volume vs Rate vs Mix/Simpson's Paradox), builds dbt dimensional star schemas with enforced YAML data contracts and MetricFlow semantic layers.
*   **security/** (5 skills): Identity, zero-trust mTLS & sandbox trust boundaries (auth-and-identity-rules, developer-security, developer-web-security, mtls-configuration, secrets-management). Isolates tokens (Keychain/HttpOnly cookies), enforces mutual TLS service communication, secures secrets pipelines, and cryptographically validates JWTs.
*   **growth/** (11 skills): Organic discovery, conversions, behavioral loops, experimentation & commercial negotiation (developer-seo, commerce-ux-rules, cro-commerce-audit, design-forms-wizards-checkout, marketing-copy-emotion-provoking-action-driven, the-elements-of-style-principles, analytics-event-tracking, negotiation-maximizer, experimentation-hypothesis-engine, behavioral-loops-retention-modeling, marketing-lifecycle-crm-automation). Builds durable search visibility, automates multi-channel Push/Email/SMS lifecycle waterfalls, sizes A/B test hypotheses, uncovers predictive Aha moments, models habit loops, and flattens cohort retention decay.
*   **quality/** (15 skills): Graceful degradation, APM telemetry, service mesh observability, CI/CD pipelines, cloud cost governance, headless browser inspection, endpoint discovery, edge deployments, and reusable design/art-direction systems (a11y-debugging, developer-web-performance, observability-telemetry, service-mesh-observability, istio-traffic-management, linkerd-patterns, deployment-pipeline-design, github-actions-templates, gitlab-ci-patterns, cost-optimization, web-deployment-rules, peekaboo, chrome-devtools, web-endpoint-documenter, create-design-art-direction). Replaces loaders with layout-matching skeletons, optimizes cloud infrastructure costs, automates progressive canary delivery, and enforces zero-downtime database migrations (Expand/Contract).

## Taxonomy

```
├── product/          # Strategy, 0-to-1, Growth, Optimizer, Marketplace, Pod Orchestration & governance (26 skills)
├── design/           # User onboarding & FTUX, aesthetic rules, responsive layout, motion, chart communication, skeletons, empty states (11 skills)
├── engineering/      # Code quality, audits, architecture, multi-cloud networking, resiliency, TDD, eval-driven development, IaC (12 skills)
├── data-and-api/     # Causal inference, metric investigation triage, dbt dimensional semantic layers, REST/GraphQL API design, caching (5 skills)
├── security/         # Authentication protocols, identity keys, secure cookies, mTLS, CI/CD secrets management (5 skills)
├── growth/           # SEO, lifecycle CRM automation, commerce UX, CRO, experimentation sizing, retention modeling, copywriting, analytics (11 skills)
└── quality/          # Performance debugging, telemetry, service mesh, CI/CD pipelines, FinOps cost, deployments, a11y, automation (15 skills)
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
