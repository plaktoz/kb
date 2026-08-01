## Purpose

Defines the archive and cleanup behaviour for the YouTube transcript pipeline: how processed video folders and URL source files are renamed/moved, how already-processed assets are excluded from re-runs, and how cleanup actions are logged.

## Requirements

### Requirement: Video folders moved to processed subdirectory after ingest
After ingestion, the system SHALL move each video folder from `youtube-transcript/<channel>/<video>/` to `youtube-transcript/processed/<channel>/<video>/`, preserving the channel hierarchy.

#### Scenario: Video folder moved with hierarchy preserved
- **WHEN** the archive phase runs after successful ingest
- **THEN** each video folder is moved to `youtube-transcript/processed/<channel>/<video>/` and no longer exists at its original path

#### Scenario: Processed directory created if absent
- **WHEN** `youtube-transcript/processed/<channel>/` does not yet exist
- **THEN** the directory is created before the move

### Requirement: YouTube URL source files renamed after processing
After all URLs in a source file have been processed, the system SHALL rename the source file from `raw/youtube/<name>.md` to `raw/youtube/<name>.processed.md`. The original file SHALL NOT be deleted.

#### Scenario: Source file renamed on successful pipeline run
- **WHEN** the archive phase runs after ingest
- **THEN** each source file in `raw/youtube/` is renamed to `<name>.processed.md`

#### Scenario: Source file renamed on early exit (no transcripts staged)
- **WHEN** the pipeline exits early because no transcripts were found to stage
- **THEN** source files in `raw/youtube/` are still renamed to `<name>.processed.md`

### Requirement: Processed assets excluded from discovery on re-run
The system SHALL skip already-processed assets during discovery so that subsequent pipeline runs do not re-process them.

#### Scenario: Processed URL files excluded from YouTube URL discovery
- **WHEN** the Discover phase scans `raw/youtube/` for URL source files
- **THEN** files matching `*.processed.md` are ignored

#### Scenario: Processed video folders excluded from Stage transcript search
- **WHEN** the Stage phase scans `youtube-transcript/` for `transcript.md` files
- **THEN** files inside `youtube-transcript/processed/` are ignored

### Requirement: Cleanup logged as archive
The system SHALL append a row to `kbm.log.md` with activity value `archive` (not `delete`) for each asset cleaned up during the archive phase.

#### Scenario: Log row written for renamed source file
- **WHEN** a source URL file is renamed to `*.processed.md`
- **THEN** `kbm.log.md` receives a row: `| YYYY-MM-DD | <new-filename> | archive |`

#### Scenario: Log row written for moved video folder
- **WHEN** a video folder is moved to `youtube-transcript/processed/`
- **THEN** `kbm.log.md` receives a row: `| YYYY-MM-DD | <video-folder-name> | archive |`
