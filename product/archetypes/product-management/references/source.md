# Product Management: Strategy, PRD Authoring, & Archetype Governance

Product management translates ambiguous customer problems and company vision into **crisp, testable, decision-ready specifications and execution roadmaps**.

---

## 1. The 4 Specialized Product Archetypes

General product management connects to four specialized archetype engines depending on the product lifecycle stage and operational constraint:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     THE 4 SPECIALIZED PRODUCT ARCHETYPES                    │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 1. 0-TO-1 DISCOVERY & PMF            │ 2. GROWTH & RETENTION LOOPS          │
│ Skill: /product-zero-to-one          │ Skill: /product-growth               │
│ • Steve Blank (Customer Dev)         │ • Brian Balfour (4 Fits & Loops)     │
│ • Eric Ries (Lean Startup & MVPs)    │ • Fareed Mosavat (Retention First)   │
│ • Teresa Torres (OSTs & Discovery)   │ • Elena Verna (Product-Led Growth)   │
│ • Rahul Vohra (40% PMF Engine)       │ • Nir Eyal (The Hooked Model)        │
│ • Clayton Christensen (JTBD Forces)  │ • Josh Elman (The Core Action)       │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 3. FEATURE & OPTIMIZER SCALING       │ 4. TWO-SIDED MARKETPLACES            │
│ Skill: /product-optimizer-feature    │ Skill: /product-marketplace          │
│ • Marty Cagan (4 Product Risks)      │ • Andrew Chen (Cold Start & Atomic)  │
│ • John Cutler (Metric Trees & Flow)  │ • Casey Winters (Marketplace Loops)  │
│ • Shreyas Doshi (Pre-Mortem & LNO)   │ • Dan Hockenmaier (Liquidity Engine) │
│ • Don Norman & Steve Krug (Usability)│ • Bill Gurley (10 Marketplace Rules) │
│ • Baymard Institute (Checkout UX)    │ • Gokul Rajaram (SPADE & Take-Rate)  │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 2. Decision-Ready PRD Specification Blueprint

A high-performance Product Requirements Document (PRD) must eliminate ambiguity:

1. **Problem Statement & Customer Evidence**:
   - What exact pain point is being solved?
   - What quantitative or qualitative evidence proves this is painful and urgent?
2. **Target Persona & Context**:
   - Who is the specific user? What is their job-to-be-done?
3. **Goals & Explicit Non-Goals**:
   - **Goals**: Quantifiable target metrics (e.g. Increase conversion by 15%).
   - **Non-Goals**: What are we deliberately choosing *not* to build in this release?
4. **Key User Flows & Edge Cases**:
   - Happy path step-by-step walkthrough.
   - Unhappy paths: offline state, invalid input, permission failure, network timeout.
5. **Success Metrics & Guardrails**:
   - Primary Success Metric (North Star / Driver metric).
   - Guardrail Metrics (e.g. latency $p95 < 200	ext{ms}$, unsubscribe rate $< 0.5\%$).
6. **Cross-Functional Impact Checklist**:
   - Security / Auth / Privacy (GDPR, PII).
   - Billing / Pricing / Tax compliance.
   - Customer Support / Documentation readiness.
