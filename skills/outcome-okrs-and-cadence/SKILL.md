---
name: outcome-okrs-and-cadence
description: "Draft outcome-driven OKRs, structure 4-quadrant canvases, and facilitate weekly commitment cadences."
---

# Rule: Outcome OKRs & Radical Focus Execution Cadence

> [!IMPORTANT]
> **Ethos & Theoretical Lineage**:
> Grounded in **Christina Wodtke** (*Radical Focus: Achieving Your Most Important Goals with Objectives and Key Results*), **Andy Grove** (*High Output Management*), and **John Doerr** (*Measure What Matters*).
>
> **The Prime Directive**: *"Focus on one thing at a time, commit ruthlessly, and pair outcome metrics with non-negotiable health guardrails."* Never formulate OKRs as a laundry list of output tasks or feature launches. Set **1 qualitative, inspirational Objective** paired with **3 quantitative outcome Key Results** (5/10 confidence baseline), governed by the **4-Quadrant Radical Focus Canvas** and sustained through the **Monday Commitments $\rightarrow$ Friday Wins** operational rhythm.

---

## When to use

Use this skill when:
- Defining quarterly Objectives and Key Results (OKRs) for a product squad, department, or company.
- Transitioning teams from activity/output-based metrics ("Launch feature X") to customer/business outcome metrics ("Increase conversion from 12% to 28%").
- Establishing the 4-Quadrant OKR execution canvas to balance focal goals against operational health metrics.
- Running the weekly execution rhythm: Monday Commitment meetings (setting P1/P2 priorities and calibrating confidence) and Friday Wins sessions (celebrating progress and demos).
- Conducting end-of-quarter scoring (0.0 to 1.0) and blameless retrospectives.

## When not to use

Do not use this skill for:
- Sprint-level user story sizing, velocity tracking, or daily standup blockers (use `scrum-planning-and-refinement` and `scrum-daily-sync`).
- Authoring technical PRDs or BDD test criteria (use `create-prd`).
- Structuring multi-horizon product problem roadmaps (use `now-next-later-roadmaps`).
- Cascading enterprise-wide 5-10 year strategic intent hierarchies (use `decision-stack-governance`).

## Trigger cues

- Explicit references: `outcome-okrs-and-cadence`, `outcome OKRs`, `radical focus OKRs`, `Christina Wodtke OKRs`, `4 quadrant OKR canvas`, `Monday commitments Friday wins`, `quarterly OKR scoring`.
- Request phrases: "set up outcome-driven OKRs", "create a Radical Focus OKR canvas", "structure our quarterly OKRs with health metrics", "run Monday commitments and Friday wins cadence", "score and grade our quarterly Key Results".

## Routing boundary

- Primary for OKR goal setting, 4-Quadrant canvas design, confidence tracking, health metric guardrails, and execution cadence rituals.
- Route upstream strategic intent cascading to `decision-stack-governance`.
- Route roadmap horizon alignment to `now-next-later-roadmaps`.
- Route sprint-level epic slicing to `prd-to-tickets` and sprint ceremonies to `scrum-planning-and-refinement`.

## Inputs required

1. **Strategic Intent / Business Priorities**: Higher-level strategic goals from leadership (`decision-stack-governance`).
2. **Current Baseline Metrics**: Quantitative baselines for key performance and operational health indicators.
3. **Team Capacity & Constraints**: Current pod focus and cross-functional dependencies.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Step 1: Formulate 1 Single Inspirational Objective (Radical Focus)**:
   - Must be **qualitative**, **inspirational**, **time-bound**, and **actionable by the team**.
   - Example: *"Establish our developer platform as the undisputed standard for real-time webhooks in North America."*
   - Avoid bland metric aggregations or feature lists.
3. **Step 2: Engineer 3 Quantitative Outcome Key Results (50% Stretch)**:
   - Frame strictly as **outcomes** (measurable behavior or business impact), NOT output tasks or deliverables.
   - Format: `[Metric Name] from [Baseline] to [Target]`.
   - Set confidence baseline at **5/10 (50%)**: an ambitious stretch target that is difficult but plausible.
   - KR1: Primary value metric (e.g. usage/activation).
   - KR2: Quality or retention metric (e.g. churn/latency).
   - KR3: Business or efficiency metric (e.g. expansion revenue/CAC).
4. **Step 3: Build the 4-Quadrant Radical Focus Canvas**:
   - **Quadrant 1 (Top-Left): Objective & Key Results**: 1 Objective, 3 KRs, and current weekly confidence ratings (e.g. 5/10).
   - **Quadrant 2 (Bottom-Left): Health Metrics (Keep the Lights On)**: 2–4 vital operational metrics that must NOT be sacrificed (e.g. code quality, team burnout, system uptime, customer NPS) with Green/Yellow/Red status.
   - **Quadrant 3 (Top-Right): This Week's Priorities**: Ruthlessly prioritized initiatives that move KRs this week. Enforce strict limits: **P1** (Must-do, max 3) and **P2** (Should-do, max 2).
   - **Quadrant 4 (Bottom-Right): Next 4 Weeks Pipeline**: Upcoming cross-functional milestones, technical dependencies, or lead-time experiments.
5. **Step 4: Execute the Weekly Rhythm of Execution**:
   - **Monday Commitments (30m)**:
     - Review progress on OKRs and adjust confidence scores (e.g. 5/10 $\rightarrow$ 6/10 with rationale).
     - Check Health Metrics (if Red/Yellow, redirect priorities to repair health).
     - Commit to this week's P1 (must do) and P2 (should do) items.
   - **Friday Wins (30m)**:
     - Demo working software and show metric movement.
     - Celebrate cross-functional contributions and team momentum.
6. **Step 5: Grade & Retrospect at Quarter End**:
   - Score each KR from **0.0 to 1.0** (Target sweet spot is **0.7**; 1.0 means goal was under-ambitious; <0.4 indicates breakdown in execution or flawed assumptions).
   - Conduct blameless retrospective to capture learnings before setting next cycle's OKRs.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- [ ] Exactly 1 qualitative, inspirational Objective per squad/cycle (Radical Focus).
- [ ] Exactly 3 quantitative outcome-based Key Results with explicit baseline, target, and 5/10 confidence ratings.
- [ ] Complete 4-Quadrant Canvas populated (Objective & KRs, Health Metrics, P1/P2 Weekly Priorities, Next 4 Weeks Pipeline).
- [ ] Zero output tasks (e.g. "Ship X", "Build Y") disguised as Key Results.
- [ ] Clear Monday Commitments and Friday Wins operational rhythm specified.

## Output format

- **4-Quadrant Radical Focus Canvas**: Rendered in structured markdown table or quadrant grid.
- **OKR Specification Table**: Objective, KRs, Baselines, Targets, Confidence, and Measurement Instrument.
- **Health Metrics Dashboard**: 2–4 guardrail metrics with current status and alert thresholds.
- **Weekly Cadence SOP**: Agendas and protocols for Monday Commitments and Friday Wins.
