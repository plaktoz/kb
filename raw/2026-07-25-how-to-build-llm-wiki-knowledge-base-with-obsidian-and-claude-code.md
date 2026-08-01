# How to Build an LLM Wiki Knowledge Base with Obsidian and Claude Code

Source: https://www.mindstudio.ai/blog/how-to-build-llm-wiki-knowledge-base-obsidian-claude-code

## The Problem with How We Consume Information

Most people read an article, watch a tutorial, or skim a PDF — and then forget 80% of it within a week. The information disappears, and finding it again means re-reading the same source from scratch.

Building an LLM wiki knowledge base solves this. Instead of passive consumption, you process every piece of content you encounter into structured, searchable, interlinked notes — automatically. Andrej Karpathy has publicly described this kind of system as a core part of how he learns, and with tools like Claude Code and Obsidian, you can build one in an afternoon.

This guide shows you exactly how to do it: ingest YouTube transcripts, PDFs, and web pages, then use Claude Code to synthesize them into a self-growing wiki inside your Obsidian vault.

## What an LLM Wiki Knowledge Base Actually Is

The idea is simple. You have a vault of markdown notes (Obsidian is built for this). Every time you encounter useful content — a video, a research paper, a blog post — an LLM processes it and writes a structured note that fits into your existing knowledge graph.

The “wiki” part matters. Unlike a flat file system or a list of bookmarks, a wiki creates links between concepts. If you’ve already got a note on “attention mechanisms” and you process a new YouTube video on transformers, the new note should reference your existing one. Over time, you get a network of interconnected ideas, not a pile of documents.

## Architecture Overview

Before writing a single line of code, it helps to understand the three layers of this system.

### Layer 1: The Vault (Obsidian)

Obsidian stores everything as local markdown files. This matters for two reasons: Claude Code can read and write them directly without any API integration, and you own your data completely. The vault becomes your “database” of structured notes.

A well-organized vault for an LLM wiki typically uses:

- A Sources/ folder for raw processed content
- A Concepts/ folder for synthesized ideas
- A MOCs/ folder (Maps of Content) for index notes that link related topics
- A consistent frontmatter schema (title, tags, date, source URL)

### Layer 2: The Ingestion Pipeline

This is where Claude Code lives. You point it at a source — a YouTube URL, a PDF file, a web page — and it handles:

1. Extracting the raw text
2. Reading your existing vault to understand context
3. Writing a structured note with links to related concepts
4. Updating relevant MOC notes

### Layer 3: The Growth Loop

The real power comes from iteration. Each new note makes the next one better, because Claude has more context to work with. A note on “RLHF” becomes richer once there are already notes on “reward modeling” and “fine-tuning” linking into it.

## Prerequisites

You don’t need to be a developer to follow this, but you should be comfortable running commands in a terminal.

What you’ll need:

- Obsidian installed with a vault set up
- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Python 3.8+ (for the transcript/PDF extraction scripts)
- `yt-dlp` for YouTube transcript extraction (`pip install yt-dlp`)
- `PyMuPDF` for PDF processing (`pip install pymupdf`)
- An Anthropic API key configured for Claude Code

Optional but useful:

- The Obsidian Dataview plugin for querying your vault
- The Templater plugin for consistent note formatting

## Step 1: Set Up Your Obsidian Vault Structure

Create a new vault or use an existing one. Inside it, create these folders:

```text
/YourVault
  /Sources
    /YouTube
    /PDFs
    /URLs
  /Concepts
  /MOCs
  /Inbox
```

The Inbox/ folder is where Claude will drop new notes before they’re fully integrated. This gives you a review step before anything enters your main knowledge base — useful when you’re starting out and want to check the output quality.

Next, create a _schema.md file at the root of your vault. This is critical. Claude Code will read this file to understand how your notes should be formatted.

### Minimal schema example

```markdown
# Vault Schema

## Note Types

### Source Note
- Frontmatter: title, source_url, date_processed, tags, type: "source"
- Sections: Summary, Key Ideas (bullet list), Quotes, Related Concepts (wikilinks)

### Concept Note
- Frontmatter: title, tags, type: "concept"
- Sections: Definition, Context, Examples, Related Concepts (wikilinks)

### MOC Note
- Frontmatter: title, tags, type: "moc"
- Sections: Overview, Notes in this cluster (wikilinks)

## Linking Rules
- Always use [[wikilink]] syntax to reference other notes
- Prefer linking to Concept notes over Source notes
- If a concept note doesn't exist yet, create it as a stub
```

## Step 2: Write the Extraction Scripts

You need three small scripts to pull raw text from each source type.

### YouTube Transcript Extractor

```python
# extract_youtube.py
import sys
import subprocess
import json

def get_transcript(url):
    result = subprocess.run(
        ['yt-dlp', '--write-auto-sub', '--skip-download', '--sub-format', 'json3', '-o', '/tmp/transcript', url],
        capture_output=True, text=True
    )
    # Parse the downloaded subtitle file
    # Return clean transcript text
    ...

if __name__ == "__main__":
    url = sys.argv[1]
    transcript = get_transcript(url)
    print(transcript)
```

