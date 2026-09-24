# american-dialect

A research-only Agent Skill for writing or rewriting American English with documented regional dialect features.

The core idea is simple: **dialect features require evidence**. The skill uses the Harvard Dialect Survey for lexical/elicited variables, modern dialectology for region boundaries and phonology, and peer-reviewed grammatical-dialect research for constructions that the HDS alone cannot justify.

## Why this is intentionally conservative

The Harvard Dialect Survey was a large online survey of regional pronunciation, vocabulary, and grammar. It did **not** measure a single holistic “Midwestern writing style,” personality, politeness pattern, or cadence. A faithful skill therefore changes only features that the research actually measured.

That means `/american-dialect -midwest` should usually be subtle.

## Install

Copy the `american-dialect/` directory into the skills directory used by your Agent Skills-compatible client.

The Agent Skills specification requires `SKILL.md`; all other files here are supporting resources.

Validate the package with the official reference implementation when available:

```bash
skills-ref validate ./american-dialect
```

## Usage

```text
/american-dialect -midwest
/american-dialect --region midwest --intensity subtle
/american-dialect --region upper-midwest --intensity medium
/american-dialect --region midland --intensity strong
/american-dialect --region great-lakes --spoken
/american-dialect --region kansas --show-evidence
```

Then provide text to rewrite, or ask the agent to compose text.

Example:

```text
/american-dialect --region upper-midwest --intensity medium

Rewrite:
Do you want to come along? We can pick up some soda on the way.
```

A research-backed result may use `come with` and a supported beverage term. It should **not** add `ope`, `you betcha`, phonetic spellings, or “Midwest nice” behavior.

## Data-driven HDS profiles

For higher fidelity, build a profile from a local machine-readable copy of the original 122-question Harvard Dialect Survey data.

```bash
python scripts/build_profile.py ./dialect-data-survey.js --region midwest
```

The script:

1. extracts the HDS question metadata and state percentages,
2. filters to HDS question IDs 1–122,
3. aggregates the selected state proxy,
4. ranks answers by regional share, national share, lift, and margin,
5. emits only evidence records—not prose stereotypes.

Use a different source file if you have a better academic/HDS export. The builder is intentionally separate from the skill so the research data can retain its original license.

## Important limitation

State-level aggregation is a **proxy**, not a dialect boundary. Illinois, Ohio, Wisconsin, and other states contain more than one dialect zone. `references/REGIONS.md` explains how the skill handles this.

## Package

```text
american-dialect/
├── SKILL.md
├── README.md
├── LICENSE.md
├── references/
│   ├── APPLICATION_RULES.md
│   ├── REGIONS.md
│   ├── RESEARCH_POLICY.md
│   └── SOURCES.md
├── assets/
│   ├── feature-schema.json
│   ├── region-proxies.json
│   └── profiles/
│       └── midwest-core.json
├── scripts/
│   ├── audit_profile.py
│   └── build_profile.py
└── tests/
    └── EVALS.md
```
