---
name: design-sprint
description: "Trigger: design-sprint, jake knapp design sprint, sprint map, crazy 8s, 4 step sketch, storyboard grid, decider supervote, lightning demos, 3 sprint questions, stitch design sprint, tldraw design sprint, tldraw wireframes, tldraw storyboard. Scope: Jake Knapp Design Sprint Master Hub (Understand, Diverge, Decide). Covers Monday (Map & Target on tldraw/Markdown), Tuesday (Crazy 8s & Stitch/tldraw sketches), and Wednesday (Storyboard Grid & .stitch/DESIGN.md tokens). Boundary: Excludes Thursday prototype building (use design-rapid-prototype-facade) or Friday user testing (use design-5-act-user-interview-testing)."
---

# Rule: Jake Knapp Design Sprint Master Hub (Understand, Diverge, Decide)

> [!IMPORTANT]
> **Lineage & Origins**: Grounded in **Jake Knapp, John Zeratsky, and Braden Kowitz** (*Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*).
> **Dual Prototyping Engines**:
> - **Low-Fidelity Whiteboarding & Wireframing**: [`tldraw-offline`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md) (Live canvas maps, Crazy 8s grids, and visual storyboards with bound arrows).
> - **High-Fidelity AI UI Synthesis**: [`stitch-design`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md) / Stitch MCP (Lightning Demos and `.stitch/DESIGN.md` token synthesis).
>
> **The Prime Directive**: *"Start at the end, work alone together, make visual decisions, and choose the right fidelity for the problem."*

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

## Completion gate

- [ ] Clear phase artifacts generated (Map, Crazy 8s, or 10-15 panel Storyboard).
- [ ] Exactly 1 Target Step and Actor locked by the Decider.
- [ ] Storyboard laid out (on `tldraw` canvas, Stitch schema, or structured Markdown).
- [ ] Storyboard ready for Thursday handoff to `design-rapid-prototype-facade`.
