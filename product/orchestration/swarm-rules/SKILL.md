---
name: swarm-rules
description: "Trigger: swarm subagents, parallel agents, race conditions, atomic files, leader follower, multi-agent coordination, subagent concurrency, swarm execution. Scope: Multi-agent collaboration, task scoping, atomic file ownership, race condition prevention, structured JSON messaging, and lifecycle shutdown. Governed by michael-bolton-rule intent framing (Outcome, Constraints, Measures, Time-horizon) and orchestrated by michael-bolton-pod-conductor. Boundary: Excludes single-agent operations or low-level code syntax rules."
---

# Rule: Multi-Agent Swarm Operations & Concurrency Protocol

> [!IMPORTANT]
> **Governance Triad**: This skill operates as the **concurrency and runtime execution layer** in conjunction with:
> 1. [`/michael-bolton-rule`](../michael-bolton-rule/SKILL.md) (**Doctrine**): Mandates 4-part intent framing (`Outcome`, `Constraints`, `Measures`, `Time-horizon`) and Deming systems checks for every delegated task.
> 2. [`/michael-bolton-pod-conductor`](../michael-bolton-pod-conductor/SKILL.md) (**Orchestrator**): Directs the 5-Movement cross-functional lifecycle across PM, Design, Eng, Data, and PMM squads.

---

## When to use

Use this skill when spawning, coordinating, and managing multiple concurrent AI subagents:
- Enforcing the **Leader-Follower Axiom** (exactly 1 leader owns state; followers execute and report).
- Preventing race conditions and file collisions via **Atomic Task & File Ownership**.
- Managing token-efficient inter-agent communication via **Structured Inboxes** (JSON messages).
- Preventing zombie swarms through **Two-Phase Graceful Shutdown** and artifact preservation.

## When not to use

Do not use this skill for:
- Single-agent linear execution without subagents.
- Designing high-level product strategy or PRD specifications (use `product-management` or `create-prd`).
- Low-level programming syntax or test design (use `developer-development-rules` or `developer-test-driven-development`).

## Trigger cues

- Request mentions: `swarm-rules`, `swarm subagents`, `parallel agents`, `race conditions`, `atomic files`, `leader follower`, `multi-agent concurrency`, `coordinate subagents`.
- Scenarios where multiple subagents work in parallel across a repository.

## Inputs required

1. **Active Swarm Objective**: High-level goal and active lifecycle movement.
2. **Subagent Task Breakdown**: List of atomic tasks with assigned file ownership.
3. **Intent Frame for Each Agent**: Outcome, Constraints, Measures, Time-horizon (from `michael-bolton-rule`).
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Enforce the Leader-Follower Axiom**:
   - The Leader alone owns state, task decomposition, and final synthesis.
   - Teammates execute within bounded scope and report; they never unilaterally redefine scope.
3. **Enforce Atomic File Ownership & Context Isolation**:
   - Assign exactly one subagent per file/task. Zero concurrent writes to the same file.
   - Provide subagents *only* the specific files/context required ($<15\text{ KB}$ context footprint).
4. **Structure Agent Communication via JSON Inboxes**:
   - Use structured reports (`Status`, `Evidence`, `Action Taken`). Prefer targeted messages over broadcasts.
5. **Execute Two-Phase Graceful Shutdown**:
   - Harvest critical findings and diffs into permanent logs before terminating worker subagents.
