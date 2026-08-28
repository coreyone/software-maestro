---
name: behavioral-loops-retention-modeling
description: "Trigger: Retention modeling, cohort analysis, aha moment discovery, behavioral loops, habit formation, BJ Fogg behavior model, Nir Eyal hooked loop, B=MAP, user activation threshold, retention decay curve, churn diagnosis. Scope: Synthesizing BJ Fogg's Behavior Model (B=MAP, 6 Simplicity Factors, Prompts) and Nir Eyal's Hooked Model (Internal Triggers, Variable Rewards of Tribe/Hunt/Self, Stored Value Investments) with quantitative cohort retention curves (Smile vs Flat vs Bleeding) and predictive Aha moment thresholds. Boundary: Excludes client-side visual CSS styling (use design-user-onboarding-ux) or backend database sharding."
---

# Rule: Behavioral Loops, Fogg & Hook Models, & Cohort Retention Engineering

## When to use

Use this skill when analyzing user cohort retention curves, discovering predictive "Aha moment" thresholds, diagnosing churn decay, optimizing user actions via BJ Fogg's Behavior Model ($B = MAP$), or architecting habit-forming product loops using Nir Eyal's Hooked Model.

## When not to use

Do not use this skill for client-side visual CSS styling (use `design-user-onboarding-ux`) or low-level database indexing.

## Trigger cues

- Request explicitly references `behavioral-loops-retention-modeling`, retention curves, Nir Eyal, or BJ Fogg.
- Keywords: $B=MAP$, Fogg Behavior Model, Hooked Model, internal triggers, variable rewards (Tribe, Hunt, Self), stored value investment, retention curve, cohort retention, aha moment formula, activation threshold, habit formation, smiling retention, churn decay.

## Routing boundary

- Primary for behavioral growth mechanics, activation inflection thresholds, Fogg $B=MAP$ simplicity calibration, Hooked loop architecture, and cohort retention curve modeling.
- Route visual onboarding steps to `design-user-onboarding-ux` and raw event taxonomy to `analytics-event-tracking`.

## Inputs required

- Cohort retention data (Day 1, 7, 30, 90 retention %)
- User action frequencies during the first activation window (24–72 hours)
- Core user problem, negative emotional itch (Internal Trigger), and primary value delivery action
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Diagnose the **Cohort Retention Curve & Product Cadence**:
   - Classify curve morphology: *Bleeding* (terminal decay $\to 0\%$), *Flat* (asymptotic stabilization at baseline), or *Smiling* (resurrecting through network effects).
   - Establish the natural product cadence (Daily, Weekly, Monthly, Trigger-based).
3. Discover the Predictive **"Aha Moment" Threshold**:
   - Formulate the activation milestone: $X \text{ core value actions in } Y \text{ days}$.
   - Ensure the threshold maximizes separation between retained vs churned cohorts (target $\Delta \ge 40\%$).
4. Apply **BJ Fogg's Behavior Model ($B = MAP$)** to the Core Action:
   - **Motivation ($M$)**: Leverage core drivers (Pleasure/Pain, Hope/Fear, Social Belonging/Rejection).
   - **Ability ($A$) & 6 Elements of Simplicity**: Systematically reduce friction across *Time, Money, Physical Effort, Cognitive Load (Brain Cycles), Social Deviance, and Non-Routine*.
   - **Prompt ($P$) Placement**: Position Prompts above the Fogg Action Line (*Facilitator* when high motivation/low ability; *Spark* when low motivation/high ability; *Signal* when both are high).
5. Construct **Nir Eyal's 4-Phase Hook Loop**:
   - **Trigger**: Transition from *External Triggers* (Paid, Earned, Relationship, Owned) to *Internal Triggers* (alleviating negative emotional states: boredom, anxiety, uncertainty, fatigue).
   - **Action**: The simplest behavior done in anticipation of reward ($B = MAP$).
   - **Variable Reward Triad**: Provide intermittent, non-predictable rewards across *Tribe* (social validation/connection), *Hunt* (resources/insights), and *Self* (mastery/completion).
   - **Investment (Stored Value)**: Prompt the user to invest data, content, reputation, skills, or customization that *loads the next trigger* and increases switching costs.
6. Verify the **Ethical Manipulation Matrix** (*The Facilitator*: improves user's life + creator uses it).

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Cohort retention curve diagnosis and baseline quantification.
- Quantified "Aha Moment" threshold ($X$ actions in $Y$ time).
- Fogg Behavior Model ($B = MAP$) breakdown with 6 Elements of Simplicity.
- Complete Hooked Model (Internal Trigger, Action, Variable Reward category, Stored Value Investment).

## Output format

- **Cohort Retention Diagnosis**: Curve classification (Bleeding/Flat/Smiling) and terminal retention rate.
- **Aha Moment Inflection Formula**: Quantitative threshold separating retained vs churned users.
- **BJ Fogg $B=MAP$ Simplicity Audit**: Calibration of Motivation, 6 Simplicity Elements, and Prompt type.
- **Nir Eyal Hook Architecture**: Complete loop (Trigger $\to$ Action $\to$ Variable Reward of Tribe/Hunt/Self $\to$ Stored Value Investment).
- **Behavioral Optimization Roadmap**: Concrete interventions to compress Time-to-Aha and deepen stored value.
