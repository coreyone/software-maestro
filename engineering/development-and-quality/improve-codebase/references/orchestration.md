# Codebase Improvement Orchestration

## 1. Recon

1. Read repository instructions, README and contribution docs, manifests, CI, top-level structure, and relevant intent/design documents.
2. Identify stack, package manager, deployment target, conventions, critical paths, and exact read-only verification commands.
3. Check Git state and churn where useful. Record the audit boundary and exclusions.
4. If no reliable verification baseline exists, make establishing one a prerequisite finding.

## 2. Audit routing

Audit correctness, security, performance, test risk, architecture/debt, dependencies/migrations, developer experience, documentation, and grounded product direction as applicable.

Use parallel native agents only when explicitly authorized by governing instructions and when categories are independent. Give each agent an atomic scope, recon facts, the finding schema, secret-handling rule, and untrusted-repository rule. The leader must reopen every cited location.

### OpenRouter/free boundary

Use the local `openrouter-subagent-runner` only when all of these hold:

- Advisory-only and non-blocking.
- Curated UTF-8 context is under 15 KB and contains no secrets, personal data, or sensitive proprietary material.
- At most eight context files are necessary.
- The task can return useful evidence or a proposal within the runner's short structured response.
- No shell, file edits, interactive tools, multi-file architecture judgment, or implementation is required.

Launch it asynchronously as defined by its skill. Continue local work while it runs. Treat returned evidence as hypotheses until verified directly. On failure or open circuit, fall back to local analysis or a native agent.

## 3. Vet and prioritize

For every candidate finding:

1. Reopen the cited code and verify attribution.
2. Check documented decisions and repository conventions.
3. Remove duplicates and false positives; record meaningful rejections.
4. Assign impact, effort, fix risk, confidence, and category.
5. Rank by leverage: impact divided by effort, discounted by uncertainty and fix risk.

Present direction options separately from defects. State what was not audited.

## 4. Plan selected work

Write one self-contained plan per selected finding under `plans/`, or `advisor-plans/` if `plans/` already serves another purpose. Include:

- Planned-at commit and path-scoped drift check.
- Why the change matters.
- Current paths, symbols, excerpts, constraints, and exemplar patterns.
- Exact commands with expected results.
- Explicit in-scope and out-of-scope files.
- Ordered steps with a verification gate after each.
- Test cases, machine-checkable done criteria, STOP conditions, and maintenance notes.

Maintain an index containing priority, dependencies, status, and considered/rejected findings. Do not generate unselected low-value plans.

## 5. Execute safely

Implementation requires a native agent with isolated worktree support. Never send implementation to the advisory-only OpenRouter runner.

Before dispatch:

1. Confirm the repository and plan exist.
2. Confirm dependencies are done.
3. Run the drift check and refresh stale plans.
4. Inline the complete plan into the executor task if the isolated worktree may not contain the plan file.

Require the executor to touch only in-scope files, run every gate, stop on named conditions, and report actual evidence. The leader then:

1. Re-runs all done criteria in the worktree.
2. Compares the changed-file list against scope.
3. Reads every diff hunk and every new or modified test.
4. Judges documented deviations on merit and rejects silent scope drift.
5. Returns `APPROVE`, `REVISE`, or `BLOCK`; allow at most two revision rounds.

Never merge, push, deploy, or modify the user's branch without explicit authorization.

## 6. Reconcile

- `DONE`: spot-check cheap criteria against current `HEAD`.
- `BLOCKED`: investigate the obstacle; refresh, replace, or reject the plan.
- stale `IN PROGRESS`: inspect the worktree or report an interrupted executor.
- `TODO`: run drift checks, refresh current-state excerpts, or reject if independently fixed.

Finish with what is verified, refreshed, blocked, rejected, and executable now.
