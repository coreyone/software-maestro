---
name: design-system-rules
description: "Define design tokens, visual hierarchies, typographic scales, color palettes, and spacing systems."
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

---

## Anti-Patterns & Visual System Failure Modes

Guard against common generated-UI tells and visual system regressions across surfaces, typography, color, and layout.

### 1. Visual Details & Surfaces
- **`side-tab` (Side-tab accent border)**: Single-sided thick chromatic border ($\ge 2\text{px}$ on rounded cards, $\ge 3\text{px}$ on square cards), absolute $3\text{–}12\text{px}$ pseudo-element bar (`::before`/`::after`), or single-edge inset `box-shadow`. Remove the decorative stripe entirely or rely on subtle neutral elevation. *(Exemption: live alert/status banners and toasts)*.
- **`border-accent-on-rounded` (Border accent on rounded element)**: Asymmetric thick border on a container with `border-radius > 0` causing edge clash. Commit to either a borderless rounded card or a fully enclosed uniform border.
- **`dark-glow` (Glowing shadow accents)**: Zero-offset chromatic halo (`0 0 Npx <color>`) or blurred colored shadows on dark backgrounds ($\text{luminance} < 0.1$). Use neutral elevation shadows (`rgb(0 0 0 / alpha)`) and subtle surface tonal shifts.
- **`radial-halo` (Radial-gradient background halo)**: Saturated center stop ($\text{spread} \ge 24$, $\text{alpha} \ge 0.7$) dissolving to transparent over dark root backgrounds. Ground surfaces with solid shifts or subtle dark tints without fluorescent backdrops.
- **`radial-spotlight-glow` (Decorative radial spotlight glow)**: Low-opacity ($< 0.5$) colored radial gradient wash placed behind hero/features as a fake light cone. Use intentional lighting via contrast and surface boundaries, not floating color haze.
- **`gpt-thin-border-wide-shadow` (Hairline border with wide shadow)**: $1\text{px}$ hairline border paired simultaneously with a wide, diffuse elevation shadow. Pick one boundary mechanism: either an explicit border edge or soft shadow elevation.
- **`repeating-stripes-gradient` (Repeating-gradient stripes)**: `repeating-linear-gradient` or `repeating-radial-gradient` used as decorative card background texture. Use plain surfaces or purposeful vector textures.
- **`codex-grid-background` (Decorative grid-line background)**: Two-axis $1\text{px}$ hairline linear gradients tiled by a fixed pixel `background-size` cell. Reserve grid lines for CAD/canvas/graphs; use clean surfaces elsewhere.
- **`design-system-radius` (Radius outside DESIGN.md)**: Arbitrary `border-radius` values conflicting with the documented token scale. Restrict to defined radius tokens (e.g. `none`, `sm: 4px`, `md: 8px`, `lg: 16px`, `full`).

### 2. Typography & Hierarchy
- **`overused-font` (Overused font monoculture)**: Defaulting to *Inter, Roboto, Fraunces, Geist, Plus Jakarta Sans, Space Grotesk, Recoleta, Mona Sans, Montserrat*. Select distinctive typefaces matched to product tone or use clean system stacks.
- **`flat-type-hierarchy` (Flat type hierarchy)**: Heading and body scale ratio $< 1.25\times$ across steps, yielding indistinguishable hierarchy. Enforce modular type scales ($\ge 1.25\times$ major third or $1.333\times$ perfect fourth).
- **`italic-serif-display` (Italic serif display headline)**: Oversized italic serif (*Playfair, Fraunces, Recoleta, Newsreader*) at $\ge 48\text{px}$ on primary landing hero. Set display headers in roman or use purposeful editorial sans/serif display faces.
- **`hero-eyebrow-chip` (Hero eyebrow / pill chip)**: Tracked uppercase pill/chip label ($\le 14\text{px}$, tracking $\ge 1.6\text{px}$) sitting directly above an $h1 \ge 48\text{px}$. Fold kicker words directly into the headline or demote to breadcrumbs.
- **`kicker-above-heading` (Kicker / eyebrow label above heading)**: Tracked uppercase or small-caps label ($\le 14\text{px}$) sitting directly above $h1\text{–}h4$. Eliminate the kicker; let the section headline carry its own weight.
- **`numbered-section-labels` (Tiny numbered section labels)**: Small index markers (e.g. `01`, `02`) $\le 13\text{px}$ with mono/bold/tracked styling riding beside section headers. Let visual rhythm, whitespace, and copy progression structure the sequence.
- **`oversized-h1` (Oversized hero headline)**: Long full-sentence display headline taking up the entire above-the-fold viewport. Keep massive display text to 1–3 punchy words; tighten sentence headlines down to $32\text{–}48\text{px}$.
- **`extreme-negative-tracking` (Crushed letter spacing)**: Negative tracking ($< -0.04\text{em}$) crushing character silhouettes on display type. Optical tracking only; maintain glyph legibility and distinct apertures.
- **`tight-leading` (Tight line height)**: Body `line-height` $< 1.3\times$ font size on multi-line text blocks. Set body line height to $1.5\text{–}1.7\times$ font size.
- **`all-caps-body` (All-caps body text)**: Long passages of uppercase text in body copy or long descriptions. Reserve uppercase exclusively for short badges ($\le 3$ words); use sentence case for body.
- **`wide-tracking` (Wide letter spacing on body)**: Letter spacing $> 0.05\text{em}$ applied across multi-line lowercase body copy. Zero tracking for body copy; reserve wide tracking for micro uppercase labels.
- **`design-system-font` & `design-system-font-size`**: Typefaces or font sizes declared outside the project DESIGN.md typography scale.

