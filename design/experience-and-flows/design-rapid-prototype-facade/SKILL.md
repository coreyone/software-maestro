---
name: design-rapid-prototype-facade
description: "Build clickable wireframes and high-fidelity UI facades for user prototype testing."
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

### Pencil.dev as a Disposable Exploration Facade

Use Pencil.dev between Tuesday divergence and Wednesday decision when the team needs fast, visual Crazy 8s or a lightweight concept facade. The headless `pen` CLI creates and edits `.pen` files without requiring a GUI; the CLI can also export PNG, JPEG, WEBP, and PDF review artifacts.

Before use, install the CLI with `npm install -g @pen.dev/cli`, confirm Node.js 22.19 or later, and authenticate with `pen login` or `PEN_CLI_KEY`. Run `pen status` before a sprint session.

- **Crazy 8s**: Create eight labeled frames in one `.pen` file. Keep the target step, actor, content constraints, and viewport constant while varying composition, hierarchy, and interaction cues.
- **Prompt with a review question**: Include the sprint brief, authentic domain copy, required frame labels, the dimensions of variation, and the question the team will use for voting.
- **Refine selectively**: Pass critique notes as a prompt file and revise only the shortlisted frames. Preserve the original `.pen` board so the divergence evidence remains inspectable.
- **Export for decision**: Export a single board image for silent review, heatmap voting, and the Decider’s selection. Do not treat generated screens as proof of usability or implementation feasibility.
- **Handoff**: Carry the selected frame, target step, actor, decision rationale, and unresolved risks into the Wednesday storyboard. Use Pencil.dev for exploration; use this Thursday facade workflow only when the selected path needs clickable testing.

Example:

```bash
pen --out crazy-8s.pen --prompt-file sprint-brief.md --prompt "Create eight materially different Crazy 8s concepts for the locked target step. Label frames 1–8, keep the actor and content constraints constant, and vary layout, hierarchy, and interaction cues. Use authentic copy only."
pen --in crazy-8s.pen --out crazy-8s-shortlist.pen --prompt-file critique.md --prompt "Refine only the shortlisted frames identified in critique.md. Preserve frame labels and do not add backend behavior."
pen --in crazy-8s-shortlist.pen --export crazy-8s.png --export-scale 2
```

---

## When to use

Use this skill on Thursday of a Design Sprint to build the testing prototype:
- **Tier 1 (Basic Wireframe Facade)**: Building schematic, clickable wireframe prototypes in `tldraw Desktop` via `tldraw-offline` for early structural feedback.
- **Tier 2 (High-Fidelity Web Facade)**: Generating pixel-perfect screens and HTML/CSS via **Google Stitch MCP** (`generate_screen_from_text`, `edit_screens`) and multi-screen baton assembly (`stitch-loop`).
- **Pre-Thursday (Disposable Visual Exploration)**: Generating and comparing Crazy 8s or selected concept frames in **Pencil.dev** with the headless `pen` CLI. Use this before storyboard lock, not as a substitute for the clickable Thursday facade.
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
- Request mentions: `Pencil.dev`, `pencil prototype`, `pen CLI`, `Crazy 8s board`, or `disposable visual exploration`.

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
