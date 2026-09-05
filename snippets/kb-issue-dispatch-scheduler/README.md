# kb-issue-dispatch Daily Scheduler

Runs `/kb-issue-dispatch` automatically at 10:00 AM every day using macOS launchd.

## How it works

A launchd agent fires `claude -p "/kb-issue-dispatch"` at 10am. The skill fetches any open GitHub issues on `plaktoz/kb` labelled **run skills**, parses their bodies with LLM intent extraction, runs the listed skills in parallel isolated git worktrees, commits any output, opens PRs, comments results, and closes each issue.

To queue work for the next run: open a GitHub issue on `plaktoz/kb`, add the **run skills** label, and write the skills you want in the body (natural language or explicit names both work).

## Setup

### 1. Copy the plist to LaunchAgents

```bash
cp com.plaktoz.kb-issue-dispatch.plist ~/Library/LaunchAgents/
```

### 2. Load it

```bash
launchctl load ~/Library/LaunchAgents/com.plaktoz.kb-issue-dispatch.plist
```

Verify it is registered:

```bash
launchctl list | grep kb-issue-dispatch
# Expected: -  0  com.plaktoz.kb-issue-dispatch
```

### 3. Done

The job fires at 10:00 AM daily. No further action needed unless you want to change the schedule (see below).

## Logs

```bash
# stdout (skill output)
cat /tmp/kb-issue-dispatch.log

# stderr (errors)
cat /tmp/kb-issue-dispatch.err
```

## Common operations

### Test-fire immediately (without waiting for 10am)

```bash
launchctl start com.plaktoz.kb-issue-dispatch
```

### Unload (disable) the job

```bash
launchctl unload ~/Library/LaunchAgents/com.plaktoz.kb-issue-dispatch.plist
```

### Change the schedule

Edit the plist — update `Hour` and/or `Minute` under `StartCalendarInterval` — then reload:

```bash
launchctl unload ~/Library/LaunchAgents/com.plaktoz.kb-issue-dispatch.plist
# edit the file
launchctl load ~/Library/LaunchAgents/com.plaktoz.kb-issue-dispatch.plist
```

### Update the claude binary path

If you reinstall Claude Code and the path changes, update the path in `ProgramArguments` and reload.

Current path: `/Users/plaktoz/.local/bin/claude`

Find it with: `which claude`

## Notes

- The job only fires if the Mac is **on and logged in** at 10am. It does not catch up on missed runs.
- If you want runs to happen even when the Mac is asleep or off, use a GitHub Actions scheduled workflow instead.
- launchd agents (in `~/Library/LaunchAgents/`) run as your user, not root — Claude Code and `gh` auth are available.
