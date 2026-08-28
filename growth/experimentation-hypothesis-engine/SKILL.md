---
name: experimentation-hypothesis-engine
description: "Trigger: A/B testing, feature experimentation, hypothesis testing, experiment design, MDE calculation, sample size determination, statistical significance, rollout vs kill decision, growth loop experiments, experiment post-mortem. Scope: Defining testable hypothesis statements (If... Then... Due to...), growth loop step mapping, pre-experiment qualitative gating, sample sizing / Minimum Detectable Effect (MDE), primary vs guardrail metrics, and statistical rollout/kill post-mortem criteria. Boundary: Excludes server-side feature flag SDK installation or low-level database indexing."
---

# Rule: Growth Experimentation, Hypothesis Gating, & Loop Acceleration

## When to use

Use this skill when designing, sizing, running, or evaluating A/B tests, multivariate experiments, growth loop acceleration tests, or hypothesis-driven feature rollouts.

## When not to use

Do not use this skill for raw feature flag SDK code installation, low-level database performance tuning, or pure qualitative discovery interviews.

## Trigger cues

- Request explicitly references `experimentation-hypothesis-engine` or experiment design.
- Keywords: A/B test, hypothesis statement, growth loop step, sample size, MDE, minimum detectable effect, statistical significance, primary metric, guardrail metric, rollout vs kill, experiment scorecard, experiment post-mortem.

## Routing boundary

- Primary for statistical experiment design, hypothesis formulation, growth loop step integration, metric selection, and kill/post-mortem decision rubrics.
- Route behavioral habit loops to `behavioral-loops-retention-modeling` and qualitative VoC synthesis to `voc-insights-pipeline`.

## Inputs required

- Target user action, feature change, or growth loop step
- Work classification (Optimization vs Growth Loop vs Strategic Step-Function)
- Baseline conversion / retention rate and daily traffic volume
- Primary outcome metric and risk surface (guardrails)
- Qualitative evidence backing the hypothesis (session replays, VoC tickets)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Classify the **Experiment Type & Loop Step**:
   - **Type**: *Funnel Optimization* (micro-conversion), *Growth Loop Accelerator* (fueling reinvestment/virality), or *Step-Function Bet* (new capability/cohort retention).
   - **Loop Step Mapping**: Identify how user output generated in this experiment becomes the input for the next cycle.
3. Validate the **Pre-Experiment Qualitative Gate**:
   - Ensure the underlying user friction or opportunity is verified by qualitative evidence (>=5 user interviews, support tickets, or session replays) before coding variants.
4. Formulate the **Testable Hypothesis Statement**:
   - Format: *"If we [change/intervention], then [user behavioral shift] will occur, resulting in [primary metric impact], because [underlying psychological/functional rationale]."*
5. Define the **Metric Scorecard & Guardrails**:
   - **Primary Metric**: Single decision-making metric tied to the hypothesis.
   - **Secondary Metrics**: Leading indicators of user adoption.
   - **Guardrail Invariants**: Metrics that must NOT degrade (e.g., latency, support volume, 30-day retention).
6. Calculate **Sample Size, MDE, & Minimum Duration**:
   - Determine baseline rate, Minimum Detectable Effect (MDE), statistical power ($1-\beta = 80\%$), and significance level ($\alpha = 0.05$).
   - Enforce the **14-Day Minimum Duration Rule** (2 full business cycles to smooth day-of-week seasonality).
7. Execute the **Decision Rubric & 3-Way Post-Mortem**:
   - *100% Rollout*: Statistically significant lift in Primary Metric with zero breach in Guardrails.
   - *Structured Post-Mortem (on Failure/Inconclusive)*:
     - **Invalidated Mental Model**: User psychology was incorrect (log permanent learning).
     - **Execution Mismatch**: Right hypothesis, poor UI/UX execution (iterate on design).
     - **Statistical Under-Powering**: Sample size was insufficient for actual effect size.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Formal hypothesis structure with loop step mapping.
- Pre-experiment qualitative evidence requirement.
- Explicit primary, secondary, and guardrail metric definitions.
- Runtime estimation (minimum 14 days) and sample size / MDE calculation.
- Clear 3-way post-mortem criteria on failed/inconclusive experiments.

## Output format

- **Experiment Classification & Loop Step**: Type and target growth loop stage.
- **Formal Hypothesis Statement**: If... Then... Resulting in... Because...
- **Metric Scorecard**: Primary metric, secondary indicators, and guardrails.
- **Statistical Design**: Sample size per variant, MDE, and 14-day minimum duration.
- **Decision Matrix & Post-Mortem Taxonomy**: Criteria for 100% Rollout, Execution Iteration, or Assumption Invalidation.
