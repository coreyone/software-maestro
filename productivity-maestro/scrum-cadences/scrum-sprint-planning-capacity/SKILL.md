---
name: scrum-sprint-planning-capacity
description: "Trigger: sprint planning, sprint goal formulation, capacity calibration, sprint backlog lock, commitment negotiation, scrum planning, sprint forecast. Scope: Original Scrum Sprint Planning & Cybernetic Capacity Calibration. Tames the Planning Fallacy. Separates Product Owner What/Why from Developer How/Capacity. Formulates 1 qualitative Sprint Goal, sizes items against historical velocity, sets hard Work-In-Progress (WIP) limits, and locks the Sprint Backlog. Boundary: Excludes daily sync (use scrum-daily-async-sync) or PRD authoring (use create-prd)."
---

# Rule: Scrum Sprint Planning & Capacity Calibration

> [!IMPORTANT]
> **Ethos & Origins**: Grounded in **Jeff Sutherland & Ken Schwaber** (*Scrum: The Art of Doing Twice the Work in Half the Time*).
> **The Cybernetic Purpose**: Neutralizes human **Predictive Hubris and Optimism Bias**. Separates *What/Why* (owned by Product Owner) from *How/Capacity* (wholly owned by Developers).
>
> **Core Invariants**:
> - **1 Singular Sprint Goal**: Qualitative outcome that binds the team in shared fate.
> - **Historical Velocity vs. Wishful Thinking**: Forecast capacity based strictly on empirical past completion rates.
> - **Locked Sprint Backlog**: Prevents WIP sprawl and scope thrash during the sprint cycle.

---

## When to use

Use this skill at the beginning of a sprint cycle to negotiate scope and lock commitments:
- Formulating a singular, meaningful **Sprint Goal** that provides direction without micromanaging tasks.
- Sizing and selecting Product Backlog Items based on **empirical historical velocity**.
- Establishing strict **Work-In-Progress (WIP) limits** to enforce single-piece flow.
- Negotiating trade-offs when scope exceeds realistic team capacity.

## When not to use

Do not use this skill for:
- Daily standups and 24h drift triage (use `scrum-daily-async-sync`).
- High-level multi-year product strategy or portfolio roadmaps (use `decision-stack-governance`).
- End-of-sprint working software demos (use `scrum-sprint-review-increment`).

## Trigger cues

- Request mentions: `sprint planning`, `sprint goal formulation`, `capacity calibration`, `sprint backlog lock`, `commitment negotiation`, `scrum planning`, `sprint forecast`.

## Inputs required

1. **Prioritized Product Backlog**: Ordered items with clear acceptance criteria.
2. **Historical Velocity & Available Capacity**: Past sprint completion rate and known out-of-office/on-call constraints.
3. **Product Owner Intent**: Strategic milestone or release target.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Formulate the Singular Sprint Goal**:
   - Write a clear, 1-sentence qualitative goal that answers: *"Why are we running this sprint, and what outcome makes it successful?"*
3. **Calibrate Capacity & Forecast Velocity**:
   - Use empirical trailing 3-sprint velocity average. Subtract buffer for maintenance, on-call, and unplanned friction.
4. **Select & Decompose Backlog Items**:
   - Break selected user stories into discrete developer tasks ($\le 1	ext{ day}$ each).
   - Verify every item satisfies the Definition of Ready.
5. **Lock the Sprint Backlog & Establish Trade-Off Triggers**:
   - Document explicit non-goals and criteria for when scope must be trimmed.

## Completion gate

- [ ] 1 Singular qualitative Sprint Goal defined.
- [ ] Forecasted capacity matched against empirical historical velocity.
- [ ] Selected Sprint Backlog items broken into tasks with clear acceptance criteria.
- [ ] Explicit trade-off and scope adjustment boundaries locked.
