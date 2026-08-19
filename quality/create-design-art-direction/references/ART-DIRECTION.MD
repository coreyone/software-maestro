# ART-DIRECTION.MD: Compact Lever Encyclopedia

Art direction controls what the work feels like as an authored visual experience: medium, scene, narrative, motion, interaction, composition, and signature. Use it with `DESIGN.md`; do not duplicate its palette, typography, layout, or component rules.

Evidence basis: 14,340 strict winner records from 2022–2025. The strongest inferred art-direction signals were immersive/spatial (6,859), interaction-led (3,854), generative/AI (3,015), film/cinematic (2,269), motion/animation-led (2,117), socially participatory (1,467), 3D/CGI-led (811), illustration-led (616), and photography-led (427). Counts are multi-label tag occurrences, not a ranking of artistic quality.

## Lens

Choose one primary medium or visual logic. It defines the evidence the viewer trusts.

| ID | Lens | Direction |
|---|---|---|
| A1 | **Spatial / 3D** | Build a world with scale, camera, material, light, and navigable depth. |
| A2 | **Cinematic / film** | Direct the viewer through framing, shot rhythm, reveal, atmosphere, and sound-like pacing. |
| A3 | **Generative / reactive** | Make a rule visible: data, time, input, randomness, or AI produces the variation. |
| A4 | **Photographic / documentary** | Use observed people, places, objects, and evidence; resist over-styling the proof. |
| A5 | **Illustrative / editorial** | Use authored marks, metaphor, collage, and visual argument rather than literal capture. |
| A6 | **Data / diagrammatic** | Turn a model, relation, or measurement into the visual subject. |
| A7 | **Participatory / social** | Treat contributions, voices, traces, or collective behavior as the material. |

## Scene Model

Choose the world the viewer enters.

| ID | Scene | Direction |
|---|---|---|
| S1 | **Stage** | One controlled hero; everything supports a reveal or performance. |
| S2 | **World** | A navigable environment with spatial continuity and optional discovery. |
| S3 | **Archive** | A collection of objects, fragments, references, or time layers. |
| S4 | **Instrument** | A system the viewer reads, adjusts, filters, scrubs, or operates. |
| S5 | **Commons** | A shared surface where people contribute, annotate, remix, or witness one another. |

## Narrative Move

Choose the main change over time.

| ID | Move | Direction |
|---|---|---|
| N1 | **Reveal** | Withhold the important thing, then make the reveal feel earned. |
| N2 | **Wander** | Let discovery replace a single prescribed sequence; orient without over-explaining. |
| N3 | **Transform** | Make an object, image, material, or idea visibly change state. |
| N4 | **Compare** | Put two states, viewpoints, scales, or truths into productive tension. |
| N5 | **Contribute** | The viewer adds something that changes the artifact or the collective view. |

## Motion Grammar

Choose one motion regime. Motion should be legible as a behavior, not wallpaper.

| ID | Motion | Direction |
|---|---|---|
| M1 | **Still** | Let composition, material, and typography carry the drama. |
| M2 | **Choreographed** | Use staged entrance, exit, sequencing, and camera-like transitions. |
| M3 | **Continuous** | Sustain a living atmosphere through looping ambient movement. |
| M4 | **Reactive** | Tie movement to scroll, pointer, gesture, sound, time, data, or state. |

## Interaction Contract

Choose the viewer's agency.

| ID | Contract | Direction |
|---|---|---|
| I1 | **Observe** | The work reveals itself; interaction is optional and low-friction. |
| I2 | **Navigate** | The viewer chooses route, chapter, scene, object, or depth. |
| I3 | **Manipulate** | The viewer scrubs, drags, zooms, filters, compares, or tunes. |
| I4 | **Participate** | The viewer contributes, speaks, votes, annotates, remixes, or co-creates. |

## Composition Grammar

Choose how the visual material is framed.

| ID | Composition | Direction |
|---|---|---|
| G1 | **Hero** | One dominant image, object, or gesture; supporting content stays quiet. |
| G2 | **Sequence** | A chain of frames, chapters, or scenes; rhythm creates meaning. |
| G3 | **Collage** | Fragments, scales, textures, and voices collide in a controlled field. |
| G4 | **System** | Repeated units, rules, diagrams, or modules become the image. |

## Signature Move

Choose exactly one. This is the memorable idea, not a request for more effects.

| ID | Signature | Direction |
|---|---|---|
| X1 | **Spatial impossibility** | Break expected scale, gravity, camera, or continuity. |
| X2 | **Material mutation** | Let matter melt, assemble, fracture, grow, or change identity. |
| X3 | **Living rule** | Expose a generative system whose output changes with input, time, or data. |
| X4 | **Human trace** | Make testimony, annotation, contribution, or presence alter the artifact. |
| X5 | **Typographic event** | Make type become image, object, movement, navigation, or sound-like rhythm. |

## Art-Direction Protocol

- Select one value from `A`, `S`, `N`, `M`, `I`, `G`, and `X`; omit an axis only when the content genuinely does not need it.
- Keep the lens and signature different but complementary: `A1 Spatial / 3D` + `X1 Spatial impossibility` is coherent; add no second spectacle by default.
- Give the signature a trigger, a payoff, and a quiet fallback. If it has no consequence, remove it.
- Use `M4 Reactive` only when the input has meaning. Use `M3 Continuous` only when atmosphere is the point.
- Prefer `I1 Observe` or `I2 Navigate` for public-facing clarity; earn `I3 Manipulate` and `I4 Participate` with a clear reason.
- Make the first viewport prove the concept. Do not hide the art direction behind a long intro animation.
- Cap simultaneous intensity: one of `A1/A3`, one of `M3/M4`, and one of `G3/X1/X2` is enough for a first pass.
- Preserve legibility, reduced-motion behavior, keyboard access, and a static interpretation of the idea.

## Compact Prompt Form

Use this sentence to generate a controlled variant:

> Create a **[scene]** using **[lens]**, organized around **[narrative move]**, with **[motion]** motion and **[interaction]** agency. Compose it as **[composition]** and give it one signature gesture: **[signature]**. Keep the design system, typography, and color logic from `DESIGN.md`; make the signature explain the subject rather than decorate it.

Source: [DESIGN.md specification](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md) for the companion design-system format and [the award-winner CSV](../design-award-winners-2022-2025.csv) for the taxonomy evidence.
