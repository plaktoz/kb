export const meta = {
  name: 'kb-ingest-transcript',
  description: 'Full YouTube transcript pipeline: fetch → stage → parallel ingest → archive',
  phases: [
    { title: 'Fetch', detail: 'Download YouTube transcripts in parallel (up to 8)' },
    { title: 'Stage', detail: 'Convert transcripts to ingest-ready raw/ files' },
    { title: 'Ingest', detail: 'Parallel wiki note creation (up to 8 agents)' },
    { title: 'Archive', detail: 'Move transcript folders to processed/ and rename source URL files' },
  { title: 'Newsletter', detail: 'Compile today\'s ingested notes into a daily digest' },
  ],
}

const FETCH_SCHEMA = {
  type: 'object',
  properties: {
    success: { type: 'boolean' },
    transcriptFolder: { type: 'string' },
    url: { type: 'string' },
    error: { type: 'string' },
  },
  required: ['success', 'url'],
}

const STAGE_SCHEMA = {
  type: 'object',
  properties: {
    stagedFiles: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          rawFile: { type: 'string' },
          folderPath: { type: 'string' },
        },
        required: ['rawFile', 'folderPath'],
      },
    },
  },
  required: ['stagedFiles'],
}

const LOG_SCHEMA = {
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

// ── Phase 1: Fetch ─────────────────────────────────────────────────────────
phase('Fetch')

const [urlDiscovery, speakerPromptLoad] = await parallel([
  () => agent(
    'Check if the directory raw/youtube/ exists. If it does, list all .md files inside (excluding any file whose name ends in .processed.md) and extract all YouTube URLs (one per line). Return: urls (array of YouTube URL strings, may be empty), sourceFiles (array of relative file paths e.g. ["raw/youtube/queue.md"]).',
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
    'Read the file .claude/skills/baoyu-youtube-transcript/prompts/speaker-transcript.md and return its complete text content.',
    {
      label: 'load-speaker-prompt',
      schema: {
        type: 'object',
        properties: { content: { type: 'string' } },
        required: ['content'],
      },
    }
  ),
])

const discoveredUrls = (urlDiscovery && urlDiscovery.urls) ? urlDiscovery.urls : []
const argsUrls = args ? (Array.isArray(args) ? args : [args]).filter(s => typeof s === 'string' && s.startsWith('http')) : []
const urls = [...new Set([...argsUrls, ...discoveredUrls])]
const sourceFiles = (urlDiscovery && urlDiscovery.sourceFiles) ? urlDiscovery.sourceFiles : []
const speakerPrompt = (speakerPromptLoad && speakerPromptLoad.content) ? speakerPromptLoad.content : ''

if (urls.length > 0) {
  log(`Found ${urls.length} YouTube URL(s). Downloading in parallel (up to 8).`)

  await parallel(
    urls.map((url, i) => () =>
      agent(
        `Download the YouTube transcript for this URL and post-process speaker identification.

URL: ${url}

Step 1 — Download:
Run this bash command (single-quote the URL to prevent zsh glob expansion):
  npx -y bun .claude/skills/baoyu-youtube-transcript/scripts/main.ts '${url}' --chapters --speakers --output-dir youtube-transcript

The command prints the saved transcript.md path to stdout.

Step 2 — Speaker identification:
The saved transcript.md contains YAML frontmatter and a raw SRT-formatted transcript body. Post-process it:
1. Read the saved transcript.md
2. Apply the speaker identification instructions below to convert the SRT transcript into a readable structured transcript with speaker labels, chapter headings, and paragraph-level timestamps
3. Overwrite transcript.md with the processed result — keep the original YAML frontmatter unchanged

Speaker identification instructions:
${speakerPrompt}

Return success: true and transcriptFolder (the video folder path, parent directory of transcript.md, e.g. "youtube-transcript/ai-engineer/video-title/") if successful, or success: false with error message if the download failed.`,
        { label: `fetch-${i + 1}`, schema: FETCH_SCHEMA, phase: 'Fetch' }
      )
    )
  )
} else {
  log('No YouTube URLs in raw/youtube/ — checking for existing unarchived transcripts.')
}

// ── Phase 2: Stage ─────────────────────────────────────────────────────────
phase('Stage')

const stageResult = await agent(
  `Find all transcript.md files anywhere inside the youtube-transcript/ directory tree, excluding anything inside youtube-transcript/processed/. For each file:

1. Read the YAML frontmatter and extract: title, url (the YouTube URL), date (YYYY-MM-DD), channel
2. Build the staged filename: {date}-video-{title in lowercase kebab-case}.md
3. Build the staged file content in Karpathy ingest format — exactly:

# {title}

source_url: {youtube url}
author: {channel}

---

{transcript body, with these transformations applied:
 - Remove all [HH:MM:SS → HH:MM:SS] timestamp patterns
 - Remove cover image lines (any line containing "![cover]")
 - Remove the Table of Contents section (## Table of Contents and its list items)
 - Keep everything else: speaker labels (**Name:**), chapter headings (## Chapter Title), and all spoken text
}

4. Write the staged file to raw/{staged-filename}
5. Record: rawFile = staged filename only (e.g. "2026-07-28-video-every-company-should-have-a-brain.md"), folderPath = the video folder path (e.g. "youtube-transcript/ai-engineer/every-company-should-have-a-brain-garry-tan-y-combinator/")

If no transcript.md files exist in youtube-transcript/, return an empty stagedFiles array.`,
  { label: 'stage', schema: STAGE_SCHEMA }
)

const stagedFiles = (stageResult && stageResult.stagedFiles) ? stageResult.stagedFiles : []

if (stagedFiles.length === 0) {
  log('No transcripts found to stage — pipeline complete.')
  if (sourceFiles.length > 0) {
    await agent(
      `Rename each of these source YouTube URL files by inserting .processed before .md (e.g. queue.md → queue.processed.md): ${sourceFiles.join(', ')}\nThen append an archive row to kbm.log.md for each: | YYYY-MM-DD | <new-filename only, no path> | archive | (use today's date)`,
      { label: 'cleanup-source-files', phase: 'Archive' }
    )
  }
  return { ingested: 0 }
}

log(`Staged ${stagedFiles.length} transcript(s) to raw/.`)

// ── Phase 3: Ingest ────────────────────────────────────────────────────────
phase('Ingest')

const [skillLoad, catLoad] = await parallel([
  () => agent(
    'Read skills/Karpathy-Ingest-prompt.md and return its complete text content.',
    {
      label: 'load-skill',
      schema: { type: 'object', properties: { content: { type: 'string' } }, required: ['content'] },
    }
  ),
  () => agent(
    'Read data/wiki-categories.md and return its complete text content.',
    {
      label: 'load-categories',
      schema: { type: 'object', properties: { content: { type: 'string' } }, required: ['content'] },
    }
  ),
])

const rawFileNames = stagedFiles.map(s => s.rawFile)
const agentCount = Math.min(8, rawFileNames.length)
const batchSize = Math.ceil(rawFileNames.length / agentCount)
const batches = []
for (let i = 0; i < rawFileNames.length; i += batchSize) {
  batches.push(rawFileNames.slice(i, i + batchSize))
}

const skillContent = skillLoad ? skillLoad.content : ''
const catContent = catLoad ? catLoad.content : ''

const ingestResults = await parallel(
  batches.map((batch, i) => () =>
    agent(
      `You are a PKM ingest agent. Process these ${batch.length} raw file(s) from the raw/ directory:\n${batch.join('\n')}\n\nFollow these per-file instructions exactly:\n${skillContent}\n\nWiki categories reference:\n${catContent}\n\nIMPORTANT overrides for parallel mode:\n- Do NOT write to kbm.log.md — return log rows as structured output instead.\n- Still move each source file from raw/ to raw/processed/ after processing it.\n- Return one log_row per processed file: date (today's date YYYY-MM-DD), filename (raw source filename only), activity "ingest".`,
      { label: `ingest-batch-${i + 1}`, schema: LOG_SCHEMA, phase: 'Ingest' }
    )
  )
)

// ── Phase 4: Archive ───────────────────────────────────────────────────────
phase('Archive')

const allLogRows = ingestResults.filter(Boolean).flatMap(r => r.log_rows)
const ingested = allLogRows.filter(r => r.activity === 'ingest').length
const folderPaths = stagedFiles.map(s => s.folderPath)
const logLines = allLogRows.map(r => `| ${r.date} | ${r.filename} | ${r.activity} |`).join('\n')

const tasks = [
  logLines.length > 0
    ? `1. Append these rows to kbm.log.md (add to the existing table, do not overwrite):\n${logLines}`
    : '1. No ingest log rows to write.',
  folderPaths.length > 0
    ? `2. Move each of these video folders into youtube-transcript/processed/, preserving the channel subfolder (e.g. youtube-transcript/ai-engineer/video-title/ → youtube-transcript/processed/ai-engineer/video-title/). Create the channel subdirectory under youtube-transcript/processed/ if it does not exist. Then append an archive row to kbm.log.md for each moved folder: | YYYY-MM-DD | <video-folder-name> | archive | (use today's date, folder name only e.g. video-title). Folders to move:\n${folderPaths.join('\n')}`
    : '2. No transcript folders to move.',
  sourceFiles.length > 0
    ? `3. Rename each of these source YouTube URL files by inserting .processed before .md (e.g. queue.md → queue.processed.md): ${sourceFiles.join(', ')}\n   Then append an archive row for each to kbm.log.md: | YYYY-MM-DD | <new-filename only> | archive | (use today's date)`
    : '3. No source URL files to rename.',
].join('\n\n')

await agent(tasks, { label: 'archive' })

log(`Done. ${ingested} transcript(s) ingested into wiki.`)

// ── Phase 5: Newsletter ────────────────────────────────────────────────────
if (ingested > 0) {
  phase('Newsletter')

  const newsletterPromptLoad = await agent(
    'Read Skills/Daily-newsletter-prompt.md and return its complete text content.',
    {
      label: 'load-newsletter-prompt',
      schema: { type: 'object', properties: { content: { type: 'string' } }, required: ['content'] },
    }
  )

  if (newsletterPromptLoad && newsletterPromptLoad.content) {
    await agent(
      newsletterPromptLoad.content,
      { label: 'newsletter', phase: 'Newsletter' }
    )
  }
}

return { ingested }
