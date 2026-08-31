---
name: product-pricing-strategy
description: "Trigger: product-pricing-strategy, pricing strategy, van westendorp, willingness to pay, pricing tiers, packaging model, two-part tariff, pocket price waterfall. Scope: End-to-End Product Pricing & Monetization Strategy across SaaS, AI, and consumer platforms. Boundary: Excludes visual checkout UI styling (use commerce-ux-rules)."
---

# PRODUCT PRICING STRATEGY

Design, audit, and optimize end-to-end monetization engines based on value capture, mechanism design, behavioral psychology, and margin leakage governance.

## Operating Boundary

- **Triggers:** Pricing strategy, willingness-to-pay (WTP), SaaS tiering, Good-Better-Best packaging, usage-based pricing (UBP), token/agentic pricing, dynamic pricing, discount governance, price increases, two-part tariffs, Van Westendorp analysis, EVC calculation, monetization audits.
- **Cross-Domain Scope:** B2B SaaS, AI & Agentic Compute, E-Commerce & Retail, Free-to-Play Gaming, Consumer Subscriptions, Luxury & Beauty, Consumer Electronics & Hardware, Enterprise Services/BPO.
- **Anti-Triggers / Exclusions:** Routine accounting ledger bookkeeping, tax compliance calculations, pure checkout UI CSS layout without commercial logic, or standard payment gateway webhook integration.

## Inputs Required

1. **Offering Context:** Core product/service, target buyer personas, ICP vs. end-user dynamics, cost of goods sold (COGS/unit costs).
2. **Competitive Landscape:** Next Best Alternative (Reference Value), incumbent pricing models, status-quo alternatives (e.g., spreadsheets, manual labor).
3. **Value Metric Candidates:** The measurable unit that best correlates with customer value realization.
4. **Current Performance / Baseline:** Current ARPU/ACV, churn rate, Net Dollar Retention (NDR), gross margins, discount frequency, customer acquisition cost (CAC).
5. **Business Horizon:** Growth phase (land-grab / network effects) vs. extraction phase (margin expansion / enterprise monetization).

---

## Instructions

1. Read [references/source.md](references/source.md) for canonical economic theory, classic practitioner texts, and Nobel-winning literature.
2. Execute monetization strategy through the **5-Layer Universal Pricing Engine**:

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Layer 5: Realization & Leakage Control (Pocket Waterfall, Yield Mgmt)  │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Layer 4: Behavioral & Mental Framing (Prospect Theory, Decoupling)     │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Layer 3: Fencing & Versioning (Pigouvian Discrimination, Screening)    │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Layer 2: Monetization Mechanism & Metering (Two-Part Tariff, Multi-Sided)│
 ├────────────────────────────────────────────────────────────────────────┤
 │ Layer 1: Value Foundation & Surplus Geometry (EVC, Reference Value)    │
 └────────────────────────────────────────────────────────────────────────┘
