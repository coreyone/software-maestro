# Jake Knapp Design Sprint: Goldilocks Prototype Facade (Thursday)

## 1. The Prototyping Fidelity Matrix

```
┌───────────────────────────────┬───────────────────────────────┬──────────────────────────────────────────┐
│ Fidelity Tier                 │ Primary Tooling               │ When to Choose                           │
├───────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ **Low-Fidelity Wireframe**    │ `tldraw-offline`              │ • Testing rough layout & IA wayfinding   │
│                               │ (tldraw Desktop Canvas)       │ • Rapid structural validation            │
│                               │                               │ • Interactive buttons via document script│
├───────────────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ **High-Fidelity Web Facade**  │ Google Stitch MCP             │ • Testing visual appeal, branding & trust│
│                               │ + `stitch-loop`               │ • Testing real customer conversion & WTP │
│                               │                               │ • Pixel-perfect responsive HTML/CSS      │
└───────────────────────────────┴────────────────────────────────┴──────────────────────────────────────────┘
```

---

## 2. Low-Fidelity Wireframing Workflow with `tldraw-offline`

1. **Document Setup**: Discover open doc via `POST /api/search` (`api.getDocs()`).
2. **Create Wireframe Frames**: Use `/exec` to render structural screen rectangles (`editor.createShape({ type: 'geo', props: { geo: 'rectangle', w: 390, h: 844 } })`).
3. **Interactive Clicks (Durable Script)**:
   - Open `/script-workspace` and implement `script/main.js` using the `clickable-card-or-button-ui` recipe:
   ```javascript
   helpers.onShapeClick(buttonShapeId, () => {
     editor.setCamera({ x: -500, y: 0, z: 1 }, { animation: { duration: 250 } })
   })
   ```
4. **Capture Visual Proof**: Call `api.getScreenshot(docId)` to generate a snapshot for the 15:00 QA report.

---

## 3. High-Fidelity Web Facade Workflow with Google Stitch MCP

1. **Screen Generation**: Call `generate_screen_from_text` with `.stitch/DESIGN.md` tokens.
2. **Asset Retrieval**: Download `.stitch/designs/{page}.html` and high-res `.png` screenshots.
3. **Multi-Screen Baton Assembly**: Use `stitch-loop` (`.stitch/next-prompt.md`) to assemble the full golden path in `site/public/`.
4. **Targeted Edits**: Use `edit_screens` for rapid micro-adjustments.
5. **Local Verification**: Verify with Chrome DevTools MCP (`npx serve site/public`) before the 15:00 Trial Run.
