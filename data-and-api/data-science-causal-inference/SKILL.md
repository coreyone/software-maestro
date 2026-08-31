---
name: data-science-causal-inference
description: "Trigger: causal inference, quasi-experiment, difference in differences, DiD, synthetic controls, regression discontinuity, RDD, CUPED, instrumental variables, observational study, parallel trends, propensity score matching, selection bias, non-randomized rollout, cannibalization analysis, spillover effects. Scope: Designing, executing, and validating causal evaluations when randomized A/B tests are infeasible, under-powered, or contaminated. Formulates statistical methodologies for CUPED variance reduction, two-way fixed effects DiD, synthetic control donor optimization, and RDD bandwidth selection with mandatory sensitivity tests. Boundary: Excludes standard randomized A/B test sample sizing without quasi-methods (use experimentation-hypothesis-engine), raw event tracking instrumentation (use analytics-event-tracking), or system metric monitoring (use observability-telemetry)."
---

# Rule: Data Science Causal Inference & Quasi-Experimentation

## When to use

Use this skill when evaluating product changes, policy updates, regional rollouts, or marketing interventions where:
- A clean, randomized user-level A/B test is technically or ethically impossible (e.g., market-level pricing, brand campaigns, physical supply rollouts).
- Online randomized experiments suffer from spillover, network interference, or cannibalization.
- You need pre-experiment variance reduction (CUPED) to increase experiment sensitivity and detect smaller effects.
- You must analyze observational log data while controlling for selection bias and unobserved confounding.

## When not to use

Do not use this skill for:
- Basic randomized A/B test sample sizing without quasi-methods (use `experimentation-hypothesis-engine`).
- Client-side event tracking telemetry design (use `analytics-event-tracking`).
- Application server performance or error logs (use `observability-telemetry` or `diagnosing-bugs`).

## Trigger cues

- Request mentions: `causal inference`, `quasi-experiment`, `difference-in-differences`, `DiD`, `synthetic controls`, `regression discontinuity`, `RDD`, `CUPED`, `instrumental variables`, `observational study`, `selection bias`, `propensity score matching`, `spillover effects`, `parallel trends`.
- Scenarios involving market-level rollouts (city-by-city, geo-testing), network-interference features (social feeds, two-sided marketplace matching), or historical policy analysis.

## Routing boundary

- Route standard randomized A/B test hypothesis formulation and simple MDE calculation to `experimentation-hypothesis-engine`.
- Route metric tree decomposition to `incentive-design-metric-trees`.
- Route diagnostic root-cause waterfall investigations to `product-data-metric-investigation-triage`.

## Inputs required

1. **Intervention Context**: Unit of assignment (user, cluster, city, geo-market, time-period) and rollout mechanism.
2. **Outcome Metric(s)**: Continuous or discrete response variable and business interpretation.
3. **Identification Strategy**: Selected causal method (DiD, Synthetic Control, RDD, CUPED, IV, PSM).
4. **Historical Baseline & Covariates**: Pre-intervention time series data and potential confounders.
5. **Threats to Validity**: Potential spillovers, SUTVA violations, anticipation effects, or unobserved shocks.
6. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Select the Causal Identification Strategy**:
   - **CUPED (Online A/B Variance Reduction)**: When running randomized trials with pre-experiment user metrics. Compute $\theta = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}$ and adjusted metric $\tilde{Y} = Y - \theta (X - E[X])$, reducing variance by $(1 - \rho^2)$.
   - **Difference-in-Differences (DiD)**: When treatment occurs at aggregate group/time levels with panel data. Validate the **Parallel Trends Assumption** using pre-treatment event study leads ($\beta_{t < 0} \approx 0$). Check for staggered adoption using Goodman-Bacon decomposition or Callaway-Sant'Anna estimators.
   - **Synthetic Control Method (SCM)**: When evaluating a single treated unit (e.g. state/city) against a donor pool. Solve constrained optimization $W^* = \arg\min_W ||X_1 - X_0 W||_V$ subject to $w_j \ge 0, \sum w_j = 1$. Execute in-space and in-time placebo tests for $p$-value estimation.
   - **Regression Discontinuity Design (RDD)**: When treatment assignment follows an arbitrary deterministic threshold ($X \ge c$). Test running variable continuity via McCrary density test. Select bandwidth using Calonico-Cattaneo-Titiunik (CCT) optimal MSE.
   - **Instrumental Variables (IV)**: When unobserved confounding exists but a valid instrument $Z$ satisfies relevance ($F > 10$) and exclusion restriction ($\text{Cov}(Z, \epsilon) = 0$).
3. **Verify Identification Invariants & Assumptions**:
   - Verify SUTVA (Stable Unit Treatment Value Assumption): Check for cannibalization or marketplace supply/demand spillover.
   - Assess Common Support: Ensure overlap in propensity score distributions across treatment and control.
4. **Conduct Sensitivity & Robustness Checks**:
   - **Placebo Interventions**: Re-run models with fake intervention dates (in-time placebo) or untreated control units (in-space placebo).
   - **Oster's $\delta$ / Rosenbaum Bounds**: Quantify how strong unobserved confounding must be to overturn the estimated treatment effect.
5. **Synthesize Business Implications & Confidence Intervals**:
   - Report point estimates with robust/clustered standard errors and 95% confidence intervals.
   - Express results in clear business terms (lift percentage, incremental unit impact, economic value).

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit causal identification strategy selection with formal mathematical foundation.
- Verification of core identification assumptions (parallel trends, donor pool weights, running variable continuity).
- Mandatory robustness / placebo checks.
- Point estimates with confidence intervals and business translation.

## Output format

- **Executive Summary & Causal Claim**: Summary of causal finding and confidence tier.
- **Identification Framework**: Chosen method, unit of assignment, and formal model specification.
- **Assumption Verification & Diagnostics**: Parallel trends tests, covariate balance tables, or placebo test distributions.
- **Causal Treatment Effect**: $\hat{\tau}$ point estimate, standard errors, and 95% confidence intervals.
- **Sensitivity & Risk Analysis**: SUTVA assessment, spillover bounds, and unobserved confounding threshold.
- **Recommended Action**: Clear recommendation (full rollout, kill, further localized testing).
