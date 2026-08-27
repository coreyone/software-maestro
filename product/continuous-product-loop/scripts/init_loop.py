#!/usr/bin/env python3
"""
Autonomous Continuous Product Evolution Loop Bootstrapper
Initializes .product-loop/ state, roadmap, strategy, and compound learning repository.
"""

import argparse
import datetime
import json
import os
import sys
from pathlib import Path

def init_product_loop(root_dir: str, mode: str, hours: float, cycles: int, vision: str, intent: str):
    base_path = Path(root_dir).resolve()
    loop_dir = base_path / ".product-loop"
    history_dir = loop_dir / "history"
    docs_dir = base_path / "docs" / "solutions"
    patterns_dir = docs_dir / "patterns"

    # Create directories
    for directory in [loop_dir, history_dir, docs_dir, patterns_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # 1. State JSON
    state_file = loop_dir / "state.json"
    if not state_file.exists():
        state_data = {
            "version": "1.5.0",
            "cycle_count": 0,
            "execution_mode": mode.upper(),
            "max_duration_hours": hours,
            "max_cycles": cycles,
            "start_time": now_iso,
            "status": "RUNNING",
            "current_phase": "PHASE_0_STRATEGY_SYNC",
            "active_intent_id": "INTENT-01",
            "active_initiative_id": "INIT-001",
            "active_initiative_type": "EXPLOIT",
            "active_marduk_stage": "STAGE_0_SCAFFOLDING",
            "active_prd_path": "",
            "active_branch": "main",
            "last_health_check": now_iso,
            "portfolio_distribution": {
                "exploit_count": 0,
                "improve_count": 0,
                "explore_count": 0
            },
            "subtractive_metrics": {
                "lines_of_code_pruned": 0,
                "redundant_components_deleted": 0,
                "user_steps_eliminated": 0
            },
            "learning_metrics": {
                "total_rules_codified": 0,
                "solutions_documented": 0,
                "critical_patterns_active": 0,
                "skills_minted": 0,
                "zero_repeat_violations_streak": 0
            }
        }
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2)
        print(f"✓ Created {state_file}")

    # 2. Strategy MD
    strategy_file = loop_dir / "strategy.md"
    if not strategy_file.exists():
        strategy_content = f"""# Product Strategy Memo

## Strategy Sentence
We will help users achieve their core workflow goals by removing initial configuration friction, because it drives activation and retention, and we will prove it through successful first-session completion rates.

## Vision
{vision or "Effortless, intelligent product experience providing immediate customer value."}

## Strategic Intents
1. **INTENT-01:** {intent or "Streamline primary user activation and eliminate onboarding friction."}
2. **INTENT-02:** Establish bulletproof reliability, performance, and responsive feedback.

## What We Will Not Do
- We will not add speculative features before primary activation is verified.
- We will not build complex customization before sensible defaults prove sufficient.
"""
        with open(strategy_file, "w", encoding="utf-8") as f:
            f.write(strategy_content)
        print(f"✓ Created {strategy_file}")

    # 3. Roadmap MD
    roadmap_file = loop_dir / "roadmap.md"
    if not roadmap_file.exists():
        roadmap_content = """# Outcome-Driven Product Roadmap (Now-Next-Later)

## NOW (Active Focus - 1 to 2 items max)
- [ ] **INIT-001 [EXPLOIT]:** Core Workflow Foundation & Baseline Verification
  - *Target Condition:* 100% clean test suite & environment baseline.
  - *Obstacle:* Initial setup & schema verification.

## NEXT (Validated Opportunities)
- [ ] **INIT-002 [IMPROVE - Subtractive]:** Audit & Streamline Initial User Path
  - *Target Condition:* Reduce setup click-steps by 50%.
- [ ] **INIT-003 [EXPLOIT]:** High-Reliability Core Action Engine
  - *Target Condition:* Median execution latency < 200ms.

## LATER (Discovery & Exploration)
- [ ] **INIT-004 [EXPLORE]:** Autonomous Predictive Workflow Spikes
"""
        with open(roadmap_file, "w", encoding="utf-8") as f:
            f.write(roadmap_content)
        print(f"✓ Created {roadmap_file}")

    # 4. Rules MD (Ralph Loop)
    rules_file = loop_dir / "rules.md"
    if not rules_file.exists():
        rules_content = """# Ralph Loop Codified Rules Engine

> **Doctrine:** Failures Are Data | Iteration > Perfection | Zero Repeated Mistakes

- **Rule 1:** Always verify low-level primitives (schemas/auth) before building high-level UI components (God-Marduk).
- **Rule 2:** Functional code changes must strictly follow TDD: Red failing test precedes Green implementation.
- **Rule 3:** Never commit changes without running the full test suite and checking for regressions.
"""
        with open(rules_file, "w", encoding="utf-8") as f:
            f.write(rules_content)
        print(f"✓ Created {rules_file}")

    # 5. Baton MD
    baton_file = loop_dir / "baton.md"
    if not baton_file.exists():
        baton_content = f"""---
cycle: 1
phase: PHASE_0_STRATEGY_SYNC
intent: "INTENT-01: {intent or 'Streamline user activation'}"
initiative: "INIT-001: Core Workflow Foundation"
timestamp: "{now_iso}"
---

# Active Iteration Baton (Cycle 1)

## 1. Context & Objective
- **Strategic Intent:** Establish foundational baseline and verify clean environment.
- **Target Condition:** Verified build, green tests, and validated strategy sentence.

## 2. Immediate Task
Check environment and database primitives. Execute God-Marduk Stage 0-1.

## 3. Exit Criteria
- Strategy and Roadmap aligned.
- TDD test suite verified.
- Proceed to Phase 1 Discovery / Phase 4 Foundation.
"""
        with open(baton_file, "w", encoding="utf-8") as f:
            f.write(baton_content)
        print(f"✓ Created {baton_file}")

    # 6. Critical Patterns (Required Reading)
    crit_patterns_file = patterns_dir / "critical-patterns.md"
    if not crit_patterns_file.exists():
        crit_content = """# Critical Patterns & Required Reading

> **Mandatory:** This file is loaded at Phase 0 of every cycle. Follow all patterns strictly.

## Pattern 1: Dependency Hierarchy (Zero Floating Abstractions)
- ❌ **WRONG:** Creating UI dialogs or buttons before database schemas and backend engines exist.
- ✅ **CORRECT:** Define data models in Foundation (Stage 1), build engine logic in Mechanism via TDD (Stage 2), then wire UI in Interface (Stage 3).

## Pattern 2: Subtractive Restraint
- ❌ **WRONG:** Adding new nested settings menus whenever a feature requirement expands.
- ✅ **CORRECT:** Provide sensible default behavior; prune obsolete config toggles.
"""
        with open(crit_patterns_file, "w", encoding="utf-8") as f:
            f.write(crit_content)
        print(f"✓ Created {crit_patterns_file}")

    print("\n✅ Continuous Product Loop initialized successfully.")
    print(f"Directory: {loop_dir}")
    print(f"Envelope: {hours}h max duration | {cycles} max cycles | Mode: {mode.upper()}")

def main():
    parser = argparse.ArgumentParser(description="Initialize Continuous Product Evolution Loop")
    parser.add_argument("--root-dir", default=".", help="Target workspace root directory")
    parser.add_argument("--mode", default="sprint", choices=["sprint", "overnight", "marathon"], help="Execution mode")
    parser.add_argument("--hours", type=float, default=3.0, help="Max duration hours envelope")
    parser.add_argument("--cycles", type=int, default=10, help="Max cycles envelope")
    parser.add_argument("--vision", default="", help="North Star product vision")
    parser.add_argument("--intent", default="", help="Primary strategic intent")
    args = parser.parse_args()

    if args.mode == "overnight" and args.hours == 3.0:
        args.hours = 12.0
        args.cycles = 25
    elif args.mode == "marathon" and args.hours == 3.0:
        args.hours = 72.0
        args.cycles = 100

    init_product_loop(args.root_dir, args.mode, args.hours, args.cycles, args.vision, args.intent)

if __name__ == "__main__":
    main()
