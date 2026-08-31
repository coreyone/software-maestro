# Canonical References & Operational Standards: Executive Async Memos

This document provides foundational theory, executive communication methodology, and prompt transformation heuristics for asynchronous executive memos.

---

## 1. Theoretical Foundations of Executive Async Communication

### 1.1 Axios Smart Brevity (Jim VandeHei, Mike Allen, Roy Schwartz)
- **Origin:** Created by the founders of Politico and Axios (*Smart Brevity: The Power of Saying More with Less*, 2022).
- **Core Axiom:** Readers decide whether to read content within 15 seconds. Attention is fragmented; traditional memo formats waste readers' time with preamble.
- **The 4 Pillars of Smart Brevity:**
  1. **The Muscular Headline:** Strong, active verb phrase that conveys the news immediately ($\le 10$ words).
  2. **The Axiom / Lead Sentence:** The single most critical fact or development.
  3. **Visual Anchors (Signposts):** Bolded lead-ins (**Why it matters:**, **The big picture:**, **Go deeper:**, **By the numbers:**, **What's next:**) allow executive scanning in seconds.
  4. **The "Why It Matters" Context:** Explains the stakes immediately after the lead.

### 1.2 Amazon 1-Page & 6-Page Narrative Architecture (Jeff Bezos / Colin Bryar)
- **Origin:** Documented in *Working Backwards: Insights, Stories, and Secrets from Inside Amazon* (Colin Bryar & Bill Carr, 2021).
- **Narrative Over PowerPoint:** Bullet points hide sloppy thinking. Full narrative prose forces clear logical connections between cause, mechanism, and effect.
- **Components of the Strategic 1-Pager:**
  - Executive thesis and customer problem.
  - Type 1 (irreversible) vs. Type 2 (reversible) classification.
  - Rigorous evaluation of alternatives and rejected options.
  - Single-owner action commitments.

---

## 2. Integrated Writing Standards

### 2.1 ASD-STE100 & Google DevDocs Compliance
- Procedural sentences $\le 20$ words; descriptive sentences $\le 25$ words.
- Imperative verbs for actions (`Add`, `Deploy`, `Fix`, `Configure`, `Approve`).
- Mandatory connectors: `because` (cause), `after` (sequence), `can`/`must` (permission/requirement).

### 2.2 Info-to-Ink Compression
- Strip conversational greetings ("Hi everyone", "Hope you're having a good week").
- Strip speculative throat-clearing ("I've been thinking about this for a while and...").
- Preserve exact technical tokens, code identifiers, numbers, metrics, and dates.

### 2.3 Strunk & White Active Voice
- Use active voice: *"@Alex deploys the cluster"* instead of *"The cluster will be deployed by Alex"*.
- State assertions in positive form.

---

## 3. End-to-End Slack Thread Transformation Example

```
[Raw Slack Discussion Thread]
@sarah (10:14 AM): Hey team, heads up: our Postgres DB on RDS is hitting 85% CPU during peak European hours (9 AM - 12 PM GMT). We had 3 connection timeout alerts yesterday.
@dave (10:17 AM): Yeah, I looked into it. It's because the mobile app is polling /api/feed every 3 seconds instead of using WebSockets or pushing notifications.
@alex (10:22 AM): Can we just vertically scale the DB instance from db.r6g.xlarge to 2xlarge? It would cost about $350/mo extra but gives us immediate breathing room.
@sarah (10:25 AM): Scaling gives us room for this week, but it's a band-aid. We need the mobile team to increase the polling interval to 30s or implement conditional HTTP caching (ETags).
@dan (Engineering Lead) (10:30 AM): Here's the plan:
1. Alex: Upscale RDS to 2xlarge today during the 2 PM maintenance window to prevent outages (Type 2 reversible).
2. Dave: Submit PR to mobile app implementing 30-second polling and ETag support by Thursday.
3. Sarah: Verify CPU drops below 40% on Friday morning peak.

[Transformed Executive Async Memo — Smart Brevity Format]
# Upscale RDS and Patch Mobile Polling to Resolve DB Spikes
**Date:** 2026-08-31 | **Author:** @Dan | **Audience:** Engineering Leadership

## Executive Summary
**Temporarily upscale RDS database to prevent European peak outages while mobile squad deploys polling fix.**

- **Why it matters:** Database CPU peaked at 85% with three connection timeout alerts yesterday because the mobile feed polls every 3 seconds.
- **The big picture:** Vertical scaling provides immediate headroom for \$350/month while the permanent application caching fix is implemented.

## Go Deeper
- **Core Decision:** Upscale RDS from `db.r6g.xlarge` to `db.r6g.2xlarge` during today's 2:00 PM maintenance window (`Type 2 Reversible`).
- **Permanent Remediation:** Mobile app will increase polling interval from 3s to 30s and implement HTTP ETag caching.
- **Trade-offs Evaluated:** Deferring vertical scaling was rejected because traffic growth risks customer-facing database outages during tomorrow's peak.

## By the Numbers
- **CPU Peak:** 85% (Target: <40%)
- **Connection Alerts:** 3 timeout events in last 24h
- **Cost Delta:** +$350/month for temporary instance upscale
- **Target Polling Frequency:** 30 seconds (10x reduction in query volume)

## What's Next
| Single Owner (DRI) | Imperative Action Item | Hard Deadline |
| :--- | :--- | :--- |
| @Alex | Upscale RDS instance to `db.r6g.2xlarge` during 2:00 PM maintenance window | 2026-08-31 |
| @Dave | Deploy mobile app PR with 30s polling interval and ETag caching | 2026-09-03 |
| @Sarah | Verify European peak CPU utilization remains below 40% | 2026-09-04 |
```

---

## 4. Canonical Bibliography

- **Jim VandeHei, Mike Allen, Roy Schwartz:** *Smart Brevity: The Power of Saying More with Less* (Workman Publishing, 2022)
- **Colin Bryar & Bill Carr:** *Working Backwards: Insights, Stories, and Secrets from Inside Amazon* (St. Martin's Press, 2021)
- **William Strunk Jr. & E.B. White:** *The Elements of Style* (4th Edition, Pearson, 1999)
- **AeroSpace and Defence Industries Association of Europe:** *ASD-STE100 Simplified Technical English* (Issue 8, 2021)
