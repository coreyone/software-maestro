---
name: meeting-transcription-notes
description: "Trigger: meeting-transcription-notes, one-on-one-cadence, weekly-review-triage, meeting transcript, audio transcript, Zoom notes, Otter export, action items, executive readout, meeting summary. Scope: Operational Meeting Decision Records. Transforms messy meeting audio transcripts into structured decision records using McKinsey SCQA or Amazon PR/FAQ. Boundary: Excludes async email chains."
---

# OPERATIONAL MEETING INTELLIGENCE & TRANSCRIPTION SYNTHESIS

Convert raw, chaotic meeting transcripts into rigorous, high-leverage operational decision records.

> Over 80% of meeting notes fail because they function as passive chronological transcripts rather than active operational decision records. World-class organizations replace chronological narration with outcome-oriented decision architecture.

---

## Operating Boundary

- **Triggers:** Any raw transcript, multi-speaker conversational log, audio export (Otter.ai, Fathom, Grain, Descript, Fireflies, Zoom, Google Meet, Microsoft Teams), voice memo dump, or prompt requesting meeting synthesis, action item extraction, executive readout, incident postmortem notes, or structured 1:1 summaries.
- **Cross-Disciplinary Standards Applied:**
  - **`technical-language-rules` (ASD-STE100 + Google DevDocs):** Deterministic prose, $\le 20$ words/sentence procedural, $\le 25$ words/sentence descriptive, $\le 3$ noun stacks, unambiguous connectors (`because`, `after`, `can`, `must`), imperative action verbs.
  - **`info-to-ink` (Output Token Compression):** Maximum information-to-ink ratio. Drop conversational filler, pleasantries, hedging, and throat-clearing while preserving exact code, identifiers, metrics, and dates.
  - **`the-elements-of-style-principles` (Strunk & White):** Structural integrity, active voice, positive assertions, parallel grammatical construction, and ruthless omission of superfluous words.
  - **`conversion-copywriting`:** High-impact executive headlines ($\le 10$ words, no puns, no exclamation points), benefit-focused value framing, and urgent, action-driven clarity for leadership readouts.
- **Anti-Triggers / Exclusions:** Real-time audio hardware capture/streaming, speech-to-text acoustic model training, raw video editing, or verbatim legal stenography.

---

## Inputs Required

1. **Raw Transcript or Notes:** Text transcript with or without speaker labels and timestamps.
2. **Meeting Archetype (Explicit or Inferred):** Executive readout, cross-functional project sync, product strategy debate, operational incident postmortem, or fast 1:1 / standup.
3. **Target Framework (Optional):** Specific framework requested (Minto SCQA, Amazon Narrative, Apple DAP+DRI, Bridgewater Issue-Log, Tim Ferriss 80/20 MVN), or allow the autonomous Framework Selector to route.
4. **Participant Context (Optional):** Key stakeholders, roles, and decision-makers in the room.

---

