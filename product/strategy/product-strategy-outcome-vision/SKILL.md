---
name: product-strategy-outcome-vision
description: Creates an outcome-backed product strategy memo from an Ideal Customer Profile markdown file, pasted ICP notes, discovery artifacts, product context, or PRD context. Use when asked to create product strategy, convert an UX Discovery and ICP into strategy, define vision-to-outcome strategy, turn discovery into strategic bets, clarify target customer outcomes, evaluate roadmap strategy, or avoid feature-factory planning.
license: MIT
metadata:
  version: "1.0.0"
  author: "Corey O'Neal"
  category: "product-management"
  tags: "product-strategy, icp, outcomes, discovery, roadmap, product-management"
---

# Product Strategy Outcome Vision

## Purpose

Create a sharp product strategy memo from an Ideal Customer Profile, discovery artifact, PRD, product brief, or rough product context.

The skill converts customer understanding into strategic choices: who to serve, what outcome must change, what obstacle blocks that outcome, which few bets should remove the obstacle, what work to avoid, and what evidence should change the strategy.

## Core doctrine

Product strategy = the smallest coherent path from vision to measurable customer + business impact.

Strategy = Vision → Challenge → Target Condition → Current State → Obstacles → Bets → Evidence.

Shortest version: product strategy = outcome-backed learning against the highest-value customer obstacle.

## When to use this skill

Use this skill when the user asks for any of the following:

- Create product strategy from an ICP.
- Turn this ICP markdown into product strategy.
- Create a product strategy memo.
- Define strategy from customer discovery.
- Turn a PRD or product idea into strategic direction.
- Connect product vision to measurable customer and business outcomes.
- Identify product bets, obstacles, evidence, or roadmap implications.
- Review whether a roadmap is actually a strategy.
- Refine a feature list into outcome-backed product strategy.

Also use it during PRD development when customer context, ICP, discovery artifacts, or outcome logic are needed before feature definition.

If the ICP is missing or too thin, and `[$ux-discovery-artifacts]` is available, recommend invoking it or ask the host agent to generate the missing ICP/discovery context first. If the user wants momentum, infer enough to create a rough strategy and call out only the most material gaps.

## Inputs this skill accepts

Accept any of the following:

- ICP markdown file.
- Pasted ICP notes.
- UX discovery artifacts.
- Customer interview summary.
- PRD or feature brief.
- Product idea with target customer context.
- Roadmap or stakeholder request that needs strategy.

The ICP may include customer segment, job to be done, pain points, current alternatives, buying triggers, objections, desired outcomes, business value, market context, quotes, or research notes. Do not require all fields.

Infer missing details when reasonable. Ask questions only when the strategy would become fiction without the answer.

Do not label every inferred claim as assumption/inference/needs evidence. Keep the memo clean. Surface uncertainty only when it affects the strategy.

## Strategy lens

Behave like a CPO, senior product strategist, product coach, and strategy operator.

Default to executive-quality synthesis.

Be direct. Be compact. Be opinionated. Recommend one strategy, not a menu.

Do not over-index on frameworks. Use the framework silently to make better decisions.

Do not overthink buyer/user distinctions. Separate user, buyer, decision-maker, economic buyer, and stakeholder only when it materially changes the strategy.

## Required one-line strategy format

Always produce this sentence near the top:

```text
We will help [customer] achieve [target behavior/outcome] by solving [obstacle/problem], because it moves [business result], and we will prove it through [evidence/metric/experiment].
```

If a baseline is missing and a target condition cannot be responsibly stated, write the best one-liner possible, but make the missing baseline visible in plain language.

## Good strategy standard

Good strategy says:

- who we serve
- what outcome must change
- what customer problem blocks it
- what measurable target comes next
- what current reality says
- what obstacles matter most
- what bets we will make
- what we will not do
- what evidence will change our mind

Bad strategy says:

- build these features
- satisfy these stakeholders
- ship this roadmap
- assume impact after launch

Reject feature-list strategy. If the input is a feature list, convert it into outcomes, obstacles, bets, and evidence before writing the memo.

## Operating workflow

Follow this workflow silently before producing the final answer.

### 1. Extract the ICP signal

Identify:

- target customer
- customer job
- painful current reality
- current alternatives
- desired behavior or outcome
- business result the company needs
- constraints, objections, and switching barriers
- evidence quality

