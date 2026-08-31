# Opportunity Solution Tree (OST) & Continuous Discovery Framework

## 1. The 4-Tier Opportunity Solution Tree Architecture

The Opportunity Solution Tree (OST), developed by **Teresa Torres** (*Continuous Discovery Habits*) and championed by **Marty Cagan** (*Inspired*, *Empowered*), provides a visual roadmap for continuous product discovery. It ensures product teams connect high-level business and product outcomes to real customer pain points before exploring multiple potential solutions and running targeted assumption tests.

```mermaid
flowchart TD
    subgraph Tier1["Tier 1: Desired Outcome"]
        O["<b>Desired Outcome</b><br/><i>Single measurable metric</i><br/>e.g., Increase 30-day active retention from 25% to 40%"]
    end

    subgraph Tier2["Tier 2: Opportunity Space (Problem Space)"]
        OP1["<b>Parent Opportunity A</b><br/><i>'I cannot easily find relevant content'</i>"]
        OP2["<b>Parent Opportunity B</b><br/><i>'I forget to return to complete my workflow'</i>"]
        OP1_1["<b>Sub-Opportunity A.1</b><br/><i>'Search filters are too rigid'</i>"]
        OP1_2["<b>Sub-Opportunity A.2</b><br/><i>'Recommendations feel generic'</i>"]
    end

    subgraph Tier3["Tier 3: Solution Space (Ideation)"]
        S1["<b>Solution 1</b><br/>Natural language search bar"]
        S2["<b>Solution 2</b><br/>Tag-based interactive filters"]
        S3["<b>Solution 3</b><br/>Collaborative peer bookmarking"]
    end

    subgraph Tier4["Tier 4: Assumption Tests (Experimentation)"]
        AT1["<b>Value Assumption Test</b><br/>Fake-door test on search queries"]
        AT2["<b>Usability Assumption Test</b><br/>Clickable prototype usability test"]
        AT3["<b>Feasibility Assumption Test</b><br/>LLM latency spike benchmark"]
    end

    O --> OP1
    O --> OP2
    OP1 --> OP1_1
    OP1 --> OP1_2
    OP1_1 --> S1
    OP1_1 --> S2
    OP1_1 --> S3
    S1 --> AT1
    S1 --> AT2
    S1 --> AT3
```

---

## 2. Framing Opportunities vs. Feature Ideas

An opportunity is a customer need, pain point, friction point, or desire. It resides strictly in the **problem space**, whereas features belong in the **solution space**.

| Dimension | Poorly Framed (Feature Trap) | Properly Framed Opportunity (Customer Voice) |
| :--- | :--- | :--- |
| **Search & Discovery** | *"Build an AI semantic search engine."* | *"I cannot find items when I don't know the exact technical keyword."* |
| **Onboarding** | *"Create a 5-step tutorial tooltip walkthrough."* | *"I don't understand the core value proposition within my first 2 minutes."* |
| **Collaboration** | *"Add Google Docs-style real-time comments."* | *"I lose context when discussing changes outside our primary workspace."* |
| **Notifications** | *"Send daily push notification digests."* | *"I miss critical project deadlines because reminders get buried in email."* |
| **Billing & Plans** | *"Integrate Stripe tiered subscription checkout."* | *"I cannot predict our monthly spend as our team size fluctuates."* |

---

## 3. The 5 Product Risk Dimensions (Marty Cagan & Teresa Torres)

When evaluating solutions, teams must deconstruct each idea into its foundational assumptions across five core risk dimensions:

```mermaid
mindmap
  root((5 Product Risks))
    Value / Desirability
      Will customers choose this?
      Is the pain acute enough to pay or switch?
      Does it solve the core opportunity?
    Usability
      Can users figure out how to use it?
      Is the cognitive load acceptable?
      Can users complete the flow unaided?
    Feasibility
      Can engineering build it?
      Do we have the technical skills and time?
      Are third-party dependencies reliable?
    Viability
      Does it align with business and pricing model?
      Are there legal, regulatory, or compliance issues?
      Can Sales and Customer Success support it?
    Ethics & Safety
      Does it create dark patterns or user harm?
      Are data privacy and security maintained?
      Could it introduce algorithmic bias?
```

### Risk Dimension Breakdown

1. **Value Risk (Desirability)**:
   - *Question*: Will customers buy it or choose to use it?
   - *Key Assumption*: Users perceive enough value to alter existing habits or pay money.
   - *Testing Method*: Smoke tests, landing page conversion tests, LOI (Letter of Intent) requests, user interviews.

2. **Usability Risk**:
   - *Question*: Can users figure out how to use it effectively?
   - *Key Assumption*: Users intuitively understand UI affordances, terminology, and workflows.
   - *Testing Method*: Unmoderated usability sessions, clickable prototypes, task completion time studies.

3. **Feasibility Risk**:
   - *Question*: Can our engineers build and scale this with available time and technology?
   - *Key Assumption*: Backend algorithms, third-party APIs, and databases can meet performance, scale, and latency requirements.
   - *Testing Method*: Technical spikes, proof-of-concept benchmarks, load testing on mock endpoints.

