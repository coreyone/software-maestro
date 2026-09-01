---
name: design-rapid-prototype-facade
description: "Trigger: design-rapid-prototype-facade, rapid prototype, hollywood facade, goldilocks prototype, disposable prototype, prototype sprint, stitch prototype, tldraw wireframe prototype, tldraw clickable prototype, stitch rapid facade, basic wireframe facade. Scope: Goldilocks Rapid Facade Prototyping (Thursday Sprint). Builds realistic, disposable, interactive facade prototypes for user testing in <24h across two fidelity tiers: (1) Low-Fidelity Clickable Wireframes via tldraw-offline, or (2) High-Fidelity UI Facades via Google Stitch MCP and the Stitch Build Loop. Boundary: Excludes writing production backend code or database migrations."
---

# Rule: Jake Knapp Design Sprint — Goldilocks Prototype Facade (Thursday)

> [!IMPORTANT]
> **Foundation & Lineage**: 
> - **Jake Knapp, John Zeratsky, Braden Kowitz (*Sprint*)**: The Goldilocks Facade—appropriate fidelity, zero backend engineering, disposable for Friday testing.
> - **Tony Fadell (*Build*)**: *"Make a tangible prototype so the team can touch, hold, and evaluate real sensory experience in <24 hours."*
>
> **Dual-Fidelity Prototype Engines**:
> 1. **Low-Fidelity Wireframe Facades ([`tldraw-offline`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md))**: Use when the team needs ultra-fast, schematic, clickable wireframes on an infinite canvas with scripted interactive buttons (`clickable-card-or-button-ui`).
> 2. **High-Fidelity Visual Facades ([`stitch-design`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md), [`stitch-loop`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md))**: Use when the team needs pixel-perfect visual realism, responsive HTML/CSS, and sub-150ms interactions via Google Stitch MCP.
>
> **The Prime Directive**: *"Fake it, don't build it. Match fidelity to the uncertainty being tested."*

---

## When to use

Use this skill on Thursday of a Design Sprint to build the testing prototype:
- **Tier 1 (Basic Wireframe Facade)**: Building schematic, clickable wireframe prototypes in `tldraw Desktop` via `tldraw-offline` for early structural feedback.
- **Tier 2 (High-Fidelity Web Facade)**: Generating pixel-perfect screens and HTML/CSS via **Google Stitch MCP** (`generate_screen_from_text`, `edit_screens`) and multi-screen baton assembly (`stitch-loop`).
- Organizing the sprint team across **Maker**, **Stitcher**, **Writer**, and **Asset Collector** roles.
- Enforcing **100% authentic copy and domain data** (strict zero *Lorem Ipsum* rule).
- Conducting the mandatory **15:00 Trial Run QA audit**.

## When not to use

Do not use this skill for:
- Storyboarding or deciding on features (use `design-sprint`).
- Writing production backend APIs or databases (use `developer-development-rules` or `system-architecture-rules`).
- Conducting 5-Act user interviews (use `design-5-act-user-interview-testing`).

## Trigger cues

- Request mentions: `goldilocks prototype`, `prototype facade`, `realistic UI illusion`, `stitch prototype`, `tldraw wireframe prototype`, `tldraw clickable prototype`, `rapid interactive prototype`, `hollywood set facade`, `stitch rapid facade`, `basic wireframe facade`.

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Select Prototype Fidelity**:
   - **Low-Fidelity (tldraw)**: When testing conceptual layout or structural navigation. Use `tldraw-offline` to create shape frames, text labels, and wire interactive click transitions with durable document scripts (`script/main.js`).
   - **High-Fidelity (Google Stitch)**: When testing visual desirability, conversion, or emotional resonance. Use Stitch MCP (`generate_screen_from_text`) with `.stitch/DESIGN.md` tokens.
3. **Execute Industrial Role Division**:
   - **Makers**: Build screens on `tldraw` canvas or call Stitch MCP.
   - **Writer**: Injects authentic microcopy, real pricing, and persona names (zero *Lorem Ipsum*).
   - **Stitcher**: Wires navigation links across screens (`site/public/` or `tldraw` frame transitions).
   - **Refinement**: Uses `edit_screens` (Stitch) or `/exec` (tldraw) for fast micro-adjustments.
4. **15:00 Trial Run QA**:
   - Walk the prototype end-to-end against the storyboard. Fix broken paths before 17:00.

## Completion gate

- [ ] Interactive facade covering 100% of storyboard scenes produced.
- [ ] Zero *Lorem Ipsum* or generic placeholder text.
- [ ] Sub-150ms interaction latency on golden path.
- [ ] 15:00 Trial Run QA report logged with zero blocker bugs.
