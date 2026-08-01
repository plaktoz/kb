## 1. Discovery exclusions

- [x] 1.1 Discover agent prompt (line ~66): add exclusion for `*.processed.md` when reading `raw/youtube/` URL source files
- [x] 1.2 Stage agent prompt (line ~134): add exclusion for `youtube-transcript/processed/` when searching for `transcript.md` files

## 2. Early-exit cleanup (line ~167)

- [x] 2.1 Replace "Delete these source YouTube URL files" with rename to `*.processed.md`
- [x] 2.2 Change log activity in that agent prompt from `delete` to `archive`

## 3. Archive phase — folder cleanup (line ~229)

- [x] 3.1 Replace "Delete these youtube-transcript video folders" with move to `youtube-transcript/processed/<channel>/<video>/` preserving hierarchy
- [x] 3.2 Add log row instruction for each moved folder: `| YYYY-MM-DD | <video-folder-name> | archive |`

## 4. Archive phase — source URL cleanup (line ~232)

- [x] 4.1 Replace "Delete these source YouTube URL files" with rename to `*.processed.md`
- [x] 4.2 Change log activity from `delete` to `archive`
