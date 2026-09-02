---
name: design-responsive-rules
description: "Trigger: design-responsive-rules, responsive layout, media queries, mobile breakpoints, container queries, thumb zone, fold postures, tablet layouts. Scope: Responsive & Adaptive Viewport Behavior across mobile, tablet, foldable, and desktop viewports. Boundary: Excludes color token styling or typography definitions."
---

# Responsive Web Design (2026) — Guidelines for Design + Design Engineering

## When to use

Use this skill when the task is primarily about design and this guidance is the most relevant operating rule set.

## When not to use

Do not use this skill as the primary guide when another skill has a tighter domain fit for the requested output.

## Trigger cues

- Request explicitly references `design-responsive-rules` or this source file.
- Request language includes terms like: design, responsive, rules.
- Keywords include: IA, usability, responsive layout, design system, aesthetic direction, motion.

## Routing boundary

- Primary for UX architecture, visual hierarchy, responsiveness, and interface behavior.
- Do not use as primary for backend architecture, threat modeling, or release operations.

## Inputs required

- Goal or task request
- Current constraints (time, scope, platform, risk)
- Existing artifacts (code, docs, screenshots, metrics) when available
- Source of truth: `references/source.md`

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

## Anti-Patterns & Responsive Viewport Invariants

Prevent broken layout boundaries, gutter clipping, and container spillage across breakpoints:

- **`body-text-viewport-edge` (Body text touching viewport edge)**: Paragraphs or headings rendering flush against mobile viewport edges with zero horizontal gutter. Wrap content in containers providing at least $16\text{px}$ (mobile) to $24\text{–}32\text{px}$ (desktop) padding (`px-4 sm:px-6 lg:px-8`).
- **`first-viewport-column-overflow` (First viewport column overflow)**: Opening multi-column grid where one column runs significantly below the fold while the adjacent column terminates early, creating lopsided dead space and an awkward fold line. Equalize column weights or push auxiliary content below the fold.
- **`edge-flush-cards` (Cards flush against scroller edge)**: Horizontal scroll carousels or tab panels where leading cards sit flush against the boundary at rest, clipping outer rounded corners and elevation shadows. Enforce balanced scroll-padding and inset gutters on both edges of the scroll track.
- **`text-overflow` (Content overflowing container)**: Flex/grid children or long strings bursting out of their parents and triggering unintended horizontal window scrolling. Use `min-w-0` on flex children, `truncate` / `break-words`, and explicit container bounds.
- **`clipped-overflow-container` (Positioned child clipped by overflow container)**: Absolutely-positioned dropdowns, flyout menus, tooltips, or action sheets truncated by ancestor containers with `overflow: hidden` or `overflow: clip`. Render floating overlays through portals or move them outside the clipping boundary.

