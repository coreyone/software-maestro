---
name: user-story-mapping
description: "Build user story maps, backbone user journeys, and slice release milestones."
---

# Rule: User Story Mapping & Incremental Release Slicing Framework

> [!IMPORTANT]
> **Foundational Methodologies & Upstream/Downstream Links**:
> 1. **Jeff Patton (*User Story Mapping*)**: 2-Dimensional Story Map (Horizontal narrative timeline vs. Vertical priority depth) and user-centric conversation modeling.
> 2. **Edo van Royen & Alistair Cockburn**: The **Walking Skeleton** (the thinnest possible end-to-end implementation across every step of the backbone).
> 3. [`/create-prd`](../../discovery-and-specs/create-prd/SKILL.md): Ingests high-level user personas, problem statements, and functional requirements.
> 4. [`/prd-to-tickets`](../../discovery-and-specs/prd-to-tickets/SKILL.md): Compiles horizontal release slices into tracer-bullet execution tickets with blocking DAG dependencies.
> 5. [`/god-marduk`](../../orchestration/god-marduk/SKILL.md): Sequences the resulting delivery across the 6-phase engineering lifecycle.
> 6. [`/scrum-planning-and-refinement`](../../../productivity-maestro/scrum-cadences/scrum-planning-and-refinement/SKILL.md): Calibrates team capacity and sprint goals against story map release slices.

---

## When to use

Use this skill when:
- Transforming a flat, unprioritized backlog into a coherent 2-dimensional user journey.
- Defining the narrative backbone and chronological user flow for a new product, major workflow, or feature redesign.
- Carving out an uncompromised **Walking Skeleton (MVP Release Slice 1)** that works end-to-end.
- Structuring subsequent release increments (Release 2: Core Enhancements / Release 3: Future & Edge Cases) without losing the holistic user experience.
- Facilitating cross-functional discovery workshops with engineering, design, and product to build shared understanding.
- Preventing horizontal architectural siloing (e.g., building 100% of the backend database without any usable user interface).

## When not to use

Do not use this skill for:
- Writing low-level unit test assertions or code diffs (use `developer-test-driven-development`).
- Generating granular engineering tickets with file-level bounding and BDD criteria (use `prd-to-tickets`).
- Conducting daily standup triage (use `scrum-daily-sync`).

## Trigger cues

- Request mentions: `user story mapping`, `story mapping`, `jeff patton`, `walking skeleton`, `user journey backbone`, `narrative backbone`, `release slicing`, `mvp slice`, `story map`, `edo van royen`, `user activities and tasks`.

## Routing boundary

- Primary for 2D story map structure, user journey backbone definition, and horizontal release slicing.
- Route PRD generation to `create-prd`.
- Route ticket decomposition with blocking DAGs to `prd-to-tickets`.
- Route sprint capacity planning to `scrum-planning-and-refinement`.

## Inputs required

1. **User Personas & Goals**: Primary user archetypes and what they are attempting to achieve.
2. **User Journey Context**: High-level workflow steps from initial entry to ultimate goal completion.
3. **Business & Release Constraints**: Target release milestones, market window, and technical baseline.
4. **Source of truth**: [references/source.md](references/source.md)

---

## Instructions

1. **Read [references/source.md](references/source.md) first**.
2. **Frame the User Journey & Personas**:
   - Identify the primary user persona and their core job-to-be-done.
   - Establish the boundary conditions (where the journey starts and where it successfully concludes).
3. **Build the Horizontal Backbone (User Activities)**:
   - Identify 4–7 high-level **User Activities** representing the chronological narrative flow from left to right (*e.g., Discover $\rightarrow$ Select $\rightarrow$ Configure $\rightarrow$ Checkout $\rightarrow$ Track*).
4. **Decompose into User Tasks (Steps)**:
   - Under each Activity, place specific **User Tasks** in sequence (the essential actions a user takes to complete that activity).
5. **Expand Vertically with Options, Details & Variations**:
   - Brainstorm variations, alternative paths, edge cases, and delighters under each User Task.
   - Place simpler/mandatory tasks near the top and advanced/optional variations lower down.
6. **Carve Horizontal Release Slices**:
   - **Slice 1: Walking Skeleton (MVP)**: The absolute thinnest, simplest end-to-end slice spanning across *every single activity* on the backbone. A user can complete the entire journey from start to finish.
   - **Slice 2: Core Enhancements / Delighters**: Adds efficiency, better ergonomics, primary alternative paths, and automated conveniences.
   - **Slice 3: Advanced & Edge Variations**: Handles edge cases, internationalization, power-user shortcuts, batch operations, and administrative controls.
7. **Walk the Map for Flow & Continuity**:
   - Validate that each release slice forms a complete, unbroken narrative from left to right.
   - Ensure no "orphaned" steps or broken transitions exist in Slice 1.
8. **Bridge to Execution Backlog**:
   - Feed sliced stories into `prd-to-tickets` for tracer-bullet ticket compilation and God-Marduk phasing.

---

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- [ ] Complete horizontal Backbone with chronological User Activities (left-to-right).
- [ ] User Tasks mapped under each activity with vertical depth.
- [ ] Explicit **Walking Skeleton (Slice 1 / MVP)** that touches every backbone activity end-to-end.
- [ ] Clearly demarcated Release Slices (Slice 1, Slice 2, Slice 3) with defined user outcomes.
- [ ] Elimination of horizontal component silos (every slice delivers end-to-end user value).

---

## Output format

- **User Personas & Scope**: Target user, primary goal, and boundary triggers.
- **Narrative Backbone**: Sequence of high-level User Activities (Left $\rightarrow$ Right).
- **2D Story Map Matrix**: Tabular representation showing Activities, User Tasks, and Vertical Depth.
- **Release Slice Definitions**:
  - *Slice 1: Walking Skeleton (MVP)*
  - *Slice 2: Next Release / Enhancements*
  - *Slice 3: Future / Edge Variations*
- **Continuity Walkthrough**: Verification of end-to-end user experience across each slice.
