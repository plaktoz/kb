---
name: kb-ingest-pdf
description: Extract content from PDFs in raw/pdf/, save each as a clean markdown file in raw/, then move the PDF to raw/pdf/processed/. Use when the user drops PDFs into the vault for ingestion.
---

# PDF Ingest Skill

You are a PDF extraction agent with file access. Your job is to read PDFs from `raw/pdf/`, extract their text content, and save each as a clean markdown file in `raw/` — ready for the normal ingest pipeline.

## Input

Read all `.pdf` files directly inside `raw/pdf/`. Skip any file already in `raw/pdf/processed/`.

## Per-PDF Instructions

### 1. Skip if already extracted

Before reading, check whether `raw/` or `raw/processed/` already contains a file with a matching `source_file` in its frontmatter. If found, skip it.

### 2. Extract content

Use the `Read` tool to extract the PDF text:

- For PDFs of **20 pages or fewer**: read in a single call with no `pages` parameter.
- For PDFs **longer than 20 pages**: read in 20-page chunks (`pages: "1-20"`, `"21-40"`, etc.) and concatenate all chunks into one body. Do not truncate.

Extract:
- Document title (from first heading or metadata — fall back to the PDF filename slug if absent)
- Author (from byline or metadata — fall back to `"Unknown"`)
- Publication date (from document content or metadata — fall back to today's date)
- Full body text

Strip: page numbers, headers/footers that repeat across pages, and any boilerplate cover-page decoration.

### 3. Save the file

Derive the output filename from the PDF filename:
- Strip the `.pdf` extension
- Convert to lowercase kebab-case
- Prefix with the publication date: `YYYY-MM-DD-slug.md`

Save to `raw/YYYY-MM-DD-slug.md` with this format:

```md
---
source_file: raw/pdf/{original-filename}.pdf
author: {Author or "Unknown"}
date: {YYYY-MM-DD}
---

# {Document Title}

{Full extracted body text}
```

### 4. Move the PDF

After successfully saving the markdown file, move the original PDF to `raw/pdf/processed/{original-filename}.pdf`.

### 5. Log each extracted file

Append a row to `kbm.log.md` for each successfully saved file:

```
| YYYY-MM-DD | YYYY-MM-DD-slug.md | scrape |
```

### 6. Handle failures

If a PDF fails to read (corrupt file, unreadable, etc.), log the failure to `kbm.log.md` with activity `scrape-failed` and continue to the next file. Do not create a markdown file for failures.

## Expected outcome

1 PDF = 1 file in `raw/YYYY-MM-DD-slug.md`, original PDF moved to `raw/pdf/processed/`.

## Next step

The extracted files in `raw/` are ready for `/kb-ingest` or `/kb-ingest-parallel`.
