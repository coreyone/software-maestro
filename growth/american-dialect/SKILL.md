---
name: american-dialect
description: "Rewrite or compose American English using research-backed regional dialect features. Trigger: American regional dialect, Midwest, Upper Midwest, Inland North, Great Lakes, Midland, /american-dialect. Scope: Research-backed regional lexical, grammatical, and phonological features. Boundary: Excludes stereotypes, invented slang, caricature spellings, and unsupported cadence."
license: See LICENSE.md
metadata:
  version: "0.1.0"
  evidence-policy: "research-only"
---

# American Dialect

Write American regional English from **documented linguistic evidence**, not stereotypes.

This skill is conservative by design. A regional dialect is a statistical pattern, not a costume. Preserve the user's meaning and voice; modify only features that have explicit research support for the requested region.

## Invocation

Treat these as equivalent:

- `/american-dialect --region midwest`
- `/american-dialect -midwest`
- “rewrite this in Midwestern American English”
- “make this sound like someone from the Upper Midwest”
- “use Midland American English”

Recognized controls:

- `--region`: `midwest`, `upper-midwest`, `great-lakes`, `midland`, or a U.S. state
- `--subregion`: `north-central`, `inland-north`, `midland`
- `--intensity`: `subtle` (default), `medium`, `strong`
- `--mode`: `rewrite` (default) or `compose`
- `--spoken`: allow pronunciation-aware dialogue notes; default is off
- `--show-evidence`: append the evidence ledger after the transformed text
- `--strict`: research-only mode; always on unless the user explicitly asks for creative/stereotyped dialect

The Agent Skills standard does not define slash-command parsing. The syntax above is a user-facing convention for activating this skill.

## Non-negotiable evidence rule

Before introducing any regional feature, it must satisfy **all** of these:

1. The feature exists in `references/SOURCES.md` or in a generated profile produced from the Harvard Dialect Survey.
2. The source actually supports the requested geographic region or subregion.
3. The feature is appropriate to the current semantic context.
4. The feature does not change factual meaning, social identity, education level, race, class, or personality.
5. The output does not imply that every speaker in the region uses the feature.

If a candidate fails any test, leave the text unchanged.

Never invent a feature because it “sounds Midwestern.”

## First decision: region

Read `references/REGIONS.md` whenever the request is `midwest`, `upper-midwest`, `great-lakes`, `inland-north`, `north-central`, or `midland`.

Important:

- **Midwest is not one linguistic dialect region.**
- `midwest` is a broad convenience label crossing multiple dialect zones.
- When only `midwest` is requested, use only broad features with strong evidence across a large portion of the region.
- Strong local grammar requires a narrower subregion.
- Never silently turn `midwest` into Minnesota/Fargo-style speech.

Default mapping:

- `midwest` → conservative broad profile
- `upper-midwest` / `north-central` → Minnesota–Dakotas–northern Wisconsin-oriented evidence
- `great-lakes` / `inland-north` → Great Lakes / Northern Cities evidence
- `midland` → central Ohio through the central Plains-oriented Midland evidence

State requests override broad aliases.

## Workflow

### 1. Preserve the source

For rewrites, first lock:

- factual claims
- names
- numbers
- quotations
- technical terms
- intent
- level of formality
- user-specific vocabulary that is not the target of a supported regional alternation

Do not “regionalize” protected content.

### 2. Load evidence

Always read `references/APPLICATION_RULES.md`.

Then load the smallest useful evidence set:

- broad Midwest: `assets/profiles/midwest-core.json`
- regional boundaries: `references/REGIONS.md`
- source provenance: `references/SOURCES.md`
- if a machine-generated HDS profile exists, prefer it over the small bundled starter profile

For a data-driven profile, run:

```bash
python scripts/build_profile.py /path/to/dialect-data-survey.js --region midwest
```

The builder accepts only the original Harvard Dialect Survey question IDs 1–122. It rejects modeled or extended questions.

### 3. Identify opportunities, not decorations

Scan the text for concepts represented by supported variables.

Examples:

- generic carbonated beverage → HDS question 105
- athletic footwear → HDS question 73
- plural second-person address → HDS question 50
- positive `anymore` contexts → Midland grammar research
- motion verb + particle `with` → Upper Midwest research
- `need` + passive participle → Midland grammar research

Do not insert a dialect marker where the concept was not already naturally relevant.

Bad:
> We should grab some pop and head over.

when the original text never mentioned drinks.

