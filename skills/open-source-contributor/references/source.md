# Open Source Contribution & Etiquette Reference Manual

A comprehensive reference for contributing to open source repositories with professional standards, constructive etiquette, and clean git history.

---

## 1. GitHub Open Source Guide Principles

From `opensource.guide`:

### 1.1 Understanding Maintainers
- Maintainers are often unpaid volunteers balancing project maintenance with full-time jobs.
- High-quality contributions reduce review fatigue.
- Incomplete bug reports and massive unsolicited PRs create maintenance burden.

### 1.2 Submitting an Issue
- Search existing issues before creating a new one.
- Provide a minimal, reproducible example (MRE).
- State expected behavior versus actual behavior. Include system information, versions, and full error logs.
- For new features, open a discussion or RFC before writing code.

### 1.3 Submitting a Pull Request
- Follow the repository `CONTRIBUTING.md` guidelines.
- Keep the change focused on a single concern.
- Include automated tests covering new paths.
- Update documentation and changelogs when relevant.

---

## 2. Google Engineering Practices (Review Etiquette & Small Changes)

From `google/eng-practices`:

### 2.1 Small Changes
- Ideal change size is under 200 lines of code.
- Small changes result in faster reviews, fewer merge conflicts, and lower defect rates.
- Split refactoring from functional changes. Never bundle formatting sweeps into bug fixes.

### 2.2 Writing Code Review Comments
- **Critique the code, never the person.**
  - Poor: "You missed this edge case."
  - Better: "This function can throw when input is empty. Adding a check avoids a crash."
- **Explain the rationale.** Cite documentation, specs, or potential failure modes.
- **Differentiate must-fix from suggestions.** Use `nit:` for optional personal preferences.
- **Collaborate on solutions.** Suggest concrete diffs or pseudocode.

### 2.3 Responding to Reviews
- Treat feedback as collaboration to improve code health.
- Avoid defensive responses.
- Explain trade-offs with data when disagreeing.
- Acknowledge every comment before requesting re-review.

---

## 3. Contributor Covenant Code of Conduct (v2.1)

From `EthicalSource/contributor_covenant`:

### 3.1 Positive Behaviors
- Demonstrating empathy and kindness toward other people.
- Being respectful of differing opinions, viewpoints, and experiences.
- Giving and gracefully accepting constructive feedback.
- Accepting responsibility and apologizing to those affected by our mistakes.
- Focusing on what is best for the overall community.

### 3.2 Unacceptable Behaviors
- Trolling, insulting or derogatory comments, and personal attacks.
- Public or private harassment.
- Publishing private information without explicit permission.
- Conduct reasonably considered inappropriate in a professional setting.

---

## 4. Conventional Commits 1.0.0 Specification

From `conventionalcommits.org`:

### 4.1 Schema
```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 4.2 Commit Types
- `feat`: adds a new feature (correlates with `MINOR` in Semantic Versioning).
- `fix`: patches a bug (correlates with `PATCH` in Semantic Versioning).
- `docs`: documentation changes only.
- `style`: changes that do not affect code meaning (white-space, formatting, missing semicolons).
- `refactor`: code change that neither fixes a bug nor adds a feature.
- `perf`: code change that improves performance.
- `test`: adding missing tests or correcting existing tests.
- `build`: changes that affect the build system or external dependencies.
- `ci`: changes to CI configuration files and scripts.
- `chore`: other changes that do not modify `src` or test files.
- `revert`: reverts a previous commit.

### 4.3 Breaking Changes
- Append `!` immediately before `:` in the prefix: `feat(api)!: remove legacy authentication`.
- Or add a footer starting with `BREAKING CHANGE: <explanation>`.

---

## 5. First Contributions Protocol (Fork & Branch Git Workflow)

From `firstcontributions/first-contributions`:

### 5.1 Remote Setup
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
git remote add upstream https://github.com/<original-owner>/<repo-name>.git
git remote -v
```

### 5.2 Branch Lifecycle
```bash
# Keep local main clean and updated
git checkout main
git fetch upstream
git merge upstream/main

# Create branch for your task
git checkout -b fix/resolve-parser-leak

# Commit changes
git add src/parser.c
git commit -m "fix(parser): free allocated memory on syntax error"

# Rebase on latest upstream before pushing
git fetch upstream
git rebase upstream/main

# Push to your fork
git push -u origin fix/resolve-parser-leak
```

### 5.3 Post-Review Iteration
```bash
# Make requested adjustments
git add src/parser.c
git commit --amend # or create a fixup commit
git push --force-with-lease origin fix/resolve-parser-leak
```
