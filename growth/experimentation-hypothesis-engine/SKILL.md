---
name: experimentation-hypothesis-engine
description: "Trigger: experimentation-hypothesis-engine, A/B testing, MDE calculation, sample size determination, statistical power, SRM check, experiment post-mortem. Scope: Statistical Experimentation & A/B Testing Design. Governs sample sizing (MDE), Sample Ratio Mismatch (SRM) checks, and 3-way post-mortems. Boundary: Excludes qualitative user interviews."
---

# EXPERIMENTATION, HYPOTHESIS GATING & EMPIRICAL CLAIMS ENGINE

Audit empirical claims against primary sources, rigorously check statistical methodology for bias and p-hacking, query raw telemetry via Google MCP Toolbox for Databases (`googleapis/mcp-toolbox`), formulate falsifiable hypotheses, design statistically powered experiments, and execute structured post-mortems.

> "A hypothesis is only as valid as the empirical truth of its primary evidence and the statistical integrity of its methodology. Extraordinary claims require primary source verification, strict bias auditing, and statistical power."

---

## Operating Boundary

- **Triggers:**
  - **Empirical Claims & Study Verification:** Requests to verify assertions against primary sources, audit scientific research papers, cross-check news claims against original data/bills/PDFs, extract overlooked data, audit statistics for bias or p-hacking, calculate effect sizes and confidence intervals, and determine if methodological flaws invert conclusions.
  - **Database Telemetry & Primary Data Retrieval:** Extracting raw event logs, cohort metrics, and experiment telemetry directly from enterprise databases (BigQuery, PostgreSQL, MySQL, AlloyDB, Cloud Spanner) via **Google MCP Toolbox for Databases** (`googleapis/mcp-toolbox`).
  - **Product & Growth Experimentation:** Requests to design A/B tests, multivariate experiments, growth loop acceleration tests, calculate sample size and Minimum Detectable Effect (MDE), establish primary vs. guardrail metrics, prevent early peeking, test for Sample Ratio Mismatch (SRM), and conduct 3-way experiment post-mortems.
- **Cross-Disciplinary & Tooling Standards Applied:**
  - **Google MCP Toolbox for Databases (`googleapis/mcp-toolbox`):** Connects agents securely to operational databases and data warehouses (BigQuery, PostgreSQL, MySQL, AlloyDB, Spanner) to query raw experiment telemetry, verify baseline rates ($\mu$), and audit sample distributions without relying on third-party dashboard proxies.
  - **`technical-language-rules` (ASD-STE100 + Google DevDocs):** Deterministic prose, $\le 20$ words/sentence procedural, $\le 25$ words/sentence descriptive, imperative action verbs, unambiguous connectors (`because`, `after`, `can`, `must`).
  - **`info-to-ink` (Output Token Compression):** High signal-to-noise ratio. Eliminate rhetorical filler, pleasantries, and hand-waving. Preserve exact numerical figures, confidence intervals, sample sizes, and mathematical formulas.
  - **`the-elements-of-style-principles` (Strunk & White):** Positive form, active voice, and concrete, observable evidence.
- **Anti-Triggers / Exclusions:** Raw feature flag SDK code installation, low-level database performance tuning, qualitative-only brainstorming with zero empirical basis, or subjective editorial opinions.

---

## Inputs Required

1. **Input Subject / Artifact:**
   - *For Claims & Study Audits:* Article URL/text, scientific paper, press release, empirical dataset, policy claim, or whitepaper.
   - *For Product Experiments:* Proposed feature change, target user action, baseline metric, daily traffic volume, and qualitative friction evidence.
2. **Primary Source Documents & Data Access:**
   - Original research PDFs, clinical trial registrations, government records, or live database connectivity via **`googleapis/mcp-toolbox`** (BigQuery, Postgres, MySQL, Spanner).
3. **Statistical Parameters (When Designing Tests):** Baseline conversion rate ($\mu$), target MDE ($\Delta$), statistical power ($1-\beta = 80\%$), and significance level ($\alpha = 0.05$).

---

## The 6-Stage Empirical Verification & Experimentation Pipeline