## The 5 Canonical Operational Frameworks

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          OPERATIONAL MEETING FRAMEWORK MATRIX                          │
├───────────────────────┬───────────────────────────────┬────────────────────────────────┤
│ Framework             │ Origin / Paradigm             │ Optimal Meeting Archetype      │
├───────────────────────┼───────────────────────────────┼────────────────────────────────┤
│ 1. Minto Pyramid/SCQA │ Barbara Minto (McKinsey/BCG)  │ Steering committees, Exec syncs│
│ 2. Silent Narrative   │ Jeff Bezos (Amazon)           │ Strategy, Resource allocation  │
│ 3. DAP + Single DRI   │ Apple / Silicon Valley        │ Cross-functional execution     │
│ 4. Issue-Log & 5 Whys │ Ray Dalio (Bridgewater)       │ Retros, Postmortems, Outages   │
│ 5. 80/20 MVN          │ Tim Ferriss / First Principles│ 1:1s, Quick standups, Founder  │
└───────────────────────┴───────────────────────────────┴────────────────────────────────┘
```

### Framework Selection Engine (Heuristic Router)

If the user does not specify a framework, automatically select based on content cues:
- **Executive Readout / High-Stakes Proposal / Board Update $\to$ McKinsey Minto Pyramid (SCQA)**
- **Strategic Direction / Major Architecture / Capital & Headcount $\to$ Amazon Silent Narrative**
- **Sprint Sync / Cross-Team Dependency / Product Launch Execution $\to$ Apple DAP + DRI**
- **Incident Postmortem / Operational Failure / Process Retro $\to$ Bridgewater Issue-Log & 5 Whys**
- **Daily Standup / 1:1 Mentorship / Rapid Triage / Brainstorm $\to$ Tim Ferriss 80/20 MVN**

---

## Execution Instructions

Follow this 5-stage synthesis pipeline for every transcript:

```
  [Stage 1: Ingest & Clean]  --> Strip timestamps, verbal filler, false starts, acoustic noise.
             │
  [Stage 2: Filter & Isolate]--> Separate conversational banter from core decision nodes.
             │
  [Stage 3: Prose Compression] -> Enforce STE-100, Info-to-Ink, and Strunk & White brevity.
             │
  [Stage 4: Framework Route] --> Apply Minto, Amazon, Apple, Bridgewater, or Ferriss model.
             │
  [Stage 5: DRI Enforcement] --> Assign EXACTLY ONE directly responsible individual per item.
```

### Stage 1: Ingest & Cleanse
1. Strip non-semantic artifacts: timestamps (`[00:14:22]`), filler words (`um`, `uh`, `like`, `you know`, `basically`, `actually`), conversational throat-clearing, and audio glitches.
2. Normalize speaker tags and consolidate fragmented conversational turns into coherent thematic points.

### Stage 2: Filter & Isolate Semantic Nodes
1. Extract the **Core Tension / Primary Question**: What was the fundamental disagreement or problem that necessitated this meeting?
2. Extract **Binding Decisions**: What was definitively resolved vs. what remains open?
3. Extract **Action Commitments**: Specific deliverables promised by participants.
4. Extract **Dissents & Concerns**: Unresolved objections, minority viewpoints, and risks raised.

### Stage 3: Apply Writing & Compression Standards

1. **Apply `info-to-ink` Output Compression:**
   - Drop pleasantries, hedging (*"I think"*, *"seems to be"*), wrap-up filler, and conversational narrative.
   - Maximize decision density per token.
   - Preserve technical tokens exactly: code identifiers, API endpoints, metrics, dates, and names.

2. **Apply `technical-language-rules` (ASD-STE100 + Google DevDocs):**
   - Action items must start with an imperative verb (`Add`, `Deploy`, `Fix`, `Migrate`, `Verify`).
   - Sentence limits: $\le 20$ words for procedural actions, $\le 25$ words for descriptive summaries.
   - Restrict noun clusters to $\le 3$ nouns.
   - Use deterministic connectors: `because` (never *since*/*as*), `after` (never *once*), `can` vs. `must` (never *may*), `before` (never *prior to*), `to` (never *in order to*).

3. **Apply `the-elements-of-style-principles` (Strunk & White):**
   - Use active voice: *"@Sarah deploys the gateway"* (not *"The gateway will be deployed by Sarah"*).
   - Put statements in positive form; eliminate evasive wording.
   - Enforce parallel grammatical construction across list items and table rows.
   - Omit needless words: make every word tell.

4. **Apply `conversion-copywriting` (Executive Readouts):**
   - Frame executive headlines and takeaways with punchy, benefit-focused clarity ($\le 10$ words).
   - Stir urgency around strategic priorities without cute puns or exclamation points.

### Stage 4: Structure According to Selected Framework

#### 1. The Strategy Consulting Standard (McKinsey / BCG / Deloitte: Minto Pyramid / SCQA)
- **Executive Summary:** One punchy, benefit-focused headline ($\le 10$ words) and a 1–2 sentence synthesis.
- **S (Situation):** Agreed baseline facts and context (non-controversial starting point).
- **C (Complication):** The catalyst, friction, or constraint that triggered the debate.
- **Q (Core Question):** The central strategic question addressed.
- **A (Answer / Agreed Direction):** The explicit recommendation or resolution.
- **MECE Next Steps (DRI Table):** Directly Responsible Individual, Imperative Action, Verifiable Deliverable, Hard Deadline.

#### 2. The Big Tech Strategic Model (Amazon Silent Narrative & 2-Pizza Rule)
- **The "So What?" (Executive Decision):** High-level strategic resolution.
- **Decision Categorization:**
  - **Type 1 (Irreversible / High-Stakes):** Heavy deliberation required; two-way doors closed.
  - **Type 2 (Reversible / Bias-for-Action):** High velocity; lightweight test-and-learn.
- **Open Tenets & Dissent (Disagree & Commit):** Explicitly document who disagreed, why, and their commitment to support execution.
- **Single-Owner Action Registry:** 1 name, 1 measurable milestone, 1 target date.

#### 3. The Big Tech Execution Model (Apple DAP + DRI)
- **D (Decisions):** Binary agreements reached in the room (No ambiguity).
- **A (Actions & DRI):** Table with `DRI (Single Name)`, `Imperative Task`, `Hard Deadline`, `Verification Metric`.
- **P (Problems & Blockers):** Active escalations, cross-team dependencies, and unresolved risks with required forum for resolution.

#### 4. The Radical Transparency Model (Bridgewater / Ray Dalio Issue-Log)
- **Gap Analysis (What Happened vs. What Should Have Happened):** Objective reality vs. standard expectation.
- **5 Whys Root Cause Chain:** Drill down through human error to systemic/process/governance failures.
- **Principle Codified:** The generalized rule or operating policy established so this class of issue never recurs.
- **Machine Adjustment Action Plan:** Tooling, gating, or checklist updates assigned to individual DRIs.

#### 5. The High-Leverage / First-Principles Model (Tim Ferriss 80/20 MVN)
- **The 1 Thing:** The single highest-impact outcome or breakthrough of this session.
- **Core Constraint / Bottleneck:** The primary bottleneck throttling progress right now.
- **Who / What / When:** 2–3 mission-critical high-leverage actions maximum. Everything else eliminated.

---

## Output Templates

### Template A: McKinsey SCQA Format

```markdown
# [Meeting Title] — Executive Decision Record (SCQA)
**Date:** YYYY-MM-DD | **Attendees:** [List] | **Framework:** McKinsey SCQA

