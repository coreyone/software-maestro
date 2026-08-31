---
name: grounded-search-rules
description: "Trigger: grounded-search-rules, search grounding, free search adapter, DDGS search, SearXNG, backend RAG evidence, web search adapter. Scope: Backend Web Search Grounding. Connects free/OSS search adapters (DDGS, SearXNG) into backend RAG retrieval pipelines. Boundary: Excludes browser automation."
---

# 🔎 Core Philosophy: Ground app-side LLM output in real retrieval, without a billing wall.

## When to use

Use this skill when implementing a feature *inside an application's own code* (a SvelteKit route, a background adapter, a batch job) that needs live web results to ground an LLM's answer, produce citations, or gather evidence server-side — anywhere the app itself, not the Claude Code agent, needs to search the web at runtime.

## When not to use

- Claude Code's own research during a conversation: use the built-in `WebSearch` tool directly. Never shell out to this skill's tooling for that — it adds latency and a Python dependency for a capability Claude already has natively.
- Rendering, clicking, or extracting content from an already-known page: that's `headless-browsing`'s job, not this skill's.
- The user has explicitly asked for a specific paid vendor (Exa, Tavily, Perplexity, Google grounding with billing enabled): honor that choice; this skill's default is the free path, not the only path.

## Trigger cues

- Key terms: grounding, web search integration, RAG, retrieval-augmented, citations, DDGS, SearXNG, Crawl4AI, Firecrawl, "give the LLM live data," "search the web from the app," fact-check pipeline, evidence source.
- Building or extending a content/research pipeline (e.g. editorial-desk-style topic scoring, case-study evidence gathering) that needs a live web-search backend.

## Routing boundary

- Primary for wiring search *retrieval* into application code.
- Secondary to `headless-browsing` when the actual need is fetching/rendering one specific, already-identified page rather than discovering results for a query.
- Secondary to `developer-eval-driven-development` when the ask is really about judging an LLM's answer quality, not the retrieval mechanism.

## Inputs required

- Target app/repo and its existing adapter/error-handling conventions (e.g. editorial-desk's `ProblemDetails` + `provenanceMode: 'live'|'fixture'` discipline).
- What the grounding is for: citations, RAG context injection, fact-checking, or raw evidence collection.
- Source of truth: `references/source.md`

## Instructions

1. **Default to the free primitive, not a paid vendor.** `~/.claude/tools/ground-search/ground.py` (ddgs-backed, zero-key) is the default. Do not reach for Gemini's search-grounding tool or OpenRouter's `web` plugin as the default — both were confirmed live (2026-08-24) to require paid billing/credits despite being documented as free-tier accessible. Only use them if the user explicitly wants that vendor.
2. **Verify, don't assume, richer local infrastructure exists.** SearXNG, Crawl4AI, Firecrawl, and Ollama are *not* installed on this machine as of 2026-08-24 (no Docker, no `ollama`, no `uv`). Check (`which docker`, `which ollama`, `curl localhost:8080`) before referencing them as available; do not install them speculatively — only when a real, demonstrated limit of `ddgs` (rate-limited under load, snippet-only depth blocking a specific task) justifies it.
3. **Wire it in as a proper in-repo adapter, not a bare script call.** Match the project's existing evidence-honesty pattern. `ground.py` already returns `{"ok": true, "results": [...]}` or `{"ok": false, "error": "..."}` — preserve that ok/error distinction through to the app's own error contract (e.g. `ProblemDetails`) rather than collapsing it.
4. **Respect rate limits.** `ddgs` multiplexes across engines but each engine still throttles. Do not hot-loop queries inside a scan/batch job. Apply the same pacing discipline already established for other rate-limited free sources in this workspace (e.g. `reddit-rss.ts`'s "one subreddit per invocation, rotate by longest-since-polled").
5. **Treat results as leads, not verified content.** `ground.py` returns snippets only, never full page text. Pair with a plain HTTP fetch + text extraction step (see `reddit-rss.ts`'s `extractPlainBody` for a proven, dependency-free pattern) when the app needs actual page content rather than a result list.
6. **Never fabricate on `ok:false` or an empty result set.** An empty `results` array is a real, honest answer ("searched, found nothing"), not an error to paper over with invented findings. Surface it the same way every other adapter in this workspace already does.

## Completion gate

Before reporting the grounding feature done, confirm:

- A live call actually returned real results — verified by inspection, not assumed from the code reading correctly.
- The failure path (`ok:false`, non-zero exit, or a network error) surfaces through the app's own structured error shape, not a raw uncaught exception.
- No fixture, mock, or cached data can silently pass as a live result if the project has a provenance/fixture-guard convention.

## Output format

- Primary decision/output: adapter code (plus its test file, if the project follows TDD) that calls `ground.py` and maps its output into the app's own types.
- Summary: one paragraph stating which backend was used (`ground.py`/ddgs by default) and why, naming the free-vs-paid tradeoff explicitly if a paid alternative was considered.
- Evidence: a real, logged/observed successful call and a real, logged/observed failure-path call, not just the happy path.
