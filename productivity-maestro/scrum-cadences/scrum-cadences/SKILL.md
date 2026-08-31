---
name: scrum-cadences
description: "Trigger: scrum, scrum cadence, sprint planning, daily scrum, daily standup, sprint review, sprint retrospective, backlog refinement, story grooming, scrum meeting, agile ceremonies, definition of ready, definition of done. Scope: Original Scrum Cybernetic Behavioral Harness Master Hub. Orchestrates the 5 canonical Scrum closed-loop feedback cadences: (1) Backlog Refinement (DEEP framework, INVEST slicing, 3 Cs, DoR gating), (2) Sprint Planning (1 singular Sprint Goal, empirical velocity calibration, WIP limits), (3) Daily Scrum (24h drift triage, peer unblocking, 16th-minute swarm pairing), (4) Sprint Review (Working increment demo against DoD, anti-slide law, backlog adaptation), and (5) Sprint Retrospective (Norm Kerth Prime Directive, 5-Whys root cause, strictly 1 Kaizen process upgrade). Boundary: Excludes high-level company OKRs (use decision-stack-governance) or architectural code execution (use developer-development-rules)."
---

# Rule: Scrum Cybernetic Behavioral Harness Master Hub

> [!IMPORTANT]
> **Lineage & Origins**: Grounded in **Ken Schwaber, Jeff Sutherland** (*The Scrum Guide*), **Norm Kerth** (*Project Retrospectives*), **Roman Pichler** (*DEEP Backlog*), **Mike Cohn** (*Planning Poker & Story Slicing*), and **W. Edwards Deming** (Systems Quality).
> **The Cybernetic Purpose**: Neutralizes human and synthetic cognitive failures: predictive hubris, silent error hiding, "90% done" watermelon theater, and defensive scapegoating.

---

## The 5 Scrum Closed-Loop Cadences

| Cadence | Mode | Primary Focus | Key Output Artifact |
| :--- | :--- | :--- | :--- |
| **1. Backlog Refinement** | `refinement` | DEEP slicing, INVEST audit, Definition of Ready | `refined_backlog_slices.md` |
| **2. Sprint Planning** | `planning` | 1 Sprint Goal, empirical velocity calibration | `sprint_commitment_contract.md` |
| **3. Daily Standup** | `daily` | 24h drift detection, peer unblocking | `daily_sync_brief.md` |
| **4. Sprint Review** | `review` | Live working software demo vs. Definition of Done | `sprint_increment_audit.md` |
| **5. Sprint Retrospective**| `retro` | Egoless Kaizen, 5-Whys root cause on friction | `retrospective_kaizen_action.md` |

---

## When to use

Invoke `scrum-cadences` for any Scrum event or operating ritual:
- **`refinement`**: Decomposing monolithic epics into INVEST-compliant user stories ($\le 8	ext{ pts}$) with Gherkin acceptance criteria.
- **`planning`**: Locking a single qualitative Sprint Goal and sizing backlog items to match historical velocity.
- **`daily`**: Running the 15-minute peer synchronization to surface blockers and maintain Sprint Goal alignment.
- **`review`**: Inspecting live, working software with stakeholders (strict ban on PowerPoint decks) and adapting the Product Backlog.
- **`retro`**: Applying Norm Kerth's Prime Directive and 5-Whys to commit to **strictly 1 measurable process change**.

## Completion gate

- [ ] Selected cadence artifact generated with zero vanity metrics or filler.
- [ ] Strict adherence to Definition of Ready (DoR) or Definition of Done (DoD).
- [ ] Action items have single named owners and explicit verification metrics.
