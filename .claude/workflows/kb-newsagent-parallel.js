export const meta = {
  name: 'kb-newsagent-parallel',
  description: 'Parallel news search: fans out one agent per category, collector merges + writes file and log',
  phases: [
    { title: 'Discover', detail: 'Read holdings and determine output filename' },
    { title: 'Search', detail: 'Parallel search + viability-check — one agent per category, up to 6 concurrent' },
    { title: 'Finalize', detail: 'Merge category sections into one file, write log row' },
  ],
}

// Keep in sync with data/wiki-categories.md's article-count column if it changes.
const CATEGORIES = [
  { key: 'technology', heading: '## 🚀 Technology', count: 3, hint: 'AI OR software OR startup news today (tech industry, tools)' },
  { key: 'finance', heading: '## 📊 Finance', count: 3, hint: 'stock market OR investing OR economy news today' },
  { key: 'productivity', heading: '## ⚡ Productivity', count: 3, hint: 'productivity tips OR time management OR deep work' },
  { key: 'learning', heading: '## 🧠 Learning', count: 3, hint: 'learning strategies OR skill development OR online education' },
  { key: 'health', heading: '## 🩺 Health', count: 3, hint: 'health research OR wellness OR nutrition OR mental health news today' },
  { key: 'holdings', heading: '## 📈 My Holdings', count: 3, hint: null },
]

// Inlined rules shared by every category worker — keep in sync with .claude/skills/kb-newsagent/SKILL.md
// if that file changes. Tightened vs. the sequential skill: viability-checking now prefers Tavily's
// own include_raw_content over a separate WebFetch round-trip, and caps replacement attempts at 1
// (not 2) — a slow run showed a single dead page being retried twice as the biggest tail-latency cost.
const SHARED_RULES = `
## Search

Use the Tavily MCP tool (mcp__tavily__tavily_search) as the primary search method, called with
include_raw_content: true so results already carry extractable article text. Keep max_results small
(5 is plenty) — you're running alongside 5 other search agents concurrently, and large
include_raw_content payloads (many full articles in one response) are the likely cause of stalls
seen in earlier runs. Make at most 2-3 search calls total for your category before picking your
final candidates; don't keep issuing broader queries hoping for better results. If Tavily errors,
hangs, or returns no MCP connection, fall back to the Serper MCP tool (mcp__serper-search__google_search)
immediately rather than retrying Tavily repeatedly.

## Dedup — required before finalizing your candidate list

For each candidate URL, run: grep -rl "source_url: {URL}" raw/ wiki/ 2>/dev/null
If any match is found, the article is already in the vault — drop it and pick a replacement.
Do not try to read kbm.log.md in full (it can be ~300KB) — this grep check is the authoritative signal.

## Blacklisted domains — never include

- reuters.com
- www.reuters.com

## Avoid live-blog / JS-rendered pages

Skip URLs with "live-updates", "/live/", or "liveblog" in the path — these are typically client-side
rendered and return empty content even when the domain isn't blocked. Prefer a static recap or
analysis article covering the same story instead.

## Viability check — tightened for speed

Tavily's include_raw_content already gives you the article text in the search result itself — treat
a non-trivial raw_content (a few hundred+ chars of real prose, not nav/boilerplate) as passing,
with no separate fetch needed. Only do one WebFetch check if raw_content is missing, empty, or
suspiciously short/menu-like. If a candidate fails viability, search for exactly ONE replacement in
the same category and re-check it the same way. If that replacement also fails, drop the slot and
note the shortfall in your section_body, e.g.:

(2 of 3 — one candidate was unscrapable and no working replacement was found)

Do not include a URL you have not verified has real extractable content.

## Output format for section_body

Bullet list only (no heading — the coordinator adds that), full raw URLs, no masked anchor text:

- **[Article title]**: [1-sentence description of why this is relevant]
  URL: https://...

- **[Article title]**: [1-sentence description]
  URL: https://...
`

const CATEGORY_SCHEMA = {
  type: 'object',
  properties: {
    heading: { type: 'string' },
    section_body: { type: 'string' },
    found: { type: 'number' },
    requested: { type: 'number' },
  },
  required: ['heading', 'section_body', 'found', 'requested'],
}

// Phase 1: Discover — holdings + output filename
phase('Discover')

