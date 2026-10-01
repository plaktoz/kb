// Runs .claude/workflows/kb-scrapecontent-parallel.js with stubbed workflow hooks and checks
// what it asks agents to do. Usage: node workflow_harness.mjs [queue.json]
import { readFileSync } from 'node:fs'
import assert from 'node:assert/strict'

const root = new URL('../../', import.meta.url)
const src = readFileSync(new URL('.claude/workflows/kb-scrapecontent-parallel.js', root), 'utf8')
const body = src.replace(/^export const meta = /m, 'const meta = ')
const run = new Function('agent', 'parallel', 'phase', 'log', 'args', `return (async () => {\n${body}\n})()`)

async function exec(items, respond) {
  const calls = []
  const agent = async (prompt, opts) => {
    calls.push({ prompt, opts })
    return respond(prompt, calls.length - 1)
  }
  const parallel = thunks => Promise.all(thunks.map(t => t().catch(() => null)))
  const result = await run(agent, parallel, () => {}, () => {}, { date: '2026-10-01', items })
  return { calls, result }
}

const fixture = [
  { url: 'https://ok.example/a', verdict: 'ok', reason: '5000 chars of text', text_path: '/tmp/kb-scrape-x/a.md',
    title: 'A title', author: 'Ann', published: '2026-09-30' },
  { url: 'https://wsj.example/b', verdict: 'blocked', reason: 'bot challenge page' },
  { url: 'https://hbr.example/c', verdict: 'paywall', reason: 'isAccessibleForFree=false, 800 chars visible' },
  { url: 'https://gone.example/d', verdict: 'dead', reason: 'http 404' },
  { url: 'https://slow.example/e', verdict: 'unreachable', reason: 'no response in 10s' },
]
const items = process.argv[2] ? JSON.parse(readFileSync(process.argv[2], 'utf8')).items : fixture

const { calls, result } = await exec(items, (prompt, i) => {
  if (prompt.includes('https://ok.example/a')) return { filename: '2026-09-30-a-title.md', activity: 'scrape' }
  if (prompt.includes('https://hbr.example/c')) return { filename: 'https://hbr.example/c', activity: 'scrape-failed', reason: 'tavily returned a teaser' }
  if (prompt.includes('https://slow.example/e')) return null
  return { filename: `x${i}`, activity: 'scrape-failed', reason: 'tavily_extract failed' }
})

const live = items.filter(i => i.verdict !== 'dead')
assert.equal(calls.length, live.length, 'one agent per non-dead url, none for dead urls')
for (const [i, c] of calls.entries()) {
  const urls = new Set(c.prompt.match(/https?:\/\/[^\s"')]+/g))
  assert.deepEqual([...urls], [live[i].url], `agent ${i} prompt names exactly its own url`)
  assert.match(c.prompt, /grep -rl "source_url: /, 'agent checks for an earlier attempt first')
  assert.match(c.prompt, /exactly one mcp__tavily__tavily_extract/, 'fallback is bounded to one call')
  if (live[i].verdict === 'ok') assert.ok(c.prompt.includes(live[i].text_path), 'ok urls read the probe text')
  else assert.ok(c.prompt.includes(`${live[i].verdict} (${live[i].reason})`), 'non-ok prompt carries the verdict')
}
assert.equal(result.rows.length, items.length, 'every url gets exactly one log row, including stalled agents')

if (!process.argv[2]) {
  assert.deepEqual(result.rows, [
    { filename: '2026-09-30-a-title.md', activity: 'scrape' },
    { filename: 'https://wsj.example/b (tavily_extract failed)', activity: 'scrape-failed' },
    { filename: 'https://hbr.example/c (tavily returned a teaser)', activity: 'scrape-failed' },
    { filename: 'https://slow.example/e (agent stalled or errored)', activity: 'scrape-failed' },
    { filename: 'https://gone.example/d (dead: http 404)', activity: 'scrape-failed' },
  ])
  const empty = await exec([], () => assert.fail('no agent for an empty queue'))
  assert.deepEqual(empty.result, { scraped: 0, failed: 0, rows: [] })
}
console.log(`ok: ${items.length} items -> ${calls.length} agents, ${result.scraped} scraped, ${result.failed} failed`)
