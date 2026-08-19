# Software Maestro

Capability orchestra for AI IDE agents. Conducts product strategy, design systems, engineering execution, growth, and negotiation from a single developer baton.

## Install

```bash
npx skills add coreyone/software-maestro
```
*(Alternative: clone directly to the target AI IDE config/skills directory. The shared Agent Skills format is intended to work across Claude Code, Gemini CLI, OpenAI Codex, and other compatible runtimes.)*

## Lifecycle Structure

*   **product/**: Strategy & execution governance (create-prd, product-management, product-management-press-memo, product-strategy-outcome-vision, ux-discovery-artifacts, michael-bolton-rule, swarm-rules, god-marduk). Validates customer truth before roadmaps. Decides what not to build.
*   **design/**: Wayfinding & visual systems (aesthetic-rules, responsive-rules, design-animation, design-system-rules, design-usability-rules, chart-communication). Structures for instant orientation (IA), WCAG AA typography-first layout, and tactile microinteractions.
*   **engineering/**: Clean code, architecture, and governed improvement workflows (developer-development, code-review, improve-codebase, TDD, eval-driven development, system-architecture, resiliency, tech-stack). Isolates components, decouples modules, and improves probabilistic behavior through versioned baselines, calibrated evaluators, and regression datasets.
*   **data-and-api/**: Contract-first endpoints & persistence schemas (api-design-guidelines, data-persistence-caching). Bypasses client-state latency using local memory replication.
*   **security/**: Identity & sandbox trust boundaries (developer-security, developer-web-security, auth-and-identity-rules). Isolates tokens (Keychain/HttpOnly cookies) and cryptographically validates JWTs.
*   **growth/**: Organic discovery, conversions, behavioral loops & commercial negotiation (developer-seo, commerce-ux, cro-commerce-audit, design-forms, marketing-copy, elements-of-style, analytics-event-tracking, negotiation-maximizer). Builds durable search and AI-answer visibility, qualifies traffic by business outcomes, standardizes event tracking (`object:action`), and maximizes negotiated value while keeping tactics invisible.
*   **quality/**: Graceful degradation, APM telemetry, and edge deployments (a11y-debugging, web-performance, telemetry, web-deployment, peekaboo, chrome-devtools). Replaces loaders with layout-matching skeletons. Enforces zero-downtime database migrations (Expand/Contract).

## Taxonomy

```
├── product/          # Strategy & execution (create-prd, product-management, product-management-press-memo, product-strategy-outcome-vision, ux-discovery-artifacts, michael-bolton-rule, swarm-rules, god-marduk)
├── design/           # Aesthetic rules, responsive layout, motion, chart communication, skeletons, empty states
├── engineering/      # Code quality, audits, implementation planning, architecture, resiliency, TDD, eval-driven development
├── data-and-api/     # REST/GraphQL API design, database schemas, ORM models, caching
├── security/         # Authentication protocols, identity keys, secure cookies, keychain
├── growth/           # SEO, commerce UX, CRO, copywriting, analytics, negotiation maximization
└── quality/          # Performance debugging, telemetry observability, deployments, a11y audit, chrome automation
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
