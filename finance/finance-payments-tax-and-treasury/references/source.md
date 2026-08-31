# Autonomous Finance, Payments, Tax & Treasury Playbook

## 1. First Principles & Invariants

1. **Immutable Double-Entry Ledgering**: No monetary balance is ever updated in place. Every transaction is a balanced set of debits and credits across assets, liabilities, equity, revenues, and expenses. Total debits must strictly equal total credits ($\sum \text{Debits} = \sum \text{Credits}$).
2. **Idempotency Across All Rails**: Every financial API call, webhook handler, and settlement transfer must carry a deterministic idempotency key. Network retries must never cause duplicate debits or disbursements.
3. **Continuous Tax Liability Accrual**: Tax liability is recognized at the moment of payment authorization and held in a dedicated tax reserve liability account until remittance.
4. **Evidence-Backed Dispute Defense**: Every chargeback has a specific network reason code and strict statutory deadline. Dispute representments must deterministically match network evidence requirements.

---

## 2. Double-Entry Ledger Architecture

### Account Hierarchy Chart
- **Assets (1000-1999)**:
  - `1010` Operating Cash (Bank Accounts)
  - `1020` Settlement Clearing (Funds in Transit from Processors)
  - `1030` Reserve Accounts (Processor Holdbacks)
- **Liabilities (2000-2999)**:
  - `2010` Seller Escrow Payable (Held pending fulfillment)
  - `2020` Sales Tax Payable (State / Municipal)
  - `2030` VAT / GST Payable (International)
  - `2040` Customer Unearned Revenue (Prepaid bookings/credits)
- **Revenue (4000-4999)**:
  - `4010` Marketplace Take-Rate Fee Revenue
  - `4020` Payment Processing Fee Surcharges
- **Expenses (5000-5999)**:
  - `5010` Interchange & Processor Fees
  - `5020` Chargeback Losses & Fines

### Transaction Journal Entry Pattern
```json
{
  "journal_entry_id": "je_9f81a2bc-7d31-41ae",
  "transaction_ref": "txn_order_849201",
  "idempotency_key": "idem_849201_charge_succeeded",
  "timestamp": "2026-08-31T14:30:00Z",
  "postings": [
    {"account": "1020_settlement_clearing", "amount": 10000, "currency": "USD", "direction": "DEBIT"},
    {"account": "2010_seller_escrow_payable", "amount": 8500, "currency": "USD", "direction": "CREDIT"},
    {"account": "2020_sales_tax_payable", "amount": 500, "currency": "USD", "direction": "CREDIT"},
    {"account": "4010_marketplace_take_rate", "amount": 1000, "currency": "USD", "direction": "CREDIT"}
  ]
}
```

---

## 3. Marketplace Escrow & Payout Routing

### Release Schedules & Risk Corridors
- **Physical Goods (Etsy model)**: Payout released on carrier `status == "DELIVERED"` webhook + 24 hours. If unfulfilled after 7 days, hold escrow and alert risk queue.
- **Lodging / Experiences (Airbnb model)**: Payout released 24 hours after verified guest check-in timestamp.
- **Software / Subscriptions (Stripe / Notion model)**: Instant recognition to operating cash; prorated refunds booked against unearned revenue.
- **Rolling Reserves**: For new or high-risk sellers, maintain a 10% rolling 90-day reserve held in `2015_seller_risk_reserve`.

---

## 4. Multi-Jurisdictional Tax Nexus & Statutory Reporting

### Economic Nexus Matrix
- **US States**: Track gross receipts and transaction counts against state thresholds (e.g., California $500k, Texas $500k, New York $500k + 100 transactions).
- **Marketplace Facilitator Laws**: Automatically collect and remit sales tax on behalf of 3rd-party sellers once state facilitator thresholds are met.
- **Municipal Occupancy Tax (TOT)**: Compute local city/county hotel and tourist taxes based on precise geocoded property coordinates.
- **EU / UK VAT & Digital Services**: Enforce VAT MOSS / OSS rules; validate VAT IDs via VIES API and apply destination VAT rates.

### Statutory Reporting Automation
- **IRS Form 1099-K**: Aggregate calendar year gross payments per taxpayer identification number (TIN/SSN/EIN). Generate IRS electronic filing format and recipient copies.
- **EU DAC7 Directive**: Track seller identity, banking details, gross consideration, and fees paid. Generate annual DAC7 XML filings for member state tax authorities.

---

## 5. Automated Chargeback & Dispute Defense Pipeline

### Evidence Assembly Rule Matrix

| Dispute Reason Code | Core Evidence Required |
| :--- | :--- |
| **Fraud / Unrecognized** (Visa 10.4, MC 4837) | Carrier proof of delivery with GPS coordinates + signature; Customer account creation date; IP address & device fingerprint log; Timestamped Terms of Service acceptance. |
| **Product Not Received** (Visa 13.1, MC 4855) | Carrier tracking URL with confirmed delivery scan at buyer's verified billing/shipping address; In-app messaging history confirming receipt. |
| **Cancelled Recurring** (Visa 13.2, MC 4853) | Subscription cancellation policy presented at checkout; Log showing cancellation occurred after billing cut-off; Post-cancellation product usage logs. |

### Automated Representment Builder
```python
def compile_dispute_packet(chargeback_event):
    order = db.get_order(chargeback_event.order_id)
    carrier_tracking = shipping_api.get_tracking(order.tracking_number)
    audit_log = security_api.get_session_audit(order.checkout_session_id)
    
    return {
        "dispute_id": chargeback_event.dispute_id,
        "evidence": {
            "customer_name": order.customer_name,
            "customer_email": order.customer_email,
            "customer_ip_address": audit_log.ip_address,
            "device_fingerprint": audit_log.device_fingerprint,
            "service_date": order.created_at,
            "billing_address": order.billing_address,
            "shipping_address": order.shipping_address,
            "shipping_tracking_number": order.tracking_number,
            "shipping_carrier": order.carrier,
            "shipping_documentation": carrier_tracking.delivery_receipt_url,
            "shipping_date": carrier_tracking.shipped_at,
            "delivery_date": carrier_tracking.delivered_at,
            "customer_communication": order.in_app_chat_transcript,
            "terms_of_service_disclosure": "User consented to Terms of Service on checkout at " + order.tos_accepted_at,
            "refund_policy_disclosure": order.store_policy_url
        }
    }
```

---

## 6. Treasury & Multi-Currency Liquidity

1. **Target Balance Corridors**: Maintain 3 days of expected payout volume in operating payout accounts (e.g., Chase, Silicon Valley Bank, Barclays, Stripe Treasury).
2. **Automated Netting & FX Execution**: Settle international transactions into local currencies daily using algorithmic netting to minimize FX conversion spreads.
3. **Failure Alarms**: Trigger automated circuit breaker when settlement account variance exceeds 0.01% or when payout return rates exceed 0.5%.
