---
name: prd-to-tickets
description: "Decompose product requirement documents into tracer-bullet vertical slice tickets with dependency graphs."
---

# Rule: PRD to Tracer-Bullet Tickets Compiler

> [!IMPORTANT]
> **Orchestration & Quality Foundations**:
> 1. [`/god-marduk`](../../orchestration/god-marduk/SKILL.md): Enforces Infrastructure-First sequencing across 6 smart phases (`0: Scaffolding`, `1: Foundation`, `2: Mechanism`, `3: Interface`, `4: Hardening`, `5: Synthesis`).
> 2. [`/technical-language-rules`](../../../engineering/development-and-quality/technical-language-rules/SKILL.md): Applies ASD-STE100 and Google DevDocs writing standards ($\le 20$ words per procedural step, $\le 3$-noun stacks, imperative verbs, `because` instead of `since/as`, `after` instead of `once`).
> 3. **Matt Pocock**: Tracer-bullet vertical slices (DB $\rightarrow$ API $\rightarrow$ UI $\rightarrow$ Test) and strict blocking edges (DAG).
> 4. [`/developer-development-rules`](../../../engineering/development-and-quality/developer-development-rules/SKILL.md): Pre-factoring (*"Make the change easy first"*), Unhappy-Path-First failure contracts, and Engineering Definition of Done (DoD).
> 5. [`/swarm-rules`](../../orchestration/swarm-rules/SKILL.md) & [`/michael-bolton-rule`](../../orchestration/michael-bolton-rule/SKILL.md): Atomic file isolation, Small-Batch Slicing ($<200$ LOC diffs), and explicit **Andon Cord (Stop-the-Line)** triggers.
> 6. [`/developer-test-driven-development`](../../../engineering/development-and-quality/developer-test-driven-development/SKILL.md): Red-Green-Refactor sequence with executable BDD/Gherkin acceptance criteria.
> 7. [`/proven-product-spec`](../proven-product-spec/SKILL.md): **[Proven / Better / New]** taxonomy tagging and non-goals.

---

## When to use

Use this skill to compile any PRD, functional spec, or architectural plan into an actionable ticket backlog:
- Sequencing tickets across **God-Marduk 6-Phase Lifecycle** (`Phase 0` Scaffolding to `Phase 5` Synthesis).
- Enforcing **ASD-STE100 Technical Language Rules** across all ticket titles, descriptions, and acceptance criteria.
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

- Request mentions: `prd to tickets`, `prd to issues`, `spec to tickets`, `generate tickets from prd`, `break prd into tasks`, `tracer bullet tickets`, `decompose spec into issues`, `prd to kanban`, `prd to linear`, `prd to github issues`, `now next later tickets`, `god marduk phasing`.

## Inputs required

1. **Source Document**: A completed PRD (`PRD.md`), functional specification, or architectural RFC.
2. **Target Tracker / Destination Format**: Markdown Kanban, GitHub Issues, Linear, Notion, Obsidian, or Now/Next/Later.
3. **Repository Context & ADRs**: Existing architectural constraints, tech stack conventions, and domain glossary.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Apply God-Marduk 6-Phase Structure**:
   - Organize tickets into progressive lifecycle phases:
     - `Phase 0: Scaffolding` (Deploy baseline with active CI/CD).
     - `Phase 1: Foundation` (Data schemas, auth, and security contracts).
     - `Phase 2: Mechanism` (Core business logic engine without UI).
     - `Phase 3: Interface` (Responsive UI, design system tokens, empty states).
     - `Phase 4: Hardening` (Security audit, performance latency budgets, accessibility).
     - `Phase 5: Synthesis` (Telemetry verification, retrospective learning).
3. **Enforce ASD-STE100 Technical Prose Rules**:
   - Limit procedural instructions to $\le 20$ words per sentence.
   - Limit descriptive summaries to $\le 25$ words per sentence.
   - Use active voice, present tense, and imperative verbs (`Create`, `Add`, `Verify`).
   - Use `because` (not *since/as*), `after` (not *once*), `must/can` (not *may*), `before` (not *prior to*), and `to` (not *in order to*).
   - Restrict noun clusters to $\le 3$ consecutive nouns.
4. **Extract Problem, Outcome & Invariants (`create-prd` & `proven-product-spec`)**:
   - Ingest PRD goals, non-goals, and anti-personas.
   - Tag every ticket with **[Proven]** (commoditized patterns), **[Better]** (friction reduction), or **[New]** (novel spike).
5. **Identify Pre-factoring & Expand-Contract Needs (`developer-development-rules`)**:
   - Sequence pre-factoring tickets first (*"Make the change easy, then make the easy change"*).
   - Sequence breaking schema changes as **Expand $\rightarrow$ Migrate $\rightarrow$ Contract** batches.
6. **Draft Tracer-Bullet Vertical Slices (Matt Pocock + SPIDR)**:
   - Slice vertically through all tiers (Schema $\rightarrow$ Logic/API $\rightarrow$ UI $\rightarrow$ Tests).
   - Enforce **Unhappy Path First**: Specify error status codes, fallbacks, and boundary validations.
   - Enforce **Small-Batch Slicing**: Sized strictly $\le 200$ LOC diff / $\le 3-5$ story points (`swarm-rules`).
7. **Declare Multi-Agent Safety & Blocking Edges (`swarm-rules` + `michael-bolton-rule`)**:
   - Declare explicit dependency edges (`blocked_by: [TICKET_IDS]`, `blocks: [TICKET_IDS]`).
   - Define bounded **Target File Paths** to prevent concurrent write collisions.
   - Define explicit **Andon Cord (Stop-the-Line)** trigger criteria.
8. **Attach TDD & Verification Gates (`developer-test-driven-development` + `developer-code-review-rules`)**:
   - Attach executable BDD/Gherkin scenarios (`Given / When / Then`).
   - Specify required Red-Green-Refactor test matrix (Unit, Integration, E2E).
   - Include the 5-point Engineering **Definition of Done (DoD)** checklist.
9. **Compile to Target Tracker Schema**:
   - Render as formatted Markdown Kanban, automated `gh issue create` bash script, or structured JSON for Linear/Jira/Notion.

## Completion gate

- [ ] All PRD features mapped across God-Marduk Phases 0–5.
- [ ] 100% of prose complies with ASD-STE100 and Google DevDocs style rules.
- [ ] Explicit dependency DAG (`blocked_by` / `blocks`) defined for every ticket.
- [ ] Each ticket contains Proven/Better/New tag, bounded file paths, BDD criteria, and DoD gate.
- [ ] Output formatted cleanly in the requested tracker format.