## Executive Summary
**[Punchy Benefit-Driven Headline under 10 words]**
[1-2 sentences capturing the overarching agreement and business impact using active voice.]

## Strategic Context (SCQA)
- **Situation (Baseline):** [Agreed operational context and stable baseline facts]
- **Complication (Trigger):** [The friction, market shift, or blocker forcing a decision]
- **Question (Core Dilemma):** [The specific question the room convened to answer]
- **Answer (Agreed Resolution):** [The synthesized recommendation and path forward]

## Decision & Rationale
- **Decision:** [Explicit outcome stated in active voice]
- **Rationale & Trade-offs:** [Why this path was chosen because of specific evidence]
- **Key Evidence / Data:** [Metrics or proof points cited in discussion]

## MECE Action Matrix
| Directly Responsible Individual (DRI) | Imperative Action & Verifiable Deliverable | Hard Deadline | Status / Dependency |
| :--- | :--- | :--- | :--- |
| @Name | [Imperative verb + concrete deliverable] | YYYY-MM-DD | [Dependencies] |

## Open Risks & Unresolved Questions
- [ ] [Risk / Question 1] — Escalation path / next review date
```

### Template B: Amazon Narrative Memo Format

```markdown
# [Meeting Title] — Strategic Narrative Record
**Date:** YYYY-MM-DD | **Attendees:** [List] | **Framework:** Amazon Narrative (Type 1 / Type 2)

## 1. The "So What?" (Core Decision)
**[Strategic Headline under 10 words]**
[Executive summary of the strategic outcome and customer impact.]

