---
name: premortem-kill-criteria
description: "Conduct premortem risk assessments and define explicit kill criteria for risky product bets."
---

# PREMORTEM & KILL CRITERIA GOVERNANCE

Conduct rigorous prospective hindsight analyses, define objective pre-committed kill/pivot criteria, and design psychological off-ramps to combat escalation of commitment and the sunk cost fallacy.

## Operating Boundary

- **Triggers:** Premortem analysis, kill criteria, quitting thresholds, Adam Thomas survival metrics, prospective hindsight exercises, Gokul Rajaram SPADE kill milestones, project off-ramps, sunk cost reviews, assumption stress-testing, pivot governance, pre-mortem risk mapping.
- **Cross-Domain Scope:** Multi-quarter strategic bets, 0-to-1 product launches, high-risk infrastructure migrations, M&A integrations, venture experiments, new market expansions, platform rewrites.
- **Anti-Triggers / Exclusions:** Routine sprint retrospectives (use `scrum-review-and-retro`), basic Jira issue risk labeling, real-time production incident postmortems, or day-to-day sprint capacity planning.

## Theoretical Foundations

1. **Prospective Hindsight (Gary Klein & Daniel Kahneman):** Imagining a future catastrophic failure eliminates confirmation bias, breaks social conformity/groupthink, and creates psychological safety to surface systemic vulnerabilities before capital is deployed.
2. **Pre-Committed Kill Criteria & Quitting Science (Annie Duke):** Defining explicit "states and dates" before starting an initiative neutralizes cognitive biases (sunk cost fallacy, status quo bias, endowment effect). Quitting is recognized as decision optimization, not failure.
3. **Survival Metrics (Adam Thomas):** Continuous calibration across three vital operational axes—**Fast** (learning velocity), **Focus** (alignment with core strategic intents), and **Safe** (containment of blast radius and psychological safety to flag failure).
4. **SPADE Framework with Decision Gates (Gokul Rajaram):** Structural clarity on **S**etting, **P**eople (Decider vs. Approver vs. Consulted), **A**lternatives, **D**ecision, and **E**xplanation—embedded with non-negotiable review milestones.
5. **Data vs. Opinion Decision Matrix (Tony Fadell — *Build* Ch 5):** Separate decisions governed by **Data** (known parameters, telemetry, conversion funnels) from decisions governed by **Informed Opinion / Conviction** (0-to-1 novel bets where no prior data exists). Stop teams from hiding behind endless A/B tests on conviction bets.

---

## Inputs Required

1. **Initiative Charter:** Core objective, proposed architecture/solution, strategic hypothesis, committed budget/headcount, and targeted delivery window.
2. **Strategic Context:** Upstream Strategic Intents (from `decision-stack-governance`) and make-or-break product assumptions (from `product-hypothesis-loop`).
3. **Stakeholder & Decision Roles:** Identified Decider, Approvers, and Independent Arbiter ("Quitting Coach").
4. **Historical Reference Class Data:** Past failure rates, actual vs. estimated timeline variances in similar legacy projects.
5. **Source of Truth:** Consult [references/source.md](references/source.md).

---

## Instructions

1. Review [references/source.md](references/source.md) for canonical execution frameworks, math models, and facilitation scripts.
2. Execute the **5-Stage Premortem & Kill Criteria Protocol**:

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Stage 5: Sunk Cost Circuit Breaker & Governance Cadence               │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Stage 4: Survival Metrics Calibration (Fast, Focus, Safe)              │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Stage 3: Objective Kill Criteria Matrix ("States and Dates")           │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Stage 2: Failure Taxonomy & Root-Cause Clustering                      │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Stage 1: Prospective Hindsight Simulation (Total Catastrophe)          │
 └────────────────────────────────────────────────────────────────────────┘
