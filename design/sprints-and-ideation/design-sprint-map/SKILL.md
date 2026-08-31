---
name: design-sprint-map
description: "Trigger: design sprint map, sprint question, long term goal, target customer friction, pick sprint target, understand phase, jake knapp design sprint, monday sprint map, customer journey map sprint. Scope: Jake Knapp Design Sprint Monday (Understand & Map). Formulates the 6m-5y Long-Term Goal, inverts critical risks into 3 pessimistic Sprint Questions, maps the 5-15 step linear Customer Journey, clusters How Might We (HMW) opportunities, and locks the Decider Target selection. Ingests upstream context directly from ux-discovery-artifacts (Proto-Personas, JTBD, RAT matrix). Boundary: Excludes divergent sketching (use design-sketch-crazy-8s) or general PRD creation (use create-prd)."
---

# Rule: Jake Knapp Design Sprint — Understand & Map (Monday)

> [!IMPORTANT]
> **Foundation**: Grounded in **Jake Knapp, John Zeratsky, and Braden Kowitz** (*Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*).
> **The Prime Directive**: *"Start at the end."* Anchor on the long-term goal, invert assumptions into 3 falsifiable sprint questions, map the customer journey, and pick exactly one target friction point.
>
> **Lifecycle Governance**:
> - **Doctrine**: [`/michael-bolton-rule`](../../product/orchestration/michael-bolton-rule/SKILL.md) (Intent framing & Deming checks).
> - **Upstream Input**: Ingests directly from [`/ux-discovery-artifacts`](../../product/discovery-and-specs/ux-discovery-artifacts/SKILL.md) (Proto-Personas, JTBD hypotheses, journey maps).
> - **Downstream Handoff**: Passes the locked Target and Sprint Questions to [`/design-sketch-crazy-8s`](../design-sketch-crazy-8s/SKILL.md).

---

## When to use

Use this skill on Monday of a Design Sprint to establish problem framing and target selection:
- Formulating the **Long-Term Goal** (6 months to 5 years forward vision).
- Generating the **3 Pessimistic Sprint Questions** via pre-mortem inversion.
- Building the linear **5-to-15 Step Customer Journey Map** (Actors on left $\rightarrow$ Value Goal on right).
- Ingesting and clustering **How Might We (HMW)** notes on the map.
- Guiding the **Decider Target Selection** to isolate exactly one actor and one critical step.

## When not to use

Do not use this skill for:
- Divergent solution sketching or Crazy 8s (use `design-sketch-crazy-8s`).
- Decider voting on UI concepts or storyboarding (use `design-storyboard-decide`).
- Standard PRD authoring without a timeboxed sprint (use `create-prd`).

## Trigger cues

- Request mentions: `design sprint map`, `sprint question`, `long term goal`, `target customer friction`, `pick sprint target`, `understand phase`, `jake knapp design sprint`, `monday sprint map`.
- Scenarios requiring team alignment on high-stakes product uncertainty before prototyping.

## Inputs required

1. **Product / Problem Context**: Raw opportunity, market space, or redesign initiative.
2. **Upstream Discovery Artifacts**: Ingest from `ux-discovery-artifacts` (Proto-Personas, JTBD statements, current workarounds).
3. **Decider Identity**: Designated stakeholder with final veto and selection authority.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Formulate the Long-Term Goal**:
   - Structure an ambitious, qualitative 6-month to 5-year vision: `[Time Horizon] + [Target Customer] + [Transformative Outcome]`.
3. **Invert Assumptions into 3 Sprint Questions**:
   - Run a pre-mortem: *"If this failed in 12 months, what killed us?"*
   - Formulate exactly 3 testable interrogatives (`"Can we...?"`, `"Will users...?"`).
4. **Construct the Customer Journey Map**:
   - List key actors on the left, end goal on the right, and 5–15 linear operational steps in between. Zero branching loops.
5. **Cluster HMW Notes & Lock Decider Target**:
   - Group HMW notes onto map steps.
   - The Decider selects **exactly 1 Target Actor** and **1 Target Step**.

## Completion gate

- [ ] `sprint_map.md` with 5–15 linear steps produced.
- [ ] Exactly 3 falsifiable sprint questions documented.
- [ ] Exactly 1 Target Actor and 1 Target Step locked by the Decider.
- [ ] Seamlessly linked to `ux-discovery-artifacts`.
