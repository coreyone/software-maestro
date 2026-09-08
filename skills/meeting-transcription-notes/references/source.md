# Canonical References & Operational Standards: Meeting Intelligence

This document provides foundational theory, executive literature, transcript processing heuristics, and the integrated writing standards governing operational meeting notes.

---

## 1. Theoretical Foundations of the 5 Canonical Frameworks

### 1.1 The Minto Pyramid Principle & SCQA (Barbara Minto / McKinsey & Company)
- **Origin:** Developed by Barbara Minto during her tenure at McKinsey (*The Minto Pyramid Principle: Logic in Writing and Thinking*, 1987).
- **Core Axiom:** Human cognition processes ideas top-down. Raw chronological narration forces the listener to construct their own conclusions. To ensure alignment, state the recommendation first, followed by logically grouped arguments, supported by data.
- **SCQA Architecture:**
  - **Situation:** A non-controversial statement of the status quo that all participants agree upon.
  - **Complication:** A change, constraint, or external friction that introduces urgency.
  - **Question:** The core business dilemma prompted by the complication.
  - **Answer:** The synthesized recommendation or agreed operational direction.
- **MECE Standard:** Arguments must be **Mutually Exclusive** (no overlapping categories) and **Collectively Exhaustive** (no structural gaps in logic).

### 1.2 Amazon Silent Narrative & Two-Way Doors (Jeff Bezos / Amazon)
- **Origin:** Instituted by Jeff Bezos in 2004, replacing slide presentations with structured 6-page narrative memos read silently at the start of meetings (*Bezos Letters to Shareholders*, 2015).
- **Type 1 vs. Type 2 Decisions:**
  - **Type 1 (One-Way Doors):** Irreversible decisions with massive company-wide blast radius (e.g., acquisitions, database re-architecture). Require deep diligence, dissent, and high conviction.
  - **Type 2 (Two-Way Doors):** Reversible decisions that can be quickly unwound if wrong (e.g., UI experiments, pricing tweaks). Must be made rapidly by small autonomous teams with high bias for action.
