---
name: design-storyboard-decide
description: "Trigger: storyboard grid, sticky decision, heat map voting, speed critique, decider supervote, 15 panel storyboard, rumble prototype, sprint decide, wednesday storyboard. Scope: Jake Knapp Design Sprint Wednesday (Decide & Storyboard). Runs the Sticky Decision funnel (Art Museum, Heat Map Dot Voting, 3-min Speed Critique, Straw Poll, Decider Supervote), determines Rumble vs All-in-One architecture, and draws the 10-15 panel Goldilocks Storyboard blueprint from opening scene to target finish. Boundary: Excludes prototype code execution (use design-rapid-prototype-facade) or user interviews (use design-5-act-user-interview-testing)."
---

# Rule: Jake Knapp Design Sprint — Decide & Storyboard (Wednesday)

> [!IMPORTANT]
> **Foundation**: Grounded in **Jake Knapp, John Zeratsky, and Braden Kowitz** (*Sprint*).
> **The Prime Directive**: Convert subjective debate into structured visual selection via the **Sticky Decision Funnel** and draft the **10-to-15 panel Goldilocks Storyboard** as an unambiguous blueprint for Thursday's build.
>
> **Lifecycle Governance**:
> - **Input**: Evaluates 3-panel Solution Sketches from [`/design-sketch-crazy-8s`](../design-sketch-crazy-8s/SKILL.md).
> - **Output Handoff**: Delivers the 10–15 panel Storyboard Blueprint to [`/design-rapid-prototype-facade`](../../experience-and-flows/design-rapid-prototype-facade/SKILL.md).

---

## When to use

Use this skill on Wednesday of a Design Sprint to critique, decide, and storyboard:
- Executing the **Sticky Decision Funnel**:
  1. *Art Museum* (silent gallery walk).
  2. *Heat Map Dot Voting* (component-level interest clustering).
  3. *3-Minute Speed Critique* (structured review per sketch).
  4. *Straw Poll* (non-binding simultaneous vote).
  5. *Decider Supervote* (authoritative vector lock).
- Structuring **Rumble vs. All-in-One** decisions for competing concepts.
- Building the **10-to-15 Panel Goldilocks Storyboard** (Opening Scene $\rightarrow$ Golden Path $\rightarrow$ Target Finish).

## When not to use

Do not use this skill for:
- Monday target mapping (use `design-sprint-map`).
- Tuesday sketching (use `design-sketch-crazy-8s`).
- Building the interactive prototype facade in code (use `design-rapid-prototype-facade`).

## Trigger cues

- Request mentions: `storyboard grid`, `sticky decision`, `heat map voting`, `speed critique`, `decider supervote`, `15 panel storyboard`, `rumble prototype`, `sprint decide`, `wednesday storyboard`.

## Inputs required

1. **Inventory of Solution Sketches**: From `design-sketch-crazy-8s`.
2. **Decider Authority**: Stakeholder holding the Supervote dots.
3. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Execute Sticky Decision Funnel**:
   - Review sketches silently in the Art Museum.
   - Aggregate Heat Map dot clusters and log Speed Critique observations.
   - Collect Straw Poll rationales.
   - Record the Decider Supervote and strategic rationale.
3. **Choose Architecture (All-in-One vs. Rumble)**:
   - If concepts are complementary, merge into one flow. If conflicting, establish a 2-brand Rumble A/B test.
4. **Construct the 10-to-15 Panel Storyboard**:
   - *Panel 1 (Opening Scene)*: Realistic pre-product context (search ad, app store, email).
   - *Panels 2–14 (Journey Spine)*: Step-by-step UI wire-frames with exact button labels and microcopy.
   - *Panel 15 (Target Finish)*: Definitive value payoff or confirmation screen.
   - **Strict Storyboard Laws**: Work with what you have; no new features invented at the board; Decider breaks deadlocks in $<60$ seconds; zero *Lorem Ipsum*.

## Completion gate

- [ ] Sticky Decision Funnel documented with Decider Supervote verdict.
- [ ] Storyboard with strictly 10–15 contiguous panels generated.
- [ ] Panel 1 set in realistic discovery context.
- [ ] 100% of panels contain final copy, UI controls, and transition states.
