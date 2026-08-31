---
name: technical-language-rules
description: "Trigger: technical-language-rules, simplified technical english, ASD-STE100, google devdocs style, technical prose, deterministic docs, commit style, unambiguous connectors. Scope: Technical Language & Documentation Standard based on ASD-STE100 and Google Developer Style Guide. Enforces <=20 words procedural, <=25 words descriptive, <=3 noun stacks, and imperative commits. Boundary: Excludes persuasive marketing copywriting (use conversion-copywriting)."
---

# Rule: Technical Language & Documentation Standard (ASD-STE100 + Google DevDocs)

## When to use
Use when authoring documentation, PR summaries, code comments, architecture decision records, or commit messages.

## Non-Negotiable Rules
1. **Sentence Length**: $\le 20$ words for procedural/instructions; $\le 25$ words for descriptive text.
2. **Noun Stacks**: Maximum 3 consecutive nouns.
3. **Unambiguous Connectors**: Use `because` (not `since`/`as`), `after` (not `once`), `can`/`must` (not `may`).
4. **Imperative Commits**: Conventional commits with imperative verbs (`feat: add auth token refresh`).
