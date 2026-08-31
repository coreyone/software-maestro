---
name: michael-bolton-pod-conductor
description: "Trigger: michael-bolton-pod-conductor, pod conductor, pod orchestrator, lifecycle conductor, autonomous pod, agent pod director. Scope: Autonomous Multi-Agent Pod Conductor operating under the Michael Bolton Rule. Oversees lifecycle initiation, task routing, intent verification, and completion synthesis. Boundary: Excludes single-agent tactical debugging."
---

# Rule: Michael Bolton Product Pod Conductor & Lifecycle Baton

> [!IMPORTANT]
> **Foundation**: This skill embeds and enforces `/michael-bolton-rule` ([`product/michael-bolton-rule/SKILL.md`](../michael-bolton-rule/SKILL.md)) across the entire cross-functional product lifecycle.
> **The Prime Directive**: *"Your job is not to plan work. Your job is to make work work."*
> - Create **direction** without micromanagement (Outcome + Constraints + Measures + Time-horizon).
> - Design the **system & feedback loops** before judging subagent effort (Deming-first System Failure Checklist).
> - Delegate **continuously** across Mintzberg real-time roles (Decider, Connector, Information Hub, Coach).
> - Balance execution with learning using March's **70% Exploit / 20% Improve / 10% Explore** portfolio.
> - Enforce multi-agent concurrency & atomic task isolation via `/swarm-rules` ([`product/swarm-rules/SKILL.md`](../swarm-rules/SKILL.md)).

---

## When to use

Use this skill to conduct an end-to-end product development lifecycle across specialized functional agent skills:
- Leading a full cross-functional product pod (`Data Scientist`, `Staff PM`, `Lead Designer`, `Principal Engineer`, `PMM Lead`) to design, specify, build, and ship a product or feature.
- Spawning and supervising autonomous subagents with rigorous intent framing (`Outcome`, `Constraints`, `Measures`, `Time-horizon`).
- Managing structured artifact handoffs and gate approvals between empirical discovery, causal data sizing, UI design systems, contract-first engineering, and GTM release.
- Diagnosing and remediating subagent execution failures via the **Deming System Failure Checklist** rather than blaming subagents.

## When not to use

Do not use this skill for:
- Implementing a single isolated function or fixing a bug in one file (use `developer-development-rules` or `improve-codebase`).
- Designing high-level company strategic intents or multi-year portfolio roadmaps (use `decision-stack-governance`).
- Pure marketing copywriting without lifecycle orchestration (use `conversion-copywriting`).

## Trigger cues

- Request mentions: `michael-bolton-pod-conductor`, `orchestrate product pod`, `software lifecycle orchestra`, `conduct pod`, `full company product lifecycle`, `cross-functional handoff`, `PM design eng data PMM`, `autonomous software pod`, `delegate with outcome constraints measures`.
- Complex multi-disciplinary requests spanning data science validation, PRD product strategy, UI design, backend implementation, and GTM launch.

## Routing boundary

- Route single-task leadership principles to `michael-bolton-rule`.
- Delegate statistical quasi-experiments and metric investigations to `data-science-causal-inference` and `product-data-metric-investigation-triage`.
- Delegate PRD formulation to `create-prd` and `continuous-product-loop`.
- Delegate design systems and UI to `design-user-onboarding-ux`, `aesthetic-rules`, and `stitch-design`.
- Delegate architecture, TDD, and code implementation to `system-architecture-rules`, `developer-test-driven-development`, and `improve-codebase`.
- Delegate commercial positioning to `product-marketing-narrative` and `release-readiness-gtm`.

## Inputs required

