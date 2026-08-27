---
name: design-user-onboarding-ux
description: "Trigger: user onboarding, first-time user experience, FTUX, activation flow, aha moment, product walkthrough, empty states, guided tour, bowling alley framework, progressive disclosure, signup friction. Scope: Consumer and developer product onboarding design, cognitive friction reduction, time-to-value optimization, contextual learning-by-doing. Boundary: Excludes backend auth token issuance, database schema migrations, and transactional email infrastructure."
license: MIT
metadata:
  version: "1.0.0"
  author: "Corey O'Neal"
  category: "design"
  tags: "onboarding, ftux, nng, cognitive-load, bowling-alley, time-to-value, progressive-disclosure, usability"
---

# User Onboarding & First-Time User Experience (FTUX) Rules

## Core Philosophy

Users do not use software to become masters of the software; they use software to become better at their own goals (Samuel Hulick's *Fire Flower* principle / Kathy Sierra's *Badass Users*). 

Effective onboarding is not a product tour or a frontloaded manual. It is an **invisible, scaffolded path that delivers the user to their first core value realization ("Aha! moment") with zero extraneous cognitive load**.

---

## When to use

Use this skill when designing, auditing, or refactoring:
- First-time user experiences (FTUX) and welcome flows for consumer, mobile, SaaS, or developer products.
- Empty states, starter dashboards, and sandbox templates.
- Contextual, just-in-time guidance, feature discovery callouts, and inline checklists.
- Activation funnels, time-to-value (TTV) reduction initiatives, and drop-off recovery flows.

## When not to use

Do not use this skill as the primary guide for:
- Backend authentication token issuance, session encryption, or SSO protocol implementation (use `auth-and-identity-rules`).
- Database schema modeling or persistence architecture (use `data-persistence-caching`).
- Multi-step checkout payment gateways or billing compliance (use `design-forms-wizards-checkout`).

---

## Trigger Cues

- Explicit mentions of `design-user-onboarding-ux`, onboarding, FTUX, first-run experience, welcome flow, or product walkthrough.
- Requests to reduce user drop-off after signup, increase activation rates, or improve time-to-value (TTV).
- Tasks involving empty states, sample data, progressive disclosure, tutorial popups, or guided checklists.
- Designing developer "Zero-to-Hello-World" quickstart experiences.

---

## Routing Boundary

- **Primary**: User onboarding architecture, behavioral friction elimination, cognitive scaffolding, empty state design, progressive disclosure, and activation flows.
- **Upstream**: `ux-discovery-artifacts`, `product-strategy-outcome-vision`, `create-prd`.
- **Downstream**: `design-usability-rules`, `design-system-rules`, `failure-states-empty-states`, `analytics-event-tracking`.

---

## Inputs Required

1. **Target User & Context**: Consumer, enterprise operator, or developer.
2. **Core Value Metric ("Aha! Moment")**: The specific action or artifact that proves product value (e.g., first graph rendered, first song played, first message sent).
3. **Current Flow / Constraints**: Existing screens, permissions required, signup steps, or technical dependencies.
4. **Source of Truth**: [references/source.md](references/source.md).

---

## Instructions & Execution Checklist

1. **Read References First**:
   - Consult [references/source.md](references/source.md) for research-backed guidelines from Nielsen Norman Group (NN/g), O'Reilly, MIT Press, and Pragmatic Bookshelf.

2. **Establish the Straight-Line Flow (ProductLed / Bowling Alley Framework)**:
   - Identify the shortest path from launch to the Aha! moment.
   - Ruthlessly prune every step, configuration field, or permission request not strictly required for the first value delivery.

3. **Enforce NN/g Cognitive Guardrails**:
   - **Ban Carousel Overlays**: Never use multi-step modal swipe-throughs or "next-next-next" tooltip tours before the user touches the UI.
   - **Learn-by-Doing (Just-in-Time)**: Deliver contextual hints only when the user triggers or focuses on the relevant action.
   - **Make Onboarding Always Skippable**: Provide an immediate, visible "Skip" or "Dismiss" action. Never trap the user.
   - **Delayed / Lazy Registration**: Allow consumers to interact with core features or sandbox data before demanding account registration whenever feasible.

4. **Scaffold Empty States & Default Data**:
   - Transform zero-data views into action catalysts using pre-filled starter templates, sample sandboxes, or single-action primary CTAs.
   - Show the interface in its "completed" state rather than a barren wasteland.

5. **Design Progressive Scaffolding (MIT Press / Kathy Sierra)**:
   - Provide **Minimum Viable Instruction (MVI)**: Give the minimum guidance needed to experience success within 60 seconds.
   - Apply the **"Low Floor, High Ceiling"** principle: Instant first win (low floor) without limiting deep downstream power (high ceiling).
   - Scaffolding hierarchy: 
     1. *Passive*: Starter templates & illustrative empty states.
     2. *Interactive*: Action checklists with progress indicators (Zeigarnik Effect).
     3. *Contextual*: Inline micro-badges appearing on focus.

6. **Track the Activation Funnel**:
   - Define exact telemetry events (`onboarding:started`, `onboarding:skipped`, `aha_moment:reached`, `first_core_action:completed`).

---

## Completion Gate

Before reporting completion, verify against the following binary criteria:
- [ ] **No multi-step modal carousel**: Replaced with contextual inline guidance or interactive empty state.
- [ ] **Time-to-Value (TTV) < 60s**: The user can generate or experience first value immediately.
- [ ] **Always Skippable**: All tours, checklists, and prompts have clear dismissal controls.
- [ ] **Persistent Resumption**: If dismissed, an entry point remains in the navigation/profile to resume guided setup.
- [ ] **Actionable Empty States**: Every empty screen contains dummy data or an active creation CTA.
- [ ] **Accessible & Non-Destructive**: Keyboard accessible, compliant with WCAG AA contrast, and never erases entered user state.

---

## Output Format

- **Primary Output**: Onboarding flow blueprint, step-by-step wireframe specification, or UI component implementation.
- **Summary**: Concise one-paragraph rationale explaining how the design shortens Time-to-Value.
- **Friction Audit**: Table of eliminated steps vs. retained straight-line actions.
- **State Specifications**: Exact designs for empty state, first-run state, active checklist, and completion confirmation.
