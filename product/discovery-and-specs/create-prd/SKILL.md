---
name: create-prd
description: "Author comprehensive product requirement documents with background, user stories, and acceptance criteria."
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

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`: explicit problem and measurable outcome, non-goals, unambiguous `Given / When / Then` acceptance behavior, and visible unknowns rather than invented facts.

## Output format

- Primary decision/output: Problem scope, measurable outcomes, BDD/Gherkin acceptance criteria, and what not to build yet.
- Summary: one-paragraph decision or result
- Actions: compact checklist with owners and status
- Evidence: links/paths to artifacts proving completion

## Definition of Done (DoD) Verification Gate for PRD Artifacts

Before marking any PRD or product requirement document as COMPLETE, the author must pass the 6-point binary DoD audit:

- [ ] **1. Tony Fadell "On-the-Box" Storytelling (Day 1)**: Header contains the 3-sentence retail box pitch, 30-second elevator story, and emotional customer transformation before any technical specs or APIs are defined.
- [ ] **2. Problem & Outcome Precision**: Core problem framed with quantifiable success metrics and explicit baseline vs. target values.
- [ ] **3. Non-Goals & Scope Boundaries**: Explicit list of out-of-scope capabilities, anti-personas, and deferred features.
- [ ] **4. BDD / Gherkin Acceptance Contracts**: Every feature requirement contains unambiguous `Given / When / Then` scenarios covering both happy paths and edge/error cases.
- [ ] **5. Technical & Design Feasibility Sign-off**: Dependencies, API endpoints, data retention, and UX design token mappings validated with engineering.
- [ ] **6. Telemetry & Analytics Contract**: Defined behavioral tracking events, property taxonomies, and conversion funnel checkpoints.
