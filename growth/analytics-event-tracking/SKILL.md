---
name: analytics-event-tracking
description: "Trigger: analytics-event-tracking, behavioral-loops-retention-modeling, marketing-lifecycle-crm-automation, incentive-design-metric-trees, PostHog events, Segment schema, event tracking taxonomy, user funnel telemetry, tracking spec. Scope: Behavioral Analytics & Telemetry Taxonomy. Governs event naming conventions, schema properties, and user funnel telemetry. Boundary: Excludes system performance exceptions."
---

# 📈 Core Philosophy: Standardized telemetry taxonomy drives actionable product insights.

## When to use

Use this skill when defining user event schemas, instrumenting CTA interaction code, building marketing/analytics conversion loops, setting up user identity profiles, or adding behavioral tracking hooks (e.g., PostHog, Amplitude, Segment).

## When not to use

Do not use this skill for internal application performance monitoring (APM), database queries logging, or server-level exception handling.

## Trigger cues

- Key terms: analytics, telemetry tracking, event capture, user funnel, PostHog, Amplitude, Segment, event schema, tracking plan, conversion funnel, properties, user identifier.
- Designing behavioral logs, tracking button clicks, instrumenting onboarding funnels, or setting up identity mapping.

## Routing boundary

- Primary for product telemetry, behavioral schemas, funnel analysis, and tracking plans.
- Secondary to `observability-telemetry` for performance tracing and system stability.

## Inputs required

- Target analytics engine/tracker (e.g., PostHog, Segment, Mixpanel)
- Tracking plan requirements (funnel actions, user properties)
- Source of truth: `references/source.md`

## Instructions

1. **Detect Stack**: Inspect the workspace files to identify the project's existing telemetry and analytics libraries (e.g., PostHog, Amplitude, Google Analytics, Segment).
2. **Do Not Migrate**: Never propose or force a technology stack change. Apply the principles in this skill using the project's current tooling.
3. Read [references/source.md](references/source.md) to understand taxonomy formatting and event mapping.
4. Establish unified tracking schemas (Object:Action structure) for key conversion milestones.
5. Log high-cardinality metadata in event property blocks instead of creating duplicate events.
6. Verify client-side privacy safeguards (never track raw PII like passwords or full names).

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`: stable `Object:Action` milestones, variants in properties, no raw PII, and no unnecessary analytics-stack migration.

## Output format

- Primary decision/output: Tracking plan definition, event instrumentation code snippets, and property models.
- Summary: One-paragraph overview of product behavioral telemetry.
- Actions: Verification checklist for event taxonomy, PII checks, and identity mapping accuracy.
