---
name: continuous-product-loop
description: "Trigger: continuous-product-loop, autonomous product loop, bounded goal envelope, explore exploit portfolio, autonomous TDD, multi-day product run. Scope: Autonomous Product Evolution Loop. Continuously strategizes, discovers, specifies, builds via TDD, and prunes across multi-day runs. Boundary: Excludes single-day sprint cadences."
---

# Continuous Product Loop

Autonomous, self-governing product evolution harness designed for long-running execution (1h to 72h).

Combines **Melissa Perri's Decision-Making Stack** (escaping the Build Trap), **Now-Next-Later outcome roadmapping**, **God-Marduk phased engineering** (Foundation → Mechanism → Interface → Hardening), **Subtractive Feature Pruning**, **Ralph Loop failure capture**, and **Continuous Meta-Skill Minting**.

---

## 1. Core Doctrine & Bounded Goal Envelope

```
┌────────────────────────────────────────────────────────────────────────┐
│ OUTER GUARDRAIL: Bounded Time / Cycle Envelope (e.g. 3h, 12h, 24h, 72h) │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ INNER ENGINE: Goal-Mode Relay Loop (Continuous Autonomy)        │   │
│   │                                                                │   │
│   │   [Cycle 1: Exploit (70%)] ──► TDD ──► Hardening ──► Evidence  │   │
│   │          │                                                     │   │
│   │          ▼ (Auto-Schedule Next Baton via `schedule`)           │   │
│   │   [Cycle 2: Prune (20%)]   ──► Simplify UI ──► Check Regress   │   │
│   │          │                                                     │   │
│   │          ▼ (Auto-Schedule Next Baton via `schedule`)           │   │
│   │   [Cycle 3: Explore (10%)] ──► Spike Test ──► Meta-Skill Mint  │   │
│   │          │                                                     │   │
│   │          ▼                                                     │   │
│   │   [Budget Check: Elapsed < Max Duration?]                      │   │
│   └──────────┬─────────────────────────────────────────────────────┘   │
│              │                                                         │
│              ▼ (When Budget Exhausted)                                 │
│   [Clean Landing Synthesis: walkthrough.md + Git Commit + Pause]       │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Inner Goal Engine:** Never stop after one feature. When an initiative passes verification, immediately commit, archive cycle history, write the next baton, and advance the roadmap.
2. **Outer Budget Guardrail:** Bounded by `max_duration_hours` (e.g. 3h Sprint, 12h Overnight, 72h Marathon) in `.product-loop/state.json`.
3. **Clean Landing:** When the envelope expires, finish the active phase cleanly, emit a synthesis report, and pause without breaking git state.

---

## 2. Trigger Cues & Routing Boundaries

### Trigger Cues
- User requests: "run continuous product loop", "autonomous product improvement", "work autonomously for hours/days", "build trap loop", `/continuous-product-loop`.
- Long-running autonomous goals: "evolve the product autonomously", "improve codebase and features overnight", "run 10 product cycles".
- Invocations with time parameters: `--duration 3h`, `--duration 24h`, `--cycles 6`.

### When to Use
- You need an autonomous, multi-hour engineering agent that builds, tests, refactors, prunes, and documents without human intervention.
- The project needs disciplined product evolution guided by measurable customer outcomes rather than random feature spam.

### When NOT to Use
- Simple, one-off targeted tasks (e.g., "fix this CSS bug", "add one test case", "format this JSON"). Use standard tactical skills directly.
- Ambiguous architectural refactors where human design sign-off is required before any code can be touched.

---

## 3. The 8-Phase Autonomous Lifecycle

Every cycle runs through the 8-phase state machine. Each phase enforces strict exit criteria:

| Phase | Phase Name | Primary Local Skill | Key Deliverables & Exit Criteria |
| :--- | :--- | :--- | :--- |
| **0** | **Strategy & Envelope Check** | `product-strategy-outcome-vision`, `god-marduk` | Validated strategy sentence; check elapsed time vs. envelope; select top item from Now-Next-Later; load `critical-patterns.md`. |
| **1** | **Discovery & Problem Framing** | `ux-discovery-artifacts`, `ask-a-product-expert` | JTBD, target persona, friction point, and measurable target condition baseline established. |
| **2** | **Market & Competitor Spec** | `proven-product-spec` | Benchmark proven solutions; categorize into Proven / Better / New; define non-goals and subtractive targets. |
| **3** | **Spec & Press Memo** | `create-prd`, `product-management-press-memo` | PRD saved to `tasks/prd-*.md`; launch press memo drafted; Strategy Smell Check passed. |
| **4** | **God-Marduk Stage 0-1 (Foundation)** | `god-marduk`, `data-persistence-caching` | Low-level primitives: schemas defined, migrations tested (expand-contract), auth secured, env vars mounted via 1Password. |
| **5** | **God-Marduk Stage 2-3 (Mechanism & UI)** | `developer-test-driven-development`, `aesthetic-rules`, `design-system-rules` | Engine tests written (Red) and satisfied (Green); UI built using design tokens with resilient empty/error states (or code pruned). |
| **6** | **God-Marduk Stage 4 (Hardening & Review)** | `developer-code-review-rules`, `developer-security` | Security audit passed; timeouts/circuit breakers configured; zero regressions across full test suite. |
| **7** | **Synthesis, Meta-Skill Minting & Relay** | `ralph-loop`, `compound-learning`, `continuous-learning`, `schedule` | Ralph retrospective completed; solution docs captured; skills minted; budget checked; next baton scheduled. |

---

## 4. God-Marduk Execution Hierarchy (Zero Floating Abstractions)

Never write UI components on unverified assumptions. Strictly follow God-Marduk's dependency ordering:

```
  [Stage 0: Scaffolding]    ──► Infra, deployment targets, env baseline (1Password MCP)
            │
  [Stage 1: Foundation]     ──► Low-level primitives: DB schemas, migrations, auth boundaries
            │
  [Stage 2: Mechanism]      ──► Core logic & engine implemented via strict TDD (No UI)
            │
  [Stage 3: Interface]      ──► UI connected to engine using design tokens & WCAG AA standards
            │
  [Stage 4: Hardening]      ──► Security audits, circuit breakers, timeouts, bundle checks
            │
  [Stage 5: Synthesis]      ──► Memory pipeline (Capture → Stabilize → Store → Retrieve → Update)
