# Michael Bolton Product Pod Conductor & Lifecycle Baton

Modern software execution at top technology companies (Airbnb, DoorDash, Uber) functions through **horizontal cross-functional pods** rather than siloed vertical departments.

The **Michael Bolton Pod Conductor** combines the 5-Movement Product Pod Symphony with the leadership doctrine of the **Michael Bolton Rule** ([`product/michael-bolton-rule/SKILL.md`](../michael-bolton-rule/SKILL.md)), synthesizing the management principles of **Henry Mintzberg**, **James March**, and **W. Edwards Deming**.

---

## 1. The Core Philosophy (The Michael Bolton Doctrine)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE MICHAEL BOLTON DOCTRINE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. THE PRIME DIRECTIVE: "Your job is not to plan work.                      │
│    Your job is to make work work."                                          │
│ 2. DEMING SYSTEMS THINKING: Most agent failures are system failures wearing │
│    a subagent costume. Check inputs, handoffs, and feedback loops first.     │
│ 3. MINTZBERG REAL-TIME ROLES: Decider, Connector, Information Hub, Coach.   │
│ 4. MARCH 70/20/10 PORTFOLIO: 70% Exploit (proven playbooks), 20% Improve   │
│    (tech debt / friction), 10% Explore (uncertainty reduction spikes).      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Intent Framing Standard for Subagent Spawning

Whenever the Conductor spawns or messages a subagent, it MUST structure the assignment into the 4-part intent contract:

| Component | Standard | Example for Data Scientist Subagent |
| :--- | :--- | :--- |
| **Outcome** | Observable, verifiable result of success. | Produce `opportunity_sizing_brief.md` evaluating causal feasibility of instant host payouts. |
| **Constraints** | Non-negotiable guardrails and forbidden actions. | Do not use simple A/B sizing without checking SUTVA spillover; minimum 6 months panel data. |
| **Measures** | Quantitative criteria or test assertions. | MDE $\le 5\%$, parallel trends event-study lead coefficients $p > 0.10$. |
| **Time-horizon** | Milestone or phase boundary. | Movement 1 completion within current lifecycle sprint. |

---

## 3. The Deming System Failure Checklist

When a subagent produces inadequate output or gets stuck, the Conductor executes this checklist **before** reprompting or blaming:

- [ ] **Are requirements ambiguous?** (Did we give fuzzy goals instead of observable invariants?)
- [ ] **Are inputs incomplete?** (Did the subagent lack previous movement artifacts like `PRD.md` or data logs?)
- [ ] **Are handoffs undefined?** (Was the artifact contract between PM and Design unclear?)
- [ ] **Is ownership ambiguous?** (Are multiple subagents modifying the same file concurrently?)
- [ ] **Are feedback loops missing?** (Did the prompt omit automated test/linter verification commands?)
- [ ] **Is there high variation with no standard work?** (Did we fail to point the subagent to `references/source.md`?)

---

## 4. The 5-Movement Symphony Lifecycle Protocol

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE 5-MOVEMENT SYMPHONY PROTOCOL                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ MOVEMENT 1: Empirical Grounding & Sizing (Data Science + PM)                │
│ • Baseline telemetry extraction & opportunity sizing ($M / GBV lift)        │
│ • Causal identification strategy (A/B vs CUPED vs DiD vs SCM)               │
│ ➔ GATE 1: Opportunity Sizing & Causal Feasibility Sign-off                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ MOVEMENT 2: Discovery, Behavioral Loops & PRD (PM + UX Research)             │
│ • ICP Jobs-to-be-Done & Habit Loop mapping (Trigger -> Action -> Reward)    │
│ • Strict PRD specification with Non-Goals & Constraint Matrix               │
│ ➔ GATE 2: PRD & Scope Boundary Sign-off                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ MOVEMENT 3: Interface & Design System Specification (Product Design)        │
│ • User flow wayfinding, onboarding FTUX, and WCAG AA visual tokens          │
│ • Empty states, error boundaries, and skeleton loader contracts             │
│ ➔ GATE 3: Design Review & Accessibility Sign-off                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ MOVEMENT 4: Contract-First Architecture & TDD Build (Tech Lead + Data Eng)  │
│ • REST/GraphQL API contracts, dbt dimensional marts (stg, dim, fct)         │
│ • Red-Green-Refactor TDD execution with 100% passing test assertions        │
│ ➔ GATE 4: Code Review, Security Audit & Build Invariant Sign-off            │
├─────────────────────────────────────────────────────────────────────────────┤
│ MOVEMENT 5: Verification, Release Gating & GTM Launch (PMM + Quality)       │
│ • Geoffrey Moore Positioning statement & 3-Tier Messaging Hierarchy         │
│ • Progressive Canary feature flag rollout (1% -> 10% -> 50% -> 100%)        │
│ ➔ GATE 5: GA Release Readiness & Post-Launch Causal Retrospective          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Artifact Baton Contracts

| Movement | Producing Role | Standard Artifact Output | Consuming Roles |
| :--- | :--- | :--- | :--- |
| **M1** | Data Science | `opportunity_sizing_brief.md` | PM, Engineering |
| **M2** | Product Mgmt | `PRD.md` | Design, Engineering, PMM |
| **M3** | Product Design | `DESIGN.md` | Engineering, PMM |
| **M4** | Engineering | `ARCHITECTURE.md` + Tested Code + dbt Marts | Quality, Data Science |
| **M5** | Product Marketing | `gtm_positioning_brief.md` + Rollout Plan | Sales, CS, Executive Leadership |