4. **Viability Risk**:
   - *Question*: Does this solution work for the business as a whole?
   - *Key Assumption*: Solution complies with legal (GDPR/HIPAA), finance (unit economics), sales, marketing, and brand guidelines.
   - *Testing Method*: Cross-functional stakeholder reviews, margin calculations, legal compliance audits.

5. **Ethics & Safety Risk**:
   - *Question*: Does this solution create unintended negative consequences or exploit users?
   - *Key Assumption*: Data handling is fair, transparent, and non-exploitative.
   - *Testing Method*: Ethical pre-mortems, bias testing on datasets, privacy threat modeling.

---

## 4. Assumption Mapping & Rapid Testing Matrix

Instead of building full Minimum Viable Products (MVPs) to test a whole solution, teams map individual assumptions on a 2x2 grid to isolate high-risk unknowns.

```
       HIGH IMPORTANCE (Failure is fatal to the solution)
                           │
             LEAP OF FAITH │ PLAN & PROCEED
           ┌───────────────┼───────────────┐
           │   TEST NOW    │  BUILD WITH   │
           │ (Experiment)  │  CONFIDENCE   │
           │               │               │
LOW EVIDENCE ──────────────┼─────────────── HIGH EVIDENCE
(Unknown / Guess)          │               (Validated / Known)
           │  EVALUATE     │   IGNORE /    │
           │   LATER       │    PRUNE      │
           └───────────────┼───────────────┘
                           │
       LOW IMPORTANCE (Minor inconvenience if wrong)
```

### Rapid Experiment Types

| Experiment Type | Cost / Speed | Best For Testing | Concrete Example |
| :--- | :--- | :--- | :--- |
| **Fake-Door / Smoke Test** | Low ($<1$ day) | Value & Demand | Adding a "Generate AI Summary" button that triggers a "Coming Soon / Join Waitlist" modal to measure intent clicks. |
| **Concierge Prototype** | Low ($1–2$ days) | Value & Feasibility | Manually matching candidates via spreadsheet behind a mockup interface to test workflow viability before writing code. |
| **Clickable Prototype Test** | Medium ($2–3$ days) | Usability & Desirability | Testing an interactive Figma prototype with 5 target users to observe task completion friction. |
| **Technical Spike** | Medium ($2–4$ days) | Feasibility & Scale | Writing a standalone script querying vector database endpoints to benchmark latency under 10k QPS. |
| **Wizard of Oz** | Medium ($3–5$ days) | Value & Interaction Flow | Presenting an automated UI while a human manually fulfills backend tasks behind the scenes. |

---

## 5. Continuous Discovery Triad Operational Cadence

The **Product Triad** (Product Manager, Product Designer, Tech Lead) discovers together in continuous weekly loops.

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Target User / Customer
    participant Triad as Discovery Triad (PM + Designer + Tech Lead)
    participant OST as Opportunity Solution Tree
    participant Backlog as Delivery Pipeline

    Note over Triad,OST: Weekly Discovery Cadence
    Triad->>Customer: Conduct Weekly Discovery Interview (45 min)
    Customer-->>Triad: Unpacks story, friction, unmet desires
    Triad->>OST: Extract & update Opportunity hierarchy
    Triad->>OST: Diverge on candidate solutions for top opportunity
    Triad->>OST: Map assumptions & identify Leap-of-Faith risks
    Triad->>Customer: Run 24-48h rapid assumption test (Prototype/Smoke)
    Customer-->>Triad: Generates behavioral evidence
    alt Assumption Validated
        Triad->>Backlog: Handoff solution to PRD / God-Marduk execution
    else Assumption Invalidated
        Triad->>OST: Pivot to alternative solution under same opportunity
    end
```

---

## 6. Anti-Patterns & Systematic Repairs

| Anti-Pattern | Manifestation | Root Cause | Systematic Repair |
| :--- | :--- | :--- | :--- |
| **Solution First / Orphan Solutions** | Feature list masquerading as a discovery roadmap without linked customer problems. | Team starts with exciting ideas rather than customer pain points. | Force every solution to attach as a child node under a validated Opportunity node in the OST. |
| **Whether-or-Not Trap** | Team debates whether to build Solution A vs. doing nothing at all. | Fixating on the first idea generated (confirmation bias). | Enforce generating at least 3 distinct competing solutions per sub-opportunity before testing. |
| **Testing Whole MVPs** | Spending 6 weeks building software just to test if users want a feature. | Conflating delivery with discovery. | Isolate the top Leap-of-Faith assumption and run a 1-day smoke test or prototype test instead. |
| **Outcome Shifting** | Changing metrics mid-stream when a solution fails to perform. | Lack of strategic commitment to the target outcome. | Lock the root Desired Outcome node; change solutions and opportunities, not the goal. |
| **The Scribe PM** | PM interviews customers alone and passes notes down to design and engineering. | Siloed functional hierarchy. | Involve Product Designer and Tech Lead in every discovery interview and assumption mapping session. |
