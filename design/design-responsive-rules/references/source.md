# Responsive Web Design (2026) — Guidelines for Design + Design Engineering

**Key idea:** Design **mobile-first** for flow and constraints, then scale up with **layout breakpoints** and **component container queries**.  
**Goal:** Consistent UX, minimal breakpoint debt, fast implementation, fewer regressions.

---

## 0) Outcomes we care about (definition of “done”)
✅ Works at all target widths without horizontal scroll  
✅ Core tasks are easy to find and complete at every breakpoint  
✅ Tap targets meet minimum size + spacing  
✅ Images are responsive and don’t cause layout shift  
✅ Components adapt to their container (not just the viewport)  
✅ Desktop doesn’t feel like a “blown-up mobile page” (no content dispersion)
✅ Foldables, high-density displays, keyboard/mouse, touch, and coarse pointers are usable
✅ Viewport height changes, safe areas, hinges, and virtual keyboards do not hide critical actions

---

## 1) Principles (what to optimize for)
1. **Content-first**: layout serves hierarchy and tasks, not device models.
2. **Fewer breakpoints, better designs**: every breakpoint adds design/dev/test cost.
3. **Components are portable**: a card should work in 1-column, 2-column, sidebar, and grid.
4. **Progressive enhancement**: baseline experience is excellent on small screens.
5. **Readable by default**: control line length, spacing, and hierarchy at every size.
6. **Touch-friendly interactions**: avoid tiny targets; prioritize forgiving UI.
7. **Performance is UX**: responsive images, avoid over-fetching, keep layouts stable.
8. **Capabilities over device labels**: use available width, height, pointer, hover, orientation,
   reduced-motion preference, and safe-area insets; device names are test fixtures, not CSS rules.

---

## 2) Modern viewport and device test matrix

Use the following as a **minimum visual QA matrix**. The first resolution in each row is the
CSS viewport in logical pixels; the second is the common physical display resolution. Layout
breakpoints respond to the CSS viewport, not the physical pixel count or device marketing name.
High-density screens must be tested at their CSS viewport size and at the intended device pixel
ratio where image sharpness, canvas rendering, and text rasterization matter.

| Class | CSS viewport (W × H) | Physical display (W × H) | Primary risks to test |
|---|---:|---:|---|
| Mobile (Standard) | 393 × 852 | 1170 × 2532 | Safe areas, one-handed reach, dynamic browser chrome, long labels |
| Mobile (Compact) | 360 × 800 | 1080 × 2400 | Wrapping, minimum tap targets, dense headers, keyboard overlap |
| Mobile Foldable (Cover Screen) | 344 × 882 | 1080 × 2640 | Narrow cover flow, safe areas, compact navigation, posture changes |
| Mobile Foldable (Unfolded Screen) | 768 × 1072 | 1812 × 2176 | Two-pane opportunity, hinge/fold obstruction, orientation changes |
| Laptop 13″ (Compact) | 1280 × 800 | 2560 × 1600 | Short height, persistent nav, dense work surfaces, zoom |
| Laptop 15″ (Midsize) | 1440 × 900 | 2880 × 1864 | Default desktop composition, sidebars, table density |
| Laptop 17″ (Widescreen) | 1536 × 864 | 1920 × 1080 | Wide but short viewport, horizontal rhythm, vertical clipping |
| Desktop Standard (1080p) | 1920 × 1080 | 1920 × 1080 | Content containment, multi-column balance, readable line length |
| Desktop XL (QHD / 4K) | 2560 × 1440 | 3840 × 2160 | Content dispersion, oversized empty space, image density |
| Desktop Ultrawide | 3440 × 1440 | 3440 × 1440 | Excessive line length, side-rail sprawl, focus travel |

### 2.1 Matrix rules

- Treat every row as a **test target**, not a request for a device-specific media query.
- Test portrait and landscape where the product supports rotation; at minimum test the compact
  mobile, both foldable postures, and the shortest-height laptop/desktop cases.
- Include browser zoom at 200% and OS text scaling where accessibility is in scope. A layout is
  not responsive if it only works at 100% zoom.
- Test both touch/coarse-pointer and keyboard/fine-pointer input. Hover is an enhancement, never
  the only way to discover state or action.
