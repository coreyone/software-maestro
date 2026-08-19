---
name: create-design-art-direction
description: Create polished, coherent digital design systems and art direction from a brief by asking adaptive, high-information clarifying questions, selecting compatible levers, and comparing, rejecting, and revising candidate directions from the bundled DESIGN.md and ART-DIRECTION.MD encyclopedias. Use for new websites, product interfaces, campaign pages, editorial experiences, immersive sites, generative concepts, design-system directions, or requests to make a design more distinctive, premium, cinematic, experimental, or award-caliber.
---

# Create Design & Art Direction

Turn a product or creative brief into a constrained visual system with a clear art-directed point of view. Treat the bundled encyclopedias as the canonical option set; do not inflate them with synonyms or generic style adjectives.

## Read the encyclopedias

Before selecting anything, read:

- [DESIGN.md](references/DESIGN.md) for color, typography, type behavior, layout, depth, shape, and system-archetype levers.
- [ART-DIRECTION.MD](references/ART-DIRECTION.MD) for lens, scene, narrative, motion, interaction, composition, and signature-move levers.
- [QUESTION-MATRIX.md](references/QUESTION-MATRIX.md) for the adaptive clarification flow and question-to-lever mappings.

Use the IDs from those files (`C1`, `T2`, `SYS6`, `A3`, `X5`, etc.) in the working decision so another agent can reproduce or vary the direction.

## Clarification gate

Ask clarifying questions by default when the user has not provided explicit lever IDs, an existing design system, or enough concrete references to resolve the high-impact choices. Do not silently assume an aesthetic direction merely because the brief is incomplete.

Skip questions when the user says to decide independently, asks for a first-pass concept, or supplies a sufficiently complete direction. State any defaults used.

Use two rounds by default:

1. Ask up to three high-information questions that resolve several axes at once.
2. Build a decision ledger and ask only about unresolved or conflicting high-impact axes.

Ask no more than three questions in one message. Do not ask one question for every option. Stop when every relevant axis is explicit, confidently inferred, or safely defaulted.

Track each axis as:

- `explicit`: directly chosen by the user
- `inferred`: mapped from the user's language or references
- `defaulted`: selected because the axis is low-impact or unspecified
- `unresolved`: ambiguous or in conflict; ask a follow-up

When asking, describe the meaningful choice first and show the relevant IDs second. Prefer questions about purpose, behavior, and feeling over unexplained taxonomy labels.

## Workflow

### 1. Extract and clarify the brief

Identify the subject, audience, desired action, content density, platform, accessibility needs, technical constraints, and what must feel memorable. Use [QUESTION-MATRIX.md](references/QUESTION-MATRIX.md) to ask the smallest useful question set. Preserve the user's answers as a decision ledger with the selected ID, basis, and confidence.

### 2. Select the design system

Choose one option from each relevant design axis:

- `SYS`: system archetype
- `L`: layout
- `C`: color logic
- `T`: typography voice
- `TB`: type behavior
- `E`: elevation/depth
- `SH`: shape language

Use the selected options to define semantic tokens, hierarchy, spacing rhythm, component vocabulary, and responsive behavior. When creating a `DESIGN.md`, keep YAML frontmatter valid and preserve the required section order from the DESIGN.md specification: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.

### 3. Select the art direction

Choose one option from each relevant art-direction axis:

- `A`: lens
- `S`: scene model
- `N`: narrative move
- `M`: motion grammar
- `I`: interaction contract
- `G`: composition grammar
- `X`: signature move

Omit an axis only when the content genuinely does not need it. The art direction must explain the subject; it is not a request for decorative effects.

### 4. Resolve conflicts

- Keep one dominant hierarchy, one primary action, and one signature gesture.
- Keep two font families or fewer and one corner language.
- Cap simultaneous intensity: normally choose only one of `A1/A3`, one of `M3/M4`, and one of `G3/X1/X2`.
- Use reactive or generative behavior only when the input has meaning.
- Make the first viewport prove the concept; do not hide the idea behind an intro animation.
- Define a static/reduced-motion fallback, keyboard path, contrast behavior, loading state, and recovery/exit state for interactive work.

