#!/usr/bin/env bash
# Symlink all Software Maestro skills into Codex, Gemini, Antigravity, Claude, and universal runtime dirs

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIRS=(
  "${HOME}/.agents/skills"
  "${HOME}/.claude/skills"
  "${HOME}/.codex/skills"
  "${HOME}/.gemini/config/skills"
  "${HOME}/.gemini/skills"
)

# Ensure all target directories exist
for target_dir in "${TARGET_DIRS[@]}"; do
  mkdir -p "${target_dir}"
done

# Find and symlink every skill
find "${REPO_DIR}" -mindepth 2 -maxdepth 3 -name "SKILL.md" | while read -r skill_md; do
  skill_dir="$(dirname "${skill_md}")"
  skill_name="$(basename "${skill_dir}")"

  for target_dir in "${TARGET_DIRS[@]}"; do
    ln -sfn "${skill_dir}" "${target_dir}/${skill_name}"
  done
done

echo "✓ All Software Maestro skills successfully installed across Codex, Gemini, Claude, and universal runtime hubs!"
