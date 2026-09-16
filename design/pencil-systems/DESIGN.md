# Corey Interface Foundation for Pencil.dev

This is the design contract for Pencil.dev exploration in Software Maestro. It makes visual exploration portable without making the canvas a second, competing design system.

## Product character

- Calm, precise, editorial-technical, and useful.
- Use restraint: one strongest focal point, clear hierarchy, and no decorative noise.
- Prefer warm near-black and warm off-white surfaces with a restrained teal transformation accent.
- Do not use generic SaaS decoration, lilac gradients, arbitrary glass, or invented visual effects.
- Treat loading, empty, success, error, recovery, permission, and undo states as first-class design work.

## Pencil source of truth

- Shared library: `design/pencil-systems/core-ios.lib.pen`.
- iOS reconstruction template: `design/pencil-systems/templates/ios-reconstruction-template.pen`.
- Crazy 8s template: `design/pencil-systems/templates/crazy-8s-ios-template.pen`.
- Reusable briefs: `design/pencil-systems/templates/ios-reconstruction-brief.md` and `design/pencil-systems/templates/crazy-8s-brief.md`.
- Keep these files beside screenshots, custom fonts, and source references. Commit `.pen` files with the feature work.

## Token contract

Use the variables in `core-ios.lib.pen`; do not hardcode a competing scale.

| Concern | Contract |
| --- | --- |
| Surfaces | `surface-canvas`, `surface-raised`, `surface-muted` |
| Content | `text-primary`, `text-secondary`, `text-on-accent` |
| Semantic colors | `accent`, `accent-soft`, `success`, `warning`, `danger` |
| Type | SF Pro Text for iOS UI, SF Pro Display for display type, IBM Plex Mono for data and audit notes |
| Pencil preview | Use the documented portable fallback when SF Pro is unavailable; preserve the native token name for handoff |
| Spacing | 4, 8, 12, 16, 24, 32 |
| Radius | 8, 12, 20 |
| Interaction | 44pt minimum target, 2px visible focus treatment, 200ms micro motion, 300ms route motion |
| Themes | Light and dark variables are required for shortlisted concepts |

The Pencil file is the visual contract. Production implementation maps it to the project stack: SvelteKit and TypeScript, Vite, Bun, Biome, Vanilla CSS or Tailwind CSS, Bits UI/shadcn-svelte/Melt UI, Lucide or iconoir, Motion, and Zod or Valibot where the product path needs them. Pencil does not authorize adding a new runtime library.

## Component policy

Use instances from the shared library for Button, Surface/Card, Field, Feedback/Status, Navigation, Overlay, and Layout patterns. Prefer slots and variable aliases. Detach only when the concept proves a real product exception, and record the reason beside the affected frame.

Use icon nodes from Lucide or iconoir with consistent stroke weight. Do not draw replacement icons or paste arbitrary SVGs when a library icon exists.

## Accessibility and usability gate

- Every actionable target is at least 44×44pt.
- Text and controls meet WCAG AA contrast: 4.5:1 for normal text and 3:1 for large text or UI boundaries.
- Focus is visible and never communicated by color alone.
- Labels, errors, loading, empty, success, recovery, and undo states are explicit.
- Reduced-motion behavior is defined before motion is added.
- Use recognition over recall, progressive disclosure, strong information scent, and a clear F/Z scan.
- Keep choices bounded. If a screen presents more than 5–7 meaningful choices, group or defer them.
- Preserve authentic content and the user’s goal. Do not use lorem ipsum or generic AI copy.

## Workflow contract

1. Read this file and the applicable brief.
2. Open Pencil and import `core-ios.lib.pen` through Libraries. Verify variables, themes, components, slots, icons, and fonts before generating.
3. Start from the appropriate template. Keep root frames clean, use `clip: true` for screens, and preserve editability.
4. Use instances and variables first. Use Code on Canvas only for repeated or parameterized structures, then convert to editable layers when the pattern is stable.
5. Compare every reconstruction with the simulator screenshot. Keep viewport, safe area, user, content, and target step fixed while exploring one intentional change.
6. Record deviations, unresolved risks, and audit results in the review brief or beside the affected frame.

## Handoff

Crazy 8s produce divergence evidence. The selected frame moves into the storyboard and then into the rapid prototype facade. A Pencil reconstruction is not proof of native behavior; keep SwiftUI/UIKit or the web facade as the runtime source of truth.
