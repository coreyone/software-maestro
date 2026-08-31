# Product Pricing Strategy: The Definitive Reference Canon

## Contents
1. Core Economic Literature & Nobel-Winning Foundations
2. Canonical Practitioner Bibles & Frameworks
3. Modern SaaS, AI, & Usage-Based Monetization
4. Behavioral Economics & Cognitive Heuristics
5. Margin Leakage & The Pocket Price Waterfall
6. The Innovation Monetization Failure Taxonomy

---

## 1. Core Economic Literature & Nobel-Winning Foundations

### A. Two-Part Tariffs & Extraction of Consumer Surplus
* **Walter Oi (1971) — "A Disneyland Dilemma: Two-Part Tariffs for a Mickey Mouse Monopoly"** (*Quarterly Journal of Economics*, 85(1), 77–96)
  * *Thesis:* A monopoly can capture maximal consumer surplus by charging a two-part tariff: a lump-sum entry fee ($F$) equal to consumer surplus, plus a per-unit price ($p$) set at marginal cost.
  * *Application:* Fundamental to cloud compute, API gateways, telecom, Costco memberships, and modern hybrid SaaS models.

### B. Quality Versioning & Nonlinear Pricing (Screening)
* **Michael Mussa & Sherwin Rosen (1978) — "Monopoly and Product Quality"** (*Journal of Economic Theory*, 18(2), 301–317)
  * *Thesis:* Monopolists maximize profit by offering a menu of quality-price bundles designed so that different buyer types self-select into their optimal tier without cannibalizing higher-margin offerings. Low-end goods are deliberately degraded ("damaged goods") to preserve pricing power at the high end.
  * *Application:* Feature gating, tier limits, watermarking, and SSO paywalls.

### C. Multi-Sided Platforms & Network Externalities
* **Jean-Charles Rochet & Jean Tirole (2003 / 2006) — "Platform Competition in Two-Sided Markets"** (*Journal of the European Economic Association*)
  * *Thesis:* Nobel laureate Jean Tirole established that the optimal price on one side of a two-sided platform depends on the price elasticity of demand and the magnitude of cross-side network effects. The side that creates the most positive externality should be subsidized or free.
  * *Application:* Marketplace fees (Uber, Airbnb), App Stores (Apple, Google), F2P gaming (free players as content for paying players).

### D. Mechanism Design & Optimal Auctions
* **William Vickrey (1961) — "Counterspeculation, Auctions, and Competitive Sealed Tenders"** (*Journal of Finance*)
  * *Thesis:* Second-price sealed-bid auctions incentivize bidders to reveal their true willingness-to-pay (dominant strategy incentive compatibility).
* **Roger Myerson (1981) — "Optimal Auction Design"** (*Mathematics of Operations Research*)
  * *Thesis:* Virtual value transformations and reserve price optimization for dynamic yield extraction.

---

## 2. Canonical Practitioner Bibles & Frameworks

### A. The Value-Based Pricing Bible
* **Thomas T. Nagle, Georg Müller, & Gerald Smith — *The Strategy and Tactics of Pricing*** (Routledge)
  * Establishes the **Economic Value to Customer (EVC)** equation:
    $$\text{EVC} = \text{Reference Value} + \text{Positive Differentiation} - \text{Negative Differentiation}$$
  * Details price fences, elasticity segmentation, and the transition from reactive cost-plus to proactive value-capture.

### B. Power Pricing & Commercial Strategy
* **Hermann Simon — *Confessions of the Pricing Man: How Price Affects Everything*** (Springer)
  * Written by the founder of Simon-Kucher & Partners.
  * Explores the psychological dynamics of willingness-to-pay (WTP), non-linear pricing, price wars, and dynamic yield management.

### C. Designing Products Around Price
* **Madhavan Ramanujam & Georg Tacke — *Monetizing Innovation: How Smart Companies Design the Product Around the Price*** (Wiley)
  * Core thesis: Prioritize willingness-to-pay conversations *before* writing code or engineering physical products.
  * Categorizes customer segments by WTP rather than demographics.

---

## 3. Behavioral Economics & Cognitive Heuristics

### A. Prospect Theory & Asymmetric Valuation
* **Daniel Kahneman & Amos Tversky (1979) — "Prospect Theory: An Analysis of Decision under Risk"** (*Econometrica*, 47(2), 263–291)
  * *Key finding:* Value is perceived relative to a reference point; losses loom $\approx 2.25\times$ larger than equivalent gains.
  * *Pricing rule:* Frame investments around downside mitigation, continuity insurance, and operational cost elimination rather than speculative upside.

### B. Mental Accounting & Transaction Utility
* **Richard Thaler (1985) — "Mental Accounting and Consumer Choice"** (*Marketing Science*, 4(3), 199–214)
  * Total utility consists of Acquisition Utility (value received vs. price paid) and Transaction Utility (perceived fairness / deal quality compared to internal reference price).
  * Decoupling payment from consumption reduces cognitive friction (e.g., pre-funded wallets, all-inclusive packages).

---

## 4. Margin Leakage & The Pocket Price Waterfall

* **Michael V. Marn, Eric V. Roegner, & Craig C. Zawada — *The Price Advantage*** (McKinsey & Company / Wiley)

Every price point experiences leakage across the transaction chain:

```
  List Price ($100.00)
    │
    ├── (-) Standard Volume Discount (-$10.00)
    ├── (-) Sales Discretionary Concession (-$5.00)
    ├── (-) Payment Term Cash Discount (-$2.00)
    ├── (-) Free Onboarding / Service Credits (-$3.00)
    ├── (-) Freight / Infrastructure Subsidies (-$2.00)
    ├── (-) Payment Gateway & Processing (-$2.50)
    ▼
  Realized Pocket Price ($75.50)  <-- True Captured Revenue
```

### Governance Rules:
1. **Tiered Authorization Matrix:** Discretionary discounting strictly capped by seniority.
2. **Mandatory Quid-Pro-Quo:** Concessions must extract measurable contract value (longer terms, upfront annual cash, case study rights).
3. **Automatic Renewal Escalators:** Standard 5%–8% annual uplift clauses to offset inflation and compound ACV.

---

## 5. The Innovation Monetization Failure Taxonomy

1. **Feature Shock:** Over-engineering a product with bloated capabilities that inflate costs and confuse buyers without increasing WTP.
   * *Remedy:* Unbundle into a lean core tier and modular add-ons.
2. **Minnow (Underpricing):** Setting prices too low due to fear or ignorance of true differentiation value.
   * *Remedy:* Implement price elasticity tests and introduce high-margin Enterprise / VIP tiers.
3. **Hidden Gem:** A high-value capability buried as a free sub-feature of a commodity plan.
   * *Remedy:* Extract the feature and monetize it as an independent metered add-on or tier gateway.
4. **Undead:** An offering that satisfies internal engineering curiosity but possesses zero market demand or willingness-to-pay.
   * *Remedy:* Discontinue or pivot before allocating ongoing maintenance resources.
