---
name: design-system-rules
description: Use when task matches design-system-rules guidance for IA, usability, responsiveness, systems, motion, visual QA, visual identity, art direction, illustration, composition, asset systems, or AI recreation fidelity.
---

# Design System Rules

## When to use

Use this skill when the task is primarily about design-system definition, UX architecture, visual hierarchy, responsive behavior, motion, visual identity, illustration direction, composition, or screenshot-based visual QA.

## When not to use

Do not use this skill as the primary guide when another skill has a tighter domain fit for backend architecture, threat modeling, release operations, or a specialized platform implementation.

## Trigger cues

- User explicitly references `design-system-rules` or this source file.
- Request includes design system, visual language, IA, usability, responsive layout, aesthetic direction, motion, illustration, art direction, collage, layering, asymmetry, edge bleed, visual identity, or brand fidelity.
- The task asks an AI or engineer to recreate an existing interface from screenshots, a URL, or a reference product.

## Routing boundary

Primary for:

- User flow clarity, information hierarchy, and interaction models.
- Responsive layout, visual rhythm, and component consistency.
- Color, typography, imagery, illustration, composition, layering, and motion systems.
- Screenshot-based visual QA and AI-recreation fidelity.

Not primary for backend architecture, threat modeling, release operations, or implementation-specific framework guidance.

## Inputs required

- Goal, audience, platform, and scope.
- Current constraints, risk, and delivery horizon.
- Existing artifacts: code, docs, screenshots, URLs, metrics, brand assets, and interaction states when available.
- Source of truth: `references/source.md` in this skill directory.
- Optional aesthetic profile from `references/aesthetic-profiles/` when the project has a selected visual direction.

## Operating model

1. Read `references/source.md` completely before taking task actions.
2. Inspect the existing interface and asset evidence before naming tokens or prescribing style.
3. Derive the system in layers: identity → visual language → composition grammar → foundations/tokens → components → responsive behavior → motion → accessibility.
4. Treat illustration, imagery, layering, symmetry/asymmetry, edge bleed, negative space, and asset provenance as first-class system concerns whenever they affect recognition.
5. Keep the core analysis profile-neutral. Load an aesthetic profile only when it is selected or supported by evidence; do not let the example profile become a universal default.
6. Translate findings into concrete rules, do/don’t guidance, acceptance checks, and implementation-ready tokens. Avoid abstract taste statements.
7. Validate with evidence: screenshots, interaction states, computed styles, asset inventories, accessibility checks, tests, diffs, or written audit findings.
8. Record decisions, tradeoffs, open dependencies, and likely AI-recreation failure modes so another designer or engineer can continue without rediscovery.

## Aesthetic profiles

Aesthetic profiles are optional overlays on the universal checklist. They describe how the system should express the universal categories for a particular product or visual direction.

- Load only the profile relevant to the current project.
- Preserve the universal requirements for accessibility, responsive behavior, interaction clarity, and evidence.
- Add new profiles under `references/aesthetic-profiles/` instead of hard-coding one style into this skill.
- The included `eames-data.md` profile is an example, not a default.

## AI-recreation resilience

When the target will be recreated by an AI, the output must include:

- An identity sentence that names the distinctive point of view.
- Asset taxonomy and approved/prohibited asset sources.
- Illustration and imagery grammar, including medium, silhouette, linework, texture, and mixed-media rules.
- Composition grammar: dominant object, layer order, symmetry/asymmetry, crop/edge bleed, overlap, negative space, and density.
- Responsive art direction: what scales, what recomposes, what disappears, and what remains invariant.
- A failure-mode table with acceptance checks.
- A prompt-ready handoff block that includes negative constraints, not only positive adjectives.

## Output format

- **Primary decision/output:** user flow clarity, interaction model, visual identity, composition grammar, and visual-system constraints.
- **Summary:** one concise paragraph stating the design-system decision or result.
- **Actions:** compact checklist with status and owner when known.
- **Evidence:** links/paths to screenshots, assets, code, tests, diffs, or audit artifacts.

## Content-responsive widths and margin discipline

### Principles

- Margins respond to content, readability, hierarchy, rhythm, and visual tension—not device labels alone.
- Constrain reading width before adding more horizontal content; body copy generally stays near `55–70ch`, with long-form prose closer to `60–70ch`.
- Use distinct width roles for `page`, `content`, `prose`, `media`, and `wide`; do not force every region into one universal `max-width`.
- Protect the viewport edge with a dependable minimum inline gutter, and keep left/right alignment consistent within a section.
- On wide screens, extra space becomes whitespace before text lines or controls become oversized.
- Separate layout width from background width: a background may span the viewport while meaningful content stays inside a constrained inner container.
- Treat full-bleed content as exceptional and purposeful—reserved for emphasis, large media, transitions, or deliberate edge tension.
- Use a small number of strong alignment axes; hierarchy should be stronger than a grid that flattens every region into the same width.
- Make section spacing larger than spacing between related elements; adjacent items stay closer than unrelated groups.
- Match density to purpose: operational dashboards and tables may tighten gutters, while editorial and premium marketing compositions need more air.
- Compose wide and narrow extremes intentionally; mobile is not merely compressed desktop and desktop is not stretched tablet.

### Concrete tactics

- Define tokens for `page`, `content`, `prose`, `media`, and `wide` widths, plus minimum, fluid, and maximum page gutters.
- Use logical properties such as `padding-inline`, `margin-inline`, `max-inline-size`, and `gap` so rules remain direction-aware.
- Use fluid outer gutters with a hard floor and ceiling, for example `padding-inline: clamp(20px, 4vw, 80px)`; start narrow layouts around `20–24px` and verify safe-area insets where relevant.
- Center constrained containers with `margin-inline: auto`; use a full-width section wrapper with a constrained inner container when only the background should bleed.
- Set body copy near `max-inline-size: 65ch`; constrain short hero headlines near `10–18ch` and use `text-wrap: balance` when supported.
- Cap major marketing compositions around `1200–1440px` and dense application layouts around `1200–1600px` only when the content and interaction model justify those roles.
- Use CSS Grid for intentional column relationships; let media extend one grid column beyond text when appropriate while preserving at least one shared alignment edge.
- Use `minmax()` to stop cards shrinking below usable width. Switch layouts when content becomes awkward, and use container queries for components reused in different contexts.
- Use a small spacing scale such as `4, 8, 12, 16, 24, 32, 48, 64, 96`; prefer parent `gap` over scattered child margins.
- Let whitespace grow slower than typography; add extra gutter near oversized type only when visual collision or wrap quality requires it.
- Give asymmetrical imagery asymmetrical breathing room when equal padding looks mathematically centered but optically wrong.
- Keep dense tables aligned to the page system, but allow horizontal scrolling rather than crushing columns or reducing text below a usable size.

### Validation and failure checks

- Choose breakpoints from composition failures and minimum usable widths, not from a fixed device taxonomy.
- Inspect representative narrow, medium, wide, and ultrawide widths—including `320px`, `375px`, `768px`, `1024px`, `1440px`, and beyond—without treating those widths as design labels.
- Test at `200%` browser zoom, larger accessibility text settings, 30–50% longer headings, translations, empty states, and dense data.
- Confirm that left edges, wrap points, gutter floors, and section rhythm remain intentional; keep controls away from mobile edges and browser gesture zones.
- Overlay vertical guides on screenshots and inspect the page at a glance or while squinting/blurred to expose accidental misalignment and weak hierarchy.
- Treat these as failure signals: oversized body lines, unusably narrow cards, random gutter changes, every block spanning edge to edge, centered text that scans poorly, or equal whitespace around visually unequal objects.
