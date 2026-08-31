---
name: prd-to-tickets
description: "Trigger: prd to tickets, prd to issues, spec to tickets, generate tickets from prd, break prd into tasks, tracer bullet tickets, decompose spec into issues, prd to kanban, prd to linear, prd to github issues, now next later tickets. Scope: Translates PRDs, functional specs, and architecture plans into tracer-bullet vertical slice tickets with explicit blocking edge DAGs, INVEST sizing, Gherkin BDD acceptance criteria, and Definition of Ready (DoR) gates. Technology-agnostic: compiles cleanly to Markdown Kanban (kanban.md), GitHub Issues (gh issue create CLI), Linear, Jira, Notion, Obsidian, or Now/Next/Later horizons. Boundary: Excludes writing the PRD from scratch (use create-prd) or direct code execution (use developer-development-rules)."
---

# Rule: PRD to Tracer-Bullet Tickets Compiler

> [!IMPORTANT]
> **Ethos & Lineage**: Synthesizes **Matt Pocock** (*Tracer-Bullet Vertical Slices & Blocking Edges*), **Marty Cagan** (*Outcome vs. Feature Factory & 4 Product Risks*), **John Cutler** (*Flow & Value Trees*), **Jeff Patton** (*Story Mapping*), **Mike Cohn** (*SPIDR Slicing*), and **Janna Bastow** (*Now/Next/Later*).
>
> **The Prime Directive**: *"Make the change easy, then make the easy change."* Decompose specs into narrow, verifiable **tracer-bullet vertical slices** that cut through every layer (DB $\rightarrow$ API $\rightarrow$ UI $\rightarrow$ Test), declare strict **blocking edges** (DAG), and fit into a single agent context window ($<200$ LOC diff).

---

## When to use

Use this skill to compile a PRD, spec, or architectural plan into an actionable ticket backlog:
- Decomposing complex PRDs into **tracer-bullet vertical slices** with explicit dependencies (`blocked_by` / `blocks`).
- Sizing tickets for single-context-window autonomous execution ($<200$ LOC diffs for `ralph.sh` or subagents).
- Structuring wide refactors via **Expand-Contract** phases rather than broken horizontal slices.
- Generating technology-agnostic tickets for **Markdown Kanban (`kanban.md`)**, **GitHub Issues (`gh issue create`)**, **Linear**, **Jira**, **Notion**, **Obsidian**, or **Now/Next/Later** boards.
- Attaching executable **BDD/Gherkin acceptance criteria** and **Definition of Ready (DoR)** gates to every issue.

## When not to use

Do not use this skill for:
- Authoring the initial PRD or problem scope (use `create-prd`).
- Storyboarding UI during a design sprint (use `design-storyboard-decide`).
- Direct implementation of code and test suites (use `developer-test-driven-development` or `developer-development-rules`).

## Trigger cues

- Request mentions: `prd to tickets`, `prd to issues`, `spec to tickets`, `generate tickets from prd`, `break prd into tasks`, `tracer bullet tickets`, `decompose spec into issues`, `prd to kanban`, `prd to linear`, `prd to github issues`, `now next later tickets`.

## Inputs required

1. **Source Document**: A completed PRD (`PRD.md`), functional specification, or architectural RFC.
2. **Target Tracker / Destination Format**: Markdown Kanban, GitHub Issues, Linear, Notion, Obsidian, or Now/Next/Later.
3. **Repository Context & ADRs**: Existing architectural constraints, tech stack conventions, and domain glossary.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Extract Problem, Outcome & Invariants**:
   - Ingest PRD goals, non-goals, and acceptance criteria.
   - Separate core value outcomes (Marty Cagan / John Cutler) from implementation details.
3. **Identify Pre-factoring & Expand-Contract Needs**:
   - Check if the spec requires pre-factoring existing code (*"Make the change easy first"*).
   - If a wide refactor touches shared interfaces, sequence it as **Expand $\rightarrow$ Migrate $\rightarrow$ Contract** tickets.
4. **Draft Tracer-Bullet Vertical Slices**:
   - Apply SPIDR heuristics (Spikes, Paths, Interfaces, Data, Rules).
   - Ensure every slice cuts end-to-end (Schema $\rightarrow$ Logic/API $\rightarrow$ UI $\rightarrow$ Tests) and delivers verifiable value in isolation.
   - Size each ticket to fit in a single execution session ($\le 200$ LOC diff / $\le 3-5$ story points).
5. **Declare Explicit Blocking Edges (DAG)**:
   - For every ticket, declare `blocked_by: [TICKET_IDS]` and `blocks: [TICKET_IDS]`.
   - Tickets with zero blockers are immediately actionable in parallel.
6. **Compile to Target Tracker Schema**:
   - Render as formatted Markdown Kanban, automated `gh issue create` bash script, or structured JSON for Linear/Jira/Notion.

## Completion gate

- [ ] All PRD features mapped to vertical tracer-bullet tickets.
- [ ] Explicit dependency DAG (`blocked_by` / `blocks`) defined for every ticket.
- [ ] Each ticket contains BDD/Gherkin acceptance criteria and Definition of Ready (DoR) checklist.
- [ ] Wide refactors sequenced as Expand-Contract batches.
- [ ] Output formatted cleanly in the requested tracker format.
