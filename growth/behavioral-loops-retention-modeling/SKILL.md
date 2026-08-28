---
name: behavioral-loops-retention-modeling
description: "Trigger: Retention modeling, cohort analysis, aha moment discovery, behavioral loops, habit formation, user activation threshold, retention decay curve, churn diagnosis. Scope: Identifying inflection-point activation thresholds (Aha moments), designing habit formation loops (Trigger -> Action -> Variable Reward -> Investment), and modeling cohort retention decay curves (Smile vs Flat vs Bleeding). Boundary: Excludes client-side visual onboarding walkthrough design (use design-user-onboarding-ux) or backend database sharding."
---

# Rule: Behavioral Loops & Cohort Retention Modeling

## When to use

Use this skill when analyzing user retention curves, identifying the predictive "Aha moment" threshold, designing habit-forming product loops, or diagnosing cohort churn decay.

## When not to use

Do not use this skill for front-end CSS/visual onboarding tours (use `design-user-onboarding-ux`) or low-level database indexing.

## Trigger cues

- Request explicitly references `behavioral-loops-retention-modeling` or retention modeling.
- Keywords: retention curve, cohort retention, aha moment, habit loop, activation threshold, Nir Eyal loop, churn decay, retention flattening, smiling retention.

## Routing boundary

- Primary for behavioral growth mechanics, activation inflection thresholds, habit loop architecture, and cohort retention curve analysis.
- Route visual onboarding steps to `design-user-onboarding-ux` and raw event taxonomy to `analytics-event-tracking`.

## Inputs required

- Cohort retention data (Day 1, 7, 30, 90 retention %)
- User action frequencies during the first 72 hours
- Core value delivery event (the product's primary output)
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Analyze the **Cohort Retention Curve**:
   - Classify curve shape: *Bleeding* (falls to zero), *Flat* (stabilizes at healthy baseline), or *Smiling* (resurrects via network effects).
   - Calculate terminal retention baseline.
3. Identify the **"Aha Moment" Activation Threshold**:
   - Identify the specific behavioral formula: $X 	ext{ actions in } Y 	ext{ days}$ (e.g., *"3 exports in 7 days"*, *"7 friends in 10 days"*).
   - Evaluate predictive correlation with long-term 90-day retention.
4. Design the **Compounding Behavioral Habit Loop**:
   - **Trigger (External / Internal)**: Push/email notifications or user emotional cues (anxiety, curiosity).
   - **Action**: Smallest possible friction-free user behavior.
   - **Variable Reward**: Immediate value or feedback (novel insight, peer recognition, dopamine).
   - **Investment**: Storing data, customizing profile, or creating content that increases switching costs.
5. Deliver a **Retention Improvement Plan** targeting the critical drop-off gaps.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Cohort retention curve classification and baseline rate.
- Precise, quantified "Aha moment" activation threshold ($X$ actions in $Y$ time).
- Complete 4-step habit loop design (Trigger, Action, Variable Reward, Investment).

## Output format

- **Retention Curve Diagnosis**: Classification (Bleeding/Flat/Smiling) and terminal retention rate.
- **Aha Moment Formula**: Quantitative threshold driving long-term retention.
- **Behavioral Habit Loop Design**: Breakdown of Trigger $ightarrow$ Action $ightarrow$ Reward $ightarrow$ Investment.
- **Optimization Roadmap**: Specific interventions to compress Time-to-Aha.
