---
name: now-next-later-roadmaps
description: "Trigger: now-next-later-roadmaps, now next later roadmap, Janna Bastow roadmap, time horizon roadmap, outcome-based roadmap, problem-oriented roadmap, roadmap prioritization, roadmap alignment. Scope: Outcome-Driven Now-Next-Later Roadmapping (Janna Bastow). Replaces date-driven Gantt charts with uncertainty horizons (Now = high certainty/granular problems, Next = medium certainty/discovery, Later = low certainty/directional strategy) tied to business objectives. Boundary: Excludes sprint backlog estimation (use scrum-planning-and-refinement) and tactical PRD authoring (use create-prd)."
---

# Rule: Outcome-Driven Now-Next-Later Roadmapping

> [!IMPORTANT]
> **Ethos & Theoretical Lineage**:
> Grounded in **Janna Bastow** (*ProdPad, Creator of Now-Next-Later*), **Melissa Perri** (*Escaping the Build Trap*), **Bruce McCarthy & C. Todd Lombardo** (*Product Roadmaps Relaunched*), **Marty Cagan** (*Inspired*), and **Tony Fadell (*Build* — Ch 16: Heartbeats and Handcuffs)**.
>
> **The Prime Directive**: *"A roadmap is a strategic communication tool, not a release plan or a Gantt chart."* Never commit to fixed dates and static feature lists months in advance. Structure roadmaps around **customer problems and business outcomes** across three horizons of decreasing certainty: **Now** (current focus / high certainty), **Next** (near-term priorities / medium certainty), and **Later** (future opportunities / low certainty).
>
> **The Fadell Heartbeat Invariant**: When shipping deadlines for the "Now" horizon arrive, **never slip the date—slip the scope**. Fixed shipping heartbeats force ruthless scope trade-offs and prevent perfectionist paralysis.

---

## When to use

Use this skill when:
- Establishing, restructuring, or presenting a product roadmap focused on outcomes rather than fixed-date feature promises.
- Communicating strategic direction and product priorities to executives, sales, customer success, engineering, or customers.
- Transitioning teams away from timeline-based Gantt charts and "feature factory" dynamics.
- Aligning product initiatives across three time horizons based on validated certainty and discovery status.
- Structuring roadmap cards around problems to solve, target outcomes, candidate experiments, and business objectives.

## When not to use

Do not use this skill for:
- Decomposing roadmap cards into sprint tickets or user stories (use `prd-to-tickets`).
- Authoring detailed engineering PRDs and BDD acceptance criteria (use `create-prd`).
- Sprint backlog grooming, daily standups, or 2-week agile ceremonies (use `scrum-planning-and-refinement` and `scrum-daily-sync`).
- High-level multi-year executive strategy tree cascading (use `decision-stack-governance`).

## Trigger cues

- Explicit references: `now-next-later-roadmaps`, `now next later roadmap`, `Janna Bastow roadmap`, `time horizon roadmap`, `outcome-based roadmap`, `problem-oriented roadmap`.
- Request phrases: "create a Now-Next-Later roadmap", "reframe our feature roadmap into problems to solve", "build an outcome-driven roadmap", "replace our timeline Gantt chart with time horizons", "prioritize product bets across Now Next Later".

## Routing boundary

- Primary for time-horizon roadmap architecture, problem-to-outcome mapping, certainty calibration, and stakeholder alignment.
- Route upstream strategic cascading to `decision-stack-governance`.
- Route downstream spec authoring to `create-prd` and ticket slicing to `prd-to-tickets`.
- Route sprint execution tracking to `scrum-planning-and-refinement` and release governance to `release-readiness-gtm`.

## Inputs required

1. **Company Vision & Strategic Objectives / OKRs**: High-level business targets and strategic themes.
2. **Customer Problem Backlog / Insights**: Qualitative user feedback (`voc-insights-pipeline`) and empirical validation (`product-hypothesis-loop`).
3. **Current Delivery Status**: Active work in progress vs. discovery opportunities.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Step 1: Map the Three Horizons of Certainty**:
   - **NOW (High Certainty / In-Flight / 0–2 Months)**:
     - Clear, granular customer problem with validated demand.
     - Active delivery and technical execution underway.
     - Immediate target metric and clear success criteria defined.
   - **NEXT (Medium Certainty / Discovery & Prototyping / 1–4 Months)**:
     - Validated customer friction or business need; solution space currently being explored.
     - Active research, facade prototypes, and customer interviews.
     - Candidate solutions identified but uncommitted.
   - **LATER (Low Certainty / Strategic Bets / 3–12+ Months)**:
     - Broad strategic opportunities aligned with vision and long-term OKRs.
     - Low certainty; problem space understood directionally but not yet prioritized for active discovery.
     - Uncommitted exploration; subject to reprioritization or pruning.
3. **Step 2: Structure Each Roadmap Card (Problem-Oriented Anatomy)**:
   Every roadmap card MUST adhere to the 5-point anatomy:
   - **Title**: Expressed as a problem statement or desired outcome (NOT a feature name).
   - **Strategic Theme / Objective**: Linked business intent or OKR.
   - **Problem to Solve (JTBD)**: Who experiences the friction and what is their struggle.
   - **Target Outcome & Metric Lift**: Measurable quantitative/qualitative key result.
   - **Candidate Solutions / Options**: 2–3 testable hypotheses or experiment approaches (explicitly non-binding).
4. **Step 3: Establish Horizon Progression & Pruning Rules**:
   - Items graduate from Later $\rightarrow$ Next $\rightarrow$ Now only when discovery reduces uncertainty and evidence supports investment.
   - Kill or pivot items in Next/Later when discovery disproves demand without breaking delivery trust.
   - Maintain WIP limits: Now column should contain strictly 2–4 active initiatives per squad to avoid context fragmentation.
5. **Step 4: Conduct Stakeholder Roadmap Reviews**:
   - Frame conversations around *problems and impact* rather than *shipping dates*.
   - Decouple strategic roadmaps from release plans (use release milestones for committed go-to-market dates).

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- [ ] Roadmap explicitly organized across **Now**, **Next**, and **Later** columns.
- [ ] Zero arbitrary calendar dates or Gantt timelines embedded in strategic cards.
- [ ] Every card framed as a **Problem to Solve** with linked **Strategic Theme / OKR** and **Target Metric Lift**.
- [ ] Candidate solutions formatted as testable options rather than rigid feature commitments.
- [ ] WIP limits enforced on the **Now** horizon (2–4 items per team).

## Output format

- **Now-Next-Later Strategic Canvas**: Structured table or card matrix organized by Strategic Theme and Time Horizon.
- **Card Specification**: Detailed breakdown of each card (Problem, Target Outcome, Candidate Options, Risks).
- **Certainty & Progression Rationale**: Explicit evidence justifying why each item sits in Now, Next, or Later.
- **Stakeholder Communication Guide**: Framing for execs, sales, and customers to prevent date-locking traps.
