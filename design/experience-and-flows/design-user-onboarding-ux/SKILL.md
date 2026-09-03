---
name: design-user-onboarding-ux
description: "Design first-time user onboarding experiences, product activation flows, and empty states."
---

# User Onboarding & First-Time User Experience (FTUX) Rules

## Core Philosophy

Users do not use software to become masters of the software; they use software to become better at their own goals (**Samuel Hulick's Fire Flower** principle / **Kathy Sierra's Badass Users**). 

Effective onboarding is not a product tour or a frontloaded manual. It is an **invisible, scaffolded path that delivers the user to their first core value realization ("Aha! moment") with zero extraneous cognitive load**.

---

## Operating Boundary & Integration

- **Primary**: User onboarding architecture, behavioral friction elimination, cognitive scaffolding, empty state design, progressive disclosure, and activation flows.
- **Upstream**: `ux-discovery-artifacts`, `product-strategy-outcome-vision`, `create-prd`.
- **Downstream**: `design-usability-rules`, `design-system-rules`, `failure-states-empty-states`, `analytics-event-tracking`.
- **Eval Pairing**: Grounded in `developer-eval-driven-development`—every onboarding flow is evaluated against explicit binary behavioral gates and measurable time-to-value (TTV) baselines.

---

## When to use

Use this skill when designing, auditing, or refactoring:
- First-time user experiences (FTUX) and welcome flows for consumer, mobile, SaaS, or developer products.
- Empty states, starter dashboards, sandbox templates, and default workspaces.
- Contextual, just-in-time guidance, feature discovery callouts, and interactive checklists.
- Activation funnels, time-to-value (TTV) reduction initiatives, and drop-off recovery flows.
- Developer "Zero-to-Hello-World" quickstart and CLI/SDK adoption flows.

## When not to use

Do not use this skill as the primary guide for:
- Backend authentication token issuance, session encryption, or SSO protocol implementation (use `auth-and-identity-rules`).
- Database schema modeling or persistence architecture (use `data-persistence-caching`).
- Multi-step checkout payment gateways or billing compliance (use `design-forms-wizards-checkout`).

---

## Trigger Cues

- Explicit mentions of `design-user-onboarding-ux`, onboarding, FTUX, first-run experience, welcome flow, or product walkthrough.
- Requests to reduce user drop-off after signup, increase activation rates, or improve time-to-value (TTV).
- Tasks involving empty states, sample data, progressive disclosure, tutorial popups, or guided checklists.
- Designing developer "Zero-to-Hello-World" quickstart experiences.

---

## Theoretical Frameworks & Literature Foundations

This skill translates the seminal research across five major schools of thought into actionable interface mechanics:

1. **Nielsen Norman Group (NN/g)**:
   - **Anti-Pattern**: Elimination of frontloaded modal carousels and "next-next-next" tooltip tours (working memory overload).
   - **Learn-by-Doing**: Contextual, just-in-time guidance attached strictly to the user's active focus.
   - **Empty States**: Transform zero-data views into action catalysts with templates and outcome-specific CTAs.
   - **Delayed / Lazy Registration**: Experience core value before requiring credentials or credit cards.
   - **User Autonomy**: Always provide immediate, prominent "Skip" / "Dismiss" controls with persistent background resumption.

2. **O'Reilly Media (Applied UX & Behavior Design)**:
   - **Kathy Sierra (*Badass: Making Users Awesome*)**: Minimum Viable Instruction (MVI). The product is not the hero; the user is. Eliminate UI training that does not unlock immediate capability within 60 seconds.
   - **Stephen Wendel (*Designing for Behavior Change*)**: The **CREATE** Framework (**C**ue, **R**eaction, **E**valuation, **A**bility, **T**iming, **E**xecution).
   - **Jenifer Tidwell, Charles Brewer, Aynne Valencia (*Designing Interfaces*)**: Progressive disclosure, inline discovery badges, and sandbox modes.
   - **Theresa Neil (*Mobile Design Pattern Gallery*)**: Interactive guided tasks tailored to touch ergonomics.

3. **MIT Press (Cognitive Science, HCI & Game Design)**:
   - **Katie Salen & Eric Zimmerman (*Rules of Play*)**: The "Invisible Tutorial" / Level-1 Game Design. Teach through safe, bounded interaction where early mistakes are harmless.
   - **Seymour Papert & Mitchel Resnick (*Mindstorms* / Lifelong Kindergarten)**: "Low Floor, High Ceiling, Wide Walls" (instant start, unlimited depth, multiple pathways).
   - **Don Norman (*The Design of Everyday Things*)**: Affordances and signifiers that communicate function visually without textual explanations.
   - **Jesper Juul (*The Art of Failure*)**: Competence scaffolding—early micro-wins to prevent cognitive churn.

4. **The Pragmatic Bookshelf (Developer Experience & Technical Onboarding)**:
   - **"Zero to Hello World in Under 5 Minutes"**: Single-command bootstrapping, sensible defaults, runnable sandboxes, and copy-pasteable error recovery.

