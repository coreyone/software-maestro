---
name: systems-retro-pruning
description: "Audit product operations debt, stack-rank tool utility, and deprecate redundant ceremonies."
---

# Rule: Systems Retrospective, Toolchain Governance, & Process Pruning

## When to use

Use this skill when conducting quarterly system retrospectives, auditing product toolchains and ceremonies, eliminating process bloat, and actively deprecating outdated templates or meetings.

## When not to use

Do not use this skill for code-level refactoring, dead code cleanup, or software dependency upgrading.

## Trigger cues

- Request explicitly references `systems-retro-pruning` or process deprecation.
- Keywords: systems retro, tool stack audit, process pruning, eliminate process debt, deprecate meetings, product ops retro, anti-process bloat, Amplitude retro model.

## Routing boundary

- Primary for product operating system health audits, ceremony rationalization, and toolchain optimization.
- Route codebase hardening to `improve-codebase` and agile team sprint retros to agile skills.

## Inputs required

- Inventory of current product tools, templates, and recurring meetings
- User feedback / sentiment from PMs, Engineering, and GTM stakeholders
- Annual software spend per tool
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Conduct an **Operating System Inventory**:
   - List all recurring cross-functional meetings, approval gates, document templates, and software tools.
3. Run the **Utility Stack-Ranking Survey**:
   - Ask PMs, Engineering leads, and GTM stakeholders to rank each process/tool from *Most Valuable* to *Least Useful / Friction Generator*.
4. Categorize each system element into the **Pruning Matrix**:
   - **Keep & Amplify**: High utility, high adoption (e.g., automated release notes, self-serve telemetry).
   - **Streamline / Automate**: High utility, high manual effort (e.g., automate manual slide deck creation).
   - **Deprecate / Kill**: Low utility, high friction (e.g., redundant status syncs, 50-page PRD sign-off gates).
5. Publish the **Deprecation Notice & Streamlined Operating Baseline**.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Full inventory of audited processes, meetings, and tools.
- Explicit stack-ranking based on utility and friction.
- Actionable deprecation list with clear termination dates.

## Output format

- **Systems Audit Summary**: Overview of total meeting hours, active tools, and friction points.
- **Utility Stack-Ranking**: Categorized by Keep, Streamline, or Deprecate.
- **Active Deprecation Actions**: Specific meetings cancelled, templates retired, or tools consolidated.
- **Streamlined Operating Model**: Revised, lightweight process baseline.
