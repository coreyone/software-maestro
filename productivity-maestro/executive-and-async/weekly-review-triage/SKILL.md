---
name: weekly-review-triage
description: "Trigger: weekly review, Friday triage, Monday planning, task triage, GTD review, Eisenhower matrix, prioritize tasks, organize backlog, mind sweep, weekly Big 3, open loops triage. Scope: Conduct comprehensive end-of-week or beginning-of-week task triage, inbox-zero sweeps, Eisenhower prioritization (Do/Schedule/Delegate/Eliminate), and weekly Big 3 outcome calibration. Incorporates ASD-STE100 technical language rules, info-to-ink token compression, Elements of Style brevity, and action-driven execution. Boundary: Excludes agile sprint estimation story-pointing and low-level calendar API scripting."
---

# WEEKLY REVIEW & OPERATIONAL TASK TRIAGE

Conduct a ruthless, high-leverage weekly operating review integrating David Allen's Getting Things Done (GTD) and Dwight D. Eisenhower's Urgency/Importance Decision Matrix.

> "Most people confuse motion with progress. Without a weekly operating rhythm to close open loops, prune low-leverage commitments, and calibrate strategic focus, engineers and leaders default to reacting to whatever screams loudest."

---

## Operating Boundary

- **Triggers:** Any request for weekly planning, end-of-week triage, Monday prioritization, GTD weekly review, Eisenhower matrix sorting, task list cleanup, backlog rationalization, inbox-zero sweep, or defining the "Weekly Big 3" outcomes.
- **Cross-Disciplinary Standards Applied:**
  - **`technical-language-rules` (ASD-STE100 + Google DevDocs):** Imperative action verbs (`Complete`, `Delegate`, `Archive`, `Block`), $\le 20$ words per task item, unambiguous connectors (`because`, `after`, `can`, `must`).
  - **`info-to-ink` (Output Token Compression):** High decision density. Eliminate filler and self-narration. Preserve exact project names, ticket IDs, metrics, and dates.
  - **`the-elements-of-style-principles` (Strunk & White):** Active voice, positive assertions, and ruthless pruning of zombie tasks.
  - **`marketing-copy-emotion-provoking-action-driven`:** Compelling, high-agency framing for the Weekly Big 3 outcomes to maximize focus and momentum.
- **Anti-Triggers / Exclusions:** Agile sprint story-pointing, personal journal writing, or calendar integration API scripting.

---

## Inputs Required

1. **Task & Commitment Dump:** Current task list, backlog items, unread/flagged Slack messages, open PRs, or rough mental notes.
2. **Current Project Status (Optional):** Active strategic initiatives and deadlines.
3. **Time Horizon:** Retrospective (closing the past week) + Forward Planning (calibrating the upcoming week).

---

## The 4-Stage GTD + Eisenhower Triage Engine

```
  [Stage 1: Mind Sweep & Ingestion]  --> Capture all open loops, lingering pings, and uncommitted ideas.
             │
  [Stage 2: Eisenhower Classification]--> Sort into Do (Q1), Schedule (Q2), Delegate (Q3), Eliminate (Q4).
             │
  [Stage 3: Strategic Calibration]   --> Lock in the "Weekly Big 3" (highest-leverage needle-movers).
             │
  [Stage 4: Pruning & De-commitment] --> Kill zombie projects; say explicit "NO" to low-ROI tasks.
```

### The Eisenhower 2x2 Operational Matrix

```
                      URGENT                        NOT URGENT
         ┌───────────────────────────────┬───────────────────────────────┐
         │ Q1: DO FIRST (Crises & Fires) │ Q2: SCHEDULE (High Leverage)  │
         │ • Production outages / Sev-1  │ • Architecture deep work      │
         │ • Hard deadline client deliverables • Refactoring core tech debt  │
         │ • Imminent launch blockers    │ • Strategic planning & 1:1s   │
IMPORTANT├───────────────────────────────┼───────────────────────────────┤
         │ Q3: DELEGATE / AUTOMATE       │ Q4: ELIMINATE / PRUNE         │
         │ • Routine status requests     │ • Zombie backlog tickets      │
         │ • Non-critical ad-hoc pings   │ • Unproductive recurring syncs│
NOT      │ • Repetitive manual workflows │ • Vanity metrics investigation│
IMPORTANT└───────────────────────────────┴───────────────────────────────┘
```

---

## Execution Instructions

### Stage 1: The Mind Sweep (Close Open Loops)
1. Review all inputs and extract unclosed loops: pending code reviews, unanswered leadership pings, stalled PRs, and informal verbal commitments.
2. Convert every raw thought into a single, concrete, imperative action sentence ($\le 20$ words).

