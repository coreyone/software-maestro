---
name: legal-contracts-and-compliance
description: "Review master services agreements, data processing addenda, and enterprise software compliance standards."
---

# ⚖️ Core Philosophy: Clear contracts, strong liability boundaries, and verifiable compliance unlock enterprise velocity.

## When to use

Use this skill when reviewing and redlining enterprise B2B contracts (MSAs, DPAs, SLAs, Business Associate Agreements), filling out customer security questionnaires (Whistic, Conveyor, OneTrust, spreadsheets), and assembling continuous audit evidence for SOC 2 Type II, ISO 27001, PCI-DSS, HIPAA, or the EU AI Act.

## When not to use

Do not use this skill for implementing code-level application security defenses like CSP headers or SQL escaping (use `developer-security`), or configuring OAuth 2.1 authentication tokens (use `auth-and-identity-rules`).

## Trigger cues

- Key terms: Master Services Agreement (MSA), Data Processing Agreement (DPA), Service Level Agreement (SLA), Business Associate Agreement (BAA), limitation of liability, indemnification, intellectual property assignment, redline, fallback playbook, security questionnaire, Whistic, Conveyor, OneTrust, SOC 2 Type II, ISO 27001, PCI-DSS Level 1, HIPAA, GDPR Standard Contractual Clauses (SCCs), EU AI Act, audit evidence vault.
- Reviewing enterprise customer contracts, completing vendor security audits, or preparing for annual compliance audits.

## Routing boundary

- Primary for enterprise contract redlining, vendor security questionnaire automation, and compliance audit frameworks.
- Secondary to `developer-security` for technical vulnerability scanning and code-level CVE remediation.
- Secondary to `product-pricing-strategy` for commercial deal packaging and discount approval matrices.

## Inputs required

- Inbound contract documents (.docx, markdown, or PDF).
- Company standard legal playbook and risk thresholds (liability caps, IP preservation, governing law).
- Verifiable security & compliance artifacts (SOC 2 Type II report, ISO certificates, penetration test executive summaries).
- Source of truth: `references/source.md`

## Instructions

1. **Contract Ingestion & Clause Extraction**:
   - Parse inbound agreement into discrete clauses: (1) Grant of Rights / IP, (2) Fees & Payment, (3) Warranties, (4) Mutual Indemnification, (5) Limitation of Liability, (6) Data Privacy / Security, (7) Term & Termination, (8) Governing Law.
2. **Autonomous Redlining Against Legal Playbook**:
   - *Limitation of Liability*: Strictly reject uncapped liability. Insist on a mutual cap of 1x–2x Annual Contract Value (ACV). Super-caps (e.g., for gross negligence or data breach) must not exceed 3x–5x ACV.
   - *Intellectual Property*: Ensure company retains 100% ownership of underlying software, platform architecture, pre-existing IP, and AI model weights/embeddings. Only grant customers a limited, non-exclusive license to use the service.
   - *Indemnification*: Enforce mutual IP infringement indemnification with standard exclusions (modifications, unauthorized combinations). Reject customer requests for unilateral customer defense obligations.
   - *Data Processing (DPA)*: Ensure GDPR compliance via EU Standard Contractual Clauses (SCCs), clearly declare subprocessors, and restrict customer data usage exclusively to service delivery.
3. **Security Questionnaire Auto-Fill Engine**:
   - Parse incoming questions and map them to verified SOC 2 Type II Trust Services Criteria (Security, Availability, Confidentiality) and ISO 27001 Annex A controls.
   - Provide exact, verifiable citations (e.g., citing AES-256 encryption at rest, TLS 1.3 in transit, role-based access control, quarterly penetration tests, and annual disaster recovery failover exercises).
4. **Continuous Compliance Audit Vault**:
   - Continuously harvest and timestamp machine-readable evidence: IAM privilege access reviews, branch protection PR approvals (two-person rule), static code analysis results, and dependency vulnerability scans.

## Completion gate

Before reporting completion, verify the applicable binary contracts in `evals/cases.json`:
- Contract redlining capping liability, preserving core IP/model weights, and enforcing mutual indemnity.
- Security questionnaire responses mapped to exact SOC 2 / ISO 27001 audit control citations.
- Continuous compliance audit evidence collection covering IAM, change management, and vulnerability scans.

## Output format

- Primary decision/output: Redlined contract markup with explanatory comment bubbles, completed security questionnaire response matrix, or structured compliance evidence manifest.
- Summary: Executive legal & security risk assessment.
- Actions: Deal blockers, required approvals, and next negotiation steps.