- Test with the virtual keyboard open, browser chrome expanded/collapsed, and safe-area insets
  applied. Critical controls must remain reachable without relying on a fixed `100vh` assumption.
- Record the **design break** and the user-visible behavior for each transition; do not record
  only a pixel value.

### 2.2 Modern window and posture cases

- Test a resizable desktop window, OS split view, and mobile multi-window mode. A page may receive
  a much smaller viewport than the physical screen suggests.
- On foldables, treat cover and unfolded screens as separate flows. Keep content out of the hinge,
  crease, or occluded region; when posture APIs are unavailable, use a safe single-column fallback.
- Prefer `100svh` for stable minimum-height layouts, `100dvh` when the layout should follow the
  visible viewport, and `100lvh` only when the expanded viewport is intentional. Never make a
  primary action reachable only below a viewport-height calculation.
- Use `env(safe-area-inset-*)` for edge-to-edge surfaces and fixed controls. Add padding; do not
  use safe-area values as a substitute for content spacing.
- For installable web apps, test browser, standalone, and fullscreen display modes. Re-check
  status-bar treatment, back navigation, focus restoration, and fixed bottom bars in each mode.

---

## 3) Breakpoint strategy (page layout)
### 3.1 Default breakpoint set (start here)
Use these **viewport tiers** for *page-level* layout changes:
- **Phone:** 0–639
- **Tablet:** 640–1023
- **Desktop:** 1024–1279
- **Wide:** 1280–1535
- **XL Wide:** 1536+

> Rule: Start with **Phone / Tablet / Desktop** only. Add Wide/XL only if you have a real layout need.

### 3.2 What is allowed to change at viewport breakpoints
Use viewport breakpoints for:
- **Navigation pattern** (tabs ⇢ collapsible ⇢ full nav)
- **Column count** and **sidebar behavior**
- **Density** (cards per row, table vs list)
- **Hero layout** (stacked ⇢ split)
- **Global spacing scale** (padding/margins bump)

Avoid using viewport breakpoints for:
- Small component tweaks (use **container queries** instead)
- Device-specific rules (no “iPhone 14” targets)

### 3.3 Breakpoints are chosen by “design breaks”
Add/adjust breakpoints when:
- Nav labels wrap or truncate in a harmful way
- Cards collapse into awkward aspect ratios
- Important content drops below the fold unnecessarily
- Interaction becomes error-prone (tiny taps, crowded controls)

---

## 4) Container query strategy (component behavior)
### 4.1 When to use container queries
Use container queries for:
- Cards/tiles that appear in grids of varying columns
- Modules used in both main content and sidebars
- Buttons/toolbars that sometimes compress (filters, sort, actions)
- Media blocks (image + text) that reflow based on space

### 4.2 Component “size classes” (container widths)
Define these container-driven states (names can vary, keep consistent):
- **Compact**: single-column, narrow container
- **Standard**: typical content column
- **Expanded**: wide container / multi-column area

Each component must specify:
- Layout (stack vs split)
- Visible metadata (what shows/hides)
- Typography scale (minor adjustments only)
- Action placement (inline vs overflow)

---

## 5) Layout rules (design system expectations)
### 5.1 Grid + spacing
- Use a **fluid grid**; avoid fixed widths for columns/cards.
- Use **consistent spacing tokens** (e.g., 4/8/12/16/24/32).
- Cap reading width for text-heavy pages:
  - **Ideal line length:** ~60–80 characters per line.
  - Use a **max content width** to prevent “content dispersion” on large screens.

### 5.2 Type
- Use fluid type where appropriate (e.g., `clamp()` on headings).
- Maintain clear hierarchy:
  - H1/H2/H3 scaling should not collapse on mobile.
- Avoid giant desktop type that causes excessive scroll.

### 5.3 Page structure
- Prefer **single primary column** on mobile; avoid competing side rails.
- On tablet/desktop, add rails only if they add real value:
  - related content, filters, summary, actions.

---

## 6) Navigation and discoverability
### 6.1 Mobile nav (execution rules)
- Don’t hide *everything* behind a menu by default.
- If using a hamburger:
  - Keep key actions visible (e.g., Search, Cart, Primary CTA).
  - Keep the menu label clear (“Menu” + icon) if space permits.
- For tablet and up, consider surfacing top-level categories or persistent nav.
