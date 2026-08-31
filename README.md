# Software Maestro

Capability orchestra of 90 agent skills for AI IDE agents. Conducts product strategy, design systems, engineering execution, data science & causal inference, security, growth, quality, and day-to-day productivity operations from a single developer baton.

## Install

```bash
npx skills add coreyone/software-maestro
```
*(Alternative: clone directly to the target AI IDE config/skills directory. The shared Agent Skills format is intended to work across Claude Code, Gemini CLI, OpenAI Codex, and other compatible runtimes.)*

## Lifecycle Structure

*   **product/** (26 skills organized across 5 Information Architecture subdomains):
    *   **`product/archetypes/`** (5 skills): Specialized product manager archetypes and core routing engine (`product-management`, `product-zero-to-one`, `product-growth`, `product-optimizer-feature`, `product-marketplace`).
    *   **`product/orchestration/`** (4 skills): Cross-functional pod conductors, delegation doctrine, and multi-agent swarm operations (`michael-bolton-pod-conductor`, `michael-bolton-rule`, `swarm-rules`, `god-marduk`).
    *   **`product/strategy/`** (5 skills): Executive strategy deployment, decision stacks, capital allocation, pricing, and strategic constraints (`decision-stack-governance`, `product-strategy-outcome-vision`, `portfolio-allocation-capitalization`, `strategic-tradeoffs-constraint-matrix`, `product-pricing-strategy`).
    *   **`product/discovery-and-specs/`** (6 skills): Customer problem discovery, opportunity mapping, market benchmarks, VoC synthesis, and decision-ready PRDs (`create-prd`, `proven-product-spec`, `ux-discovery-artifacts`, `voc-insights-pipeline`, `how-might-we`, `product-management-press-memo`).
    *   **`product/operations-and-gtm/`** (6 skills): Continuous evolution loops, GTM launch gating, PMM messaging, metric trees, platform primitives, and operational waste pruning (`continuous-product-loop`, `release-readiness-gtm`, `product-marketing-narrative`, `incentive-design-metric-trees`, `platform-enablement-internal-leverage`, `systems-retro-pruning`).
*   **design/** (11 skills): Wayfinding, onboarding & visual systems (design-user-onboarding-ux, aesthetic-rules, aesthetic-science, design-responsive-rules, design-animation, design-system-rules, design-usability-rules, design-review-rules, design-information-architecture-rules, chart-communication, failure-states-empty-states). Structures for instant orientation (IA), cognitive friction-free onboarding, WCAG AA typography-first layout, perceptual physics, and tactile microinteractions.
*   **engineering/** (13 skills): Clean code, architecture, multi-cloud networking, free search grounding, and governed improvement workflows (developer-development-rules, developer-code-review-rules, improve-codebase, developer-test-driven-development, developer-eval-driven-development, system-architecture-rules, resiliency-circuit-breakers, tech-stack-preferences, hybrid-cloud-networking, multi-cloud-architecture, terraform-module-library, info-to-ink, grounded-search-rules). Isolates components, decouples modules, provisions multi-cloud infrastructure, wires zero-key web-search grounding into backend adapters, and improves probabilistic behavior through versioned baselines, calibrated evaluators, and regression datasets.
*   **data-and-api/** (5 skills): Causal inference, KPI triage, semantic layers, contract-first endpoints & persistence schemas (data-science-causal-inference, product-data-metric-investigation-triage, data-warehouse-semantic-layer, api-design-guidelines, data-persistence-caching). Formulates quasi-experiments (CUPED, DiD, SCM, RDD), mathematically decomposes metric drops (Volume vs Rate vs Mix/Simpson's Paradox), builds dbt dimensional star schemas with enforced YAML data contracts and MetricFlow semantic layers.
*   **security/** (5 skills): Identity, zero-trust mTLS & sandbox trust boundaries (auth-and-identity-rules, developer-security, developer-web-security, mtls-configuration, secrets-management). Isolates tokens (Keychain/HttpOnly cookies), enforces mutual TLS service communication, secures secrets pipelines, and cryptographically validates JWTs.
*   **growth/** (11 skills): Organic discovery, conversions, behavioral loops, experimentation & commercial negotiation (developer-seo, commerce-ux-rules, cro-commerce-audit, design-forms-wizards-checkout, marketing-copy-emotion-provoking-action-driven, the-elements-of-style-principles, analytics-event-tracking, negotiation-maximizer, experimentation-hypothesis-engine, behavioral-loops-retention-modeling, marketing-lifecycle-crm-automation). Builds durable search visibility, automates multi-channel Push/Email/SMS lifecycle waterfalls, sizes A/B test hypotheses, uncovers predictive Aha moments, models habit loops, and flattens cohort retention decay.
*   **quality/** (15 skills): Graceful degradation, APM telemetry, service mesh observability, CI/CD pipelines, cloud cost governance, headless browser inspection, endpoint discovery, edge deployments, and reusable design/art-direction systems (a11y-debugging, developer-web-performance, observability-telemetry, service-mesh-observability, istio-traffic-management, linkerd-patterns, deployment-pipeline-design, github-actions-templates, gitlab-ci-patterns, cost-optimization, web-deployment-rules, peekaboo, chrome-devtools, web-endpoint-documenter, create-design-art-direction). Replaces loaders with layout-matching skeletons, optimizes cloud infrastructure costs, automates progressive canary delivery, and enforces zero-downtime database migrations (Expand/Contract).
*   **productivity-maestro/** (4 skills): Operational intelligence, executive synthesis, task triage, and high-output 1:1 cadences (meeting-transcription-notes, executive-async-memo, weekly-review-triage, one-on-one-cadence). Distills messy multi-speaker meeting transcripts into structured operational decision records across 5 corporate paradigms (McKinsey SCQA, Amazon Narrative, Apple DAP+DRI, Bridgewater 5 Whys, Tim Ferriss 80/20 MVN), synthesizes scattered Slack/email threads into Axios Smart Brevity async memos, executes GTD mind sweeps with Eisenhower 2x2 matrix triage and Weekly Big 3 calibration, and runs Andy Grove 4-pillar 1:1 cadences with two-way commitment contracts.

## Taxonomy

```
├── product/                  # Product Management & Orchestration (26 skills across 5 IA subdomains)
│   ├── archetypes/           # 0-to-1, Growth, Optimizer, Marketplace, Base PM router (5 skills)
│   ├── orchestration/        # Pod Conductor, Bolton Rule, Swarm Rules, God-Marduk (4 skills)
│   ├── strategy/             # Decision Stack, Strategy Vision, Capital Allocation, Constraints, Pricing (5 skills)
│   ├── discovery-and-specs/  # PRDs, Proven Specs, UX Discovery, VoC Pipeline, HMW, Press Memo (6 skills)
│   └── operations-and-gtm/   # Continuous Loop, GTM Release, PMM Narrative, Metric Trees, Platforms, Retro Pruning (6 skills)
├── design/                   # User onboarding & FTUX, aesthetic rules, responsive layout, motion, charts, skeletons (11 skills)
├── engineering/              # Code quality, audits, architecture, multi-cloud networking, search grounding, resiliency, TDD, eval-driven dev, IaC (13 skills)
├── data-and-api/             # Causal inference, metric investigation triage, dbt dimensional semantic layers, REST/GraphQL API, caching (5 skills)
├── security/                 # Authentication protocols, identity keys, secure cookies, mTLS, CI/CD secrets management (5 skills)
├── growth/                   # SEO, lifecycle CRM automation, commerce UX, CRO, experimentation sizing, retention modeling, copywriting, analytics (11 skills)
├── quality/                  # Performance debugging, telemetry, service mesh, CI/CD pipelines, FinOps cost, deployments, a11y, automation (15 skills)
└── productivity-maestro/      # Meeting intelligence, Smart Brevity async memos, GTD/Eisenhower triage, Andy Grove 1:1s (4 skills)
```

## Binary evals

High-contract skills include `evals/cases.json` suites with positive and negative trigger prompts, atomic pass/fail rules, and known-pass/known-fail fixtures. Validate every suite:

```bash
python3 scripts/check_binary_evals.py
```

Score a candidate response against one case:

```bash
python3 scripts/check_binary_evals.py path/to/skill --case case-id --response response.txt
```