## 2. Decision Classification
- **Classification:** `Type 1 (Irreversible)` OR `Type 2 (Reversible / Two-Way Door)`
- **Strategic Impact:** [Explanation of stakes, blast radius, and reversibility cost]
- **Customer Impact:** [Direct benefit to end-users]

## 3. Discussion Points & Stress-Testing
- [Core thesis debated and key arguments evaluated]
- [Alternative options rejected because of specific trade-offs]

## 4. Disagree & Commit (Documented Dissent)
- **Dissenting Perspective:** [Stakeholder name] raised concerns regarding [specific risk].
- **Resolution:** Group aligned on [path] with [Stakeholder] committing to execute.

## 5. Single-Owner Deliverables
| Single Owner | Imperative Action & Target Metric | Target Date |
| :--- | :--- | :--- |
| @Name | [Imperative verb + measurable milestone] | YYYY-MM-DD |
```

### Template C: Apple DAP + DRI Format

```markdown
# [Meeting Title] — Execution Sync (DAP)
**Date:** YYYY-MM-DD | **Attendees:** [List] | **Framework:** Apple DAP + DRI

## Decisions (D)
1. **[Decision 1]:** [Clear, binary resolution reached in the room]
2. **[Decision 2]:** [Clear, binary resolution reached in the room]

## Actions & DRIs (A)
| DRI (Single Owner) | Imperative Action & Deliverable | Hard Deadline | Success Criteria |
| :--- | :--- | :--- | :--- |
| @Name | [Imperative verb + concrete task] | YYYY-MM-DD | [Verifiable outcome] |

## Problems & Blockers (P)
- ⚠️ **[Blocker 1]:** [Description] | **Owner:** @Name | **Escalation Path:** [Forum / Date]
```

### Template D: Bridgewater Issue-Log & 5 Whys

```markdown
# [Incident / Meeting Title] — Machine Root Cause & Principle Log
**Date:** YYYY-MM-DD | **Attendees:** [List] | **Framework:** Bridgewater Issue-Log

## 1. Reality Gap Analysis
- **What Happened:** [Objective factual breakdown of the event/outcome]
- **What Should Have Happened:** [Expected standard operating procedure]
- **Delta / Failure Cost:** [Quantified impact]

## 2. 5 Whys Root Cause Chain
1. *Why did X fail?* $\to$ [Immediate technical/procedural failure]
2. *Why did that happen?* $\to$ [Proximate cause]
3. *Why wasn't it caught?* $\to$ [Detection/testing gap]
4. *Why did the process allow it?* $\to$ [Process/policy absence]
5. *Why is the system designed this way?* $\to$ [**Systemic Root Cause**]

## 3. Codified Principle
> **Principle [ID/Name]:** [General rule and operational mental model to prevent recurrence]

## 4. Machine Engineering Action Plan
| DRI | System/Process Adjustment | Completion Target |
| :--- | :--- | :--- |
| @Name | [Tooling/policy update with imperative verb] | YYYY-MM-DD |
```

### Template E: Tim Ferriss 80/20 Minimum Viable Note (MVN)

```markdown
# [Meeting Title] — 80/20 Minimum Viable Note (MVN)
**Date:** YYYY-MM-DD | **Attendees:** [List] | **Framework:** 80/20 MVN

## The 1 Thing
> **[Single highest-leverage outcome or breakthrough from this session]**

## The Primary Bottleneck
- **Constraint:** [The one blocker or friction point throttling velocity]
- **Removal Tactic:** [Direct action to eliminate the bottleneck]

