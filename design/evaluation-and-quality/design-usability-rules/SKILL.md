---
name: design-usability-rules
description: "Trigger: design-usability-rules, usability heuristics, nielsen norman audit, visual design review, UI heuristic evaluation, interface critique. Scope: Usability Heuristics & Visual Interface Critique based on Nielsen Norman 10 heuristics and cognitive affordance principles. Boundary: Excludes marketing copywriting."
---

# 🗺️ Layout & Navigation

## When to use

Use this skill when the task is primarily about design and this guidance is the most relevant operating rule set.

## When not to use

Do not use this skill as the primary guide when another skill has a tighter domain fit for the requested output.

## Trigger cues

- Request explicitly references `design-usability-rules` or this source file.
- Request language includes terms like: design, usability, rules.
- Keywords include: IA, usability, responsive layout, design system, aesthetic direction, motion.

## Routing boundary

- Primary for UX architecture, visual hierarchy, responsiveness, and interface behavior.
- Do not use as primary for backend architecture, threat modeling, or release operations.

## Inputs required

- Goal or task request
- Current constraints (time, scope, platform, risk)
- Existing artifacts (code, docs, screenshots, metrics) when available
- Source of truth: `subagents/rules/design/design-usability-rules.md`

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Extract the non-negotiable rules and translate them into a short execution checklist.
3. Apply the checklist to the current task, produce concrete outputs, and avoid abstract recommendations.
4. Validate outcomes with evidence (tests, screenshots, logs, diffs, or written audit findings).
5. Record decisions and tradeoffs so another engineer can continue without re-discovery.

## Output format

- Primary decision/output: User flow clarity, interaction model, and visual system constraints.
- Summary: one-paragraph decision or result
- Actions: compact checklist with owners and status
- Evidence: links/paths to artifacts proving completion

---

## Anti-Patterns & Usability Heuristic Invariants

Enforce accessibility compliance, cognitive legibility, and robust visual affordances:

- **`low-contrast` (Low contrast text - WCAG AA)**: Text failing minimum contrast ratio ($4.5:1$ for body text, $3.0:1$ for large text $\ge 18\text{pt}$ or $\ge 14\text{pt}$ bold). Evaluate contrast across all composited background surfaces, gradient stops, and interactive `:hover` / `:focus` states.
- **`undersized-ui-text` (Undersized functional UI text)**: Interactive or data-bearing text (links, buttons, navigation items, form labels, table cells, meta badges) rendered below $11\text{px}$. Strictly enforce an $11\text{px}$ floor across all components (with $10\text{px}$ permitted only for non-interactive legal fine print).
- **`tiny-text` (Tiny body text)**: Body paragraphs rendered below $12\text{px}$. Ensure body copy is at least $14\text{px}$ ($16\text{px}$ preferred) for sustained reading comfort across high-DPI and mobile displays.
- **`justified-text` (Justified body text)**: Justified text alignment without automated hyphenation producing uneven word spacing ("rivers of white"). Use `text-align: left` (or `start` for RTL).
- **`skipped-heading` (Skipped heading hierarchy level)**: Jumping heading levels (e.g. `$h1$` directly to `$h3$`), breaking the document outline and screen-reader tree navigation. Maintain strict sequential heading structures.
- **`repeated-container-text` (Redundant repeated container text)**: Rendering the exact same literal label or status $\ge 3$ times within a single card or modular container. State key messages once in their primary contextual slot.
- **`content-hidden-at-rest` (Content invisible at rest)**: Core text left at `opacity: 0` or `visibility: hidden` because an entrance animation or reveal trigger failed to fire. Ensure content is visible by default; layer motion progressively.
- **`text-occlusion` (Text occluded by overlapping layers)**: Text obscured under an opaque decorative graphic, fixed floating widget, or leaking container padding. Ensure safe z-index layering and clearance.
- **`broken-image` (Broken or placeholder image references)**: Missing `src`, empty string `src=""`, or dummy placeholder tokens rendering broken image icons. Provide production-ready media assets with fallback dimensions.

