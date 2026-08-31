---
name: design-rapid-prototype-facade
description: "Trigger: design-rapid-prototype-facade, rapid prototype, hollywood facade, goldilocks prototype, disposable prototype, prototype sprint. Scope: Goldilocks Rapid Facade Prototyping (Thursday Sprint). Builds realistic, disposable, interactive facade prototypes for user testing in <24h. Boundary: Excludes writing production backend code."
---

# Rule: Jake Knapp Design Sprint — Goldilocks Prototype Facade (Thursday)

> [!IMPORTANT]
> **Foundation & Lineage**: 
> - **Jake Knapp, John Zeratsky, Braden Kowitz (*Sprint*)**: The Goldilocks Facade—high surface fidelity, zero backend engineering, disposable for Friday testing.
> - **Tony Fadell (*Build* — Ch 12: Make the Intangible Tangible)**: *"Never debate in PowerPoint or abstract specs. Make a tangible prototype—foam, balsa wood, or clickable interactive shell—so the team can touch, hold, and evaluate real sensory experience in <24 hours."*
>
> **The Prime Directive**: *"Fake it, don't build it."* Create a disposable **Hollywood set facade** with Goldilocks fidelity—pixel-perfect visual surface realism, perceived sensory responsiveness, and zero backend logic, designed to elicit authentic customer reactions.
>
> **Lifecycle Governance**:
> - **Input**: Built strictly from [`/design-sprint`](../../sprints-and-ideation/design-sprint/SKILL.md).
> - **Output Handoff**: Delivers the interactive facade to [`/design-5-act-user-interview-testing`](../../evaluation-and-quality/design-5-act-user-interview-testing/SKILL.md).

---

## When to use

Use this skill on Thursday of a Design Sprint to build the testing prototype:
- Creating a **Goldilocks Facade** (high surface fidelity, zero backend logic).
- Organizing the sprint team across **Maker**, **Stitcher**, **Writer**, and **Asset Collector** roles.
- Building clickable interactive web facades using Stitch, Tailwind/HTML, Figma, or `generative_ui`.
- Enforcing **100% authentic copy and domain data** (strict zero *Lorem Ipsum* rule).
- Conducting the mandatory **15:00 Trial Run QA audit**.

## When not to use

Do not use this skill for:
- Storyboarding or deciding on features (use `design-storyboard-decide`).
- Writing production backend APIs or databases (use `developer-development-rules` or `system-architecture-rules`).
- Conducting 5-Act user interviews (use `design-5-act-user-interview-testing`).

## Trigger cues

- Request mentions: `goldilocks prototype`, `prototype facade`, `realistic UI illusion`, `stitch prototype`, `rapid interactive prototype`, `hollywood set facade`, `fake it dont build it`, `thursday prototype`.

## Inputs required

1. **Storyboard Blueprint**: 10–15 panel grid from `design-storyboard-decide`.
2. **Authentic Domain Data**: Real pricing, persona names, transaction figures.
3. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Adopt the Prototype Mindset**:
   - Prototype is disposable; build only the golden path needed for Friday's interview.
   - Use static mock data and hardcoded state transitions.
3. **Execute Industrial Role Division**:
   - *Makers*: Build screen UI layouts.
   - *Writer*: Write all headlines, button microcopy, and error labels.
   - *Asset Collector*: Gather high-res logos, authentic avatars, and product media.
   - *Stitcher*: Assemble screens into a unified clickable flow.
4. **Enforce Realistic Content**:
   - Replace every generic name, fake date, and placeholder price with realistic values.
5. **Run the 15:00 Trial Run QA**:
   - Walk the prototype end-to-end against the storyboard. Fix missing links and copy bugs before 17:00.

## Completion gate

- [ ] Interactive facade covering 100% of storyboard scenes produced.
- [ ] Zero *Lorem Ipsum* or generic placeholder text.
- [ ] Sub-150ms interaction latency on golden path.
- [ ] 15:00 Trial Run QA report logged with zero blocker bugs.
