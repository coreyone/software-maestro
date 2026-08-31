---
description: motion guidelines for modern UI animation (NN/g usability + O’Reilly tactical patterns) tuned for SvelteKit + Motion + OSS-first stacks
---

## ▣ Key takeaway
Animations feel “right” when they improve **comprehension** and **control** while staying **fast**, **subtle**, and **consistent**.

## ▸ What “right” means (practical definition)
- Users always know **what changed**, **why it changed**, and **what to do next**.
- Motion never blocks the task.
- Motion never surprises, distracts, or slows the interface.

---

## 0) ▦ Default workflow for this stack (Static Maximalist → Enhanced Motion)
1. **Ship the static HTML page first** (layout, hierarchy, states, copy, empty/loading/error).
2. Add **CSS transitions** for common state changes (hover, focus, pressed, expand/collapse).
3. Add **Mount/unmount transitions** for component presence (menus, dialogs, toasts).
4. Use **Motion (motion.dev)** only for:
   - choreography (sequencing, stagger, shared transitions),
   - gestures/drag,
   - layout transitions (FLIP-like behaviors),
   - complex interactive demos.
5. If Motion is removed, the UI must still work (progressive enhancement mindset).

---

## 1) ◈ NN/g intent rules (motion must be functional)
Animation is allowed only when it serves one of these purposes:
- **Feedback**: confirms an action happened (press, toggle, save).
- **State change**: clarifies before/after (filters applied, error shown).
- **Orientation**: preserves spatial/mental model (where did the panel come from?).
- **Attention**: directs focus to the right element at the right moment.
- **Continuity**: reduces “teleporting” by showing relationships.

If you can’t name the purpose in one sentence, remove the animation.

---

## ◈ High-Impact & Orchestrated Motion
* **One Great Moment**: Prioritize one well-orchestrated page load over scattered micro-interactions.
* **Staggered Reveals**: Use `animation-delay` to create depth and rhythm during entry.
* **Scroll-Triggered Narrative**: Use motion to reveal content as the user explores, creating a sense of discovery.
* **Surprise & Delight**: Design hover and active states that surprise the user—unexpected transitions or unique spatial shifts.

---

## 2) ⧈ Apply NN/g heuristics directly to motion (10 checks)
- **Visibility of system status**: show progress with motion (but keep it brief and non-looping unless loading).
- **Match to the real world**: motion should reflect “physical” expectations (fast start, gentle stop for arrivals).
- **User control & freedom**: users can interrupt/escape (close dialog mid-animation; no locked UI).
- **Consistency & standards**: reuse the same durations/easings across the product (tokens, not one-offs).
- **Error prevention**: don’t animate into destructive states accidentally (avoid “slide-to-delete” surprises).
- **Recognition over recall**: animate reveals to show where options came from (menus anchored to triggers).
- **Flexibility & efficiency**: motion supports power users (no slow flourishes on repeated tasks).
- **Aesthetic & minimalist**: motion is subtle; the content is the hero.
- **Help users recover**: errors animate in near the cause; successes resolve clearly.
- **Help & documentation**: if motion teaches a gesture, provide an alternate control (button + hint).

---

## 3) ⏱️ Timing standards (durations you can reuse)
### ▸ Global rule
Use a small, consistent duration palette. Avoid custom durations per component.

### ▸ Duration tiers (pick one)
- **micro** (hover/press/focus): 80–140ms
- **ui** (toggle/chip/icon/inline feedback): 120–200ms
- **panel** (dropdown/popover/accordion): 160–260ms
- **modal** (dialog/sheet): 220–360ms
- **navigation** (route/section): 300–600ms (only when it clarifies orientation)

### ▸ Distance ↔ duration coupling
- Small distance → shorter duration.
- Large distance → longer duration, but avoid sluggishness.
- If users can complete the task faster than the animation finishes, the animation is too long.

---

## 4) ∿ Easing standards (taste, but systemized)
### ▸ Easing should reflect intent
- **Enter / arrival**: fast start, soft landing (ease-out).
- **Exit / dismissal**: quick commitment (ease-in).
- **Attention nudge**: quick, tiny, and done (short ease-out).
- **Continuous / scrubbed** (scroll/drag): linear or near-linear.

### ▸ Easing palette (keep it small)
Define 2–3 easings and reuse them everywhere.
- `ease.standard` (general UI)
- `ease.emphasized` (rare, for hero moments)
- `ease.exit` (dismissals)

Avoid mixing 7 different easings across a UI. Consistency is the “feels right” multiplier.

---

