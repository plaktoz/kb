## Context

`skills/Daily-workflow-prompt.md` is a sequential prompt executed by Claude. It chains four steps: News → Scrape → Ingest → Newsletter. Steps 2 and 3 currently tell Claude to read a serial skill file and execute it inline. The parallel equivalents are registered Workflow scripts (`kb-scrapecontent-parallel`, `kb-ingest-parallel`) that fan out up to 8 concurrent agents each.

## Goals / Non-Goals

**Goals:**
- Replace serial step 2 and step 3 with Workflow tool invocations of the parallel equivalents
- Keep the same sequential structure, error-resilience, and end-of-run summary format

**Non-Goals:**
- No changes to Step 1 (news agent) or Step 4 (newsletter) — these have no parallel equivalents
- No changes to the summary format or error handling logic
- No changes to the parallel workflow scripts themselves

## Decisions

**Direct Workflow invocation vs. referencing parallel skill files**
The parallel skill files (`.claude/skills/kb-scrapecontent-parallel/SKILL.md`, `.claude/skills/kb-ingest-parallel/SKILL.md`) each contain a single line: "Run the Workflow tool with `name: ...`". Calling them via "Read and execute" adds a layer of indirection with no benefit. The daily workflow prompt should invoke the Workflow tool directly — same result, one fewer hop.

**Reporting language**
The current steps say "execute the instructions exactly as written" which implies inline execution. The replacement language should say "run... wait for it to complete... then continue" to make the async handoff to the Workflow tool explicit.

## Risks / Trade-offs

- **Workflow tool unavailability** → If the Workflow tool is not available in the execution context, the step will fail. Same failure mode as before (serial skill could also fail). Error is collected and pipeline continues per the existing error-resilience policy.
- **Summary counts** → Parallel workflows return structured result objects (`{ scraped, failed }` / `{ ingested }`). The end-of-run summary template expects counts — Claude should extract these from the workflow result.
