# Region model

## Why `midwest` is an alias, not a dialect

Modern dialectology does not support one uniform “Midwestern dialect.”

Labov, Ash, and Boberg's *Atlas of North American English* identifies major phonological regions including the Inland North and Midland; Upper Midwestern / North-Central English is also treated as a distinct or residual regional variety in later research. Grieve's corpus work on written American English identifies a broader Midwest region statistically, but that does not erase subregional variation.

For writing, the safest interpretation is:

- **midwest** = broad, conservative macro-profile
- **upper-midwest / north-central** = Upper Midwest evidence
- **great-lakes / inland-north** = Great Lakes / Northern Cities evidence
- **midland** = Midland evidence

## User-facing aliases

### `midwest`

Use only features that are well-supported across a substantial part of the broad Midwest.

Do not use strong subregional grammar unless the user selects a subregion or state.

A state-level data proxy may use:

`IL IN IA KS MI MN MO NE ND OH SD WI`

This 12-state set is a computational convenience for aggregating HDS state-level data, not a claim that all twelve states form one linguistic region.

### `upper-midwest` / `north-central`

Use for North-Central / Upper Midwestern features.

Strongest academic anchors include Minnesota and nearby Upper Midwestern speech communities. Wisconsin contains important internal variation and overlaps with Inland North patterns, so do not treat all Wisconsin speech as identical to Minnesota speech.

Useful research-backed grammar:
- particle-like `come with` in informal accompaniment contexts

Avoid importing Midland grammar automatically.

### `great-lakes` / `inland-north`

Use for the Great Lakes / Inland North area associated with the Northern Cities Shift.

Important: the most distinctive Inland North evidence is phonological. Do not convert vowel-shift research into comic spelling.

In ordinary written prose, the Great Lakes profile should rely more on HDS lexical evidence than pronunciation.

### `midland`

Use for the Midland zone extending across parts of the central United States.

Research-backed grammatical candidates include:
- positive `anymore`
- `need + passive participle` (`The car needs washed`)
- `want/need + directional preposition` (`The cat wants in`)

These constructions are not equally frequent everywhere. `needs washed`, for example, is strongly associated with core Midland areas and is rejected in much of the Upper Midwest.

## State requests

If the user specifies a state, prefer state-specific HDS distributions over a broad regional alias.

However, state borders are not dialect borders. If a state contains multiple linguistic regions:

- use high-confidence state-wide lexical tendencies,
- avoid phonological overprecision,
- avoid strong grammatical features unless research places them in that part of the state.

## City requests

A city is better than a state when research provides city-level evidence.

Examples:
- Chicago → Inland North / Great Lakes phonology is relevant
- Kansas City → western Midland context; positive `anymore` is documented but less frequent than in some eastern Midland cities
- Minneapolis / Minnesota → Upper Midwest `come with` evidence is relevant

Do not generalize one city to the entire Midwest.
