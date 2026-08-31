# Design System Audit Checklist

Purpose: assess whether a design system captures not only UI primitives and components, but also the visual identity, composition grammar, asset direction, and behavior needed to reproduce the product without drifting into generic design.

## 1) Principles and philosophy

- [ ] Design principles are short, memorable, and actionable.
- [ ] UX principles cover clarity, speed, error prevention, recovery, and trust.
- [ ] Accessibility stance is explicit: WCAG target, keyboard behavior, focus, contrast, reduced motion, touch targets, and readable text.
- [ ] Consistency strategy distinguishes invariant system rules from intentional art-directed variation.
- [ ] Product voice and tone principles are documented.
- [ ] Identity sentence states the distinctive point of view in one paragraph or less.
- [ ] Distinctive character is named with evidence; the system does not default to generic AI aesthetics.
- [ ] Negative constraints identify what the product must not become.
- [ ] The selected aesthetic profile is explicit and separate from the universal checklist.

## 2) Foundations: tokens and visual language

### 2.1 Design tokens

- [ ] Tokens exist and use a documented naming convention.
- [ ] Color: semantic roles, product/state palette, contrast pairs, light/dark behavior, and color-independent state cues.
- [ ] Typography: family, source, sizes, weights, line heights, tracking, casing, display rules, and readable utility floor.
- [ ] Spacing: base scale, fluid spacing, grid gutters, asymmetric exceptions, and density guidance.
- [ ] Geometry: radii, borders, strokes, corner relationships, optical corrections, and outline rules.
- [ ] Elevation: shadow roles, offset direction, blur policy, and surface layering.
- [ ] Motion: duration, easing, interruptibility, sequencing, scroll-linked behavior, and reduced-motion equivalents.
- [ ] Backgrounds: color fields, gradients, grain, noise, texture, and where each is allowed.
- [ ] Breakpoints: layout changes and art-direction changes are documented separately.
- [ ] Layering: z-index roles for canvas, artwork, content, navigation, overlays, dialogs, and transitions.
- [ ] Opacity and scrim tokens are named and state-specific.
- [ ] Focus rings and interaction-state tokens are defined for every surface color.
- [ ] Illustration tokens: outline, stroke range, silhouette, texture, tilt/rotation, edge bleed, and asset treatment.
- [ ] Composition tokens: dominant-object scale, support-object count, overlap, crop, alignment, negative space, and density.
- [ ] Asset tokens or metadata: approved logo, product/package assets, image treatment, aspect ratios, and provenance.
- [ ] Token formats are implementation-ready: CSS vars, JSON, Sass, TypeScript, or equivalent.
- [ ] Token governance defines who may add, rename, deprecate, or override a token.

### 2.2 Visual language

- [ ] Color guidance explains semantic meaning and do/don’t usage.
- [ ] Typography guidance explains hierarchy, line length, reading rhythm, and localization risk.
- [ ] Layout guidance explains grid, alignment, rhythm, asymmetry, and intentional exceptions.
- [ ] Iconography documents source/set, stroke vocabulary, optical alignment, and icon/text relationships.
- [ ] Illustration style documents medium, subject families, silhouette, linework, stroke variation, texture, palette, and imperfection.
- [ ] Imagery/photography rules document subject, crop, lighting, color treatment, compositing, and approved sources.
- [ ] Mixed-media rules explain how illustration, photography, 3D, typography, and UI surfaces may collide.
- [ ] Data visualization style, when applicable, documents chart palette, direct labels, scales, and non-color encodings.

### 2.3 Art direction and composition grammar

- [ ] Dominant object per state/region is identified.
- [ ] Supporting-object count and hierarchy are defined.
- [ ] Layer order is documented: background field → decorative art → product/hero object → copy/CTA → navigation → overlay/transition, or an intentional alternative.
- [ ] Symmetry/asymmetry rules are explicit; intentional imbalance is not left as vague “playfulness.”
- [ ] Crop, overlap, edge bleed, clipping, and overflow behavior are documented.
- [ ] Negative-space rules explain what must remain empty and why.
- [ ] Scale and rotation ranges are documented for art-directed assets.
- [ ] Silhouette and shape grammar explain what makes objects belong to the identity.
- [ ] Visual density describes how many objects, controls, and text blocks may compete in a region.
- [ ] Responsive art direction says what scales, recomposes, moves, hides, or remains invariant.
- [ ] Whitespace is treated as a compositional token, not missing content to be filled.
- [ ] Asset provenance prevents AI or implementation drift in logos, packaging, characters, and signature illustrations.
- [ ] At least one annotated reference plate or screenshot demonstrates the composition grammar.

## 3) Components library

### 3.1 Coverage

- [ ] Foundations: Button, Link, Text, Icon, Spinner.
- [ ] Form inputs: TextInput, TextArea, Select, Checkbox, Radio, Switch, Slider.
- [ ] Form structure: Label, HelpText, ErrorText, Field, Form layout.
- [ ] Feedback: Toast, Alert, Banner, Inline validation, Empty states.
- [ ] Overlays: Modal, Drawer, Popover, Tooltip, Menu, Dialog.
- [ ] Navigation: Tabs, Breadcrumbs, Side nav, Top nav, Pagination, Product selector.
- [ ] Layout: Grid, Stack, Box, Section, Media, Artboard, Collage layer.
- [ ] Content: Card, Product card, Feature card, Editorial block, Social/gallery tile.

