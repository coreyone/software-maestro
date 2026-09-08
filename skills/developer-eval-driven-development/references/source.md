# Eval-Driven Development Reference

## Contents

1. Development loop
2. Eval contract
3. Dataset design
4. Evaluator design
5. Experiment design
6. Analysis and release decisions
7. Production learning loop
8. Failure patterns
9. Source influences

## 1. Development loop

Eval-driven development applies the test-first discipline to behavior whose correct output has multiple valid forms.

Use this cycle:

1. **Specify** — define observable behavior, failure modes, and decision thresholds.
2. **Baseline** — run the current system and preserve its outputs and metadata.
3. **Challenge** — prove the evaluators reject known-bad behavior.
4. **Improve** — change one material variable.
5. **Compare** — rerun the frozen experiment and inspect paired examples.
6. **Analyze** — distinguish application, evaluator, and dataset failures.
7. **Lock** — add regressions, preserve holdouts, version artifacts, and monitor drift.

This is the probabilistic counterpart to Red-Green-Refactor:

- **Red:** an eval demonstrates a meaningful failure or unmet threshold.
- **Green:** the smallest change clears the criterion without critical regression.
- **Refine:** improve the system and eval design while keeping evidence comparable.

Do not begin by selecting an eval framework. Begin with the release decision the evidence must support.

## 2. Eval contract

Write the contract before changing the application. It should state:

- user or business outcome
- application entry point under test
- capabilities in scope
- consequential failure modes
- dataset slices and provenance
- criterion-to-evaluator mapping
- pass rule for each criterion
- critical failures that cannot be averaged away
- quality, safety, cost, and latency budgets
- experiment budget and stopping rule

Prefer criteria derived from failure modes over vague dimensions such as “overall quality.”

Weak criterion:

> The answer is good.

Stronger criterion:

> When the retrieval context lacks the requested fact, the answer states that the evidence is insufficient and does not invent a value.

Every criterion must identify what evidence the evaluator reads and what result changes the release decision.

## 3. Dataset design

### Build representative slices

Cover:

- frequent happy paths
- boundary and malformed inputs
- rare but costly failures
- adversarial or misuse cases
- historical production failures
- long, multilingual, or domain-specific inputs when applicable
- uncertain cases where the current behavior is not already known

Production-derived and expert-curated examples are usually stronger than synthetic-only data. Remove secrets and personal information. Preserve provenance and the reason each example exists.

### Separate dataset roles

- **Development set:** visible cases used during iteration.
- **Regression set:** confirmed failures that must not recur.
- **Holdout set:** untouched cases used for final comparison.
- **Shadow or production sample:** monitored cases used to detect drift.

Do not repeatedly optimize against the holdout. Rotate or refresh it when exposure makes it functionally part of the development set.

### Avoid self-fulfilling datasets

Existing fixtures are acceptable when they represent real requirements or production behavior. Reject fixtures that merely mirror the implementation, prompt wording, or evaluator assumptions.

Track:

- dataset name and version
- example ID and slice labels
- source and collection date
- expected behavior or reference
- annotation status and reviewer
- sensitivity classification

Use enough examples to represent the decision. For directional experiments, start with at least 30 varied examples when feasible, then increase sample size based on observed variance and slice coverage. Never treat a convenient sample count as proof of statistical power.

## 4. Evaluator design

### Use an evaluator ladder

Choose the lowest rung that measures the requirement:

1. deterministic executable assertion
2. task-specific reference comparison
3. calibrated model judge
4. human adjudication

Examples:

| Criterion | Preferred evaluator |
|---|---|
| Valid JSON schema | Deterministic parser/schema check |
| Correct tool and arguments | Deterministic trace assertion |
| Response cites supplied evidence | Citation/grounding assertion plus semantic check |
| Completeness of an open-ended answer | Calibrated model judge |
| High-impact ambiguous safety case | Human review with judge assistance |

### Design model judges

- Use generic variables such as `input`, `output`, `reference`, and `context`.
- Define one focused dimension per evaluator.
- Make label output exact and machine-parseable.
- Default to `pass` and `fail` when the downstream decision is binary.
- State criteria in observable terms.
- Include labeled boundary examples during calibration.
- Use deterministic inference settings where supported.
- Request concise reasoning for calibration and audits, but parse the label separately.
- Do not let the judge see metadata that leaks the candidate identity or expected winner.

### Validate the evaluator

An evaluator is another model or program that can fail. Before making it a gate:

