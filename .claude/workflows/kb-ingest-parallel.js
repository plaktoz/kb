export const meta = {
  name: 'kb-ingest-parallel',
  description: 'Parallel ingest: fans out up to 8 agents over raw/ articles into wiki notes, collector writes log',
  phases: [
    { title: 'Discover', detail: 'Find eligible raw files, load skill prompt and categories' },
    { title: 'Ingest', detail: 'Parallel conversion to wiki notes — up to 8 concurrent agents' },
    { title: 'Finalize', detail: 'Write log rows to kbm.log.md' },
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

// Phase 1: Discover files + load skill prompt + load categories in parallel
phase('Discover')

const [discovery, skillLoad, catLoad] = await parallel([
  () => agent(
    'List all .md files directly in raw/ (not in subdirectories) that contain a "source_url:" header. Return their filenames only (e.g. "2026-07-28-article-slug.md"), not full paths.',
    {
      label: 'discover-files',
      schema: {
        type: 'object',
        properties: {
          files: { type: 'array', items: { type: 'string' } },
        },
        required: ['files'],
      },
    }
  ),
  () => agent(
    'Read the file skills/Karpathy-Ingest-prompt.md and return its complete text content.',
    {
      label: 'load-skill',
      schema: {
        type: 'object',
        properties: { content: { type: 'string' } },
        required: ['content'],
      },
    }
  ),
  () => agent(
    'Read data/wiki-categories.md and return its complete text content.',
    {
      label: 'load-categories',
      schema: {
        type: 'object',
        properties: { content: { type: 'string' } },
        required: ['content'],
      },
    }
  ),
])

if (!discovery || !discovery.files || discovery.files.length === 0) {
  log('No raw files eligible for ingest.')
  return { ingested: 0, log_rows: [] }
}

log(`Found ${discovery.files.length} file(s) to ingest. Splitting into up to 8 batches.`)

const files = discovery.files
const agentCount = Math.min(8, files.length)
const batchSize = Math.ceil(files.length / agentCount)
const batches = []
for (let i = 0; i < files.length; i += batchSize) {
  batches.push(files.slice(i, i + batchSize))
}

const skillContent = skillLoad ? skillLoad.content : 'Transform raw files into structured wiki notes with YAML frontmatter, Summary, Core Concepts, and Key Takeaways sections.'
const catContent = catLoad ? catLoad.content : ''

// Phase 2: Ingest in parallel — up to 8 agents
phase('Ingest')

const results = await parallel(
  batches.map((batch, i) => () =>
    agent(
      `You are a PKM ingest agent. Process these ${batch.length} raw file(s) from the raw/ directory:\n${batch.join('\n')}\n\nFollow these per-file instructions exactly:\n${skillContent}\n\nWiki categories reference:\n${catContent}\n\nIMPORTANT overrides for parallel mode:\n- Do NOT write to kbm.log.md — return log rows as structured output instead.\n- Still move each source file from raw/ to raw/processed/ after processing it (this remains your responsibility).\n- Return one log_row per processed file: date (YYYY-MM-DD, today's date), filename (the raw source filename), activity ("ingest").`,
      { label: `ingest-batch-${i + 1}`, schema: WORKER_SCHEMA }
    )
  )
)

// Phase 3: Finalize — coordinator writes all log rows
phase('Finalize')

const allLogRows = results.filter(Boolean).flatMap(r => r.log_rows)
const ingested = allLogRows.filter(r => r.activity === 'ingest').length

log(`${ingested} file(s) ingested. Writing log.`)

const logLines = allLogRows.map(r => `| ${r.date} | ${r.filename} | ${r.activity} |`).join('\n')

await agent(
  `Append these rows to kbm.log.md (add to the existing table, do not overwrite):\n${logLines}\n\nUse today's date for any rows missing a date.`,
  { label: 'finalize-log' }
)

return { ingested, log_rows: allLogRows }
