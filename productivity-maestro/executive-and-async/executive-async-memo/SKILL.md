---
name: executive-async-memo
description: "Trigger: executive-async-memo, async memo, smart brevity, executive summary, leadership update, project briefing memo, 1-page memo. Scope: High-Leverage Asynchronous Executive Memos using Axios Smart Brevity and Amazon narrative principles. Boundary: Excludes live spoken meeting transcripts."
---

# EXECUTIVE ASYNC MEMO GENERATION

Transform noisy Slack/Teams threads, sprawling email chains, and complex project notes into high-impact, scannable executive async memos.

> The most valuable executive currency is attention. Sprawling 50-message Slack threads and fragmented email chains cause decision paralysis and lost context. High-performing organizations distill complex discussions into structured 1-page narrative memos and Smart Brevity briefings that drive immediate alignment.

---

## Operating Boundary

- **Triggers:** Any request to convert a Slack/Teams discussion thread, email chain, project update, or multi-party conversation into an executive memo, 1-pager, async briefing, leadership update, or Smart Brevity announcement.
- **Cross-Disciplinary Standards Applied:**
  - **`technical-language-rules` (ASD-STE100 + Google DevDocs):** Deterministic prose, $\le 20$ words/sentence procedural, $\le 25$ words/sentence descriptive, $\le 3$ noun stacks, unambiguous connectors (`because`, `after`, `can`, `must`), imperative action verbs.
  - **`info-to-ink` (Output Token Compression):** Maximum information-to-ink ratio. Drop conversational filler, pleasantries, hedging, and throat-clearing while preserving exact code, identifiers, metrics, and dates.
  - **`the-elements-of-style-principles` (Strunk & White):** Structural integrity, active voice, positive assertions, parallel grammatical construction, and ruthless omission of superfluous words.
  - **`marketing-copy-emotion-provoking-action-driven`:** Punchy headline under 10 words, benefit-driven value framing, and clear call-to-action without fluff or exclamation points.
- **Anti-Triggers / Exclusions:** Live spoken audio meeting transcripts (use `meeting-transcription-notes`), technical bug reproduction logs, or external paid ad copy.

---

## Inputs Required

1. **Source Content:** Raw Slack/Teams messages, email thread, project notes, or unstructured bullet points.
2. **Target Audience (Explicit or Inferred):** C-suite executives, VP/Directors, cross-functional stakeholders, or team-wide all-hands.
3. **Memo Paradigm (Optional):**
   - **Mode 1: Axios Smart Brevity** (Optimal for fast leadership briefings, status readouts, and company announcements).
   - **Mode 2: Amazon 1-Page / 6-Page Narrative** (Optimal for high-stakes proposals, capital allocations, and major architectural pivots).

---

## The 2 Canonical Async Memo Frameworks

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              ASYNC MEMO FRAMEWORK MATRIX                               │
├───────────────────────┬───────────────────────────────┬────────────────────────────────┤
│ Framework             │ Origin / Paradigm             │ Optimal Use Case               │
├───────────────────────┼───────────────────────────────┼────────────────────────────────┤
│ 1. Axios Smart Brevity│ Jim VandeHei & Mike Allen     │ Leadership updates, Slack sync │
│ 2. Amazon Narrative   │ Jeff Bezos (Working Backwards)│ Architectural & resource pivots│
└───────────────────────┴───────────────────────────────┴────────────────────────────────┘
```

---

## Execution Instructions

Follow this 5-stage async synthesis pipeline:

```
  [Stage 1: Thread Ingestion]  --> Parse messages, resolve timestamps, identify key authors.
             │
  [Stage 2: Core Signal Triage]--> Extract core thesis, tension, decisions, and data points.
             │
  [Stage 3: Prose Compression] --> Apply STE-100, info-to-ink, and Strunk & White brevity.
             │
  [Stage 4: Paradigm Assembly] --> Format into Smart Brevity or Amazon 1-Pager.
             │
  [Stage 5: DRI & Action Gate] --> Assign single human owner per deliverable with hard date.
```

### Stage 1: Thread Ingestion & Noise Cleansing
1. Strip conversational chatter, emoji reactions (`:+1:`, `:fire:`), scheduling back-and-forth, and fragmented replies.
2. Reconstruct the chronological and semantic debate into unified topic threads.

### Stage 2: Core Signal Triage
1. **The Axiom / Headline:** What is the single most important development or proposal?
2. **The "Why It Matters":** What is the quantifiable business, customer, or technical consequence?
3. **The Data / Evidence:** What metrics, benchmarks, or cost figures substantiate this?
4. **The Friction & Trade-offs:** What objections or alternative approaches were considered?
5. **The Decision / Next Step:** What action is required, who owns it, and by when?

### Stage 3: Apply Writing & Compression Standards
- **Headline Rule:** Under 10 words, start with a strong action verb or power noun, no articles ("The", "A"), no exclamation points.
- **Axios Smart Brevity Anchors:** Use bold signposts: **Why it matters:**, **Go deeper:**, **By the numbers:**, **What's next:**.
- **ASD-STE100 Rules:** Imperative verbs for actions (`Deploy`, `Approve`, `Migrate`), $\le 20$ words per action sentence, `because` instead of *since*/*as*.
- **Info-to-Ink:** Drop all throat-clearing (*"I am writing this memo to inform you that..."* $\to$ state the fact immediately).

---

## Output Templates

### Template A: Axios Smart Brevity Format (Default for Leadership & Slack)

```markdown
# [Memo Title under 10 words]
**Date:** YYYY-MM-DD | **Author:** @Name | **Audience:** [Target Stakeholders]

## Executive Summary
**[One-sentence axiom stating the core development and outcome.]**

