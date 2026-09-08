# Product Release Readiness & GTM Lifecycle Framework

## 1. Release Tiering Taxonomy

| Tier | Definition | GTM Scope & Lead Time | Core Deliverables Required |
| :--- | :--- | :--- | :--- |
| **Tier 1 (Major)** | Net-new product, major paradigm shift, monetization change, or enterprise expansion. | 6–8 weeks lead time. Company-wide enablement, PR/marketing campaign, executive sign-off. | Launch brief, press memo, customer webinar, sales deck & pricing guide, support training, legal review, beta program readout. |
| **Tier 2 (Medium)** | Significant feature enhancement, major workflow improvement, or new integration. | 3–4 weeks lead time. Targeted marketing, customer newsletter, standard sales update. | In-app announcement, release notes, customer help center docs, sales demo script, support macro updates. |
| **Tier 3 (Minor / Patch)** | UI polish, minor capability, bug fixes, performance improvements, internal tools. | 1–2 weeks lead time. Self-serve release notes and internal squad briefing. | Public changelog entry, internal squad release notes, monitoring dashboard. |

---

## 2. Product Development Status Guidelines & Sales Boundaries

To prevent premature customer commitments and roadmaps being misused by sales teams, enforce strict gating:

```
[ Discovery ] ─────────► [ Alpha ] ─────────► [ Beta ] ─────────────► [ General Availability ]
      │                     │                    │                           │
  Internal only         Internal &           Sales can discuss           Live, fully packaged,
  Sales CANNOT          friendly tests       concept & timeline          ready to be sold
  discuss               Sales CANNOT sell    Sales CANNOT commit         and implemented
```

### Phase Guardrails:
* **Discovery (0–20% Confidence)**:
  - *Definition*: Problem discovery, technical feasibility, user prototype validation.
  - *Sales Boundary*: Strictly internal. Sales **CANNOT** mention, pitch, or document in RFPs.
* **Alpha (20–50% Confidence)**:
  - *Definition*: Functional prototype tested on internal teams and a few trusted design partners under strict NDA.
  - *Sales Boundary*: Sales **CANNOT** quote, sell, or promise delivery dates.
* **Beta (50–90% Confidence)**:
  - *Definition*: Feature complete, testing stability, scalability, and UX friction with opt-in cohort.
  - *Sales Boundary*: Sales **CAN** discuss concepts and high-level release quarters, but **CANNOT** make contractual commitments or add custom terms.
* **General Availability (100% Launch)**:
  - *Definition*: Full public release, billing enabled, telemetry operational, SLA backed.
  - *Sales Boundary*: Ready to sell, demo, and contract.

---

## 3. Cross-Functional Launch Readiness Matrix

Before greenlighting a GA release, all functions must verify completion:

| Function | Required Milestone / Deliverable | Owner | Verification Evidence |
| :--- | :--- | :--- | :--- |
| **Product** | Feature complete, telemetry instrumented, GA sign-off | Lead PM | Amplitude/Mixpanel tracking live |
| **Engineering** | Scalability tested, error rate < 0.1%, rollback runbook ready | Tech Lead | Load test report & Datadog alerts |
| **Marketing** | Positioning brief, blog post, email campaign, website update | PMM | Staging links & collateral review |
| **Sales** | Battlecard, demo script, pricing/packaging sheet, team trained | Sales Ops | Demo Day session recorded |
| **Customer Success** | Customer migration guide, tiering impact, high-touch training | CS Lead | Account list & outreach plan |
| **Support** | Help center articles, troubleshooting guide, Zendesk macros | Support Lead | Help center articles staged |
| **Legal / Security** | Terms of service updated, DPA compliant, security sign-off | Legal Counsel | Written approval |
