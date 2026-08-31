# PRD to Tickets: Tracer-Bullet Decomposition & DAG Compiling

## 1. Cross-Skill Synthesis & Foundational Principles

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           CROSS-SKILL INTEGRATION MATRIX                     │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ 1. Matt Pocock & SPIDR        │ Tracer-bullet vertical slices + Blocking DAG │
│ 2. developer-development-rules│ Pre-factoring + Unhappy-Path-First contracts │
│ 3. swarm-rules & Bolton       │ Atomic file isolation + <200 LOC + Andon Cord│
│ 4. developer-tdd              │ Red-Green-Refactor test matrix per ticket    │
│ 5. proven-product-spec        │ [Proven / Better / New] taxonomy tagging     │
│ 6. developer-code-review-rules│ Verification evidence + Review readiness     │
└───────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 2. Vertical Slicing vs. Wide Refactor Rules

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ 1. TRACER-BULLET VERTICAL SLICE (Standard Feature Work)                      │
│    Cuts through Schema -> API -> UI -> Automated Tests in ONE ticket.        │
│    Demoable and deployable on its own.                                       │
├──────────────────────────────────────────────────────────────────────────────┤
│ 2. EXPAND-CONTRACT PATTERN (Wide Refactors & Breaking Schema Changes)        │
│    Ticket A [Expand]: Add new column/interface beside old. (CI Green)       │
│    Ticket B [Migrate]: Migrate call sites in bounded batches. (CI Green)     │
│    Ticket C [Contract]: Delete old deprecated interface once unused.         │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. The Unified Tracer-Bullet Ticket Schema

```markdown
### [TICKET-ID]: [Taxonomy Tag] Title of Tracer Bullet Slice
- **Horizon / Column**: [Now / Next / Later] OR [Backlog / Ready / In Progress / Done]
- **Story Points**: [1, 2, 3, 5] (Estimated Diff: <= 200 LOC)
- **Blocked By**: [TICKET-XXX] (or None - Ready to Start)
- **Blocks**: [TICKET-YYY]
- **Taxonomy**: [Proven: Standard Pattern] | [Better: Friction Reduction] | [New: Novel Spike]
- **Target File Boundaries**: `src/features/auth/*`, `tests/auth/*` (Zero overlap with concurrent tickets)

#### 1. Outcome & Intent (Marty Cagan / John Cutler)
- **Problem Solved**: Specific customer friction or system capability unlocked.
- **Non-Goals**: Explicit out-of-scope items deferred to future tickets.

#### 2. Vertical Scope (Matt Pocock Tracer Bullet)
- [ ] **Schema / DB**: Data model migration or cache schema.
- [ ] **API / Engine**: Core business logic, validation, and error contracts.
- [ ] **UI / Interaction**: Visual components, loading skeleton, empty states, and WCAG AA contrast.
- [ ] **Unhappy Path**: Error toasts, timeouts, network retry with jitter, fallback boundaries.

#### 3. TDD Test Matrix (Red-Green-Refactor)
- **Unit Tests**: Pure function domain invariants and edge-case boundary checks.
- **Integration Tests**: API route contracts, database queries, and third-party adapter mocks.
- **E2E / Smoke Tests**: Golden path user workflow.

#### 4. Executable BDD Acceptance Criteria (Gherkin)
```gherkin
Scenario: Happy path execution
  Given <precondition>
  When <action>
  Then <verifiable_result>

Scenario: Unhappy path / Boundary validation
  Given <invalid_input_or_network_timeout>
  When <action_attempted>
  Then <graceful_error_toast_and_fallback>
```

#### 5. Multi-Agent Safety & Andon Cord Trigger (swarm-rules)
- **Andon Cord Triggers**: Halt execution immediately if:
  - Upstream schema contract is broken or missing.
  - Test suite failure cannot be resolved within 3 TDD cycles.
  - Diff projection exceeds 200 lines of code.

#### 6. Definition of Done (DoD) Verification Gate
- [ ] 100% automated test pass rate (Unit, Integration, E2E).
- [ ] Bounded diff (<= 200 LOC). Zero dead code or unhandled lint/type errors.
- [ ] Deterministic evidence artifact logged (CLI test report or DOM verification).
```

---

## 4. Compilation Targets

### A. Markdown Kanban (`kanban.md`)
Structures tickets under:
- `## Backlog`
- `## Ready (Unblocked DAG Nodes meeting DoR)`
- `## In Progress (WIP Limited)`
- `## Review & QA (DoD Verification)`
- `## Done (Shipped Increment)`

### B. GitHub Issues CLI (`generate_issues.sh`)
```bash
gh issue create   --title "TICKET-01: [Proven] Payment Gateway Adapter & DB Table"   --body-file "tickets/ticket-01.md"   --label "phase:foundation,type:vertical-slice,pts:3"
```

### C. Now / Next / Later Roadmap Matrix (Janna Bastow)
- **Now (Immediate Execution)**: Finely sliced, 0 blockers, meets DoR, bounded file paths.
- **Next (Upcoming Sprints)**: Coarsely sliced, candidate dependencies mapped.
- **Later (Strategic Themes)**: Unestimated problem scopes and exploratory spikes.
