---
name: developer-eval-driven-development
description: "Build evaluation datasets, LLM-as-judge rubrics, and regression benchmarks for AI software."
---

# EVAL-DRIVEN DEVELOPMENT (EDD)

Treat evaluation as the development loop for behavior that cannot be proven with ordinary assertions.

## Operating boundary

- Use EDD for probabilistic or semantic behavior: model responses, retrieval quality, tool selection, structured generation, safety, and multi-step agent outcomes.
- Use `developer-test-driven-development` for deterministic code paths, schemas, parsers, and business logic.
- Use both when an AI feature contains deterministic infrastructure and probabilistic behavior.
- Evaluate the application behavior users receive, not an isolated prompt in a playground.

## Inputs required

- Target behavior, users, and consequential failure modes
- Executable application entry point or representative trace
- Current prompt, model, tools, retrieval, and runtime configuration
- Existing production examples, incidents, fixtures, or acceptance criteria
- Cost, latency, safety, and release constraints

If credentials, required configuration, or the meaningful entry point are unavailable, report the exact blocker. Do not replace the system under evaluation with a fake and claim an end-to-end result.

## Instructions

1. Read [references/source.md](references/source.md) before designing or changing an eval system.
2. Write a compact eval contract before changing the application:
   - target behavior and user outcome
   - capabilities and high-cost failure modes
   - dataset slices
   - evaluator and pass rule for every criterion
   - release threshold, budget, and stop condition
3. Capture a baseline on the current implementation. Preserve per-example outputs, traces, scores, latency, cost, errors, and version identifiers.
4. Prove the eval can fail:
   - run a known-bad fixture, historical failure, or deliberate behavioral mutation
   - confirm each evaluator detects the failure it claims to measure
   - investigate false passes and false failures before trusting aggregate scores
5. Make one scoped behavioral change. Keep the comparison dataset, evaluators, and runtime controls fixed unless the experiment explicitly studies one of them.
6. Run the same eval suite and compare paired examples against the baseline. Inspect regressions and slice-level behavior; do not accept an aggregate score alone.
7. Analyze the run before iterating:
   - separate application failures, evaluator failures, and dataset failures
   - record uncertainty, variance, and unsupported conclusions
   - rank fixes by user harm and recurrence risk
8. Iterate with a bounded budget. Stop after the agreed limit, at convergence, or when further changes overfit the development set.
9. Lock learning into the system:
   - add confirmed failures to the regression set
   - preserve a hidden or untouched holdout set
   - version the dataset, evaluator, prompt, model, and application
   - monitor production drift and feed verified incidents back into evals

## Non-negotiable rules

- Prefer executable deterministic checks for exact properties; use model judges only for semantic properties.
- Run real-model calls in end-to-end evals. Mock them only in deterministic unit tests that are not presented as model-quality evidence.
- Calibrate judge rubrics against labeled pass and fail examples before using them as gates.
- Default classification evaluators to exact binary labels when the release decision is binary.
- Use generic evaluator variables rather than embedding application-specific content in reusable judge prompts.
- Keep development and holdout data separate. Do not tune against every case used for final acceptance.
- Include happy paths, edge cases, adversarial cases, historical failures, and at least one uncertain failure-mode case.
- Pin or record all material versions and inference settings. Repeat stochastic cases when one run cannot support the decision.
- Treat quality, safety, latency, and cost as separate dimensions. A weighted average must not hide a critical failure.
- Protect secrets and personal data in datasets, traces, and reports.

## Evaluator selection

Use the least subjective evaluator that measures the criterion:

1. Deterministic assertion: schema, exact value, tool arguments, citation presence, policy rule, latency, or cost.
2. Reference comparison: semantic similarity or task-specific comparison where a reference answer is meaningful.
3. Model judge: correctness, completeness, groundedness, tone, or other semantic qualities.
4. Human review: high-impact, ambiguous, novel, or judge-disagreement cases.

Never use a judge to replace an executable assertion. Never use string equality to judge an open-ended answer.

## Completion gate

Before reporting success, verify:

- the baseline and candidate both ran against a versioned, comparable dataset
- every release criterion has an evaluator and explicit pass rule
- evaluators rejected representative known-bad behavior
- every case has a result or a documented blocking error
- critical slices and individual regressions were inspected
- model, prompt, evaluator, dataset, application, and inference settings are recorded
- cost and latency stayed within their budgets
- the holdout set was not used for iterative tuning
- the final report distinguishes observed evidence from inference
- applicable binary contracts in `evals/cases.json` pass

Do not claim improvement from raw scores without baseline comparison, per-example evidence, and uncertainty analysis.

## Output format

- **Decision:** ship, revise, or block, with the governing threshold
- **Scorecard:** baseline versus candidate by criterion and dataset slice
- **Regressions:** failed examples, severity, evidence, and owner
- **Validity:** evaluator calibration, dataset limits, variance, and contamination risks
- **Actions:** prioritized application, evaluator, and dataset changes
- **Evidence:** artifact paths, run IDs, versions, traces, cost, and latency
