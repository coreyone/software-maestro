---
name: scrum-planning-and-refinement
description: "Refine product backlogs with INVEST slicing criteria and calibrate sprint planning capacity."
---

# Rule: Scrum Sprint Planning & Backlog Refinement (Prep Phase)

> [!IMPORTANT]
> **Lineage & Origins**: Grounded in **Ken Schwaber & Jeff Sutherland** (*The Scrum Guide*), **Roman Pichler** (*DEEP Backlog*), **Mike Cohn** (*Planning Poker & SPIDR Slicing*), and **Bill Wake** (*INVEST*).
> **The Cybernetic Purpose**: Neutralizes **Predictive Hubris, Optimism Bias, and Large-Batch Requirements Stagnation**.
>
> **The Two Inseparable Prep Cadences**:
> 1. **Backlog Refinement (Continuous / 10% Capacity)**: Slices epics into INVEST-compliant user stories ($\le 8	ext{ pts}$ / $\le 2	ext{ days}$) with executable BDD/Gherkin acceptance criteria to maintain a rolling queue of 2 sprints of Definition of Ready (DoR) work.
> 2. **Sprint Planning (Sprint Kickoff)**: Product Owner defines *What/Why*; Developers define *How/Capacity*. Commits to **1 singular qualitative Sprint Goal** and sizes the Sprint Backlog against empirical historical velocity.

---

## When to use

Use this skill for sprint preparation and scope negotiation:
- **Mode: `refinement`**: Decomposing monolithic epics into thin vertical slices using SPIDR heuristics, applying the 3 Cs (Card, Conversation, Confirmation), sizing with Planning Poker (Story Points), and gating against the **Definition of Ready (DoR)**.
- **Mode: `planning`**: Formulating a single cohesive **Sprint Goal**, calculating velocity capacity, selecting sprint backlog items, establishing WIP limits, and locking the sprint backlog.

## Completion gate

- [ ] All candidate user stories sliced into INVEST units ($\le 8	ext{ pts}$) meeting Definition of Ready.
- [ ] 1 Singular qualitative Sprint Goal defined.
- [ ] Capacity forecasted using trailing 3-sprint empirical velocity.
- [ ] Explicit non-goals and trade-off triggers locked.
