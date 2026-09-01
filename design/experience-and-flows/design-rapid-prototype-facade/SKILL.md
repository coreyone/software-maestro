---
name: design-rapid-prototype-facade
description: "Trigger: design-rapid-prototype-facade, rapid prototype, hollywood facade, goldilocks prototype, disposable prototype, prototype sprint, stitch prototype, stitch rapid facade, stitch mcp prototype. Scope: Goldilocks Rapid Facade Prototyping (Thursday Sprint). Builds realistic, disposable, interactive facade prototypes for user testing in <24h using Google Stitch MCP (generate_screen_from_text, edit_screens) and the Stitch Build Loop. Boundary: Excludes writing production backend code or database migrations."
---

# Rule: Jake Knapp Design Sprint — Goldilocks Prototype Facade (Thursday)

> [!IMPORTANT]
> **Foundation & Lineage**: 
> - **Jake Knapp, John Zeratsky, Braden Kowitz (*Sprint*)**: The Goldilocks Facade—high surface fidelity, zero backend engineering, disposable for Friday testing.
> - **Tony Fadell (*Build* — Ch 12: Make the Intangible Tangible)**: *"Make a tangible prototype so the team can touch, hold, and evaluate real sensory experience in <24 hours."*
> - **Google Stitch AI Design ([`stitch-design`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md), [`stitch-loop`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md))**: Fast AI-driven screen generation, design system consistency, and multi-screen baton assembly via Stitch MCP.
>
> **The Prime Directive**: *"Fake it, don't build it."* Create a disposable **Hollywood set facade** with Goldilocks fidelity—pixel-perfect visual surface realism, perceived sensory responsiveness, and zero backend logic, designed to elicit authentic customer reactions.
>
> **Lifecycle Governance**:
> - **Input**: Built strictly from the 10-15 panel storyboard in [`/design-sprint`](../../sprints-and-ideation/design-sprint/SKILL.md).
> - **Output Handoff**: Delivers the interactive facade to [`/design-5-act-user-interview-testing`](../../evaluation-and-quality/design-5-act-user-interview-testing/SKILL.md).

---

## When to use

Use this skill on Thursday of a Design Sprint to build the testing prototype:
- Creating a **Goldilocks Facade** (high surface fidelity, zero backend logic).
- Generating pixel-perfect screens and assets via **Google Stitch MCP** (`generate_screen_from_text`, `edit_screens`).
- Assembling multi-screen clickable flows using the **Stitch Build Loop (`stitch-loop`)** baton pattern.
- Organizing the sprint team across **Maker**, **Stitcher**, **Writer**, and **Asset Collector** roles.
- Enforcing **100% authentic copy and domain data** (strict zero *Lorem Ipsum* rule).
- Conducting the mandatory **15:00 Trial Run QA audit** (and Chrome DevTools visual verification).

## When not to use

Do not use this skill for:
- Storyboarding or deciding on features (use `design-sprint`).
- Writing production backend APIs or databases (use `developer-development-rules` or `system-architecture-rules`).
- Conducting 5-Act user interviews (use `design-5-act-user-interview-testing`).

## Trigger cues

- Request mentions: `goldilocks prototype`, `prototype facade`, `realistic UI illusion`, `stitch prototype`, `rapid interactive prototype`, `hollywood set facade`, `stitch rapid facade`, `thursday prototype`.

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Adopt the Prototype Mindset**:
   - Prototype is disposable; build only the golden path needed for Friday's interview.
3. **Execute Industrial Role Division with Stitch MCP**:
   - **Makers**: Call Stitch MCP (`generate_screen_from_text`) with the enhanced prompts from `.stitch/DESIGN.md` to generate HTML and full-resolution screenshot assets (`.stitch/designs/{page}.html` and `.png`).
   - **Writer**: Injects authentic microcopy, real pricing, and persona names directly into the prompt structure.
   - **Stitcher**: Assembles screens into `site/public/`, updates relative navigation links (`href="{page}.html"`), and maintains visual consistency across headers/footers.
   - **Refinement**: Uses `edit_screens` via Stitch MCP for rapid micro-adjustments (color tweaks, CTA sizing) without full re-generation.
4. **Visual Verification & 15:00 Trial Run**:
   - If Chrome DevTools MCP is available, navigate to `http://localhost:3000/{page}.html` to visually verify rendering fidelity.
   - Walk the prototype end-to-end against the storyboard. Fix missing links and copy bugs before 17:00.

## Completion gate

- [ ] Interactive facade covering 100% of storyboard scenes produced.
- [ ] Zero *Lorem Ipsum* or generic placeholder text.
- [ ] Sub-150ms interaction latency on golden path.
- [ ] 15:00 Trial Run QA report logged with zero blocker bugs.
