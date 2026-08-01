## 1. Serial skill — skills/Scrape-content-prompt.md

- [x] 1.1 Input section: add exclusion note so `*.processed.md` files are skipped during URL discovery
- [x] 1.2 After-all-URLs section: replace "Delete the source file" instruction with rename to `<name>.processed.md`
- [x] 1.3 After-all-URLs section: change log activity in the example row from `delete` to `archive`

## 2. Parallel workflow — .claude/workflows/kb-scrapecontent-parallel.js

- [x] 2.1 Discover agent prompt (line ~35): add instruction to exclude files matching `*.processed.md`
- [x] 2.2 Finalize agent prompt (line ~103): replace "Delete these source URL files" with rename instruction (`<name>.md` → `<name>.processed.md`)
- [x] 2.3 Finalize agent prompt: change log activity in step 3 from `delete` to `archive`
