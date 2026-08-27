# God-Marduk Phased Development Workflow Reference

## 1. Phased Dependency Hierarchy

God-Marduk enforces strict dependency-directed engineering. Never create high-level user interfaces without verifying the underlying low-level primitives first:

```
┌──────────────────────────────────────────────────────────────┐
│ STAGE 0: Scaffolding                                         │
│ - Infrastructure, CI/CD pipeline, environment baseline      │
│ - Automated secret injection via 1Password MCP               │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│ STAGE 1: Foundation                                          │
│ - Data schemas, database migrations (expand-contract)        │
│ - Auth boundaries, domain model invariants, type definitions │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│ STAGE 2: Mechanism                                           │
│ - Core engine & business logic implemented via strict TDD    │
│ - Red-Green-Refactor with zero frontend UI dependencies      │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│ STAGE 3: Interface                                           │
│ - UI components wired to engine mechanisms                   │
│ - Design system tokens, WCAG AA compliance, tactile UX       │
│ - Resilient empty, loading, error, and offline states        │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│ STAGE 4: Hardening                                           │
│ - Security audits, input validation, CSRF/CORS/CSP           │
│ - Circuit breakers, timeouts, bounded backoff with jitter    │
│ - Bundle size and Core Web Vitals (LCP/INP) verification     │
└──────────────────────────────┬───────────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────────┐
│ STAGE 5: Synthesis                                           │
│ - Memory pipeline (Capture → Stabilize → Store → Update)     │
│ - Ralph Retrospective & Compound Learning documentation      │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Test-Driven Development (TDD) Protocol

Every functional initiative in Stage 2 must strictly execute the 3-step TDD cycle:

1. **RED (Write Failing Test):**  
   Create unit/integration test cases that assert exact expected behavior, error codes, and edge-case invariants. Run the test suite and verify that the tests fail with clear, unambiguous assertion errors.
2. **GREEN (Make Tests Pass):**  
   Write the minimal clean production code required to satisfy the failing tests.
3. **REFACTOR (Clean Architecture):**  
   Refactor code for modularity, readability, and performance without changing test outcomes.

---

## 3. Deming Systems Thinking Checkpoints

When unexpected failures occur during execution:
- **Audit Inputs:** Were the requirements or discovery artifacts underspecified?
- **Audit Feedback Loops:** Did a missing unit or integration test allow a regression to slip through?
- **Audit Standard Work:** Did the agent deviate from established design tokens or repository conventions?
