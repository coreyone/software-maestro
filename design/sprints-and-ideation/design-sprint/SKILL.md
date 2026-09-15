---
name: design-sprint
description: "Facilitate 5-day design sprints, problem sketches, decision matrices, and user testing."
---

# Rule: Jake Knapp Design Sprint Master Hub (Understand, Diverge, Decide)

> [!IMPORTANT]
> **Lineage & Origins**: Grounded in **Jake Knapp, John Zeratsky, and Braden Kowitz** (*Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*).
> **Dual Prototyping Engines**:
> - **Low-Fidelity Whiteboarding & Wireframing**: [`tldraw-offline`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md) (Live canvas maps, Crazy 8s grids, and visual storyboards with bound arrows).
> - **High-Fidelity AI UI Synthesis**: [`stitch-design`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md) / Stitch MCP (Lightning Demos and `.stitch/DESIGN.md` token synthesis).
>
> **The Prime Directive**: *"Start at the end, work alone together, make visual decisions, and choose the right fidelity for the problem."*

## Pencil.dev Prototyping for Crazy 8s

Use Pencil.dev when the team needs eight fast visual variations that are easier to compare, refine, and export than hand-drawn sketches. Treat each `.pen` file as a disposable exploration artifact, not production UI.

- **Create the board**: Use the headless `pen` CLI to create a `.pen` file with eight clearly labeled frames. Keep each frame focused on one solution variation or one target step.
- **Prompt the variations**: Use `pen --out crazy-8s.pen --prompt-file brief.md --prompt "Create eight materially different concepts for [target step]. Label each frame 1–8. Preserve the same user, goal, and content constraints while varying layout, hierarchy, and interaction."`
- **Work in batches**: Generate one board first, then use `pen --in crazy-8s.pen --out crazy-8s-refined.pen --prompt "Refine only frames 2, 5, and 7 using the critique notes in critique.md"` for targeted iteration.
- **Compare and share**: Export a review image with `pen --in crazy-8s-refined.pen --export crazy-8s.png --export-scale 2`. Use the exported board for silent review, heatmap voting, and Decider selection.
- **Keep the sprint boundary**: Do not add backend behavior, responsive completeness, polished copy, or design-system infrastructure. Carry only the selected concept and its evidence into the storyboard.

### Pencil.dev Crazy 8s Prompt Contract

Every Pencil.dev Crazy 8s prompt must state:

1. The target step, actor, and user outcome.
2. The fixed content and domain constraints shared by all eight frames.
3. The dimensions of variation: layout, hierarchy, navigation, or interaction model.
4. The required labels, frame order, and output file.
5. The review question that will decide which concept advances.

### Importing an Existing iOS UI

Pencil.dev does not import a running native iOS app as editable layers. Use the Simulator as the visual source of truth, then combine screenshots with the iOS source code.

1. Capture each relevant app state at the target device size with `xcrun simctl io booted screenshot app-state.png`.
2. Import the PNG into Pencil.dev as a locked reference. PNG and JPEG imports remain flattened image layers.
3. Keep the `.pen` file beside the Xcode project and ask the agent to recreate the relevant SwiftUI or UIKit view as editable layers using the screenshot for visual accuracy and source code for structure.
4. Duplicate the recreated screen into interaction states, then use Pencil transitions for prototype behavior.

For Crazy 8s, import one real screen as the baseline and vary only the locked target step. Keep the device viewport, brand system, typography, user, and real content constant. Vary layout hierarchy, primary-action placement, navigation, information density, and interaction reveal patterns. Treat the screenshot as exact visual evidence and the reconstruction as subject to visual QA.

---

## When to use

Use this skill during the initial 3 days of a Design Sprint:
- **Mode: `map` (Monday)**: Setting the Long-Term Goal, inverting risks into 3 Sprint Questions, drawing the 5–15 step linear Customer Journey Map on `tldraw` canvas (or Markdown), and selecting the Decider Target.
- **Mode: `sketch` (Tuesday)**: Reviewing Lightning Demos (exploring visual styles with Google Stitch), executing 4-step sketches, forcing 8 variations with Crazy 8s on `tldraw`, and creating 3-panel Solution Sketches with authentic copy.
- **Mode: `decide` (Wednesday)**: Running the Sticky Decision Funnel (Art Museum, Heatmap Dot Voting, Speed Critique, Supervote), drafting the 10–15 frame Storyboard Blueprint on `tldraw` canvas or Stitch prompt schema, and generating `.stitch/DESIGN.md` tokens for Thursday's facade build.

## Prototyping Engine Acceleration

- **tldraw Desktop for Basic Wireframes & Journey Maps**:
  - Use `tldraw-offline` (`/api/doc/:id/exec`) to programmatically render Customer Journey Maps with bound arrows (`helpers.createArrowBetweenShapes`) and arrange Crazy 8s / 10-15 panel storyboard frames directly on the user's live canvas.
- **Google Stitch MCP for High-Fidelity Exploration**:
  - Prompt Stitch MCP (`generate_screen_from_text`) during Tuesday Lightning Demos to explore diverse UI atmospheres (*Bento Grid*, *Glassmorphism*, *Minimalist Monospace*) and synthesize `.stitch/DESIGN.md` tokens.
- **Pencil.dev for Crazy 8s and Disposable Visual Exploration**:
  - Use the headless `pen` CLI to generate, revise, and export eight labeled `.pen` concepts. Use it for divergent visual exploration before the Decider locks one Target Step and Actor; use `design-rapid-prototype-facade` for the selected Thursday prototype.

## Completion gate

- [ ] Clear phase artifacts generated (Map, Crazy 8s, or 10-15 panel Storyboard).
- [ ] Exactly 1 Target Step and Actor locked by the Decider.
- [ ] Storyboard laid out (on `tldraw` canvas, Stitch schema, or structured Markdown).
- [ ] Crazy 8s reviewed as eight labeled Pencil.dev concepts when visual divergence is part of the sprint.
- [ ] Storyboard ready for Thursday handoff to `design-rapid-prototype-facade`.
