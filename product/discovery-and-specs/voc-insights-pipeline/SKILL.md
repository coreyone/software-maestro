---
name: voc-insights-pipeline
description: "Trigger: Voice of Customer, VoC aggregation, feedback tagging, customer signal synthesis, customer problem repository, win/loss feedback, feedback taxonomy, product feedback telemetry. Scope: Ingesting, deduplicating, and synthesizing qualitative feedback from Sales, Support, and UXR into atomized, tagged customer problem theses linked to revenue and customer segments using an abstract, extensible pipeline architecture. Boundary: Excludes live user interview conducting or marketing copywriting."
---

# Rule: Voice of Customer (VoC) Aggregation & Feedback Synthesis

## When to use

Use this skill when collecting, structuring, and synthesizing disparate customer feedback, support tickets, sales win/loss notes, and user research into a single source of truth for problem prioritization.

## When not to use

Do not use this skill for conducting live user interviews directly or writing customer-facing marketing copy.

## Trigger cues

- Request explicitly references `voc-insights-pipeline` or Voice of Customer synthesis.
- Keywords: VoC, customer feedback synthesis, feedback taxonomy, problem repository, win/loss analysis, customer pain points, feature request tagging, support ticket triage, qualitative-quantitative correlation.

## Routing boundary

- Primary for cross-channel qualitative data ingestion, problem atomization, and customer need assessment.
- Route PRD generation to `create-prd` and pricing strategy to `product-pricing-strategy`.

## Inputs required

- Raw feedback sources (Sales CRM notes, Support ticket exports, call recordings/transcripts, survey results)
- Customer segmentation dimensions (SMB vs Mid-Market vs Enterprise, Tier, Geography)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Structure the **Abstract Ingestion & Automation Pipeline**:
   - Ingest multi-channel signals via webhooks or scheduled batch ETL (*e.g., n8n, Trigger.dev, custom webhooks*).
   - Transcribe audio/video interviews through transcription pipelines (*e.g., ElevenLabs, Whisper*).
3. Process raw feedback with **AI Synthesis & Problem Atomization**:
   - Extract **Atomized Problem Statements** separating root friction from requested solutions using LLMs (*e.g., Qwen, Gemini, Claude, OpenAI*).
   - Cluster and deduplicate problem entities using vector embeddings (*e.g., pgvector, Qdrant, Pinecone*).
4. Tag and Enrich signals:
   - Categorize by **Customer Segment** (SMB, Mid-Market, Enterprise), **Channel** (Sales, Support, UXR, Account Management), and **Revenue Weight (ARR/MRR)**.
   - Correlate qualitative friction with quantitative product telemetry (*e.g., PostHog, Amplitude, Mixpanel, Datadog*).
5. Conduct a **Usefulness Assessment Matrix** across core user jobs:
   - *Fully Met*: Existing solution solves the problem friction-free.
   - *Partially Met*: Workarounds or usability issues exist.
   - *Not Met*: Severe blocker with high churn/loss risk.
6. Generate the **Synthesized VoC Problem Digest & Repository Schema**.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit atomized problem statements (separated from solution requests).
- Customer segment, source channel, and revenue impact tagging.
- Architectural design covering the 4 pipeline stages (Ingestion $\rightarrow$ Synthesis $\rightarrow$ Persistence/Telemetry $\rightarrow$ Interface).
- Clear Usefulness Assessment ratings (Fully Met, Partially Met, Not Met).

## Output format

- **Problem Theses**: Atomized statements of user friction.
- **Signal Breakdown by Channel**: Data from Sales, Support, Account Management, and UXR.
- **Segment & Revenue Impact Analysis**: Weight by customer tier and ARR risk.
- **Usefulness Assessment Matrix**: Status across critical user jobs.
- **Abstract Architecture & Example Implementations**: Ingestion mechanism, synthesis engine, persistence/telemetry model, and exploration interface.
