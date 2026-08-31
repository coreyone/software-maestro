# Subtractive & Pruning Engine Reference ("Marie Kondo Doctrine")

## 1. The Value of Subtraction

Product debt accumulates when agents and teams only add features. Every unnecessary line of code or complex setting adds:
- Cognitive load to the end user.
- Maintenance overhead and test runtime to the engineering team.
- Potential attack surface and bundle weight to the runtime environment.

The Subtractive Engine mandates that at least **20% of the active portfolio (March's 70/20/10 rule)** focuses on simplification, code deprecation, and feature removal.

---

## 2. Four Subtractive Initiative Families

### 1. Flow Streamlining
- **Symptom:** Multi-step wizards, excessive confirmation dialogs, or mandatory form fields that could be inferred.
- **Remedy:** Replace 4-step wizard with 1-click action backed by intelligent defaults and undo capabilities.

### 2. Feature & Flag Pruning
- **Symptom:** Obsolete feature flags, unreferenced routes, deprecated legacy API parameters, or orphan components.
- **Remedy:** Safely purge dead flags, verify that no consumer relies on deprecated routes, and delete dead source files.

### 3. Cognitive Noise Elimination
- **Symptom:** Cluttered screens with redundant primary buttons, competing color badges, low-contrast microcopy, or duplicative navigation items.
- **Remedy:** Enforce visual hierarchy (`aesthetic-science`), remove decorative fluff, and maximize discriminability between states.

### 4. Dependency & Code Diet
- **Symptom:** Heavy external npm/pip packages used for trivial functions (e.g. lodash, moment.js, heavy CSS frameworks).
- **Remedy:** Replace external packages with standard modern JavaScript/TypeScript or Python standard library primitives.

---

## 3. Reverse TDD & Deprecation Protocol

1. **Impact Check:** Search codebase for all references (`grep_search` / `find_by_name`).
2. **Update Assertions:** Update or remove obsolete test cases to reflect the simplified architecture.
3. **Execute Deletion:** Remove dead code, components, and CSS styles.
4. **Regression Run:** Run full test suite to guarantee 100% green status.
5. **Record Savings:** Document lines deleted, bundle bytes saved, and steps eliminated in `.product-loop/learnings.md`.
