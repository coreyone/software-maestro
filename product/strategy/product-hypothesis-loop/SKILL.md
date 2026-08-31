---
name: product-hypothesis-loop
description: "Trigger: product-hypothesis-loop, empirical hypothesis, essential question, user market tech variables, rapid product test, testable assumption, tara seshan hypothesis. Scope: Modern Empirical Product Management & Rapid Hypothesis Loop. Formulates the 1 Essential Question, maps Users x Market x Tech, and dispatches the fastest empirical test vehicle (<48h). Boundary: Excludes full 20-page PRD authoring (use create-prd)."
---

# Rule: Modern Empirical Product Hypothesis Loop

> [!IMPORTANT]
> **Ethos & Theoretical Lineage**:
> Grounded in **Tara Seshan** (*The Empirical Hypothesis Process*), **Marty Cagan** (*4 Product Risks: Value, Usability, Feasibility, Viability*), **Teresa Torres** (*Continuous Discovery & Assumption Testing*), and **Eric Ries** (*Validated Learning Loops*).
>
> **The Prime Directive**: *"Kill documentation-as-validation. Be prolific and empirical."* Never write a 20-page speculative specification before testing the single make-or-break hypothesis across **Users $\times$ Market $\times$ Technology** using the fastest disposable test vehicle.
>
> **Lifecycle Governance**:
> - **Upstream Ingress**: Grounded in [`/ux-discovery-artifacts`](../../discovery-and-specs/ux-discovery-artifacts/SKILL.md) (Proto-Personas, JTBD, RAT matrix) and [`/design-sprint-map`](../../../design/sprints-and-ideation/design-sprint-map/SKILL.md) (Long-term goal, 3 sprint questions).
> - **Test Vehicle Dispatching**: Dispatches to [`/design-rapid-prototype-facade`](../../../design/experience-and-flows/design-rapid-prototype-facade/SKILL.md) + [`/design-5-act-user-interview-testing`](../../../design/evaluation-and-quality/design-5-act-user-interview-testing/SKILL.md) for qualitative testing, or [`/experimentation-hypothesis-engine`](../../../growth/experimentation-hypothesis-engine/SKILL.md) for quantitative A/B testing.
> - **Closed-Loop Learning**: Follows [`/ralph-loop`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md) and [`/continuous-product-loop`](../../operations-and-gtm/continuous-product-loop/SKILL.md) failure codification.
> - **Downstream Synthesis**: Verified hypotheses graduate to [`/create-prd`](../../discovery-and-specs/create-prd/SKILL.md), [`/product-management-press-memo`](../../discovery-and-specs/product-management-press-memo/SKILL.md), and [`/prd-to-tickets`](../../discovery-and-specs/prd-to-tickets/SKILL.md).

---

## When to use

Use this skill when evaluating new product ideas, feature opportunities, or major pivots:
- Formulating the **1 Essential Question** that determines make-or-break product success.
- Mapping the **3-Variable Intersection** (**Users** [behavior/psychology] $\times$ **Market** [unit economics/distribution] $\times$ **Technology** [feasibility/latency]).
- Selecting and dispatching the **cheapest, fastest empirical test vehicle** ($<24-48$ hours).
- Pre-committing to binary **Pass / Pivot / Kill** falsification criteria before building.
- Running rapid iterative learning loops to evolve product strategy based on empirical evidence.

## When not to use

Do not use this skill for:
- Writing complete, post-validation engineering PRDs (use `create-prd`).
- Decomposing validated specs into Jira/GitHub tickets (use `prd-to-tickets`).
- Statistical A/B test sample sizing and SQL telemetry queries (use `experimentation-hypothesis-engine`).
- Pure visual UI token styling (use `design-system-rules`).

## Trigger cues

- Request mentions: `product hypothesis loop`, `empirical hypothesis`, `essential question`, `user market tech variables`, `rapid product test`, `testable assumption`, `assumption mapping`, `fast hypothesis iteration`, `tara seshan hypothesis`, `prolific empirical PM`.

## Inputs required

1. **Raw Product Opportunity / Idea**: Customer friction, market opening, or technological unlock.
2. **Upstream Discovery Artifacts**: Ingest from `ux-discovery-artifacts` or `design-sprint-map`.
3. **Assumptions & Uncertainty**: Key beliefs regarding user behavior, willingness to pay, or technical feasibility.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Step 1: Define the 1 Essential Question**:
   - Invert all assumptions into the single critical question: *"What must be true for this to succeed, and what single assumption would kill us if false?"*
3. **Step 2: Map the 3-Variable Intersection**:
   - **Users**: Identify the non-obvious psychological friction, emotional motivation, and current workarounds.
   - **Market**: Identify willingness to pay, unit economic margin, and competitive distribution channel dynamics.
   - **Technology**: Identify the architectural enabler, API contract, or latency threshold that makes this possible now.
4. **Step 3: Dispatch the Fastest Empirical Test Vehicle**:
   - Select the cheapest vehicle based on the primary risk:
     - *Desirability / Usability Risk*: 24h Hollywood Facade (`design-rapid-prototype-facade`) + 5-Act Interview (`design-5-act-user-interview-testing`).
     - *Market Demand / Pricing Risk*: Fake Door / Smoke Landing Page (`design-landing-page` + `commerce-ux-rules`).
     - *Feasibility / Latency Risk*: 1-Day Technical Spike (<200 LOC via `developer-development-rules`).
     - *Conversion / Metric Lift*: 14-Day A/B Test (`experimentation-hypothesis-engine`).
5. **Step 4: Execute the Closed-Loop Refinement (Ralph Loop Method)**:
   - Establish pre-committed numeric pass criteria.
   - Run the test, capture verbatim quotes and telemetry, codify learnings, and update the hypothesis card within 24 hours.
   - If Validated $
ightarrow$ Feed evidence into `create-prd` and `product-management-press-memo`.
   - If Invalidated $
ightarrow$ Pivot the variable intersection and trigger the next rapid test cycle.

## Completion gate

- [ ] 1 Essential Question formulated in falsifiable interrogative structure.
- [ ] 3-Variable Intersection Matrix (Users × Market × Tech) fully mapped.
- [ ] Fastest Empirical Test Vehicle selected with explicit test design and timeline.
- [ ] Pre-committed binary Pass / Pivot / Kill thresholds defined.
- [ ] Seamlessly linked upstream to `ux-discovery-artifacts` and downstream to `create-prd`.
