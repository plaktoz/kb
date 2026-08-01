export const meta = {
  name: 'kb-scrapecontent-parallel',
  description: 'Parallel scrape: fans out up to 8 agents over URLs from raw/url/, collector writes log',
  phases: [
    { title: 'Discover', detail: 'Extract and deduplicate all URLs from raw/url/' },
    { title: 'Scrape', detail: 'Parallel fetch — up to 8 concurrent agents' },
    { title: 'Finalize', detail: 'Write log rows and delete source URL files' },
  ],
}

const WORKER_SCHEMA = {
  type: 'object',
  properties: {
    log_rows: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          date: { type: 'string' },
          filename: { type: 'string' },
          activity: { type: 'string' },
        },
        required: ['date', 'filename', 'activity'],
      },
    },
  },
  required: ['log_rows'],
}

// Phase 1: Discover URLs and load skill prompt in parallel
phase('Discover')

const [discovery, skillLoad] = await parallel([
  () => agent(
    'Read all .md files in raw/url/, skipping any file whose name ends in .processed.md. Extract every URL found across all files. Deduplicate. Return: urls (array of unique URLs), sourceFiles (array of file paths that were read, relative to repo root).',
    {
      label: 'discover-urls',
      schema: {
        type: 'object',
        properties: {
          urls: { type: 'array', items: { type: 'string' } },
          sourceFiles: { type: 'array', items: { type: 'string' } },
        },
        required: ['urls', 'sourceFiles'],
      },
    }
  ),
  () => agent(
    'Read the file skills/Scrape-content-prompt.md and return its complete text content.',
    {
      label: 'load-skill',
      schema: {
        type: 'object',
        properties: { content: { type: 'string' } },
        required: ['content'],
      },
    }
  ),
])

if (!discovery || !discovery.urls || discovery.urls.length === 0) {
  log('No URLs found in raw/url/ — nothing to scrape.')
  return { scraped: 0, failed: 0, log_rows: [] }
}

log(`Found ${discovery.urls.length} URL(s) across ${discovery.sourceFiles.length} file(s). Splitting into up to 8 batches.`)

const urls = discovery.urls
const agentCount = Math.min(8, urls.length)
const batchSize = Math.ceil(urls.length / agentCount)
const batches = []
for (let i = 0; i < urls.length; i += batchSize) {
  batches.push(urls.slice(i, i + batchSize))
}

const skillContent = skillLoad ? skillLoad.content : 'Fetch each URL. Extract article title, author, date, and body. Save to raw/YYYY-MM-DD-slug.md with a source_url: header.'

// Phase 2: Scrape in parallel — up to 8 agents
phase('Scrape')

const results = await parallel(
  batches.map((batch, i) => () =>
    agent(
      `You are a web scraping agent. Scrape these ${batch.length} URL(s):\n${batch.join('\n')}\n\nFollow these per-URL instructions exactly:\n${skillContent}\n\nIMPORTANT overrides for parallel mode:\n- Do NOT delete files from raw/url/ — the coordinator handles that.\n- Do NOT write to kbm.log.md — return log rows as structured output instead.\n- Return one log_row per URL attempted: date (YYYY-MM-DD, today's date), filename (e.g. 2026-07-28-article-slug.md or the url file if failed), activity ("scrape" for success, "scrape-failed" for failure).`,
      { label: `scrape-batch-${i + 1}`, schema: WORKER_SCHEMA }
    )
  )
)

// Phase 3: Finalize — coordinator writes all log rows and cleans up
phase('Finalize')

const allLogRows = results.filter(Boolean).flatMap(r => r.log_rows)
const scraped = allLogRows.filter(r => r.activity === 'scrape').length
const failed = allLogRows.filter(r => r.activity === 'scrape-failed').length

log(`${scraped} scraped, ${failed} failed. Writing log and deleting source URL files.`)

const logLines = allLogRows.map(r => `| ${r.date} | ${r.filename} | ${r.activity} |`).join('\n')
const deleteList = discovery.sourceFiles.join(', ')

await agent(
  `Perform these cleanup tasks in order:\n1. Append these rows to kbm.log.md (add to the existing table, do not overwrite):\n${logLines}\n2. Rename each of these source URL files by inserting .processed before .md (e.g. news.md → news.processed.md): ${deleteList}\n3. For each renamed file, append a row to kbm.log.md: | YYYY-MM-DD | <new-filename> | archive | (use today's date)`,
  { label: 'finalize' }
)

return { scraped, failed, log_rows: allLogRows }
