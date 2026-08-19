# Clarification Question Matrix

Use this matrix to navigate the 62 canonical options without turning the process into a 62-item questionnaire. Ask questions in order of information gain, record provisional mappings, and ask follow-ups only where the answer remains ambiguous or creates a conflict.

Contents: [Decision ledger](#decision-ledger) · [First question round](#first-question-round) · [Second question round](#second-question-round) · [Stop and conflict rules](#stop-and-conflict-rules)

## Decision ledger

Record one row per relevant axis:

| Axis | Selected ID | Basis | Confidence |
|---|---|---|---|
| `SYS` | `SYS1` | User described a task-oriented interface | explicit / inferred / defaulted / unresolved |

Never hide a meaningful default. Show the ledger before generating files or implementation when questions were asked.

## First question round

Ask up to three questions. Prefer the wording on the left; use the IDs on the right to make the mapping auditable.

### Q1 — What is the artifact primarily for?

This selects `SYS` and usually constrains `S` and `I`.

| User-facing choice | Primary ID |
|---|---|
| A tool people operate | `SYS1` Product / UI |
| A story people read or progress through | `SYS2` Editorial / story |
| A flexible public-facing campaign | `SYS3` Campaign / brand |
| A collection, institution, or body of work | `SYS4` Cultural / archive |
| A task, service, or civic process | `SYS5` Service / civic |
| A world people enter and explore | `SYS6` Immersive / world |

Follow up if the user names two purposes with different component vocabularies.

### Q2 — How should the space organize attention?

This selects `L` and proposes `G` and `S`.

| User-facing choice | Primary ID | Provisional companions |
|---|---|---|
| Stable, precise, easy to scan | `L1` Rational grid | `G4` System, `S4` Instrument |
| Authored, asymmetric, editorial | `L2` Editorial offset | `G2` Sequence or `G3` Collage, `S3` Archive |
| Immersive, edge-to-edge, cinematic | `L3` Full-bleed field | `G1` Hero, `S1` Stage or `S2` World |
| Repeated, browsable, collection-like | `L4` Serial modules | `G4` System, `S3` Archive |
| Shared surface shaped by people | `S5` Commons | `G4` System, `I4` Participate |

Ask separately about `G` or `S` only when the provisional companion would materially change the experience.

### Q3 — What visual posture should it take?

This selects `C` and proposes `E` and `SH`.

| User-facing choice | Primary ID | Provisional companions |
|---|---|---|
| Quiet, warm, clear, editorial | `C1` Paper / ink / signal | `E1` Tonal or `E2` Constructed; `SH1` or `SH2` |
| Dark, luminous, high-contrast | `C2` Dark / electric | `E3` Layered or `E4` Volumetric; `SH1` or `SH2` |
| Playful, expressive, color-forward | `C3` Chromatic field | `E1` Tonal or `E3` Layered; `SH2` or `SH3` |
| Tactile, organic, grounded | `C4` Mineral / natural | `E1` Tonal or `E3` Layered; `SH2` or `SH3` |

Do not infer `E` or `SH` as final when the user has a strong opinion about physicality, corners, or material.

## Second question round

Ask only the questions needed after the first ledger is built.

### Q4 — What should typography do?

Select both a voice `T` and behavior `TB`.

| User-facing choice | Voice | Behavior |
|---|---|---|
| Trustworthy, literary, cultural | `T1` Editorial serif | `TB1` Reading |
| Direct, contemporary, product-clear | `T2` Neutral grotesk | `TB1` Reading or `TB2` Labeling |
| Instrumental, precise, system-like | `T3` Technical mono | `TB2` Labeling |
| Visually dominant, expressive, memorable | `T4` Expressive display | `TB3` Performing |

If the user chooses a voice but not a behavior, infer the least theatrical behavior compatible with the brief.

### Q5 — What is the primary visual medium?

Select one `A` lens:

| User-facing choice | ID |
|---|---|
| World, camera, material, depth | `A1` Spatial / 3D |
| Framing, atmosphere, shot rhythm | `A2` Cinematic / film |
| Visible rules driven by input, time, data, or AI | `A3` Generative / reactive |
| Observed people, places, objects, evidence | `A4` Photographic / documentary |
| Authored marks, metaphor, collage, visual argument | `A5` Illustrative / editorial |
| Models, relationships, or measurements | `A6` Data / diagrammatic |
| Contributions, voices, traces, collective behavior | `A7` Participatory / social |

### Q6 — How should the experience unfold?

Select one `N`, one `M`, and one `I` when the content needs them.

| User-facing choice | Narrative | Motion | Interaction |
|---|---|---|---|
| Reveal information in a controlled sequence | `N1` Reveal | `M2` Choreographed | `I1` Observe or `I2` Navigate |
| Let the viewer discover a non-linear world | `N2` Wander | `M3` Continuous or `M4` Reactive | `I2` Navigate |
| Show visible change or transformation | `N3` Transform | `M2` Choreographed or `M4` Reactive | `I3` Manipulate |
| Put states or viewpoints into tension | `N4` Compare | `M1` Still or `M2` Choreographed | `I3` Manipulate |
| Let the viewer change the artifact or collective view | `N5` Contribute | `M4` Reactive | `I4` Participate |

### Q7 — What single idea should people remember?

Select exactly one `X` signature move:

| User-facing choice | ID |
|---|---|
| Break expected scale, gravity, camera, or continuity | `X1` Spatial impossibility |
| Let matter melt, assemble, fracture, grow, or change identity | `X2` Material mutation |
| Expose a generative system changing with input, time, or data | `X3` Living rule |
| Make testimony, annotation, contribution, or presence alter the artifact | `X4` Human trace |
| Make type become image, object, movement, navigation, or rhythm | `X5` Typographic event |

If the signature cannot be described in one sentence with a trigger and payoff, ask for a sharper idea instead of adding more effects.

## Stop and conflict rules

- Stop after the first round if all high-impact choices are explicit or confidently inferred.
- Ask a follow-up when two selected axes compete, such as `SYS1` Product / UI with `I4` Participate, or `E4` Volumetric with `L1` Rational grid.
- Default `E` and `SH` only when the user has no meaningful preference; mark them `defaulted` in the ledger.
- Keep at most one of `A1/A3`, one of `M3/M4`, and one of `G3/X1/X2` in a first pass.
- If the user asks to decide independently, stop asking, choose coherent defaults, and expose every default in the ledger.
