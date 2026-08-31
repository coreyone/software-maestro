---
name: how-might-we
description: "Trigger: how-might-we, how might we, HMW, HMW statements, problem reframing, IDEO HMW, min basadur, opportunity framing, generative problem questions. Scope: Generative Problem Reframing & Opportunity Framing via the Min Basadur & IDEO/Stanford d.school How Might We (HMW) methodology. Converts customer pains and insights into expansive, solution-agnostic opportunity statements across 10 reframing angles. Boundary: Excludes running full 5-day design sprints (use design-sprint) or Opportunity Solution Tree tree maintenance (use opportunity-solution-mapping)."
---

# Rule: Generative Problem Reframing via "How Might We" (HMW)

> [!IMPORTANT]
> **Lineage & Origins**: Developed by **Min Basadur** (Simplex process at Procter & Gamble) and codified by **IDEO & Stanford d.school** (Tim Brown, David Kelley).
> **The Prime Directive**: *"A great HMW statement does not propose a solution; it carves open an unexplored problem space with the Goldilocks balance—neither too broad to act upon nor too narrow to constrain creativity."*
>
> **The Goldilocks Calibration**:
> - ❌ **Too Narrow (Prescriptive)**: *"How might we add a dropdown menu to filter search results?"* (Bakes in the UI mechanism).
> - ❌ **Too Broad (Boiling the Ocean)**: *"How might we revolutionize online shopping?"* (Lacks actionable constraint).
> - ✅ **Goldilocks Sweet Spot**: *"How might we make comparing complex technical specifications feel effortless and instantaneous for first-time buyers?"*

---

## When to use

Use this skill when:
- Converting raw customer interview insights, usability blockers, or support pain points into generative opportunity statements.
- Pre-sprint ideation: Generating prompt questions for Crazy 8s or Solution Sketches.
- Deadlocked problem definition: Reframing a technical or business bottleneck into customer-centric challenge angles.
- Brainstorming preparation: Expanding a single negative problem statement into 10 diverse, generative exploration vectors.

## When not to use

Do not use this skill for:
- Orchestrating the full 5-day Design Sprint lifecycle (use `design-sprint`).
- Hierarchical Opportunity Solution Tree mapping across multi-quarter outcomes (use `opportunity-solution-mapping`).
- Writing formal PRDs or BDD user stories (use `create-prd` or `prd-to-tickets`).

## Trigger cues

- Explicit requests: `how-might-we`, `how might we`, `HMW`, `HMW statements`, `generate HMWs`, `reframing problems into opportunities`.
- Situations where the user has a list of complaints, friction points, or survey findings and needs actionable ideation questions.

## Routing boundary

- Route upstream qualitative feedback ingestion to `voc-insights-pipeline`.
- Route multi-day sprint orchestration to `design-sprint`.
- Route assumption risk testing to `opportunity-solution-mapping`.

## Inputs required

1. **Core Problem or Customer Friction Point**: The observed struggle, obstacle, or unmet need.
2. **Target Persona / User Context**: Who is struggling and in what specific circumstance?
3. **Current Known Constraints & Business Reality**: Any hard technical, financial, or regulatory guardrails.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Audit the Raw Problem Statement**:
   - Strip out presupposed solutions or implementation bias (e.g., turn *"Users don't click our onboarding checklist"* into *"Users feel overwhelmed before experiencing core value"*).
3. **Apply the 10 IDEO / Stanford d.school Reframing Angles**:
   - Generate at least one HMW statement for each relevant lens:
     1. *Amplify the Good*: Leverage an existing positive behavior or delight moment.
     2. *Remove the Bad*: Eliminate the friction point entirely.
     3. *Explore the Opposite*: Invert the premise (e.g., what if we made the process slower/more deliberate?).
     4. *Question an Assumption*: Challenge a "mandatory" step or industry orthodoxy.
     5. *Go After Adjectives / Emotions*: Target the user's emotional state (anxiety, frustration, confidence).
     6. *Identify Unexpected Resources*: Use ambient data, idle assets, or community knowledge.
     7. *Create an Analogy*: Borrow mechanics from an unrelated domain (gaming, hospitality, aviation).
     8. *Play Against the Challenge*: Reframe the friction into a feature or game.
     9. *Change the Status Quo / Default*: Shift responsibility from the user to the system.
     10. *Break into Pieces / Slices*: Split a massive ordeal into micro-moments.
4. **Run the Goldilocks Calibration Test on Every HMW**:
   - *Test for Narrowness*: Does it mention a UI element, feature format, or database table? If yes, widen it.
   - *Test for Broadness*: Could this statement apply to any company on earth? If yes, anchor it with customer context.
5. **Score & Select the Top 3 High-Leverage HMWs**:
   - Score candidates on *Actionability*, *Generative Potential* (how many distinct ideas it sparks), and *Strategic Fit*.
   - Mark the primary HMW with the Decider recommendation.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- [ ] Raw problem clearly decoupled from solution mechanisms.
- [ ] Multiple diverse HMW statements generated across distinct reframing lenses.
- [ ] Zero prescriptive UI components or feature mandates in the HMW statements.
- [ ] Exactly 1 primary recommended HMW selected with explicit strategic rationale.

## Output format

```markdown
### 🎯 Problem Diagnosis & Deconstruction
- **Raw Friction**: [Observed customer struggle]
- **Root Cause Context**: [Circumstance and emotional state]

### 💡 10 Reframing Angles (IDEO / Stanford d.school)
1. **Amplify the Good**: How might we...
2. **Remove the Bad**: How might we...
3. **Explore the Opposite**: How might we...
4. **Question an Assumption**: How might we...
5. **Target the Emotion**: How might we...
6. **Leverage Unexpected Resources**: How might we...
7. **Cross-Domain Analogy**: How might we...
8. **Reframe into a Benefit**: How might we...
9. **Automate / Shift Status Quo**: How might we...
10. **Micro-Step Slicing**: How might we...

### 🏆 Curated Top 3 High-Leverage HMWs
- **Primary (Recommended)**: *"How might we..."* (Rationale: [Why this offers the highest generative payoff])
- **Alternative 1 (Contrarian)**: *"How might we..."*
- **Alternative 2 (De-risking)**: *"How might we..."*
```
