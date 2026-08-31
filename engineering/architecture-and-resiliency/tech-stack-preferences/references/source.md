# Tech Stack Preferences

Be a static maximalist HTML page first.

OSS-first. Free, low-cost, and fast. e.g. Netlify + Qwen + fal.ai.
 
When building new projects, use these defaults when natural unless there's a specific reason not to.

---

## Core Stack

Every project starts here.

- **Framework**: SvelteKit (TypeScript) — full-stack, simple, fast
- **Framework (Alternative)**: [SolidJS](https://github.com/solidjs/solid) — high-performance, simple reactivity (no VDOM)
- **Build**: Vite — just works
- **Runtime**: Bun — default runtime when ecosystem compatibility allows
- **Package Manager**: Bun (`bun install`) — default package manager
- **Bundler**: Bun (`bun build`) for scripts/libraries; use Vite for app dev server + HMR workflows
- **Lint + Format**: Biome — one tool, zero config
- **Flowcharting Documentation**: [Mermaid](https://mermaid.js.org/intro/)

### Bun (When Natural)

Use Bun as more than a package manager when it makes sense for compatibility and speed:

- **Runtime**: `bun run` for local scripts, tooling, and server entrypoints
- **Package Manager**: `bun install` and `bunx` for task execution
- **Bundler**: `bun build` for small services, CLIs, and library builds
- **Test Runner**: `bun test` for Bun/Node-compatible unit tests

Prefer existing stack tools when they are a better fit:

- Keep **Vite** for SvelteKit/Solid app dev server and HMR experience
- Keep **Vitest** where plugin ecosystem, browser-like testing behavior, or team standards require it

---

## UI

### Styling
Use Vanilla CSS or Use **Tailwind CSS** for utility-first styling.


### Component Kits

Pick one based on needs:

- **Base UI** — Unstyled UI components for building accessible web apps and design systems. https://github.com/mui/base-ui.  This is preferred for react. 
- **Bits UI** — Unstyled UI components for building accessible web apps and design systems. https://github.com/huntabyte/bits-ui.  This is preferred for svelte. 
- **shadcn-svelte** — polished, accessible, svelte-native.
- **Skeleton** — svelte-first, ships quick
- **DaisyUI** — get it done mode

### Headless Components

When you need full control:

- **Bits UI** — great DX
- **Melt UI** — solid a11y primitives

### Visual Utilities

- **Icons**: Lucide or iconoir
- **Animation**: Motion (motion.dev)
- **3D**: Three.js
- **Canvas & Shader Effects**: [Canvas UI](https://github.com/DavidHDev/canvas-ui) — WebGL shader effects over live, interactive HTML/DOM elements
- **Charts**: LayerChart
- **Maps**: MapLibre GL JS
- **Loading Spinners**  Unicode Animations (https://www.npmjs.com/package/unicode-animations)
- **Haptics** Mobile web haptics (https://github.com/lochie/web-haptics)

### UI Libraries

- **Canvas UI** — for interactive WebGL shader overlays on DOM elements (https://github.com/DavidHDev/canvas-ui)
- **NumberFlow** — for animating numbers
- **Driver.js** — for user onboarding, guided tours, and feature spotlights (https://github.com/kamranahmedse/driver.js)
- **input-otp** — for one-time passwords
- **Liveline** — for real-time charts
- **Leva** — for customizable GUIs
- **cmdk** — for command menus
- **Virtuoso** — for virtualization
- **dnd kit** — for drag and drop
- **Sonner** — for notifications

### UI library selection rules

Prefer the smallest tool that solves a demonstrated interaction. Do not add a UI library just because it is available.

- **Canvas UI — when to use**: Use for high-impact landing pages, creative hero sections, interactive showcases, or micro-interactions requiring WebGL shader effects (e.g., glass refraction, shatter, rain droplets, hex float) layered directly over live, accessible, interactive DOM elements across React, Svelte, Vue, Solid, or Vanilla JS.
- **Canvas UI — when not to use**: Do not use for standard application layouts, dense data tables, administrative interfaces, or low-end mobile experiences where standard CSS (like `backdrop-filter`) is sufficient and WebGL overhead would hurt performance or battery life.
- **Driver.js — when to use**: Use for lightweight, interactive product walkthroughs, feature highlight tours, or guided onboarding steps. It is MIT-licensed, zero-dependency, vanilla TS (~5 KB gzip), and framework-agnostic (works with SvelteKit, Solid, React, or static HTML).
- **Driver.js — when not to use**: Do not use when native headless primitives (e.g. Bits UI / Base UI dialogs, popovers, or step checklists) offer a better inline UX than full-screen spotlight overlays. Avoid heavy dual-licensed alternatives like Intro.js.

#### 415FC live draft companion

- **NumberFlow — consider later.** Useful for refreshed roster counts, pick totals, and status metrics when a value change needs emphasis. Keep the dense player tables static; manual refresh does not need realtime number motion.
- **cmdk — consider later.** A good fit for a keyboard-first “jump to player,” “change view,” or “refresh” command surface. Do not add it until those commands are numerous enough to justify a palette. `cmdk` is React-oriented, so use a Svelte-native equivalent if the app moves to SvelteKit. [cmdk](https://github.com/dip/cmdk)
- **Sonner — do not add now.** The app has one small inline toast surface and should keep it local and visually restrained. Sonner is React-oriented; if notification volume grows, choose a framework-native equivalent before introducing a global toast system. [Sonner](https://www.npmjs.com/package/sonner)
- **Virtuoso — not needed now.** The draft board and cheat sheet are small enough for normal rendering, and virtualization would work against positional scanning. Reconsider only for a much larger player-search surface or a full multi-season dataset.
- **input-otp — not applicable.** V1 has no OTP or authentication flow.
- **Liveline — not applicable now.** V1 is manual-refresh and has no realtime chart feed. Use a static table or compact trend treatment if draft-history analysis is added later.
- **Leva — not for the product UI.** It is a developer control surface, not an owner-facing settings pattern. Use the existing settings surface or a normal form for user controls.
- **dnd kit — not needed now.** Draft order and picks come from Sleeper; drag-and-drop would create a second source of truth. Reconsider only for an explicitly user-authored board or lineup workflow.

Default for this app: keep the current dependency set. Add a library only with a named user task, a measurable interaction benefit, and a fallback plan for the app’s current framework/runtime.
---

## Forms + Data

- **Forms**: sveltekit-superforms — server + client, native to SvelteKit
- **Form UI**: formsnap — pairs well with tailwind/shadcn
- **Validation**: Zod (or Valibot if bundle size matters)
- **Tables**: [TanStack Table](https://tanstack.com/table) — headless, flexible
- **Server State**: [TanStack Query](https://tanstack.com/query) — caching done right
- **Dates**: date-fns — tiny, treeshakeable
- **Rich Text**: Tiptap or Lexical — depends on needs
- **Collaboration**: Hocuspocus CRDT Y.js WebSocket backend for conflict-free real-time collaboration, hocuspocus collaboration. 
- **Sync / Zero-latency**: [Zero](https://zero.rocicorp.dev) — general-purpose sync engine for instant UI, automatic reactivity, and zero-latency (zero__ms) data sync.
- **Validation**: Zod (or Valibot if bundle size matters) https://zod.dev
---

## API

Default to **SvelteKit endpoints**. Keep it simple.

When you need more:

- **Hono** — tiny, edge-ready functions
- **tRPC** — type-safe RPC
- **ts-rest** — contract-first REST
- **Zodios** — REST tooling on Zod

---

## Database

- **ORM**: Drizzle — TS-first, handles migrations
- **Postgres**: Supabase (self-host ok) or Neon (managed)

---

## Auth

Pick one:

- **Better Auth** — drop-in, fastest path
- **Auth.js** — standards-based, good ecosystem
- **Netlify Identity** — zero config if already on Netlify

Note: Lucia v3 is deprecated. Plan migrations accordingly.

---

## Deploy

- **Host**: Netlify
- **Adapter**: adapter-netlify
- **Forms**: Netlify Forms for quick wins
- **Background Jobs**: Trigger.dev for long-running pipelines

---

## Content

- **Markdown**: MDsveX — svelte + markdown
- **Prose linting**: [Vale](https://github.com/vale-cli/vale) — fast, markup-aware, extensible linting for documentation prose, including spelling and style checks
- **CMS**: Decap CMS — git-based, Netlify-friendly
  - **CMS**: [astro.build](https://astro.build)

---

## Media + Uploads

- **Uploads**: Uppy
- **Images**: sharp (server-side processing)
- **Audio**: Howler.js
- **Audio Transcription**: elevenlabs.io
- **Voice Audio Generation**: elevenlabs.io

---

## Email

- **API**: Resend
- **Templates**: React Email (optional, for polished templates)

---

## Analytics + Experiments

- **Product Analytics**: PostHog (OSS) or Plausible (OSS) or Umami (https://umami.is/docs) or Goatcounter (https://goatcounter.com)
- **Feature Flags**: GrowthBook or Unleash (OSS)
- **Closed exception**: Statsig if you need enterprise features

---

## AI — LLMs

### Models

- **Primary**: Qwen (general) + Qwen-Coder (coding tasks)
- **Also**: Gemini Flash

### Local Runners

- **Ollama** — easy setup, good for dev
- **llama.cpp** — low-level control, embed in apps

### Production Serving

- **vLLM** — high-throughput inference

---

## AI — Generative Media

- **Hosted GPU**: fal.ai — images, video, upscalers, just works
- **Local Pipelines**: ComfyUI — full control when needed

---

## AI — Web Search / Grounding

- **Default**: `ground.py` at `~/.claude/tools/ground-search/` — a ddgs-backed, zero-key, free web search primitive callable identically from Claude Code skills (shell out) and any app (spawn a subprocess). Confirmed live 2026-08-24.
  - Call: `~/.claude/tools/ground-search/venv/bin/python3 ~/.claude/tools/ground-search/ground.py "<query>" [max_results]` → `{"ok": true, "results": [{title, url, snippet}]}` on stdout, or `{"ok": false, "error": "..."}` (exit 1) on failure. `ok:true` with an empty `results` array means "searched, found nothing" — not a failure.
  - App consumer, not a Claude-skill router: `headless-browsing`'s own scope explicitly excludes ordinary web search ("prefer an existing search or fetch tool"), so this stays a plain callable dependency for app backends (SvelteKit routes, adapters) — not wired into any skill's routing table.
  - Why this over the obvious "AI grounding" options: Gemini's Google Search grounding tool 429s on the free-tier API key (requires real billing even to try, confirmed live); OpenRouter's `web` plugin (Exa-backed) requires paid account credits (confirmed live, 402 on a $0 account). Both are marketed as free-tier accessible but are not, in practice.
  - Returns snippets only, not full page text — pair with a plain HTTP fetch + text extraction (see `reddit-rss.ts`'s pattern in the editorial-desk project for a proven, zero-dependency example) when an app needs the actual page content, not just a result list.
  - Upgrade path once Docker/Ollama are actually installed on the machine: self-hosted SearXNG (meta-search, no API key, aggregates multiple engines) as a richer discovery layer, and local Qwen via Ollama as the summarizing model — neither is installed as of 2026-08-24, so don't assume they're available without checking first.

## AI — Tooling

- **LLM Gateway**: LiteLLM — one OpenAI-style API to many providers
- **AI Framework**: [TanStack AI](https://tanstack.com/ai/latest) — type-safe AI hooks for React, Solid, Svelte, and Vue
- **Observability**: Langfuse — prompts, evals, management
- **Agentic Context**: [Context7](https://context7.com) — MCP server for high-fidelity context injection and knowledge retrieval. Use the Context7 API to search libraries and fetch documentation programmatically:
  ```bash
  curl -X GET "https://context7.com/api/v2/libs/search?libraryName=next.js&query=setup+ssr" \
    -H "Authorization: Bearer ctx7sk-bf353672-198f-4dd0-b455-494fda116585"
  ```
- **Regression Testing**: promptfoo — catch prompt drift early

---

## Vibe-coding Tools

- **IDE Assistant**: Continue — OSS, works with Qwen
- **Terminal**: Aider — pair programmer
- **Agent Framework**: OpenHands — agentic dev platform

---

## Testing

- **Unit + Integration**: Bun test (default where compatible) or Vitest (when ecosystem/tooling needs it)
- **E2E**: Playwright

---

## Automation

- **Workflows**: n8n
- Browser AI Automation: https://github.com/browserbase/stagehand
