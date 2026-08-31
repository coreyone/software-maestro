---
name: product-optimizer-feature
description: "Trigger: feature product manager, optimizer PM, feature factory trap, reducing UX friction, checkout optimization, usability heuristics, Marty Cagan 4 risks, John Cutler metric trees, Shreyas Doshi product judgment, Don Norman affordances, Steve Krug dont make me think, Baymard checkout UX, Jeff Patton story mapping, Edo van Royen PRD, improving existing features, flow optimization, conversion rate optimization. Scope: Optimizing, refining, and scaling existing core product surfaces, workflows, and features to maximize conversion, reduce cognitive friction, and eliminate the Feature Factory trap. Formulates Marty Cagan's 4 Product Risks (Value, Usability, Feasibility, Viability); John Cutler's 4-Dimension Metric Trees (Breadth, Depth, Frequency, Efficiency); Shreyas Doshi's High-Agency Judgment, Pre-Mortems, and LNO task allocation; Don Norman & Steve Krug usability heuristics; Baymard Institute checkout benchmarks; and Jeff Patton User Story Mapping. Boundary: Excludes pre-PMF 0-to-1 ideation (use product-zero-to-one), high-level portfolio strategy governance (use decision-stack-governance), or low-level database query optimization (use data-persistence-caching)."
---

# Rule: Feature & Optimizer Product Management

> [!IMPORTANT]
> **Expert Attribution**: This skill embeds the documented frameworks and methodologies of **Marty Cagan** (Empowered Teams & 4 Product Risks), **John Cutler** (Feature Factory & Metric Trees), **Shreyas Doshi** (High-Agency Product Judgment, Pre-Mortems, LNO), **Don Norman** (Design of Everyday Things & Affordances), **Steve Krug** (Don't Make Me Think), **Baymard Institute** (E-Commerce UX Benchmarks), **Jeff Patton** (User Story Mapping), and **Edo van Royen** (Decision-Ready PRDs).

---

## When to use

Use this skill when optimizing, refining, or overhauling existing core product features and workflows:
- Improving existing high-traffic funnels (checkout, registration, onboarding, search results, settings).
- Deconstructing usability friction and cognitive overload on core screens.
- Auditing against **Marty Cagan's 4 Product Risks** (Value, Usability, Feasibility, Business Viability).
- Decomposing product improvement targets using **John Cutler's 4-Dimension Metric Trees** (Breadth, Depth, Frequency, Efficiency).
- Conducting adversarial **Pre-Mortems** (Shreyas Doshi) to uncover hidden failure modes before shipping.
- Slicing backlog releases by user narrative value using **Jeff Patton's User Story Mapping**.

## When not to use

Do not use this skill for:
- 0-to-1 early-stage customer problem discovery before finding PMF (use `product-zero-to-one`).
- High-level multi-year company strategic roadmapping (use `decision-stack-governance` or `portfolio-allocation-capitalization`).
- Low-level database indexing or Redis query caching (use `data-persistence-caching`).

## Trigger cues

- Request mentions: `feature product manager`, `optimizer PM`, `feature factory`, `reduce UX friction`, `checkout optimization`, `usability heuristics`, `Marty Cagan`, `4 risks`, `John Cutler`, `metric tree`, `Shreyas Doshi`, `pre-mortem`, `LNO framework`, `Don Norman`, `Steve Krug`, `Baymard`, `Jeff Patton`, `story mapping`, `improve existing feature`.
- Requests to diagnose conversion drop-offs, streamline multi-step workflows, or write decision-ready feature improvement PRDs.

## Routing boundary

- Route 0-to-1 PMF discovery to `product-zero-to-one`.
- Route closed growth loops and viral flywheels to `product-growth`.
- Route multi-sided marketplace matching to `product-marketplace`.

## Inputs required

1. **Existing Feature / Surface Context**: The current UI flow, user behavior data, and known friction points.
2. **Target Funnel Step & Primary Metric**: The specific conversion step or engagement metric to improve.
3. **Observed Failure / Drop-Off Data**: Funnel conversion percentages, session replays, or user feedback.
4. **Technical & Business Constraints**: Fixed backend APIs, third-party integrations, or legal requirements.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Audit the 4 Product Risks (Marty Cagan)**:
   - *Value Risk*: Will customers actually choose to use this feature over their current workaround?
   - *Usability Risk*: Can the user understand the mental model and complete the task with zero instructions?
   - *Feasibility Risk*: Do our engineers have the time, skills, and infrastructure to build this reliably?
   - *Business Viability Risk*: Does this work for Sales, Legal, Finance, Security, and Compliance?
3. **Map the 4-Dimension Metric Tree Decomposition (John Cutler)**:
   - Deconstruct the target metric across:
     - **Breadth (Reach)**: What % of active users touch this surface?
     - **Depth (Engagement)**: How many actions/units per session?
     - **Frequency**: How many days/weeks do they return to this flow?
     - **Efficiency / Conversion**: What is the completion rate and time-to-complete?
4. **Eliminate Cognitive Load & Usability Friction (Don Norman & Steve Krug)**:
   - Apply **Steve Krug's "Don't Make Me Think"** principles: Self-evident visual hierarchy, eliminate unneeded choices, provide instant feedback.
   - Apply **Don Norman's Affordances & Signifiers**: Clear visual affordances, error prevention, and forgiving recovery.
   - Apply **Baymard E-Commerce Benchmarks**: Eliminate superfluous form fields, enable guest flows, use inline validation.
5. **Slice Sprints via User Story Mapping (Jeff Patton)**:
   - Establish the **Narrative Backbone** (horizontal user journey across time).
   - Slice releases vertically by delivering an end-to-end, functional slice of user value—never by technical layers.
6. **Execute the Shreyas Doshi Pre-Mortem Simulation**:
   - *"Imagine it is 6 months post-launch and this feature was a total failure. What caused it?"*
   - Categorize failure modes: *Mental model confusion, slow latency, hidden edge cases, or lack of ongoing incentive*.
   - Add invariant guardrails directly into the PRD specification to prevent each failure mode.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Full audit of Marty Cagan's 4 Product Risks.
- John Cutler 4-dimension metric tree decomposition (Breadth, Depth, Frequency, Efficiency).
- Steve Krug & Don Norman usability friction elimination.
- Jeff Patton User Story Mapping release slicing.
- Shreyas Doshi Pre-Mortem failure mode simulation and guardrails.

## Output format

- **Feature Optimization Brief**: Target surface, baseline metric, and core hypothesis.
- **4 Product Risks Assessment (Marty Cagan)**: Value, Usability, Feasibility, Viability analysis.
- **4-Dimension Metric Tree (John Cutler)**: Breadth $	imes$ Depth $	imes$ Frequency $	imes$ Efficiency targets.
- **Usability & UX De-Frictioning (Krug / Norman / Baymard)**: Cognitive friction audit and UI heuristics.
- **Story Map Release Slicing (Jeff Patton)**: Narrative backbone and MVP value slice.
- **Pre-Mortem Failure Simulation (Shreyas Doshi)**: Top failure vectors and preventative guardrails.
