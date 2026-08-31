---
name: prd-to-tickets
description: "Trigger: prd to tickets, prd to issues, spec to tickets, generate tickets from prd, break prd into tasks, tracer bullet tickets, decompose spec into issues, prd to kanban, prd to linear, prd to github issues, now next later tickets. Scope: Translates PRDs, functional specs, and architecture plans into tracer-bullet vertical slice tickets with explicit blocking edge DAGs, INVEST sizing, Gherkin BDD acceptance criteria, and Definition of Ready (DoR) gates. Ingests and enforces core doctrines: developer-development-rules (unhappy path, pre-factoring), swarm-rules & michael-bolton-rule (atomic file isolation, <200 LOC diffs, Andon Cord triggers), developer-test-driven-development (Red-Green-Refactor test assertions), developer-code-review-rules (review readiness), and proven-product-spec (Proven/Better/New taxonomy). Technology-agnostic: compiles cleanly to Markdown Kanban (kanban.md), GitHub Issues (gh issue create CLI), Linear, Jira, Notion, Obsidian, or Now/Next/Later horizons. Boundary: Excludes writing the PRD from scratch (use create-prd) or direct code execution (use developer-development-rules)."
---

# Rule: PRD to Tracer-Bullet Tickets Compiler

> [!IMPORTANT]
> **Cross-Skill Synthesis & Lineage**:
> 1. **Matt Pocock**: Tracer-bullet vertical slices cutting across all layers (DB $\rightarrow$ API $\rightarrow$ UI $\rightarrow$ Test) and strict blocking edges (DAG).
> 2. [`/developer-development-rules`](../../../engineering/development-and-quality/developer-development-rules/SKILL.md): Pre-factoring (*"Make the change easy first"*), Unhappy-Path-First failure contracts, and Engineering Definition of Done (DoD).
> 3. [`/swarm-rules`](../../orchestration/swarm-rules/SKILL.md) & [`/michael-bolton-rule`](../../orchestration/michael-bolton-rule/SKILL.md): Atomic file isolation (zero write collisions), Small-Batch Slicing ($<200$ LOC diffs), and explicit **Andon Cord (Stop-the-Line)** triggers.
> 4. [`/developer-test-driven-development`](../../../engineering/development-and-quality/developer-test-driven-development/SKILL.md): Red-Green-Refactor sequence with executable BDD/Gherkin acceptance criteria.
> 5. [`/proven-product-spec`](../proven-product-spec/SKILL.md) & [`/create-prd`](../create-prd/SKILL.md): **[Proven / Better / New]** taxonomy tagging, non-goals, and outcome metrics.
> 6. [`/developer-code-review-rules`](../../../engineering/development-and-quality/developer-code-review-rules/SKILL.md): Verification evidence artifacts and review-readiness gates.

---

## When to use

Use this skill to compile any PRD, functional spec, or architectural plan into an actionable ticket backlog:
- Decomposing complex PRDs into **tracer-bullet vertical slices** with explicit dependencies (`blocked_by` / `blocks`).
- Sizing tickets for single-context-window autonomous execution ($<200$ LOC diffs for `ralph.sh` or subagents).
- Tagging tickets with the **Proven / Better / New** innovation taxonomy.
- Structuring wide refactors via **Expand-Contract** phases rather than broken horizontal slices.
- Defining bounded **atomic file footprints** and **Andon Cord triggers** for multi-agent swarm safety.
- Generating technology-agnostic tickets for **Markdown Kanban (`kanban.md`)**, **GitHub Issues (`gh issue create`)**, **Linear**, **Jira**, **Notion**, **Obsidian**, or **Now/Next/Later** boards.
- Attaching executable **BDD/Gherkin scenarios**, **TDD test plans**, and **Definition of Ready (DoR)** gates to every issue.

## When not to use

Do not use this skill for:
- Authoring the initial PRD or problem scope from scratch (use `create-prd`).
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
2. **Extract Problem, Outcome & Invariants (`create-prd`)**:
   - Ingest PRD goals, non-goals, anti-personas, and acceptance criteria.
   - Tag each feature area with the **[Proven / Better / New]** taxonomy from `proven-product-spec`.
3. **Identify Pre-factoring & Expand-Contract Needs (`developer-development-rules`)**:
   - Check if the spec requires pre-factoring existing code (*"Make the change easy, then make the easy change"*).
   - If a wide refactor touches shared interfaces or database schemas, sequence it as **Expand $\rightarrow$ Migrate $\rightarrow$ Contract** tickets.
4. **Draft Tracer-Bullet Vertical Slices (Matt Pocock + SPIDR)**:
   - Apply SPIDR heuristics (Spikes, Paths, Interfaces, Data, Rules).
   - Ensure every slice cuts end-to-end (Schema $\rightarrow$ Logic/API $\rightarrow$ UI $\rightarrow$ Tests) and delivers demonstrable value.
   - Enforce **Unhappy Path First**: Every ticket must specify error states, fallbacks, and boundary validations.
   - Enforce **Small-Batch Slicing**: Sized strictly $\le 200$ LOC diff / $\le 3-5$ story points to fit in a single agent context window (`swarm-rules`).
5. **Declare Multi-Agent Safety & Blocking Edges (`swarm-rules` + `michael-bolton-rule`)**:
   - Declare explicit dependency edges (`blocked_by: [TICKET_IDS]`, `blocks: [TICKET_IDS]`).
   - Define the bounded **Target File Paths** for each ticket to ensure atomic file ownership and zero write collisions.
   - Define explicit **Andon Cord (Stop-the-Line)** conditions for unexpected breaks.
6. **Attach TDD & Verification Gates (`developer-test-driven-development` + `developer-code-review-rules`)**:
   - Attach executable BDD/Gherkin scenarios (`Given / When / Then`).
   - Specify required Red-Green-Refactor test matrix (Unit, Integration, E2E).
   - Include the 5-point Engineering **Definition of Done (DoD)** checklist.
7. **Compile to Target Tracker Schema**:
   - Render as formatted Markdown Kanban, automated `gh issue create` bash script, or structured JSON for Linear/Jira/Notion.

## Completion gate

- [ ] All PRD features mapped to vertical tracer-bullet tickets.
- [ ] Explicit dependency DAG (`blocked_by` / `blocks`) defined for every ticket.
- [ ] Each ticket contains Proven/Better/New tag, bounded file paths, BDD/Gherkin criteria, and DoD gate.
- [ ] Wide refactors sequenced as Expand-Contract batches.
- [ ] Output formatted cleanly in the requested tracker format.
