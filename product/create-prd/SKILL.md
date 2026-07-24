---
name: create-prd
description: "Trigger: PRD, product requirements, spec, problem framing, project scoping, roadmap. Scope: Creating and updating product requirement documents and framing problem scopes. Boundary: Excludes code implementation, design mocks, or CI/CD config."
---

# Rule: Generating a Product Requirements Document (PRD)

## When to use

Use this skill when the task is primarily about product and this guidance is the most relevant operating rule set.

## When not to use

Do not use this skill as the primary guide when another skill has a tighter domain fit for the requested output.

## Trigger cues

- Request explicitly references `create-prd` or this source file.
- Request language includes terms like: create, prd.
- Keywords include: PRD, success metrics, goals/non-goals, user journey, roadmap, launch memo, BDD, Gherkin, acceptance criteria.

## Routing boundary

- Primary for problem definition, PRD scope, metrics, BDD acceptance criteria, and product narrative.
- Do not use as primary for deep UI styling or low-level code implementation.

## Inputs required

- Goal or task request
- Current constraints (time, scope, platform, risk)
- Existing artifacts (code, docs, screenshots, metrics) when available
- Source of truth: `subagents/product manager/create-prd.md`

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Extract the non-negotiable rules and translate them into a short execution checklist.
3. Include unambiguous BDD/Gherkin scenarios (`Given / When / Then`) under Acceptance Criteria as a bridge to implementation test suites.
4. Apply the checklist to the current task, produce concrete outputs, and avoid abstract recommendations.
5. Validate outcomes with evidence (tests, screenshots, logs, diffs, or written audit findings).
6. Record decisions and tradeoffs so another engineer can continue without re-discovery.

## Output format

- Primary decision/output: Problem scope, measurable outcomes, BDD/Gherkin acceptance criteria, and what not to build yet.
- Summary: one-paragraph decision or result
- Actions: compact checklist with owners and status
- Evidence: links/paths to artifacts proving completion
