Two ways to ingest a transcript

Option A — Full pipeline (recommended)

Put the YouTube URL in raw/youtube/queue.md, then run /kb-ingest-transcript. It downloads the transcript, post-processes speaker IDs, stages to raw/, ingests into wiki, and archives.

Option B — Manual file drop (you already have the text)

If you have the transcript content already, create a file directly in raw/ using this format, then run /kb-ingest:

# Video Title Here

source_url: https://www.youtube.com/watch?v=XXXX
author: Channel Name

---

Transcript body goes here...

**Speaker A:** This is what they said.

**Speaker B:** And the response.

---

Required fields

┌─────────────┬─────────────┬─────────────────────────────────────────────────────────────────┐
│    Field    │  Required   │                              Notes                              │
├─────────────┼─────────────┼─────────────────────────────────────────────────────────────────┤
│ source_url: │ Yes         │ Must be present — /kb-ingest uses this to find and dedupe files │
├─────────────┼─────────────┼─────────────────────────────────────────────────────────────────┤
│ author:     │ Recommended │ Maps to the wiki note's author frontmatter                      │
└─────────────┴─────────────┴─────────────────────────────────────────────────────────────────┘

The title (# H1) becomes the wiki note slug. The source_url: and author: lines sit between the title and the --- separator — they are not YAML frontmatter, just plain key-value lines that the ingest prompt knows to parse.

Option B is the right path if you exported a transcript from another tool, pasted it from YouTube's auto-captions, or have a .txt from an external service — just drop it into raw/ with those two header lines and /kb-ingest handles the rest.