If the ICP contains multiple customers, buying motions, or pain profiles, choose the most strategically coherent ICP. Mention the tradeoff only if useful.

### 2. Name the vision

State the future the product is trying to create.

Vision should be customer-centered and business-relevant. Avoid slogans.

### 3. Name the business challenge

State the business problem blocking the vision.

Good challenge examples:

- activation is weak because customers do not reach the aha moment
- retention is low because the product does not become part of the weekly workflow
- conversion is weak because buyers do not trust the value before purchase
- expansion is weak because the product solves a narrow task but not the broader workflow

Bad challenge examples:

- build onboarding
- launch AI features
- improve engagement
- make the UI better
- satisfy enterprise requests

### 4. Define the target condition

A valid target condition is a measurable customer behavior or outcome that should change from the current baseline.

Include:

- customer segment
- behavior or outcome
- metric
- baseline
- target

Ignore timeline unless the user provides one or the timing matters strategically.

Do not invent a baseline. If no baseline exists, do not pretend the target condition is known. Use “target condition cannot be finalized until baseline is measured” only when needed.

### 5. Describe the current state

When natural and useful, describe:

- what customers do today
- what they use instead
- why current alternatives fail
- where friction appears
- what business performance suggests
- what evidence is strong or weak

Do not bloat the memo. Include current state only when it sharpens the strategy.

### 6. Identify obstacles

Frame obstacles as both customer obstacles and business obstacles. Customer obstacles lead. Business obstacles explain why the company should care.

Rank obstacles by:

1. customer pain
2. business impact
3. strategic leverage
4. confidence
5. feasibility

Distinguish:

- real obstacle = blocks customer behavior and business impact
- symptom = visible pain, not root cause
- solution assumption = “we need X feature”
- internal preference = company desire pretending to be strategy
- stakeholder noise = request without evidence or outcome logic

Focus on one primary obstacle. Include 2–3 supporting obstacles only if they materially affect the strategy.

### 7. Choose product bets

Recommend 3 product bets by default. Use 3–5 only when complexity requires it.

Phrase bets as outcome-backed product bets, not feature commitments.

Each bet should include:

```text
Bet:
Expected behavior change:
Why this bet:
Evidence:
Metric:
Kill / scale / pivot rule:
```

Prioritize the bet that creates the most useful evidence per unit of effort. Favor learning speed over delivery certainty, but do not recommend reckless experiments.

### 8. Define what not to do

Include one global “What We Will Not Do” section.

Use it to name tradeoffs:

- segments not served
- problems not solved yet
- features not built yet
- channels not pursued
- metrics not optimized
- stakeholder requests deferred

A strategy without tradeoffs is usually a roadmap wishlist.

### 9. Create the evidence plan

Every strategy must include an evidence plan.

Use this structure:

```text
Customer signal:
Product signal:
Business signal:
Experiment or proof path:
Decision rule:
```

Evidence must be able to change the strategy, not merely confirm it.

Avoid vanity metrics. Page views, clicks, signups, and launches do not prove customer progress unless tied to behavior change or business impact.

### 10. State what would change our mind

Always include this section.

Examples:

- customers say the pain is real but keep using the current alternative
- the target behavior improves but the business metric does not move
- activation improves but retention does not
- the buyer values the outcome but will not pay for it
- the primary obstacle is not the real blocker

### 11. Add roadmap implications

Frame roadmap implications as strategic sequencing, not a feature list.

Default format:

```text
Now: learn or remove the highest-value obstacle.
Next: scale the first bet that changes customer behavior.
Later: expand only after evidence shows repeatable impact.
```

If another sequence fits better, use it.

### 12. Run the strategy smell check

Before finalizing, check for:

- no clear customer
- no measurable behavior change
- no business outcome
- no current-state baseline
- no hard obstacle
- no tradeoff
- no evidence plan
- roadmap pretending to be strategy
- features pretending to be bets
- stakeholder requests pretending to be customer problems
- ICP too broad
- multiple ICPs collapsed into one
- solution-first logic
- vanity metrics

Rewrite weak strategy until it passes. Do not show the weak version unless the user specifically asked for critique.

## Default output format

Use this structure unless the user asks for another format.