## Taste layer

Use taste as selection under constraints, not as maximal novelty. The goal is a direction whose choices reinforce the subject, audience, and behavior.

### Choose

1. Anchor the direction with `SYS`, `L`, and `A`: what the artifact is, how attention is organized, and what medium carries the idea.
2. Derive `S`, `N`, `G`, and `I` from the content's world, change, framing, and required agency; choose `C`, `T`, `TB`, `E`, `SH`, and `M` to support tone and production conditions.
3. Generate up to three candidates by changing one lever at a time. Keep the brief, content structure, and technical budget constant.
4. Keep a lever only when it earns a job: meaning, hierarchy, behavior, orientation, or material character.

### Compare

Compare candidates pairwise, never only in isolation. For each candidate, mark `pass`, `concern`, or `fail` against:

- **Fit** — does the form explain the subject and serve the audience?
- **Hierarchy** — is the first read and primary action unmistakable?
- **Coherence** — do the selected levers reinforce one another?
- **Distinctiveness** — is there one memorable mechanism rather than a pile of effects?
- **Restraint** — can anything be removed without reducing meaning or clarity?
- **Craft** — does it survive type, contrast, responsive, state, performance, and accessibility checks?

Select the winner by strongest fit and coherence, not by the highest spectacle. Record the runner-up and the decisive reason when more than one candidate is viable.

### Reject

Reject a candidate when:

- an effect is decorative, unearned, or disconnected from the content;
- it creates multiple competing focal points or primary actions;
- the signature does not change meaning, behavior, or understanding;
- typography needs motion or image treatment to remain interesting or legible;
- the art direction fights the system archetype, content density, or interaction contract;
- it fails static, reduced-motion, keyboard, contrast, loading, recovery, or performance requirements;
- it depends on unavailable assets, unexplained AI randomness, or award-fashion language.

Do not rescue a weak candidate by adding effects. Remove the weakest lever or replace the highest-conflict lever.

### Revise

When a candidate is close but not ready, revise in this order:

1. Remove secondary spectacle and restore one dominant hierarchy.
2. Repair the mapping between content, action, and visual emphasis.
3. Repair typography, spacing, contrast, responsive behavior, and states.
4. Replace one conflicting lever; do not change several axes at once.
5. Re-run the six comparisons and stop after the direction passes without a new unresolved conflict.

For internal reasoning, preserve a compact record: `candidate`, selected IDs, one-sentence mechanism, `keep/revise/reject`, strongest evidence, and next change. Expose the record when it helps the user choose; otherwise return the winning direction and the material tradeoff.

### 5. Produce the requested output

If the user asks for direction, return:

1. A one-sentence north star.
2. The decision ledger: selected lever IDs, names, basis, and confidence.
3. The visual rules: palette, type hierarchy, layout, depth, shape, components, medium, motion, and interaction.
4. The signature gesture with trigger, payoff, and fallback.
5. A compact implementation brief with responsive and accessibility constraints.

If the user asks for files, create a spec-compliant `DESIGN.md` and an `ART-DIRECTION.MD` that preserve the selected IDs and rationale. If the user asks for an implementation, translate the same decisions into the existing project’s components and tokens rather than introducing a parallel design language.

## Quality gate

Before handing off, check that:

- Every major visual decision maps to a selected lever or a concrete content need.
- No high-impact axis remains `unresolved` without the user's explicit acceptance.
- The direction remains recognizable in a static screenshot.
- The signature can be described in one sentence and changes the meaning or behavior of the work.
- Type remains legible without animation and interaction is not required to understand the primary message.
- Components, states, empty states, errors, mobile layouts, reduced motion, and keyboard use follow the same system.
- No option was added merely because it sounds fashionable, premium, futuristic, or award-winning.

Use the [ART-DIRECTION.MD compact prompt form](references/ART-DIRECTION.MD) when a downstream generative tool needs a single prompt. Treat the result as an award-calibrated design hypothesis, never as a guarantee of recognition.