1. Assemble human-labeled pass, fail, and boundary examples.
2. Run the evaluator blind.
3. Measure false passes, false failures, and disagreement by slice.
4. Revise the rubric or use human adjudication for unresolved cases.
5. Version the evaluator prompt, model, code, and calibration set.

For high-stakes decisions, sample human review even after calibration. Investigate judge disagreement rather than averaging it away.

## 5. Experiment design

Record:

- application commit or build
- prompt and policy versions
- exact model identifier or deployment
- temperature, seed, token limits, and other inference settings
- tool and retrieval configuration
- dataset and evaluator versions
- environment and dependency versions when material
- run ID, timestamp, latency, token usage, and cost

Capture a reference trace before building assertions around an unfamiliar system. Verify that the trace includes the inputs, retrieved context, tool calls, model spans, outputs, and errors needed by the evaluators.

Use real model calls for end-to-end behavior. Unit tests may replace the model to verify deterministic orchestration, but those tests do not measure model quality.

Compare candidates on the same examples. Prefer paired per-example deltas over unrelated aggregate runs. When outputs vary materially, repeat cases and report distributions or confidence intervals rather than selecting a favorable run.

Change one material factor at a time when the goal is causal learning. If multiple factors must change together, describe the result as a bundle comparison.

Set bounds before running:

- maximum iterations
- maximum model calls or spend
- maximum elapsed time
- convergence threshold
- regression tolerance

Three to five focused iterations are usually enough to reveal whether the current direction is converging. Stop earlier for critical regressions or later only with an explicit reason and budget.

## 6. Analysis and release decisions

Analyze three systems separately:

### Application quality

- Which user behaviors improved or regressed?
- Which failures are severe even if rare?
- Are tool calls, retrieval, and final answers internally consistent?

### Evaluator quality

- Do scores match human judgment on sampled cases?
- Are labels stable across paraphrases and slices?
- Does the evaluator over-reward verbosity, references, or superficial keywords?

### Dataset quality

- Are important users and failure modes represented?
- Is any slice too small to support a conclusion?
- Did test leakage or duplicate cases distort the result?

Report:

- baseline and candidate counts, rates, and deltas
- per-slice results
- critical failures
- per-example regressions
- variance and uncertainty
- cost and latency
- invalid, missing, and blocked cases

Do not:

- ship from an average that hides a critical safety failure
- treat a missing score as a pass
- compare runs with silently changed datasets or evaluators
- claim causality after changing several variables
- call a one-run stochastic win a stable improvement

## 7. Production learning loop

After release:

- monitor quality proxies, errors, refusals, tool failures, latency, and cost
- sample traces with privacy-aware retention
- detect changes by model, prompt, customer segment, language, and task slice
- review user corrections and escalations
- turn verified incidents into regression examples
- rerun the suite before model, prompt, retrieval, or tool changes

Every confirmed AI behavior defect should produce:

1. a minimized reproducible example
2. a dataset entry with provenance
3. an evaluator that detects the failure
4. a system fix
5. a production signal for recurrence where practical

## 8. Failure patterns

- **Scoreboard without a decision:** metrics exist, but no threshold changes ship behavior.
- **Judge all the things:** subjective evaluators replace exact executable checks.
- **Mocked intelligence:** a fake model makes an end-to-end eval tautological.
- **Prompt overfitting:** iteration improves visible cases while holdout quality falls.
- **Aggregate camouflage:** a mean score hides a critical slice regression.
- **Evaluator drift:** judge model or rubric changes without recalibration.
- **Dataset contamination:** examples expose the answer through labels, filenames, or candidate metadata.
- **Unbounded iteration:** repeated runs consume budget without a stopping rule.
- **Uninterpreted results:** raw scores are delivered without example-level analysis or actions.
- **Versionless evidence:** the run cannot be reproduced because material inputs were not recorded.

## 9. Source influences

This reference adapts principles from:

- [GitHub Awesome Copilot: eval-driven-dev](https://github.com/github/awesome-copilot/tree/main/skills/eval-driven-dev)
- [GitHub Awesome Copilot: agentic-eval](https://github.com/github/awesome-copilot/tree/main/skills/agentic-eval)
- [GitHub Awesome Copilot: arize-evaluator](https://github.com/github/awesome-copilot/tree/main/skills/arize-evaluator)
- [GitHub Awesome Copilot: arize-experiment](https://github.com/github/awesome-copilot/tree/main/skills/arize-experiment)

The Software Maestro skill is intentionally framework- and language-neutral. Pixie, Arize, promptfoo, DeepEval, OpenAI Evals, custom harnesses, and comparable systems may implement the workflow; none is required.