```

### March's 70/20/10 Portfolio Governance
Every 10 cycles must adhere to:
- **70% Exploit:** High-certainty delivery of validated roadmap features.
- **20% Improve:** Subtractive feature pruning, refactoring, and friction elimination.
- **10% Explore:** Timeboxed spike experiments to reduce technical/market uncertainty.

---

## 5. Subtractive & Pruning Engine ("Marie Kondo Doctrine")

Continuous product improvement mandates removing clutter as aggressively as adding features:
1. **Flow Streamlining:** Consolidate multi-step wizards into 1-step direct actions with smart defaults.
2. **Dead Code & Flag Pruning:** Purge obsolete feature flags, unreferenced components, and orphan API endpoints.
3. **Cognitive Noise Reduction:** Eliminate redundant buttons, inconsistent badges, and low-contrast labels.
4. **Dependency Diet:** Strip heavy unused packages; replace with standard web/Node primitives.

---

## 6. Ralph Loop & Compound Learning Engine

### Ralph Loop (Failures Are Data)
When bugs, race conditions, or test failures occur, follow the Ralph SOP:
1. **Reproduce:** Document the exact failure command or user interaction.
2. **Identify:** Categorize root cause (`Auth`, `Logic`, `Environment`, `Contract`, `Styling`).
3. **Minimal Fix:** Apply smallest verified fix.
4. **Verify:** Prove with automated regression test.
5. **Codify:** Append imperative rule to `.product-loop/rules.md`.

### Compound Learning Repository (`docs/solutions/`)
Document all non-trivial solutions in `docs/solutions/[category]/[sanitized-slug]-[YYYYMMDD].md` with validated YAML frontmatter.

### Critical Patterns (Required Reading)
When a mistake recurs (3+) or represents a high-severity foundational rule, extract a **`❌ WRONG vs ✅ CORRECT`** pattern and append it directly to `docs/solutions/patterns/critical-patterns.md`.

---

## 7. Meta-Skill Extraction (`continuous-learning`)

When a cycle produces a non-obvious solution or reusable pattern, the agent mints a permanent `SKILL.md`:
1. **Trigger Conditions:** Non-obvious workarounds, project-specific conventions, tool/API edge cases, misleading error signatures, or workflow optimizations.
2. **Quality Filter:** Must be **Reusable** (≥3 future cycles), **Non-trivial** (required discovery), **Specific** (exact regex/cues/diffs), and **Verified** (passing tests).
3. **Registration:** Save to `.agents/skills/[skill-name]/SKILL.md` or `~/.gemini/config/skills/[skill-name]/SKILL.md`.

---

## 8. Perpetual Backlog Discovery (Self-Replenishing Queue)

When the `NOW` queue in `.product-loop/roadmap.md` is empty, do NOT halt. Trigger the discovery engine:
1. **Dogfood & A11y Audit:** Crawl live routes (`dogfood`, `a11y-debugging`, `chrome-devtools`) for visual breaks and UX friction.
2. **Performance Audit:** Profile bundle weight and CWV (`debug-optimize-lcp`, `developer-web-performance`).
3. **Subtractive Audit:** Detect dead code, orphaned routes, and unused config toggles.
4. **Competitor Spikes:** Benchmark market trends (`proven-product-spec`) to populate `NOW`, `NEXT`, and `LATER`.

---

## 9. Directory Structure & State Schemas

```
.product-loop/
├── state.json                          # Machine-readable loop state, envelope & metrics
├── baton.md                            # Active iteration context & immediate instructions
├── rules.md                            # Accumulated imperative rules (Ralph Loop)
├── strategy.md                         # Melissa Perri Decision Stack
├── roadmap.md                          # Now-Next-Later Outcome Roadmap (Additive + Subtractive)
├── learnings.md                        # Strategic pivots, validated hypotheses & pruning logs
└── history/                            # Archived baton summaries per completed cycle
    ├── cycle-001.md
    └── cycle-002.md