### 3.2 Component contracts

Every component documents:

- [ ] Purpose, anatomy, slots, props, and ownership of content/state.
- [ ] Default, hover, pressed, selected, disabled, loading, error, empty, and success states where applicable.
- [ ] Desktop, tablet, mobile, touch, keyboard, and reduced-motion behavior.
- [ ] Minimum hit area and adjacent-control collision rules.
- [ ] Focus order, accessible name, semantic role, and announcement behavior.
- [ ] Visual variants and permitted art-direction overrides.
- [ ] Do/don’t examples and misuse risks.

## 4) Surface, motion, responsive, and implementation quality

### 4.1 Surface geometry

- [ ] Nested rounded surfaces use concentric geometry: outer radius = inner radius + intervening padding, with optical correction when needed.
- [ ] Icons and asymmetric shapes are optically aligned; bounding-box centering is not sufficient.
- [ ] Borders and shadows have explicit roles. Use borders for boundaries, inputs, dividers, and dense data; use layered low-opacity shadows for elevation and depth.
- [ ] Images use a subtle neutral outline when edge separation is needed; avoid tinted edge contamination.
- [ ] Interactive hit areas are at least 44×44px for touch and 40×40px for desktop controls; invisible extensions do not overlap adjacent controls.

### 4.2 Motion behavior

- [ ] Interactive state changes use interruptible transitions; fixed keyframes are reserved for intentional staged sequences.
- [ ] Entrance motion is divided into semantic chunks and staggered only when sequencing adds hierarchy; exits are quieter.
- [ ] State-changing icons preserve object continuity through opacity, scale, or blur rather than abrupt swaps.
- [ ] Default components do not replay entrance animation on every load unless the entrance is intentional.
- [ ] Press feedback is subtle and context-specific; no universal scale value is imposed.
- [ ] Scroll-linked, parallax, and decorative motion document trigger, duration, easing, performance cost, and reduced-motion fallback.
- [ ] Every animated component remains understandable with motion removed.

### 4.3 Motion performance

- [ ] No `transition: all`; list only changed properties.
- [ ] Prefer composited properties such as transform and opacity.
- [ ] Add `will-change` only after observing first-frame stutter and remove it when no longer imminent.
- [ ] Use the installed motion system when appropriate; otherwise prefer platform CSS over adding a dependency for a minor effect.

### 4.4 Responsive behavior

- [ ] Responsive rules cover both layout changes and art-direction changes.
- [ ] Mobile is explicitly classified as shrink, reflow, or recomposition for each major region.
- [ ] Breakpoint changes preserve hierarchy, product truth, asset legibility, and action clarity.
- [ ] No decorative asset obscures labels, controls, or product/package information at any viewport.
- [ ] Narrow-screen screenshots confirm no clipping, overflow, lost focus state, or accidental density collapse.

### 4.5 Review contract

- [ ] Every implemented change is recorded in a Before | After table with component, token/property, and verification evidence.
- [ ] Review output omits categories with no findings and never hides changed values behind a representative subset.
- [ ] Visual QA covers light, dark, high-contrast, reduced-motion, touch, keyboard, and representative responsive states.
- [ ] Findings use severity tags: `[BLOCKER]`, `[WARNING]`, `[NIT]`.

## 5) AI recreation resilience

- [ ] Likely generic substitutions are listed: stock imagery, perfect symmetry, palette soup, substitute logo, invented packaging, generic motion, or shrunken desktop art.
- [ ] Non-negotiable identity traits are separated from optional decoration.
- [ ] Approved asset sources are named; generated substitutes are explicitly prohibited where fidelity matters.
- [ ] Illustration and imagery rules include positive direction and negative constraints.
- [ ] Composition rules include dominant object, layer order, asymmetry, edge bleed, overlap, negative space, and density.
- [ ] Responsive art direction states what must be recomposed on mobile/tablet.
- [ ] A failure-mode table maps failure signature → why it is wrong → acceptance check.
- [ ] A prompt-ready handoff block is included for AI-assisted recreation.
- [ ] The result is tested against at least one screenshot corpus and one interaction-state corpus.

## 6) Evidence and delivery

- [ ] Screenshot matrix includes desktop, tablet, mobile, full-page/section states, and key interaction states.
- [ ] Asset inventory identifies logo/wordmark, product/package art, illustration families, photography, icons, and fonts.
- [ ] Computed styles or source inspection support exact tokens where available.
- [ ] Accessibility checks include contrast, focus visibility, semantics, alt classification, reduced motion, and hit areas.
- [ ] Output includes: summary, identity statement, interaction model, foundations/tokens, composition grammar, component contracts, responsive art direction, AI handoff, prioritized findings, governance, and evidence.
- [ ] Decisions and tradeoffs are recorded so another designer or engineer can continue without rediscovery.