```

### 1. Layer 1: Quantify Economic Value to Customer (EVC)
- Compute the theoretical boundary:
  $$\text{EVC} = \text{Reference Value (Next Best Alternative)} + \text{Positive Differentiation} - \text{Negative Differentiation}$$
- Quantify positive differentiation into hard metrics: revenue added, cost eliminated, time saved, risk avoided, or psychological status created.
- Deduct switching friction, migration cost, and adoption risk.
- **Surplus Rule:** Target capturing **20%–40%** of net differentiation value in B2B/Enterprise; **10%–25%** in high-velocity B2C; **>70%** in non-linear luxury/Veblen goods. Never price at 100% EVC (which destroys purchase incentive).

### 2. Layer 2: Architect the Metering Mechanism
- Select the value metric matching customer utility scaling:
  - **Flat / User-Based:** Best when marginal cost $\approx 0$ and usage variance is low. (Caution: Seat pricing penalizes AI automation).
  - **Two-Part Tariff ($F + p \cdot q$):** Fixed platform fee ($F$) covers base margin + variable usage ($p$) scales with volume.
  - **Work-Unit / Outcome:** Bill per verified output (e.g., resolved ticket, lead qualified, transaction completed).
  - **Multi-Sided Platform:** Subsidize the highly elastic/network-generating side; monetize the inelastic side.

### 3. Layer 3: Build Segmentation Fences & Versioning
- Segment along distinct Willingness-to-Pay (WTP) curves.
- Apply **Mussa-Rosen Quality Screening:** Ensure each tier is distinct enough that high-WTP customers self-select into premium tiers without cannibalizing down.
- Deploy 4 fence types:
  - **Feature Fences:** SSO, audit logs, custom integrations, SLAs, priority routing.
  - **Quantitative Fences:** Capacity caps, monthly compute credits, seats, volume limits.
  - **Contextual Fences:** Student, non-profit, regional/purchasing-power parity (PPP).
  - **Service/Support Fences:** Community vs. dedicated account manager and uptime guarantees.

### 4. Layer 4: Behavioral & Cognitive Framing
- Apply **Kahneman-Tversky Prospect Theory:** Frame pricing around loss prevention, continuity insurance, or guaranteed downside protection (losses loom $\approx 2.25\times$ larger than gains).
- Apply **Thaler Mental Accounting Decoupling:** Minimize transaction friction via bundled tiers, annual prepays (e.g., "2 months free"), or pre-funded credit balances.
- Apply **Anchoring & Decoys:** Anchor with the enterprise/top-tier price first to make core tiers feel accessible. Introduce asymmetric decoys where needed.

### 5. Layer 5: Enforce Pocket Price Governance
- Map the **Pocket Price Waterfall:** List Price $\to$ Standard Discount $\to$ Discretionary Sales Concession $\to$ Payment Term Rebate $\to$ Free Onboarding Credits $\to$ Payment Processing Fees $\to$ **Realized Pocket Price**.
- Enforce strict discount matrices:
  - $\le 10\%$: Account Executive discretion.
  - $11\%\text{--}25\%$: VP Sales approval with mandatory quid-pro-quo (annual prepay, logo rights, multi-year term).
  - $>25\%$: CFO/Executive approval.
- Embed annual CPI / 5%–8% contractual escalation clauses in all multi-year agreements.

---

## Pricing Strategy Scoring Grid (Audit Rubric)

Use this scoring rubric to evaluate, audit, and benchmark any pricing model across 6 pillars (Max Score: 24 points).

| Pillar | 0 - Failing | 1 - Poor | 2 - Adequate | 3 - Strong | 4 - World-Class |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Value Grounding & EVC** | Cost-plus or arbitrary gut-feel pricing. | Blind competitor matching without differentiation analysis. | High-level estimates of customer savings without empirical WTP data. | Documented EVC model with quantified customer ROI and validated Van Westendorp/Gabor-Granger data. | Continuous empirical WTP research, automated cohort elasticity tracking, and explicit EVC capture ratios. |
| **2. Metric Alignment** | Metric penalizes product value or incentivizes churn (e.g., seat pricing for automated AI). | Metric is disconnected from core customer value or confusing to calculate. | Understandable metric with minor misalignments in heavy usage tiers. | Metric scales predictably with customer value and protects gross margin against COGS spikes. | Pure value-aligned hybrid metric (Two-part tariff or work-unit) that accelerates expansion revenue seamlessly. |
| **3. Fencing & Packaging** | Single flat tier or arbitrary feature splits causing mass down-selling. | Weak fences; high-WTP enterprise customers can easily thrive on free/starter tiers. | Standard Good-Better-Best with minor feature cannibalization. | Strict, impenetrable fences (SSO, SLA, compliance, volume) driving natural tier upgrades. | Flawless Mussa-Rosen screening where every customer segment self-selects into the profit-maximizing tier. |
| **4. Behavioral Framing** | Raw numbers presented with maximum friction and zero anchoring. | Confusing table layout with cognitive overload and decision paralysis. | Standard pricing page with clear toggle (Monthly vs. Annual). | High-anchor decoy effect, loss-aversion messaging, and low-friction decoupled credit mechanisms. | Optimized cognitive architecture with dynamic personalized anchors, frictionless onboarding, and social proof. |
| **5. Pocket Realization** | Uncontrolled rogue sales discounting; massive margin leakage. | Informal discount guidelines regularly breached; no waterfall tracking. | Basic approval thresholds for discounts; periodic review. | Formal discount matrix requiring strict concessions (quid-pro-quo) and annual price escalation clauses. | Complete Pocket Price Waterfall visibility, real-time margin tracking, automated CPI renewals, and zero unearned discounts. |
| **6. Anti-Pattern Immunity** | Suffers from Feature Shock, Minnow underpricing, or Undead offerings. | Severe margin squeeze from unmetered compute or uncontrolled service costs. | Aware of failure modes but lacks proactive mitigations. | Robust unit economics, sustainable margins, and clear unbundling of non-core features. | Proactive portfolio monetizing (hidden gems unbundled, minnows up-leveled, feature shocks eliminated). |

### **Score Interpretation:**
- **21–24 (Elite):** World-class monetization engine; high NDR ($>120\%$), minimal discount leakage, perfect value alignment.
- **16–20 (Strong):** Healthy commercial model; minor leakage in sales discounting or sub-optimal packaging.
- **11–15 (Vulnerable):** Misaligned metrics or porous fences; vulnerable to margin compression and down-selling.
- **$\le 10$ (Critical Risk):** Cost-plus or seat-trap stagnation; immediate pricing overhaul required.

---

## Non-Negotiable Rules

1. **Never Price on Cost-Plus:** Costs set the price floor, not the price point. Price strictly against Economic Value to Customer (EVC) and Willingness-to-Pay (WTP).
2. **No Concessions Without Quid-Pro-Quo:** Every discount must extract value in return (longer term, upfront payment, logo rights, case study commitment).
3. **Do Not Penalize Customer Efficiency:** Avoid pure seat-based metrics for automation or AI tools that reduce human headcount.
4. **Enforce Unforgiving Fences:** Features like SAML SSO, HIPAA/SOC2 compliance, dedicated VPCs, and SLA guarantees belong exclusively in Enterprise tiers.
5. **Decouple Recurring Margin from Variable COGS:** Always structure compute-heavy or variable-cost services with two-part tariffs or consumption overages.
6. **Price Before You Build:** Test WTP during customer discovery before engineering non-core features (Ramanujam principle).

---

## Completion Gate

Before finalizing any pricing recommendation or audit, verify:
- [ ] Next Best Alternative (Reference Value) is identified and quantified.
- [ ] Primary value metric scales directly with customer value realization and protects gross margins.
- [ ] Tiers are fenced with clear, non-porous barriers preventing enterprise down-selling.
- [ ] Psychological anchoring and loss-aversion framing are applied.
- [ ] Pocket price waterfall leakage points and discounting matrices are explicitly governed.
- [ ] Strategy is evaluated against the 6-Pillar Scoring Grid.
- [ ] Failure archetypes (Feature Shock, Minnow, Hidden Gem, Undead) are screened and resolved.

---

## Output Format

- **Executive Summary & Scoring:** Overall audit score (0–24) and core strategic verdict.
- **Economic Value Architecture:** Reference value, differentiation value calculation, and recommended capture ratio.
- **Packaging & Tier Matrix:** Good-Better-Best table with target buyer, value metric, quantitative limits, and fenced features.
- **Behavioral Framing & Packaging:** Pricing page structure, anchoring order, billing frequency incentives, and mental accounting mechanisms.
- **Realization & Governance:** Discount authority matrix, escalation terms, and pocket waterfall protections.
- **Implementation & Migration Roadmap:** Phased rollout plan, grandfathering policies for legacy accounts, and communication scripts.