Better:
> Pick up some soda on the way.
→
> Pick up some pop on the way.

### 4. Apply intensity

Intensity controls **density of eligible changes**, never extremity or caricature.

- `subtle`: use only the most secure regional choices; normally 0–2 changes per 150 words
- `medium`: use supported regional choices when natural; normally 1–4 changes per 150 words
- `strong`: use most eligible supported features for the chosen **specific subregion**; never add unsupported spellings or stereotypes

For broad `midwest`, `strong` still remains conservative. If the requested feature set is too sparse, preserve standard wording rather than fabricate markers.

### 5. Handle lexical evidence

Lexical substitutions are preferred because the Harvard Dialect Survey directly measured many lexical alternations.

Rules:

- replace only semantic equivalents
- respect register
- do not replace proper nouns or quotations
- do not force a low-frequency answer merely because it is geographically distinctive
- if multiple variants are common in the target area, keep the user's original variant unless a profile shows a clear regional preference
- do not stack several conspicuous variants into one sentence

### 6. Handle grammar evidence

Grammar has a higher bar than vocabulary.

Use a grammar feature only when:

- it is documented in a cited academic source
- the requested subregion matches the documented distribution
- the context is natural
- the requested intensity is `medium` or `strong`, unless the user's source text already contains the construction

Specific guards:

- **Upper Midwest `come with`**: use only in informal contexts where `come/go ... with` means accompany. Do not generalize `with` deletion/particle behavior to arbitrary verbs.
- **Midland positive `anymore`**: use sparingly. It is low-frequency and varies substantially within the Midland.
- **Midland `needs washed`**: do not use for `upper-midwest`; research shows strong rejection in much of Minnesota/Wisconsin. Use only where the Midland profile supports it.

### 7. Handle pronunciation

Written dialect is not phonetic transcription.

Default: do **not** encode pronunciation through eye dialect.

Never manufacture spellings such as:

- `dontcha`
- `ya`
- `fer`
- `warsh`
- elongated vowels
- dropped final `g` as a regional marker

If `--spoken` is requested, consult the phonological sources in `references/SOURCES.md`. Describe pronunciation in performance notes or IPA only when useful; do not turn it into comic spelling.

### 8. Keep social variation separate

Geographic dialect research does not license claims about:

- friendliness
- politeness
- intelligence
- education
- politics
- race or ethnicity
- socioeconomic class
- rurality
- personality
- humor
- conversational directness

Do not add “Midwest nice,” folksiness, excessive apologies, small talk, or rural imagery unless the user separately asks for those traits.

### 9. Audit before returning

Run this internal checklist:

- [ ] Every introduced regional feature has a source ID.
- [ ] Each source supports the requested geography.
- [ ] No feature changes meaning.
- [ ] No unsupported slang or eye dialect was added.
- [ ] No stereotype stands in for linguistic evidence.
- [ ] Broad Midwest output does not overfit Minnesota, Chicago, or Kansas.
- [ ] The result still sounds like the original author, just regionally shifted.

If `--show-evidence` is on, append a compact ledger:

```text
Evidence:
- “pop” — HDS q105 — broad Midwest lexical tendency
- “come with” — Spartz 2008 — Upper Midwest grammar
```

Do not expose hidden chain-of-thought. The ledger lists only source-backed edits.

## Built-in starter evidence

The bundled starter profile is intentionally small. It contains only features with clear published support:

- broad Midwest: `pop` as a generic carbonated-beverage term
- Midwest / especially Great Lakes: `gym shoes` as a documented regional athletic-footwear term, used conservatively
- Upper Midwest: particle-like `come with`
- Midland: positive `anymore`
- Midland: `need + passive participle` (`needs washed`)
- Midland: `want/need + directional preposition` (`wants in`)

These are **candidates**, not mandatory replacements. Read `assets/profiles/midwest-core.json` for scope and guards.

## Research-only exclusions

Do not add the following merely because popular culture associates them with the Midwest:

- `ope`
- `uff da`
- `you betcha`
- `dontcha know`
- exaggerated `Fargo` vowel spellings
- random `ya`
- forced `supper`
- “Midwest nice” politeness
- farm, snow, church, casserole, or small-town references

A feature may be added later only with a source, geographic scope, usage constraints, and evidence entry.

## Failure mode

If the requested variety cannot be supported by the available research:

1. preserve the text,
2. make only supported changes,
3. state that the evidence set is insufficient for a stronger transformation.

Never fill evidence gaps with intuition.
