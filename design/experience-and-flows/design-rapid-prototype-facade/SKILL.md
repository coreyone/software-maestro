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

### Required Design-System Inputs

Before generating or reconstructing any screen, load the product system into Pencil:

1. Keep `DESIGN.md`, the working `.pen` file, the starter `.lib.pen` library, custom fonts, and referenced images in one workspace.
2. Read `DESIGN.md` and extract principles, aesthetic direction, accessibility, semantic colors, typography, spacing, radii, elevation, borders, motion, responsive rules, themes, and component constraints.
3. Import the `.lib.pen` file through Pencil’s Libraries panel before using the agent. Inspect variables, themes, components, slots, icons, and fonts. Do not assume a starter kit is active merely because it exists in the folder.
4. Attach `DESIGN.md` to CLI prompts with `--prompt-file DESIGN.md` and state that existing library instances and variables are mandatory. The CLI can edit the prepared `.pen` document; perform library setup in the desktop or IDE workflow when required.
5. Run a design-system audit before handoff. Check token usage, component reuse, accessibility, light/dark behavior, responsive behavior, motion, and distinctive visual character. Record every intentional deviation beside the affected frame.

Use this prompt prefix for every Pencil task:

```text
Read DESIGN.md before editing.
Use the imported Pencil library, its variables, themes, components, slots,
icons, and fonts. Reuse an existing primitive whenever it matches.
Do not invent competing tokens or patterns. List intentional deviations
from DESIGN.md with a reason. Keep all output editable.
```

- **Crazy 8s**: Create eight labeled frames in one `.pen` file. Keep the target step, actor, content constraints, and viewport constant while varying composition, hierarchy, and interaction cues.
- **Prompt with a review question**: Include the sprint brief, authentic domain copy, required frame labels, the dimensions of variation, and the question the team will use for voting.
- **Refine selectively**: Pass critique notes as a prompt file and revise only the shortlisted frames. Preserve the original `.pen` board so the divergence evidence remains inspectable.
- **Export for decision**: Export a single board image for silent review, heatmap voting, and the Decider’s selection. Do not treat generated screens as proof of usability or implementation feasibility.
- **Handoff**: Carry the selected frame, target step, actor, decision rationale, and unresolved risks into the Wednesday storyboard. Use Pencil.dev for exploration; use this Thursday facade workflow only when the selected path needs clickable testing.

Example:

```bash
pen --out crazy-8s.pen --prompt-file DESIGN.md --prompt-file sprint-brief.md --prompt "Create eight materially different Crazy 8s concepts for the locked target step. Use the imported Pencil library and DESIGN.md as mandatory constraints. Label frames 1–8, keep the actor and content constraints constant, and vary layout, hierarchy, and interaction cues. Use authentic copy only."
pen --in crazy-8s.pen --out crazy-8s-shortlist.pen --prompt-file critique.md --prompt "Refine only the shortlisted frames identified in critique.md. Preserve frame labels and do not add backend behavior."
pen --in crazy-8s-shortlist.pen --export crazy-8s.png --export-scale 2
```

### Recreating an Existing iOS App UI

Pencil.dev cannot currently pull a running native iOS app into editable layers. Use this workflow when an existing app is the visual baseline:

1. **Capture the runtime**: Run the app in Xcode Simulator and capture every storyboard state at the target device size. Use `xcrun simctl io booted screenshot app-state.png`, including home, loading, empty, menu, form, error, and selected states.
2. **Import the reference**: Import each PNG into Pencil.dev and lock it behind the reconstruction. PNG and JPEG files become image layers, so they preserve pixel accuracy but are not editable UI.
3. **Recreate the layers**: Keep the `.pen` file beside the Xcode project. Ask the AI agent to recreate the relevant SwiftUI or UIKit view as editable Pencil layers, using the screenshot as the visual source of truth and the source code as the structural source of truth.
4. **Build prototype states**: Duplicate the recreated screen into named states such as `Home`, `Home — menu open`, `Home — loading`, and `Home — error`. Wire transitions between those states in Pencil.
5. **Run visual QA**: Export the Pencil screen and compare it with the Simulator screenshot. Correct safe-area placement, typography, wrapping, spacing, colors, corner radii, shadows, icon sizes, and viewport dimensions before using the facade for testing.

Use this prompt pattern:

```text
Recreate the UI shown in app-home.png from
Sources/Features/Home/HomeView.swift.

Match the screenshot exactly:
- Preserve the 393x852 viewport and safe-area placement
- Match typography, spacing, colors, corner radii, shadows, and icon sizes
- Use editable Pencil layers and reusable components
- Do not invent content
```

For exact native behavior, keep the prototype in SwiftUI or UIKit. Use Pencil for editable visual reconstruction, state exploration, and prototype transitions—not as a replacement for the iOS runtime.

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
- [ ] `DESIGN.md` was read and attached to the agent task.
- [ ] The starter `.lib.pen` library was imported, and matching variables and components were reused.
- [ ] Design-system audit passes for tokens, accessibility, themes, responsive behavior, motion, and distinctive character.
- [ ] Intentional deviations are documented beside the affected frame.
- [ ] Sub-150ms interaction latency on golden path.
- [ ] 15:00 Trial Run QA report logged with zero blocker bugs.