## 5) ⚙︎ Motion tokens (single source of truth)
### ▸ CSS custom props (works with Vanilla CSS + Tailwind + Svelte)
:root {
  --motion-duration-micro: 120ms;
  --motion-duration-ui: 200ms;
  --motion-duration-modal: 320ms;

  --motion-ease-standard: cubic-bezier(0.2, 0.0, 0.0, 1.0);
  --motion-ease-exit: cubic-bezier(0.4, 0.0, 1.0, 1.0);

  --motion-distance-1: 4px;
  --motion-distance-2: 8px;
  --motion-distance-3: 16px;
}

### ▸ “One-liners” you can standardize
- hover/focus: transition: transform var(--motion-duration-micro) var(--motion-ease-standard), opacity var(--motion-duration-micro) var(--motion-ease-standard);
- enter panels:  transition: transform var(--motion-duration-ui) var(--motion-ease-standard), opacity var(--motion-duration-ui) var(--motion-ease-standard);
- exit panels:   transition: transform var(--motion-duration-ui) var(--motion-ease-exit), opacity var(--motion-duration-ui) var(--motion-ease-exit);

### ▸ Tailwind note
- Prefer Tailwind’s utilities for layout/typography.
- Prefer CSS variables for motion tokens so Motion + CSS + Svelte share the same values.

---

## 6) ⚡ Performance rules (what to animate, what not to animate)
### ▸ Animate “cheap” properties
- **transform** (translate/scale/rotate)
- **opacity**

### ▸ Avoid layout thrash (unless unavoidable)
Avoid animating: width, height, top, left, margin, padding, box-shadow on large areas.

### ▸ Use FLIP for reorders and layout transitions
- Measure first/last positions.
- Invert with transform.
- Play the transform back to 0.

### ▸ “Will-change” is a scalpel, not a lifestyle
- Apply it shortly before animation.
- Remove it afterward.
- Don’t blanket `will-change: transform` across a whole app.

---

## 7) ⊹ Practical patterns (O’Reilly-style reusable recipes)
### A) Button press (feedback)
Goal: instant confirmation without waiting for network.
- duration: micro
- properties: transform (scale 0.98–0.995), opacity (optional)
- rule: never delay the pressed state; ensure the release feels snappy and distinctive.

### B) Dropdown / popover (orientation)
Goal: show it is anchored to a trigger.
- origin: align to trigger (top-left/right depending on placement)
- enter: small translateY + fade
- exit: quicker than enter
- keep distance small (≤16px)

### C) Accordion / disclosure (comprehension)
Goal: reveal content without layout jank.
- prefer transform-based techniques when possible
- if animating height, keep it short and avoid heavy shadows

### D) Toast / inline success (status)
Goal: confirm, then get out of the way.
- enter: 160–220ms
- exit: 120–180ms
- auto-dismiss with pause-on-hover and clear close affordance

### E) Loading (status without anxiety)
Goal: show work is happening without “fake progress.”
- immediate: show skeleton or spinner quickly
- avoid long, decorative loops
- if load completes quickly, avoid flashing loaders (debounce show/hide)

### F) Route transitions (orientation, used sparingly)
Goal: preserve context between pages.
- only animate when it clarifies hierarchy (list → detail, tab switch)
- keep it subtle (fade + small translate)
- never slow down repeated navigation tasks

---

## 8) ♿ Reduced motion (must be first-class)
### ▸ Baseline policy
If `prefers-reduced-motion: reduce`:
- remove large transforms and parallax
- replace springs with simple fades
- keep essential feedback (state change) but minimize motion distance

### ▸ Implementation pattern
- Central toggle: `data-motion="off"` on <html> for debugging and QA parity with reduce-motion users.
- Provide motion fallbacks for:
  - dialogs,
  - route transitions,
  - gesture-driven UI.

---

## 9) ⟡ Motion + SvelteKit + Motion.dev (division of labor)
### ▸ Choose the simplest tool that fits
- **CSS transitions**: hover/press/focus, small state changes.
- **Svelte transitions**: mount/unmount, presence changes.
- **Motion**: gesture + layout transitions + orchestrated sequences.

### ▸ Keep orchestration explicit
- Define variants / states (idle → hover → pressed → loading → success).
- Keep state charts small.
- Prefer declarative timelines over scattered imperative calls.

---

## 10) ▤ Testing & QA gates (modern, practical)
### ▸ “Feels right” review (fast checklist)
- Purpose is explicit (feedback, orientation, status, attention).
- Duration matches distance.
- Easing matches intent (enter vs exit).
- Animation never blocks input.
- Interruptions behave (escape closes, click-away cancels).
- Works with reduced motion.