5. **ProductLed / Wes Bush & Stanford Behavior Design (BJ Fogg / Samuel Hulick)**:
   - **The Bowling Alley Framework**: Straight-line onboarding (shortest path to value) bounded by Product Bumpers (in-app guidance) and Conversational Bumpers (re-engagement).
   - **BJ Fogg ($B = MAP$)**: Radical friction reduction when motivation peaks at first launch.
   - **Samuel Hulick (*UserOnboard*)**: The Super Mario Fire Flower model and the Activation Funnel (Setup $\to$ Aha! $\to$ Habit).

6. **Tony Fadell (*Build* — The Whole Product & Unboxing Experience)**:
   - **The 360° Customer Lifecycle (Ch 21)**: The product is not just in-app screens. It begins at the marketing hook, extends through the first 5 minutes of installation and "unboxing" (CLI bootstrapping, environment setup), includes out-of-band touchpoints (welcome emails, custom tooling, companion docs), and mandates graceful error recovery.
   - **Zero-Friction Unboxing**: Eliminate setup friction before the user reaches the app. Provide zero-config sensible defaults so the initial unboxing feels effortless.

---

## Eval-Driven Development (EDD) Workflow for Onboarding

Follow this iterative evaluation cycle for all onboarding work:

```
┌────────────────────────────────────────────────────────────────────────┐
│ ONBOARDING EVAL-DRIVEN DEVELOPMENT LOOP                                │
│                                                                        │
│  1. CAPTURE BASELINE ──► Measure TTV, step count, cognitive load       │
│           │                                                            │
│           ▼                                                            │
│  2. WRITE EVAL SUITE ──► Define binary gates in evals/cases.json       │
│           │              (Test against known failure modes)            │
│           ▼                                                            │
│  3. APPLY FRAMEWORKS ──► Prune steps (Straight-Line), scaffold empty   │
│           │              states, add Just-in-Time guidance             │
│           ▼                                                            │
│  4. VERIFY CONTRACTS ──► Run eval grader (check_binary_evals.py)       │
│           │                                                            │
│           ▼                                                            │
│  5. LOCK IN EVIDENCE ──► Record before/after friction audit table      │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Capture Baseline Friction**:
   - Count total screens, fields, and clicks between launch and the first value delivery.
   - Document cognitive load leaks (e.g., upfront passwords, unskippable overlays, empty tables).

2. **Define Binary Behavioral Evaluators**:
   - Establish explicit pass/fail criteria matching the non-negotiables in `evals/cases.json`.
   - Prove the eval rejects known bad UX (e.g., 5-step carousels, forced surveys).

3. **Execute Straight-Line Optimization**:
   - Prune every step not on the straight line to the Aha! moment.
   - Replace blank screens with rich sample templates or actionable zero-states.
   - Attach contextual tooltips only to active user focus (max 1 tooltip active).

4. **Verify Against Binary Completion Gate**:
   - Ensure all automated checks and UX criteria pass before shipping.

---

## Completion Gate (Binary Release Criteria)

Before reporting completion, verify against the following non-negotiable criteria:
- [ ] **No Multi-Step Modal Carousel**: Zero frontloaded slide tours; replaced with contextual inline hints or interactive empty states.
- [ ] **Time-to-Value (TTV) < 60s**: User produces or experiences primary core value within one minute of landing.
- [ ] **Straight-Line Pruning**: All non-essential profile, setup, or permission fields are deferred or auto-configured with sensible defaults.
- [ ] **Always Skippable & Resumable**: Every guided sequence has an obvious "Skip" control, with a persistent drawer/checklist to resume later.
- [ ] **Actionable Empty States**: No blank screens; includes pre-populated sample data or a single clear creation CTA.
- [ ] **Competence Scaffolding (Level 1)**: First user action is sandboxed, safe from catastrophic error, and provides immediate visual confirmation.
- [ ] **Binary Eval Suite Passes**: All test cases in `evals/cases.json` score 100% via `scripts/check_binary_evals.py`.

---

## Output Format

- **Primary Output**: Onboarding blueprint, interactive wireframe specification, or frontend component code.
- **Summary**: One-paragraph rationale detailing how the design minimizes Time-to-Value (TTV).
- **Friction Audit Table**:
  | Step / Screen | Original Friction | Framework Applied | Straight-Line Action |
  | :--- | :--- | :--- | :--- |
  | Welcome Tour | 4-step modal carousel | NN/g + Kathy Sierra MVI | Replaced with active empty state |
  | Account Setup | 6 mandatory fields | BJ Fogg ($B=MAP$) | Deferred to Lazy Registration |
- **State Specifications**: Exact layouts for Empty State, First-Run Scaffold, Active Checklist, and Value Confirmation.
- **Eval Evidence**: Link to verified eval suite or passing test run.
