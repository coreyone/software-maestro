---
name: design-5-act-user-interview-testing
description: "Conduct 5-act qualitative usability interviews and build prototype test scorecards."
---

# Rule: Michael Margolis & Jake Knapp — 5-Act User Interview Testing (Friday)

> [!IMPORTANT]
> **Foundation**: Grounded in **Michael Margolis** (*Learn More Faster*) and **Jake Knapp** (*Sprint*), anchored by **Jakob Nielsen's 5-User Rule** ($U(n) = N[1 - (1-L)^n]$).
> **The Prime Directive**: Extract empirical customer evidence without confirmation bias. Run 5 live 1-on-1 interviews using the 5-Act protocol, build the color-coded pattern scorecard, and answer Monday's 3 Sprint Questions.
>
> **Lifecycle Governance**:
> - **Input**: Tests the interactive facade from [`/design-rapid-prototype-facade`](../../experience-and-flows/design-rapid-prototype-facade/SKILL.md).
> - **Downstream Synthesis**: Feeds verified verdicts into [`/create-prd`](../../../product/discovery-and-specs/create-prd/SKILL.md) and [`/michael-bolton-pod-conductor`](../../../product/orchestration/michael-bolton-pod-conductor/SKILL.md).

---

## When to use

Use this skill on Friday of a Design Sprint to test and synthesize customer evidence:
- Conducting **5 live 1-on-1 customer interviews** (60 min each: 45 min test + 15 min debrief).
- Running the **5-Act Interview Protocol** (Welcome $\rightarrow$ Context $\rightarrow$ Introduce Prototype $\rightarrow$ Tasks & Nudges $\rightarrow$ Debrief).
- Applying non-directive, neutral probing prompts (*"What did you expect to happen?"*).
- Building the **Color-Coded Pattern Scorecard Matrix** (Green = Validated, Red = Friction/Dropoff, Yellow = Mixed).
- Generating evidence-backed verdicts for Monday's **3 Sprint Questions** and delivering a **Go / Pivot / Kill** recommendation.

## When not to use

Do not use this skill for:
- Automated headless browser tests (use `chrome-devtools` or `playwright`).
- Quantitative A/B experimentation analytics (use `analytics-event-tracking` or `data-science-causal-inference`).
- Storyboarding or prototyping (use `design-storyboard-decide` or `design-rapid-prototype-facade`).

## Trigger cues

- Request mentions: `5 act interview`, `5 act user interview testing`, `design sprint testing`, `user test debrief`, `5 user testing`, `michael margolis interview`, `prototype reaction scorecard`, `jakob nielsen 5 user rule`, `friday sprint test`.

## Inputs required

1. **Interactive Facade**: From `design-rapid-prototype-facade`.
2. **3 Sprint Questions & Target**: From `design-sprint-map`.
3. **5 Target ICP Participants**: Matching the Monday persona definition.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Execute the 5-Act Interview Protocol with 5 Users**:
   - *Act 1 (Welcome)*: Establish safety; remind participant you are testing the prototype, not them.
   - *Act 2 (Context)*: Ask open workflow questions without mentioning the solution.
   - *Act 3 (Introduce)*: Present prototype with scenario framing.
   - *Act 4 (Tasks & Nudges)*: Observe actions; ask non-leading think-aloud questions.
   - *Act 5 (Debrief)*: Capture holistic takeaways, price sensitivity, and comparison to existing tools.
3. **Populate Pattern Scorecard Wall**:
   - Color code observations: 🟩 Green (Validated), 🟥 Red (Broken/Rejection), 🟨 Yellow (Neutral).
4. **Synthesize Sprint Question Verdicts**:
   - Rate each of Monday's 3 Sprint Questions as **Validated**, **Invalidated**, or **Inconclusive** backed by direct verbatim quotes.
5. **Issue Executive Decision Recommendation**:
   - Deliver clear Go / Pivot / Kill directive for engineering and product leadership.

## Completion gate

- [ ] 5 completed 1-on-1 interview notes documented.
- [ ] Pattern Scorecard Matrix fully populated across all test steps.
- [ ] Explicit evidence-backed verdicts for all 3 Sprint Questions.
- [ ] Actionable Go / Pivot / Kill next steps defined.
