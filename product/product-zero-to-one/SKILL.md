---
name: product-zero-to-one
description: "Trigger: 0-to-1 product, zero to one, customer discovery, finding product market fit, PMF engine, lean startup MVP, problem solution fit, opportunity solution tree, leap of faith assumption, Steve Blank customer dev, Teresa Torres continuous discovery, Rahul Vohra PMF 40%, Clayton Christensen JTBD, Ash Maurya lean canvas, Jake Knapp design sprint, prototype testing. Scope: Leading early-stage 0-to-1 product discovery, navigating market uncertainty, formulating testable hypotheses, and driving toward verified Product-Market Fit (PMF). Formulates Steve Blank Customer Development interviews, Teresa Torres Opportunity Solution Trees, Rahul Vohra's 40% 'very disappointed' survey scoring, Eric Ries Lean Startup feedback loops, Clayton Christensen Jobs-to-be-Done forces, and Ash Maurya Lean Canvas risk prioritizations. Boundary: Excludes post-PMF acquisition funnel scaling (use product-growth), high-scale checkout UX optimizations (use product-optimizer-feature), or two-sided liquidity balancing (use product-marketplace)."
---

# Rule: 0-to-1 Product Management & Customer Discovery

> [!IMPORTANT]
> **Expert Attribution**: This skill embeds the documented frameworks and methodologies of **Steve Blank** (Customer Development), **Eric Ries** (Lean Startup), **Teresa Torres** (Continuous Discovery Habits), **Rahul Vohra** (Superhuman PMF Engine), **Clayton Christensen** (Jobs to be Done), **Ash Maurya** (Lean Canvas), and **Jake Knapp** (Design Sprints).

---

## When to use

Use this skill when exploring, shaping, or launching new products, zero-to-one capabilities, or major venture bets before Product-Market Fit:
- Conducting customer problem discovery interviews and identifying unmet needs.
- Mapping opportunities and testing high-risk assumptions using Opportunity Solution Trees (OST).
- Formulating Minimum Viable Products (MVPs), Concierge prototypes, or Wizard-of-Oz experiments.
- Measuring Product-Market Fit quantitatively using Rahul Vohra's 40% "Very Disappointed" metric.
- Deconstructing customer switching friction using Christensen's Four Forces of Progress (JTBD).

## When not to use

Do not use this skill for:
- Scaling post-PMF growth loops, referral flywheels, or paid ad channels (use `product-growth`).
- Optimizing existing feature workflows, checkout funnels, or usability micro-interactions (use `product-optimizer-feature`).
- Multi-sided marketplace liquidity balancing and take-rate elasticity (use `product-marketplace`).

## Trigger cues

- Request mentions: `0-to-1 product`, `zero to one`, `customer discovery`, `find product-market fit`, `PMF engine`, `lean startup`, `problem-solution fit`, `opportunity solution tree`, `leap of faith assumption`, `Steve Blank`, `Teresa Torres`, `Rahul Vohra`, `Clayton Christensen`, `JTBD`, `Ash Maurya`, `design sprint`.
- Scenarios involving early-stage ideation, pre-PMF validation, customer interview synthesis, or MVP experiment design.

## Routing boundary

- Route post-PMF retention flywheels and growth loops to `product-growth`.
- Route core feature optimization and usability heuristics to `product-optimizer-feature`.
- Route two-sided supply-demand matching to `product-marketplace`.

## Inputs required

1. **Target Customer Persona & Market Context**: Initial hypothesis on target user / ICP.
2. **Observed Problem or Customer Tension**: The raw pain point or market friction.
3. **Proposed Value Proposition & Solution Hypothesis**: The early concept or capability idea.
4. **Core Leap-of-Faith Assumptions (LOFAs)**: The riskiest assumptions (Value, Usability, Feasibility, Viability).
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Deconstruct the Customer Problem via Jobs-to-be-Done (Clayton Christensen)**:
   - Map the **Four Forces of Progress**:
     - *Push of the Present*: Current frustrations, costs, and pain points.
     - *Pull of the New*: Desired outcome and transformational superpower.
     - *Anxiety of the New*: Fear of switching, setup friction, learning curve.
     - *Habit of the Present*: Inertia, existing workflows, comfort with status quo.
3. **Execute Customer Discovery (Steve Blank & Teresa Torres)**:
   - Structure open-ended discovery interviews focused on past actual behaviors (not hypothetical future promises).
   - Build an **Opportunity Solution Tree (OST)**:
     $$	ext{Desired Outcome} \longrightarrow 	ext{Customer Opportunities (Pains/Needs)} \longrightarrow 	ext{Solution Concepts} \longrightarrow 	ext{Assumption Tests}$$
4. **Formulate the Lean Canvas & Leap-of-Faith Assumptions (Ash Maurya & Eric Ries)**:
   - Identify the single riskiest assumption across the 4 risk dimensions:
     - *Value Risk*: Do customers care enough to switch?
     - *Usability Risk*: Can they figure out how to use it?
     - *Feasibility Risk*: Can we build it with current technology?
     - *Business Viability Risk*: Can we acquire and monetize sustainably?
5. **Design the Minimum Viable Experiment (Jake Knapp & Eric Ries)**:
   - Design the lowest-fidelity test that can falsify the assumption: *Interactive Prototype, Concierge MVP, Wizard-of-Oz, or Smoke Test*.
   - Define explicit falsification criteria before running the test.
6. **Measure Quantitative Product-Market Fit (Rahul Vohra)**:
   - Survey users: *"How would you feel if you could no longer use this product?"*
   - Target benchmark: $\ge 40\%$ answering **"Very Disappointed"**.
   - Isolate High-Expectation Customers (HXC), analyze what they love, and build roadmap around amplifying their core delight while fixing blockers for the "Somewhat Disappointed" cohort.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- JTBD Four Forces analysis (Push, Pull, Anxiety, Habit).
- Opportunity Solution Tree structure (Outcome -> Opportunities -> Solutions -> Tests).
- Identification of Leap-of-Faith Assumptions (LOFAs) with explicit falsification criteria.
- Rahul Vohra 40% PMF benchmark and HXC segmentation strategy.

## Output format

- **Executive 0-to-1 Discovery Summary**: Problem statement, target ICP, and validation milestone.
- **Jobs-to-be-Done Four Forces Canvas**: Push vs Pull vs Anxiety vs Habit analysis.
- **Opportunity Solution Tree (OST)**: Structured opportunity hierarchy with competing solutions.
- **Riskiest Assumption Test (RAT) Plan**: LOFA, MVP experiment design, and falsification threshold.
- **Product-Market Fit Engine Roadmap**: Rahul Vohra survey scoring plan and HXC roadmap prioritization.
