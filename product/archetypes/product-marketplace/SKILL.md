---
name: product-marketplace
description: "Trigger: marketplace product manager, two-sided marketplace, cold start problem, atomic networks, hard side of marketplace, marketplace liquidity, search to book ratio, fill rate, take rate economics, Andrew Chen cold start, Casey Winters marketplace loops, Gokul Rajaram SPADE, Dan Hockenmaier liquidity, Bill Gurley marketplace characteristics, supply demand matching, host pricing algorithms, marketplace cannibalization, buyer seller asymmetry. Scope: Designing, scaling, and balancing two-sided and multi-sided marketplace platforms (e.g. Airbnb, Uber, DoorDash, Etsy). Formulates Andrew Chen's Cold Start Framework (Atomic Networks, The Hard Side, Tipping Points, Escape Velocity); Casey Winters' Supply vs Demand Constrained growth loops; Dan Hockenmaier & Bill Gurley's Liquidity Dynamics (Search-to-Book, Fill Rate, Take-Rate Elasticity, Fragmentation); Gokul Rajaram's Marketplace Decision Matrix; and two-sided ranking/matching mechanics. Boundary: Excludes single-sided SaaS 0-to-1 validation (use product-zero-to-one), linear marketing ad copywriting (use marketing-copy-emotion-provoking-action-driven), or payment gateway SDK integration (use api-design-guidelines)."
---

# Rule: Two-Sided Marketplace Product Management

> [!IMPORTANT]
> **Expert Attribution**: This skill embeds the documented frameworks and methodologies of **Andrew Chen** (The Cold Start Problem & Atomic Networks), **Casey Winters** (Marketplace Growth Loops), **Dan Hockenmaier** (Marketplace Liquidity & Asymmetric Dynamics), **Bill Gurley** (10 Characteristics of a Great Marketplace), **Gokul Rajaram** (Marketplace Opportunity Sizing & SPADE), and operational marketplace architectures from **Airbnb** and **Uber**.

---

## When to use

Use this skill when designing, launching, balancing, or optimizing two-sided and multi-sided marketplaces:
- Solving the **Cold Start Problem** and bootstrapping early **Atomic Networks** (hyper-localized density).
- Identifying and subsidizing the **Hard Side of the Marketplace** (usually supply, sometimes high-value demand).
- Measuring and optimizing **Marketplace Liquidity** (Fill Rate, Search-to-Book, Match Time, Supplier Utilization).
- Diagnosing whether a market is **Supply-Constrained** or **Demand-Constrained** (Casey Winters).
- Modeling **Take-Rate Economics** and pricing elasticity (Host commission vs Guest service fees).
- Designing two-sided search ranking, matching algorithms, and anti-cannibalization guardrails.

## When not to use

Do not use this skill for:
- Single-sided B2B SaaS discovery or linear software apps (use `product-zero-to-one` or `product-optimizer-feature`).
- Writing general ad copy or email marketing subject lines (use `marketing-copy-emotion-provoking-action-driven`).
- Core payment gateway tokenization and credit card processing code (use `api-design-guidelines` or `data-persistence-caching`).

## Trigger cues

- Request mentions: `marketplace product manager`, `two-sided marketplace`, `cold start problem`, `atomic networks`, `hard side of marketplace`, `marketplace liquidity`, `search to book ratio`, `fill rate`, `take rate`, `Andrew Chen`, `Casey Winters`, `Dan Hockenmaier`, `Bill Gurley`, `Gokul Rajaram`, `supply demand matching`, `host pricing`, `marketplace economics`.
- Inquiries about bootstrapping buyer/seller liquidity, city launch playbooks, supply onboarding quality, or marketplace commission optimization.

## Routing boundary

- Route single-sided SaaS 0-to-1 PMF validation to `product-zero-to-one`.
- Route single-sided product-led growth to `product-growth`.
- Route single-surface UI/checkout optimization to `product-optimizer-feature`.

## Inputs required

1. **Marketplace Structure**: Two-sided (Buyer/Seller, Guest/Host, Rider/Driver) or multi-sided.
2. **Geographic / Vertical Scope**: Localized geo-market (e.g. City-by-City) vs Global cross-border.
3. **Current Bottleneck Constraint**: Supply-constrained vs Demand-constrained.
4. **Core Liquidity Metrics**: Current search volume, active listings, match rate, fill rate, and take-rate.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Solve the Cold Start Problem via Atomic Networks (Andrew Chen)**:
   - Identify the smallest **Atomic Network** where the product is self-sustaining (e.g. 1 city, 1 college campus, 1 hyper-local neighborhood).
   - Never launch nationally or globally before achieving liquidity in one atomic cell.
3. **Identify & Subsidize the Hard Side of the Marketplace (Andrew Chen & Casey Winters)**:
   - Determine which side is harder to acquire and retain (usually Supply: Airbnb hosts, Uber drivers).
   - Build specialized tooling, guarantees, and economic subsidies for the hard side (e.g., Host Damage Protection, minimum earning guarantees, instant payouts).
4. **Measure & Optimize Marketplace Liquidity (Dan Hockenmaier & Bill Gurley)**:
   - **Fill Rate**: $rac{	ext{Successful Transactions}}{	ext{Buyer Intent Queries}}$. Target: $\ge 85-95\%$.
   - **Search-to-Book Ratio**: Median searches required per successful booking.
   - **Supplier Utilization Rate**: % of available inventory/time booked per month.
   - **Time-to-Match**: Latency between demand request and supply confirmation.
5. **Model Take-Rate & Pricing Elasticity (Bill Gurley & Gokul Rajaram)**:
   - Balance take-rate ($T = rac{	ext{Net Revenue}}{	ext{Gross Merchandise Value}}$) without driving users off-platform (disintermediation risk).
   - Split fees across demand and supply (e.g. 3% host fee + 14% guest fee) to reduce supply friction.
6. **Design Dynamic Matching, Ranking & Quality Guardrails**:
   - Ranking algorithm must optimize for expected value:
     $$	ext{Rank Score} = P(	ext{Click}) 	imes P(	ext{Book} \mid 	ext{Click}) 	imes P(	ext{Host Accept}) 	imes 	ext{Quality Rating}$$
   - Implement supply quality thresholds (e.g. Superhost status, minimum 4.7-star rating) with automated penalty/demotion for cancellations.

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Atomic network boundary and cold start strategy (Andrew Chen).
- Identification and tooling/subsidy for the Hard Side.
- Quantitative Liquidity Scorecard (Fill Rate, Search-to-Book, Utilization).
- Take-rate economics and disintermediation defense.
- Dynamic matching and search ranking formula.

## Output format

- **Executive Marketplace Overview**: Two-sided structure, geographic scope, and constraint status.
- **Cold Start & Atomic Network Plan (Andrew Chen)**: Boundary definition and bootstrap playbook.
- **The Hard Side Strategy**: Subsidies, dedicated software tools, and retention mechanics.
- **Marketplace Liquidity & Economics Scorecard (Dan Hockenmaier & Bill Gurley)**: Fill rate, search-to-book, take-rate.
- **Matching & Ranking Architecture**: Algorithmic ranking loss function and quality guardrails.
