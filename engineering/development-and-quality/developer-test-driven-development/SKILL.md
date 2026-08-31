---
name: developer-test-driven-development
description: "Trigger: developer-test-driven-development, TDD, test driven development, red green refactor, unit testing, integration tests, mock assertions. Scope: Test-Driven Development (TDD) Methodology. Enforces writing failing test assertions before implementing production features. Boundary: Excludes probabilistic LLM evals."
---

# TEST DRIVEN DEVELOPMENT (TDD)

## When to use

Use this skill when the task is primarily about engineering and this guidance is the most relevant operating rule set.

## When not to use

Do not use this skill as the primary guide when another skill has a tighter domain fit for the requested output.

## Trigger cues

- Request explicitly references `developer-test-driven-development` or this source file.
- Request language includes terms like: developer, test, driven, development.
- Keywords include: implementation, TDD, tests, architecture, performance, web security, code review, BDD, Gherkin, mutation testing, Stryker, cargo-mutants, PIT, quality gates, complexity caps, property testing, fuzzing.

## Routing boundary

- Primary for code quality, test-driven design, BDD specifications, mutation testing, quantitative quality gates, and performance engineering.
- Do not use as primary for product positioning or conversion copy strategy.

## Inputs required

- Goal or task request
- Current constraints (time, scope, platform, risk)
- Existing artifacts (code, docs, screenshots, metrics) when available
- Source of truth: `subagents/rules/developer/developer-test-driven-development.md`

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Extract non-negotiable rules into a short execution checklist (Red-Green-Refactor, AAA pattern, BDD Gherkin scenarios).
3. Apply quantitative quality gates (complexity caps, coverage thresholds, zero critical linter/audit flaws).
4. Integrate mutation testing (Stryker, cargo-mutants, PIT) and property-based testing/fuzzing where applicable to verify assertion strength and invariants.
5. Apply the checklist to the current task, produce concrete outputs, and avoid abstract recommendations.
6. Validate outcomes with evidence (test runs, mutant kill reports, static analysis logs, diffs, or written audit findings).
7. Record decisions and tradeoffs so another engineer can continue without re-discovery.

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`: the new test failed before the fix and passed afterward, assertion strength was tested where appropriate, and every production bug produces a fix, regression test, and monitor.

## Output format

- Primary decision/output: Implementation approach, test coverage & mutation results, quality gate audit, and risk controls.
- Summary: one-paragraph decision or result
- Actions: compact checklist with owners and status
- Evidence: links/paths to artifacts proving completion
