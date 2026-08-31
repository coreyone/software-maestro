---
name: trust-safety-fraud-and-claims
description: "Trigger: trust-safety-fraud-and-claims, fraud ring, counterfeits, AirCover, property damage, KYC/KYB, sanctions screening, listing moderation, buyer protection. Scope: Trust, Safety, Fraud Defense & Physical Claims Arbitration. Governs multimodal content moderation, identity/AML screening, and binding physical damage claim adjudication. Boundary: Excludes low-level software secrets management (use secrets-management)."
---

# 🛡️ Core Philosophy: Safety, integrity, and fair adjudication are the bedrock of marketplace liquidity and trust.

## When to use

Use this skill when designing or executing trust and safety engines, multimodal content moderation, fraud ring mitigation, KYC/KYB sanctions screening, account takeover (ATO) defense, and binding physical damage/claim arbitration (e.g., Airbnb AirCover, Etsy Buyer Protection).

## When not to use

Do not use this skill for code-level secrets management (use `secrets-management`), general web application firewalls (use `developer-web-security`), or payment settlement ledgering (use `finance-payments-tax-and-treasury`).

## Trigger cues

- Key terms: trust and safety, content moderation, fraud detection, card testing, account takeover (ATO), fake listings, counterfeits, DMCA, KYC, KYB, OFAC, PEP, sanctions, FinCEN BOI, beneficial ownership, physical claims, AirCover, property damage, host claims, buyer protection, dispute arbitration, proof of condition.
- Processing listing moderation requests, fraud alerts, sanctions screening matches, or property/shipping damage claims.

## Routing boundary

- Primary for trust, safety, AML identity verification, content moderation, and physical claims arbitration.
- Secondary to `finance-payments-tax-and-treasury` for final financial ledger debit/credit postings.
- Secondary to `auth-and-identity-rules` for user login token mechanics.

## Inputs required

- Platform policy guidelines (e.g., community guidelines, prohibited item lists, damage coverage terms).
- Ingested evidence: images, video tours, message transcripts, corporate registry documents, police reports, receipts.
- Source of truth: `references/source.md`

## Instructions

1. **Multimodal Content & Listing Moderation**:
   - Ingest all listing assets: photos, 3D tours, titles, descriptions, and seller communication.
   - Run multimodal classification to detect prohibited items (weapons, drugs), counterfeit goods, fake property locations, and off-platform payment contact details (phone numbers in images, external URLs).
2. **KYC / KYB & Sanctions Compliance**:
   - Verify legal business registry filings, cross-check beneficial ownership (FinCEN BOI $\ge 25\%$), and match names against OFAC, PEP, and international sanctions lists.
   - Flag high-risk matches for human-in-the-loop (HITL) compliance officer review and maintain immutable audit logs for Suspicious Activity Reports (SAR).
3. **Fraud Ring & Account Takeover (ATO) Defense**:
   - Monitor real-time velocity signals: sudden IP/device changes, burst card authorizations, and listing price anomalies.
   - Trigger step-up authentication (Passkey / WebAuthn) or hold suspicious payouts immediately.
4. **Physical Claim & Damage Adjudication**:
   - Ingest claim evidence: timestamped pre-stay/pre-shipment baseline photos, post-incident damage photos, contractor repair invoices, police reports, and carrier transit logs.
   - Compare metadata (EXIF timestamps, GPS coordinates) between baseline and damage photos.
   - Compute allowable reimbursement based on platform terms, depreciation schedules, and pre-authorized policy caps.

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`:
- Multimodal listing inspection detecting policy violations and off-platform leakage.
- Automated KYC/KYB and sanctions screening with SAR audit trails.
- Evidence-backed physical damage claim adjudication validating photos and repair invoices.

## Output format

- Primary decision/output: Content moderation classifications, fraud risk scores, KYC verification records, and claim arbitration rulings.
- Summary: One-paragraph verdict or operational summary.
- Actions: Action items (e.g., listing takedown, account restriction, claim payout authorization, law enforcement referral).
