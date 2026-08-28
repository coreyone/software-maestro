---
name: strategic-tradeoffs-constraint-matrix
description: "Trigger: Strategic trade-offs, where not to play, constraint management, non-goals, anti-personas, opportunity cost matrix, strategic refusal, saying no to features. Scope: Defining hard strategic boundaries, anti-personas, explicit non-goals, opportunity cost evaluations, and structured trade-off matrices (e.g. speed vs accuracy, customization vs scalability). Boundary: Excludes daily backlog grooming or UI visual design styling."
---

# Rule: Strategic Trade-offs & Constraint Management ("Where NOT to Play")

## When to use

Use this skill when defining product boundaries, rejecting feature requests that pull the product off-strategy, resolving conflicting stakeholder priorities, or codifying explicit non-goals and anti-personas.

## When not to use

Do not use this skill for daily agile backlog grooming or low-level UI styling decisions.

## Trigger cues

- Request explicitly references `strategic-tradeoffs-constraint-matrix` or 'where not to play'.
- Keywords: strategic trade-offs, non-goals, anti-personas, constraint matrix, saying no to features, opportunity cost, strategic refusal, focus boundaries.

## Routing boundary

- Primary for establishing strategic boundaries, trade-off contracts, and explicit exclusion criteria.
- Route PRD generation to `create-prd` and decision stack alignment to `decision-stack-governance`.

## Inputs required

- Target market or proposed feature initiatives
- Strategic intent and core value proposition
- Competing trade-off axes (e.g., Bespoke Enterprise vs Self-Serve Simplicity)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Formulate the **Strategic Playing Field & Exclusions ("Where NOT to Play")**:
   - Define the **Anti-Persona**: Customer profiles who are explicitly NOT the target.
   - Define **Non-Goals**: Product capabilities the team will deliberately refuse to build.
3. Construct the **Strategic Trade-off Matrix**:
   - Map competing values on explicit trade-off pairs (e.g., *Speed over Comprehensiveness*, *Opinionated Simplicity over Infinite Customization*, *Standardized Self-Serve over Bespoke Professional Services*).
4. Conduct an **Opportunity Cost & Strategic Refusal Evaluation**:
   - Calculate the direct cost of saying yes (engineering distraction, tech debt, market confusion).
   - Draft a crisp **Strategic Refusal Memo** to align stakeholders on why a feature request is rejected.
5. Codify the **Constraint Boundaries** into product governance artifacts.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit "Where NOT to play" boundaries and Anti-Persona definitions.
- Paired trade-off principles (X over Y) with clear rationale.
- Actionable non-goals preventing feature bloat.

## Output format

- **Strategic Boundaries ("Where NOT to Play")**: Excluded segments and use-cases.
- **Anti-Persona Profile**: Who this product is not designed for.
- **Strategic Trade-off Matrix**: Paired choices (We choose X even when it costs us Y).
- **Non-Goals & Refusal Decisions**: Explicit rejected requests with strategic rationale.
