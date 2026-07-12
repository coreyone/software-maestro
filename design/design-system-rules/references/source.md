# Design System Audit Checklist ✅
Purpose: Quickly assess what a design system includes, how mature it is, and how easy it is to adopt.

---

## 1) Principles & Philosophy
- [ ] Design principles (short, memorable, actionable)
- [ ] UX principles (clarity, speed, error prevention, etc.)
- [ ] Accessibility stance (WCAG target, keyboard-first, reduced motion, contrast)
- [ ] Consistency strategy (what must be consistent vs customizable)
- [ ] Product voice & tone principles
- [ ] Cohesive Aesthetic Point-of-View (Commitment to a bold conceptual direction)
- [ ] Distinctive Character (Avoidance of generic "AI slop" aesthetics)

---

## 2) Foundations (Tokens / Style)
### 2.1 Design Tokens
- [ ] Tokens exist (yes/no)
- [ ] Token categories:
  - [ ] Color (semantic + scale)
  - [ ] Typography (font families, sizes, weights, line heights; distinctive pairings)
  - [ ] Spacing (scale; asymmetric possibilities)
  - [ ] Radii
  - [ ] Elevation / shadow (multi-layered / dramatic)
  - [ ] Borders / strokes (custom/decorative)
  - [ ] Motion (duration, easing; staggered reveals, scroll-triggering)
  - [ ] Backgrounds (gradient meshes, noise textures, grain overlays)
  - [ ] Breakpoints / responsive
  - [ ] Z-index / layering
  - [ ] Opacity
  - [ ] Focus rings
- [ ] Token formats: (CSS vars / JSON / Sass / TS)
- [ ] Token naming system documented
- [ ] Light + Dark modes
- [ ] Theming model (multi-brand / tenant themes / per-app overrides)
- [ ] Token governance (how changes are proposed + approved)

### 2.2 Visual Language
- [ ] Color system guidance (semantic meaning, do/don’t)
- [ ] Typography rules (hierarchy, line length, spacing)
- [ ] Layout guidance (grid, rhythm, spacing rules)
- [ ] Iconography (set + usage rules)
- [ ] Illustration style (if applicable)
- [ ] Data visualization style (charts, colors, accessibility rules)
- [ ] Imagery / photography rules (if applicable)

---

## 3) Components Library
### 3.1 Coverage (Catalog)
- [ ] Foundations: Button, Link, Text, Icon, Spinner
- [ ] Form inputs: TextInput, TextArea, Select, Checkbox, Radio, Switch, Slider
- [ ] Form structure: Label, HelpText, ErrorText, Field, Form layout
- [ ] Feedback: Toast, Alert, Banner, Inline validation, Empty states
- [ ] Overlays: Modal, Drawer, Popover, Tooltip, Menu
- [ ] Navigation: Tabs, Breadcrumbs, Side nav, Top nav, Pagination
- [ ] Layout: Grid, Stack, Box,

---

## 4) Surface, Motion, and Implementation Quality

### 4.1 Surface geometry

- [ ] Nested rounded surfaces use concentric geometry: `outer radius = inner radius + intervening padding`, with optical correction when the mathematical result looks wrong.
- [ ] Icons and asymmetric shapes are optically aligned; play triangles, carets, arrows, and icon/text buttons are not accepted solely because their bounding boxes are centered.
- [ ] Borders and shadows have explicit roles. Use borders for boundaries, inputs, dividers, and dense data; use layered low-opacity shadows for elevation and depth.
- [ ] Images use a subtle neutral outline when edge separation is needed: pure black at low opacity in light mode and pure white at low opacity in dark mode, avoiding tinted edge contamination.
- [ ] Interactive hit areas are at least 44x44 px for touch contexts and 40x40 px for desktop controls; invisible hit-area extensions never overlap adjacent controls.

### 4.2 Motion behavior

- [ ] Interactive state changes use interruptible transitions; fixed keyframes are reserved for staged, one-shot sequences.
- [ ] Entrance motion is divided into semantic chunks and staggered only when sequencing adds hierarchy; exits are quieter and travel less than entrances.
- [ ] State-changing icons preserve object continuity through opacity, scale, or blur rather than abrupt unmount/remount swaps.
- [ ] Default-state components do not replay entrance animation on initial page load unless that entrance is intentional.
- [ ] Press feedback is subtle; begin near `scale(0.96)` and adjust for component size, platform conventions, accessibility, and product tone. Never encode a universal value where context requires another behavior.
- [ ] Every animated component has a reduced-motion equivalent and remains understandable with motion removed.

### 4.3 Motion performance

- [ ] No `transition: all`; list only the properties that change.
- [ ] Prefer composited properties such as transform and opacity. Avoid animating layout properties when a transform can express the same result.
- [ ] Add `will-change` only after observing first-frame stutter, only to the affected element, and remove it when the animation is no longer imminent.
- [ ] Existing project dependencies determine implementation. Use the installed motion system when appropriate; otherwise prefer platform CSS rather than adding a dependency for a minor effect.

### 4.4 Review contract

- [ ] Every implemented change is recorded in a `Before | After` table with component, token/property, and verification evidence.
- [ ] Review output omits categories with no findings and never hides changed values behind a representative subset.
- [ ] Visual QA covers light, dark, high-contrast, reduced-motion, touch, keyboard, and representative responsive states.
