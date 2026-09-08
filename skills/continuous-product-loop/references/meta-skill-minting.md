# Meta-Skill Extraction & Autonomous Capability Synthesis Reference

## 1. Core Principle

The continuous product loop is self-expanding: when it discovers non-obvious engineering solutions, project-specific conventions, or optimized workflows, it extracts and compiles new permanent agent skills (`SKILL.md`).

---

## 2. Skill Extraction Filter (Selectivity Gate)

A skill is minted ONLY if it satisfies all 4 criteria:

1. **Reusable:** Will directly assist ≥ 3 future product cycles or other projects.
2. **Non-Trivial:** Required deep discovery, experimentation, or debugging; not just looking up basic docs.
3. **Specific:** Contains exact trigger cues, symptom regex, and concrete code diffs.
4. **Verified:** The solution has been verified with passing automated test evidence.

---

## 3. The 5-Step Skill Extraction Pipeline

```text
[Identify Discovery] ──► [Ground & Verify] ──► [Structure SKILL.md] ──► [Targeted Cues] ──► [Register]
```

### Step 1: Identify the Discovery
- Extract the core problem, symptoms, and generalized mechanism.

### Step 2: Ground & Verify (2025/2026 Web/Docs)
- Run targeted web or documentation searches to verify compatibility with current ecosystem standards and official documentation.

### Step 3: Structure SKILL.md
Follow standard Agent Skills schema:
```markdown
---
name: [skill-name]
description: [Short, high-density description with trigger cues]
license: MIT
metadata:
  version: "1.0.0"
  author: "Continuous Product Loop"
  category: "engineering"
---

# [Skill Title]

## Purpose
[Compact explanation of the problem solved]

## Trigger Cues & When to Use
[Exact symptoms, error messages, and context markers]

## Verified Solution
[Before/after code diffs and explanation]

## Verification
[Commands to test and prove completion]
```

### Step 4: Write High-Density Trigger Cues
- Ensure the description contains explicit action phrases ("Use when...", "Solves...") and exact technical terms.

### Step 5: Save & Register
- Save to `.agents/skills/[skill-name]/SKILL.md` (project-level) or `~/.gemini/config/skills/[skill-name]/SKILL.md` (global).