### ▸ Automated checks (Playwright)
- Run tests with reduced motion enabled.
- Assert critical UI is visible and interactive without waiting for animations.
- Assert no layout shift explosions during transitions (especially on slow devices).

### ▸ Instrumentation (PostHog / Plausible / Umami)
Track regressions motion can cause:
- rage clicks (repeated taps while UI is “busy”)
- time-to-interactive
- drop-off at multi-step flows where transitions exist

---

## 11) ⛔ Do-not-ship list (high-frequency failures)
- Purpose unclear (“because it looks cool”).
- 400ms+ on common repeated interactions.
- Multiple unique easings across the UI.
- Animating layout-heavy properties on large containers.
- Motion that steals focus or moves controls away from the cursor.
- No reduced-motion support.
- Spinners that loop forever without clear next state.

---

## 12) ▣ Copy-paste starter presets (edit once, reuse everywhere)
motion.duration = { micro: 120, ui: 200, modal: 320 }
motion.ease = { standard: [0.2, 0.0, 0.0, 1.0], exit: [0.4, 0.0, 1.0, 1.0] }
motion.distance = { 1: 4, 2: 8, 3: 16 }

Rule: ship tokens first. Then tune per component only when you can prove a usability reason.

---

## 13) Motion Audit and Planning Amendment

Use this protocol for codebase-wide animation audits or when handing motion improvements to another engineer or agent. For a single component, apply only the relevant checks.

### 13.1 Recon: map the motion surface

Before judging animation quality:

1. Identify the framework, rendering model, component library, and installed motion tools: CSS, WAAPI, Svelte transitions, Motion, Framer Motion, React Spring, GSAP, or equivalents.
2. Locate motion tokens, global CSS, Tailwind configuration, keyframes, transition declarations, motion props, layout-animation code, and gesture handlers.
3. Record existing easing, duration, distance, and spring conventions. Extend the established system instead of creating a parallel vocabulary.
4. Describe the product's motion personality: crisp, calm, expressive, playful, cinematic, or utilitarian.
5. Build a frequency map. Distinguish interactions repeated constantly, regularly, occasionally, and rarely.

Useful searches include `transition`, `transition: all`, `animation`, `@keyframes`, `@starting-style`, `motion.`, `animate=`, `useSpring`, `ease-in`, `scale(0)`, `prefers-reduced-motion`, `transform-origin`, `requestAnimationFrame`, and animated layout properties.

### 13.2 Frequency as a motion budget

- Constantly repeated actions such as keyboard navigation, command palettes, and dense list operations should normally have no animation or nearly instant feedback.
- Regular hover, selection, and navigation effects must be short and quiet.
- Occasional dialogs, drawers, disclosures, and toasts may use the standard motion system.
- Rare onboarding, success, and celebration moments may spend more of the delight budget.
- Treat frequency thresholds as review triggers, not universal failures. Retain motion when it materially improves orientation, causality, or accessibility without slowing expert use.

### 13.3 Eight-pass audit

Review motion in these independent passes:

1. **Purpose and frequency**: remove motion whose repeated cost exceeds its explanatory value.
2. **Easing and duration**: verify responsiveness, distance-duration coupling, and token use.
3. **Physicality and origin**: verify scale ranges, anchoring, transform origin, and spatial continuity.
4. **Interruptibility**: rapidly reverse toggles, disclosures, toasts, and gestures; motion must continue from current state rather than restart visibly.
5. **Performance**: find unintended transitions, layout animation, excessive blur, style-recalculation fanout, and unnecessary JavaScript-driven predetermined motion.
6. **Accessibility**: verify reduced motion, hover capability, keyboard behavior, focus stability, and non-motion state cues.
7. **Cohesion and tokens**: identify near-duplicate curves, durations, springs, or mismatched personality.
8. **Missed opportunities**: report only grounded state changes or spatial relationships that currently teleport or become hard to understand.

Every finding must cite `file:line`, observable impact, frequency, severity, confidence, and a concise fix direction. Reopen every cited location before presenting it. Keep additive opportunities separate from defects.

### 13.4 Easing review triggers

Use these as strong starting curves when the product lacks an established motion system:

