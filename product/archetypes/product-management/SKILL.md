---
name: product-management
description: "Trigger: product management, product archetype, 0-to-1 search, growth loops, feature optimization, 2-sided marketplace, PM routing, PM framework. Scope: Master Product Management Archetype Router. Identifies optimal mental models and execution playbooks across 0-to-1, Growth, Optimizer, and Marketplace archetypes. Boundary: Excludes authoring full PRDs (use create-prd) or code implementation."
---

# Product Management

Defines and clarifies product vision, PRD requirements, problem alignment, and execution roadmaps. Directs general product initiatives and routes specialized domain challenges to dedicated product archetype skills.

---

## Specialized Product Archetype Routing

When your product challenge matches a specialized domain archetype, consult or delegate to the corresponding specialized product archetype skill:

- **0-to-1 Product Management (`product-zero-to-one`)**:
  - *When to route*: Early-stage discovery, navigating extreme uncertainty, finding Product-Market Fit (PMF), formulating hypotheses, conducting customer problem interviews.
  - *Core Experts & Frameworks*: Steve Blank (Customer Development), Eric Ries (Lean Startup & MVPs), Teresa Torres (Opportunity Solution Trees), Rahul Vohra (40% PMF Engine), Clayton Christensen (JTBD 4 Forces of Progress), Ash Maurya (Lean Canvas).

- **Growth Product Management (`product-growth`)**:
  - *When to route*: Post-PMF acquisition loops, referral flywheels, onboarding activation milestones ($N$ actions in $T$ days), natural frequency of use, habit-forming retention hooks.
  - *Core Experts & Frameworks*: Brian Balfour (4 Growth Fits & Compounding Loops), Fareed Mosavat (Retention-First & Natural Frequency), Elena Verna (Product-Led Growth), Nir Eyal (Hooked Model), Josh Elman (The Core Action), Lenny Rachitsky (7 Growth Channels).

- **Optimizer / Feature Product Management (`product-optimizer-feature`)**:
  - *When to route*: Refining and scaling existing core product surfaces, eliminating the "Feature Factory" trap, checkout and form optimization, usability friction removal.
  - *Core Experts & Frameworks*: Marty Cagan (4 Product Risks: Value, Usability, Feasibility, Viability), John Cutler (4D Metric Trees), Shreyas Doshi (Pre-Mortem & High-Agency Judgment), Don Norman (Affordances & Signifiers), Steve Krug (Don't Make Me Think), Baymard Institute (Checkout UX), Jeff Patton (Story Mapping).

- **Marketplace Product Management (`product-marketplace`)**:
  - *When to route*: Two-sided or multi-sided platform dynamics (Demand vs Supply), bootstrapping atomic networks, cold start problems, subsidizing the hard side, marketplace liquidity (Fill Rate, Search-to-Book), take-rate economics.
  - *Core Experts & Frameworks*: Andrew Chen (The Cold Start Problem & Atomic Networks), Casey Winters (Marketplace Loops), Dan Hockenmaier (Liquidity Dynamics), Bill Gurley (10 Marketplace Rules), Gokul Rajaram (SPADE Framework).

---

## When to use

Use this skill when defining product vision, scoping PRDs, prioritizing roadmaps, or framing problem-solution narratives.

## When not to use

Do not use this skill for:
- Low-level source code implementation (use relevant engineering skills).
- Visual UI component layout or CSS styling (use `design-system-rules` or `shadcn-ui`).
- Specialized archetype deep-dives (use `product-zero-to-one`, `product-growth`, `product-optimizer-feature`, or `product-marketplace`).

## Trigger cues

- Request mentions: `product management`, `PM`, `PRD`, `user story`, `roadmap`, `problem alignment`, `product narrative`, `feature scoping`, `product requirements document`.
- Requests to structure product requirements, define measurable success metrics, or decompose user journeys.

## Inputs required

1. **Goal or Product Intent**: The target user outcome and business objective.
2. **Current Constraints**: Time, resources, technical boundaries, regulatory risk.
3. **Target Persona & Context**: Target audience and observed pain points.
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Determine Product Archetype**:
   - Check if the task is primarily **0-to-1 Discovery** (`product-zero-to-one`), **Growth/Retention** (`product-growth`), **Feature Optimization** (`product-optimizer-feature`), or **Two-Sided Marketplace** (`product-marketplace`). If specialized, incorporate that archetype's specific framework.
3. **Structure Problem Alignment**:
   - Define the specific problem being solved, evidence of customer pain, and business justification.
4. **Author Decision-Ready PRD Specifications**:
   - **Problem & Goals**: State measurable outcomes and explicit Non-Goals.
   - **Target Persona & Use Cases**: Specific customer circumstance and job.
   - **Solution Architecture & Key Flows**: User journeys, error states, and edge cases.
   - **Success Metrics & Impact Checklist**: Primary KPI, guardrail metrics, permissions, pricing, security.
5. **Enforce Execution Discipline**:
   - Keep requirements unambiguous, deterministic, and testable.

## Output format

- **Executive Product Summary**: Problem statement, target customer, and core thesis.
- **Archetype Lens & Routing**: Identified product archetype and expert framework applied.
- **Decision-Ready PRD Specification**: Problem, Goals, Non-Goals, Key Flows, and Edge Cases.
- **Success Metrics & Guardrails**: Primary KPI, input metrics, and constraint thresholds.
