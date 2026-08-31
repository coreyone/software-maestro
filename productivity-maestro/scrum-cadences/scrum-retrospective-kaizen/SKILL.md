---
name: scrum-retrospective-kaizen
description: "Trigger: sprint retrospective, blameless retro, kaizen process improvement, systemic failure triage, norm kerth prime directive, scrum retro, retro action item. Scope: Original Scrum Sprint Retrospective & Egoless Kaizen Engine. Enforces Norm Kerth's Prime Directive and Deming's System Variation thinking (separating systemic flaws from individual blame). Analyzes sprint friction, runs 5-Whys root cause triage on system failures, and commits to strictly one measurable process upgrade for the next sprint. Boundary: Excludes stakeholder product review (use scrum-sprint-review-increment) or organizational restructuring (use systems-retro-pruning)."
---

# Rule: Scrum Sprint Retrospective & Egoless Kaizen

> [!IMPORTANT]
> **Ethos & Origins**: Grounded in **Norm Kerth** (*Project Retrospectives*), **W. Edwards Deming** (Systems Quality), and **Jeff Sutherland**.
> **The Prime Directive**:
> *"Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."*
>
> **The Cybernetic Purpose**: Neutralizes **Defensive Scapegoating and Stagnation**. Converts friction into **Kaizen** (continuous empirical improvement) by committing to **strictly 1 measurable system change per sprint**.

---

## When to use

Use this skill at the end of every sprint cycle to inspect team processes and execute continuous improvement:
- Conducting a **blameless Sprint Retrospective**.
- Applying the **5-Whys Root Cause Analysis** on engineering and coordination bottlenecks.
- Inspecting relationships, tools, environment, and Definition of Done.
- Committing to **strictly 1 high-leverage process upgrade** for the immediate next sprint.

## When not to use

Do not use this skill for:
- Product demo and stakeholder feedback (use `scrum-sprint-review-increment`).
- Annual organizational restructuring (use `systems-retro-pruning`).
- Daily blocker triage (use `scrum-daily-async-sync`).

## Trigger cues

- Request mentions: `sprint retrospective`, `blameless retro`, `kaizen process improvement`, `systemic failure triage`, `norm kerth prime directive`, `scrum retro`, `retro action item`.

## Inputs required

1. **Sprint Events Timeline**: Incidents, blocked tickets, unexpected delays, team sentiment.
2. **Previous Sprint Retro Commitment**: Audit whether the prior improvement was executed.
3. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Reaffirm Norm Kerth's Prime Directive**:
   - Establish total psychological safety. Focus on *system variation*, not personal effort.
3. **Audit Previous Retro Commitment**:
   - Review whether last sprint's Kaizen experiment succeeded.
4. **Gather Data & Generate Insights**:
   - Cluster observations: *What went well? What caused friction? What surprised us?*
5. **Run 5-Whys Root Cause Triage on Top Friction**:
   - Dig past superficial human error to identify tooling, input, or process root causes.
6. **Commit to Strictly 1 Kaizen Process Upgrade**:
   - Define 1 concrete, verifiable action item with an owner and success metric for the next sprint backlog.

## Completion gate

- [ ] Prime directive established and prior retro action audited.
- [ ] 5-Whys root-cause analysis completed on top friction point.
- [ ] Exactly 1 concrete, measurable Kaizen process upgrade defined for the next sprint.
