---
name: platform-enablement-internal-leverage
description: "Trigger: Internal platform design, product platform primitives, developer platform enablement, internal leverage, reusable core primitives, platform multiplier effect. Scope: Designing internal platforms, self-serve primitives, shared capability SDKs, and compound multiplier systems that enable 1 platform squad to multiply the velocity of 10 stream-aligned squads. Boundary: Excludes low-level cloud Kubernetes infrastructure provisioning."
---

# Rule: Internal Platform Enablement & Leverage Architecture

## When to use

Use this skill when designing internal product/developer platforms, creating shared capabilities and reusable primitives, establishing internal platform SLAs, or measuring the multiplier impact of enablement teams.

## When not to use

Do not use this skill for raw Kubernetes cluster setup or basic infrastructure sysadmin tasks.

## Trigger cues

- Request explicitly references `platform-enablement-internal-leverage` or internal platform design.
- Keywords: platform enablement, internal primitives, platform multiplier, self-serve platform, stream-aligned squads, reusable capabilities, internal DX, platform product management.

## Routing boundary

- Primary for platform product strategy, internal API/SDK primitive design, and leverage measurement.
- Route CI/CD pipelines to `deployment-pipeline-design` and low-level system architecture to `system-architecture-rules`.

## Inputs required

- Target stream-aligned squad capabilities and duplicate workflows
- Proposed shared primitives (e.g., Auth, Billing, Telemetry SDK, Design System)
- Platform adoption metrics and internal developer friction points
- Source of truth: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. Identify **Duplicate Undifferentiated Work across Stream-Aligned Squads**:
   - Audit repeated implementations (e.g., 5 squads building custom CSV exporters, 3 squads writing custom webhook retry queues).
3. Design **Self-Serve Platform Primitives**:
   - Treat the Platform as a **Product**: APIs, SDKs, and CLIs with clear documentation, self-serve onboarding, and zero manual gatekeeping.
   - Design for **Thinnest Viable Platform (TVP)**: Build the absolute minimal shared primitive that solves 80% of downstream needs.
4. Establish **Platform SLA & Developer Experience (DX) Contracts**:
   - Define uptime, API version stability, and Time-to-First-Integration SLAs.
5. Measure the **Platform Leverage Multiplier**:
   $$	ext{Leverage Ratio} = rac{	ext{Hours Saved Across } N 	ext{ Stream Squads}}{	ext{Platform Squad Hours Invested}}$$

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Explicit identification of duplicate undifferentiated squad work.
- Self-serve primitive specification (API, SDK, or shared component).
- Quantifiable leverage multiplier metric (Time-to-delivery compression across stream squads).

## Output format

- **Platform Primitive Charter**: Reusable capability, target internal consumers, and API contract.
- **Thinnest Viable Platform (TVP) Design**: Core features vs out-of-scope custom logic.
- **Developer Experience (DX) Standards**: Self-serve documentation and integration SLAs.
- **Leverage Multiplier Scorecard**: Time-to-integrate reduction and cross-squad engineering hours saved.
