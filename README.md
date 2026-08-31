# Software Maestro

A capability orchestra of 90 agent skills for AI IDE agents. You conduct product strategy, design systems, engineering execution, data science, security, growth, quality, and operational cadences from one developer baton.

## Install

Run the following command in your terminal:

```bash
npx skills add coreyone/software-maestro
```

Alternatively, clone this repository directly into your AI IDE configuration directory. This format works across Claude Code, Gemini CLI, OpenAI Codex, and compatible runtimes.

## Lifecycle Structure

<details>
<summary><strong><code>product/</code></strong> (26 skills across 5 subdomains)</summary>

*   **`product/archetypes/`** (5 skills): Specialized product manager archetypes and core routing engine (`product-management`, `product-zero-to-one`, `product-growth`, `product-optimizer-feature`, `product-marketplace`).
*   **`product/orchestration/`** (4 skills): Cross-functional pod conductors, delegation doctrine, and multi-agent swarm operations (`michael-bolton-pod-conductor`, `michael-bolton-rule`, `swarm-rules`, `god-marduk`).
*   **`product/strategy/`** (5 skills): Executive strategy deployment, decision stacks, capital allocation, pricing, and strategic constraints (`decision-stack-governance`, `product-strategy-outcome-vision`, `portfolio-allocation-capitalization`, `strategic-tradeoffs-constraint-matrix`, `product-pricing-strategy`).
*   **`product/discovery-and-specs/`** (6 skills): Customer problem discovery, opportunity mapping, market benchmarks, VoC synthesis, and decision-ready PRDs (`create-prd`, `proven-product-spec`, `ux-discovery-artifacts`, `voc-insights-pipeline`, `how-might-we`, `product-management-press-memo`).
*   **`product/operations-and-gtm/`** (6 skills): Continuous evolution loops, GTM launch gating, PMM messaging, metric trees, platform primitives, and operational waste pruning (`continuous-product-loop`, `release-readiness-gtm`, `product-marketing-narrative`, `incentive-design-metric-trees`, `platform-enablement-internal-leverage`, `systems-retro-pruning`).

</details>

<details>
<summary><strong><code>design/</code></strong> (11 skills across 4 subdomains)</summary>

*   **`design/systems-and-foundations/`** (3 skills): Foundational design systems, visual tokens, and perceptual neuroscience (`design-system-rules`, `aesthetic-rules`, `aesthetic-science`).
*   **`design/interaction-and-layout/`** (3 skills): Spatial layout, responsive breakpoints, motion physics, and wayfinding architecture (`design-responsive-rules`, `design-animation`, `design-information-architecture-rules`).
*   **`design/experience-and-flows/`** (3 skills): First-time user onboarding, empty/error state recovery, and cognitive data visualization (`design-user-onboarding-ux`, `failure-states-empty-states`, `chart-communication`).
*   **`design/evaluation-and-quality/`** (2 skills): Usability heuristics, Norman affordances, and visual design review audits (`design-usability-rules`, `design-review-rules`).

</details>

<details>
<summary><strong><code>engineering/</code></strong> (13 skills across 3 subdomains)</summary>

*   **`engineering/development-and-quality/`** (6 skills): Clean code craft, evidence-backed code reviews, TDD, eval-driven AI development, codebase audits, and output token efficiency (`developer-development-rules`, `developer-code-review-rules`, `developer-test-driven-development`, `developer-eval-driven-development`, `improve-codebase`, `info-to-ink`).
*   **`engineering/architecture-and-resiliency/`** (4 skills): Clean architecture, circuit breakers, standardized tech stacks, and web-search grounding backend adapters (`system-architecture-rules`, `resiliency-circuit-breakers`, `tech-stack-preferences`, `grounded-search-rules`).
*   **`engineering/cloud-and-infrastructure/`** (3 skills): Multi-cloud architecture, hybrid cross-premises networking, and reusable Terraform IaC modules (`multi-cloud-architecture`, `hybrid-cloud-networking`, `terraform-module-library`).

</details>

<details>
<summary><strong><code>data-and-api/</code></strong> (5 skills)</summary>

*   Causal inference, KPI triage, semantic layers, contract-first endpoints, and persistence schemas (`data-science-causal-inference`, `product-data-metric-investigation-triage`, `data-warehouse-semantic-layer`, `api-design-guidelines`, `data-persistence-caching`). Formulates quasi-experiments (CUPED, DiD, SCM, RDD), decomposes metric shifts (Volume vs. Rate vs. Mix), and builds dbt star schemas with enforced data contracts.

</details>

<details>
<summary><strong><code>security/</code></strong> (5 skills)</summary>

*   Identity, zero-trust mTLS, and sandbox trust boundaries (`auth-and-identity-rules`, `developer-security`, `developer-web-security`, `mtls-configuration`, `secrets-management`). Isolates session tokens, enforces mutual TLS service communication, secures secrets pipelines, and validates JWTs cryptographically.

</details>

