# User Onboarding & First-Time User Experience (FTUX) Master Reference
_Source spine: Nielsen Norman Group (NN/g), O'Reilly Media, MIT Press, The Pragmatic Bookshelf, and Behavioral Usability Research._

---

## 0) North Star & Fundamental Equations

### First-Principles (Why)
- **The Fire Flower Principle** (*Samuel Hulick / UserOnboard*): Users do not want to become experts at your tool; they want to become better at their own superpowers. Mario does not care about the fire flower itself; he cares about throwing fireballs and rescuing the princess.
- **Minimum Viable Instruction (MVI)** (*Kathy Sierra / O'Reilly*): Cognitive resources, willpower, and working memory degrade rapidly during initial encounters with new software. Every unnecessary explanation or non-essential field depletes the user's ability to reach their goal.
- **Behavior Equation** (*Dr. BJ Fogg / Stanford*):
  $$B = MAP \quad (\text{Behavior} = \text{Motivation} \times \text{Ability} \times \text{Prompt})$$
  Because user motivation is volatile and naturally decays after landing, onboarding must **radically maximize Ability** by driving friction toward zero.

### The System Equation
$$\text{Activation Rate} = \frac{\text{Perceived Value} + \text{Momentum} + \text{Immediate Feedback}}{\text{Time-to-Value (TTV)} + \text{Cognitive Load} + \text{Setup Friction} + \text{Uncertainty}}$$

---

## 1) Nielsen Norman Group (NN/g) Usability Findings

### A. The Anti-Pattern of Frontloaded Instruction Manuals
- **Usability Finding**: Users overwhelmingly swipe through or dismiss initial modal carousels and multi-step tooltip tours without reading.
- **Root Cause**: Humans cannot store 4–6 abstract interface steps in working memory before using the software. Information presented out of context is immediately discarded.
- **Rule**: Never greet a first-time user with a 5-step modal carousel explaining UI geography.

### B. Contextual "Learn by Doing" (Just-in-Time Guidance)
- **Usability Finding**: Guidance is effective only when attached to the user's immediate intent.
- **Rule**: Present prompts, hints, and inline microcopy strictly when the user focuses on or triggers the relevant action.
- **Limit**: Maximum 1 contextual callout visible at any given time. Never stack tooltips.

### C. Empty States as Primary Onboarding Catalysts
- **Usability Finding**: Blank screens ("No projects created yet") produce choice paralysis and abandonment.
- **Rule**: Replace empty views with:
  1. **Pre-populated sample data / templates** (showing what a finished state looks like).
  2. **A single, high-contrast primary CTA** with outcome-oriented copy (e.g., "Create Your First Invoice").
  3. **Embedded sandbox mode** where users can safely experiment without breaking production data.

### D. Delayed & Lazy Registration
- **Usability Finding**: Forcing registration or credit cards before demonstrating value causes up to 80% abandonment.
- **Rule**: Allow users to experience the core mechanism (e.g., customize a design, calculate a metric, draft a document) before asking for account creation to save state.

### E. User Autonomy & Exit Freedom
- **Usability Finding**: Trapping users in non-skippable onboarding flows induces acute frustration and app uninstalls.
- **Rule**: Every walkthrough, prompt, or wizard must provide an immediate, obvious "Skip" or "Dismiss" action. Maintain a persistent "Getting Started" drawer or checklist so users can voluntarily resume setup later.

---

## 2) O'Reilly Media Principles (Applied UX & Behavior Design)

### Kathy Sierra (*Badass: Making Users Awesome*)
- **Post-Heroic Design**: The product is not the hero; the user is the hero. Remove all self-congratulatory marketing copy from onboarding screens.
- **Compilations of Skills**: Scaffold complex applications by breaking them into automatic micro-skills. Let the user master step 1 before exposing step 2.

### Stephen Wendel (*Designing for Behavior Change*) — The CREATE Framework
- **Cue**: Provide an intuitive, unambiguous prompt to start.
- **Reaction**: Ensure the user has an immediate, visceral understanding of what to do next.
- **Evaluation**: Minimize the perceived effort and cost of the action.
- **Ability**: Ensure the user possesses all necessary information (or provide sensible defaults).
- **Timing**: Deliver the prompt at the exact moment the user is ready.
- **Execution**: Eliminate technical, visual, and validation blockers.

### Jenifer Tidwell, Charles Brewer, Aynne Valencia (*Designing Interfaces*)
- **Progressive Disclosure**: Defer advanced tools, secondary configuration, and granular settings until the basic workflow is completed.
- **Inline Hints & Discovery Badges**: Use subtle visual pulses or discoverable badges rather than jarring modal popups.

### Theresa Neil (*Mobile Design Pattern Gallery*)
- Mobile users have fragmented attention and physical thumb-zone constraints.
- Replace full-screen walkthroughs with **Interactive Guided Tasks** where the UI guides the user through completing an authentic task.

---

## 3) MIT Press Foundations (Cognitive Science, HCI & Game Design)

### Katie Salen & Eric Zimmerman (*Rules of Play*) — The "Invisible Tutorial"
- **Level 1 Design**: Super Mario World 1-1 teaches jumping, dodging, and collecting mushrooms without a single word of tutorial text.
- **Sandboxed Failure**: Create safe boundaries where first-time mistakes have zero destructive consequences (e.g., auto-saving drafts, non-destructive sample workspaces).

### Seymour Papert & Mitchel Resnick (*Mindstorms* / Constructionism)
- **Low Floor, High Ceiling, Wide Walls**:
  - *Low Floor*: Getting started takes < 60 seconds with zero prerequisites.
  - *High Ceiling*: Advanced power users can scale to maximum complexity over time.
  - *Wide Walls*: Multiple entry pathways cater to different user mental models.

### Don Norman (*The Design of Everyday Things*)
- If an interface requires an explicit tooltip saying "Click here to add an item," the **signifier and affordance** of that button have failed. Design affordances that communicate their function visually.

### Jesper Juul (*The Art of Failure*) — Competence Scaffolding
- Users experience dopamine and sustained engagement when early micro-actions result in immediate positive feedback.

---

## 4) The Pragmatic Bookshelf (Developer & Technical Product Onboarding)

### Zero-to-Hello-World in Under 5 Minutes
- In developer tooling, SDKs, CLIs, and APIs, every additional terminal command, credential generation step, or config file syntax error doubles drop-off.
- **Requirements for DX Onboarding**:
  1. Single-command initialization (`npx create-...` or `brew install ...`).
  2. Pre-configured sensible defaults (zero mandatory config editing to run).
  3. Interactive, runnable sandbox or local dev server opening instantly in the browser.
  4. Actionable error messages that include the exact copy-pasteable fix command.

---

## 5) ProductLed: The Bowling Alley Framework (*Wes Bush*)

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE BOWLING ALLEY FRAMEWORK                     │
│                                                                        │
│  [LEFT BUMPER: Product Bumpers]                                        │
│  • Empty State Templates • Interactive Checklists • Progress Bars     │
│  • Contextual Tooltips   • In-App Welcome Banner                       │
│                                                                        │
│   ════════════════════════════════════════════════════════════════►   │
│   [STRAIGHT-LINE ONBOARDING]: Shortest Path to First Value (Aha!)      │
│   ════════════════════════════════════════════════════════════════►   │
│                                                                        │
│  [RIGHT BUMPER: Conversational Bumpers]                                │
│  • Re-engagement Push    • Behavioral Email Triggers                   │
│  • SMS Verification Link • Smart Desktop Notifications                 │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Straight-Line Onboarding**: The absolute bare-minimum sequence of steps required to deliver initial value. Every non-essential screen, dropdown, and verification modal is pruned.
2. **Product Bumpers**: In-app UI mechanisms that prevent the user from getting lost or confused within the software.
3. **Conversational Bumpers**: Out-of-app automated triggers that recover abandoned sessions based on user behavior (e.g., "Your draft is saved — click here to publish with 1 click").

---

## 6) The 3-Tier Progressive Onboarding Matrix

| Level | Pattern | When to Use | Behavioral Mechanism |
| :--- | :--- | :--- | :--- |
| **Tier 1: Passive** | Empty States & Default Data | Initial screen landing | Eliminates the blank canvas; demonstrates finished product state. |
| **Tier 2: Interactive** | Action Checklists & Steppers | Multi-step setup workflows | Leverages the **Zeigarnik Effect** (give credit for step 1 completed automatically upon signup). |
| **Tier 3: Contextual** | Just-in-Time Badges & Hints | Feature discovery during flow | Delivers cognitive support at the exact point of need without interrupting workflow. |

---

## 7) Tactical Onboarding Checklist

### First 10 Seconds (Orientation & Low Floor)
- [ ] User lands immediately on the workspace or active creation canvas.
- [ ] No blocking multi-screen welcome carousels or unskippable overlays.
- [ ] Clear signifiers and visual affordances eliminate the need for explanatory text.

### First 60 Seconds (Time-to-Value & Aha! Moment)
- [ ] User completes their first meaningful action (creates a doc, runs a query, customizes a card).
- [ ] Intelligent defaults pre-select standard configurations (no unnecessary form inputs).
- [ ] Immediate positive visual feedback confirms task completion.

### First Session Retention (Scaffolding & Recovery)
- [ ] Persistent "Getting Started" checklist tracks progress (e.g., 2 of 4 steps complete).
- [ ] Progress is automatically saved to prevent data loss on tab close or navigation.
- [ ] If user dismisses guidance, an entry point remains easily accessible in the sidebar or profile.

---

## 8) Do Not Ship List (Anti-Patterns)

- **Do Not Ship** forced multi-slide modal carousels ("Welcome to version 2.0! Slide 1 of 5").
- **Do Not Ship** compulsory upfront profile questionnaires before demonstrating any product value.
- **Do Not Ship** empty states that display only raw whitespace or unhelpful text like "Nothing here yet."
- **Do Not Ship** unskippable walkthroughs or modal traps without an immediate `Esc` / `Skip` / `Dismiss` action.
- **Do Not Ship** destructive reset behavior that wipes user-entered data if they exit the onboarding flow.
- **Do Not Ship** generic tooltips that state the obvious (e.g., a tooltip on a Search icon saying "Click here to search").
- **Do Not Ship** developer onboarding that requires more than 3 terminal commands to run a local "Hello World."
