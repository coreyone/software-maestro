# Pencil.dev system assets

These assets make Pencil.dev fit the Software Maestro design sprint and rapid prototype facade workflows.

## Assets

- [`DESIGN.md`](DESIGN.md) — product character, tokens, stack mapping, accessibility, and workflow contract.
- [`core-ios.lib.pen`](core-ios.lib.pen) — reusable light/dark variables and core components.
- [`templates/ios-reconstruction-template.pen`](templates/ios-reconstruction-template.pen) — 393×852 reference-plus-editable reconstruction board.
- [`templates/crazy-8s-ios-template.pen`](templates/crazy-8s-ios-template.pen) — eight labeled iOS variation frames with reference, concept, and audit areas.
- [`templates/ios-reconstruction-brief.md`](templates/ios-reconstruction-brief.md) — prompt contract for existing iOS screens.
- [`templates/crazy-8s-brief.md`](templates/crazy-8s-brief.md) — prompt contract for divergent target-step exploration.

## Use the library

Open the library file in Pencil, then import it from Libraries into each consumer `.pen` file. Verify that the variables and reusable components are visible before generating screens. Keep source fonts and images available beside the files; library links and custom assets depend on that workspace remaining portable.

The generated library is a `.lib.pen` file. If a Pencil installation requires an explicit library conversion, use Pencil’s “Turn this file into a library” action before importing it.

## CLI workflow

```bash
pen interactive -i design/pencil-systems/templates/crazy-8s-ios-template.pen \
  -o design/pencil-systems/exports/crazy-8s-review.pen

pen --in design/pencil-systems/exports/crazy-8s-review.pen \
  --out design/pencil-systems/exports/crazy-8s-shortlist.pen \
  --prompt-file design/pencil-systems/DESIGN.md \
  --prompt-file design/pencil-systems/templates/crazy-8s-brief.md \
  --prompt "Refine only the shortlisted frames. Preserve the target step and use the imported library."

pen --in design/pencil-systems/exports/crazy-8s-shortlist.pen \
  --export design/pencil-systems/exports/crazy-8s-review.png --export-scale 2
```

For agent work, read `read_skill()`, then inspect `get_app_state()`, variables, reusable components, and the imported library before editing. Save after each meaningful checkpoint. Use `pen --prompt-file` so the design contract is part of every run.

## Existing iOS apps

Capture Simulator screenshots with `xcrun simctl io booted screenshot`. Import them as locked references. Screenshots remain flattened; recreate SwiftUI/UIKit structure as editable Pencil layers and compare exported screens against the Simulator baseline. Pencil is the visual reconstruction and state exploration layer, not a native iOS runtime.

## Validation evidence

Before handoff, record:

- imported library and inspected variables/themes/components;
- target viewport and safe-area baseline;
- token and instance reuse;
- light/dark, state, responsive, motion, and accessibility audit;
- screenshot comparison and intentional deviations;
- selected frame, review question, and unresolved risks.
