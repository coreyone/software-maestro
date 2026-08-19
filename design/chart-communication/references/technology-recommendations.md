# Technology recommendations for chart work

Use these as defaults for a new web visualization. Favor open-source, low-cost, fast-to-ship choices. Follow the repository’s established stack when it is healthy and compatible; do not rewrite a project merely to match this list.

## Selection ladder

1. **Static HTML + SVG/CSS first** for a single report, prototype, or chart with no application state. This is the lowest-cost, most inspectable, and easiest-to-share output.
2. **SvelteKit + TypeScript + Vite** for a maintained web chart, dashboard, or data story that needs routing, server data, or reusable components.
3. **LayerChart** as the default chart library in a Svelte project. Use native SVG or Canvas for a small custom chart when the library would add more complexity than value.
4. **D3** only for custom geometry, scales, layouts, or interactions that the chosen chart layer does not provide. Keep data transforms separate from rendering.
5. **SolidJS** is a reasonable alternative for a new high-performance interactive visual when SvelteKit is not a natural fit.

## Project defaults

- Use Bun for package management, scripts, and tests when the ecosystem supports it; keep Vite for SvelteKit development and HMR.
- Use Biome for formatting and linting. Prefer TypeScript types plus Zod; use Valibot when bundle size is the limiting constraint.
- Use vanilla CSS or Tailwind. Use Bits UI, Melt UI, or shadcn-svelte only when the surrounding application already uses them or accessible controls are needed.
- Use Lucide or Iconoir for interface icons, not icons scaled as fake data marks. Use Mermaid for explanatory flowcharts in documentation.
- Use TanStack Query for remote server state and TanStack Table for exact-value lookup or dense operational detail. A chart should not replace a table when lookup is the job.
- Use SvelteKit endpoints by default; add Hono only for an edge-oriented boundary that needs it. Use Drizzle with Supabase or Neon when persistence is required.
- Prefer Netlify with `adapter-netlify` for a small Svelte deployment when the project has no stronger hosting constraint. Use static output when server behavior is not needed.

## Data and runtime rules

- Validate request and file shapes at the boundary. Reject malformed input with a clear error; never coerce invalid values into a plausible-looking chart.
- Keep time in UTC internally and convert to an IANA timezone only at the presentation edge. Label the displayed timezone when it affects interpretation.
- Keep raw data, transformations, and visual encodings distinct. Name derived fields and document filters, aggregation, normalization, currency, inflation, and forecast logic.
- Make colors, scales, sort order, and annotations deterministic so a later refresh does not silently change the story.
- Use a stable chart ID and accessible names for interactive controls. Keep exact values available as text or a table, not only in a tooltip.

## Delivery and verification

- Test data transformations with Bun test or Vitest. Use Playwright for responsive, keyboard, tooltip, and screenshot checks when the chart is interactive.
- Check the actual delivery width, narrow screens, grayscale, contrast, zoom, and `prefers-reduced-motion` behavior. Do not treat a desktop screenshot as proof of accessibility.
- In SSR applications, keep browser-only measurement and resize code behind the appropriate client boundary; avoid layout shifts when the chart hydrates.
- Verify empty, loading, error, partial-period, zero, negative, missing, and very-large-value states. Preserve a meaningful fallback table or message for each.
- If the chart is embedded in a slide or document, export a static, self-contained artifact and include source, timeframe, units, and alt text alongside it.
