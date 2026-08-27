---
name: proven-product-spec
description: Create size-scaled product specifications for features or products by researching successful competitors, challengers, adjacent products, customer behavior, business models, and convergent market patterns. Use when a user asks to ground a PRD, product strategy, UX, or design direction in what the market has already validated, especially through the Proven-Better-New philosophy.
---

# Proven Product Spec

## Purpose

Create a product spec that reuses validated market learning before spending innovation capital. Treat **Proven** as evidence from successful products and customer behavior—not merely familiar UX conventions or a competitor feature list.

Use the supplied product-strategy, PRD, design-direction, and aesthetic guidance as compatible lenses:

`market evidence → category baseline → strategic choice → product requirements → design direction → testable outcome`

The result must make the evidence boundary visible. Do not turn a plausible pattern into a fact, and do not present a competitor's existence as proof of customer value.

## Operating doctrine

> **Copy the commodity. Improve the friction. Invent the advantage.**

- **Proven:** Reuse patterns with convergent evidence and a credible reason they work.
- **Better:** Address a documented customer or business friction in the baseline.
- **New:** Make the smallest differentiated hypothesis that could earn preference or durable advantage.

Default to Proven. Earn Better. Ration New.

Do not recommend cloning protected code, content, brand identity, trade secrets, private data, or proprietary implementation. Reuse observable product patterns and outcomes while checking applicable legal and platform constraints.

## Clarification gate

Ask no more than three high-information questions when the brief cannot support responsible research. Resolve, in this order:

1. What job, customer, market, geography, and platform are in scope?
2. Is this a small feature, medium-sized feature/workflow, or large product/strategy effort?
3. What business outcome, constraint, launch horizon, or existing evidence should shape the work?

Proceed with explicit assumptions when the user wants momentum. Do not ask for details that internet research can establish. If the scope is ambiguous, choose a provisional size, state it, and keep the output easy to resize.

## Choose the output size

Use the smallest document that can carry the decision.

### Small: feature or focused workflow

Produce a concise spec containing:

- opportunity and target user/job;
- 3–5 researched comparators or adjacent examples;
- a compact Proven / Better / New baseline;
- one target behavior and success metric;
- user flow and key states;
- functional requirements and 3–6 Given / When / Then scenarios;
- non-goals, risks, open questions, and evidence links.

### Medium: multi-step feature or meaningful product area

Add:

- category map and comparator-selection rationale;
- evidence ledger with confidence and counterevidence;
- current alternatives and switching barriers;
- outcome-backed strategy sentence, obstacles, and 2–4 bets;
- pricing/packaging or acquisition implications when relevant;
- detailed requirements, edge cases, analytics, and design direction;
- staged validation and kill / scale / pivot rules.

### Large: full product, new category, or product strategy

Add:

- market and category landscape across direct, challenger, and adjacent products;
- customer behavior and business-model evidence;
- segment/ICP choice and deferred segments;
- category baseline with explicit table-stakes and differentiation boundaries;
- vision, challenge, target condition, obstacles, bets, tradeoffs, and roadmap sequencing;
- product architecture at the capability level, not speculative implementation detail;
- acquisition, retention, monetization, marketplace, and operational mechanics where applicable;
- design system/art direction derived from proven behavior and product meaning;
- evidence plan, research gaps, launch hypotheses, and decision gates.

Do not inflate a small request into a strategy document. Do not compress a new product into a feature checklist.

## Research workflow

### 1. Frame the job and desired outcome

Extract the target customer, job to be done, current alternative, desired behavior, business result, platform, geography, constraints, and evidence quality. Narrow broad audiences to one coherent primary segment; defer the rest.

Write a provisional strategy sentence in this form:

`We will help [customer] achieve [target behavior/outcome] by solving [obstacle/problem], because it moves [business result], and we will prove it through [evidence/metric/experiment].`

Do not invent a baseline. Mark it as needing measurement when absent.

### 2. Build a comparator portfolio

Research a purposeful mix rather than collecting feature lists:

- **Direct leaders:** closest successful products serving the same job.
- **Fast-growing challengers:** newer patterns gaining adoption or attention.
- **Adjacent products:** different categories solving the same behavior or anxiety.
- **Customer evidence:** reviews, support complaints, public communities, interviews, usage studies, and other observed behavior.
- **Business evidence:** pricing, packaging, distribution, acquisition loops, retention mechanics, marketplace dynamics, and public company/product signals.

For small work, use 3–5 comparators. For medium work, use 5–8. For large work, use a broader portfolio, but stop when new sources stop changing the baseline. Search the web before drafting claims; cite every material market assertion with a direct URL and access date where useful.

Prefer primary and directly observable sources: official product pages, pricing pages, documentation, product announcements, public filings, app stores, product walkthroughs, and customer-authored evidence. Use secondary analysis to triangulate, not to substitute for evidence. Label search snippets, anonymous claims, stale pages, and inferred success as weak or unverified.

### 3. Deconstruct outcomes, not just interfaces

For every meaningful pattern, record:

- what the product does;
- which customer job or obstacle it addresses;
- who uses or pays for it;
- what evidence suggests adoption, value, retention, trust, or revenue;
- whether the evidence is direct, triangulated, or inferred;
- counterevidence, limitations, and likely category-specific causes;
- what can be safely reused and what must be independently designed.

