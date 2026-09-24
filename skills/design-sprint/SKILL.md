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

### Current pen.dev workflow

Use the current authenticated `pen` CLI or the pen.dev desktop/IDE MCP integration. Run `pen status` first; use `pen login` for local work, `PEN_CLI_KEY` for CI/CD, and `pen codex-login` for Codex agent mode. Keep the `.pen` file beside the project and pass `--repo` when the agent must inspect source, tokens, screenshots, or assets.

- For an existing web app, use Code → Design: ask Pencil to recreate the relevant component or page from source, then compare it with the running UI.
- For an existing iOS app, attach Simulator screenshots and SwiftUI/UIKit source. Screenshots define visual truth; source defines structure. Pencil does not directly import a running native app.
- Synchronize CSS variables and Pencil variables when the system is approved. Resolve variable conflicts explicitly; do not create duplicate token families.
- Use desktop browser import for web pages or selected elements, Figma import for complete Figma files, SVG import for editable vectors, and PNG/JPEG import for flattened reference evidence.
- Use the current built-in icon libraries where appropriate: Lucide, Phosphor, Feather, or Material Symbols. Keep production code on the project’s preferred Lucide or iconoir path.
- In Codex, open the intended `.pen` file, enable the Pencil MCP integration, confirm `pencil` is in the live tool list, attach `DESIGN.md` and briefs, and include the full document path in the prompt.

### Corey Pencil system contract

Use [`design/pencil-systems/DESIGN.md`](../../pencil-systems/DESIGN.md) and import [`core-ios.lib.pen`](../../pencil-systems/core-ios.lib.pen) before generating. Start from [`crazy-8s-ios-template.pen`](../../pencil-systems/templates/crazy-8s-ios-template.pen) for iOS target steps, or [`ios-reconstruction-template.pen`](../../pencil-systems/templates/ios-reconstruction-template.pen) when a real screen is the baseline. These are required inputs, not optional starter kits.

- Map Pencil variables and components to the project preferences: SvelteKit and TypeScript, Vite, Bun, Biome, Vanilla CSS or Tailwind CSS, Bits UI/shadcn-svelte/Melt UI, Lucide or iconoir, Motion, and Zod or Valibot where applicable.
- Use SF Pro Text and SF Pro Display for native iOS intent, IBM Plex Mono for data and audit notes, and declare any Pencil preview fallback. Do not silently substitute a competing type scale.
- Read `DESIGN.md`, run `read_skill()`, inspect `get_app_state()`, variables, themes, reusable components, slots, icons, and fonts, then verify the imported library before creating frames.
- Reuse instances and token aliases. Do not detach or invent colors, spacing, radii, type, icons, or motion without documenting the deviation. Use Code on Canvas only for repeated or parameterized structures.
- Apply the usability and accessibility gate: 44pt targets, visible focus, WCAG AA contrast, non-color state communication, reduced motion, authentic labels, and idle/loading/empty/success/error/recovery states.
- Keep the target step, actor, viewport, content, and brand constant across eight frames. Vary one meaningful hypothesis per frame and preserve the locked reference.

### Pencil.dev Crazy 8s Prompt Contract

Every Pencil.dev Crazy 8s prompt must state:

1. The target step, actor, and user outcome.
2. The fixed content and domain constraints shared by all eight frames.
3. The dimensions of variation: layout, hierarchy, navigation, or interaction model.
4. The required labels, frame order, and output file.
5. The review question that will decide which concept advances.
6. The `DESIGN.md` path and imported starter library that the agent must use.
7. The allowed system deviations, with a reason for each deviation.
8. The design-system audit checks required before voting.

### Importing an Existing iOS UI

Pencil.dev does not import a running native iOS app as editable layers. Use the Simulator as the visual source of truth, then combine screenshots with the iOS source code.

1. Capture each relevant app state at the target device size with `xcrun simctl io booted screenshot app-state.png`.
2. Import the PNG into Pencil.dev as a locked reference. PNG and JPEG imports remain flattened image layers.
3. Keep the `.pen` file beside the Xcode project and ask the agent to recreate the relevant SwiftUI or UIKit view as editable layers using the screenshot for visual accuracy and source code for structure.
4. Duplicate the recreated screen into interaction states, then use Pencil transitions for prototype behavior.

For Crazy 8s, import one real screen as the baseline and vary only the locked target step. Keep the device viewport, brand system, typography, user, and real content constant. Vary layout hierarchy, primary-action placement, navigation, information density, and interaction reveal patterns. Treat the screenshot as exact visual evidence and the reconstruction as subject to visual QA.

**Existing-app precedence:** During reconstruction, the Simulator screenshot and observed runtime states are the visual source of truth. `DESIGN.md` explains the tokens and principles behind the UI and constrains proposed changes; it must not silently overwrite an existing screen. Label screenshot-versus-system mismatches as observed legacy, intentional product behavior, or proposed change.

### Mandatory Pencil.dev Design-System Setup

Do not start Pencil exploration from a blank canvas when a product system exists. Treat `DESIGN.md` and the imported Pencil starter library as required design inputs.

1. Read `DESIGN.md` and extract the product principles, aesthetic direction, accessibility stance, tokens, themes, responsive rules, motion rules, and component constraints.
2. Open or create the starter `.pen` file, then import its `.lib.pen` design library into the working document. Inspect variables, theme modes, components, slots, icons, fonts, and reusable patterns before generating screens.
3. Use existing variables and component instances for every matching element. Create a new component only when the concept requires a genuinely new pattern.
4. Include `DESIGN.md` in every agent prompt. Require the agent to cite intentional deviations and never invent a competing color, type scale, spacing scale, radius, or component pattern.
5. Audit each shortlisted concept against the `design-system-rules` checklist: principles, tokens, visual language, accessibility, component reuse, light/dark behavior, responsive behavior, motion, and distinctive character.

If no starter library exists, create the minimum viable library before Crazy 8s: semantic color variables, typography variables, spacing, radii, elevation, focus treatment, light/dark themes, and the core Button, Text, Icon, Field, Feedback, Navigation, Overlay, and Layout components.

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
- [ ] `DESIGN.md` and the Pencil starter library were loaded before generation.
- [ ] The actual Pencil library import, variables, themes, and reusable components were verified before generation.
- [ ] Shortlisted concepts pass the design-system audit, or document intentional deviations.
- [ ] Storyboard ready for Thursday handoff to `design-rapid-prototype-facade`.
