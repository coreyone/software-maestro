# PRD to Tickets: Tracer-Bullet Decomposition & DAG Compiling

## 1. First Principles & Expert Lineage
- **Matt Pocock (Tracer Bullets & Blocking Edges)**: A tracer bullet cuts a thin but complete path through all architectural tiers. It is independently testable, demoable, and sized for a single agent context window ($<200$ LOC).
- **Marty Cagan (Empowered Outcomes)**: Tickets must preserve the *Why* and *Outcome*, not just mindless tasks. Tackle Value, Usability, Feasibility, and Viability risks upfront.
- **John Cutler (Flow & Value Trees)**: Map tickets to explicit customer feedback loops; keep WIP low; avoid the feature factory trap.
- **Jeff Patton (User Story Mapping)**: Sequence slices along the user journey backbone from walking skeleton to polished capability.
- **Mike Cohn (SPIDR Slicing)**: Split along Spikes, Paths, Interfaces, Data, and Rules.

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

## 3. Technology-Agnostic Ticket Template

```markdown
### [TICKET-ID]: Title of Tracer Bullet Slice
- **Horizon / Column**: [Now / Next / Later] OR [Backlog / Ready / In Progress / Done]
- **Story Points**: [1, 2, 3, 5]
- **Blocked By**: [TICKET-XXX] (or None - Ready to Start)
- **Blocks**: [TICKET-YYY]
- **Outcome / Value**: Why this slice matters to the customer or system.

#### Vertical Scope
- [ ] Schema / Data model changes
- [ ] API Endpoint / Business logic
- [ ] UI / Interaction surface
- [ ] Unit & Integration test suite

#### BDD Acceptance Criteria
```gherkin
Scenario: Happy path execution
  Given <precondition>
  When <action>
  Then <verifiable_result>
```

#### Definition of Ready (DoR) Gate
- [x] Sized <= 200 LOC diff
- [x] Zero unresolved external blockers
- [x] BDD scenarios unambiguous
```

## 4. Compilation Targets

### A. Markdown Kanban (`kanban.md`)
Structures tickets under `## Backlog`, `## Ready (Unblocked)`, `## In Progress`, `## Review/QA`, `## Done`.

### B. GitHub Issues CLI (`generate_issues.sh`)
```bash
gh issue create --title "TICKET-01: [Title]" --body "..." --label "phase:foundation,priority:high"
```

### C. Now / Next / Later Matrix
- **Now (Immediate Sprint)**: Finely sliced, 0 blockers, meets DoR.
- **Next (Upcoming Sprints)**: Coarsely sliced, candidate dependencies mapped.
- **Later (Strategic Themes)**: Unestimated problem scopes.
