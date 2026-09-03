---
name: product-data-metric-investigation-triage
description: "Diagnose KPI drops, metric anomalies, and funnel conversion regressions across analytics pipelines."
---

# Rule: Product Data Metric Investigation & Root-Cause Triage

## When to use

Use this skill when a product or business metric experiences an unexpected drop, spike, or anomaly:
- Top-line conversion, booking volume, activation, or retention declines unexpectedly.
- A KPI drops despite all sub-funnel conversion steps appearing healthy (Simpson's Paradox).
- You need a structured waterfall decomposition to isolate whether a drop was driven by traffic volume, within-segment conversion rates, or traffic mix changes.
- You must triage a metric incident and establish whether it is a P0 active service regression, a P1 funnel blockage, or a benign P2 seasonal/mix shift.

## When not to use

Do not use this skill for:
- Infrastructure stack trace debugging or core crash logs (use `diagnosing-bugs` or `observability-telemetry`).
- Designing new North Star metric trees from scratch (use `incentive-design-metric-trees`).
- Writing product requirement documents (use `create-prd`).

## Trigger cues

- Request mentions: `metric drop`, `conversion drop`, `why did KPI decline`, `metric anomaly`, `waterfall decomposition`, `mix shift`, `rate shift`, `Simpson's Paradox`, `triage metric incident`, `cohort degradation`, `funnel drop investigation`.
- Urgent inquiries about sudden revenue, retention, sign-up, or booking degradation.

## Routing boundary

- Route system error logs and infrastructure tracing to `observability-telemetry` or `diagnosing-bugs`.
- Route A/B test statistical analysis to `experimentation-hypothesis-engine` or `data-science-causal-inference`.
- Route event schema and telemetry instrumentation to `analytics-event-tracking`.

## Inputs required

1. **Anomaly Description**: Impacted metric, magnitude of change, and detection timestamp.
2. **Baseline Comparison Period**: Prior period (WoW, MoM, YoY) or pre-anomaly baseline window.
3. **Segmentation Dimensions**: Traffic slice metadata (Device/OS, Geography/Market, Acquisition Channel, User Tenure Cohort, App Version).
4. **Event & Release Context**: Recent deployments, feature flag rollouts, external marketing campaigns, outages, or seasonality.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Assign Incident Triage Severity**:
   - **P0 (Critical Active Outage)**: Drop $>20\%$ in core conversion/revenue, concentrated in recent build/platform, active user blocking.
   - **P1 (High Funnel Degradation)**: Drop $5-20\%$ in key conversion step, localized to specific segment or cohort.
   - **P2 (Medium Mix/Seasonal Shift)**: Top-line movement driven primarily by traffic composition change, baseline within normal variance.
3. **Execute 3-Factor Mathematical Variance Decomposition**:
   - For an aggregate metric $M = \frac{\sum V_i R_i}{\sum V_i}$ (where $V_i$ is volume and $R_i$ is conversion rate for segment $i$):
     $$\Delta M = \underbrace{\sum \Delta w_i \bar{R}_i}_{\text{Mix Shift Effect}} + \underbrace{\sum \bar{w}_i \Delta R_i}_{\text{Rate Effect}} + \text{Interaction Residual}$$
   - Quantify exact percentage points attributable to *Mix Shift* vs *True Conversion Rate Degradation*.
4. **Conduct Multi-Dimensional Slicing Waterfall**:
   - Slice by: (1) Platform/OS & App Version, (2) Country/Geo-Market, (3) Traffic Acquisition Channel (Organic vs Paid vs Direct), (4) User Persona/Tenure (New vs Existing vs Power).
   - Test for **Simpson's Paradox**: Check if conversion rates increased across every segment individually while falling in aggregate due to an influx of low-converting traffic.
5. **Autonomous Dimensional Query Execution**:
   - For autonomous database investigation and dimensional slicing, interface via [MCP Toolbox for Databases (`googleapis/mcp-toolbox`)](https://github.com/googleapis/mcp-toolbox) to execute parameterized slice queries with connection pooling and telemetry.
6. **Correlate with Deployment & Incident Timeline**:
   - Cross-reference with: Git release tags, feature flag ramp percentages, 3rd party SDK updates, payment gateway incidents, and marketing budget reallocations.
7. **Formulate Root Cause & Corrective Action Plan**:
   - Categorize root cause: *Code Regression*, *Telemetry Pipeline Loss*, *Marketing Mix Dilution*, or *Macro/Seasonal Shock*.
   - Define immediate containment (e.g., feature flag rollback, pipeline re-ingest) and permanent preventive remediation.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Incident severity classification (P0, P1, P2).
- Formal 3-factor mathematical decomposition (Volume, Rate, Mix).
- Slicing across core dimensions with Simpson's Paradox check.
- Cross-referencing against release timeline and actionable remediation plan.

## Output format

- **Triage Summary & Severity Level**: Severity tier, metric impact $\Delta$, and confidence assessment.
- **Mathematical Variance Decomposition**: Exact waterfall breakdown (Mix Effect vs Rate Effect vs Volume Effect).
- **Dimensional Attribution Table**: Segment-by-segment contribution to the total delta.
- **Root Cause Diagnosis**: Verified trigger mechanism (code bug, tracking drop, traffic shift, external factor).
- **Immediate Containment & Action Plan**: Remediation steps, owners, and recovery verification timeline.
