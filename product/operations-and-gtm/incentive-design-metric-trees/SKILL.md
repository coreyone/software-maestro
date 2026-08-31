---
name: incentive-design-metric-trees
description: "Trigger: Metric tree decomposition, North Star Metric, input metrics, guardrail metrics, incentive design, Goodhart's law prevention, outcome vs output alignment, OKR metric alignment, John Cutler North Star, Christina Wodtke OKRs, metric pre-mortem. Scope: Decomposing high-level North Star metrics into responsive 3R input trees (Breadth, Depth, Frequency, Efficiency), running Metric Pre-Mortems to prevent gaming, pairing anti-Goodhart guardrails, and enforcing weekly 4-quadrant health rhythms. Boundary: Excludes payroll compensation administration or agile story point estimation."
---

# Rule: North Star Metric Tree Decomposition, Anti-Goodhart Governance, & Incentive Architecture

## When to use

Use this skill when defining a company or product North Star Metric, decomposing top-line business goals into squad-level 3R input metrics, running metric pre-mortems to prevent Goodhart's Law gaming, establishing guardrail pairs, or structuring 4-quadrant OKR operating rhythms.

## When not to use

Do not use this skill for employee payroll compensation schemes, raw database telemetry instrumentation (use `analytics-event-tracking`), or sprint velocity tracking.

## Trigger cues

- Request explicitly references `incentive-design-metric-trees`, North Star Metric, or metric tree decomposition.
- Keywords: metric tree, North Star Metric, 3R input metrics, guardrail metrics, Goodhart's Law, metric pre-mortem, Cutler North Star, Wodtke OKR quadrants, outcome vs output, proxy metric invalidation.

## Routing boundary

- Primary for mathematical metric decomposition, input responsiveness validation, anti-gaming guardrail design, and outcome incentive alignment.
- Route strategic roadmaps to `decision-stack-governance` and R&D capitalization to `portfolio-allocation-capitalization`.

## Inputs required

- High-level business objective or proposed North Star Metric
- Squad domain boundaries and current team initiatives
- Potential gaming risks / vulnerability vectors
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Select and define the **North Star Metric (NSM)**:
   - Must capture the **Value Exchange Duality**: *Customer Value Delivered* $\cap$ *Business Value Captured*.
3. Decompose the NSM into the **4-Dimension Metric Tree**:
   $$\text{North Star} = f(\text{Breadth} \times \text{Depth} \times \text{Frequency} \times \text{Efficiency})$$
4. Validate Squad Input Metrics with the **3R Test (Cutler Model)**:
   - **Responsive**: Detectably shifts within 1–4 weeks of squad interventions (unlike lagging ARR).
   - **Representational**: Measures an observable customer behavioral shift (not internal task completion).
   - **Reflexive**: Moves in direct proportion to real customer value creation.
5. Execute the **Metric Pre-Mortem (Anti-Goodhart Gaming Simulation)**:
   - Ask: *"If an aggressive squad wanted to 5x this input metric without improving the product, how would they game it?"*
   - Use the simulated gaming vectors to establish mandatory **Paired Guardrail Metrics**.
6. Establish the **4-Quadrant Weekly Operating Rhythm (Wodtke Model)**:
   - *Q1: Active Bets & Hypotheses* (2–3 priority experiments).
   - *Q2: Input Metric Trend* (Week-over-week trajectory).
   - *Q3: Confidence Score (1–10)* (Team qualitative conviction).
   - *Q4: Health Invariants* (Customer trust, defect rate, team health).
7. Apply the **Proxy Invalidation Rule**: If an input metric increases for 2 consecutive quarters while the North Star remains flat, invalidate and prune the metric.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit North Star Metric definition with customer/business duality.
- 4-branch Metric Tree (Breadth, Depth, Frequency, Efficiency) passing the 3R test.
- Metric Pre-Mortem simulation with paired anti-Goodhart guardrails.
- 4-quadrant operating rhythm specification.

## Output format

- **North Star Metric Statement**: Definition and value exchange formula.
- **3R Metric Tree Hierarchy**: North Star $\to$ 4 Dimension Drivers $\to$ Squad Input Metrics.
- **Metric Pre-Mortem & Guardrail Pairing**: Gaming vectors and protective invariants.
- **4-Quadrant Operating Rhythm**: Weekly review structure and proxy pruning rules.
