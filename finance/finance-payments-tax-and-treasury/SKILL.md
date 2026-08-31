---
name: finance-payments-tax-and-treasury
description: "Trigger: finance-payments-tax-and-treasury, settlement rails, tax nexus, 1099-K, DAC7, VAT/GST, Airbnb TOT, dispute evidence, chargebacks, FX hedging, payout escrow. Scope: Multi-Rail Settlement, Marketplace Tax Nexus, Dispute Arbitration & Treasury Operations. Governs payout routing, multi-jurisdiction tax withholding, and chargeback defense. Boundary: Excludes client-side checkout visual UI (use commerce-ux-rules)."
---

# 💳 Core Philosophy: Money and tax obligations must balance to the cent with zero untracked liability.

## When to use

Use this skill when designing or operating payment settlement engines, multi-currency treasury pipelines, marketplace payout escrow systems, dynamic sales tax/VAT/TOT withholding calculation, 1099-K/DAC7 tax reporting, and automated chargeback dispute arbitration.

## When not to use

Do not use this skill for frontend checkout UI layout or styling (use `commerce-ux-rules`), database indexing (use `data-persistence-caching`), or user authentication (use `auth-and-identity-rules`).

## Trigger cues

- Key terms: payment rails, settlement, FedNow, RTP, SEPA, Pix, card networks, interchange, double-entry ledger, escrow holdback, seller payout, sales tax nexus, marketplace facilitator, VAT, GST, DAC7, 1099-K, Transient Occupancy Tax (TOT), chargeback, dispute evidence, representment, FX hedging, liquidity management.
- Implementing financial transaction reconciliation, tax withholding engines, payment dispute workflows, or multi-currency treasury operations.

## Routing boundary

- Primary for settlement rails, multi-jurisdictional tax compliance, dispute defense, and treasury operations.
- Secondary to `commerce-ux-rules` for customer checkout conversion and forms.
- Secondary to `developer-security` for secrets and encryption key management.

## Inputs required

- Payment service provider contracts and settlement formats (e.g., Stripe, Adyen, Banking APIs, FedNow/SEPA specs).
- Geographic footprint and transaction tax nexus thresholds (US States, EU Member States, UK, Canada, Australia, municipal jurisdictions).
- Source of truth: `references/source.md`

## Instructions

1. **Double-Entry Ledger Invariant**: Always model financial flows as immutable, double-entry ledger entries. Every debit must have an equal and offsetting credit. Never update balances with destructive `UPDATE` queries; always append balanced journal entries.
2. **Idempotency & Settlement Routing**: Ensure all payment webhooks, payout transfers, and refund disbursements include deterministic idempotency keys (`Idempotency-Key` or hashed transaction UUID).
3. **Escrow & Payout Holdbacks**: Enforce marketplace payout holdback windows based on risk tier, delivery confirmation (carrier tracking delivered webhook), or physical stay check-in + 24 hours.
4. **Automated Tax Nexus & Withholding**:
   - Continuously evaluate transaction volume and revenue against state/country economic nexus thresholds.
   - Dynamically compute and withhold state sales tax, EU VAT, and municipal occupancy taxes (Airbnb TOT) at point-of-sale.
   - Aggregate annual gross payment volume per seller/host to generate statutory 1099-K (US IRS) and DAC7 (EU) annual tax records.
5. **Chargeback Defense Automation**:
   - Ingest chargeback reason codes (e.g., Visa 10.4, Mastercard 4837).
   - Automatically compile evidence packets: proof of delivery (carrier tracking + GPS/signature), customer IP/device fingerprint audit trail, and timestamped terms of service acceptance.
6. **Treasury & FX Liquidity**:
   - Monitor multi-currency account balances against daily payout obligations.
   - Execute automated FX conversions using netting and target reserve corridors to mitigate currency fluctuation risk.

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`:
- Idempotent double-entry ledgering with escrow holdbacks.
- Multi-jurisdiction economic nexus tracking with automated tax withholding and 1099-K/DAC7 generation.
- Complete dispute defense packets with courier delivery proof, device/IP telemetry, and terms consent.

## Output format

- Primary decision/output: Financial architecture specs, double-entry schema definitions, tax withholding logic, dispute evidence generators, and treasury settlement policies.
- Summary: One-paragraph operational summary.
- Actions: Verification checklist covering ledger balance integrity, tax remittance accuracy, and dispute win-rate telemetry.