### PDF Extractor

```python
# extract_pdf.py
import sys
import fitz  # PyMuPDF

def extract_pdf(filepath):
    doc = fitz.open(filepath)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    print(extract_pdf(sys.argv[1]))
```

### URL Extractor

```python
# extract_url.py
import sys
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Remove nav, footer, scripts
    for tag in soup(['nav', 'footer', 'script', 'style']):
        tag.decompose()
    return soup.get_text(separator='\n', strip=True)

if __name__ == "__main__":
    print(fetch_page(sys.argv[1]))
```

## Step 3: Write the Claude Code Prompt

Create a file called ingest_prompt.md in your vault root.

```markdown
You are a knowledge base curator. Your job is to process new content and add it to the vault following the schema in _schema.md.

## Your Task
1. Read _schema.md to understand note formatting rules
2. Scan the Concepts/ folder to understand what's already in the vault
3. Read the provided source text
4. Create a Source note in Sources/[type]/ with proper frontmatter
5. Identify 3-5 key concepts from the source
6. For each concept:
   - Check if a Concept note already exists
   - If yes: add a link to the new Source note in the Related section
   - If no: create a stub Concept note
7. Update or create the relevant MOC note
8. Output a summary of what you created/modified

## Source Information
- Type: {type}
- URL/Path: {source}
- Raw Text: {content}

## Important Rules
- Never modify existing note content, only append
- Always use [[wikilink]] syntax
- Keep Source note summaries under 300 words
- Concept notes should be timeless — no dates in the content
```

## Step 4: Automate the Ingestion Workflow

Wrap the process in a single shell script:

```bash
#!/bin/bash
# ingest.sh

VAULT="/path/to/your/vault"
TYPE=$1
SOURCE=$2

case $TYPE in
  youtube)
    CONTENT=$(python "$VAULT/scripts/extract_youtube.py" "$SOURCE")
    ;;
  pdf)
    CONTENT=$(python "$VAULT/scripts/extract_pdf.py" "$SOURCE")
    ;;
  url)
    CONTENT=$(python "$VAULT/scripts/extract_url.py" "$SOURCE")
    ;;
  *)
    echo "Unknown type. Use: youtube, pdf, or url"
    exit 1
    ;;
esac

claude-code \
  --cwd "$VAULT" \
  --prompt "$VAULT/ingest_prompt.md" \
  --var type="$TYPE" \
  --var source="$SOURCE" \
  --var content="$CONTENT"
```

## Step 5: Improve Note Quality Over Time

### Add a Review Step

Route all new notes to Inbox/ first. After a week, you’ll notice patterns in what needs fixing and can update your ingest_prompt.md accordingly.

### Teach Claude Your Vocabulary

Add a glossary.md file to your vault that lists terms you use in a specific way. If you call something “sparse attention” but the source calls it “local attention,” Claude will create two separate concepts instead of linking them.

### Run Periodic Synthesis

Every few weeks, run a synthesis prompt that asks Claude to look across your Concepts folder and identify:

- Concepts that should be merged
- Missing links between related notes
- Concepts that have grown enough to warrant their own MOC

## Step 6: Handle Edge Cases

### Videos Without Transcripts

Some YouTube videos have auto-captions disabled. For these, use yt-dlp to download the audio and process it with a local Whisper model.

### Large PDFs

Academic papers and books can exceed Claude’s context window. Split them first and process each chunk separately, then merge the notes.

### Duplicate Detection

Before creating a new note, Claude should check for duplicates by searching for the source URL in existing frontmatter.

## Where MindStudio Fits Into This Workflow

MindStudio lets you build automated AI workflows without writing infrastructure code. The relevant piece here is its Agent Skills Plugin, which lets AI agents like Claude Code call external capabilities as simple method calls. That can turn a personal tool into a team knowledge base.

## Common Mistakes to Avoid

- Skipping the schema file
- Processing too much too fast
- Not linking back to sources
- Ignoring concept sprawl

## Frequently Asked Questions

- Does this work with private or paywalled content?
- How much does Claude Code cost to run?
- Can I use a different LLM instead of Claude?
- How do I handle content in languages other than English?
- Will this work with audio or video files I record myself?
- How does this compare to tools like Mem or Notion AI?

## Key Takeaways

- An LLM wiki knowledge base pairs Obsidian’s local markdown vault with Claude Code’s file system awareness to build a self-growing network of interconnected notes.
- The schema file is the most important piece — it’s what keeps Claude’s output consistent across hundreds of notes.
- Three extraction scripts plus a single shell script reduce the ingestion workflow to one command.
- Periodic synthesis runs keep the vault clean and prevent concept sprawl.
- For teams, MindStudio can add a no-code trigger layer on top of the same pipeline.
