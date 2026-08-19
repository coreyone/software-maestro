---
version: alpha
name: Design Lever Encyclopedia
description: A compact, factorized visual grammar for generating polished digital design systems.
colors:
  ink: "#111312"
  paper: "#F5F1E8"
  surface: "#FFFFFF"
  muted: "#68736D"
  signal: "#E4573D"
  night: "#0B1114"
  electric: "#B7FF4A"
  cobalt: "#2457FF"
  sun: "#F0B429"
  mineral: "#9B4D3A"
typography:
  display-editorial:
    fontFamily: "Georgia, ui-serif, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: -0.04em
  display-grotesk:
    fontFamily: "Arial, ui-sans-serif, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 0.98
    letterSpacing: -0.05em
  display-mono:
    fontFamily: "ui-monospace, SFMono-Regular, monospace"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.03em
  body:
    fontFamily: "Arial, ui-sans-serif, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "ui-monospace, SFMono-Regular, monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: 0.08em
rounded:
  sharp: 0px
  restrained: 8px
  soft: 16px
  pill: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
components:
  primary-action:
    backgroundColor: "{colors.signal}"
    textColor: "{colors.paper}"
    rounded: "{rounded.restrained}"
    padding: 12px
    height: 48px
  quiet-action:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.restrained}"
    padding: 12px
    height: 48px
  surface:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.restrained}"
    padding: "{spacing.lg}"
  field:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.restrained}"
    padding: 12px
    height: 48px
---

# DESIGN.md: Compact Lever Encyclopedia

## Overview

This is a design grammar, not a fixed theme. Select exactly one option from each relevant lever, then let the selected system control every screen. The goal is a coherent point of view with enough degrees of freedom for exploration—not a pile of effects.

Evidence basis: 14,340 strict winner records from 2022–2025. The strongest inferred signals were immersive/3D systems, product/UI systems, immersive/spatial art direction, interaction-led work, generative/AI, utilitarian style, experimental style, playful style, and typographic-led work. The source tags are multi-label and reflect award-category and metadata bias; they are inspiration signals, not causal proof of quality.

Generation rule: choose one row per lever; keep one dominant visual hierarchy; make one signature decision legible within the first viewport; vary one lever at a time when searching a design space.

## Colors

Use one palette logic. Do not mix palette logics casually.

| ID | Palette lever | Use |
|---|---|---|
| C1 | **Paper / ink / signal** — `{colors.paper}` foundation, `{colors.ink}` text, `{colors.signal}` one accent | Editorial, civic, product, cultural; maximum clarity with one memorable interrupt. |
| C2 | **Dark / electric** — `{colors.night}` foundation, `{colors.electric}` or `{colors.signal}` signal | Cinematic, immersive, nocturnal, high-contrast experiences. |
| C3 | **Chromatic field** — `{colors.cobalt}`, `{colors.sun}`, `{colors.signal}` in large color planes | Playful, experimental, campaign, social; color is structural, not decoration. |
| C4 | **Mineral / natural** — `{colors.mineral}`, paper, muted neutrals | Organic, tactile, cultural, luxury; warmth without visual noise. |

## Typography

Typography is a voice and a behavior. Pick one primary voice and one role for type.

| ID | Voice lever | Use |
|---|---|---|
| T1 | **Editorial serif** — `{typography.display-editorial}` | Authority, intimacy, cultural depth, long-form narrative. |
| T2 | **Neutral grotesk** — `{typography.display-grotesk}` | Directness, product clarity, contemporary brand confidence. |
| T3 | **Technical mono** — `{typography.display-mono}` | Instrument panels, data, process, systems, precision. |
| T4 | **Expressive display** — oversized, compressed, hand-made, or visibly manipulated type | Type becomes image, navigation, or the main art-directed object. |

