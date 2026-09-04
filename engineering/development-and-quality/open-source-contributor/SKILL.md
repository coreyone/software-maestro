---
name: open-source-contributor
description: "Prepare and execute open source contributions with rigorous etiquette across pull requests, issue comments, code reviews, and git commits. Trigger: open source contribution, OSS PR, GitHub issue triage, Conventional Commits, code review feedback, Contributor Covenant conduct, upstream git sync. Scope: PR descriptions, commit messages, review critiques, dispute resolution, patch slicing. Boundary: Excludes internal proprietary repos with custom commit schemas or private company HR policies."
---

# Open Source Contributor: Standards, Commits & Etiquette

Follow this protocol when contributing to external and open source projects. Keep changes small, communicate with empathy and facts, and format commits with strict conventional standards.

## When to use

Use this skill when:
- Authoring pull requests or issue comments on public or shared repositories.
- Conducting or responding to code reviews in open source communities.
- Formatting commit messages using Conventional Commits.
- Syncing upstream forks, rebasing feature branches, or preparing patch sets.
- Handling contributor disagreements or enforcing Contributor Covenant standards.

## When not to use

Do not use this skill as primary guidance when:
- Working in private repos that require alternative commit conventions or ticket tooling.
- Conducting internal personnel performance reviews or workplace HR escalations.

## Trigger cues

- Explicit references: `open source`, `OSS`, `contribute to repo`, `Conventional Commits`, `Contributor Covenant`, `code review etiquette`.
- Actions: drafting PR summaries, commenting on issues, formatting commit histories, reviewing outside code.

---

## 1. Core Operating Principles

1. **Maintainer Empathy First**: Maintainers work on limited time. Do not demand immediate reviews. Make review effortless through concise descriptions and test evidence.
2. **Small Changes Beat Monolithic Diffs**: Cap PR diffs at <= 200 lines of functional change whenever possible. Split large refactors and feature code into separate PRs.
3. **Egoless Critique**: Critique the code, never the author. Praise good patterns. Frame suggestions around shared system goals.
4. **Technical Facts Over Preference**: Support feedback with specs, test runs, or benchmarks. If a style preference has no lint rule or team agreement, mark it nit: and do not block.
5. **No Entitlement**: Maintainers can reject PRs that do not fit project scope. Accept decisions gracefully and move forward.

---

## 2. Conventional Commits 1.0.0 Specification

Format all commit messages and PR titles with strict conventional syntax:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Allowed Types

- `feat`: Adds a new user-facing feature.
- `fix`: Patches a bug for the user.
- `docs`: Documentation changes only.
- `style`: Formatting, whitespace, or punctuation changes that do not alter code logic.
- `refactor`: Code changes that neither fix bugs nor add features.
- `perf`: Code changes that improve runtime performance.
- `test`: Adds missing tests or corrects existing tests.
- `build`: Changes affecting build system or external dependencies.
- `ci`: Changes to CI configuration files or deployment scripts.
- `chore`: Maintenance tasks, tooling updates, or repo hygiene.
- `revert`: Reverts a previous commit.

### Structural Rules

- Use the imperative present tense: `add`, not `added` or `adds`.
- Do not capitalize the first letter of `<description>`.
- Do not place a period `.` at the end of `<description>`.
- Keep the title line <= 72 characters.
- Indicate breaking changes with `!` before the colon (e.g. `feat(api)!: drop v1 auth endpoints`) or with a `BREAKING CHANGE:` footer.

---

## 3. Code Review & Etiquette Standards

Apply Google Engineering Practices and Contributor Covenant conduct across every comment:

### Author Directives
- **Describe the Problem and Fix**: State what broke, why it broke, and how the patch fixes it.
- **Link Issues**: Connect related issues using GitHub keywords (`Fixes #123`, `Closes #456`).
- **Provide Verification Proof**: Paste passing test commands, reproduction scripts, or UI before/after screenshots.
- **Respond to Every Comment**: Address every reviewer comment with action or technical explanation. Mark resolved threads after applying fixes.

### Reviewer Directives
- **Grade Priority Explicitly**:
  - `[BLOCKING]`: Correctness bugs, security holes, missing test coverage, breaking regressions.
  - `[QUESTION]`: Inquiring about design tradeoffs without blocking.
  - `[NIT]`: Non-blocking style choices or minor simplifications.
- **Use Direct, Neutral Phrasing**:
  - Bad: *"You forgot to handle null here."*
  - Good: *"Handling null here prevents a panic when the user record is empty."*
  - Bad: *"Why did you write this terrible loop?"*
  - Good: *"Can we replace this nested loop with a map lookup to avoid an O(n^2) bottleneck?"*

### Community Conduct (Contributor Covenant 2.1)
- Welcome new contributors with patience and clarity.
- Do not use condescending language, gatekeeping, sexualized remarks, or personal insults.
- Focus discussions purely on technical facts and shared project goals.

---

## 4. Fork & Branch Git Workflow

Follow the First Contributions protocol for git hygiene:

1. **Fork and Clone**:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   git remote add upstream https://github.com/<upstream-owner>/<repo-name>.git
   ```

2. **Sync Before Branching**:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

3. **Isolate Work on Topic Branches**:
   ```bash
   git checkout -b feat/add-rate-limiter
   ```

4. **Rebase Before Submission**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

---

## 5. Voice & Anti-Slop Enforcement

When writing PRs, issue descriptions, commit messages, and review notes:
- Use active voice with human subjects.
- Keep sentences <= 20 words for instructions and <= 25 words for descriptions.
- Ban buzzwords: delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, transformative.
- Drop filler adverbs: literally, actually, fundamentally, crucially.
- Show concrete file lines, error messages, and reproducible commands. End on the next step.

---

## 6. Completion Checklist

Before submitting any open source contribution, confirm:
- [ ] PR description states problem, fix mechanism, and links related issue.
- [ ] Commits follow Conventional Commits formatting.
- [ ] Automated tests pass with evidence provided.
- [ ] Branch is rebased cleanly on latest upstream/main.
- [ ] Review comments critique code and logic rather than authors.
- [ ] Non-blocking items are labeled nit: without holding up approval.
