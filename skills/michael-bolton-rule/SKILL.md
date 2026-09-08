---
name: michael-bolton-rule
description: "Enforce 4-part intent delegation framing outcomes, constraints, measures, and time horizons."
---

# Rule: The Michael Bolton Doctrine of Direction & Delegation

> [!IMPORTANT]
> **The Prime Directive**: *"Your job is not to plan work. Your job is to make work work."*  
> Grounded in **Mintzberg** (real-time steering & unblocking), **Deming** (variation control & systems quality checks), and **March** (70/20/10 exploit/improve/explore portfolio allocation).
>
> **Governance Triad**:
> - **Doctrine**: `/michael-bolton-rule` (This skill — Intent framing & Deming failure audits).
> - **Lifecycle Orchestrator**: [`/michael-bolton-pod-conductor`](../michael-bolton-pod-conductor/SKILL.md) (5-Movement pod execution).
> - **Concurrency & Runtime**: [`/swarm-rules`](../swarm-rules/SKILL.md) (Atomic task claims & race condition prevention).

---

## When to use

Use this skill when structuring agent delegation, governing execution feedback loops, or diagnosing why a subagent or system failed:
- Framing tasks using the **4-Part Intent Architecture**: Outcome, Constraints, Measures, Time-horizon.
- Applying the **Deming System Failure Checklist** before blaming subagent effort.
- Enforcing March's **70% Exploit / 20% Improve / 10% Explore** resource allocation.

## When not to use

Do not use this skill for:
- Direct low-level code implementation (use `developer-development-rules`).
- Single-page UI styling or visual design (use `design-system-rules`).

## Trigger cues

- Request mentions: `michael-bolton-rule`, `standard work`, `deming first`, `system failure checklist`, `delegation check`, `outcome constraints measures`, `70 20 10 portfolio`.

## Inputs required

1. **Delegation Goal / Assignment**: Task description and expected result.
2. **Current Constraints & Non-Negotiables**: Guardrails, blast radius, forbidden shortcuts.
3. **Verification Measures**: Binary success criteria and test suites.
4. **Time-Horizon**: Current sprint cadence or lifecycle phase.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Structure Every Delegation Across 4 Dimensions**:
   - **Outcome**: Verifiable artifacts and concrete system state.
   - **Constraints**: Guardrails, anti-patterns, context boundaries.
   - **Measures**: Deterministic binary evaluation criteria.
   - **Time-horizon**: Explicit phase milestones.
3. **Execute Deming-First Failure Triage**:
   - If an agent produces drifting or failing work, check:
     1. *Input Integrity*: Was the input prompt/schema ambiguous?
     2. *Feedback Loops*: Did the agent have access to fast local test feedback?
     3. *Standard Work*: Was a concrete template or interface contract provided?
     4. *Process Variation*: Did the agent attempt too many unconstrained edits?
4. **Maintain March 70/20/10 Portfolio Balance**:
   - 70% Core value delivery / 20% System debt reduction / 10% De-risking spikes.
## Quality Invariants: Andon Cord & Small-Batch Governance

### 1. The Executive Andon Cord (Stop-the-Line)
- Deming quality demands stopping the line the instant a defect or unhandled variance appears.
- Pod Conductors and Managers must never incentivize agents to "push through" broken feedback loops or ambiguous constraints.
- When an Andon Cord is pulled:
  - Audit the 4 Deming Failure dimensions (*Input*, *Feedback*, *Standard Work*, *Process Variation*).
  - Repair the system constraint before restarting execution.

### 2. Small-Batch Flow Enforcement (<200 LOC per Task Batch)
- Work must be decomposed into high-frequency, single-piece flow increments ($\le 200$ LOC).
- Any delegation package projected to exceed 200 lines must be recursively decomposed using story splitting or interface decoupling before worker assignment.
