---
name: experimentation-hypothesis-engine
description: "Trigger: A/B testing, feature experimentation, hypothesis testing, experiment design, MDE calculation, sample size determination, statistical significance, rollout vs kill decision. Scope: Defining testable hypothesis statements (If... Then... Due to...), sample sizing / Minimum Detectable Effect (MDE), primary vs guardrail metrics, and statistical rollout/kill criteria. Boundary: Excludes server-side feature flag SDK installation or low-level database indexing."
---

# Rule: Feature Experimentation & Hypothesis Gating

## When to use

Use this skill when designing, sizing, running, or evaluating A/B tests, multivariate experiments, or hypothesis-driven feature rollouts.

## When not to use

Do not use this skill for raw feature flag SDK code installation or database performance tuning.

## Trigger cues

- Request explicitly references `experimentation-hypothesis-engine` or experiment design.
- Keywords: A/B test, hypothesis statement, sample size, MDE, minimum detectable effect, statistical significance, primary metric, guardrail metric, rollout vs kill, experiment scorecard.

## Routing boundary

- Primary for statistical experiment design, hypothesis formulation, metric selection, and kill/rollout decision rubrics.
- Route behavioral loop modeling to `behavioral-loops-retention-modeling` and event tracking syntax to `analytics-event-tracking`.

## Inputs required

- Target user action or feature change
- Baseline conversion / retention rate and daily traffic volume
- Primary outcome metric and potential risk surface (guardrails)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Structure the **Testable Hypothesis**:
   - Format: *"If we [change/intervention], then [user behavioral change] will occur, resulting in [primary metric impact], because [underlying psychological/functional rationale]."*
3. Define the **Metric Hierarchy**:
   - **Primary Metric**: The single decision-making metric (e.g., checkout completion rate).
   - **Secondary / Proxy Metrics**: Early indicators of user adoption.
   - **Guardrail Metrics**: Invariants that must NOT degrade (e.g., page load latency, support ticket rate, unsubscribe rate).
4. Calculate **Sample Size & Runtime**:
   - Determine baseline rate, Minimum Detectable Effect (MDE), statistical power ($1-eta = 80\%$), and significance level ($lpha = 0.05$).
   - Compute required sample size per variant and minimum runtime to prevent day-of-week seasonality bias (minimum 1–2 full weeks).
5. Establish **Decision Rubric (Rollout / Iterate / Kill)**:
   - *Rollout*: Statistically significant lift in Primary Metric with zero breach in Guardrails.
   - *Iterate*: Inconclusive primary lift but strong qualitative signal or sub-segment win.
   - *Kill*: Statistically significant drop in Primary Metric or breach in Guardrail limits.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Formal hypothesis structure (If... Then... Resulting in... Because...).
- Explicit primary, secondary, and guardrail metric definitions.
- Runtime and sample size / MDE estimation.
- Clear, unambiguous Rollout, Iterate, and Kill decision criteria.

## Output format

- **Experiment Hypothesis**: Formal test statement.
- **Metric Scorecard**: Primary metric, secondary indicators, and guardrails.
- **Statistical Design**: Sample size per variant, MDE, and minimum runtime.
- **Decision Matrix**: Exact criteria for 100% Rollout, Iteration, or Immediate Kill.
