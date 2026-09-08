# Systems Retrospective & Process Pruning Framework

## 1. The Anti-Process Philosophy

Product Operations must actively prevent the accumulation of process debt. Every new template, meeting, or tool introduces cognitive load. High-performing ProdOps teams regularly conduct **Systems Retrospectives** to simplify and deprecate.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE SYSTEMS PRUNING MATRIX                            │
├──────────────────────────────┬──────────────────────────────────────────────┤
│ HIGH VALUE / LOW FRICTION    │ HIGH VALUE / HIGH FRICTION                   │
│ ➔ KEEP & AMPLIFY             │ ➔ AUTOMATE & STREAMLINE                      │
│ (Self-serve analytics, VoC   │ (Quarterly planning data packs,              │
│  problem repositories)       │  cross-functional release checklists)        │
├──────────────────────────────┼──────────────────────────────────────────────┤
│ LOW VALUE / LOW FRICTION     │ LOW VALUE / HIGH FRICTION                    │
│ ➔ MONITOR OR CONSOLIDATE     │ ➔ DEPRECATE IMMEDIATELY                      │
│ (Ad-hoc team newsletters,    │ (50-page PRD approval gates,                 │
│  redundant chat channels)    │  weekly status check-in meetings)            │
└──────────────────────────────┴──────────────────────────────────────────────┘
```

---

## 2. Quarterly Systems Retro Process (Amplitude / Uber Model)

### Step-by-Step Cadence:
1. **Quarterly Audit**: Catalogue all 1) Recurring meetings, 2) Required templates/artifacts, and 3) Paid product tools.
2. **Stakeholder Stack-Ranking**:
   - Survey PMs, Eng managers, and GTM partners: *"If you could eliminate one meeting and one template tomorrow, what would they be?"*
   - Stack-rank from 1 (Indispensable) to 10 (Pure overhead).
3. **Deprecation Mandate**:
   - The bottom 20% of tools or processes must either be fundamentally overhauled or formally deprecated within 30 days.

---

## 3. Tool Stack Governance Guidelines

| Layer | Standard Tools | Governance Rule | Red Flag |
| :--- | :--- | :--- | :--- |
| **Product Analytics** | Amplitude / Pendo | Single source of truth for user telemetry. | Multiple teams using divergent event definitions. |
| **Experimentation** | Optimizely / LaunchDarkly | Strict hypothesis, sizing, and kill criteria. | Zombie feature flags left in production code. |
| **Roadmapping** | Productboard / Dragonboat | Dynamic rollup from sprint to strategic intent. | Static PowerPoint decks used for roadmap sharing. |
| **Feedback Repo** | Dovetail / Notion | Atomized tagging linked to customer segments. | Feedback trapped in personal PM Google Docs. |