Separate these statements:

- `Competitor has it` = clue.
- `Several successful products converge on it` = market pattern.
- `Customers use/value it` = customer evidence.
- `It improves the desired outcome` = proven only when outcome evidence supports the link.

### 4. Establish the category baseline

Classify each candidate pattern:

| Class | Decision rule | Spec treatment |
| --- | --- | --- |
| Proven | Convergence plus credible success and/or customer behavior evidence | Reuse faithfully; avoid gratuitous differentiation |
| Better | Proven baseline has documented friction, exclusion, cost, or trust gap | Improve the friction; define the expected behavior change |
| New | A differentiated hypothesis could create meaningful preference or advantage | Keep narrow; isolate it and design an experiment |
| Unproven | Single-source, legacy, low-confidence, or unsupported pattern | Do not copy by default; investigate or omit |

For each baseline decision, include evidence, confidence, rationale, and any legal/platform boundary. Call out where the market converges for incompatible reasons or where no reliable proof exists.

### 5. Convert evidence into strategy

Use one primary obstacle and only the supporting obstacles that materially change the plan. Recommend 2–4 outcome-backed bets, not a roadmap of features. For each bet specify expected behavior change, why it follows from evidence, proof path, metric, and kill / scale / pivot rule.

Include explicit tradeoffs:

- customer segments and jobs not served yet;
- features, channels, or business models deferred;
- metrics not optimized;
- patterns intentionally not copied and why.

### 6. Convert strategy into requirements

Write requirements that preserve the proven baseline and isolate the novel bet. Include:

- user stories tied to the target behavior;
- functional requirements with unambiguous language;
- Given / When / Then acceptance scenarios;
- primary flow, alternate flow, loading, empty, error, permission, recovery, and exit states;
- analytics events tied to decisions, not vanity counts;
- technical constraints and dependencies only when they affect feasibility or risk;
- non-goals and open questions.

Do not prescribe a novel implementation merely because a competitor uses it. Specify the outcome, contract, and constraint; leave implementation choices to the engineering context unless the evidence requires a mechanism.

### 7. Derive design direction from proven behavior

Use established interaction patterns when they reduce learning cost. Make visual differentiation earn a job: hierarchy, trust, orientation, comprehension, or product meaning.

For interface work, state:

- information hierarchy and primary action;
- proven interaction conventions retained;
- friction intentionally improved;
- the single signature or novel gesture, if any;
- typography, contrast, responsive, keyboard, reduced-motion, and state requirements;
- static fallback and performance constraints.

Do not add decorative novelty to compensate for weak product differentiation. A design direction must remain understandable in a static screenshot and must not rely on motion to establish hierarchy.

## Evidence discipline

Read [references/evidence-rubric.md](references/evidence-rubric.md) when planning research, grading evidence, or resolving conflicts between competitor convergence and customer behavior.

Maintain an evidence ledger with these fields:

`claim | source | source type | observed evidence | desired outcome | confidence | counterevidence | decision`

Use confidence labels consistently:

- **High:** multiple independent strong sources plus direct customer or outcome evidence;
- **Medium:** repeated convergence and credible success evidence, but weak outcome proof;
- **Low:** one source, indirect signal, stale information, or inference;
- **Unknown:** no reliable evidence yet.

Never call a pattern Proven solely because it appears in a famous product, has become a UX convention, or is easy to implement. State when “success” is inferred from funding, visibility, longevity, or traffic rather than directly measured.

## Output format

Use this structure, adapting depth to the selected size:

```markdown
# [Product or Feature] — Proven Product Spec

## Executive Summary
## Scope and Evidence Boundary
## Strategy Sentence
## Customer, Job, and Target Outcome
## Market Research
### Comparator Portfolio
### Evidence Ledger
### Category Baseline: Proven / Better / New
## Strategic Choices
### Vision
### Challenge and Primary Obstacle
### Product Bets
### What We Will Not Do
## Product Requirements
### User Stories
### Primary Journey and Key States
### Functional Requirements
### Acceptance Criteria (Given / When / Then)
### Analytics and Success Metrics
### Technical Considerations
## Design Direction
## Risks, Legal / Platform Boundaries, and Open Questions
## Validation and Decision Gates
## Roadmap Implications
## Sources
```

For small work, combine or omit sections that do not change the decision. For large work, keep the headings and add appendices only when the evidence volume requires them.

## Quality gate

Before handing off, verify:

- the customer, job, desired behavior, and business outcome are specific;
- the web was researched and material claims have direct citations;
- direct, challenger, adjacent, customer, and business evidence are not conflated;
- each Proven item has a reason beyond “competitor has it”;
- Better and New are narrow, outcome-backed, and separated from table stakes;
- counterevidence and uncertainty are visible;
- the strategy has one primary obstacle, explicit tradeoffs, and decision rules;
- requirements are testable and include unhappy paths and key states;
- design guidance preserves clarity, accessibility, responsiveness, and reduced-motion behavior;
- the document is proportional to small, medium, or large scope;
- no protected implementation, content, branding, or private data is recommended for copying.

If the evidence cannot support a Proven classification, label the item `Unproven` and propose the smallest research or experiment needed to resolve it.
