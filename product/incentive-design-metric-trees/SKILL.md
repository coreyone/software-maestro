---
name: incentive-design-metric-trees
description: "Trigger: Metric tree decomposition, North Star Metric, input metrics, guardrail metrics, incentive design, Goodhart's law prevention, outcome vs output alignment, OKR metric alignment. Scope: Decomposing high-level North Star metrics into actionable input trees and counter-balancing guardrail metrics, aligning team incentives to customer/business outcomes rather than output theater. Boundary: Excludes payroll compensation administration or agile story point estimation."
---

# Rule: Metric Tree Decomposition & Incentive Architecture

## When to use

Use this skill when defining a company or product North Star Metric, decomposing top-line business goals into squad-level input metrics, establishing anti-Goodhart guardrails, or aligning team incentives to business outcomes.

## When not to use

Do not use this skill for employee compensation/payroll design or daily sprint velocity tracking.

## Trigger cues

- Request explicitly references `incentive-design-metric-trees` or North Star decomposition.
- Keywords: metric tree, North Star Metric, input metrics, guardrail metrics, incentive architecture, Goodhart's Law, output theater, outcome-based OKRs, KPI tree.

## Routing boundary

- Primary for mathematical metric decomposition, outcome incentive alignment, and guardrail design.
- Route strategic roadmaps to `decision-stack-governance` and R&D capitalization to `portfolio-allocation-capitalization`.

## Inputs required

- Company North Star Metric or primary business objective
- Squad charters and functional domain boundaries
- Potential unintended gaming risks (Goodhart's Law traps)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Select and define the **North Star Metric (NSM)**:
   - Must represent the intersection of *customer value delivered* and *business value captured*.
3. Decompose the NSM into a **Mathematical Metric Tree**:
   $$	ext{North Star} = f(	ext{Breadth} 	imes 	ext{Depth} 	imes 	ext{Frequency} 	imes 	ext{Efficiency})$$
   - Assign atomic **Input Metrics** to specific product squads (inputs must be directly influenceable by team actions).
4. Implement **Anti-Goodhart Guardrail Metrics**:
   - For every input metric, establish a pairing guardrail to prevent gaming (e.g., *Input: Sign-up conversion* $\leftrightarrow$ *Guardrail: Refund rate / 30-day churn*).
5. Align **Team Incentives & Review Mechanisms**:
   - Evaluate squads based on *movement in their assigned Input Metric under Guardrail constraints*, eliminating output theater (story points shipped).

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit North Star Metric definition with customer/business duality.
- Multi-branch Metric Tree decomposing NSM into actionable input levers.
- Explicit paired Guardrail metrics preventing Goodhart's Law gaming.

## Output format

- **North Star Metric Statement**: Definition and customer/business value linkage.
- **Metric Tree Hierarchy**: North Star $ightarrow$ Primary Drivers $ightarrow$ Squad Input Metrics.
- **Anti-Goodhart Guardrail Pairs**: Input vs Guardrail pairing table.
- **Outcome-Based Review Cadence**: How incentives are governed without output theater.
