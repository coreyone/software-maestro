---
name: chart-communication
description: "Use when a task requires designing, choosing, critiquing, implementing, or explaining a chart, graph, plot, dashboard, KPI visualization, data story, or quantitative presentation; reviewing axes, scales, labels, color, accessibility, uncertainty, or chart integrity; turning CSV, JSON, spreadsheet, database, or table data into visual evidence; or selecting a web-chart implementation. Trigger even when the user says visualize this, show the trend, compare metrics, make a dashboard, or make the data clearer without naming a chart. Do not use for generic UI styling, spreadsheet formula cleanup, database or ETL work, or decorative illustrations without quantitative data."
---

# Chart Communication

Make quantitative evidence easy to compare, difficult to misunderstand, and useful for a specific audience and decision.

## Operating contract

Choose an operating mode before acting:

- **Explore** — discover patterns; preserve alternatives, distributions, missingness, outliers, and uncertainty.
- **Explain** — communicate one supported takeaway; use a message title and direct attention to the evidence.
- **Monitor** — support a recurring operational decision; keep layout and scales stable and highlight exceptions.
- **Audit** — critique an existing visual; prioritize integrity and misinterpretation risk over taste.

Start with a chart brief:

```text
Audience:
Decision or use:
Question:
Primary analytical task:
Intended takeaway:
Evidence and source:
Relevant comparison:
Delivery context:
Constraints:
```

Ask for clarification only when the missing answer could materially change the analysis or chart choice. Otherwise state the assumption and proceed.

## Workflow

### 1. Inspect the evidence before designing

Trace every plotted value to its source. Verify the metric definition, unit, denominator, date range and timezone, population or sample, filters and exclusions, missing values, duplicates, zero and negative values, aggregation, category completeness, actual versus estimate versus forecast, and material uncertainty or sample size.

Expose source, extraction date, methodology, exclusions, and caveats when they affect interpretation. Never silently convert counts to rates, nominal to real values, fiscal to calendar periods, cumulative to period values, means to medians, or percentage change to percentage-point change.

Do not invent, interpolate, silently repair, hide inconvenient periods, imply causation from correlation, or choose a scale because it makes a result look stronger.

### 2. Choose the comparison, then the form

Use the simplest form that makes the intended comparison easiest:

| Analytical task | Default form | Important guardrail |
|---|---|---|
| Exact lookup | Table | Put units in headers; right-align numbers; use consistent precision. |
| Single KPI | Prominent value plus delta and benchmark | Do not use a gauge when text communicates it better. |
| Category comparison or ranking | Sorted horizontal bars or dot plot | Use natural order for processes, scales, or geographic sequence. |
| Change over time | Line chart | Keep chronological, even intervals; mark gaps and partial periods. |
| Discrete period totals | Columns | Use only when discrete magnitude is the point. |
| Before/after change | Dumbbell, connected dots, or slopegraph | Connect the same entities across periods. |
| Actual versus target | Bullet, dot with reference line, or target marker | Keep the target distinct but subordinate to the actual. |
| Distribution | Histogram, strip plot, dot plot, or box plot | Do not reduce a meaningful distribution to an average. |
| Relationship | Scatterplot | State correlation without claiming causation; show outliers and sample size when material. |
| Composition | Stacked bar, 100% stacked bar, or small multiples | Use pie/donut only for one whole, few slices, and approximate shares. |
| Deviation | Diverging/variance bar, difference line, control chart, or residual plot | Make zero, target, or baseline explicit. |
| Geography | Map only when location or spatial pattern matters | Use ranked bars when precise regional comparison is the real task. |
| Flow | Sankey or flow diagram | Use only when movement between states is the subject. |
| Uncertainty | Interval, range, error bar, fan/scenario band, or distribution | Do not let a central estimate erase uncertainty. |

Choose one default chart and at most one alternative when it supports a genuinely different task. A sentence or table is preferable when a chart adds no useful comparison.

### 3. Encode and compose

