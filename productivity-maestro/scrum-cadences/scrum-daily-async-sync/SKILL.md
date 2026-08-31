---
name: scrum-daily-async-sync
description: "Trigger: daily scrum, daily standup, async drift triage, unblock subagents, 24h sync, daily sync brief, daily blocker triage. Scope: Original Scrum Daily Standup & 24h Cybernetic Drift Triage. Eliminates status reporting to managers; focuses on peer unblocking, surfacing hidden impediments, and maintaining alignment to the Sprint Goal. Answers the 3 core questions with zero filler: (1) Last 24h increment, (2) Next 24h commitment, (3) Blockers and drift risks. Boundary: Excludes sprint planning (use scrum-sprint-planning-capacity) or retrospective root-cause audits (use scrum-retrospective-kaizen)."
---

# Rule: Scrum Daily Standup & 24h Drift Triage

> [!IMPORTANT]
> **Ethos & Origins**: Grounded in **Jeff Sutherland & Ken Schwaber** (*Scrum Guide*).
> **The Cybernetic Purpose**: Neutralizes human **Isolation, Sunk Cost, and Error Hiding**.
>
> **The Prime Directive**: The Daily Scrum is **peer-to-peer coordination**, not a status report to management. It runs in $<15$ minutes to detect drift within 24 hours and swarm on blockers immediately.

---

## When to use

Use this skill daily to synchronize pod execution and unblock progress:
- Conducting daily asynchronous or live **15-minute synchronization**.
- Surfacing impediments, technical blockers, and dependency stalls early.
- Re-aligning daily work directly against the **Sprint Goal**.
- Coordinating swarm pairing when a team member is stuck.

## When not to use

Do not use this skill for:
- Long-winded technical architecture debates (schedule a 16th-minute sidebar).
- Sprint Planning or scope negotiation (use `scrum-sprint-planning-capacity`).
- Evaluating working software with stakeholders (use `scrum-sprint-review-increment`).

## Trigger cues

- Request mentions: `daily scrum`, `daily standup`, `async drift triage`, `unblock subagents`, `24h sync`, `daily sync brief`, `daily blocker triage`.

## Inputs required

1. **Active Sprint Goal**: The committed objective for the current sprint.
2. **Current Sprint Board / Task State**: In-progress, completed, and blocked tasks.
3. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Answer the 3 Core Questions with High Information Density**:
   - *Yesterday*: What did I finish that helped the team meet the Sprint Goal?
   - *Today*: What will I finish today to help the team meet the Sprint Goal?
   - *Blockers*: What impediments or friction points are slowing me down?
3. **Enforce Anti-Status Rules**:
   - Zero narrative storytelling or activity lists. Focus strictly on *Increments Completed* and *Blockers*.
4. **Trigger 16th-Minute Swarm Action**:
   - If a blocker is identified, immediately assign a pairing partner and schedule an isolated sidebar.

## Completion gate

- [ ] Clear 3-part daily sync brief produced.
- [ ] Explicit link between daily commitments and the Sprint Goal.
- [ ] All blockers flagged with designated unblock owners.
