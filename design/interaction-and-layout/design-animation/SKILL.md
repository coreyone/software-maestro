---
name: design-animation
description: "Trigger: design-animation, UI motion, animation physics, spring easing, micro-interactions, transition duration, transform origin, reduced motion. Scope: Interface Motion & Animation Physics. Governs easing curves, duration tokens, gestural feedback, and accessibility reduced-motion. Boundary: Excludes static layout styling."
---

# ▣ Key takeaway

## When to use

Use this skill when the task is primarily about design and this guidance is the most relevant operating rule set.

## When not to use

Do not use this skill as the primary guide when another skill has a tighter domain fit for the requested output.

## Trigger cues

- Request explicitly references `design-animation` or this source file.
- Request language includes terms like: design, animation.
- Keywords include: IA, usability, responsive layout, design system, aesthetic direction, motion.

## Routing boundary

- Primary for UX architecture, visual hierarchy, responsiveness, and interface behavior.
- Do not use as primary for backend architecture, threat modeling, or release operations.

## Inputs required

- Goal or task request
- Current constraints (time, scope, platform, risk)
- Existing artifacts (code, docs, screenshots, metrics) when available
- Source of truth: `subagents/rules/design/design-animation.md`

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

## Anti-Patterns & Motion Invariants

Reject decorative motion gimmicks and performance-degrading animation patterns:

- **`bounce-easing` (Bounce or elastic easing)**: Overshoot cubic-bezier curves ($y < -0.1$ or $y > 1.1$), keyframes named `bounce`, `elastic`, `wobble`, `jiggle`, `spring`, or `animate-bounce`. Real physical interfaces decelerate smoothly without cartoonish recoil. Enforce exponential ease-out (`cubic-bezier(0.16, 1, 0.3, 1)` or `cubic-bezier(0, 0, 0.2, 1)`).
- **`pulsing-dot` (Decorative pulsing status dot)**: Small circular indicators ($\le 16\text{px}$ square, `border-radius: 50%`) with infinite pulsing scale, opacity, or shadow loops in headers, navbars, or badges. Reserve pulse animations exclusively for verifiable live data streaming or emergency states; static color-coded indicators with text labels are clearer and calmer.
- **`marquee` (Auto-scrolling marquee)**: `<marquee>` elements or infinite horizontal loops translating track containers across $\ge 20\%$ width. Demands unearned visual attention while concealing half its contents. Replace with deliberate user-driven horizontal scrollers or static multi-column grids.
- **`layout-transition` (Layout property animation)**: Animating geometry properties (`width`, `height`, `padding`, `margin`, `max-height`, `min-width`) that trigger layout thrashing and dropped frames. Restrict transitions to compositor properties (`transform`, `opacity`), or use `grid-template-rows: 0fr -> 1fr` for smooth height accordions.
- **`image-hover-transform` (Image hover scale or rotate)**: Scaling (`scale-105`), translating, or tilting images on cursor hover. Keep editorial and product photography stationary; reserve interaction feedback for buttons and interactive controls.
- **`blinking-cursor` (Decorative blinking cursor)**: Simulating a command-line blinking caret in marketing hero headers. Let typography and layout anchor attention without faux-CLI decoration.

