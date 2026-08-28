---
name: voc-insights-pipeline
description: "Trigger: Voice of Customer, VoC aggregation, feedback tagging, customer signal synthesis, customer problem repository, win/loss feedback, feedback taxonomy, PostHog feedback correlation, n8n feedback triage. Scope: Ingesting, deduplicating, and synthesizing qualitative feedback from Sales (CRM/Gong), Support (Zendesk), and UXR into atomized, tagged customer problem theses linked to revenue and customer segments using OSS and preferred stack architectures. Boundary: Excludes live user interview conducting or marketing copywriting."
---

# Rule: Voice of Customer (VoC) Aggregation & Feedback Synthesis

## When to use

Use this skill when collecting, structuring, and synthesizing disparate customer feedback, support tickets, sales win/loss notes, and user research into a single source of truth for problem prioritization.

## When not to use

Do not use this skill for conducting live user interviews directly or writing customer-facing marketing copy.

## Trigger cues

- Request explicitly references `voc-insights-pipeline` or Voice of Customer synthesis.
- Keywords: VoC, customer feedback synthesis, feedback taxonomy, problem repository, win/loss analysis, customer pain points, feature request tagging, Zendesk feedback triage, PostHog qualitative correlation.

## Routing boundary

- Primary for cross-channel qualitative data ingestion, problem atomization, and customer need assessment.
- Route PRD generation to `create-prd` and pricing strategy to `product-pricing-strategy`.

## Inputs required

- Raw feedback sources (Sales CRM notes, Support Zendesk exports, Gong/call transcripts, user survey results)
- Customer segmentation dimensions (SMB vs Mid-Market vs Enterprise, Tier, Geography)
- Preferred stack architecture guidelines (n8n/Trigger.dev, PostHog, Drizzle + Supabase/Neon, Qwen/Gemini via LiteLLM)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Structure the **Ingestion & Automation Flow**:
   - Ingest signals via webhooks/connectors (n8n, Trigger.dev) from CRM, Support, and User Research.
   - Transcribe audio/video interviews using transcription APIs (e.g., ElevenLabs / Whisper).
3. Process raw feedback with **AI Synthesis & Classification**:
   - Use fast, low-cost LLMs (Qwen, Gemini Flash via LiteLLM) to extract **Atomized Problem Statements** (focus on root friction, not feature requests).
   - Deduplicate and cluster problem entities using semantic vector similarity (pgvector in Postgres).
4. Tag and Enrich signals:
   - Categorize by **Customer Segment** (SMB, Mid-Market, Enterprise), **Channel** (Sales, Support, UXR, Account Management), and **Revenue Weight (ARR/MRR)**.
   - Correlate qualitative complaints with **PostHog** product telemetry (session replays, error rates, drop-off funnels).
5. Conduct a **Usefulness Assessment Matrix** across core user jobs:
   - *Fully Met*: Existing solution solves the problem friction-free.
   - *Partially Met*: Workarounds or usability issues exist.
   - *Not Met*: Severe blocker with high churn/loss risk.
6. Generate the **Synthesized VoC Problem Digest & Repository Schema**.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit atomized problem statements (separated from solution requests).
- Customer segment, source channel, and revenue impact tagging.
- Correlation with product analytics (e.g. PostHog) and pipeline automation (e.g. n8n / Trigger.dev).
- Clear Usefulness Assessment ratings (Fully Met, Partially Met, Not Met).

## Output format

- **Problem Theses**: Atomized statements of user friction.
- **Signal Breakdown by Channel**: Data from Sales, Support, Account Management, and UXR.
- **Segment & Revenue Impact Analysis**: Weight by customer tier and ARR risk.
- **Usefulness Assessment Matrix**: Status across critical user jobs.
- **Architecture & Tooling Alignment**: Ingestion workflows (n8n/Trigger.dev), storage schema (Drizzle + Postgres), and analytics telemetry (PostHog).
