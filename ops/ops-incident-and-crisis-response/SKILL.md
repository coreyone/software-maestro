---
name: ops-incident-and-crisis-response
description: "Trigger: ops-incident-and-crisis-response, SEV-0/SEV-1, outage war room, canary kill, status page, customer crisis, SLA credit reconciliation, post-mortem RCA. Scope: Mission-Critical Incident Command, Real-Time Crisis Communications & Blameless RCA Synthesis. Governs SEV-0/1 war room triage, canary rollback, status page communications, and customer emergency resolution. Boundary: Excludes routine local unit test debugging (use developer-test-driven-development)."
---

# 🚨 Core Philosophy: Contain blast radius first, communicate transparently, and harden systems blamelessly.

## When to use

Use this skill when triaging and resolving live production incidents (SEV-0, SEV-1, SEV-2), executing canary rollbacks or traffic-shedding circuit breakers, drafting customer/executive status communications, resolving high-stakes physical/human customer emergencies (e.g., stranded guests, frozen merchant disbursements), and compiling blameless post-mortem Root Cause Analyses (RCAs).

## When not to use

Do not use this skill for routine local unit test debugging (use `developer-test-driven-development`), standard CI/CD deployment pipeline design (use `deployment-pipeline-design`), or general software telemetry logging (use `observability-telemetry`).

## Trigger cues

- Key terms: SEV-0, SEV-1, SEV-2, incident commander, war room, outage, degraded performance, canary rollback, kill switch, traffic shedding, rate limiting, status page update, customer crisis escalation, emergency re-booking, merchant payout freeze, post-mortem, Root Cause Analysis (RCA), 5-Whys, blameless retro, prevention tickets, SLA credits.
- Responding to live alerts, executing disaster recovery, communicating during service disruptions, or facilitating post-incident investigations.

## Routing boundary

- Primary for live production incident management, war room coordination, emergency customer crisis handling, and post-mortems.
- Secondary to `observability-telemetry` for underlying Prometheus/OpenTelemetry query syntax.
- Secondary to `system-architecture-rules` for static architecture design patterns.

## Inputs required

- Real-time incident telemetry (error rates, p99 latency, trace IDs, failing health checks).
- Affected customer cohorts and business impact scope (revenue lost per minute, locked-out users).
- Source of truth: `references/source.md`

## Instructions

1. **Incident Triage & Command Structure**:
   - Establish single Incident Commander (IC) with sole authority over operational decisions.
   - Assign dedicated roles: *Operations Lead* (hands-on mitigation), *Communications Lead* (status page & executives), *Scribe* (timeline recording).
   - Classify severity strictly:
     - **SEV-0**: Complete outage of core revenue / user-critical flow (e.g., all checkouts failing, global API outage, active security breach).
     - **SEV-1**: Major degradation affecting significant user subset without instant workaround.
     - **SEV-2**: Moderate issue with available workaround; core operations intact.
2. **Immediate Blast-Radius Containment**:
   - **Mitigate before Root-Causing**: Execute fast rollback, kill bad canaries, enable degraded mode, shed non-critical background traffic, or scale up capacity before deep code analysis.
   - Never debug in live production while customer blast radius is expanding.
3. **Transparent Real-Time Crisis Communications**:
   - Post initial status page update within 10 minutes of SEV-0/1 confirmation.
   - Follow standard update cadence: every 15–20 minutes during active mitigation.
   - Never blame 3rd parties or downplay impact; acknowledge symptoms, state active mitigation steps, and commit to the next update time.
4. **High-Empathy Customer Crisis Resolution**:
   - For real-world physical emergencies (e.g., Airbnb guest locked out in severe weather, Etsy seller missing holiday cutoff, Stripe merchant unable to disburse payroll), activate pre-authorized override authority (e.g., instant hotel voucher, emergency cash disbursement, manual courier re-route).
5. **Blameless Post-Mortem & Preventative Hardening**:
   - Compile second-by-second chronological timeline of alerts, actions, and impact.
   - Execute 5-Whys analysis focused entirely on systemic failures, missing alarms, and architectural gaps rather than individual human error.
   - Generate mandatory preventative engineering action items with tracked tickets and regression tests.

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`:
- Immediate containment execution (canary rollback, traffic shedding) led by an Incident Commander.
- Timestamped status page communications acknowledging impact and committing to cadence.
- Blameless 5-Whys post-mortem generating concrete regression test action items and prevention tickets.

## Output format

- Primary decision/output: Incident command actions, status page broadcasts, customer crisis vouchers, or post-mortem RCA documents.
- Summary: Incident impact summary (downtime duration, error budget consumed, customer impact).
- Actions: Immediate mitigation steps, prevention tickets assigned with owners and deadlines.
