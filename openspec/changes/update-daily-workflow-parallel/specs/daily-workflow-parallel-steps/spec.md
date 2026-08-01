## ADDED Requirements

### Requirement: Daily pipeline uses parallel scrape workflow
The daily pipeline skill SHALL invoke the `kb-scrapecontent-parallel` Workflow instead of executing the serial scrape skill inline.

#### Scenario: Parallel scrape invoked in Step 2
- **WHEN** the daily pipeline reaches Step 2
- **THEN** the Workflow tool is called with `name: "kb-scrapecontent-parallel"` and execution waits for it to complete before continuing

### Requirement: Daily pipeline uses parallel ingest workflow
The daily pipeline skill SHALL invoke the `kb-ingest-parallel` Workflow instead of executing the serial ingest skill inline.

#### Scenario: Parallel ingest invoked in Step 3
- **WHEN** the daily pipeline reaches Step 3
- **THEN** the Workflow tool is called with `name: "kb-ingest-parallel"` and execution waits for it to complete before continuing

### Requirement: Error resilience preserved
The daily pipeline SHALL continue to subsequent steps even if a parallel workflow step fails, collecting errors for the end-of-run summary.

#### Scenario: Pipeline continues after workflow failure
- **WHEN** a parallel workflow step fails or returns an error
- **THEN** the error is noted and the pipeline proceeds to the next step