const discovery = await agent(
  `Do two things and return structured output:
1. Read data/investments.md and return its holdings table rows as {ticker, name, category} — category is "Stock" or "ETF".
2. Determine today's date (YYYY-MM-DD) from your own current-date context, then list raw/url/ and find the right output filename: raw/url/{today}-news-aggregation.md if no file matching {today}-news-aggregation*.md exists yet (checking .md and .processed.md variants), otherwise the next available numbered variant (-2, -3, ...).
Return {date, holdings, output_filename} where output_filename is the relative path e.g. "raw/url/2026-09-29-news-aggregation-3.md".`,
  {
    label: 'discover',
    schema: {
      type: 'object',
      properties: {
        date: { type: 'string' },
        holdings: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              ticker: { type: 'string' },
              name: { type: 'string' },
              category: { type: 'string' },
            },
            required: ['ticker', 'name', 'category'],
          },
        },
        output_filename: { type: 'string' },
      },
      required: ['date', 'holdings', 'output_filename'],
    },
  }
)

// Phase 2: Search — one agent per category, fully concurrent
phase('Search')

const holdingsList = discovery.holdings.map(h => `${h.ticker} (${h.name}, ${h.category})`).join(', ')

const results = await parallel(
  CATEGORIES.map(cat => () => {
    const task =
      cat.key === 'holdings'
        ? `Category: My Holdings. Find exactly ${cat.count} distinct, high-quality, breaking/trending articles from the last 24–48 hours across these holdings: ${holdingsList}. For each Stock ticker, search "{TICKER} news today". For each ETF, infer a theme from the fund name and search by theme (e.g. an S&P 500 ETF -> "S&P 500 market news today"). Pick the ${cat.count} best/most distinct results across all holding queries.`
        : `Category: ${cat.key}. Find exactly ${cat.count} distinct, high-quality, breaking/trending articles from the last 24–48 hours using queries like: "${cat.hint}".`

    return agent(
      `You are a news search agent working on ONE category of a larger news-aggregation run.\n\n${task}\n${SHARED_RULES}\n\nReturn {heading, section_body, found, requested} — heading is exactly "${cat.heading}", requested is ${cat.count}, found is how many articles you actually included.`,
      { label: `search-${cat.key}`, phase: 'Search', schema: CATEGORY_SCHEMA }
    )
  })
)

// Phase 3: Finalize — assemble sections, write file + single log row
phase('Finalize')

// Preserve full category coverage even when an agent errored/stalled — a dropped category must
// show up as an explicit shortfall, never vanish silently (that reads as "no news that day" when
// it actually means "the search agent failed").
const sections = CATEGORIES.map((cat, i) => {
  const r = results[i]
  if (r) return r
  log(`WARNING: ${cat.key} search agent failed to return a result — noting shortfall (0 of ${cat.count}).`)
  return {
    heading: cat.heading,
    section_body: `(0 of ${cat.count} — search agent failed to complete, no replacement found)`,
    found: 0,
    requested: cat.count,
  }
})

const failedCategories = CATEGORIES.filter((cat, i) => !results[i]).map(cat => cat.key)
const totalFound = sections.reduce((sum, r) => sum + (r.found || 0), 0)
const totalRequested = sections.reduce((sum, r) => sum + (r.requested || 0), 0)

log(`${totalFound}/${totalRequested} articles found across ${CATEGORIES.length} categories${failedCategories.length ? ` (failed: ${failedCategories.join(', ')})` : ''}. Writing ${discovery.output_filename}.`)

const body = sections.map(r => `${r.heading}\n\n${r.section_body}`).join('\n\n')
const fullContent = `# News Aggregation — ${discovery.date}\n\n${body}\n`

await agent(
  `Write this exact content to ${discovery.output_filename} (create the file, overwrite if it somehow already exists):\n\n---BEGIN FILE CONTENT---\n${fullContent}\n---END FILE CONTENT---\n\nThen append this single row to kbm.log.md (add to the existing table, do not overwrite):\n| ${discovery.date} | ${discovery.output_filename.replace(/^raw\/url\//, '')} | news-fetch |`,
  { label: 'finalize' }
)

return {
  output_filename: discovery.output_filename,
  per_category: sections.map(r => ({ heading: r.heading, found: r.found, requested: r.requested })),
}
