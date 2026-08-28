---
name: voc-insights-pipeline
description: "Trigger: Voice of Customer, VoC aggregation, feedback tagging, customer signal synthesis, customer problem repository, win/loss feedback, feedback taxonomy. Scope: Ingesting, deduplicating, and synthesizing qualitative feedback from Sales (Salesforce/Gong), Support (Zendesk), and UXR into atomized, tagged customer problem theses linked to revenue and customer segments. Boundary: Excludes live user interview conducting or marketing copywriting."
---

# Rule: Voice of Customer (VoC) Aggregation & Feedback Synthesis

## When to use

Use this skill when collecting, structuring, and synthesizing disparate customer feedback, support tickets, sales win/loss notes, and user research into a single source of truth for problem prioritization.

## When not to use

Do not use this skill for conducting live user interviews directly or writing customer-facing marketing copy.

## Trigger cues

- Request explicitly references `voc-insights-pipeline` or Voice of Customer synthesis.
- Keywords: VoC, customer feedback synthesis, feedback taxonomy, problem repository, win/loss analysis, customer pain points, feature request tagging, Zendesk feedback triage.

## Routing boundary

- Primary for cross-channel qualitative data ingestion, problem atomization, and customer need assessment.
- Route PRD generation to `create-prd` and pricing strategy to `product-pricing-strategy`.

## Inputs required

- Raw feedback sources (Sales CRM notes, Support Zendesk exports, Gong call transcripts, user survey results)
- Customer segmentation dimensions (SMB vs Mid-Market vs Enterprise, Tier, Geography)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Ingest qualitative inputs and extract **Atomized Problem Statements** (focus on underlying pain, not requested feature solutions).
3. Tag each problem by **Segment** (SMB, Mid-Market, Enterprise), **Channel** (Sales, Support, UXR, Account Management), and **Frequency/ARR Weight**.
4. Conduct a **Usefulness Assessment** across the core user jobs:
   - *Fully Met*: Existing solution solves the problem friction-free.
   - *Partially Met*: Workarounds or usability issues exist.
   - *Not Met*: Severe blocker with high churn/loss risk.
5. Generate a **Synthesized VoC Problem Digest** linking customer evidence directly to strategic product initiatives.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit atomized problem statements (separated from solution requests).
- Customer segment and source channel tagging.
- Clear prioritization matrix based on frequency and revenue impact.

## Output format

- **Problem Theses**: Atomized statements of user friction.
- **Signal Breakdown by Channel**: Data from Sales, Support, Account Management, and UXR.
- **Segment Impact Analysis**: Weight by customer tier and revenue risk.
- **Actionable Strategic Insights**: Prioritized problem opportunities for product roadmaps.
