---
name: marketing-lifecycle-crm-automation
description: "Trigger: lifecycle marketing, CRM automation, push notification campaign, email sequence, SMS marketing, abandoned cart recovery, customer journey automation, activation nudges, churn win back, onboarding drip, retention marketing, re engagement campaign, message frequency capping, multi channel messaging, Braze, Iterable, Customer.io. Scope: Designing, sequencing, and automating multi-channel event-driven lifecycle marketing and CRM workflows across Push, SMS, Email, and In-App messages. Formulates user lifecycle state machines (Unactivated, Activated, Engaged, At-Risk, Dormant, Resurrected), multi-step drip cadences (abandoned checkout waterfalls, FTUX activation milestones, post-purchase review generation, predictive win-back sequences), fatigue frequency capping rules, quiet hours enforcement, and copy template specifications. Boundary: Excludes client-side event tracking telemetry instrumentation (use analytics-event-tracking), transactional email backend SMTP server infrastructure (use aws-ses or cloudflare-email-service), or commercial GTM product positioning briefs (use product-marketing-narrative)."
---

# Rule: Lifecycle Marketing, CRM Automation, & Retention Workflows

## When to use

Use this skill when designing, building, or auditing event-driven customer lifecycle communications and automated CRM campaigns:
- Designing multi-channel automated workflows (Push Notifications, In-App Messages, Email, SMS) triggered by user behavioral state transitions.
- Building high-conversion abandoned cart or abandoned booking recovery waterfalls.
- Crafting post-signup activation drip sequences to accelerate time-to-first-value (Aha moment).
- Establishing predictive churn mitigation, re-engagement, and win-back campaigns for dormant user cohorts.
- Defining global frequency capping, message fatigue policies, channel hierarchy rules, and quiet hours delivery guardrails.

## When not to use

Do not use this skill for:
- Client-side event tracking schemas or data taxonomy design (use `analytics-event-tracking`).
- Low-level transactional SMTP relay server configuration or DNS SPF/DKIM records (use `aws-ses` or `cloudflare-email-service`).
- High-level commercial product positioning or Geoffrey Moore messaging hierarchies (use `product-marketing-narrative`).

## Trigger cues

- Request mentions: `lifecycle marketing`, `CRM automation`, `abandoned cart email`, `push notification drip`, `activation nudges`, `onboarding email sequence`, `win-back campaign`, `re-engagement flow`, `Braze campaign`, `Iterable workflow`, `Customer.io triggers`, `message frequency cap`.
- Inquiries about automating user communication after signup, search, abandoned checkout, or churn risk detection.

## Routing boundary

- Route product behavioral telemetry schemas and tracking tags to `analytics-event-tracking`.
- Route habit retention modeling and dopamine loops to `behavioral-loops-retention-modeling`.
- Route GTM launch playbooks and sales battlecards to `product-marketing-narrative`.

## Inputs required

1. **Target Lifecycle Stage / Persona**: Target state (e.g., Unactivated New User, High-Intent Cart Abandoner, Dormant >60d Guest).
2. **Behavioral Trigger Events**: Event names and payload properties (e.g., `checkout_started`, `listing_saved`, `booking_completed`).
3. **Available Delivery Channels**: Push, In-App Modals, Email, SMS/WhatsApp.
4. **Primary Goal Metric & Guardrails**: Target conversion rate, re-activation rate, opt-out rate, unsubscribe rate.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Map the Lifecycle State Machine**:
   - Classify user into state: `Unactivated` $\to$ `Activated` $\to$ `Engaged / Habitual` $\to$ `At-Risk` $\to$ `Dormant` $\to$ `Resurrected`.
   - Define exact entry and exit event triggers for the target stage.
3. **Architect the Multi-Channel Delivery Waterfall**:
   - **Playbook 1: Cart / Booking Abandonment Waterfall**:
     - *T+15m*: In-App / Push reminder with deep link (*"Still looking at [Item]? Dates are in high demand."*).
     - *T+24h*: Rich Email with personalized summary, social proof reviews, and cancellation flexibility.
     - *T+48h*: Final urgency / incentive push (*"Price drop or price freeze on your saved trip"*).
   - **Playbook 2: Activation & Onboarding Drip**:
     - Progressive milestone nudges keyed to incomplete onboarding steps (Profile $\to$ Search $\to$ Wishlist $\to$ First Booking).
   - **Playbook 3: Predictive Churn & Win-Back**:
     - Triggered when $p_{\text{churn}} > 0.70$ or inactivity exceeds $2.5\times$ normal cohort cadence. 3-step value reactivation sequence.
4. **Enforce Global Fatigue Capping & Guardrail Invariants**:
   - **Universal Send Cap**: Max 1 Push/day, max 2 Marketing Emails/week, max 1 SMS/7 days per user.
   - **Channel Priority Hierarchy**: In-App $\to$ Push $\to$ Email $\to$ SMS.
   - **Quiet Hours Rule**: Zero marketing push/SMS between 9:00 PM and 9:00 AM in user's local timezone.
   - **Deliverability Threshold**: Spam complaint rate must stay $<0.08\%$; hard bounce rate $<1.5\%$.
5. **Draft High-Conversion Message Copy & Payload Specs**:
   - Specify subject lines, preheaders, push titles, body copy, CTA button labels, and deep link URI schemes.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit user lifecycle state machine classification.
- Multi-channel delivery waterfall with precise time delays (e.g. T+15m, T+24h, T+48h).
- Global fatigue frequency capping and quiet hours enforcement.
- Message copy templates with personalization tokens and deep links.
- Target conversion metrics and unsubscribe/spam guardrails.

## Output format

- **Lifecycle Workflow Architecture**: Target state, entry trigger event, and conversion goal.
- **Multi-Channel Sequence Table**: Step, timing delay, channel (Push/Email/SMS), trigger condition, and fallback rule.
- **Message Copy & Payload Specifications**: Subject, title, body copy, dynamic template variables, and CTA deep links.
- **Fatigue & Deliverability Policies**: Frequency caps, quiet hours logic, and unsubscribe/opt-out handling.
- **Measurement & Evaluation Scorecard**: Primary lift metric, control group holdout size (e.g. 5%), and fatigue guardrails.
