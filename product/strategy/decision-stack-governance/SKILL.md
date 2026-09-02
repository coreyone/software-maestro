---
name: decision-stack-governance
description: "Trigger: decision-stack-governance, portfolio-allocation-capitalization, strategic-tradeoffs-constraint-matrix, decision stack, melissa perri strategy, strategic intents, product portfolio cadence, QBR planning, strategy deployment. Scope: Strategy Deployment & Portfolio Cadence. Cascades Company Vision (5-10y) -> Strategic Intents (1-3y) -> Product Initiatives (6-12m) -> Options (3-6m). Boundary: Excludes sprint-level daily standups."
---

# Rule: Decision Stack Alignment & Cadence Governance

## When to use

Use this skill when connecting high-level company vision to team backlog execution, structuring strategic planning cycles (Annual CKO, QBRs, Monthly Roadmap reviews), or reconciling roadmap conflicts with executive goals.

## When not to use

Do not use this skill for daily agile standups, individual sprint ticket grooming, or writing code diffs.

## Trigger cues

- Request explicitly references `decision-stack-governance` or strategy deployment.
- Keywords: Decision Stack, Strategic Intents, Product Initiatives, Options, Oscar Health planning model, Now-Next-Later roadmap governance, QBR structure, strategic cadence.

## Routing boundary

- Primary for multi-horizon product strategy alignment, cadence governance, and executive planning rituals.
- Route PRD generation to `create-prd` and phased execution management to `god-marduk`.

## Inputs required

- Company vision and long-term targets
- Strategic intents (1–3 year business challenges)
- Proposed product initiatives and squad options
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Structure the organization's product strategy across the **Cascading Decision Stack**:
   - **Company Vision (5–10 yrs)**: North star and customer value position (Owner: CEO/Execs).
   - **Strategic Intents (1–3 yrs)**: Core business challenges to overcome (Owner: CPO, CRO, CFO).
   - **Product Portfolio Initiatives (1–3 yrs / 6–12 mos)**: Problems to address to unlock intents (Owner: Product Leadership).
   - **Options (3–6 mos)**: Specific solutions, prototypes, and experiments tested by squads (Owner: Product Dev Teams).
3. Establish the **Strategic Governance Cadence** (Annual CKO $
ightarrow$ Quarterly QBR $
ightarrow$ Monthly Roadmap Review $
ightarrow$ Monthly Demo Day).
4. Run the **Now-Next-Later Roadmap Rollup**, ensuring every sprint epic traces back to an approved Product Initiative.
5. Deploy executive alignment mechanisms (e.g., Oscar Health "Phone-a-Friend" surveys) to calibrate resource allocations before locking commitments.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Full 4-level Decision Stack hierarchy populated with measurable outcomes.
- Traceability from squad options/experiments up to Strategic Intents.
- Clear meeting cadence specification (Audience, Inputs, Outputs).

## Output format

- **Decision Stack Mapping**: Vision $
ightarrow$ Strategic Intent $
ightarrow$ Product Initiative $
ightarrow$ Squad Option.
- **Now-Next-Later Strategic Roadmap**: Structured by Strategic Intent and Pod.
- **Operating Cadence Matrix**: Cadence schedule, attendees, agenda, and out-of-scope boundaries.
