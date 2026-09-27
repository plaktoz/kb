---
source_url: https://tangled.org/yanndegat.tngl.sh/drawgent
author: yann.degat
date: 2026-09-27
---

# drawgent: Your Coding Agent on a Live Excalidraw Canvas

**drawgent** is a Rust-based tool that bridges your own AI coding agent (Claude Code, Codex, or opencode) to a live Excalidraw whiteboard. The agent can view the canvas via screenshot, edit diagrams in real time, and respond to inline instructions written directly on the canvas.

## Setup & Launch

- Run `drawgent setup <agent>` once to verify CLI installation, login status, ACP bridge, and headless Chrome availability.
- `drawgent up` starts a local editor at `127.0.0.1:7300`, launches an agent session, and opens your browser.
- `drawgent up --attach` connects to an already-running agent session.

## Canvas Interaction Modes

1. **Chat panel** — send requests, stream replies, approve permissions, or stop a turn.
2. **AGENT: notes** — write `AGENT: …` on the canvas near a shape; fires ~2.5s after you stop typing.
3. **Laser zones** — use Excalidraw's laser tool to circle elements; the chat panel opens with a chip listing covered elements, and the trace clears when the agent finishes.

## excalidraw.com Room Support

Connect via `--room 'https://excalidraw.com/#room=...'` so the agent joins as a collaborator with end-to-end encrypted traffic.

## Agent Attach Modes by Tool

| Agent | Discovery | Mode |
|---|---|---|
| Claude Code | `claude agents --json` | Fork (new ACP session) |
| opencode | Local HTTP servers | Live (messages appear in your TUI) |
| Codex | `~/.codex/sessions` | Live (`codex queue`) |

## MCP Canvas Tools

`get_scene`, `get_screenshot`, `add_elements`, `add_mermaid`, `update_elements`, `delete_elements`, `clear_canvas`, `list_instructions`, `resolve_instruction`, `set_status`

## Architecture

- **Rust** (`src/`): CLI, setup, ACP driver, scene store, CDP-based Chrome renderer, MCP server, room client
- **Web** (`web/`): React editor (`main.jsx`, `chat.jsx`, `laser.js`) and renderer page
- Scene persisted to `.drawgent/scene.json` (auto git-ignored)

## Notable Limits

- Chrome is required for rendering (native renderer planned)
- Claude "attach" is a fork, not injection into a live terminal session
- One scene per workspace; images/files are not synced
