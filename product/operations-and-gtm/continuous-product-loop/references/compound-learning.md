# Ralph Loop & Compound Learning Architecture Reference

## 1. Ralph Loop: Failures Are Data

The Ralph Loop treats every runtime error, layout break, or race condition as institutional training data:

```text
[Hurdle / Failure Encountered]
             │
             ▼
1. Reproduce: Capture exact command / action
             │
             ▼
2. Classify: Auth | Logic | Environment | Contract | Styling
             │
             ▼
3. Minimal Fix: Apply smallest verified patch
             │
             ▼
4. Verify: Run regression test / dry-run
             │
             ▼
5. Codify: Append imperative rule to .product-loop/rules.md
```

---

## 2. Compound Solution Documentation (`docs/solutions/`)

For every non-trivial solution, create a markdown document in `docs/solutions/[category]/[slug]-[YYYYMMDD].md` with validated YAML frontmatter:

```markdown
---
module: "Cart & Checkout Flow"
date: 2026-08-27
problem_type: "state_management_sync"
component: "checkout_wizard"
symptoms:
  - "Stale shipping address rendered after step transition"
root_cause: "stale_closure_in_async_step_transition"
severity: "high"
tags: [react, state, wizard, checkout, sync]
---

# Solution: Stale Shipping Address in Async Step Transition

## Problem Summary
Address state was closed over in step transition hook before store dispatch completed.

## Failed Attempts
1. Added setTimeout delay before transition (flaky).

## Verified Solution
Awaited persistence promise before triggering step navigation:

```typescript
// ❌ WRONG
const handleNext = () => {
  saveAddress(localState);
  goToNextStep();
};

// ✅ CORRECT
const handleNext = async () => {
  const updated = await saveAddress(localState);
  if (updated.success) goToNextStep();
};
```

## Prevention Rule
Rule 14: Never trigger step transitions until asynchronous persistence promises resolve.
```

---

## 3. Critical Patterns (Required Reading)

The file `docs/solutions/patterns/critical-patterns.md` is loaded at Phase 0 of every single iteration.

Criteria for promotion to Critical Patterns:
1. High-severity foundational bugs (Auth, database migration locks, memory leaks).
2. Recurring mistakes that appeared across 3 or more cycles.
3. Non-obvious framework quirks that break production builds.
