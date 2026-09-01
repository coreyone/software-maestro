---
name: design-sprint
description: "Trigger: design-sprint, jake knapp design sprint, sprint map, crazy 8s, 4 step sketch, storyboard grid, decider supervote, lightning demos, 3 sprint questions, stitch design sprint, stitch lightning demos. Scope: Jake Knapp Design Sprint Master Hub (Understand, Diverge, Decide). Covers Monday (Map & Target), Tuesday (Crazy 8s & Stitch Lightning Demos via stitch-design), and Wednesday (Storyboard Blueprint & .stitch/DESIGN.md synthesis). Boundary: Excludes Thursday prototype building (use design-rapid-prototype-facade) or Friday user testing (use design-5-act-user-interview-testing)."
---

# Rule: Jake Knapp Design Sprint Master Hub (Understand, Diverge, Decide)

> [!IMPORTANT]
> **Lineage & Origins**: Grounded in **Jake Knapp, John Zeratsky, and Braden Kowitz** (*Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days*), accelerated with **Google Stitch AI Design** ([`stitch-design`](../../../productivity-maestro/executive-and-async/weekly-review-triage/SKILL.md)).
> **The Prime Directive**: *"Start at the end, work alone together, make visual decisions, and synthesize design systems early."*
>
> **The 3-Day Ideation Funnel**:
> 1. **Monday (Understand & Map)**: Long-Term Goal, 3 Sprint Questions, 5-15 step Customer Journey Map, Decider Target.
> 2. **Tuesday (Diverge & Sketch)**: Lightning Demos (exploring visual styles with Google Stitch), 4-Step Sketch (Notes, Ideas, Crazy 8s, 3-Panel Solution Sketches with authentic copy).
> 3. **Wednesday (Decide & Storyboard)**: Sticky Decision Funnel (Art Museum, Heatmap Dot Voting, Speed Critique, Supervote), 10-15 Panel Storyboard Blueprint, and `.stitch/DESIGN.md` design token synthesis.

---

## When to use

Use this skill during the initial 3 days of a Design Sprint:
- **Mode: `map` (Monday)**: Setting the Long-Term Goal, inverting risks into 3 Sprint Questions, drawing the 5–15 step linear Customer Journey Map, and selecting the Decider Target.
- **Mode: `sketch` (Tuesday)**: Reviewing Lightning Demos (generating visual inspiration via `stitch-design` / `generate_screen_from_text`), executing the 4-step sketch, forcing 8 variations with Crazy 8s, and creating 3-panel Solution Sketches with authentic microcopy.
- **Mode: `decide` (Wednesday)**: Running the Sticky Decision Funnel (Art Museum, Heatmap Dot Voting, Speed Critique, Supervote), resolving Rumble vs. All-in-One, drafting the 10–15 frame Storyboard Blueprint, and generating `.stitch/DESIGN.md` tokens for Thursday's facade build.

## Stitch MCP Acceleration (Tuesday & Wednesday)

- **Lightning Demos with Stitch**: Rapidly prompt Stitch MCP (`generate_screen_from_text`) with diverse UI aesthetics (e.g. *Bento Grid*, *Minimalist Monospace*, *Glassmorphism Dashboard*) to gather live visual inspiration.
- **Storyboard-to-Prompt Mapping**: For each storyboard panel, format an enhanced prompt combining the `.stitch/DESIGN.md` token block with the panel's specific scene structure to prepare for Thursday's prototype build (`design-rapid-prototype-facade`).

## Completion gate

- [ ] Clear phase artifacts generated (Map, Crazy 8s, or 10-15 panel Storyboard).
- [ ] Exactly 1 Target Step and Actor locked by the Decider.
- [ ] Visual tokens synthesized into `.stitch/DESIGN.md` or design system notes.
- [ ] Storyboard ready for Thursday handoff to `design-rapid-prototype-facade`.