1. **Product Area Mission / Problem Statement**: The raw customer or business opportunity.
2. **Target User Persona & Context**: Primary ICP and environment constraints.
3. **Core Business / North Star Objective**: Target metric, revenue impact, or strategic milestone.
4. **Execution Constraints**: Timebox, tech stack invariants, and safety boundaries.
5. **Source of truth**: [references/source.md](references/source.md) and [`product/michael-bolton-rule/references/source.md`](../michael-bolton-rule/references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Apply Bolton Intent Framing & Swarm Concurrency Rules for Every Subagent**:
   - Enforce the **Leader-Follower Axiom** (`swarm-rules`): Conductor alone manages global task state and synthesis; subagents execute assigned atomic tasks.
   - Enforce **Atomic File Claims**: Ensure no two subagents edit the same file concurrently.
   - For every task assigned to a subagent, explicitly structure the 4-part frame:
     - **Outcome**: Exact observable definition of success.
     - **Constraints**: Non-negotiable guardrails, forbidden actions, and context isolation.
     - **Measures**: Concrete verification test.
     - **Time-horizon**: Phase timebox or movement milestone.
   - For every task assigned to a subagent, explicitly structure:
     - **Outcome**: Exact observable definition of success (e.g. `opportunity_sizing_brief.md` with MDE and parallel trends check).
     - **Constraints**: Non-negotiable guardrails and forbidden actions (e.g. zero ungrounded metrics, no raw TWFE on staggered rollouts).
     - **Measures**: Concrete verification test (e.g. passes binary evals, unit tests 100% green, WCAG AA compliance).
     - **Time-horizon**: Phase timebox or movement milestone.
   - **Deming System Failure Rule**: If a subagent returns sub-par work, run the **System Failure Checklist** (ambiguous requirements? missing inputs? broken handoffs? missing checks?) and fix the prompt/system before re-dispatching.
3. **Orchestrate Movement 1: Empirical Grounding & Sizing (The Data Scientist & PM)**:
   - Spawn Data Science subagent with `data-science-causal-inference`, `product-data-metric-investigation-triage`, and `incentive-design-metric-trees`.
   - Deliverable: `opportunity_sizing_brief.md` (Baseline volume, MDE, causal identification strategy, metric tree inputs).
   - *Gate 1 Approval*: Verify statistical feasibility and opportunity size before committing engineering/design resources.
4. **Orchestrate Movement 2: Discovery, Behavioral Loops & PRD (The Staff PM & UX Lead)**:
   - Spawn PM subagent with `create-prd`, `ux-discovery-artifacts`, `behavioral-loops-retention-modeling`, and `strategic-tradeoffs-constraint-matrix`.
   - Deliverable: `PRD.md` with explicit non-goals, user journey, and habit loop triggers.
   - *Gate 2 Approval*: Verify clear customer problem framing and trade-offs before design/eng.
5. **Orchestrate Movement 3: Interface & Design System (The Product Designer)**:
   - Spawn Design subagent with `design-user-onboarding-ux`, `aesthetic-rules`, `design-system-rules`, and `chart-communication`.
   - Deliverable: `DESIGN.md` and UI specification with WCAG AA compliance, responsive tokens, and empty/loading states.
   - *Gate 3 Approval*: Verify cognitive friction-free UX and design token consistency.
6. **Orchestrate Movement 4: Contract-First Architecture & TDD Build (The Principal Eng & Analytics Eng)**:
   - Spawn Engineering subagent with `system-architecture-rules`, `api-design-guidelines`, `data-warehouse-semantic-layer`, and `developer-test-driven-development`.
   - Deliverable: Working, tested implementation code with API contracts, dbt marts, and passing unit/integration tests.
   - *Gate 4 Approval*: 100% passing tests, type-check, and zero security regressions.
7. **Orchestrate Movement 5: Verification, Release Gating & GTM Launch (The PMM & QA Lead)**:
   - Spawn PMM & Quality subagent with `product-marketing-narrative`, `release-readiness-gtm`, `observability-telemetry`, and `experimentation-hypothesis-engine`.
   - Deliverable: `gtm_positioning_brief.md`, Canary feature flag rollout plan, and post-launch causal evaluation schedule.
   - *Gate 5 Approval*: 100% green GTM release checklist and telemetry monitors active.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Full 5-movement sequence execution with Michael Bolton intent framing (Outcome + Constraints + Measures + Time-horizon).
- Clear functional role assignment across the pod (PM, Design, Eng, Data, PMM).
- Formal artifact handoff contracts between movements.
- Explicit blocking gate approvals and Deming system failure remediation.

## Output format

- **Executive Symphony Scorecard**: Pod roles, March 70/20/10 portfolio allocation, and lifecycle milestone.
- **Movement 1 Summary (Empirical Grounding)**: Data sizing, causal strategy, and baseline truth.
- **Movement 2 Summary (PRD & Loops)**: Problem statement, behavioral loop, and trade-offs.
- **Movement 3 Summary (Design System)**: UI architecture, interaction tokens, and accessibility.
- **Movement 4 Summary (Engineering Build)**: API contracts, dbt models, and TDD test evidence.
- **Movement 5 Summary (GTM & Rollout)**: Positioning hierarchy, feature flag rollout, and telemetry gates.