### Stage 2: Eisenhower Categorization
- **Quadrant 1 (Urgent & Important):** Must be executed immediately. Assign to single human owner with hard date.
- **Quadrant 2 (Not Urgent, High Importance / Leverage):** Protect on calendar. Schedule explicit deep-work time blocks.
- **Quadrant 3 (Urgent, Low Importance):** Delegate to a teammate or automate with a script/template.
- **Quadrant 4 (Not Urgent, Low Importance):** Ruthlessly archive, cancel, or reject.

### Stage 3: Calibrate the "Weekly Big 3"
Select exactly **3 needle-moving outcomes** that define total success for the upcoming week.
- Each outcome must be binary, verifiable, and customer/business-impactful.

### Stage 4: Prune Stalled & Zombie Commitments
Identify at least 1–3 items to explicitly **de-commit**, cancel, or archive. State the exact reason for refusal.

---

## Output Template

```markdown
# Weekly Operating Review & Triage — [Week Ending / Starting Date]
**Author:** @Name | **Operating Focus:** [Core Theme of the Week]

## 1. The Weekly Big 3 (Strategic Core)
> **Outcome 1:** [Verifiable high-leverage outcome with business metric]
> **Outcome 2:** [Verifiable high-leverage outcome with business metric]
> **Outcome 3:** [Verifiable high-leverage outcome with business metric]

---

## 2. Eisenhower Prioritization Matrix

### 🔴 Quadrant 1: Do First (Immediate / High Stakes)
*High Urgency • High Importance*
| Task / Deliverable | Single Owner (DRI) | Hard Deadline | Target Metric / Verification |
| :--- | :--- | :--- | :--- |
| [Imperative action verb + task] | @Name | YYYY-MM-DD | [Verifiable outcome] |

### 🟢 Quadrant 2: Schedule & Protect (Deep Work / High Leverage)
*Low Urgency • High Importance (The True Value Engine)*
| Strategic Initiative | Calendar Deep-Work Block | Outcome Deliverable |
| :--- | :--- | :--- |
| [Deep-work focus area] | [Day / Time Block] | [Verifiable artifact / spec] |

### 🟡 Quadrant 3: Delegate & Automate (Friction Removal)
*High Urgency • Low Strategic Importance*
| Task Description | Delegated Owner / Automation Tool | Hand-off Date |
| :--- | :--- | :--- |
| [Operational task] | @Assignee OR [Script/Tool] | YYYY-MM-DD |

### ⚪ Quadrant 4: Eliminated & Pruned (The "Not-To-Do" List)
*Low Urgency • Low Strategic Importance (Saved Bandwidth)*
- ❌ **[Cancelled Item 1]:** Cancelled because [Specific rationale / Low ROI].
- ❌ **[Archived Item 2]:** Archived because [Deprioritized in favor of Q2 initiative].

---

## 3. Open Loops & Dependency Tracking
| External Dependency | Blocker Description | Owner to Ping | Next Escalation Date |
| :--- | :--- | :--- | :--- |
| [Team / Vendor] | [Waiting on X] | @Contact | YYYY-MM-DD |

---

## 4. Operational Invariants & Habits Check
- [ ] Calendar audit completed: Q2 deep work protected before meetings.
- [ ] Inbox / Slack zero achieved for the week.
- [ ] Weekly Big 3 broadcasted to pod / leadership.
```

---

## Non-Negotiable Rules

1. **Strict Limit of 3 Big Outcomes:** Never define more than 3 primary weekly outcomes. If everything is important, nothing is.
2. **Every Q1/Q2 Item Must Have a Verifiable Metric:** Avoid vague tasks (*"Work on backend"* $\to$ *"Deploy auth endpoint with 100% test coverage"*).
3. **Mandatory De-Commitment:** Every weekly review must prune at least one task or declare an explicit non-goal.
4. **Deterministic STE Action Verbs:** Action items must begin with an imperative verb (`Deploy`, `Write`, `Merge`, `Audit`, `Schedule`).
5. **No Shared Accountability:** Every item in the triage table has exactly one named DRI.

---

## Completion Gate

Before finalizing any weekly review:
- [ ] Exactly 3 Big Weekly Outcomes are declared with verifiable success criteria.
- [ ] Tasks are categorized into Eisenhower quadrants with zero overlap.
- [ ] At least one low-leverage task is explicitly pruned or cancelled.
- [ ] All action items have single named DRIs and hard deadlines.
- [ ] Sentences adhere to ASD-STE100 length limits ($\le 20$ words per task).
