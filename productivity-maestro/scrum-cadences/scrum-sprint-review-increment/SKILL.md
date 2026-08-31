---
name: scrum-sprint-review-increment
description: "Trigger: sprint review, working increment demo, definition of done audit, stakeholder reality check, inspect increment, sprint demo. Scope: Original Scrum Sprint Review & Working Increment Inspection. Eliminates 90% Done theater and PowerPoint presentations. Inspects live, working, integrated software against the strict Definition of Done (DoD) directly with stakeholders. Adapts the Product Backlog based on real customer feedback. Boundary: Excludes internal team retrospective (use scrum-retrospective-kaizen) or CI/CD deployment configuration (use deployment-pipeline-design)."
---

# Rule: Scrum Sprint Review & Working Increment Inspection

> [!IMPORTANT]
> **Ethos & Origins**: Grounded in **Jeff Sutherland & Ken Schwaber** (*Scrum Guide*).
> **The Cybernetic Purpose**: Neutralizes **"Watermelon" Reporting and "90% Done" Theater**.
>
> **The Prime Directive**: No slides allowed. The Sprint Review is a working session where real stakeholders inspect **live, working, integrated software (the Increment)** that meets the strict Definition of Done.

---

## When to use

Use this skill at the end of a sprint cycle to inspect the product increment and adapt the backlog:
- Demonstrating **working software** directly to real users and business stakeholders.
- Auditing completed features against the **Definition of Done (DoD)**.
- Evaluating whether the **Sprint Goal** was achieved.
- Collecting empirical feedback to re-order and adapt the Product Backlog for the next sprint.

## When not to use

Do not use this skill for:
- Team interpersonal process retrospectives (use `scrum-retrospective-kaizen`).
- Sprint Planning or initial task sizing (use `scrum-sprint-planning-capacity`).
- Automated pipeline deployments (use `deployment-pipeline-design`).

## Trigger cues

- Request mentions: `sprint review`, `working increment demo`, `definition of done audit`, `stakeholder reality check`, `inspect increment`, `sprint demo`.

## Inputs required

1. **Committed Sprint Goal**: The target established at Sprint Planning.
2. **Deployed Increment**: Live, functional software deployed in staging/production.
3. **Definition of Done Checklist**: Explicit quality standards (code, tests, docs, security).
4. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Audit Completed Items Against Definition of Done**:
   - Binary check: 100% done or 0% done. No partial credit for "almost finished" items.
3. **Conduct Working Software Demo**:
   - Walk through live user workflows on real staging/production environments. Zero PowerPoint decks.
4. **Evaluate Sprint Goal Achievement**:
   - Assess whether the increment solved the business problem defined in the Sprint Goal.
5. **Capture Feedback & Adapt Product Backlog**:
   - Record stakeholder reactions, newly discovered requirements, and market changes directly into the Product Backlog.

## Completion gate

- [ ] Definition of Done audit completed for all sprint items.
- [ ] Live demo script and walkthrough results documented.
- [ ] Sprint Goal achievement verdict declared (Achieved / Not Achieved).
- [ ] Adapted Product Backlog updates prioritized for the next sprint.
