export const meta = {
  name: 'kb-scrapecontent-parallel',
  description: 'Parallel scrape: one agent per probed URL; the skill runs scrape_queue.py discover before and finalize after',
  phases: [
    { title: 'Scrape', detail: 'One agent per URL; the probe verdict decides which tool it may use' },
  ],
}

// args: { date, items } — copied from the queue file `scrape_queue.py discover` writes.
// Workflow scripts have no filesystem access, so
// discovery, dedup, logging and archiving stay in that script rather than in extra agents.

const ROW_SCHEMA = {
  type: 'object',
  properties: {
    filename: { type: 'string' },
    activity: { type: 'string', enum: ['scrape', 'scrape-failed'] },
    reason: { type: 'string' },
  },
  required: ['filename', 'activity'],
}

const FILE_RULES = `Save to raw/YYYY-MM-DD-slug.md where YYYY-MM-DD is the article's own publication date
(from the metadata, the URL path, or the text; if none is reliable, use today's date, {date} — never guess)
and slug is the article title in lowercase kebab-case. If that filename already exists for a different
URL, append -2. File format:

---
source_url: {url}
author: {Author or "Unknown"}
date: {YYYY-MM-DD}
---

# {Article Title}

{Clean article body: keep the article's own paragraphs and headings in order. Drop navigation, ads,
promo banners, newsletter signups, "most popular"/related-article lists, author bios, comments.
Do not summarize or add anything that is not in the source.}

Do not write to kbm.log.md and do not touch raw/url/ — the coordinator does both.`

const IDEMPOTENT = `First run: grep -rl "source_url: {url}" raw/ 2>/dev/null
If it matches, an earlier attempt already saved this article: return activity "scrape" with that file's
name and stop.`

const FALLBACK = `Make exactly one mcp__tavily__tavily_extract call for this URL. If it returns the article body
(several paragraphs of real prose, not a teaser, subscribe prompt, or challenge page), use it. Otherwise
stop and return activity "scrape-failed" with a short reason. Do not try WebFetch, curl, other MCP
scrapers, search engines, or archive sites — the probe already established that direct access fails,
and every extra attempt costs minutes.`

function prompt(item, date) {
  const known = [
    item.title && `title: ${item.title}`,
    item.author && `author: ${item.author}`,
    item.published && `published: ${item.published}`,
  ].filter(Boolean).join('\n')
  const source = item.verdict === 'ok'
    ? `The page was already fetched. Its extracted text is in ${item.text_path} — read that file and do
not fetch the URL. The text may still contain leftover promo or link-list lines; clean those out.
If the file is clearly not the article (an index page, cookie wall, or a few stray lines), fall back:
${FALLBACK}`
    : `A probe could not get the article directly: ${item.verdict} (${item.reason}).
${FALLBACK}`
  return [
    `Scrape one article into the knowledge vault. Today is ${date}.`,
    `URL: ${item.url}`,
    known && `Probe metadata (prefer it over guesses):\n${known}`,
    IDEMPOTENT.replaceAll('{url}', item.url),
    source,
    FILE_RULES.replaceAll('{url}', item.url).replaceAll('{date}', date),
    'Return filename (just the basename, e.g. 2026-09-28-some-title.md) for a save, or for a failure the URL; activity; and reason.',
  ].filter(Boolean).join('\n\n')
}

const items = (args && args.items) || []
const date = (args && args.date) || ''
if (!items.length) {
  log('No URLs in the queue — nothing to scrape.')
  return { scraped: 0, failed: 0, rows: [] }
}

phase('Scrape')
const dead = items.filter(i => i.verdict === 'dead')
const live = items.filter(i => i.verdict !== 'dead')
log(`${items.length} URL(s): ${live.filter(i => i.verdict === 'ok').length} fetched by the probe, ` +
  `${live.filter(i => i.verdict !== 'ok').length} need the one-shot fallback, ${dead.length} dead (no agent).`)

const results = await parallel(live.map(item => () =>
  agent(prompt(item, date), { label: `scrape:${item.url.replace(/^https?:\/\//, '').split('/')[0]}`, schema: ROW_SCHEMA })
))

const failedRow = (item, reason) => ({ filename: `${item.url} (${reason})`, activity: 'scrape-failed' })
const rows = [
  ...live.map((item, i) => {
    const r = results[i]
    if (!r) return failedRow(item, 'agent stalled or errored')
    return r.activity === 'scrape'
      ? { filename: r.filename, activity: 'scrape' }
      : failedRow(item, r.reason || `${item.verdict}: ${item.reason}`)
  }),
  ...dead.map(item => failedRow(item, `dead: ${item.reason}`)),
]
const scraped = rows.filter(r => r.activity === 'scrape').length
log(`${scraped} scraped, ${rows.length - scraped} failed.`)
return { scraped, failed: rows.length - scraped, rows }
