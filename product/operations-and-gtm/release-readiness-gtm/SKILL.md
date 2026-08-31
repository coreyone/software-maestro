---
name: release-readiness-gtm
description: "Trigger: release-readiness-gtm, GTM launch readiness, release gating, feature tiering, alpha beta GA gates, sales enablement checklist. Scope: Cross-Functional Go-To-Market Release Readiness. Defines release tiers and phased readiness gates across Sales, Marketing, CS, Legal, and Support. Boundary: Excludes CI/CD deployment pipelines."
---

# Rule: Product Release Readiness & GTM Gating

## When to use

Use this skill when preparing, coordinating, or gating product releases across Go-to-Market (GTM) functions—including Sales, Marketing, Customer Success, Legal, Compliance, and Support.

## When not to use

Do not use this skill for automated continuous integration/continuous deployment (CI/CD) pipelines, Docker builds, or visual interface design mocks.

## Trigger cues

- Request explicitly references `release-readiness-gtm` or release gating.
- Keywords: release tiers, launch readiness, GTM checklist, Alpha/Beta/GA status, sales enablement, release criteria, launch gate, feature roll-out governance.

## Routing boundary

- Primary for product lifecycle status gating, cross-functional launch SLAs, and sales enablement criteria.
- Route low-level code deployment or infra rollout to deployment and devops skills.

## Inputs required

- Target initiative / feature description and target audience
- Release tier classification (Tier 1: Major Launch, Tier 2: Feature Enhancement, Tier 3: Internal / Minor)
- Target release timeline and dependencies across functions
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Determine the **Release Tier** (Tier 1, 2, or 3) to establish SLA timelines and stakeholder involvement.
3. Classify the feature into its current **Lifecycle Gate**:
   - **Discovery**: Internal exploration; Sales and Marketing CANNOT discuss or commit.
   - **Alpha**: Internal & friendly customer validation; Sales CANNOT sell or quote.
   - **Beta**: Functional testing with targeted cohort; Sales can discuss concepts and timelines with strict non-binding guardrails.
   - **General Availability (GA)**: Live in production, fully packaged, pricing finalized, documentation published, and support trained.
4. Generate a **Cross-Functional Release Readiness Matrix** specifying owners, status, and sign-offs across Product, Engineering, Marketing, Sales, CS, Legal, and Support.
5. Create standard **Enablement Collateral**: Demo day script, release notes, sales one-pager, and support escalation runbook.
6. Validate all completion criteria before gating to General Availability.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit Release Tier assigned with justification.
- Unambiguous lifecycle gate status (Discovery, Alpha, Beta, GA) with explicit Sales communication rules.
- Complete cross-functional sign-off checklist across Marketing, Sales Enablement, Support, and Legal.

## Output format

- **Release Tier & Status**: Classification (Tier 1/2/3) and Lifecycle Phase (Discovery/Alpha/Beta/GA).
- **Sales & GTM Communication Boundary**: What Sales can and cannot say/sell.
- **Cross-Functional Readiness Matrix**: Functional owners, deliverables, and sign-off status.
- **Enablement Artifacts**: Summary release notes, support FAQ, and customer migration path.
