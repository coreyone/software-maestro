---
name: design-responsive-rules
description: Use when task matches design-responsive-rules design guidance for IA, usability, responsiveness, systems, motion, and visual QA.
---

# Responsive Web Design (2025) — Guidelines for Design + Design Engineering

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
- Source of truth: `subagents/rules/design/design-responsive-rules.md`

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

## Content-responsive widths and margin discipline

Use viewport tiers as starting points for page-level changes, not as a substitute for content constraints. Margins should respond to readability, hierarchy, rhythm, and visual tension.

### Principles

- Constrain reading width before adding more horizontal content; body copy generally stays near `55–70ch`, with long-form prose closer to `60–70ch`.
- Use nested width roles for `page`, `content`, `prose`, `media`, `navigation`, and `wide`; do not force every region into one universal `max-width`.
- Protect the viewport edge with a dependable minimum inline gutter and maintain the same section-level edge across stacked and reflowed layouts.
- Let margins grow before content stretches on wide screens; whitespace is an intentional responsive output, not leftover space.
- Separate layout width from background width: backgrounds can span the viewport while content remains inside a constrained inner wrapper.
- Treat full-bleed content as exceptional and purposeful—reserved for emphasis, large media, transitions, or deliberate edge tension.
- Align to a few strong axes, usually one to three per section; preserve repeated left edges while allowing deliberate media overflow.
- Make horizontal and vertical spacing feel proportionally related, while keeping section spacing larger than spacing between related elements.
- Match density to purpose: commerce and operational dashboards may tighten gutters; editorial and premium marketing layouts need more air.
- Design the widest and narrowest compositions explicitly; do not stretch tablet into desktop or compress desktop into mobile.

### Concrete tactics

- Define tokens for `page`, `content`, `prose`, `media`, and `wide` widths, plus minimum, fluid, and maximum page gutters.
- Use logical properties such as `padding-inline`, `margin-inline`, `max-inline-size`, and `gap`; avoid percentage-only gutters at the extremes.
- Use fluid outer gutters with a hard floor and ceiling, for example `padding-inline: clamp(20px, 4vw, 80px)`; start narrow layouts around `20–24px` and verify safe-area insets where relevant.
- Center constrained containers with `margin-inline: auto`; use full-width section wrappers with constrained inner containers when only the background should bleed.
- Set body copy near `max-inline-size: 65ch`; constrain short hero headlines near `10–18ch` and use `text-wrap: balance` when supported so wrapping remains intentional.
- Cap major marketing compositions around `1200–1440px` and dense application layouts around `1200–1600px` when the content and interaction model justify those roles.
- Use CSS Grid for intentional column relationships; let images extend one grid column beyond text when appropriate while preserving at least one shared alignment edge.
- Use `minmax()` to stop cards shrinking below usable width. Add a breakpoint when a card, navigation row, or action group becomes awkward—not because a device name changed.
- Use container queries for components that appear in different contexts; define compact, standard, and expanded states with explicit layout, metadata, type, and action behavior.
- Use a small spacing scale such as `4, 8, 12, 16, 24, 32, 48, 64, 96`; prefer parent `gap` over scattered child margins.
- Let whitespace grow slower than typography; increase gutters near oversized type only when visual collision or wrap quality requires it.
- Keep dense tables aligned to the page system, but allow horizontal scrolling rather than crushing columns or reducing text below a usable size.
- Keep controls away from mobile edges and browser gesture zones; use `env(safe-area-inset-left)` and its logical equivalent where relevant.

### Validation and failure checks

- Choose breakpoints from composition failures and minimum usable widths. The existing phone/tablet/desktop tiers are defaults to test, not mandatory design targets.
- Inspect `320px`, `375px`, `768px`, `1024px`, `1440px`, and ultrawide widths continuously, including intermediate widths where the composition is likely to fail.
- Test at `200%` browser zoom, larger accessibility text settings, 30–50% longer headings, translations, empty states, and dense data.
- Confirm that left edges, wrap points, gutter floors, and section rhythm remain intentional after every reflow; verify there is no accidental horizontal scroll.
- Overlay vertical guides on screenshots and inspect the whitespace silhouette at a glance or while squinting/blurred to expose accidental misalignment and weak hierarchy.
- Treat these as failure signals: oversized body lines, unusably narrow cards, random gutter changes, every section spanning edge to edge, centered text that scans poorly, or equal whitespace around visually unequal objects.
