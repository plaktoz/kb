---
name: kb-scrapecontent
description: Scrape URLs from /raw/url/ files, save clean articles to /raw/, and log activity to kbm.log.md. Use when the user wants to ingest URLs into the knowledge base.
---

# Scrape Content Prompt

You are a web scraping agent with file access. Your job is to extract URL content and save each article as a clean raw markdown file for later processing by the Karpathy-Ingest pipeline.

## Input

Read `.md` files from `/raw/url/`, **excluding any file whose name ends in `.processed.md`**. Two supported formats:

- **Search result / aggregation file** — a structured file with many URLs embedded in the content (e.g. a news aggregation with titles, URLs, and descriptions)
- **Simple URL list** — a plain `.md` file with one URL per line

Extract every URL found across all input files.

## Per-URL Instructions

### 1. Deduplicate

If the same URL appears more than once, process it only once.

### 2. Skip if already scraped

Before fetching, run a fast exact-match check: `grep -rl "source_url: {URL}" raw/ wiki/ 2>/dev/null` (this covers `raw/`, `raw/processed/`, and any `wiki/` note the URL may already have been ingested into). If any match is found, this article has already been scraped and/or ingested — skip it without fetching.

### 3. Fetch and clean

Fetch the URL and extract only:

- Article title
- Byline (author, if present)
- Publication date
- Article body text

Strip everything else: navigation, ads, footers, related articles, cookie banners, comment sections.

### 4. Handle failures

If a URL fails to fetch (404, paywall, timeout, or any error), log the failure to `kbm.log.md` and continue to the next URL. Do not create a file for failed fetches.

### 5. Save the file

Save to `/raw/YYYY-MM-DD-slug.md` where:

- `YYYY-MM-DD` is the article's own publication date (extract from the URL path or article metadata)
- `slug` is the article title converted to lowercase kebab-case

File format:

```md
---
source_url: {URL}
author: {Author or "Unknown"}
date: {YYYY-MM-DD}
---

# {Article Title}

{Clean article body}
```

### 6. Log each scraped file

Append a row to `kbm.log.md` for each successfully saved file:

```md
| YYYY-MM-DD | filename.md | scrape |
```

## After all URLs in a file are processed

1. Rename the source file in `/raw/url/` by inserting `.processed` before `.md` — e.g. `news.md` → `news.processed.md`. Do not delete the file.
2. Append a cleanup row to `kbm.log.md`:

```md
| YYYY-MM-DD | source-filename.processed.md | archive |
```

## Expected outcome

1 URL = 1 file in `/raw/YYYY-MM-DD-slug.md`