```css
--ease-out-strong: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out-strong: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

- Prefer strong ease-out for responsive arrivals and many interactive dismissals.
- Prefer ease-in-out for movement or morphing that remains visible throughout.
- Use linear only for genuinely constant or scrubbed motion.
- Flag `ease-in` on interactive UI for review because its slow start can delay visible response; retain it only when a fast committed departure clearly benefits from it.
- Preserve the repo's established curves when they already produce coherent, responsive motion.

### 13.5 Physicality and transform origin

- Do not enter from `scale(0)` unless disappearance into a literal point is part of the model. Start most scale entrances around `0.9–0.97` with opacity zero.
- Keep press feedback subtle, usually within `0.95–0.98`, adjusted for control size and platform conventions.
- Anchor popovers, dropdowns, and tooltips to their trigger. Use library-provided origins when available:

```css
transform-origin: var(--radix-popover-content-transform-origin);
transform-origin: var(--transform-origin);
```

- A centered modal may correctly use `transform-origin: center`; do not treat all centered origins as defects.
- Prefer percentages such as `translateY(100%)` when travel should track the element's own size. Consider `clip-path: inset()` when a reveal should expose rather than move content.

### 13.6 Interruptibility and gesture physics

- Use CSS transitions or springs for reversible dynamic interactions; reserve keyframes for finite staged sequences.
- For CSS entry transitions, prefer `@starting-style` where supported and provide a mounted-state fallback only when required by the browser baseline.
- Springs should carry gesture velocity through interruption. Starting range for restrained interactive motion: bounce `0.1–0.3`; tune against product personality and real-device behavior.
- Judge drag dismissal with velocity and distance together. A starting velocity heuristic is `abs(distance) / elapsedMilliseconds > 0.11`, but tune it to device scale and task risk.
- Add increasing resistance near drag boundaries instead of an abrupt hard stop.
- Use asymmetric timing when intent and response are different phases: deliberate press or hold may take longer; confirmed system response should feel immediate.

### 13.7 Additional performance checks

- Treat `transition: all` as a finding unless a narrowly justified case proves otherwise. List only properties that actually change.
- Prefer CSS or WAAPI for predetermined motion; use JavaScript and springs for dynamic, gesture, or layout-dependent behavior.
- Avoid propagating high-frequency animation through parent CSS variables when it forces broad descendant style recalculation; update the animated element directly when profiling shows fanout.
- Keep transition-time blur restrained. Treat blur near or above `20px` as a profiling trigger, especially in Safari.
- Verify current library behavior before claiming a framework shorthand is not composited. Profile rather than enforcing stale implementation folklore.

### 13.8 Hover and reduced-motion capability

Gate decorative hover motion to devices that actually support precise hover:

```css
@media (hover: hover) and (pointer: fine) {
  .control:hover { transform: scale(1.05); }
}
```

Reduced motion means less spatial movement, not loss of feedback:

- Remove parallax, large translation, zoom, and vestibularly risky movement.
- Retain brief opacity, color, outline, or other non-spatial state feedback when it aids comprehension.
- In JavaScript, branch motion values through the framework's reduced-motion API.
- Test both the OS preference and the existing `data-motion="off"` debugging path.

### 13.9 Cohesion recipes

- Use approximately `30–80ms` staggering only when sequencing communicates grouping or hierarchy. Never let stagger delay interaction readiness.
- For visibly double-exposed crossfades, test a subtle blur near `2px` as a mask; remove it if performance or legibility suffers.
- Consolidate repeated near-identical curves, durations, distances, and springs into tokens after confirming they express the same intent.

### 13.10 Mandatory perceptual verification

Separate mechanical checks from feel checks.

Mechanical checks:

- Typecheck, lint, and test with the repository's exact commands.
- Confirm only expected properties animate.
- Verify no unexpected layout shift, focus movement, or blocked input.
- Exercise reduced motion and fine-pointer capability conditions.

Feel checks:

- Run the actual interaction, not an isolated still state.
- Use the browser Animations panel at roughly 10% playback to inspect origin, overlap, sequencing, and exit behavior frame by frame.
- Spam reversible controls to verify interruption does not restart from zero.
- Test touch gestures on a real device or representative simulator and check velocity, resistance, cancellation, and accidental activation.
- Record when code inspection cannot establish feel; require rendered evidence instead of guessing.

### 13.11 Animation implementation-plan contract

When handing work to an executor with no prior context, include:

1. Commit stamp and drift check.
2. Problem, frequency, user impact, and exact `file:line` evidence.
3. Current code excerpt and exact target values: duration, curve, origin, spring, and reduced-motion behavior.
4. Repository tokens and one exemplar to follow.
5. Explicit in-scope and out-of-scope files; no new dependency unless authorized.
6. Ordered edits with a verification gate after each step.
7. Mechanical checks and the concrete slow-motion feel check.
8. Machine- or eye-checkable done criteria.
9. STOP conditions for code drift, false assumptions, unexpected scope expansion, or repeated verification failure.

Write one plan per coherent finding. Merge findings only when they share the same files, intent, and fix pattern. Do not ask a weaker executor to choose values by taste.