docs/
└── solutions/                          # Compound Learning Repository
    ├── patterns/
    │   ├── critical-patterns.md        # Required reading (WRONG vs CORRECT)
    │   └── common-solutions.md         # Consolidated solution patterns
    ├── foundation/                     # DB, Auth, Schema solutions
    ├── mechanism/                      # Engine logic, state machines
    ├── interface/                      # UI, CSS, accessibility
    └── hardening/                      # Security, performance, network resilience
```

---

## 10. Autonomous Advisory Escalation (`ask-a-product-expert`)

When facing deadlocks or ambiguity, consult virtual masters before acting:

| Trigger Scenario | Primary Expert Consulted | Focus Question / Output |
| :--- | :--- | :--- |
| **Unclear Problem vs. Symptom** | **Melissa Perri** / **Teresa Torres** | "Is this an authentic customer obstacle or a solution in disguise?" |
| **Feature Pruning & Simplification** | **John Cutler** / **Marty Cagan** | "Is this feature carrying its weight? What happens if we delete this toggle?" |
| **Architecture & Dependency Order** | **God-Marduk** / **Martin Fowler** | "What is the strict dependency hierarchy? How do we decouple mechanism from UI?" |
| **Scope Creep / Bloat Risk** | **Shreyas Doshi** / **Gibson Biddle** | "What is the non-negotiable Minimal Viable Product? What is the LNO classification?" |
| **Prioritization Disagreement** | **Janna Bastow** / **Gokul Rajaram** | "Does this belong in Now, Next, or Later? What is the SPADE prioritization?" |
| **Growth / Retention Mechanics** | **Brian Balfour** / **Elena Verna** | "What is the natural product loop and retention lever here?" |
| **Aesthetic / Usability Friction** | **Don Norman** / **Steve Krug** | "What is the cognitive load penalty? How can we eliminate affordance ambiguity?" |
| **Systemic Process Defect** | **Michael Bolton** / **W. Edwards Deming** | "What feedback loop or standard work template was missing in our pipeline?" |

---

## 11. Execution CLI & Bootstrap Instructions

### Initializing the Loop
Run the bundled bootstrap script to initialize state:

```bash
python scripts/init_loop.py --mode overnight --hours 12 --vision "Effortless workspace automation"
```

### Running the Loop
```text
Execute /continuous-product-loop --duration 12h
```

---

## 12. Non-Negotiable Restraint Rules

1. **No Additive-Only Bias:** Never complete 5 consecutive cycles of pure feature addition without triggering a subtractive/pruning review.
2. **No Floating Abstractions:** Never write frontend UI components before underlying data schemas and engine mechanisms are built and tested.
3. **No Amnesiac Runs:** Always load `docs/solutions/patterns/critical-patterns.md` and `.product-loop/rules.md` at Phase 0 before generating code.
4. **No Skipping TDD:** Red phase (failing test) MUST precede Green phase (implementation) on 100% of functional initiatives.
5. **No Infinite Zombie Drift:** Always respect the time/cycle budget envelope configured in `state.json`.
