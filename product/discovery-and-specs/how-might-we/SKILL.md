---
name: how-might-we
description: >
  Frame evidence-backed How Might We (HMW) questions for design thinking,
  product discovery, UX research, service design, design sprints, PRDs, and
  system change. Use when the user asks to generate, critique, rewrite,
  compare, prioritize, workshop, or apply HMW questions; convert observations,
  interviews, JTBD, journeys, research synthesis, or problem statements into
  bounded design opportunities; or connect HMW work to d.school, IDEO, Double
  Diamond, design sprints, Opportunity Solution Trees, or assumption tests.
  Do not use for generic brainstorming without a user/context problem,
  feature specifications, implementation, or final research synthesis unless
  HMW framing is the requested output.
---

# How Might We

Use HMW as a framing operation, not as a substitute for discovery, strategy, or validation.
Convert evidence into a bounded design opportunity, preserve the user and context, open multiple solution paths, then connect promising ideas to explicit assumptions and tests.

## Core model

Use this chain:

```text
evidence -> insight or point of view -> HMW frame -> solution alternatives -> assumptions -> tests and decision
```

Treat an HMW as successful when it is:

- grounded in observed behavior, a documented need, or a clearly labeled hypothesis;
- tied to a meaningful user, product, service, or system outcome;
- open to several materially different solution families;
- bounded by the relevant actor, context, and non-negotiable constraints; and
- useful for producing testable next actions.

Read [references/frameworks.md](references/frameworks.md) when the user asks for expert attribution, framework comparison, historical lineage, or a research-level explanation.

## Workflow

### 1. Establish the frame

Extract or state:

- affected user, stakeholder, or non-human impact;
- situation and observed behavior;
- insight, need, or tension;
- desired progress or outcome;
- constraints, risks, and excluded scope; and
- evidence versus assumption.

If material context is missing, make the smallest safe assumption and label it. Ask one focused question only when different answers would materially change the HMW direction.

Do not treat a feature request, stakeholder preference, or metric decline as an insight without identifying the underlying behavior or need.

### 2. Write the opportunity before the question

Use a compact point-of-view or opportunity statement:

```text
[actor] needs [desired progress] in [context] because [evidence-backed insight], despite [constraint or tension].
```

Keep the opportunity separate from the solution. “Needs a faster way to submit expenses” is an opportunity; “needs a mobile receipt scanner” is a solution hypothesis.

### 3. Generate a small set of HMW candidates

Write 3–7 candidates. Use different reframing moves when useful:

- amplify what is already working;
- explore the opposite or remove an assumed rule;
- take the idea to an extreme;
- focus on emotion, trust, identity, or social context;
- question an assumption;
- focus on a specific moment, actor, or constraint; or
- use an analogy from another domain.

Do not generate variants by swapping synonyms. Each candidate should open a meaningfully different intervention space.

### 4. Evaluate and select

Score or discuss each candidate against:

| Criterion | Check |
|---|---|
| Evidence fidelity | Can the question be traced to evidence or a labeled hypothesis? |
| Outcome relevance | Would a good answer advance the intended outcome? |
| Solution range | Could different solution families answer it? |
| Scope | Is it neither “redesign everything” nor a disguised feature? |
| Testability | Could an answer produce an observable prediction? |
| Inclusion and ethics | Does it account for affected people, power, access, and harm? |

Recommend one primary HMW and retain at most two alternatives when they represent genuinely different frames. Explain what each frame makes visible and what it hides.

### 5. Separate divergence from convergence

During ideation, use the selected HMW to generate and combine options before judging them. Afterward, converge with explicit criteria and assumptions. Do not use the HMW as evidence that an idea is desirable, feasible, viable, usable, or ethical.

Map the strongest ideas to:

```text
outcome -> opportunity -> solution -> assumption -> test
```

Prefer the smallest test that can distinguish competing solutions or invalidate the riskiest assumption.

### 6. Revise when the evidence changes

An HMW is a working frame, not a commitment. Reframe it when interviews, observation, prototype behavior, feasibility findings, or stakeholder impact reveal that the original opportunity was wrong, too narrow, or solving the wrong level of the system.

## Output modes

### Generate

Return:

1. evidence and assumptions;
2. the opportunity or point of view;
3. 3–7 HMW candidates;
4. the recommended HMW with rationale;
5. scope, ethical, or framing risks; and
6. the smallest useful next test.

### Critique or rewrite

For each supplied HMW, identify:

- the implied user and outcome;
- any hidden solution, assumption, or power issue;
- whether it is too broad, too narrow, or appropriately bounded;
- the solution families it enables or excludes; and
- a stronger rewrite.

### Facilitate a workshop

Provide a timeboxed sequence with the input artifact, activity, decision rule, and output for each step. Keep research synthesis, divergent HMW generation, solution ideation, and prioritization as separate moments. Include the people affected by the frame when feasible.

### Explain the method

Distinguish HMW from adjacent artifacts:

- a research question asks what is true;
- an HMW asks what could be designed or changed;
- a product requirement says what should be built;
- a success metric says how change will be observed.

Use the named frameworks only when they change the explanation. Do not name-drop experts or present HMW as a universal recipe.

## Guardrails

- Never turn “How might we?” into a feature template such as “How might we add a dashboard?”
- Never invent customer evidence, quotes, stakeholder consent, or expert positions.
- Never equate a brainstorm’s volume with innovation or validation.
- Preserve important constraints; do not broaden a question merely to make it sound creative.
- Make “we” explicit when roles, incentives, or power differ.
- Include non-user effects and ethical risks for systemic, public-sector, health, financial, or AI work.
- Treat “might” as permission to explore, not permission to avoid a decision.
- Prefer several competing solution paths over premature commitment to the first attractive answer.
- Keep the final response proportional: concise for a simple rewrite, structured for a workshop or discovery artifact.

## Compact example

Input insight:

> First-time teams abandon setup when asked to invite collaborators before they have experienced product value.

Opportunity:

> First-time teams need to reach an initial moment of value before coordination overhead becomes necessary.

Candidates:

- How might we help a first-time team experience value before asking it to coordinate?
- How might we make setup useful even when only one person is present?
- How might we turn the first collaboration step into evidence of value rather than administration?

Recommended HMW:

> How might we help a first-time team experience value before asking it to coordinate?

Possible solution families include sample data, a solo mode, guided import, or a collaborative invitation that produces immediate value. Test desirability and usability before committing to a particular feature.
