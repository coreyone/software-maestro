# Evidence Rubric

Use this reference to make “Proven” falsifiable and to keep market research proportional to the product decision.

## Source hierarchy

Prefer sources in this order, while triangulating across types:

1. **Direct product evidence:** official product flows, pricing/packaging, documentation, changelogs, app-store listings, public demos, and observable behavior.
2. **Direct customer evidence:** reviews with context, public support threads, interviews, research studies, community discussions, and repeated complaints or workarounds.
3. **Business/outcome evidence:** public filings, credible usage or revenue signals, retention or conversion disclosures, marketplace liquidity, adoption, and repeat purchase behavior.
4. **Independent analysis:** reputable industry research, comparative reviews, analyst reports, and technical or product journalism.
5. **Weak signals:** search snippets, unsourced listicles, anonymous assertions, stale pages, vanity popularity, funding alone, or a single competitor’s feature.

Use weak signals to generate queries, never as the sole basis for a Proven decision. Record the source date when the claim can drift.

## Minimum evidence patterns

Use judgment rather than a mechanical score, but apply these defaults:

| Classification | Minimum defensible pattern |
| --- | --- |
| Proven interaction or capability | At least 3 credible successful products converge, plus a plausible job explanation; upgrade confidence with direct customer or outcome evidence |
| Proven business mechanic | Repeated use across successful products plus evidence of willingness to pay, retention, acquisition, liquidity, or another relevant business outcome |
| Better opportunity | Repeated customer friction, exclusion, cost, or trust failure in an otherwise validated baseline |
| New hypothesis | One meaningful differentiation with an explicit causal hypothesis and an isolated test |

“Three products” is a research floor, not proof by itself. A pattern can remain unproven when the products share a vendor, legacy constraint, or copied convention and customer value is absent.

## Research query patterns

Adapt queries to the job and category:

- `[category] leading products pricing`
- `[product] reviews [job or workflow]`
- `[product] alternatives why switch`
- `site:reddit.com [category] [pain or workaround]`
- `[product] customer story [outcome]`
- `[category] retention acquisition marketplace business model`
- `[feature] adoption usability complaint [category]`
- `[product] changelog [pattern]`

Search by job and obstacle, not only by competitor name. Verify important claims on the underlying source rather than citing a search result page.

## Evidence ledger guidance

For each material claim, write one row:

```text
Claim:
Source(s):
Source type:
Observed evidence:
Customer/job explanation:
Desired outcome:
Confidence: High | Medium | Low | Unknown
Counterevidence or limitation:
Decision: Proven | Better | New | Unproven
```

Keep observation separate from interpretation. Example:

```text
Observed: Four category leaders offer saved views.
Interpretation: Returning users likely need continuity across recurring work.
Evidence gap: No direct retention or usage evidence is public.
Decision: Proven pattern, medium confidence; reuse the behavior, test the retention effect.
```

## Conflict handling

When competitors converge but customer evidence is negative:

1. Preserve the underlying job, not necessarily the interface.
2. Identify whether the pattern is mandatory, legacy, or a local optimization.
3. Treat the customer pain as a Better opportunity.
4. Test a simpler or alternative mechanism before copying the full implementation.

When customers value a behavior but competitors do not converge:

1. Treat it as a potentially underserved opportunity, not automatically New.
2. Verify willingness to switch or pay and the operational constraints.
3. Keep the proposed solution narrow until outcome evidence accumulates.

When success evidence is unclear:

1. Say what is observed.
2. Say what is inferred.
3. Name the smallest experiment or source needed to resolve the uncertainty.

## Citation rules

- Put a direct URL beside every material market or customer claim.
- Prefer the source that supports the exact claim, not a general homepage.
- Distinguish a product’s stated promise from independently observed behavior.
- Do not cite a source as proof of success when it only proves the feature exists.
- Note access date for pricing, policy, product availability, or other fast-changing claims.
- Never reproduce protected copy, code, screenshots, or private customer information as a deliverable.
