# Modern Empirical Product Hypothesis Loop

## 1. First Principles & Theoretical Lineage
- **Tara Seshan (The Empirical Loop)**: Product management is not about writing 20-page speculative decks; it is the discipline of rapid, prolific hypothesis formulation and empirical testing.
- **Marty Cagan (The 4 Risks)**: Isolate Value, Usability, Feasibility, and Viability risks upfront.
- **Teresa Torres (Continuous Assumption Testing)**: Test the atomic assumptions *underlying* an idea rather than building the entire idea.
- **The Ralph Loop & Continuous Product Loop**: Treat test outcomes as immutable empirical learning data. Codify failure modes immediately into system knowledge.

---

## 2. The 3-Variable Intersection Matrix

```
                            THE 3-VARIABLE INTERSECTION
                                         ▲
                                        /                                        /                                         /                            [ USERS ] ────┼───────┼──── [ MARKET ]
                       Desirability  │ HYPO- │     Viability
                       & Psychology  │ THESIS│     & Economics
                                     \       /
                                      \     /
                                       \   /
                                        \ /
                                         ▼
                                  [ TECHNOLOGY ]
                                   Feasibility
                                   & Constraints
```

1. **Users**:
   - What behavioral habit or emotional friction is being resolved?
   - What is the existing painful workaround?
2. **Market**:
   - What is the customer's willingness-to-pay threshold?
   - What are the unit economics and channel CAC-to-LTV payback mechanics?
3. **Technology**:
   - What technical capability (e.g., fast LLM inference, WebAssembly, edge workers) makes this viable today?
   - What latency budget or API reliability invariant must hold?

---

## 3. Empirical Test Vehicle Dispatcher

| Risk Tested | Uncertainty Focus | Fastest Test Vehicle | Execution Time | Linked Skill |
| :--- | :--- | :--- | :--- | :--- |
| **Value & Usability** | Will users understand and want the solution? | 24h Disposable Hollywood Facade + 5-Act Live User Interviews | 1–3 Days | `design-rapid-prototype-facade` + `design-5-act-user-interview-testing` |
| **Demand & Price** | Will users commit budget or pre-order? | Smoke Test / Fake Door Landing Page | 24 Hours | `design-landing-page` + `commerce-ux-rules` |
| **Feasibility & Speed**| Can we process the data within latency limits? | 1-Day Architectural Spike (<200 LOC) | 1 Day | `developer-development-rules` (Spike Mode) |
| **Optimization Lift** | Does variant A increase conversion over B? | 14-Day Statistical A/B Experiment | 14 Days | `experimentation-hypothesis-engine` |

---

## 4. The 1-Page Hypothesis Card Schema

```markdown
# Hypothesis Card: [Opportunity Name]
**Upstream Inputs:** [ux-discovery-artifacts.md | design-sprint-map.md]
**Date & Cycle:** [YYYY-MM-DD | Cycle #]

## 1. The 1 Essential Question
*"[Single falsifiable question that determines product success or failure]?"*

## 2. The 3-Variable Intersection
- **Users (Psychology & Friction)**: [Observed behavioral struggle and workaround]
- **Market (Viability & Willingness-to-Pay)**: [Price point, CAC/LTV dynamics, competitive alternative]
- **Technology (Feasibility & Enablers)**: [Key technical invariant, API contract, or latency budget]

## 3. The Empirical Test Vehicle
- **Selected Vehicle**: [24h Hollywood Facade | Smoke Test | 1-Day Spike | A/B Test]
- **Execution Blueprint**: [Step-by-step description of what will be exposed to participants]
- **Sample Size & Target Cohort**: [e.g., 5 ICP users | 500 landing page visitors]

## 4. Pre-Committed Decision Thresholds
- **PASS (Proceed to PRD)**: [Explicit numeric threshold, e.g., >=4/5 users complete task unassisted]
- **PIVOT (Re-test with new variable)**: [Threshold indicating interest but UX confusion]
- **KILL (Abandon opportunity)**: [Threshold indicating fundamental lack of demand]

## 5. Next-Step Action Handoff
- If PASS -> Graduate to `/create-prd` and `/product-management-press-memo`.
- If PIVOT -> Refine variable and re-run `/product-hypothesis-loop`.
```
