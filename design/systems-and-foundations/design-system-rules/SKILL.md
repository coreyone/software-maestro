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
