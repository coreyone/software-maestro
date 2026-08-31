# Grounded Search — Reference

## Why this exists

Editorial-desk (a SvelteKit content pipeline in `~/Documents/middle-mile/apps/`) needed live web evidence for its topic-quality gate. The obvious "AI grounding" options were tried live and both failed on billing, not capability:

- **Gemini API search grounding** (`tools: [{google_search: {}}]`): 429 `RESOURCE_EXHAUSTED` on a free-tier key. Plain generation worked; only the grounding tool specifically required real billing.
- **OpenRouter's `web` plugin** (Exa-backed, `plugins: [{id: 'web', engine: 'exa'}]`): 402 `Insufficient credits` on a $0 account. Confirmed live, not assumed from docs.

`ddgs` (the DuckDuckGo-search-derived metasearch library, PyPI `ddgs`, current version 9.15.0 as of 2026-08) was confirmed live to work with zero key and zero billing:

```bash
~/.claude/tools/ground-search/venv/bin/python3 \
  ~/.claude/tools/ground-search/ground.py "query text" 8
```

Returns `{"ok": true, "results": [{"title", "url", "snippet"}, ...]}` or `{"ok": false, "error": "..."}`.

## Why it isn't a Claude-facing skill

Claude Code already has a built-in `WebSearch` tool. A skill that wraps `ground.py` for Claude's own use would add subprocess/venv latency for a capability that already exists natively, with no new coverage. `headless-browsing`'s own spec already excludes ordinary web search from its routing ("prefer an existing search or fetch tool for ordinary research") — this skill does not reopen that boundary; it exists one layer down, for application code that has no `WebSearch` tool at all.

## Why SearXNG / Crawl4AI / Firecrawl / local Qwen are deferred, not adopted

Checked live on this machine (2026-08-24): no Docker, no `ollama`, no `uv`. Installing any of SearXNG, Crawl4AI, Firecrawl, or a local Qwen-via-Ollama stack would mean standing up runtime infrastructure to solve a problem `ddgs` hasn't yet demonstrated it can't solve. Per `developer-development-rules`' Rule of Parsimony ("write a big program only when it is clear by demonstration that nothing else will do") and the anti-fragile principle "prefer simple defaults; add complexity only when it pays rent" — this is a real, not aesthetic, reason to wait. Revisit only when a specific app hits a concrete `ddgs` limitation:

- Rate-limited under real batch/scan load.
- Snippet-only depth is insufficient and pairing with plain-HTTP-fetch extraction (see below) doesn't close the gap.
- A task genuinely needs meta-search aggregation across engines beyond what `ddgs`'s own multiplexing provides.

## The provenance/error discipline this pairs with

Editorial-desk's `reddit-rss.ts` adapter (built same session) establishes the pattern any app-side grounding adapter should match:

- A `provenanceMode: 'live' | 'fixture'` field on ingested items; write-boundary functions refuse to persist anything not explicitly `'live'`. This closed a real fabrication vector found live in that project (fixture data almost got attributed as real evidence).
- Structured `ProblemDetails`-shaped errors, not opaque HTTP codes or swallowed exceptions.
- Rate-limit-aware pacing: `reddit-rss.ts` polls one subreddit per invocation, rotating by longest-since-polled, because Reddit's own RSS endpoint was confirmed live to 429 at ~15s spacing and succeed at ~30-60s. `ddgs` needs the equivalent discipline for batch/scan contexts — don't assume unlimited query volume just because it's free.

## `ground.py`'s own contract

- Explicit 5s per-engine timeout (`DDGS(timeout=5)`) — matches `ddgs`'s own internal default, made explicit rather than implicit.
- `{"ok": true, "results": [...]}` (empty list is a valid, honest "found nothing," not an error) vs `{"ok": false, "error": "..."}` with a distinct message for `DDGSException` (library-level failure) vs any other unexpected exception.
- Lives in an isolated venv at `~/.claude/tools/ground-search/venv` (Homebrew's system Python is externally managed per PEP 668 and refuses bare `pip install`). **Do not `mv` this venv** — venv `pip`/scripts have shebangs with absolute paths baked in; only `python3` itself survives relocation via `pyvenv.cfg`. Recreate with `python3 -m venv` at the destination and reinstall instead.