- **Why it matters:** [1-2 concise sentences explaining the business impact, customer benefit, or risk mitigation using active voice.]
- **The big picture:** [Brief context on the friction or market change that triggered this decision.]

## Go Deeper
- **Core Decision:** [The explicit choice made or recommended.]
- **Trade-offs Evaluated:** [Key alternative rejected because of specific constraint.]
- **Key Risk & Mitigation:** [Primary risk and how it is contained.]

## By the Numbers
- **[Metric 1]:** [Quantified baseline vs target, e.g. 450ms $\to$ 85ms p95 latency]
- **[Metric 2]:** [Financial/Cost impact, e.g. \$45k monthly AWS egress savings]
- **[Metric 3]:** [Timeline or adoption target, e.g. 100% rollout by 2026-09-15]

## What's Next
| Single Owner (DRI) | Imperative Action Item | Hard Deadline |
| :--- | :--- | :--- |
| @Name | [Imperative verb + concrete deliverable] | YYYY-MM-DD |
```

### Template B: Amazon 1-Page Narrative Format (High-Stakes Proposals)

```markdown
# [Strategic Proposal Title under 10 words]
**Date:** YYYY-MM-DD | **Author:** @Name | **Framework:** Amazon 1-Pager

## 1. The "So What?" (Executive Thesis)
**[Strategic Headline under 10 words]**
[1-2 paragraphs detailing the customer problem, proposed mechanism, and outcome.]

## 2. Customer Working Backwards Rationale
- **Target Customer & Pain:** [Who suffers from this problem and what is the friction cost?]
- **The Solution Experience:** [How the customer workflow changes after implementation.]

## 3. Decision Classification & Strategic Impact
- **Classification:** `Type 1 (Irreversible / One-Way Door)` OR `Type 2 (Reversible / Two-Way Door)`
- **Strategic Impact:** [Scope of impact, reversibility cost, and blast radius.]

## 4. Analysis of Alternatives & Rejected Options
| Option | Core Trade-off | Reason for Rejection |
| :--- | :--- | :--- |
| [Alternative 1] | [Pros / Cons] | [Rejected because of specific limitation] |
| [Alternative 2] | [Pros / Cons] | [Rejected because of specific limitation] |

## 5. Dissent, Risks & Open Tenets (Disagree & Commit)
- **Documented Dissent:** [@Stakeholder raised concerns regarding X.]
- **Mitigation:** [Agreed containment mechanism.]

## 6. Execution Roadmap & Single DRI Matrix
| Directly Responsible Individual (DRI) | Deliverable Milestone | Target Date |
| :--- | :--- | :--- |
| @Name | [Measurable milestone with imperative verb] | YYYY-MM-DD |
```

---

## Non-Negotiable Rules

1. **Zero Thread Pasting:** Never paste raw quotes or conversational back-and-forth. Extract and synthesize the underlying facts and decisions.
2. **Mandatory Signposting (Smart Brevity):** In Smart Brevity mode, bold signposts (**Why it matters:**, **By the numbers:**, **What's next:**) are required.
3. **Single-DRI Accountability:** Every action item MUST have exactly one human owner and a hard date (`YYYY-MM-DD`). Shared ownership (`@Team`, `@Devs`) is strictly prohibited.
4. **Deterministic Technical Prose (ASD-STE100):** Use `because` (not *since*/*as*), `after` (not *once*), `can`/`must` (never *may*). Action sentences $\le 20$ words.
5. **No Filler or Pleasantries (`info-to-ink`):** Omit all greetings, sign-offs, and throat-clearing. Deliver 100% signal density.

---

## Quality Scoring Rubric

Evaluate generated async memos across 5 pillars (Max Score: 20 points):

| Pillar | 0 - Failing | 1 - Poor | 2 - Adequate | 3 - Strong | 4 - World-Class |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Executive Scannability** | Walls of unformatted text. | Basic bullets with mixed topics. | Structured sections but wordy paragraphs. | Clear Smart Brevity signposts and scannable bullets. | Instant executive comprehension in $<60$ seconds. |
| **2. Single-DRI Accountability** | No action items. | Vague tasks or shared team tags. | Named owners without deadlines. | 1 DRI per item with clear deadlines. | 1 DRI per item, imperative STE verbs, verifiable deliverables, and hard dates. |
| **3. Information-to-Ink Ratio** | Fluffy prose with conversational filler. | Wordy summaries with redundant phrasing. | Concise but retains non-essential context. | High token compression; zero pleasantries. | 100% signal density; every word carries operational weight. |
| **4. Technical Precision & Style** | Passive, ambiguous prose. | Weak action verbs and loose connectors. | Standard business English. | Active voice and STE connectors (`because`, `after`). | Flawless ASD-STE100 + Strunk & White compliance: active, positive, $\le 20$ words. |
| **5. Quantification & Evidence** | No data or metrics cited. | Vague estimates ("much faster", "cheaper"). | Isolated metric without baseline comparison. | Clear baselines and quantified ROI targets. | Precise By-the-Numbers section with verified metrics and cost models. |

---

## Completion Gate

Before finalizing any async memo, verify:
- [ ] Headline is under 10 words, starts with an action verb/noun, and has no exclamation points.
- [ ] Smart Brevity signposts (**Why it matters:**, **By the numbers:**, **What's next:**) are present.
- [ ] Every action item has exactly one human DRI and begins with an imperative verb.
- [ ] Sentences adhere to length limits ($\le 20$ words procedural, $\le 25$ words descriptive).
- [ ] Conversational noise, filler words, and throat-clearing are eliminated.
- [ ] Output is written in active voice and positive form.
