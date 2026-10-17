# News search and selection rules

Shared by `/kb-newsagent` and every per-category agent of `/kb-newsagent-parallel`. Find the requested number of distinct, high-quality, breaking or trending articles from the last 24 to 48 hours.

## Search

Use Tavily (`mcp__tavily__tavily_search`) with `include_raw_content: true`, so results already carry the article text, and `max_results` of about 5. Make at most 2 or 3 search calls per category before picking candidates rather than broadening the query in the hope of better results.

If Tavily errors, hangs, or has no MCP connection, switch to Serper (`mcp__serper-search__google_search`) at once instead of retrying Tavily. If neither is available, fetch the category's fallback sources listed under its heading in `data/wiki-categories.md`.

## URL filters

Skip URLs whose path contains `live-updates`, `/live/` or `liveblog`. Live blogs are rendered client-side and scrape as empty pages even on unblocked domains. Prefer a static recap or analysis of the same story.

## Dedup

Before finalizing, check every candidate URL in one call:

```bash
python3 .claude/skills/kb-scrapecontent/scripts/scrape_queue.py seen URL1 URL2 ...
```

Drop every URL listed under `inVault` (already in `raw/` or `wiki/`), `failedBefore` (a past scrape failed) or `blockedDomain` (its domain or a parent domain is in `data/blocked-domains.md`). Only `fresh` URLs may be kept. Check replacements the same way. Do not read `kbm.log.md` or `data/blocked-domains.md` yourself; this call is the authoritative signal.

## Viability check

A candidate passes when its Tavily `raw_content` holds a few hundred characters or more of real article prose, not navigation or boilerplate. Only when `raw_content` is missing, empty, or menu-like, test-fetch the URL once. It fails if the fetch is blocked, returns near-empty content, or returns a response so large it is truncated with no article text near the top.

When a candidate fails, search for exactly one replacement in the same category and check it the same way. If the replacement also fails, drop the slot and note the shortfall in that category's section, for example:

```
(2 of 3 — one candidate was unscrapable and no working replacement was found)
```

Never keep a URL you have not verified.

## Section format

Bullets only, full raw URLs, no masked anchor text:

```markdown
- **[Article title]**: [1-sentence description of why this is relevant]
  URL: https://...
```