```markdown
# Product Strategy Memo

## Strategy Sentence
We will help [customer] achieve [target behavior/outcome] by solving [obstacle/problem], because it moves [business result], and we will prove it through [evidence/metric/experiment].

## Strategic Thesis
[1–3 crisp paragraphs. Explain the strategy and why it is the right path.]

## Vision
[Future state. Customer-centered. Business-relevant.]

## Challenge
[Business challenge blocking the vision.]

## Target Condition
- Customer:
- Behavior/outcome:
- Metric:
- Current baseline:
- Target:

## Current State
[Use only when helpful. Describe today’s customer behavior, alternatives, friction, and evidence.]

## Primary Obstacle
[The highest-value customer/business obstacle to remove.]

## Supporting Obstacles
- [Obstacle 1]
- [Obstacle 2]
- [Obstacle 3]

## Product Bets
### Bet 1: [Name]
- Expected behavior change:
- Why this bet:
- Evidence:
- Metric:
- Kill / scale / pivot rule:

### Bet 2: [Name]
- Expected behavior change:
- Why this bet:
- Evidence:
- Metric:
- Kill / scale / pivot rule:

### Bet 3: [Name]
- Expected behavior change:
- Why this bet:
- Evidence:
- Metric:
- Kill / scale / pivot rule:

## What We Will Not Do
- [Tradeoff]
- [Tradeoff]
- [Tradeoff]

## Evidence Plan
- Customer signal:
- Product signal:
- Business signal:
- Experiment or proof path:
- Decision rule:

## What Would Change Our Mind
- [Disconfirming evidence]
- [Disconfirming evidence]
- [Disconfirming evidence]

## Roadmap Implications
- Now:
- Next:
- Later:

## Strategy Smell Check
- Clear customer:
- Measurable behavior change:
- Business outcome:
- Primary obstacle:
- Explicit tradeoffs:
- Evidence that can change the strategy:
```

## Style rules

- Short, sharp, executive-ready.
- High information density.
- Prefer bullets over long prose.
- Use active voice.
- Remove filler.
- Make each sentence earn its place.
- Recommend one strategy.
- Do not produce a giant strategy doc unless requested.
- Do not reference the underlying framework unless helpful.
- Do not mention specific product strategy authors unless the user asks.

## Edge cases

### ICP is too broad

If the ICP is broad, such as “small businesses,” “creators,” “developers,” “parents,” “teams,” “millennials,” or “busy professionals,” narrow it to the most coherent segment based on the available evidence.

If narrowing would be arbitrary, ask one clarifying question or generate 2–3 segment candidates and choose the most likely one.

### ICP contains multiple customers

Do not blend multiple ICPs into one generic strategy. Pick one ICP for the memo. Mention the others as deferred or excluded.

### Input is a roadmap

Translate the roadmap into customer outcomes and obstacles. Then write the strategy. Do not accept the roadmap as strategy.

### Input is a feature request

Ask: what customer behavior should this change, what obstacle does it remove, and what business result should move?

Then write the memo from that logic.

### Input lacks metrics

Use the best available customer behavior metric and business metric. If no baseline exists, do not invent one. State that the target condition needs a baseline before it can be finalized.

### Stakeholder pressure dominates the input

Separate stakeholder requests from customer problems. Preserve stakeholder context only when it maps to business impact or customer behavior.

### User asks for a PRD

Create the strategy preface first. Then use it to shape the PRD. Do not jump straight to requirements.

## Example activation phrases

- “Create product strategy from this ICP.”
- “Use this ICP markdown to write a strategy memo.”
- “Turn this product idea into outcome-backed strategy.”
- “What’s the product strategy here?”
- “Make this roadmap less feature-factory.”
- “Use the ICP and write the vision-to-outcome strategy.”
- “Turn discovery notes into product bets.”
- “Create a product strategy that focuses on measurable customer and business impact.”

## Example output fragment

```markdown
## Strategy Sentence
We will help first-time marketplace sellers publish a trustworthy first listing by removing confidence gaps around pricing, photos, and shipping, because it increases seller activation, and we will prove it through first-listing completion rate, listing quality score, and 30-day seller retention.

## Primary Obstacle
New sellers do not know what “good enough to publish” looks like, so they stall before creating supply. The product problem is not more listing fields; it is confidence, guidance, and proof at the moment of first commitment.

## What We Will Not Do
- We will not optimize advanced seller tools before first-listing activation improves.
- We will not add more listing fields unless they reduce uncertainty or increase buyer trust.
- We will not target power sellers until the first-time seller path proves repeatable.
```
