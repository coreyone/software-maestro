# software-maestro

A capability orchestra of 62 lean agent skills for AI IDE agents (Claude Code, Codex, Antigravity, Gemini).

---

## 🎯 Architecture & Intent

`software-maestro` structures skills into 12 core domains. Redundant micro-skills are consolidated into **Unified Hero Hubs** to reduce cognitive choice paralysis, eliminate near-synonym overlap, and prevent prompt token bloat while preserving 100% of expert frameworks.

---

## 🧭 Lifecycle Domains

<details>
<summary><strong><code>product/</code></strong> (14 skills across 5 subdomains)</summary>

*   **`product/archetypes/`** (1 skill): Master Product Management router covering 0-to-1 search, growth loops, feature optimization, and 2-sided marketplaces (`product-management`).
*   **`product/orchestration/`** (4 skills): God-Marduk master phased sequencing, Michael Bolton Pod Conductor, Bolton Delegation Doctrine, and Swarm Concurrency with Andon Cord & small-batch rules (`god-marduk`, `michael-bolton-pod-conductor`, `michael-bolton-rule`, `swarm-rules`).
*   **`product/strategy/`** (3 skills): Melissa Perri Decision Stack & portfolio governance, Tara Seshan empirical hypothesis loop, and pricing strategy (`decision-stack-governance`, `product-hypothesis-loop`, `product-pricing-strategy`).
*   **`product/discovery-and-specs/`** (3 skills): Outcome-oriented PRD compiler with BDD/Gherkin and Definition of Done gates, Tracer-bullet ticket compiler with blocking DAGs, and Voice of Customer synthesis (`create-prd`, `prd-to-tickets`, `voc-insights-pipeline`).
*   **`product/operations-and-gtm/`** (3 skills): Continuous product loop, GTM release readiness gating, and systems retrospective pruning (`continuous-product-loop`, `release-readiness-gtm`, `systems-retro-pruning`).

</details>

<details>
<summary><strong><code>design/</code></strong> (9 skills across 5 subdomains)</summary>

*   **`design/sprints-and-ideation/`** (1 skill): Jake Knapp Design Sprint master hub covering Monday Understand & Map, Tuesday Crazy 8s Diverge, and Wednesday Sticky Decision Storyboarding (`design-sprint`).
*   **`design/systems-and-foundations/`** (1 skill): Foundational design system tokens, visual typography scale, and aesthetic principles (`design-system-rules`).
*   **`design/interaction-and-layout/`** (3 skills): Responsive layout breakpoints, motion physics, and wayfinding architecture (`design-responsive-rules`, `design-animation`, `design-information-architecture-rules`).
*   **`design/experience-and-flows/`** (3 skills): First-time user onboarding, Hollywood prototype facades with 5-Act user testing, and cognitive chart visualization (`design-user-onboarding-ux`, `design-rapid-prototype-facade`, `chart-communication`).
*   **`design/evaluation-and-quality/`** (1 skill): Nielsen Norman usability heuristics and visual design review audits (`design-usability-rules`).

</details>

<details>
<summary><strong><code>engineering/</code></strong> (9 skills across 3 subdomains)</summary>

*   **`engineering/development-and-quality/`** (6 skills): Core engineering craft, code review checklists, Test-Driven Development (TDD), evaluation-driven AI development, ASD-STE100 technical writing standards, and info-to-ink token compression (`developer-development-rules`, `developer-code-review-rules`, `developer-test-driven-development`, `developer-eval-driven-development`, `technical-language-rules`, `info-to-ink`).
*   **`engineering/architecture-and-resiliency/`** (2 skills): Clean/Hexagonal system architecture with circuit breakers and zero-key web search grounding (`system-architecture-rules`, `grounded-search-rules`).
*   **`engineering/cloud-and-infrastructure/`** (1 skill): Multi-cloud architecture, hybrid cloud networking, and reusable Terraform IaC modules (`multi-cloud-architecture`).

</details>

<details>
<summary><strong><code>finance/</code></strong> (1 skill)</summary>

*   **`finance-payments-tax-and-treasury`**: Multi-rail settlement reconciliation (FedNow, RTP, SEPA, Pix, Card Networks), multi-jurisdiction tax nexus & statutory reporting (1099-K, DAC7, VAT, TOT), automated chargeback dispute defense, and treasury liquidity rebalancing.

</details>

<details>
<summary><strong><code>trust/</code></strong> (1 skill)</summary>

*   **`trust-safety-fraud-and-claims`**: Multimodal content moderation, counterfeit goods & policy enforcement, KYC/KYB & OFAC/PEP sanctions screening, and binding physical damage claim adjudication (AirCover, damaged shipments).

</details>

<details>
<summary><strong><code>legal/</code></strong> (1 skill)</summary>

*   **`legal-contracts-and-compliance`**: Autonomous enterprise contract redlining (MSAs, DPAs, SLAs), security questionnaire automation (Whistic, Conveyor, OneTrust), and continuous audit evidence harvesting (SOC 2, ISO 27001, PCI-DSS, EU AI Act).

</details>

<details>
<summary><strong><code>ops/</code></strong> (1 skill)</summary>

*   **`ops-incident-and-crisis-response`**: Mission-critical SEV-0/1 war room triage, canary kill & traffic shedding containment, public status communications, high-empathy customer crisis override resolution, and blameless 5-Whys RCAs.

</details>

<details>
<summary><strong><code>data-and-api/</code></strong> (3 skills)</summary>

*   **`api-design-guidelines`**: REST/GraphQL schema contracts, RFC 7807 error patterns, and database caching.
*   **`data-persistence-caching`**: Database schema indexing, cache-aside patterns, and query performance tuning.
*   **`data-science-causal-inference`**: Causal inference (DiD, Synthetic Control, CUPED), metric triage, and dbt dimensional semantic layers.