- **Disagree and Commit (Leadership Principle #13):** Leaders are obligated to respectfully challenge decisions when they disagree, but once a decision is finalized, they commit entirely to its execution. Meeting notes must explicitly record dissent and subsequent commitment.

### 1.3 Directly Responsible Individual (DRI) & DAP (Steve Jobs / Apple)
- **Origin:** Standardized by Steve Jobs at Apple and documented by Adam Lashinsky in *Inside Apple* (2012).
- **The DRI Axiom:** When everyone is responsible for an outcome, no one is. Every project, meeting action item, and blocker must have a single named human being accountable for delivery.
- **DAP Framework:**
  - **Decisions:** Clear binary commitments made during the session.
  - **Actions:** Concrete deliverables tied strictly to a single DRI and hard deadline.
  - **Problems:** Active impediments and risks escalating to leadership.

### 1.4 Ray Dalio's Issue-Log & Machine Thinking (Bridgewater Associates)
- **Origin:** Codified by Ray Dalio in *Principles: Life and Work* (2017) and Bridgewater's management system.
- **Organization as a Machine:** An organization consists of *Culture* and *People* operating within a *Machine* (Processes and Designs). When outcomes fail, the goal is not to blame people, but to diagnose and re-engineer the machine.
- **5 Whys Root Cause Analysis:** Rooted in Taiichi Ohno's Toyota Production System (TPS), tracing an immediate symptom through 5 successive levels of inquiry to reveal underlying systemic design flaws.
- **Codified Principles:** Every failure must produce a generalizable operational principle added to the company's operating playbook so that identical mistakes never recur.

### 1.5 The 80/20 Minimum Viable Note (Tim Ferriss / First Principles)
- **Origin:** Derived from Vilfredo Pareto's Power Law and popularized by Tim Ferriss (*The 4-Hour Workweek*, *Tools of Titans*).
- **Asymmetric Leverage:** 80% of meeting content is social lubricant and low-leverage detail. Capturing everything wastes cognitive bandwidth.
- **The Core Triage:** Identify the **1 Thing** that moves the needle, locate the single **Bottleneck** (Eliyahu Goldratt's Theory of Constraints), and assign no more than 2–3 mission-critical action items.

---

## 2. Technical Language Standard (ASD-STE100 + Google DevDocs)

Integrate the **`technical-language-rules`** skill across all action items, technical architectural summaries, and postmortems:

### 2.1 Sentence Length & Structure Limits
- **Procedural steps / Action items**: $\le 20$ words per sentence.
- **Descriptive context / Rationale**: $\le 25$ words per sentence.
- **Noun Clusters**: Maximum 3 consecutive nouns. Unpack complex terms using prepositions (`for`, `of`, `during`).

### 2.2 Unambiguous STE Connector Substitutions
ASD-STE100 requires one exact meaning per word. Apply these substitutions strictly:

| Prohibited Word / Phrase | Mandatory STE Replacement | Rationale |
| :--- | :--- | :--- |
| `since` / `as` (causal) | **`because`** | *Since* and *as* relate strictly to time/duration. |
| `once` (conditional) | **`after`** | *Once* is ambiguous with frequency ("once upon a time"). |
| `may` | **`can`** or **`must`** | Use *can* for capability; use *must* for requirements. |
| `prior to` | **`before`** | Concise, direct standard English. |
| `in order to` | **`to`** | Eliminates superfluous wordiness. |
| `due to the fact that` | **`because`** | Eliminates passive throat-clearing. |

### 2.3 Imperative Action Mood
Every action item must start with an approved STE imperative verb:
- `Add`, `Deploy`, `Fix`, `Migrate`, `Configure`, `Implement`, `Verify`, `Refactor`, `Update`, `Remove`.
- ❌ *Sarah will be looking into updating the auth endpoint.*
- ✅ *`@Sarah`: Update auth endpoint validation to reject expired tokens by 2026-09-05.*

---

## 3. Output Token Compression & Noise Elimination (`info-to-ink`)

Maximize the information-to-ink ratio across all meeting records:

### 3.1 Drop Conversational Noise
- **Filler Words:** `um`, `uh`, `like`, `you know`, `basically`, `actually`, `literally`, `sort of`, `kind of`.
- **Pleasantries & Banter:** *"Thanks everyone for joining"*, *"Happy Monday"*, *"Great discussion team"*.
- **Hedging:** *"I think maybe we might want to consider..."* $\to$ *"Deploy..."*
- **Throat-Clearing:** *"The main thing I wanted to bring up is..."* $\to$ State the point immediately.
- **Wrap-Up Redundancies:** *"Let's circle back on this next week"*.

### 3.2 Preserve Technical Precision Exactly
Never abbreviate or summarize away critical technical tokens:
- Exact code identifiers, function names, and types (`` `verifyToken()` ``, `` `UserRecord` ``).
- File paths and repository names (`src/auth/jwt.ts`, `productivity-maestro`).
- Numerical metrics, latency figures, percentages, and financial sums (`450ms`, `99.95%`, `\$120,000`).
- Exact dates and deadlines (`YYYY-MM-DD`).

---

## 4. Strunk & White's Elements of Style Principles

Apply the core principles from Strunk & White (*The Elements of Style*):

### 4.1 Principle I: Structural Integrity & Paragraph Architecture
- Make the paragraph the unit of composition.
- Begin each section with a sentence that sets the operational context.
- Keep related ideas together and maintain parallel grammatical construction across list items.

### 4.2 Principle II: Economy & Brevity (Omission of Needless Words)
> *"Vigorous writing is concise. A sentence should contain no unnecessary words, a paragraph no unnecessary sentences, for the same reason that a drawing should have no unnecessary lines and a machine no unnecessary parts."*
- Express coordinate ideas in similar form.
- Use the active voice: Active verbs generate energy; passive verbs obscure responsibility.
  - ❌ *The latency issue was investigated by the platform squad.*
  - ✅ *The platform squad investigated the latency issue.*
- Put statements in positive form: Make direct assertions; avoid non-committal or evasive language.

---

## 5. Emotion-Provoking & Action-Driven Executive Copy

When synthesizing executive summaries, leadership readouts, and company-wide strategic narratives:

### 5.1 Punchy Executive Headlines
- Keep headlines under **10 words**.
- Start with a strong key power word or marketing verb.
- Do not start headlines with articles ("The", "A").
- Strictly no exclamation points.

### 5.2 Benefit-Focused & Urgent Strategic Framing
- Frame decisions around direct customer value and competitive leverage.
- Highlight the cost of inaction or the breakthrough velocity unlocked by the resolution.
- Use strong, confident verbs (`Pioneer`, `Accelerate`, `Streamline`, `Unify`, `Deliver`).

---

## 6. Synthesis Heuristic Transformation Examples

```
[Raw Transcript Input]
"Speaker 1 (Dave): Yeah so um thanks for joining everyone. Basically the reason why we are here is because our checkout API is super slow right now in Europe, like 1.2 seconds, and it is causing dropoffs. Alice, do you think we can fix this prior to Friday?
Speaker 2 (Alice): Well, I think the main reason is that we are hitting the US East database directly from Frankfurt. If we deploy Cloudflare Workers KV with read replicas, that should bring latency down to under 80ms. I can definitely get the caching layer implemented once Dan approves the migration budget.
Speaker 3 (Dan): Budget is approved. Let's do it. I'm slightly worried about cache invalidation bugs, but I'll disagree and commit so we can ship fast."

[Transformed Operational Decision Record — Amazon Narrative Format]
# European Checkout Latency Optimization — Strategic Narrative Record
**Date:** 2026-08-31 | **Attendees:** @Dave, @Alice, @Dan | **Framework:** Amazon Narrative

## 1. The "So What?" (Core Decision)
**Deploy Edge Caching to Slash European Checkout Latency**
Deploy Cloudflare Workers KV read replicas in Frankfurt to reduce European checkout latency from 1,200ms to <80ms and recover dropped conversions.

## 2. Decision Classification
- **Classification:** `Type 2 (Reversible / Two-Way Door)`
- **Strategic Impact:** Low blast radius; cached read replicas can be disabled instantly if inconsistencies occur.
- **Customer Impact:** Instant checkout responsiveness for EMEA buyers.

## 3. Discussion Points & Rationale
- EMEA checkout requests currently suffer 1,200ms latency because queries route across the Atlantic to US-East-1.
- Edge KV deployment provides local read caching with sub-80ms target response times.

## 4. Disagree & Commit (Documented Dissent)
- **Dissenting Perspective:** @Dan raised concerns regarding edge cache invalidation edge-cases.
- **Resolution:** @Dan approved the infrastructure budget and committed to the deployment after @Alice agreed to add cache-control validation checks.

## 5. Single-Owner Deliverables
| Single Owner | Imperative Action & Target Metric | Target Date |
| :--- | :--- | :--- |
| @Alice | Deploy Cloudflare Workers KV read replicas in Frankfurt with <80ms p95 latency | 2026-09-04 |
| @Alice | Add cache-control header validation tests before production traffic cutover | 2026-09-03 |
```

---

## 7. Canonical Bibliography

- **Barbara Minto:** *The Minto Pyramid Principle: Logic in Writing and Thinking* (Minto International, 1987)
- **Jeff Bezos:** *Invent and Wander: The Collected Writings of Jeff Bezos* (Harvard Business Review Press, 2020)
- **Ray Dalio:** *Principles: Life and Work* (Simon & Schuster, 2017)
- **Adam Lashinsky:** *Inside Apple: How America's Most Admired--and Secretive--Company Really Works* (Business Plus, 2012)
- **William Strunk Jr. & E.B. White:** *The Elements of Style* (4th Edition, Pearson, 1999)
- **AeroSpace and Defence Industries Association of Europe:** *ASD-STE100 Simplified Technical English* (Issue 8, 2021)
- **Google LLC:** *Google Developer Documentation Style Guide* (developers.google.com/style)
- **Tim Ferriss:** *The 4-Hour Workweek* (Crown Publishing, 2007)
