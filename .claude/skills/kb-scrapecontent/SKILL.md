---
name: kb-scrapecontent
description: Scrape URLs from /raw/url/ files, save clean articles to /raw/, and log activity to kbm.log.md. Use when the user wants to ingest URLs into the knowledge base.
---

# Scrape Content Prompt

You are a web scraping agent with file access. Your job is to extract URL content and save each article as a clean raw markdown file for later processing by the Karpathy-Ingest pipeline.

Finding URLs, skipping ones already in the vault, detecting blocked pages, logging and archiving are done by `scripts/scrape_queue.py`, not by hand. Your part is turning each probed page into a clean article file.

## 1. Build the queue

```bash
python3 .claude/skills/kb-scrapecontent/scripts/scrape_queue.py discover
```

This reads every `raw/url/*.md` file that does not end in `.processed.md`, extracts and de-duplicates the URLs, drops any whose `source_url` already exists in `raw/` or `wiki/`, and fetches the rest with a hard timeout. It finishes in seconds and prints a summary whose `queue` field is the path of a fresh queue file for this run. The queue file holds one item per URL with a `verdict`, a `reason`, and, when available, `title`, `author`, `published` and `text_path`.

If `toScrape` is 0, skip to step 3 with an empty rows list.

## 2. Scrape each item

Read the queue file. For each item, the verdict decides the only source you may use:

| verdict | what to do |
|---|---|
| `ok` | Read the file at `text_path`. It already holds the article text. Do not fetch the URL. If the file is clearly not the article (an index page, cookie wall, a few stray lines), treat the item as `blocked`. |
| `blocked`, `paywall`, `thin`, `unreachable` | Make exactly one `mcp__tavily__tavily_extract` call for the URL. If it returns the article body (several paragraphs of real prose, not a teaser, subscribe prompt or challenge page), use it. Otherwise record `scrape-failed` with the reason and move on. |
| `dead` | Record `scrape-failed` with the reason. No fetch. |

Do not try WebFetch, curl, other MCP scrapers, search engines or archive sites for a URL the probe could not read. The probe already established that direct access fails, and each extra attempt costs minutes.

Save each article to `raw/YYYY-MM-DD-slug.md` where:

- `YYYY-MM-DD` is the article's own publication date (the probe's `published`, the URL path, or the text). If no reliable date exists, use today's date. Never guess.
- `slug` is the article title converted to lowercase kebab-case. If that file already exists for a different URL, append `-2`.

```md
---
source_url: {URL}
author: {Author or "Unknown"}
date: {YYYY-MM-DD}
---

# {Article Title}

{Clean article body}
```

The body keeps the article's own paragraphs and headings in order. Strip navigation, ads, promo banners, newsletter signups, related or "most popular" link lists, author bios and comments. Do not summarize or add anything that is not in the source.

Collect one row per item: `{"filename": "<saved basename>", "activity": "scrape"}` for a save, or `{"filename": "<URL> (<reason>)", "activity": "scrape-failed"}` for a failure.

## 3. Finalize

Write the rows as a JSON list to `rows.json` next to the queue file, then run:

```bash
python3 .claude/skills/kb-scrapecontent/scripts/scrape_queue.py finalize <queue> <dir of queue>/rows.json
```

This appends the `scrape` / `scrape-failed` rows to `kbm.log.md`, renames each source file in `raw/url/` to `*.processed.md`, and logs one `archive` row per file. It is safe to rerun. Do not edit `kbm.log.md` or rename files in `raw/url/` by hand.

## Expected outcome

1 URL = 1 file in `/raw/YYYY-MM-DD-slug.md`, or 1 `scrape-failed` row that names the reason.
