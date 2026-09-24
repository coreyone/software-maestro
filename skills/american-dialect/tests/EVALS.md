# Evaluation cases

These evals test whether the skill stays research-backed instead of becoming a stereotype generator.

## 1. Broad Midwest lexical rewrite

Input:
> `/american-dialect -midwest`
> Pick up some soda before you come over.

Expected:
- may change `soda` → `pop`
- should otherwise remain close to source
- should not add `ope`, `you betcha`, farm imagery, or comic spelling

Failure:
> Ope, you betcha, grab some pop there, dontcha know...

## 2. Upper Midwest grammar

Input:
> `/american-dialect --region upper-midwest --intensity medium`
> Do you want to come along?

Expected candidate:
> Do you want to come with?

Evidence:
- Spartz 2008 / Upper Midwest `come with`

## 3. Do not leak Midland grammar into Minnesota

Input:
> `/american-dialect --region upper-midwest --intensity strong`
> The car needs to be washed.

Expected:
- preserve standard construction unless other evidence applies

Failure:
> The car needs washed.

Reason:
- `needs washed` is Midland and is strongly rejected in much of the Upper Midwest.

## 4. Midland grammar

Input:
> `/american-dialect --region midland --intensity medium`
> The car needs to be washed.

Allowed:
> The car needs washed.

But the agent should not force this construction in every sentence.

## 5. Positive anymore semantic guard

Input:
> `/american-dialect --region midland --intensity strong`
> I don't go there anymore.

Expected:
- do not transform simply because `anymore` appears; this is ordinary negative-polarity `anymore`

Input:
> These days, parking is expensive.

Possible:
> Parking is expensive anymore.

Only at appropriate intensity and context.

## 6. Phonology guard

Input:
> `/american-dialect --region great-lakes`
> I can't believe that happened.

Expected:
- conventional spelling

Failure:
- eye-dialect spellings created from Northern Cities Shift descriptions

## 7. Semantic protection

Input:
> `/american-dialect -midwest`
> The product is legally classified as a “soft drink.”

Expected:
- preserve quoted/legal classification
- do not rewrite the protected term to `pop`

## 8. Evidence ledger

Input:
> `/american-dialect --region upper-midwest --show-evidence`
> Do you want to come along? Grab some soda.

Expected output includes only edits actually made, e.g.:
- `come with` — Spartz 2008
- `pop` — HDS q105

No hidden reasoning.

## 9. Sparse evidence

Input:
> `/american-dialect --region midwest --intensity strong`
> Refactor the payment service to make retries idempotent.

Expected:
- likely no dialect change
- technical prose has no natural opportunity for the supported variables

Failure:
- injecting slang merely to make the dialect visible

## 10. State specificity

Input:
> `/american-dialect --region wisconsin --intensity medium`

Expected:
- prefer state-specific HDS data if available
- do not treat all Wisconsin speech as Minnesota speech
- do not assume every Wisconsin speaker says `bubbler` without local evidence
