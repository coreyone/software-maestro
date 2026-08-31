# Enterprise Legal Contracts & Continuous Compliance Playbook

## 1. First Principles & Invariants

1. **Strict Limitation of Liability**: Never execute an enterprise agreement with uncapped liability. Standard cap is $1\times$ to $2\times$ the fees paid or payable by Customer in the preceding 12 months (Annual Contract Value / ACV).
2. **Absolute Preservation of Core IP & Model Weights**: Customer owns their raw customer data and direct customer outputs. Company strictly retains all rights, title, and interest in and to the platform, underlying software, APIs, algorithms, model architectures, weights, embeddings, and aggregate usage telemetry.
3. **Evidence-Grounded Security Disclosures**: Every answer in a vendor security questionnaire must trace directly to an official audit report (SOC 2 Type II, ISO 27001 certificate, or independent penetration test report). Never speculate or promise unreleased security features in a contractual questionnaire.

---

## 2. Enterprise MSA Clause Negotiation Playbook

| Contract Term | Preferred Position (Level 1) | Acceptable Fallback (Level 2) | Deal-Killer Position (Walk Away) |
| :--- | :--- | :--- | :--- |
| **Limitation of Liability** | Capped at 12 months fees paid ($1\times\text{ ACV}$). Mutual. | Super-cap of $2\times\text{--}3\times\text{ ACV}$ solely for data breach / confidentiality breaches. | Uncapped liability or super-caps exceeding $5\times\text{ ACV}$. |
| **Intellectual Property** | Company owns all platform components, models, and derivative algorithms. | Customer owns specific customized user-facing workflow definitions and reports. | Assigning underlying model weights, source code, or inventions to customer. |
| **Indemnification** | Mutual IP infringement indemnity capped by standard liability terms. | Uncapped IP indemnity subject to standard exceptions (customer modifications/combinations). | Defending customer against 3rd-party claims arising from customer's own content or data misuse. |
| **Termination for Convenience** | Not permitted. Multi-year commitments non-cancelable except for material breach. | Permitted with 60 days notice + payment of 50% remaining contract value. | Immediate termination for convenience with full pro-rata refund of prepaid fees. |
| **Service Level Agreement (SLA)** | 99.9% monthly uptime. Remedy strictly limited to service credits (max 10% monthly fee). | 99.95% monthly uptime. Tiered service credits up to 20% of monthly fee. | Liquidated cash damages or breach of contract penalties for service outages. |

---

## 3. Data Processing Agreement (DPA) & Privacy Terms

- **Subprocessor Notification**: Provide 30 days advance notice via email / public RSS feed of new subprocessors. Customer may object on reasonable data protection grounds.
- **Cross-Border Transfers**: Incorporate the European Commission's Standard Contractual Clauses (EU SCCs 2021/914 Module 2: Controller-to-Processor) and UK International Data Transfer Addendum.
- **Data Deletion / Return**: Provide automated export of customer data upon termination and certify complete cryptographic erasure from production and backup stores within 30 days.

---

## 4. Security Questionnaire Response Matrix (SOC 2 / ISO 27001 Mapping)

| Domain | Standard Question | Verified Enterprise Answer | Supporting Control Citation |
| :--- | :--- | :--- | :--- |
| **Encryption** | Are data encrypted in transit and at rest? | Yes. Data at rest are encrypted using AES-256 via AWS/GCP KMS with annual key rotation. Data in transit are encrypted using TLS 1.3 with mandatory HTTPS/HSTS. | SOC 2 Type II Control CC6.1, CC6.6; ISO 27001:2022 A.8.24 |
| **Access Control** | How is access to production systems managed? | Role-Based Access Control (RBAC) enforced with mandatory hardware multi-factor authentication (MFA/FIDO2). Production access requires Just-In-Time (JIT) approval with 8-hour maximum session lifetime. | SOC 2 Type II Control CC6.2, CC6.3; ISO 27001:2022 A.5.15, A.9.4 |
| **Vulnerability Mgmt** | How frequently are penetration tests and vulnerability scans conducted? | Automated container and dependency CVE scanning runs on every pull request. Independent CREST-accredited penetration testing is performed annually. | SOC 2 Type II Control CC7.1; ISO 27001:2022 A.8.8 |
| **Business Continuity** | What are your documented RPO and RTO targets? | Recovery Point Objective (RPO) is $< 1\text{ hour}$ (continuous multi-region database replication). Recovery Time Objective (RTO) is $< 4\text{ hours}$. Annual disaster recovery failover drills are conducted. | SOC 2 Type II Control CC9.1; ISO 27001:2022 A.5.29, A.5.30 |

---

## 5. Continuous Compliance Audit Evidence Vault

### Automated Evidence Collectors
1. **Infrastructure as Code (IaC) State**: Export daily Terraform/OpenTofu plan outputs confirming encryption and firewall ingress rules.
2. **Access & Permission Audits**: Run scheduled queries against Okta/Google Workspace/AWS IAM exporting active user lists, verifying 0 orphan accounts, and confirming 100% MFA enrollment.
3. **Change Management Proof**: Extract GitHub/GitLab pull request metadata verifying branch protection rules (minimum 1 peer approval, passed CI/CD security linters) for 100% of production deployments.
