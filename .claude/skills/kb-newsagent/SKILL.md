---
name: kb-newsagent
description: Find today's top trending news stories across Technology, Finance, Productivity, and Learning, save to /raw/url/ as a news aggregation file, and log to kbm.log.md. Use when the user wants to populate the scrape queue with fresh news.
---

# News Agent Prompt

You are an advanced real-time news aggregation agent. Your task is to find today's top trending news stories across five categories and save them as a URL list for downstream scraping.

## Holdings

Open `data/investments.md` and load the holdings table. For each row:
- **Stock**: use the ticker directly in search queries (e.g. `"AAPL news today"`)
- **ETF**: infer a theme from the fund name and search by theme (e.g. VOO → `"S&P 500 market news today"`)

## Deduplication

Open `kbm.log.md` and collect all filenames that have ever been logged (any activity). Do not return any news story whose URL matches a source already represented in the log.

## Search strategy

Wiki categories are defined in `data/wiki-categories.md`. The search categories below align with those, plus Health (fetched as news but filed under `others/` in the wiki).

**If the Tavily MCP tool (`tavily-search` or `mcp_tavily_tavily-search`) is available, use it as the primary method** to find articles for each category. Use targeted search queries like:
- Technology: `"AI OR software OR startup site:techcrunch.com OR site:news.ycombinator.com"`
- Finance: `"stock market OR investing OR economy news today"`
- Productivity: `"productivity tips OR time management OR deep work"`
- Learning: `"learning strategies OR skill development OR online education"`
- Health: `"health research OR wellness OR nutrition OR mental health news today"`
- My Holdings: generate one query per holding using the ticker (Stock) or theme (ETF) strategy described above; pick the 3 best results across all queries

If Tavily is not available, fall back to fetching the source URLs listed below.

## Categories, sources, and article count

Read `data/wiki-categories.md` for the full category list, article count per category, and fallback sources (the "Fallback sources" section). Find exactly the specified number of high-quality, distinct, breaking or trending articles from the last 24–48 hours for each category.

## Blacklisted sources

Never include articles from the following domains. If a URL from any of these domains appears in a source page's link list, skip it.

- reuters.com
- www.reuters.com

## Output file

Save the results to `/raw/url/YYYY-MM-DD-news-aggregation.md` (use today's date).

If a file with that name already exists, create a numbered variant: `YYYY-MM-DD-news-aggregation-2.md`, etc.

Use this exact format:

```markdown
# News Aggregation — YYYY-MM-DD

## 🚀 Technology

- **[Article title]**: [1-sentence description of why this is relevant]
  URL: https://...

- **[Article title]**: [1-sentence description]
  URL: https://...

- **[Article title]**: [1-sentence description]
  URL: https://...

## 📊 Finance

- **[Article title]**: [1-sentence description]
  URL: https://...

...

## ⚡ Productivity

...

## 🧠 Learning

...

## 🩺 Health

...

## 📈 My Holdings

...
```

- Full, raw URLs only — do not mask with anchor text.
- No conversational preamble or closing remarks. Start directly with the `#` header.
- If a source URL fails to fetch, try the next source for that category. If all sources for a category fail, skip that category and note it in the file.

## After saving the file

Append a row to `kbm.log.md`:

```
| YYYY-MM-DD | YYYY-MM-DD-news-aggregation.md | news-fetch |
```

Then stop. The user will run `/kb-scrapecontent` to process the URLs.
