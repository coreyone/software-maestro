---
name: product-growth
description: "Trigger: growth product management, growth loops, acquisition loops, retention loops, activation milestone, Aha moment, natural frequency of use, Brian Balfour 4 fits, Fareed Mosavat growth model, Elena Verna PLG, Nir Eyal hooked model, Josh Elman core action, Lenny Rachitsky growth channels, channel model fit, viral coefficient K factor, cohort retention flattening. Scope: Scaling post-PMF products through self-reinforcing growth loops, activation funnels, retention mechanics, and viral flywheels. Formulates Brian Balfour's Four Growth Fits (Market-Product, Product-Channel, Channel-Model, Model-Market) and compounding Growth Loops; Fareed Mosavat's Natural Frequency and Activation thresholds; Nir Eyal's Hooked model (Trigger, Action, Variable Reward, Investment); Josh Elman's Core Action frequency; and Elena Verna's Product-Led Growth (PLG) mechanics. Boundary: Excludes pre-PMF 0-to-1 customer discovery (use product-zero-to-one), single-page CRO micro-copy adjustments (use cro-commerce-audit or marketing-copy-emotion-provoking-action-driven), or multi-channel CRM message sending (use marketing-lifecycle-crm-automation)."
---

# Rule: Growth Product Management, Growth Loops, & Retention

> [!IMPORTANT]
> **Expert Attribution**: This skill embeds the documented frameworks and methodologies of **Brian Balfour** (Four Growth Fits & Growth Loops), **Fareed Mosavat** (Retention-First & Natural Frequency), **Elena Verna** (Product-Led Growth), **Nir Eyal** (Hooked Model), **Josh Elman** (The Core Action), **Lenny Rachitsky** (7 Growth Channels & Racecar Model), and **Adam Nash** (Feature Bucketing).

---

## When to use

Use this skill when scaling and optimizing post-PMF products to accelerate compounding growth:
- Architecting closed-loop growth flywheels (User $\to$ Action $\to$ Output $\to$ New User) to replace leaky linear funnels.
- Validating the Four Growth Fits: Market-Product, Product-Channel, Channel-Model, Model-Market.
- Defining and optimizing user **Activation Milestones** (e.g. $X$ core actions in $Y$ days) and the **Aha Moment**.
- Designing behavioral habit loops using Nir Eyal's Hooked Model (Trigger $\to$ Action $\to$ Variable Reward $\to$ Investment).
- Diagnosing and flattening cohort retention decay curves.

## When not to use

Do not use this skill for:
- Pre-PMF customer discovery interviews and early venture hypothesis shaping (use `product-zero-to-one`).
- Single-page form styling or checkout field optimization (use `product-optimizer-feature` or `design-forms-wizards-checkout`).
- Multi-channel push/email CRM campaign execution (use `marketing-lifecycle-crm-automation`).

## Trigger cues

- Request mentions: `growth product manager`, `growth loops`, `acquisition loops`, `retention loops`, `activation milestone`, `Aha moment`, `natural frequency`, `Brian Balfour`, `Fareed Mosavat`, `Elena Verna`, `PLG`, `Nir Eyal`, `Hooked model`, `Josh Elman`, `core action`, `Lenny Rachitsky`, `viral coefficient`, `K-factor`, `cohort retention`.
- Scenarios involving viral loops, onboarding activation optimization, self-serve PLG funnels, or habit loop design.

## Routing boundary

- Route pre-PMF discovery to `product-zero-to-one`.
- Route core feature optimization and usability heuristics to `product-optimizer-feature`.
- Route multi-channel push/email automation to `marketing-lifecycle-crm-automation`.

## Inputs required

1. **Core Product Action**: The single value-creating behavior (e.g. publish document, send invite, book trip).
2. **Current Retention & Conversion Baselines**: D1/D7/D30 retention curves and signup-to-activation rate.
3. **Target Growth Loop Archetype**: Viral User Loop, Content/SEO Loop, Paid Reinvestment Loop, or Sales Loop.
4. **Natural Frequency of Use**: Daily, Weekly, Monthly, or Seasonal.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Establish the Natural Frequency of Use & Core Action (Josh Elman & Fareed Mosavat)**:
   - Identify the single **Core Action** that creates customer value.
   - Define the product's **Natural Frequency**: Daily (Slack), Weekly (Notion/Asana), Monthly (Payroll), or Annual/Seasonal (Airbnb/TurboTax).
3. **Define the Activation Threshold & Aha Moment (Fareed Mosavat & Elena Verna)**:
   - Formulate the precise Activation Milestone: *"User performs [Core Action] [N] times within [T] days"* (e.g., Slack's 2,000 messages, Facebook's 7 friends in 10 days).
   - Streamline onboarding to strip out all non-essential friction prior to reaching this milestone.
4. **Architect Closed Growth Loops (Brian Balfour)**:
   - Replace linear top-of-funnel acquisition with self-reinforcing loops:
     $$	ext{New User} \longrightarrow 	ext{Core Action} \longrightarrow 	ext{Shareable Output} \longrightarrow 	ext{Exposed Non-User} \longrightarrow 	ext{New User}$$
   - Verify **Channel-Model Fit**: Ensure acquisition channel economics match ARPU and monetization model.
5. **Engineer Behavioral Habit Hooks (Nir Eyal)**:
   - **Internal Trigger**: User emotion/need (e.g. boredom, fear of missing out, collaborative anxiety).
   - **Action**: The simplest behavior in anticipation of reward (Fogg Behavior Model: Motivation, Ability, Prompt).
   - **Variable Reward**: Tribe (social recognition), Hunt (new content/insights), Self (mastery/completion).
   - **Investment**: Stored value that makes the next loop easier (data imported, reputation built, integrations configured).
6. **Diagnose Cohort Retention Flattening**:
   - Ensure long-term cohort curves flatten parallel to the x-axis. Never attempt to scale top-of-funnel acquisition if retention curves decay to zero.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit Core Action and Natural Frequency definition.
- Concrete Activation Milestone specification ($N$ actions in $T$ days).
- Formal Growth Loop design with input/output mechanics.
- Nir Eyal Hooked Model (Trigger, Action, Variable Reward, Investment).
- Assessment of Balfour's 4 Growth Fits and retention curve flattening.

## Output format

- **Executive Growth Scorecard**: Core Action, Natural Frequency, and primary growth bottleneck.
- **Activation & Aha Moment Specification**: Exact metric rule ($N$ in $T$ days) and onboarding path.
- **Growth Loop Architecture**: Step-by-step loop diagram (Input $	o$ Action $	o$ Output $	o$ Next Input).
- **Behavioral Hook Canvas (Nir Eyal)**: Internal/External Trigger $	o$ Action $	o$ Variable Reward $	o$ Investment.
- **Four Fits Evaluation (Brian Balfour)**: Market-Product, Product-Channel, Channel-Model, Model-Market audit.