## Mission-Critical Actions (Max 3)
1. **@Owner:** [Imperative Action] by **[Hard Date]**
2. **@Owner:** [Imperative Action] by **[Hard Date]**
3. **@Owner:** [Imperative Action] by **[Hard Date]**
```

---

## Non-Negotiable Rules

1. **Zero Chronological Transcribing:** Never write chronological narrative ("First Alice spoke about X, then Bob disagreed and mentioned Y"). Organize strictly by semantic decision architecture.
2. **Strict Single-DRI Enforcement:** Every action item MUST have exactly one directly responsible individual (e.g. `@Sarah`). Never allow shared or ambiguous ownership (`@Team`, `@All`, `@Devs`).
3. **Imperative Action Mood:** Every action item must begin with an imperative verb (`Add`, `Deploy`, `Fix`, `Migrate`, `Verify`). Avoid weak descriptive phrases (*"Sarah will look into..."*).
4. **Deterministic Technical Language (ASD-STE100):** Use `because` (not *since*/*as*), `after` (not *once*), `can` vs `must` (never *may*). Enforce word count limits ($\le 20$ words procedural, $\le 25$ words descriptive).
5. **High Information-to-Ink Ratio:** Omit all filler, throat-clearing, pleasantries, and decorative banter. Preserve technical tokens, metrics, endpoints, and dates verbatim.
6. **Active Voice & Positive Form (Strunk & White):** State decisions directly in the active voice. Avoid passive evasions.
7. **Explicit Decision Permanence:** For strategic meetings, categorize every major decision as **Type 1 (Irreversible)** or **Type 2 (Reversible)**.
8. **Capture Dissent Rigorously:** Do not paper over disagreements. Explicitly record dissenting opinions under *Disagree & Commit* with stakeholder attribution.
9. **Enforce Hard Deadlines:** Every action item must have a specific target date (`YYYY-MM-DD` or relative hard date). Words like "soon", "next sprint", or "TBD" are rejected unless flagged as open risks.

---

## Quality Scoring Rubric

Evaluate generated meeting notes across 5 pillars (Max Score: 20 points):

| Pillar | 0 - Failing | 1 - Poor | 2 - Adequate | 3 - Strong | 4 - World-Class |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Decision vs Narrative Ratio** | Verbatim transcript dump with zero distillation. | Chronological narrative summary with timestamps. | Grouped bullet points with mixed discussion and decisions. | Clear separation of decisions, rationale, and next steps. | 100% signal-dense decision architecture; zero conversational filler (`info-to-ink`). |
| **2. Single-DRI Accountability** | No action items or unassigned tasks. | Shared ownership (`@Engineering`, `@Product`). | Named owners but vague tasks or missing deadlines. | Every action item has 1 named DRI and a clear deadline. | 1 DRI per item, imperative STE verb, verifiable deliverable, and hard date. |
| **3. Framework Fidelity** | Incoherent or arbitrary formatting. | Loose adherence to headings with missing core components. | Correct template headings but superficial content. | Complete framework compliance with MECE rigor. | Flawless structural mastery (Minto SCQA, Amazon Type 1/2, DAP, 5 Whys, or MVN). |
| **4. Technical Precision & Style** | Passive, ambiguous prose with polysemous connectors. | Weak action verbs and loose sentence structure. | Standard corporate English with occasional passive voice. | Active voice, STE connectors (`because`, `after`), and concise sentences. | Full ASD-STE100 + Strunk & White compliance: active, positive, parallel, $\le 20$ words. |
| **5. Dissent & Strategic Clarity** | Disagreements and risks omitted entirely. | Mention of "some debate" without specifics. | Summarized friction without named attribution. | Explicit dissent documented with resolution rationale. | Complete *Disagree & Commit* logging, Type 1/2 tagging, and root cause diagnosis. |

---

## Completion Gate

Before finalizing any meeting synthesis, verify:
- [ ] Conversational noise, filler words, and timestamps are eliminated (`info-to-ink`).
- [ ] The appropriate operational framework is chosen and strictly formatted.
- [ ] Every action item has exactly one human DRI and begins with an imperative verb (`technical-language-rules`).
- [ ] Sentences adhere to length limits ($\le 20$ words procedural, $\le 25$ words descriptive).
- [ ] Ambiguous connectors are replaced (`because` for cause, `after` for sequence).
- [ ] All action items have verifiable deliverables and hard deadlines.
- [ ] Strategic decisions are classified (Type 1 vs Type 2) or root causes diagnosed (5 Whys).
- [ ] Dissent, open risks, and unresolved dependencies are surfaced explicitly.
- [ ] Output meets Strunk & White active-voice, positive-form standards.