<details>
<summary><strong><code>growth/</code></strong> (11 skills)</summary>

*   Organic discovery, conversions, behavioral loops, experimentation, and commercial negotiation (`developer-seo`, `commerce-ux-rules`, `cro-commerce-audit`, `design-forms-wizards-checkout`, `marketing-copy-emotion-provoking-action-driven`, `the-elements-of-style-principles`, `analytics-event-tracking`, `negotiation-maximizer`, `experimentation-hypothesis-engine`, `behavioral-loops-retention-modeling`, `marketing-lifecycle-crm-automation`). Builds search visibility, automates multi-channel Push/Email/SMS waterfalls, sizes A/B experiments, models habit loops, and flattens cohort retention decay.

</details>

<details>
<summary><strong><code>quality/</code></strong> (15 skills)</summary>

*   Graceful degradation, APM telemetry, service mesh observability, CI/CD pipelines, cloud cost governance, headless browser inspection, endpoint discovery, and edge deployments (`a11y-debugging`, `developer-web-performance`, `observability-telemetry`, `service-mesh-observability`, `istio-traffic-management`, `linkerd-patterns`, `deployment-pipeline-design`, `github-actions-templates`, `gitlab-ci-patterns`, `cost-optimization`, `web-deployment-rules`, `peekaboo`, `chrome-devtools`, `web-endpoint-documenter`, `create-design-art-direction`). Replaces loaders with layout-matching skeletons, optimizes cloud infrastructure costs, automates progressive canary delivery, and enforces zero-downtime database migrations.

</details>

<details>
<summary><strong><code>productivity-maestro/</code></strong> (4 skills)</summary>

*   Operational intelligence, executive synthesis, task triage, and high-output 1:1 cadences (`meeting-transcription-notes`, `executive-async-memo`, `weekly-review-triage`, `one-on-one-cadence`). Distills multi-speaker meeting transcripts into structured operational decision records, synthesizes Slack and email threads into Smart Brevity memos, executes GTD Eisenhower triage, and runs Andy Grove 1:1 cadences with two-way commitment contracts.

</details>

## Taxonomy

```
├── product/                  # Product Management & Orchestration (26 skills across 5 IA subdomains)
│   ├── archetypes/           # 0-to-1, Growth, Optimizer, Marketplace, Base PM router (5 skills)
│   ├── orchestration/        # Pod Conductor, Bolton Rule, Swarm Rules, God-Marduk (4 skills)
│   ├── strategy/             # Decision Stack, Strategy Vision, Capital Allocation, Constraints, Pricing (5 skills)
│   ├── discovery-and-specs/  # PRDs, Proven Specs, UX Discovery, VoC Pipeline, HMW, Press Memo (6 skills)
│   └── operations-and-gtm/   # Continuous Loop, GTM Release, PMM Narrative, Metric Trees, Platforms, Retro Pruning (6 skills)
├── design/                   # Visual Systems, Layout, Motion & Usability (11 skills across 4 IA subdomains)
│   ├── systems-and-foundations/ # Design tokens, aesthetic rules, aesthetic science (3 skills)
│   ├── interaction-and-layout/  # Responsive layouts, animation physics, IA wayfinding (3 skills)
│   ├── experience-and-flows/    # FTUX onboarding, empty/failure states, chart visualization (3 skills)
│   └── evaluation-and-quality/  # Usability heuristics, visual design review audits (2 skills)
├── engineering/              # Code Quality, Architecture, Cloud & IaC (13 skills across 3 IA subdomains)
│   ├── development-and-quality/ # TDD, evals, code reviews, audits, craft, info-to-ink (6 skills)
│   ├── architecture-and-resiliency/ # System architecture, circuit breakers, tech stack, search grounding (4 skills)
│   └── cloud-and-infrastructure/ # Multi-cloud, hybrid networking, Terraform IaC (3 skills)
├── data-and-api/             # Causal inference, metric investigation triage, dbt dimensional semantic layers, REST/GraphQL API, caching (5 skills)
├── security/                 # Authentication protocols, identity keys, secure cookies, mTLS, CI/CD secrets management (5 skills)
├── growth/                   # SEO, lifecycle CRM automation, commerce UX, CRO, experimentation sizing, retention modeling, copywriting, analytics (11 skills)
├── quality/                  # Performance debugging, telemetry, service mesh, CI/CD pipelines, FinOps cost, deployments, a11y, automation (15 skills)
└── productivity-maestro/      # Meeting intelligence, Smart Brevity async memos, GTD/Eisenhower triage, Andy Grove 1:1s (4 skills)
```

## Binary evals

High-contract skills include `evals/cases.json` suites with positive and negative trigger prompts, atomic pass/fail rules, and known-pass/known-fail fixtures.

Validate every suite by running:

```bash
python3 scripts/check_binary_evals.py
```

Score a candidate response against a single case:

```bash
python3 scripts/check_binary_evals.py path/to/skill --case case-id --response response.txt
```
