export const meta = {
  name: 'kb-newsagent-parallel',
  description: 'Parallel news search: fans out one agent per category, collector merges + writes file and log',
  phases: [
    { title: 'Discover', detail: 'Read holdings, news categories and the output filename' },
    { title: 'Search', detail: 'Parallel search + viability-check — one agent per category' },
    { title: 'Finalize', detail: 'Merge category sections into one file, write log row' },
  ],
}

const RULES_PATH = '.claude/skills/kb-newsagent/references/rules.md'

const HINTS = {
  technology: 'AI OR software OR startup news today (tech industry, tools)',
  finance: 'stock market OR investing OR economy news today',
  productivity: 'productivity tips OR time management OR deep work',
  learning: 'learning strategies OR skill development OR online education',
  health: 'health research OR wellness OR nutrition OR mental health news today',
  strategy: 'competitive strategy OR decision frameworks OR mental models',
}

const HOLDINGS = { key: 'holdings', heading: '## 📈 My Holdings', count: 3 }

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

phase('Discover')

const discovery = await agent(
  `Do three things and return structured output:
1. Read data/investments.md and return its holdings table rows as {ticker, name, category} — category is "Stock" or "ETF".
2. Read the table in data/wiki-categories.md and return one {key, heading, count} per row, in table order, skipping rows whose "News articles/day" is "—". key is the Category column without backticks or the trailing slash (e.g. "strategy"), heading is the "Newsletter section" column verbatim (e.g. "🎯 Strategy"), count is the "News articles/day" number.
3. Determine today's date (YYYY-MM-DD) from your own current-date context, then list raw/url/ and find the right output filename: raw/url/{today}-news-aggregation.md if no file matching {today}-news-aggregation*.md exists yet (checking .md and .processed.md variants), otherwise the next available numbered variant (-2, -3, ...).
Return {date, holdings, categories, output_filename} where output_filename is the relative path e.g. "raw/url/2026-09-29-news-aggregation-3.md".`,
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
        categories: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              key: { type: 'string' },
              heading: { type: 'string' },
              count: { type: 'number' },
            },
            required: ['key', 'heading', 'count'],
          },
        },
        output_filename: { type: 'string' },
      },
      required: ['date', 'holdings', 'categories', 'output_filename'],
    },
  }
)

if (!discovery.categories.length) throw new Error('No news categories parsed from data/wiki-categories.md')

const CATEGORIES = [
  ...discovery.categories.map(c => ({ ...c, heading: `## ${c.heading}` })),
  HOLDINGS,
]

phase('Search')

const holdingsList = discovery.holdings.map(h => `${h.ticker} (${h.name}, ${h.category})`).join(', ')

const results = await parallel(
  CATEGORIES.map(cat => () => {
    const task =
      cat.key === 'holdings'
        ? `Category: My Holdings. Find exactly ${cat.count} distinct, high-quality, breaking/trending articles from the last 24–48 hours across these holdings: ${holdingsList}. For each Stock ticker, search "{TICKER} news today". For each ETF, infer a theme from the fund name and search by theme (e.g. an S&P 500 ETF -> "S&P 500 market news today"). Pick the ${cat.count} best/most distinct results across all holding queries.`
        : `Category: ${cat.key}. Find exactly ${cat.count} distinct, high-quality, breaking/trending articles from the last 24–48 hours using queries like: "${HINTS[cat.key] ?? `${cat.key} news today`}".`

    return agent(
      `You are a news search agent working on ONE category of a larger news-aggregation run.\n\n${task}\n\nRead ${RULES_PATH} and follow it for search, URL filters, dedup, the viability check and the section format. Put only the bullets in section_body; the coordinator adds the heading.\n\nReturn {heading, section_body, found, requested} — heading is exactly "${cat.heading}", requested is ${cat.count}, found is how many articles you actually included.`,
      { label: `search-${cat.key}`, phase: 'Search', schema: CATEGORY_SCHEMA }
    )
  })
)

phase('Finalize')

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
