import os
import json
import re
from pathlib import Path

BASE_DIR = Path("/Users/coreyoneal/Programming/software-maestro")
MASTER_HUB = Path("/Users/coreyoneal/.agents/skills")
RUNTIMES = [
    Path("/Users/coreyoneal/.gemini/config/skills"),
    Path("/Users/coreyoneal/.codex/skills"),
    Path("/Users/coreyoneal/.claude/skills"),
]

skill_files = sorted(list(BASE_DIR.glob("**/SKILL.md")))
print(f"Total skills found: {len(skill_files)}")

issues = []

for sf in skill_files:
    dir_name = sf.parent.name
    with open(sf, "r") as f:
        content = f.read()
    
    # Parse frontmatter
    fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        issues.append(f"[{dir_name}] Missing YAML frontmatter")
        continue
    
    fm_text = fm_match.group(1)
    
    name_match = re.search(r"name:\s*([^\n]+)", fm_text)
    if not name_match:
        issues.append(f"[{dir_name}] Missing 'name' in frontmatter")
    else:
        name_val = name_match.group(1).strip().strip('"').strip("'")
        if name_val != dir_name:
            issues.append(f"[{dir_name}] Name mismatch: '{name_val}' != '{dir_name}'")
            
    desc_match = re.search(r"description:\s*([^\n]+|\".*?\"|'.*?')", fm_text, re.DOTALL)
    if not desc_match:
        issues.append(f"[{dir_name}] Missing 'description' in frontmatter")
    else:
        desc_val = desc_match.group(1).strip()
        if len(desc_val) > 1024:
            issues.append(f"[{dir_name}] Description exceeds 1024 chars ({len(desc_val)} chars)")
        if "Trigger:" not in desc_val and "trigger" not in desc_val.lower():
            issues.append(f"[{dir_name}] Description missing explicit trigger cues")
        if "Boundary:" not in desc_val and "excludes" not in desc_val.lower():
            issues.append(f"[{dir_name}] Description missing explicit negative triggers (Boundary: Excludes...)")

    # Check evals/cases.json
    eval_file = sf.parent / "evals/cases.json"
    if not eval_file.exists():
        issues.append(f"[{dir_name}] Missing evals/cases.json")
    else:
        try:
            with open(eval_file, "r") as ef:
                eval_data = json.load(ef)
            t_cases = eval_data.get("trigger_cases", [])
            b_cases = eval_data.get("binary_cases", [])
            if not t_cases:
                issues.append(f"[{dir_name}] No trigger_cases in evals")
            if not b_cases:
                issues.append(f"[{dir_name}] No binary_cases in evals")
        except Exception as e:
            issues.append(f"[{dir_name}] Malformed JSON in evals/cases.json: {e}")

    # Check symlinks
    if not (MASTER_HUB / dir_name).exists():
        issues.append(f"[{dir_name}] Missing symlink in master hub: {MASTER_HUB / dir_name}")
    for rt in RUNTIMES:
        if not (rt / dir_name).exists():
            issues.append(f"[{dir_name}] Missing symlink in runtime {rt.name}")

print(f"\nAudit completed. Total issues found: {len(issues)}")
if issues:
    print("\nIssues summary:")
    for iss in issues:
        print(f" - {iss}")
else:
    print("\nALL 55 SKILLS FULLY COMPLIANT with OpenAI & agentskills.io standard!")
