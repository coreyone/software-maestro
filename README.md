# Software Maestro

Capability orchestra for AI IDE agents. Conducts product strategy, design systems, and engineering execution from a single developer baton.

## Install

```bash
npx skills add coreyone/software-maestro
```
*(Alternative: clone directly to target AI IDE config/skills directory)*

## Lifecycle Structure

*   **product/**: Strategy & execution governance (create-prd, product-management, product-management-press-memo, product-strategy-outcome-vision, ux-discovery-artifacts, michael-bolton-rule, swarm-rules, god-marduk). Validates customer truth before roadmaps. Decides what not to build.
*   **design/**: Wayfinding & visual systems (aesthetic-rules, responsive-rules, design-animation, design-system-rules, design-usability-rules). Structures for instant orientation (IA), WCAG AA typography-first layout, and tactile microinteractions.
*   **engineering/**: Clean code, architecture, and governed improvement workflows (developer-development, code-review, improve-codebase, TDD, system-architecture, resiliency, tech-stack). Isolates components, decouples modules, and turns vetted findings into drift-aware plans with verified delegated execution.
*   **data-and-api/**: Contract-first endpoints & persistence schemas (api-design-guidelines, data-persistence-caching). Bypasses client-state latency using local memory replication.
*   **security/**: Identity & sandbox trust boundaries (developer-security, developer-web-security, auth-and-identity-rules). Isolates tokens (Keychain/HttpOnly cookies) and cryptographically validates JWTs.
*   **growth/**: Organic discovery, conversions & behavioral loops (developer-seo, commerce-ux, cro-commerce-audit, design-forms, marketing-copy, elements-of-style, analytics-event-tracking). Builds durable search and AI-answer visibility, qualifies traffic by business outcomes, and standardizes event tracking (`object:action`) without namespace pollution.
*   **quality/**: Graceful degradation, APM telemetry, and edge deployments (a11y-debugging, web-performance, telemetry, web-deployment, peekaboo, chrome-devtools). Replaces loaders with layout-matching skeletons. Enforces zero-downtime database migrations (Expand/Contract).

## Taxonomy

```
├── product/          # Strategy & execution (create-prd, product-management, product-management-press-memo, product-strategy-outcome-vision, ux-discovery-artifacts, michael-bolton-rule, swarm-rules, god-marduk)
├── design/           # Aesthetic rules, responsive layout, motion, skeletons, empty states
├── engineering/      # Code quality, audits, implementation planning, verified delegation, architecture, resiliency, TDD
├── data-and-api/     # REST/GraphQL API design, database schemas, ORM models, caching
├── security/         # Authentication protocols, identity keys, secure cookies, keychain
├── growth/           # SEO and AI discovery, commerce UX, conversions, copywriting, event tracking
└── quality/          # Performance debugging, telemetry observability, deployments, a11y audit, chrome automation
```
