---
name: portfolio-allocation-capitalization
description: "Trigger: Portfolio resource allocation, software capitalization, CapEx vs OpEx, R&D spend allocation, KTLO vs innovation, engineering theme budgeting, Athenahealth capitalization. Scope: Classifying and balancing engineering investments across Strategic/Innovation, Foundational Tech/Tech Debt, Reactive Trust/Bugs, and BAU/KTLO; automating software capitalization calculations and Jira work categorization for Finance. Boundary: Excludes standard bookkeeping journal entries or sprint backlog story estimation."
---

# Rule: Portfolio Resource Allocation & Software Capitalization

## When to use

Use this skill when allocating engineering and product capacity across strategic themes, modeling R&D spend, or calculating software capitalization (CapEx vs. OpEx) for finance reporting.

## When not to use

Do not use this skill for standard accounting journal entries or daily sprint task estimation.

## Trigger cues

- Request explicitly references `portfolio-allocation-capitalization`, R&D spend allocation, or software capitalization.
- Keywords: CapEx vs OpEx, software capitalization, Athenahealth model, KTLO, tech debt allocation, engineering capacity themes, R&D investment mix.

## Routing boundary

- Primary for strategic resource allocation modeling, theme budgeting, and Jira-to-capitalization workflows.
- Route individual engineering code reviews to `code-review` and financial pricing models to `product-pricing-strategy`.

## Inputs required

- Total engineering headcount and monthly fully-burdened labor costs
- Project allocations (Project list, objectives, and assigned engineering % / hours)
- Time spent on maintenance vs new development
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Categorize engineering projects into the **Four Investment Themes**:
   - **Strategic / Innovation**: Net-new functionality for end users (**Capitalizable**).
   - **Foundational Tech**: Architecture/infrastructure enabling future features (**Capitalizable** if enabling new functionality; otherwise expensed).
   - **Reactive Trust / Bugs**: Defect fixing and quality stability (**Expensed**).
   - **BAU / KTLO (Keep The Lights On)**: Maintenance, routine patching, internal support (**Expensed**).
3. Calculate the **Software Capitalization Allocation**:
   $$	ext{Final Capitalized Amount} = 	ext{Allocated Project Cost} 	imes (1 - 	ext{Maintenance \%}) \quad [	ext{for eligible projects}]$$
4. Review portfolio balance against target distributions (e.g., 30–40% Innovation, 20–30% Tech Debt, 15–20% Bugs, 10–15% KTLO).
5. Generate clear summary reports for executive leadership and corporate finance.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit classification of work into Capitalize vs Expense buckets.
- Formulaic capitalization calculation with maintenance deductions applied.
- Clear theme allocation breakdown (Strategic, Tech Debt, Bugs, KTLO).

## Output format

- **Theme Allocation Summary**: Distribution % across Innovation, Tech Debt, Bugs, and KTLO.
- **Work Categorization Table**: Project-by-project classification (New Feature, Foundational, Reactive, KTLO).
- **Capitalization Financial Schedule**: Cost allocation, capitalization eligibility, maintenance adjustments, and net capitalized amount.