```
  [Stage 1: Claim / Hypothesis Audit] ──► Deconstruct atomic claims or testable propositions.
             │
  [Stage 2: Primary Source Retrieval] ──► Query raw data via mcp-toolbox; fetch original PDFs/logs.
             │
  [Stage 3: Cross-Verification & Data] ──► Verify each claim; extract overlooked confidence bounds.
             │
  [Stage 4: Statistical & Bias Audit] ──► Check sampling, SRM, blinding, p-hacking, effect sizes, CI.
             │
  [Stage 5: Experimental Design]     ──► Size sample (MDE, 14-day rule), define primary & guardrails.
             │
  [Stage 6: Impact & Inversion]      ──► Determine if errors flip conclusion; execute 3-way post-mortem.
```

---

## Execution Instructions

### Mode 1: Primary Source & Statistical Claims Audit

Follow these 5 audit steps as a neutral, science-led expert:

#### Step 1: Atomic Claim Extraction (Audit)
- Itemize every empirical assertion, statistic, causal link, or conclusion presented in the source article or proposal.

#### Step 2: Primary Source Grounding (Source)
- Trace every secondary claim back to its **original primary artifact**:
  - Peer-reviewed journal PDFs and pre-registration protocols (OSF/ClinicalTrials.gov).
  - Raw enterprise database tables and event logs queried via **Google MCP Toolbox for Databases (`googleapis/mcp-toolbox`)**.
  - Government census/data releases, corporate 10-K/10-Q filings, or legislative texts.
- Reject citations of secondary journalism or unverified summaries.

#### Step 3: Deep Cross-Verification & Hidden Data Extraction (Verify & Insights)
- Cross-check every reported number against the primary source table/data.
- Extract **overlooked data**: baseline absolute risk, subgroup sample sizes ($N$), confidence intervals, dropout rates, and omitted variables that secondary reports obscured.

