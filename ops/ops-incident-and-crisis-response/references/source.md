# Mission-Critical Incident Command & Crisis Operations Playbook

## 1. First Principles & Invariants

1. **Mitigate Before Diagnosing**: During an active SEV-0/1, the only objective is restoring service health. Root cause identification is deferred until customer traffic is protected via rollback, traffic shedding, or restart.
2. **Single Incident Commander (IC)**: Exactly one person/agent holds IC authority. The IC makes final containment calls, delegates tasks, and prevents uncoordinated changes to production.
3. **Radical Transparency Without Blame**: Status updates must be honest, timely, and free of vendor finger-pointing. Internal post-mortems must operate on the assumption that engineers act in good faith given the information they had.

---

## 2. Severity Classification Matrix

| Severity Level | Definition | Response SLA | Command Requirements |
| :--- | :--- | :--- | :--- |
| **SEV-0** | Complete outage of critical core revenue / user flow (e.g., global checkout failure, authentication down, active data compromise). | Pager: $< 2\text{ min}$<br>Status Update: $< 10\text{ min}$ | IC assigned; dedicated live war room; executive notification; 15-min status cadence. |
| **SEV-1** | Critical feature degradation or major customer subset affected with no viable workaround (e.g., payout delays, webhook drops). | Pager: $< 5\text{ min}$<br>Status Update: $< 20\text{ min}$ | IC assigned; war room established; 30-min status cadence. |
| **SEV-2** | Moderate degradation; core flows working; viable workaround exists. | Pager: $< 30\text{ min}$ | On-call engineer owns resolution; business hours review. |
| **SEV-3** | Minor bug or cosmetic defect with no customer impact. | Next business day | Backlog triage. |

---

## 3. Incident Containment & Circuit-Breaker Playbook

```
[SEV-0 Alert Fired]
       │
       ├──► 1. Assign Incident Commander (IC) & Open War Room
       │
       ├──► 2. Execute Fast Containment Actions:
       │        ├── Action A: Revert most recent deployment (Rollback to Last Known Good SHA)
       │        ├── Action B: Kill unhealthy Canary / Blue-Green slice
       │        ├── Action C: Flip degraded mode feature flag (disable non-critical AI/analytics)
       │        └── Action D: Activate edge rate-limiting / shed bulk background traffic
       │
       ├──► 3. Post Initial Status Page Notice (within 10 minutes)
       │
       └──► 4. Verify Telemetry Recovery (p99 latency, error rate < 0.1%, throughput normalized)
```

---

## 4. Status Page & Executive Crisis Communication

### Standard Public Notice Templates
- **Investigating (0-10 min)**:
  `"We are currently investigating reports of elevated error rates affecting [Feature/API]. Our engineering teams are actively investigating the issue, and we will provide our next update within 20 minutes."`
- **Identified & Mitigating (10-30 min)**:
  `"We have identified the cause of the degradation affecting [Feature/API] and have implemented a mitigation to isolate the issue. Service recovery is currently underway. Next update in 20 minutes."`
- **Monitoring (30-60 min)**:
  `"A fix has been deployed and customer traffic is operating normally. We are continuing to monitor telemetry to ensure full platform stability."`
- **Resolved**:
  `"This incident has been resolved. All services are operating normally. A full post-incident retrospective will be published within 48 hours."`

---

## 5. High-Empathy Customer Crisis Resolution

When real-world physical or financial harm threatens users during a critical incident, autonomous agents operate under pre-authorized emergency override budgets:

- **Stranded Traveler (Airbnb model)**: If host lockout or unsafe listing occurs and support is overloaded, instantly authorize up to \$500 hotel voucher + \$100 ride credit with no human sign-off needed.
- **Frozen Merchant Payroll (Stripe model)**: If settlement rail fails on a payroll processing date, initiate emergency same-day wire transfer from secondary liquidity reserves.
- **Damaged Holiday Delivery (Etsy model)**: If high-value artisan order is destroyed or lost in transit 48h before a holiday, automatically refund buyer 100% and credit seller insurance payout immediately.

---

## 6. Blameless Post-Mortem & 5-Whys Framework

### Post-Mortem Report Structure
1. **Executive Summary**: 2-sentence summary of customer impact, total duration, and root cause.
2. **Impact Metrics**: Total minutes of downtime, error budget consumed, revenue impact, SLA credits owed.
3. **Chronological Timeline (UTC)**:
   - `14:02:00Z` Bad configuration deployed via PR #482.
   - `14:04:15Z` Automated alert fired on DB connection pool exhaustion.
   - `14:06:00Z` Incident Commander declared SEV-0; war room opened.
   - `14:11:30Z` Rollback initiated.
   - `14:14:00Z` Service recovered to 100% baseline.
4. **5-Whys Analysis**:
   - *Why 1*: API gateway returned HTTP 500 to users. (DB connections exhausted).
   - *Why 2*: DB connections spiked to 100%. (New query ran unindexed table scan).
   - *Why 3*: Unindexed query was deployed to production. (Query passed PR review without EXPLAIN plan).
   - *Why 4*: PR review did not catch missing index. (CI pipeline lacks automated DB migration linting).
   - *Why 5*: CI lacks migration linting. (Database migration tooling was never integrated into CI lint gates).
5. **Mandatory Preventative Action Items**:
   - Every post-mortem must output at least 2 preventative engineering tickets (e.g., add migration linter to CI, add automated alert threshold, write regression test suite) with assigned owners and 14-day completion SLAs.