```

### 1. Stage 1: Prospective Hindsight Simulation
- Establish the temporal anchor: *"Fast-forward 12 months. The initiative has suffered a complete, humiliating failure. The product was canceled, budget incinerated, and customer trust damaged."*
- Enforce silent, independent brainstorming for 10 minutes to eliminate anchoring and hierarchy bias.
- Mandate that every participant submit at least 3 concrete failure mechanisms across Technical, Commercial, Operational, and Behavioral domains.

### 2. Stage 2: Failure Taxonomy & Vulnerability Clustering
- Cluster submitted failure narratives into distinct root-cause categories:
  - **Viability / Market Failure:** Lack of demand, negative unit economics, competitor counter-attack.
  - **Technical / Feasibility Failure:** Scalability bottlenecks, integration collapse, unresolvable latency.
  - **Usability / Adoption Failure:** High user cognitive friction, failed workflow integration.
  - **Organizational / Execution Failure:** Resourcing starvation, dependency deadlock, scope creep.
- Rank threats using the **Expected Failure Severity Score**:
  $$\text{Severity} = \text{P(Occurrence)} \times \text{Impact} \times \text{Detection Latency}$$

### 3. Stage 3: Architect Objective Kill Criteria ("States & Dates")
- For the top-ranked failure modes, formulate strict, falsifiable Annie Duke Kill Criteria using the deterministic syntax:
  $$\text{IF } [\text{Leading Indicator / State } X] \text{ is observed by } [\text{Milestone / Date } Y], \text{ THEN } [\text{Mandated Action: Kill / Pivot / Downscope } Z].$$
- Classify criteria into four mandatory tiers:
  - **Hard Kill Trigger:** Irrevocable project termination and immediate resource reallocation.
  - **Pivot Trigger:** Compulsory alteration of architecture, value proposition, or distribution vector.
  - **Downscope Trigger:** Stripping secondary features to preserve the core hypothesis and delivery timeline.
  - **Re-evaluation Gate:** Formal executive go/no-go review with an independent arbiter.

### 4. Stage 4: Calibrate Adam Thomas Survival Metrics
- Establish leading tracking telemetry across three survival dimensions:
  - **Fast:** Maximum acceptable cycle time for qualitative/quantitative hypothesis feedback (e.g., $< 14$ days per experiment cycle).
  - **Focus:** Threshold of team time dedicated strictly to core initiative goals (e.g., $> 75\%$ time on core problem; $< 25\%$ on unplanned firefighting).
  - **Safe:** Blast radius containment and psychological safety score (e.g., zero irreversible data loss risks, quarterly blameless check-ins).

### 5. Stage 5: Enforce the Sunk Cost Circuit Breaker
- Appoint a designated **Independent Arbiter ("Quitting Coach")** who has zero reputational or political stake in the project's continuation.
- Schedule recurring Kill Gate reviews synchronized with roadmap milestones.
- Strip all consideration of past expenditures (capital, engineering hours, emotional investment) during evaluation:
  $$\text{Decision Rule: Proceed ONLY IF } \mathbb{E}[\text{Future Value}] > \text{Future Cost} + \text{Opportunity Cost of Capital}.$$

---

## Non-Negotiable Rules

1. **Pre-Commitment Invariance:** Kill criteria must be documented and signed off *before* engineering execution begins. Never allow goalpost shifting after negative data emerges.
2. **Explicit Leading Indicators:** Kill triggers must rely on leading behavioral and technical indicators, not trailing financial metrics (e.g., track Day-7 active usage velocity, not Year-1 revenue).
3. **Zero Sunk Cost Evaluation:** Past investments are economically irrelevant. Evaluate purely on forward-looking expected value and alternative capital allocation.
4. **Independent Arbiter Authority:** The project sponsor cannot unilaterally override a triggered kill condition. Overriding a Hard Kill trigger requires formal executive escalation and unanimous approval.
5. **No Punitive Quitting:** Terminating an initiative based on pre-committed kill criteria must be celebrated as a victory of disciplined capital allocation and learning.

---

## Completion Gate

Before finalizing the premortem and kill criteria artifact, verify:
- [ ] Prospective hindsight simulation executed with documented, multi-disciplinary failure narratives.
- [ ] Failure modes clustered and scored with quantified severity metrics.
- [ ] Explicit Kill Criteria formulated in strict "States and Dates" format across Hard Kill, Pivot, and Downscope tiers.
- [ ] Adam Thomas Survival Metrics (Fast, Focus, Safe) defined with concrete operational thresholds.
- [ ] Independent Arbiter assigned with unambiguous decision rights.
- [ ] Review dates and circuit breaker milestones locked into the governance calendar.

---

## Output Format

1. **Executive Summary & Premortem Synthesis:** Core initiative overview, catastrophe scenario narrative, and primary vulnerability profile.
2. **Top Failure Vectors & Severity Scoring:** Tabular breakdown of failure modes, categories, probability, impact, and detection latency.
3. **The Kill Criteria Contract ("States & Dates"):** Concrete table detailing Trigger ID, State/Condition, Milestone/Date, Required Action (Kill/Pivot/Downscope), Verification Source, and Action Owner.
4. **Survival Metrics Operational Dashboard:** Target thresholds and measurement cadences for Fast, Focus, and Safe dimensions.
5. **Decision Governance & Off-Ramp Protocol:** Designated Independent Arbiter, milestone review schedule, and asset re-deployment playbook in the event of termination.