#### Step 4: Methodological & Statistical Bias Audit (Stats Check)
Audit for methodological vulnerabilities:
1. **Sampling & Selection Bias:** Is the sample representative? Check for survivorship bias, healthy user bias, self-selection, and non-response attrition.
2. **Sample Ratio Mismatch (SRM):** For online experiments, run Chi-Square goodness-of-fit on sample allocations ($N_{\text{control}}$ vs $N_{\text{treatment}}$) via `mcp-toolbox` queries to detect traffic assignment skew ($p < 0.001$).
3. **Blinding & Randomization:** Was treatment truly randomized? Was double-blinding maintained?
4. **P-Hacking & Multiple Comparisons:** Did researchers test dozens of endpoints without Bonferroni or False Discovery Rate (FDR) corrections? Look for post-hoc subgroup cherry-picking (*HARKing*).
5. **Mathematical Verification:**
   - Compute **Effect Sizes** (Cohen's $d$, Odds Ratio, Relative Risk vs. Absolute Risk Reduction).
   - Verify **p-values & 95% Confidence Intervals (CI)**: Does the CI cross the null boundary?
   - Check **Multicollinearity & Confounders**: Assess variance inflation and omitted confounders (Simpson's Paradox, collider bias).

#### Step 5: Impact & Inversion Analysis (Impact)
- **The Inversion Test:** Does correcting the methodological flaw, bias, or data omission **flip the conclusion** from significant to null (or reverse direction)?
- Explain real-world consequences, engineering risks, and policy stakes clearly with zero ideological bias.

---

### Mode 2: Growth Experiment & Hypothesis Design

#### Step 1: Classify Work Type & Growth Loop Step
- **Work Type:** *Funnel Optimization* (micro-conversion), *Growth Loop Accelerator* (fueling reinvestment), or *Step-Function Bet* (net-new capability).
- **Loop Step:** Map input $\to$ action $\to$ output $\to$ reinvestment cycle.

#### Step 2: Pre-Experiment Qualitative Gate
- Enforce qualitative proof ($\ge 5$ session replays, support tickets, or user interviews) before allocating engineering capacity to variants.

#### Step 3: Canonical Hypothesis Formulation
$$\text{If we } [\text{Action/Intervention}] \longrightarrow \text{Then } [\text{Behavioral Shift}] \longrightarrow \text{Resulting in } [\Delta \text{ Primary Metric}] \longrightarrow \text{Because } [\text{Core Psychological/Functional Mechanism}]$$

#### Step 4: Metric Scorecard & Guardrail Invariants
- **Primary Metric:** Single decision-making metric directly tied to the hypothesis (verified via `mcp-toolbox` telemetry query).
- **Secondary Metrics:** Leading indicators of user adoption.
- **Guardrail Invariants:** Business/technical invariants that must NOT degrade (latency, error rate, support tickets, 30-day retention).

#### Step 5: Statistical Sizing & Runtime Rules
- Sample size per variant for $\alpha = 0.05$, Power = $80\%$:
  $$n \approx \frac{16 \cdot \sigma^2}{\text{MDE}^2}$$
- **14-Day Minimum Duration Rule:** Must run for at least 14 full days (two full weekly cycles) to eliminate day-of-week seasonality.
- **No Early Peeking Rule:** Pre-commit to sample size and duration; never stop a test on Day 3 because $p < 0.05$.

#### Step 6: 3-Way Experiment Post-Mortem
When a test concludes, execute the decision taxonomy:
1. **100% Rollout:** Statistically significant lift in Primary Metric with zero breach in Guardrails and confirmed SRM pass ($p > 0.01$).
2. **Invalidated Mental Model (Assumption Failure):** The behavioral hypothesis was wrong. Log learning into permanent repository; do not re-test.
3. **Execution Mismatch:** Hypothesis was sound, but variant UI was confusing or hidden. Redesign and re-test.
4. **Under-Powered Test:** True effect was smaller than MDE; increase sample size or consolidate variants.

---

## Output Templates

### Template A: Empirical Claims & Statistical Audit Report

```markdown
# Empirical Claims & Statistical Audit: [Subject / Title]
**Target Artifact:** [Source Link / Citation] | **Primary Grounding:** [Original PDF / Dataset / mcp-toolbox Database]

## 1. Executive Summary & Inversion Verdict
- **Core Verdict:** [Verified / Partially Supported / Flawed / Inverted / Debunked]
- **Conclusion Flip:** [YES / NO — Does methodological correction alter the headline outcome?]
- **Real-World Impact:** [1-2 sentences on actual stakes, practical effect size, and operational relevance.]

---

## 2. Claim-by-Claim Primary Source Verification Table
| Article / Secondary Claim | Primary Source Data / Reality | Verification Status | Overlooked Nuance / Omitted Data |
| :--- | :--- | :--- | :--- |
| "[Direct quote of claim]" | [Exact figure in Table X, Page Y of primary PDF or SQL query via mcp-toolbox] | ✅ Verified / ⚠️ Misleading / ❌ False | [Baseline denominator, subgroup sample, 95% CI] |

---

## 3. Methodological & Statistical Bias Audit
- **Primary Data Source:** [PDF / Raw database verified via `googleapis/mcp-toolbox`]
- **Sampling & Selection Bias:** [Assessment of sample representativeness, survival bias, or attrition.]
- **Sample Ratio Mismatch (SRM):** [Chi-Square test on variant traffic allocations.]
- **Blinding & Randomization:** [Assessment of control groups, blinding protocols, and allocation concealment.]
- **P-Hacking & Multiple Comparisons:** [Analysis of endpoint count, p-value clustering around 0.049, HARKing, or missing FDR/Bonferroni corrections.]
- **Effect Size vs. Statistical Significance:**
  - **Reported Metric:** [e.g., "50% relative risk increase"]
  - **Absolute Baseline Shift:** [e.g., 2 in 10,000 $\to$ 3 in 10,000 (Absolute difference: 0.01%)]
  - **95% Confidence Interval:** [Lower Bound, Upper Bound]
- **Confounders & Simpson's Paradox:** [Analysis of third-variable collinearity or subgroup inversions.]

---

## 4. Synthesis & Scientific Recommendations
- **What the Evidence Truly Supports:** [Objective, calibrated statement of valid findings.]
- **Actionable Takeaways:** [Imperative steps for engineering, policy, or business decisions.]
```

### Template B: Growth Experiment Scorecard & Post-Mortem

```markdown
# Growth Experiment Design: [Experiment Title]
**Loop Step:** [Input $\to$ Action $\to$ Output $\to$ Reinvestment] | **Work Type:** [Optimization / Accelerator / Step-Function]
**Telemetry Source:** [Verified via `googleapis/mcp-toolbox` (BigQuery/Postgres)]

## 1. Formal Hypothesis Statement
*If we* [Specific intervention], *then* [Target user action will shift], *resulting in* [Target $\Delta$ in Primary Metric], *because* [Underlying psychological/functional mechanism].

## 2. Pre-Experiment Qualitative Gate
- **Qualitative Proof:** [Summary of $\ge 5$ session replays, customer interviews, or VoC tickets proving friction.]

## 3. Metric Scorecard & Guardrail Invariants
- **Primary Decision Metric:** [Single metric tied directly to loop step.]
- **Secondary Leading Indicators:** [Adoption and engagement indicators.]
- **Guardrail Invariants:** [System latency, support volume, churn, unit economics.]

## 4. Statistical Sizing & Runtime
- **Baseline Rate:** [Current metric baseline extracted via mcp-toolbox, e.g. 12.4%]
- **Target MDE:** [e.g. +8.0% relative lift]
- **Required Sample Size:** [N per variant at $\alpha=0.05$, Power=$80\%$]
- **Estimated Runtime:** [Calculated days $\ge 14$ days mandatory minimum]

## 5. Post-Mortem Decision Taxonomy
- **100% Rollout Criteria:** Primary metric $p < 0.05$ with zero guardrail breaches and SRM verified.
- **Failure Classification Matrix:**
  - *Invalidated Mental Model*: [Specific criteria showing user psychology premise failed.]
  - *Execution Mismatch*: [Specific criteria indicating UX confusion.]
  - *Statistical Under-Powering*: [Observed effect size vs sample size threshold.]
```

---

## Non-Negotiable Rules

1. **Neutral, Science-Led Posture:** Audit claims with dispassionate scientific rigor. State facts, confidence bounds, and effect sizes regardless of narrative popularity.
2. **Zero Secondary Dependence:** Never validate a factual claim using secondary commentary, news blogs, or aggregated press releases. Ground directly against original PDFs, raw datasets queried via **`googleapis/mcp-toolbox`**, clinical trial registers, or legal statutes.
3. **Mandatory Absolute vs. Relative Risk Disclosure:** Whenever relative percentage changes are reported ("50% increase"), always calculate and surface the underlying absolute baseline numbers.
4. **Mandatory Sample Ratio Mismatch (SRM) Checks:** Check sample allocations ($N_{\text{control}}$ vs $N_{\text{treatment}}$) for traffic assignment skew before accepting experiment results.
5. **Mandatory 14-Day Experiment Runtime:** Never stop an A/B test before 14 full days (two full business cycles) to eliminate day-of-week seasonality, regardless of early p-values.
6. **Single Primary Metric & Guardrails:** Every experiment must have exactly one primary decision metric and explicit guardrail invariants that block rollout if degraded.
7. **Strict Single-DRI Assignment:** Every action item in an experiment rollout or claims audit must have exactly one named human owner and hard date.

---

## Completion Gate

Before finalizing any audit or experiment design, confirm:
- [ ] Claims are cross-checked against original primary source PDFs or raw telemetry queried via `googleapis/mcp-toolbox`.
- [ ] Methodological checks for sampling bias, blinding, SRM, and p-hacking are documented.
- [ ] Absolute baseline numbers, effect sizes, and 95% confidence intervals are reported.
- [ ] Inversion impact is analyzed (does error flip the conclusion?).
- [ ] Hypotheses follow the canonical *If... Then... Resulting in... Because...* structure.
- [ ] Statistical sample size, MDE, and 14-day minimum duration are calculated.
- [ ] Metric scorecard defines exactly 1 primary metric, secondary indicators, and guardrails.
- [ ] 3-way post-mortem taxonomy is pre-defined for test completion.
