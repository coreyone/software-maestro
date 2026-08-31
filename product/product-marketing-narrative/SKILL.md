---
name: product-marketing-narrative
description: "Trigger: product marketing narrative, PMM positioning brief, product messaging hierarchy, value proposition canvas, competitive battlecards, feature launch narrative, buyer persona enablement, product announcement story, launch tier playbook, pain to gain messaging, positioning statement, launch story. Scope: Synthesizing commercial positioning, messaging hierarchies, customer value propositions, competitive battlecards, and launch tier narratives for product and feature releases. Formulates Geoffrey Moore positioning statements, 3-tier messaging hierarchies (hero pitch, strategic pillars, concrete proof points), value proposition mapping (pains, pain relievers, gains, gain creators), and battlecard objection handling. Boundary: Excludes pure marketing copywriting / email subject lines (use marketing-copy-emotion-provoking-action-driven) and operational cross-functional GTM launch checklist gating (use release-readiness-gtm)."
---

# Rule: Product Marketing Positioning, Messaging Hierarchy, & Narrative

## When to use

Use this skill when shaping how a product, feature, or major release is positioned and communicated to the market:
- Crafting the core positioning statement and narrative architecture for a new product or major capability.
- Constructing a 3-tier messaging hierarchy (Hero Value Claim $\to$ 3 Strategic Pillars $\to$ Concrete Features & Proof Points).
- Building competitive battlecards to equip Sales, CS, and Marketing with objection handling and "Why We Win" differentiators.
- Classifying feature release tiers (Tier 1 Strategic Moment, Tier 2 Feature Expansion, Tier 3 Incremental Polish) and drafting the launch narrative.

## When not to use

Do not use this skill for:
- Writing raw marketing ad copy or conversion email subject lines (use `marketing-copy-emotion-provoking-action-driven`).
- Managing cross-functional GTM operational checklists and gating SLAs (use `release-readiness-gtm`).
- Writing engineering technical specifications (use `system-architecture-rules`).

## Trigger cues

- Request mentions: `product marketing narrative`, `positioning statement`, `PMM brief`, `messaging hierarchy`, `value proposition canvas`, `competitive battlecard`, `feature launch narrative`, `buyer persona enablement`, `launch story`, `why we win`.
- Requests to connect product capabilities into a cohesive, high-impact commercial story.

## Routing boundary

- Route GTM cross-functional operational gating (Alpha/Beta/GA checklists) to `release-readiness-gtm`.
- Route ad copywriting, emotional hook phrasing, and CTA tuning to `marketing-copy-emotion-provoking-action-driven`.
- Route PRD product requirements to `create-prd`.

## Inputs required

1. **Target Persona & Segment**: Primary Ideal Customer Profile (ICP), role, and buyer/user dynamics.
2. **Core Customer Problem & Context**: Status quo friction, emotional frustration, and economic cost.
3. **Product Solution & Capabilities**: Specific features and mechanisms being delivered.
4. **Competitive Alternatives**: Direct competitors, legacy tools, or homegrown manual workarounds.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Formulate the Standard Positioning Statement (Geoffrey Moore Framework)**:
   - *For* [Target Customer / Persona]
   - *Who* [Statement of Core Need, Pain, or Opportunity]
   - *The* [Product / Feature Name] *is a* [Product Category / Market Frame]
   - *That* [Key Benefit / Transformational Outcome]
   - *Unlike* [Primary Competitive Alternative or Status Quo]
   - *Our Product* [Primary Differentiator / Core Unfair Advantage].
3. **Map the Value Proposition Canvas (Strategyzer Model)**:
   - **Customer Profile**: Customer Jobs (Functional, Social, Emotional), Pains (Blockers, Risks), Gains (Desired Outcomes).
   - **Value Map**: Products & Services, Pain Relievers (Exact remedies), Gain Creators (Amplified outcomes).
4. **Construct the 3-Tier Messaging Hierarchy**:
   - **Tier 1 (Hero Value Claim)**: Single, memorable sentence answering "What is this and why does it matter to me right now?"
   - **Tier 2 (Three Value Pillars)**: Exactly 3 strategic pillars (e.g. *Speed & Autonomous Velocity*, *Enterprise-Grade Trust*, *Zero Friction Setup*).
   - **Tier 3 (Proof Points & Capabilities)**: Under each pillar, list 2-3 concrete features, performance benchmarks, or customer evidence points.
5. **Build the Competitive Battlecard**:
   - **Landmines to Lay**: Questions the customer should ask competitors that expose their legacy architecture.
   - **Competitor Traps**: Objections competitors will raise about us and how to reframe them.
   - **Why We Win**: The 2 undeniable product superiority pillars.
6. **Classify Release Tier & Enablement Kit**:
   - Classify as **Tier 1** (Company inflection point), **Tier 2** (Substantial feature addition), or **Tier 3** (Continuous enhancement).
   - Detail the internal and external narrative kit (Blog post angle, Sales 1-liner, CS migration guide).

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Formal Geoffrey Moore positioning statement.
- Value Proposition Canvas mapping (pains, pain relievers, gains, gain creators).
- Structured 3-tier messaging hierarchy (Hero, 3 Pillars, Proof points).
- Competitive battlecard with "Why We Win" and objection handling.
- Clear release tier classification.

## Output format

- **Executive Narrative Brief & Release Tier**: Target tier, audience, and commercial objective.
- **Formal Positioning Statement**: The 6-part Geoffrey Moore positioning formula.
- **Value Proposition Canvas**: Customer Jobs/Pains/Gains $\leftrightarrow$ Pain Relievers/Gain Creators.
- **3-Tier Messaging Hierarchy**: Hero Claim $\to$ 3 Pillars $\to$ Proof Points.
- **Competitive Battlecard**: Differentiators, landmines, and competitor objection reframes.
- **Field Enablement Summary**: Sales 1-liner, customer quote soundbite, and changelog angle.