</details>

<details>
<summary><strong><code>security/</code></strong> (2 skills)</summary>

*   **`developer-security`**: Backend/frontend threat modeling, OWASP Top 10 mitigation, CSP headers, and CI/CD secrets management.
*   **`auth-and-identity-rules`**: OAuth 2.1 PKCE, JWT session control, and zero-trust mTLS service identity.

</details>

<details>
<summary><strong><code>growth/</code></strong> (5 skills)</summary>

*   **`analytics-event-tracking`**: Behavioral telemetry taxonomies, retention modeling, and CRM lifecycle automation.
*   **`commerce-ux-rules`**: Shopping cart optimization, checkout friction reduction, and multi-step wizard forms.
*   **`developer-seo`**: Technical search engine optimization, semantic metadata, and structured schema tags.
*   **`experimentation-hypothesis-engine`**: Statistical A/B testing, MDE sample sizing, SRM validation, and 3-way post-mortems.
*   **`conversion-copywriting`**: High-conversion landing page copy, value propositions, and concise prose.

</details>

<details>
<summary><strong><code>quality/</code></strong> (8 skills)</summary>

*   **`a11y-debugging`**: WCAG AA accessibility compliance, keyboard navigation, and ARIA tree auditing.
*   **`chrome-devtools`**: Headless browser automation, page element snapshot inspection, and console debugging.
*   **`cost-optimization`**: Multi-cloud FinOps spending analysis, resource rightsizing, and cost governance.
*   **`deployment-pipeline-design`**: Multi-stage CI/CD deployment pipelines (GitHub Actions / GitLab CI) with canary gates.
*   **`dogfood`**: Systematic exploratory web testing with step-by-step bug reproduction videos and screenshots.
*   **`observability-telemetry`**: Structured logging, OpenTelemetry tracing, and service mesh monitoring.
*   **`peekaboo`**: macOS native desktop GUI automation, window management, and system dialog interactions.
*   **`web-perf`**: Core Web Vitals (LCP, INP, CLS) performance auditing and resource optimization.

</details>

<details>
<summary><strong><code>productivity-maestro/</code></strong> (5 skills across 2 subdomains)</summary>

*   **`productivity-maestro/executive-and-async/`** (2 skills): Multi-paradigm meeting intelligence (McKinsey SCQA / Amazon PR/FAQ) and Axios Smart Brevity asynchronous decision memos (`meeting-transcription-notes`, `executive-async-memo`).
*   **`productivity-maestro/scrum-cadences/`** (3 skills): Original Scrum Cybernetic Behavioral Harness cadences paired by cycle phase: (1) Sprint Planning & DEEP Backlog Refinement, (2) Daily Synchronization & 24h Drift Triage, and (3) Sprint Review (DoD) & Egoless Retrospective (Kaizen) (`scrum-planning-and-refinement`, `scrum-daily-sync`, `scrum-review-and-retro`).

</details>

---

## 🌳 Taxonomy Tree

```
├── product/                  # Product Management & Orchestration (14 skills)
│   ├── archetypes/           # Master PM archetype router (1 skill)
│   ├── orchestration/        # God-Marduk, Bolton Conductor, Bolton Rule, Swarm Rules (4 skills)
│   ├── strategy/             # Decision Stack, Hypothesis Loop, Pricing Strategy (3 skills)
│   ├── discovery-and-specs/  # PRD Compiler, PRD-to-Tickets, VoC Pipeline (3 skills)
│   └── operations-and-gtm/   # Continuous Loop, GTM Release, Systems Retro Pruning (3 skills)
├── design/                   # Visual Systems, Design Sprints, Layout & Motion (9 skills)
│   ├── sprints-and-ideation/ # Jake Knapp Design Sprint Master Hub (1 skill)
│   ├── systems-and-foundations/ # Design system tokens & visual scale (1 skill)
│   ├── interaction-and-layout/  # Responsive layouts, animation physics, IA wayfinding (3 skills)
│   ├── experience-and-flows/    # Onboarding UX, Prototype Facade, Chart viz (3 skills)
│   └── evaluation-and-quality/  # Usability heuristics & design audits (1 skill)
├── engineering/              # Code Quality, Architecture, Cloud & IaC (9 skills)
│   ├── development-and-quality/ # TDD, evals, code reviews, craft, STE prose, info-to-ink (6 skills)
│   ├── architecture-and-resiliency/ # System architecture, grounded search (2 skills)
│   └── cloud-and-infrastructure/ # Multi-cloud architecture & Terraform IaC (1 skill)
├── finance/                  # Settlement rails, tax nexus, chargebacks & treasury (1 skill)
├── trust/                    # Content moderation, KYC/AML, fraud & physical claims (1 skill)
├── legal/                    # Enterprise contract redlining, security QA & audit vault (1 skill)
├── ops/                      # SEV-0 incident command, crisis comms & blameless RCA (1 skill)
├── data-and-api/             # API guidelines, caching, and causal inference data layers (3 skills)
├── security/                 # Developer security & auth/identity rules (2 skills)
├── growth/                   # Telemetry, commerce UX, SEO, experimentation, copy (5 skills)
├── quality/                  # CI/CD, FinOps, dogfooding, a11y, observability, web perf, peekaboo (8 skills)
└── productivity-maestro/      # Executive memos, meeting intelligence & 3-tier Scrum cadences (5 skills)
    ├── executive-and-async/  # Meeting intelligence & Smart Brevity async memos (2 skills)
    └── scrum-cadences/       # Planning/Refinement, Daily Sync, Review/Retro (3 skills)
```

---

## 🧪 Binary Evals & Verification

Run automated local evaluation suites across all skills:

```bash
python3 scripts/check_binary_evals.py
```
