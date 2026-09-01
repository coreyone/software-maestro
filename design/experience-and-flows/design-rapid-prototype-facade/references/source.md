# Jake Knapp Design Sprint: Goldilocks Prototype Facade (Thursday)

## 1. First Principles & Mindsets
- **The Hollywood Set Facade**: Flawless visual surface, empty scaffolding behind the wall.
- **Goldilocks Fidelity Curve**: Wireframes evoke intellectual critiques; real code takes weeks; Goldilocks evokes honest emotional reactions.
- **Disposable Asset**: Code built for 60 minutes of testing on Friday, then discarded.
- **15:00 Trial Run**: Compulsory end-to-end rehearsal before the day ends.

---

## 2. Google Stitch MCP & Stitch-Loop Acceleration

Google Stitch transforms Thursday prototyping by automating screen generation and styling:

```
  [Storyboard Panel] ──► [Enhanced Prompt with .stitch/DESIGN.md]
                                │
                                ▼
                   [Stitch MCP: generate_screen_from_text]
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
     [.stitch/designs/{page}.html]    [.stitch/designs/{page}.png]
                 │
                 ▼
     [Assemble in site/public/{page}.html] ◄── [Stitch-Loop Baton]
                 │
                 ▼
     [edit_screens for Rapid Polish]
                 │
                 ▼
     [Chrome DevTools Local Verification & 15:00 QA]
```

### Stitch MCP Tooling Reference:
1. `create_project`: Initializes a new Stitch project (persisting `projectId` in `.stitch/metadata.json`).
2. `generate_screen_from_text`: Generates HTML and screenshot assets from structured prompts.
3. `edit_screens`: Targeted edits to existing screens (e.g. *"Change hero CTA to emerald green and update headline"*).
4. `get_screen` / `list_screens`: Retrieves screen status and asset download URLs.

### Industrial Role Division:
- **Makers (2-3)**: Generate screens via Stitch MCP and assemble HTML layouts.
- **Stitcher (1)**: Wires interactive links between pages and ensures unified header/footer navigation.
- **Writer (1)**: Crafts real headlines, button labels, and zero *Lorem Ipsum* microcopy.
- **Asset Collector (1)**: Sources authentic photography and brand logos.
- **Interviewer (1)**: Finalizes Friday's 5-Act interview guide and scorecards.
