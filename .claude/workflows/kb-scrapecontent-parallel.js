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

// Inlined from .claude/skills/kb-scrapecontent/SKILL.md — keep in sync if that file changes.
// Inlining avoids paying an agent to read-and-echo a static file on every run (was costing
// ~3 min on the critical path, and previously pointed at a stale path that never resolved).
const SKILL_CONTENT = `---
name: kb-scrapecontent
description: Scrape URLs from /raw/url/ files, save clean articles to /raw/, and log activity to kbm.log.md. Use when the user wants to ingest URLs into the knowledge base.
---

# Scrape Content Prompt

You are a web scraping agent with file access. Your job is to extract URL content and save each article as a clean raw markdown file for later processing by the Karpathy-Ingest pipeline.

## Input

Read \`.md\` files from \`/raw/url/\`, **excluding any file whose name ends in \`.processed.md\`**. Two supported formats:

- **Search result / aggregation file** — a structured file with many URLs embedded in the content (e.g. a news aggregation with titles, URLs, and descriptions)
- **Simple URL list** — a plain \`.md\` file with one URL per line

Extract every URL found across all input files.

## Per-URL Instructions

### 1. Deduplicate

If the same URL appears more than once, process it only once.

### 2. Skip if already scraped

Before fetching, run a fast exact-match check: \`grep -rl "source_url: {URL}" raw/ wiki/ 2>/dev/null\` (this covers \`raw/\`, \`raw/processed/\`, and any \`wiki/\` note the URL may already have been ingested into). If any match is found, this article has already been scraped and/or ingested — skip it without fetching.

### 3. Fetch and clean

Fetch the URL and extract only:

- Article title
- Byline (author, if present)
- Publication date
- Article body text

Strip everything else: navigation, ads, footers, related articles, cookie banners, comment sections.

### 4. Handle failures

If a URL fails to fetch (404, paywall, timeout, or any error), log the failure to \`kbm.log.md\` and continue to the next URL. Do not create a file for failed fetches.

### 5. Save the file

Save to \`/raw/YYYY-MM-DD-slug.md\` where:

- \`YYYY-MM-DD\` is the article's own publication date (extract from the URL path or article metadata). If no reliable publish date can be found in either place, use today's scrape date instead of guessing — do not invent or approximate a date.
- \`slug\` is the article title converted to lowercase kebab-case

File format:

\`\`\`md
---
source_url: {URL}
author: {Author or "Unknown"}
date: {YYYY-MM-DD}
---

# {Article Title}

{Clean article body}
\`\`\`

### 6. Log each scraped file

Append a row to \`kbm.log.md\` for each successfully saved file:

\`\`\`md
| YYYY-MM-DD | filename.md | scrape |
\`\`\`

## After all URLs in a file are processed

1. Rename the source file in \`/raw/url/\` by inserting \`.processed\` before \`.md\` — e.g. \`news.md\` → \`news.processed.md\`. Do not delete the file.
2. Append a cleanup row to \`kbm.log.md\`:

\`\`\`md
| YYYY-MM-DD | source-filename.processed.md | archive |
\`\`\`

## Expected outcome

1 URL = 1 file in \`/raw/YYYY-MM-DD-slug.md\`
`

// Phase 1: Discover URLs
phase('Discover')

const discovery = await agent(
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
)

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

const skillContent = SKILL_CONTENT

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
