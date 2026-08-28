# Feature Experimentation & Hypothesis Gating Framework

## 1. The Canonical Hypothesis Formula

To avoid ambiguous testing, every experiment must follow the 4-part structure:

$$	ext{If we } [	ext{Action/Intervention}] \longrightarrow 	ext{Then } [	ext{Behavioral Shift}] \longrightarrow 	ext{Resulting in } [\Delta 	ext{ Primary Metric}] \longrightarrow 	ext{Because } [	ext{Core Rationale}]$$

### Example:
*"If we introduce a 1-click checkout option on product pages, then mobile shoppers with saved payment methods will bypass the cart review step, resulting in an 8% lift in Mobile Checkout Conversion, because mobile purchase drop-off is driven by form fatigue."*

---

## 2. Metric Hierarchy & Guardrail Invariants

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             METRIC SCORECARD                                │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ Primary Metric (Decision)    │ Secondary Metrics (Signals)  │ Guardrails    │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ • Must be a single metric.   │ • Early adoption signals.    │ • Must NOT    │
│ • Directly tied to business  │ • Mid-funnel progression.    │   degrade.    │
│   hypothesis.                │ • Feature click-through rate.│ • Latency     │
│ • E.g., Completed Checkout %.│ • E.g., Add-to-Cart %.       │ • Unsubscribes│
│                              │                              │ • Support Vol │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

## 3. Sample Sizing & Runtime Rules

### Minimum Detectable Effect (MDE) & Sample Size:
For standard two-tailed tests ($lpha = 0.05$, Power = $80\%$):
$$n pprox rac{16 \cdot \sigma^2}{	ext{MDE}^2}$$

### Practical Runtime Rules:
1. **Never stop early (Peeking Problem)**: Pre-commit to runtime based on sample size calculations; do not stop test the moment $p < 0.05$.
2. **Seasonality Protection**: Run for at least **14 full days (two business cycles)** to smooth day-of-week and weekend fluctuations.
3. **Novelty vs. Primacy Effects**: Monitor the first 48 hours separately to detect novelty bias among existing power users.

---

## 4. Rollout vs. Iterate vs. Kill Decision Matrix

| Outcome State | Primary Metric | Guardrails | Operational Decision |
| :--- | :---: | :---: | :--- |
| **Clear Win** | $+ \Delta$ ($p < 0.05$) | Neutral / Stable | **100% Rollout**: Graduate feature flag, remove legacy branch. |
| **Inconclusive** | Neutral ($p \ge 0.05$) | Neutral / Stable | **Iterate or Kill**: If qualitative insight warrants a revised variant, iterate once; otherwise kill to prevent tech debt. |
| **Guardrail Breach** | $+ \Delta$ ($p < 0.05$) | Degraded ($p < 0.05$) | **Pause & Diagnose**: Business lift cancelled out by system harm (e.g., higher revenue but 300% support tickets). |
| **Clear Loss** | $- \Delta$ ($p < 0.05$) | Any | **Immediate Kill**: Turn off variant flag, log learning in Experiment Repository. |
