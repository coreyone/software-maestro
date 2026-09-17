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

The current CLI requires Node.js 22.19 or later and authentication for agent operations, exports, interactive mode, and workspace access. Use `pen login` for a local session, `PEN_CLI_KEY` for CI/CD, and `pen status` before work. Use `pen codex-login` when selecting Codex as the CLI agent.

```bash
pen status

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

Use `--repo path/to/project` when the agent must inspect source code, CSS, tokens, screenshots, or assets in the same workspace. Use repeatable `--prompt-file` attachments for `DESIGN.md`, briefs, source files, and critique notes. Use `--preview-output` and `--enable-preview` for iterative evidence. For agent work, read `read_skill()`, then inspect `get_app_state()`, variables, reusable components, and the imported library before editing. Save after each meaningful checkpoint.

## Current pen.dev capabilities

### Code → Design

For an existing web product, keep the `.pen` file beside the code and ask the agent to recreate a named component or page from source. This imports component structure, hierarchy, layout, styling, typography, and spacing. Attach the project’s `DESIGN.md` and token files, then explicitly name the required SvelteKit/TypeScript, Bits UI/shadcn-svelte/Melt UI, Tailwind or Vanilla CSS, Lucide/iconoir, and Motion choices.

For an existing iOS product, attach the Simulator screenshot plus SwiftUI/UIKit source. Use the screenshot as visual truth and source as structural truth. Do not treat Code → Design as a native iOS importer.

### Token synchronization

When the product has CSS variables, ask Pencil to create variables from `globals.css` or the project token file. When a Pencil system change is approved, ask it to update the CSS variables. Review conflicts instead of creating duplicate variables. Keep screenshot reconstruction separate from token normalization.

### Web and Figma import

Use the desktop app’s built-in browser to import a web page or selected element as editable layers. JavaScript interactions do not transfer. Use Screenshot for a flattened visual reference. Import complete Figma files when the source design already exists there; import SVGs when editable vector layers are needed. PNG and JPEG remain flattened image layers.

### MCP and Codex

Open the intended `.pen` file in the desktop app or IDE extension, enable Codex in Settings → MCP, reload the client, and confirm `pencil` appears in the live MCP tool list. Always include the full `.pen` path in the prompt when more than one design file is open. Attach files through the agent context and verify that each attachment is visible before sending.

### Icons

Use Pencil’s built-in Lucide, Phosphor, Feather, or Material Symbols libraries when they match the product. Use Lucide or iconoir for production code according to the project preference. Import custom SVG icons only when the product actually owns them.

## Existing iOS apps

Capture Simulator screenshots with `xcrun simctl io booted screenshot`. Import them as locked references. For an existing app, the screenshot and runtime behavior outrank the starter library during reconstruction: recreate the observed UI faithfully, then use `DESIGN.md` to identify tokens, accessibility rules, and proposed changes. Do not “normalize” an existing screen to the library unless the brief explicitly requests a redesign. Screenshots remain flattened; recreate SwiftUI/UIKit structure as editable Pencil layers and compare exported screens against the Simulator baseline. Pencil is the visual reconstruction and state exploration layer, not a native iOS runtime.

## Validation evidence

Before handoff, record:

- imported library and inspected variables/themes/components;
- target viewport and safe-area baseline;
- token and instance reuse;
- light/dark, state, responsive, motion, and accessibility audit;
- screenshot comparison and intentional deviations;
- selected frame, review question, and unresolved risks.