- Prefer position on a shared scale, then aligned position, length, direction/slope, angle, area, volume, and color intensity/hue. Do not use area, volume, perspective, or decorative shape for an important exact comparison when position or length works.
- Start quantitative bar axes at zero. A line may use a nonzero range when clearly labeled and analytically justified. Avoid unexplained dual axes, reversed axes, uneven time intervals, and inconsistent scales across comparable panels.
- Order by meaning: rank, chronology, process sequence, hierarchy, or a neutral midpoint. Alphabetical order is for lookup, not a default.
- Start with neutral marks. Use one accent for the message, muted context, and a consistent, colorblind-safe semantic palette. Never rely on color alone; supplement red/green with text, symbols, position, or pattern.
- Prefer direct labels. Make the measure, unit, timeframe, scope, source, and material methodology discoverable. Do not rotate labels when horizontal layout or a better composition solves the problem.
- Use a takeaway title in explain mode, a neutral descriptive title in explore mode, and a stable status-oriented title in monitor mode. Annotate only inflection points, events, outliers, thresholds, definition changes, forecast boundaries, gaps, and material uncertainty.
- Remove clutter, not information needed for verification, comparison, anomaly detection, or alternative interpretation. Use small multiples, tables, sparklines, and layering when they reduce confusion without hiding detail.

### 4. Connect insight to action

For explanatory work, structure the message as context → change or tension → evidence → meaning → decision. Separate observation from interpretation and do not claim a driver without attribution evidence.

Use a complete takeaway sentence:

> **[Subject] changed by [magnitude] versus [comparison], accompanied by [supported context], which means [implication].**

### 5. Implement when requested

Read [references/technology-recommendations.md](references/technology-recommendations.md) when creating or modifying a web chart, dashboard, or chart-producing code. Prefer the existing project stack when one exists. For a new web artifact, start with a static HTML/SVG representation and add application complexity only when interaction, data refresh, routing, or scale requires it.

Validate data at the boundary, keep transformations explicit and reproducible, preserve a visible table or text fallback for exact values, and make important information available without hover. Test at the actual delivery size and on narrow screens. Provide usable alt text and a concise source/method note.

## Audit and release gates

Audit an existing chart in this order:

1. Evidence integrity
2. Analytical fit
3. Perceptual accuracy
4. Context and comparison
5. Visual hierarchy
6. Labels and language
7. Accessibility
8. Decision usefulness

Before calling a chart final, adversarially ask:

- Can every value be traced, and are units, denominators, exclusions, missingness, uncertainty, and partial periods honest?
- Would another reasonable timeframe, benchmark, aggregation, or scale change the conclusion?
- Can the key comparison be made without mental arithmetic or a misleading visual encoding?
- Does the headline stay within the evidence, and is correlation kept separate from causation?
- Does meaning survive grayscale, small display sizes, keyboard or linear reading, and the absence of hover?

If a material problem remains, label the output provisional, correct it, request missing evidence, or recommend not charting it. Truthfulness is a blocking requirement.

Release only when the result is truthful, functionally aligned to the task, perceptually efficient, clear, insightful, and useful to the audience.

## Accessibility requirements

Ensure readable labels and contrast, logical reading order, non-color signals, keyboard-reachable controls, reduced-motion behavior, and a text/table alternative where exact values matter. Alt text should state the chart type and subject, main pattern, most important values, and any material exception or uncertainty; do not narrate decoration.

## Output contracts

When creating or recommending a chart, return:

```text
Decision:
Audience:
Primary takeaway:
Recommended chart:
Why this chart:
X encoding:
Y encoding:
Series or groups:
Ordering:
Scale:
Reference or benchmark:
Highlight:
Title:
Subtitle:
Annotations:
Source note:
Integrity caveats:
Alt text:
Artifact or code:
```

When critiquing a chart, return:

```text
Intended message:
Highest-impact problems: [no more than five, ordered by consequence]
Recommended redesign:
Why it works:
```

For dashboards, also name the monitored condition, normal/abnormal comparison, exception owner, refresh cadence, and decision that follows an exception. Organize overall status → exceptions → drivers → diagnostic detail.

## Hard prohibitions

Unless the user explicitly requests a knowingly decorative or experimental treatment, do not use invented data, hidden exclusions, unlabeled estimates, 3D or perspective distortion, truncated bar baselines, unexplained dual axes, rainbow scales for ordered magnitude, smoothing that implies nonexistent measurements, pies for trends or precise ranking, causal language from correlation alone, generic titles in explain mode, maps when geography is irrelevant, legends when direct labels clearly work, or dashboard elements without a monitoring purpose.
