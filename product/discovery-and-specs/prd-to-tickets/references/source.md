# PRD to Tickets: Tracer-Bullet Decomposition & DAG Compiling

## 1. Cross-Skill Synthesis & Master Orchestration

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           CROSS-SKILL INTEGRATION MATRIX                     │
├───────────────────────────────┬──────────────────────────────────────────────┤
│ 1. god-marduk Phasing         │ 6-Phase Smart Sequencing (Phase 0 to Phase 5)│
│ 2. technical-language-rules   │ ASD-STE100 prose, <=20w steps, no ambiguity  │
│ 3. Matt Pocock & SPIDR        │ Tracer-bullet vertical slices + Blocking DAG │
│ 4. developer-development-rules│ Pre-factoring + Unhappy-Path-First contracts │
│ 5. swarm-rules & Bolton       │ Atomic file isolation + <200 LOC + Andon Cord│
│ 6. developer-tdd              │ Red-Green-Refactor test matrix per ticket    │
│ 7. proven-product-spec        │ [Proven / Better / New] taxonomy tagging     │
│ 8. developer-code-review-rules│ Verification evidence + Review readiness     │
└───────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 2. God-Marduk 6-Phase Smart Lifecycle

Every project ticket backlog organizes into these progressive phases:

| Phase | Phase Name | Focus | Objective |
| :--- | :--- | :--- | :--- |
| **0** | **Scaffolding** | Infrastructure & CI/CD Baseline | Deploy baseline application with active build and test pipelines. |
| **1** | **Foundation** | Data Models, Auth & Security | Implement schemas, database migrations, and security boundaries. |
| **2** | **Mechanism** | Core Business Logic Engine | Build domain logic and API contracts without UI dependencies. |
| **3** | **Interface** | User Experience & Visual Design | Construct responsive layouts, design tokens, and interaction flows. |
| **4** | **Hardening** | Performance, Security & A11y | Stress test systems, audit WCAG AA contrast, and check CVEs. |
| **5** | **Synthesis** | Telemetry, Docs & Retrospective | Verify analytics events and document lessons learned. |

---

## 3. ASD-STE100 Technical Language Rules

All ticket descriptions and steps must follow these standards:
- **Sentence length**: $\le 20$ words per procedural step; $\le 25$ words per descriptive sentence.
- **Noun stacks**: $\le 3$ consecutive nouns.
- **Imperative verbs**: Start steps with `Add`, `Create`, `Verify`, `Run`, `Update`, `Remove`.
- **Connector precision**:
  - Use **`because`** (never *since* or *as* to explain causes).
  - Use **`after`** (never *once* to express sequence).
  - Use **`must`** for requirements; use **`can`** for optional capabilities (never *may*).
  - Use **`before`** (never *prior to*).
  - Use **`to`** (never *in order to*).

---

## 4. The Unified Tracer-Bullet Ticket Schema

```markdown
### [TICKET-ID]: [Taxonomy Tag] Title of Tracer Bullet Slice
- **Phase**: [Phase 0: Scaffolding | Phase 1: Foundation | Phase 2: Mechanism | Phase 3: Interface | Phase 4: Hardening | Phase 5: Synthesis]
- **Horizon / Column**: [Now / Next / Later] OR [Backlog / Ready / In Progress / Done]
- **Story Points**: [1, 2, 3, 5] (Estimated Diff: <= 200 LOC)
- **Blocked By**: [TICKET-XXX] (or None - Ready to Start)
- **Blocks**: [TICKET-YYY]
- **Taxonomy**: [Proven: Standard Pattern] | [Better: Friction Reduction] | [New: Novel Spike]
- **Target File Boundaries**: `src/features/auth/*`, `tests/auth/*` (Zero write collisions)

#### 1. Outcome & Intent
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
