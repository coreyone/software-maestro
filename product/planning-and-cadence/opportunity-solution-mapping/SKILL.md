---
name: opportunity-solution-mapping
description: "Map customer opportunities, problems, and candidate solutions using Teresa Torres opportunity solution trees."
---

# Rule: Opportunity Solution Tree (OST) & Continuous Discovery Framework

> [!IMPORTANT]
> **Foundational Methodologies & Upstream/Downstream Links**:
> 1. **Teresa Torres (*Continuous Discovery Habits*)**: 4-Tier Opportunity Solution Tree structure (Outcome $\rightarrow$ Opportunities $\rightarrow$ Solutions $\rightarrow$ Assumption Tests) and weekly continuous discovery cadence.
> 2. **Marty Cagan (*Inspired*, *Empowered*, *Transformed*)**: 5 Product Risk Dimensions (Value, Usability, Feasibility, Viability, Ethics) and Product Discovery Triad (PM, Designer, Tech Lead).
> 3. **Tony Fadell (*Build* — Ch 18: How to Spot a Great Idea)**: The **Painkiller vs. Vitamin Diagnostic** (evaluating acute everyday agony, frequency of frustration, and switching inertia to prune low-urgency convenience branches).
> 4. [`/decision-stack-governance`](../../strategy/decision-stack-governance/SKILL.md): Supplies upstream Company Vision and Strategic Intents.
> 5. [`/voc-insights-pipeline`](../../discovery-and-specs/voc-insights-pipeline/SKILL.md): Feeds atomized customer pain points and qualitative signals into the Opportunity branch.
> 6. [`/experimentation-hypothesis-engine`](../../../growth/experimentation-hypothesis-engine/SKILL.md): Translates high-priority assumption tests into statistical A/B and multivariate experiments.
> 7. [`/create-prd`](../../discovery-and-specs/create-prd/SKILL.md) & [`/prd-to-tickets`](../../discovery-and-specs/prd-to-tickets/SKILL.md): Compiles validated solutions into engineering PRDs and tracer-bullet tickets.

---

## When to use

Use this skill when:
- Translating a single strategic outcome into customer problems before jumping to features.
- Structuring continuous product discovery with the Product Triad (Product Manager, Product Designer, Tech Lead).
- Visualizing the discovery space with an Opportunity Solution Tree (OST).
- Generating multiple competing solution candidates for an opportunity rather than falling in love with a single idea.
- Deconstructing solutions into testable assumptions (Value, Usability, Feasibility, Viability, Ethical) and isolating Leap-of-Faith risks.
- Designing rapid, lightweight assumption tests (smoke tests, prototype walkthroughs, concierge spikes) instead of building full MVPs.

## When not to use

Do not use this skill for:
- Writing granular Jira/Linear tickets or estimating story points (use `prd-to-tickets`).
- Executing phased code delivery or system architecture (use `god-marduk` or `system-architecture-rules`).
- Conducting retrospective team process reviews (use `scrum-review-and-retro`).

## Trigger cues

- Request mentions: `opportunity solution tree`, `OST`, `continuous discovery`, `teresa torres`, `marty cagan`, `opportunity mapping`, `assumption mapping`, `leap of faith assumption`, `product discovery triad`, `opportunity backlog`, `continuous discovery habits`.

## Routing boundary

- Primary for outcome-to-opportunity structuring, multi-solution ideation, and rapid assumption testing.
- Route user narrative journey maps to `user-story-mapping`.
- Route PRD generation to `create-prd`.
- Route statistical A/B test parameterization to `experimentation-hypothesis-engine`.

## Inputs required

1. **Target Outcome**: 1 clear, lagging or leading business/product outcome (e.g., *Increase 30-day retention from 24% to 40%*).
2. **Customer Research & Signals**: Qualitative interviews, support tickets, survey feedback, or VoC problem clusters.
3. **Product Triad Context**: PM business context, Designer UX observations, Tech Lead architectural constraints.
4. **Source of truth**: [references/source.md](references/source.md)

---

## Instructions

1. **Read [references/source.md](references/source.md) first**.
2. **Establish 1 Clear Desired Outcome**:
   - Define a single business outcome (e.g., revenue, churn) or product outcome (e.g., activation rate, feature engagement).
   - Verify outcome is measurable, time-bounded, and directly influenced by user behavior.
3. **Map Customer Opportunities (Needs, Pain Points, Desires)**:
   - Frame opportunities in the customer's voice (*"I struggle to find relevant jobs"*, not *"Build AI filter"*).
   - Apply **Tony Fadell's Painkiller vs. Vitamin Diagnostic**: Score whether the friction represents acute everyday agony (Painkiller) or minor convenience (Vitamin); aggressively prune vitamin branches.
   - Structure opportunities hierarchically (Parent Opportunity $\rightarrow$ Sub-opportunities) to manage cognitive load.
   - Separate problem validation from solution ideation.
4. **Diverge on Multiple Competing Solutions per Opportunity**:
   - Brainstorm at least 3 distinct candidate solutions for each prioritized sub-opportunity.
   - Avoid the "Whether-or-Not" trap (comparing one solution to doing nothing). Compare candidate solutions against each other.
5. **Deconstruct Solutions into 5 Risk Dimensions**:
   - Identify specific underlying assumptions across:
     - **Value / Desirability**: Will customers want and choose this?
     - **Usability**: Can customers understand and navigate the interface?
     - **Feasibility**: Can engineering build this with current infrastructure and time constraints?
     - **Viability**: Does this align with business model, legal, compliance, and go-to-market constraints?
     - **Ethics / Safety**: Does this create unintended harm, bias, or data privacy risks?
6. **Prioritize via Assumption Mapping (2x2 Matrix)**:
   - Plot assumptions on **Importance** (Critical to Fatal) vs. **Evidence / Certainty** (Known vs. Unknown).
   - Isolate the **Leap-of-Faith Assumptions** (High Importance + Low Evidence).
7. **Design Rapid Assumption Tests**:
   - Define small, fast experiments (1–3 days) targeting the Leap-of-Faith assumptions directly without building production code.
   - Use simulated data, clickable Figma prototypes, unlisted landing page smoke tests, or concierge prototypes.
8. **Synthesize into the Continuous Discovery Triad Rhythm**:
   - Maintain a weekly cadence of customer touchpoints ($\ge 1$ interview per week per triad).
   - Update the OST dynamically based on evidence gathered from assumption tests.

---

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- [ ] Explicit 1-outcome root node at the top of the tree.
- [ ] Opportunities framed strictly as user problems, pain points, or desires (no solution language).
- [ ] At least 2–3 distinct candidate solutions mapped under the prioritized opportunity.
- [ ] Deconstructed assumptions tagged across all 5 risk dimensions (Value, Usability, Feasibility, Viability, Ethics).
- [ ] Rapid assumption test specifications mapped to High-Importance / Low-Evidence assumptions.

---

## Output format

- **Desired Outcome**: Measurable target metric and timeframe.
- **Opportunity Hierarchy**: Tree structure of Parent Opportunities and Sub-opportunities with supporting evidence.
- **Solution Candidates**: Comparative matrix of distinct solutions per opportunity.
- **Assumption Deconstruction Matrix**: Assumptions categorized by the 5 Risk Dimensions.
- **Assumption Mapping & Test Plan**: Leap-of-Faith prioritization and concrete experimental test designs.
