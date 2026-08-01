## Purpose

Defines how URL source files in `raw/url/` are managed after scraping: renaming processed files to prevent re-processing, excluding already-processed files from discovery, and logging the rename action.

## Requirements

### Requirement: URL source files are renamed after scraping
After all URLs in a source file have been processed, the system SHALL rename the source file from `raw/url/<name>.md` to `raw/url/<name>.processed.md` in the same directory. The original file SHALL NOT be deleted.

#### Scenario: Serial scrape renames source file
- **WHEN** the serial scrape skill finishes processing all URLs in a source file
- **THEN** the source file is renamed to `<name>.processed.md` in `raw/url/`

#### Scenario: Parallel scrape renames source files
- **WHEN** the parallel scrape workflow finalize step runs
- **THEN** each source file listed in the discovery result is renamed to `<name>.processed.md`

### Requirement: Processed files excluded from discovery
The system SHALL skip files matching the pattern `*.processed.md` when scanning `raw/url/` for URL source files to process.

#### Scenario: Already-processed file is ignored
- **WHEN** `raw/url/` contains both `news.md` and `news.processed.md`
- **THEN** only `news.md` is read for URLs; `news.processed.md` is ignored

#### Scenario: Empty discovery after all files processed
- **WHEN** all files in `raw/url/` match `*.processed.md`
- **THEN** the scrape step reports zero URLs found and exits without error

### Requirement: Source file cleanup logged as archive
The system SHALL append a row to `kbm.log.md` with activity value `archive` (not `delete`) when a URL source file is renamed after scraping.

#### Scenario: Log row written on rename
- **WHEN** a source file is renamed to `*.processed.md`
- **THEN** `kbm.log.md` receives a row: `| YYYY-MM-DD | <filename> | archive |`
