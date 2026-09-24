# Applying research to writing

## Goal

Shift only those parts of a text that correspond to documented regional variables.

The output should read like normal contemporary American English. If the reader can spot a “dialect performance” in every sentence, the skill is probably over-applying features.

## Feature types

### Lexical

Best fit for ordinary writing.

Pattern:

`concept → supported regional variant`

Examples of concepts measured in HDS include:

- generic sweetened carbonated beverage
- plural second-person address
- athletic footwear
- long cold-cut sandwich
- water fountain / drinking fountain
- garage / yard / rummage sale
- bag / sack
- frosting / icing
- highway / freeway / expressway
- many other everyday lexical alternations

Use the machine-generated HDS profile when possible.

### Grammatical

Apply only from explicit grammar sources.

Do not derive grammar from lexical maps.

#### Upper Midwest `come with`

Meaning: accompany someone, with `with` functioning particle-like.

Eligible:
- `Do you want to come along?` → `Do you want to come with?`
- `Are you going with us?` can remain unchanged; do not force deletion when not natural.

Ineligible:
- arbitrary deletion of objects after every `with`
- formal/legal prose unless the source already uses regional informal grammar

#### Midland positive `anymore`

Meaning approximately “nowadays / these days” in affirmative contexts.

Use sparingly, especially because production frequency varies within the Midland.

Eligible only if the sentence naturally expresses a current-vs-past temporal contrast.

Do not mechanically replace every `nowadays`.

#### Midland `needs washed`

Structure:
`need + passive participle`

Examples:
- `The car needs to be washed.` → `The car needs washed.`
- `The files need to be reviewed.` → `The files need reviewed.`

Use only for appropriate Midland profiles. Do not use as an Upper Midwest marker.

#### Midland `wants in`

Structure:
`want/need + directional preposition`

Examples:
- `The cat wants to come in.` → `The cat wants in.`
- `The kids need to get off the bus.` → `The kids need off the bus.`

Use conservatively; `want` is the safest documented verb family.

## Phonology

Phonological research supports how speech sounds, not how words should be misspelled.

If the user wants a screenplay, voice guide, or TTS prompt:

- describe the relevant sound pattern in a side note;
- use IPA only when it improves precision;
- keep the actual written dialogue conventionally spelled unless the user explicitly requests phonetic transcription.

Never use eye dialect simply to signal region.

## Probability and confidence

A regional feature is a tendency.

If a generated HDS profile provides:

- `regional_share`
- `national_share`
- `lift`
- `margin`

interpret them as:

- `regional_share`: mean share for the selected state proxy
- `national_share`: mean share across all available states/DC
- `lift`: regional minus national share
- `margin`: lead over the second most common answer within the target region

These are descriptive aggregates, not individual-level probabilities.

## Suggested implementation thresholds

These are **engineering defaults**, not academic findings:

- use automatically when regional share ≥ 0.50 and margin ≥ 0.10
- consider at medium/strong intensity when regional share ≥ 0.35 and lift ≥ 0.10
- otherwise keep original wording

A user-provided exact state/city profile can override these defaults.

## Rewrite precedence

When rules conflict:

1. preserve meaning
2. preserve quoted/protected text
3. honor state/city evidence
4. honor subregion evidence
5. honor broad-region evidence
6. preserve user's original wording

## Density

Do not make every eligible replacement.

A natural regional text still contains mostly nationally common English.

Use conspicuous features sparingly:
- one strong grammatical marker can be enough for a short message
- do not place `pop`, `come with`, and positive `anymore` in one sentence just to prove the dialect