### 3. Color & Contrast Invariants
- **`ai-color-palette` (AI violet / cyan palette)**: Saturated purple/violet (hex `#7c3aed`, `#8b5cf6`, `#6366f1` / hue $260^\circ\text{–}310^\circ$) or vivid cyan on dark backgrounds. Build authentic brand palettes derived from product domain and physical materials.
- **`cream-palette` (Default cream / beige palette)**: Defaulting to warm off-white/beige surfaces as a shortcut for "tasteful warmth". Deliberate neutral tones chosen for functional readability, not reflexive aesthetic trends.
- **`gradient-text` (Gradient-clipped text)**: `background-clip: text` combined with linear/radial gradients on headings or KPI metrics. Use solid text colors ensuring stable contrast across viewports and rendering engines.
- **`gray-on-color` (Gray text on colored background)**: Desaturated gray text (`text-slate-400`, neutral gray) rendered on chromatic colored cards. Use a darker/lighter tint of the parent hue, or clean near-white for contrast.
- **`design-system-color` (Undeclared literal color)**: Hardcoded raw hex/RGB strings bypassing the DESIGN.md tonal ramps. Enforce centralized semantic color tokens (`--color-surface`, `--color-ink`).

### 4. Layout & Container Hierarchy
- **`nested-cards` (Nested cards)**: Cards placed inside parent card containers, producing stacked borders and shadow depth. Flatten layout; separate groupings using whitespace, typography hierarchy, or subtle dividers.
- **`monotonous-spacing` (Monotonous spacing)**: Single spacing value (e.g. `16px` everywhere) representing $> 60\%$ of margin/padding/gap declarations. Use intentional rhythmic spacing: tight ($4\text{–}8\text{px}$) for related pairs, generous ($32\text{–}64\text{px}$) between sections.
- **`icon-tile-stack` (Icon tile stacked above heading)**: Squarish $32\text{–}128\text{px}$ container with border/bg stacked directly on top of an $h2\text{–}h4$ element. Align icon inline/side-by-side with heading, or place the icon directly in flow without a container box.
- **`cramped-padding` (Cramped container padding)**: Borders or colored containers with $< 8\text{px}$ internal padding around text content. Provide minimum $12\text{–}16\text{px}$ internal padding inside bordered or colored containers.
- **`heading-rhythm` (Heading crowded against previous block)**: Space above heading is less than or equal to space below it. Space above a heading must significantly exceed space below it ($2\times$ ratio).
- **`line-length` (Line length too wide)**: Text containers exceeding $\sim 80\text{–}85$ characters per line without max-width constraints. Constrain text reading columns to `max-w-prose` ($65\text{ch}\text{–}75\text{ch}$).

### 5. Imagery & Vector Assets
- **`shape-assembled-illustration` (Shape-assembled SVG clip-art)**: Inline SVG $\ge 200\text{px}$ assembling scenes from $\ge 8$ primitive rects/circles across $\ge 3$ fill colors. Use authentic photography, real custom illustrations, or high-fidelity renders.
- **`organic-clip-path` (Organic contour drawn via clip-path)**: `clip-path: polygon()` with $\ge 10$ off-grid vertices or `path()` with curved spline segments simulating torn paper/blobs. Use alpha-channel PNG/WebP/AVIF masks or restrict `clip-path` strictly to geometric cuts.
- **`buried-raster` (Raster buried under opaque wash)**: Background `url()` placed behind a gradient wash where all color stops have $\text{alpha} \ge 0.9$. Ensure photographic materials survive to the screen ($< 0.7$ tint) or eliminate the image asset.

