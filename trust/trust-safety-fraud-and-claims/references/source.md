# Autonomous Trust, Safety, Fraud & Claims Playbook

## 1. First Principles & Invariants

1. **Multimodal Ground Truth**: Never rely solely on user-submitted text descriptions. Cross-reference visual media (photos, videos), metadata (EXIF timestamps, GPS coordinates), network signals (IP, ASN, device hashes), and commercial registries.
2. **Proportional Risk Response**: Tier enforcement actions strictly by risk:
   - *Low Risk*: Soft warning / automated listing edit prompt.
   - *Medium Risk*: Payout hold + step-up biometric/Passkey identity verification.
   - *High / Critical Risk*: Instant account freeze + listing takedown + legal / SAR escalation.
3. **Impartial Evidence-Based Adjudication**: In claims between two platform participants (guest vs host, buyer vs seller), the burden of proof rests on documented, timestamped evidence.

---

## 2. Multimodal Content & Listing Moderation Engine

### Content Policy Inspection Pipeline
```
[Listing Submission / Update]
       │
       ├──► [Text Policy Engine]: Prohibited keywords, toxic sentiment, PII / contact leakage (regex + embedding similarity)
       ├──► [Image / Video Vision Model]: Weapon/drug detection, nudity/NSFW, copyright/trademark counterfeit logos
       └──► [OCR & Steganography Engine]: Phone numbers, email addresses, QR codes disguised in images to evade platform fees
       │
[Aggregated Policy Score] ──► (Score >= 0.85: Auto-Reject) | (0.50-0.84: Flag for Human Review) | (< 0.50: Approve)
```

---

## 3. KYC / KYB & Anti-Money Laundering (AML) Compliance

### Verification Workflow
1. **Business Identity (KYB)**:
   - Query national corporate registries (e.g., OpenCorporates, Secretary of State, Companies House).
   - Verify Tax Identification Number (EIN/VAT) and physical business operating address.
2. **Beneficial Ownership (FinCEN BOI / EU AMLD6)**:
   - Identify all ultimate beneficial owners holding $\ge 25\%$ equity or voting control.
   - Collect government ID, residential address, and SSN/Passport numbers.
3. **Sanctions & Watchlist Screening**:
   - Run daily fuzzy name-matching against OFAC SDN, UK HMT, EU Consolidated Sanctions, and Interpol Red Notices.
   - Match Politically Exposed Persons (PEP) and close associates; flag for enhanced due diligence.
4. **Suspicious Activity Reports (SAR)**:
   - Automatically compile transaction timelines, identity dossiers, and IP access logs into FinCEN XML / national FIU format for compliance officer signing.

---

## 4. Account Takeover (ATO) & Fraud Ring Defense

### Signal Scoring Matrix
- **Device & Network**: New device fingerprint + high-risk VPN/proxy IP + mismatched geolocation ($\Delta > 500\text{ miles}$ in $< 1\text{ hour}$).
- **Behavioral Velocity**: Password change followed within 10 minutes by bank payout account change and maximum withdrawal request.
- **Card Testing Patterns**: $\ge 5$ distinct card numbers attempted in $< 60\text{ seconds}$ on low-value items.

### Automated Mitigation Actions
```python
def evaluate_session_risk(session_event):
    risk_score = 0.0
    if session_event.is_tor_or_datacenter_ip:
        risk_score += 0.40
    if session_event.bank_account_modified_within_hours(24):
        risk_score += 0.35
    if session_event.device_is_unrecognized:
        risk_score += 0.25
        
    if risk_score >= 0.75:
        freeze_payouts(session_event.user_id, reason="ATO_SUSPICION")
        require_webauthn_passkey_stepup(session_event.user_id)
        alert_security_operations_center(session_event)
```

---

## 5. Physical Claims & Property Damage Adjudication

### Evidence Assessment Protocol (Airbnb AirCover / Etsy Buyer Protection)
1. **Baseline Validation**: Verify host/seller provided timestamped pre-event baseline photos (taken within 72 hours prior to reservation/shipment).
2. **Damage Verification**:
   - Verify EXIF metadata of damage photos matches the property GPS coordinates and incident reservation dates.
   - Run AI image analysis to differentiate normal wear-and-tear from acute physical damage (e.g., broken furniture, water damage, smoke residue).
3. **Invoice & Repair Validation**:
   - Validate contractor/artisan license number and business entity registration.
   - Compare itemized labor and material costs against regional market averages (e.g., RSMeans construction cost index).
4. **Binding Settlement Determination**:
   - Calculate payout = $\min(\text{Verified Repair Cost} - \text{Depreciation}, \text{Policy Cap})$.
   - Post payout authorization to `finance-payments-tax-and-treasury` ledger.
