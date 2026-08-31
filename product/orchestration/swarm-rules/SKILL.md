---
name: swarm-rules
description: "Trigger: swarm-rules, multi-agent swarm, subagent concurrency, atomic file ownership, andon cord stop the line, small batch slicing, subagent coordination. Scope: Multi-Agent Swarm Concurrency & Race Condition Prevention. Enforces 1 subagent per file, <200 LOC small-batch diffs, Andon Cord stops, and structured JSON messaging. Boundary: Excludes single-agent operations."
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
## Operational Invariants: Andon Cord & Small-Batch Slicing

### 1. Andon Cord Protocol (Stop-the-Line)
- **Trigger**: Any subagent or executor encountering an unexpected schema break, circular dependency, failing test suite with ambiguous root cause, missing credential, or >20% scope drift MUST immediately pull the Andon Cord.
- **Action**:
  1. Halt execution immediately. Do NOT forge ahead, guess missing parameters, or hallucinate mocks.
  2. Emit a structured incident payload to the Leader's inbox:
     ```json
     {
       "event": "ANDON_CORD_PULLED",
       "reason": "<precise_root_cause>",
       "last_known_good_state": "<commit_or_artifact_path>",
       "blocking_artifact": "<file_or_dependency>"
     }
     ```
  3. Wait for Leader unblock or explicit scope re-calibration before resuming work.

### 2. Small-Batch Slicing (<200 Lines of Code)
- **Invariant**: Subagents must slice implementation tasks such that individual diffs remain strictly $<200$ lines of changed code (excluding auto-generated lockfiles/fixtures).
- **Rationale**: Micro-batches minimize merge collisions, eliminate single-point failure risks in multi-agent concurrency, and allow immediate rollbacks without destabilizing adjacent streams.