| ID | Type behavior | Rule |
|---|---|---|
| TB1 | **Reading** | Preserve measure, rhythm, and calm; effects never interrupt comprehension. |
| TB2 | **Labeling** | Use type as coordinates, metadata, captions, controls, and system language. |
| TB3 | **Performing** | Type changes scale, position, texture, or timing; every transformation carries meaning. |

## Layout

Choose one primary spatial grammar. Secondary pages may borrow its vocabulary but should not replace it.

| ID | Layout lever | Use |
|---|---|---|
| L1 | **Rational grid** — strict columns, stable baseline, explicit alignment | Product/UI, service, data, technical trust. |
| L2 | **Editorial offset** — narrow measure, wide media, one deliberate off-axis anchor | Cultural, narrative, premium, authored content. |
| L3 | **Full-bleed field** — edge-to-edge media, large scene, minimal chrome | Cinematic, immersive, campaign, spatial work. |
| L4 | **Serial modules** — repeated units, rows, cards, or frames | Collections, archives, commerce, dashboards, systems. |

Density is a modifier, not a second layout system: **sparse** (one idea per view), **balanced** (one hero plus supporting structure), or **dense** (many comparable signals with strong grouping).

## Elevation & Depth

| ID | Depth lever | Rule |
|---|---|---|
| E1 | **Tonal** | Separate layers with color and whitespace; no shadow theatrics. |
| E2 | **Constructed** | Use rules, borders, frames, and hard edges to make the system visible. |
| E3 | **Layered** | Use translucent planes, blur, and soft shadow to create atmosphere without losing structure. |
| E4 | **Volumetric** | Use perspective, lighting, material, and depth as the primary composition. |

## Shapes

| ID | Shape lever | Rule |
|---|---|---|
| SH1 | **Architectural** — sharp or nearly sharp corners | Precision, editorial seriousness, technical or civic trust. |
| SH2 | **Restrained softness** — `{rounded.restrained}` to `{rounded.soft}` | Contemporary default; approachable without becoming toy-like. |
| SH3 | **Tactile / pill** — `{rounded.pill}` reserved for controls or tokens | Playful, social, friendly; use selectively or the interface loses hierarchy. |

## Components

Select one system archetype. This determines which components deserve to exist.

| ID | System archetype | Component vocabulary |
|---|---|---|
| SYS1 | **Product / UI** | Navigation, tabs, controls, cards, forms, states, feedback. |
| SYS2 | **Editorial / story** | Chapters, pull quotes, media frames, captions, progress, footnotes. |
| SYS3 | **Campaign / brand** | Hero, proof, offer, CTA, social modules, flexible content blocks. |
| SYS4 | **Cultural / archive** | Index, timeline, collection, object detail, provenance, related works. |
| SYS5 | **Service / civic** | Task steps, status, forms, alerts, eligibility, confirmation, recovery. |
| SYS6 | **Immersive / world** | Scene navigation, hotspots, object panels, spatial map, reset/exit. |

## Do's and Don'ts

- Do give every screen one dominant hierarchy, one primary action, and one memorable visual decision.
- Do keep two font families or fewer, a single spacing rhythm, and one corner language.
- Do make motion, texture, depth, and color explain content, state, or behavior.
- Do provide a quiet/static fallback for every immersive or animated treatment.
- Don't combine volumetric depth, generative motion, maximal color, and dense content by default; two high-intensity levers are usually enough.
- Don't use a component because the archetype does not need it.
- Don't call a decorative effect an art direction concept.

## Generation Protocol

1. Choose `SYS`, `L`, `C`, `T`, `TB`, `E`, and `SH`.
2. Write one sentence: “This design feels ___ because ___.” If the sentence needs more than two adjectives, remove a lever.
3. Define the hero, the repeated unit, and the exit/recovery state before styling details.
4. Generate three variants by changing one lever at a time; keep content and structure constant.
5. Reject any variant whose signature gesture cannot be described in one sentence or whose hierarchy disappears without animation.

Source: [DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md). The YAML frontmatter follows the spec's token groups; the lever tables are intentionally additive guidance.
