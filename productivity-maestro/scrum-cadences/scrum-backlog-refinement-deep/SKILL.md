---
name: scrum-backlog-refinement-deep
description: "Trigger: backlog refinement, story grooming, backlog grooming, story splitting, INVEST criteria, definition of ready, DoR audit, 3 Cs card conversation confirmation, backlog preparation, sizing user stories. Scope: Original Scrum Backlog Refinement & Deep Story Slicing. Neutralizes large-batch requirements stagnation and mid-sprint surprise blockers. Enforces INVEST criteria, Definition of Ready (DoR) gating, the 3 Cs framework (Card, Conversation, Confirmation), and horizontal/vertical story splitting heuristics. Ensures 2 sprints of fully refined, ready work are continuously staged. Boundary: Excludes sprint backlog locking (use scrum-sprint-planning-capacity) or strategic roadmapping (use decision-stack-governance)."
---

# Rule: Scrum Backlog Refinement & Deep Story Slicing

> [!IMPORTANT]
> **Ethos & Origins**: Grounded in **Ken Schwaber & Jeff Sutherland** (*The Scrum Guide*), **Ron Jeffries** (*3 Cs: Card, Conversation, Confirmation*), **Bill Wake** (*INVEST Criteria*), and **Dean Leffingwell** (*Lean-Agile Story Splitting*).
>
> **The Cybernetic Purpose**: Neutralizes **Large-Batch Requirements Stagnation, Scope Creep Ambiguity, and Mid-Sprint Blockers**.  
> **The Continuous Cadence**: Consumes ~10% of team capacity across the sprint to maintain a rolling queue of **2 sprints of Definition-of-Ready (DoR) items**.

---

## When to use

Use this skill continuously or in scheduled mid-sprint refinement sessions to prepare backlog items for upcoming sprints:
- Slicing monolithic epic stories into small, independently testable user stories ($\le 8$ points / $\le 2$ days effort).
- Applying the **INVEST criteria** (Independent, Negotiable, Valuable, Estimable, Small, Testable) to user stories.
- Enforcing **Definition of Ready (DoR)** gating prior to Sprint Planning.
- Translating ambiguous business requests into **3 Cs** (Card, Conversation, Confirmation) with BDD/Gherkin acceptance criteria.
- Identifying technical dependencies, architectural spikes, and integration risks before sprint commitment.

## When not to use

Do not use this skill for:
- Sizing and locking the immediate sprint commitment (use `scrum-sprint-planning-capacity`).
- Daily blocker triage and 24h drift detection (use `scrum-daily-async-sync`).
- Inspecting completed software increments with stakeholders (use `scrum-sprint-review-increment`).
- Initial high-level PRD creation and problem scoping (use `create-prd`).

## Trigger cues

- Request mentions: `backlog refinement`, `story grooming`, `backlog grooming`, `story splitting`, `INVEST criteria`, `definition of ready`, `DoR audit`, `3 Cs card conversation confirmation`, `backlog preparation`, `sizing user stories`.

## Inputs required

1. **Raw or Candidate Backlog Items**: Epics, feature requests, or unrefined user stories.
2. **Business Context & Acceptance Expectations**: Product Owner intent, target user persona, and success criteria.
3. **Architectural & Design Constraints**: API contracts, data models, UX wireframes/tokens.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Apply the 3 Cs Framework**:
   - **Card**: Formulate the story token: *"As a `<user_persona>`, I want `<capability>`, so that `<business_value>`"*.
   - **Conversation**: Capture technical nuances, edge cases, and architectural constraints discussed between PO and Developers.
   - **Confirmation**: Specify explicit, unambiguous BDD/Gherkin test criteria (`Given / When / Then`).
3. **Execute Story Splitting Heuristics**:
   - If a story exceeds $\le 8$ story points or 2 days of engineering effort, split using canonical patterns:
     1. *Workflow Steps*: First step vs. subsequent steps.
     2. *Business Rule Variations*: Simple baseline rule vs. complex exceptions/multi-currency.
     3. *Data Variations*: Standard text input vs. rich-media/file uploads.
     4. *Happy vs. Unhappy Path*: Core success path vs. localized fallback/error recovery.
     5. *Platform / Interface*: Mobile web vs. desktop or API-only baseline vs. UI wrapper.
4. **Audit Against INVEST Criteria**:
   - **I**ndependent: Can this story be built and deployed without coupling to uncommitted stories?
   - **N**egotiable: Is there room for implementation trade-offs?
   - **V**aluable: Does it deliver distinct user or system value?
   - **E**stimable: Does the team understand the scope well enough to size it?
   - **S**mall: Fits within a single sprint (ideal: 1–3 days)?
   - **T**estable: Are the acceptance criteria deterministic and automated-test ready?
5. **Verify Definition of Ready (DoR) Gate**:
   - Check all DoR requirements: clear acceptance criteria, dependencies mapped, designs ready, and sizing agreed upon.

## Completion gate

- [ ] All stories framed in 3 Cs structure with unambiguous BDD/Gherkin acceptance criteria.
- [ ] Monolithic stories sliced into independent units ($\le 8$ points each).
- [ ] 100% of candidate items pass INVEST audit and satisfy Definition of Ready (DoR).
- [ ] Identified spikes or architectural unknowns separated into dedicated timeboxed tasks.
