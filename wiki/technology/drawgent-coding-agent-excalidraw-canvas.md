---
type: literature-note
source_url: https://tangled.org/yanndegat.tngl.sh/drawgent
author: yann.degat
tags: [ai-coding-agents, excalidraw, developer-tools, rust]
date_consumed: 2026-09-27
---

## Summary

Drawgent is a Rust-based tool that connects AI coding agents — [[Claude Code]], Codex, or opencode — to a live [[Excalidraw]] whiteboard, enabling agents to view, edit, and respond to diagrams in real time. Users can issue instructions by writing `AGENT:` annotations directly on the canvas or by using a laser tool to circle elements of interest. The tool bridges the gap between visual, spatial thinking and AI-assisted coding workflows.

## Core Concepts

- **[[Drawgent]]**: Rust CLI that connects an [[AI Coding Agent]] to a live [[Excalidraw]] canvas via [[MCP]] (Model Context Protocol) and [[ACP]] (Agent Communication Protocol).
- **[[Excalidraw]]**: Open-source whiteboard tool; drawgent uses it as both the visual interface and instruction medium for the agent.
- **Canvas Interaction Modes**: Three ways to communicate with the agent — chat panel, inline `AGENT:` annotations on shapes, and laser-zone selection.
- **MCP Canvas Tools**: A set of server-side tools (`get_scene`, `get_screenshot`, `add_elements`, `add_mermaid`, `update_elements`, `delete_elements`, etc.) that the agent invokes to read and mutate the diagram.
- **[[CDP]] (Chrome DevTools Protocol)**: Used for headless Chrome rendering — currently a hard dependency for screenshot capture.
- **Collaborative Room Support**: Agents can join an `excalidraw.com` shared room as a collaborator with end-to-end encrypted traffic.

## Key Takeaways

- **Setup**: Run `drawgent setup <agent>` once; then `drawgent up` starts editor at `127.0.0.1:7300`.
- **Annotation trigger**: `AGENT:` canvas notes fire ~2.5s after typing stops.
- **Laser zones**: Circling elements opens chat with a chip listing covered shapes.
- **Agent modes differ**: Claude Code forks a new ACP session; opencode and Codex attach live.
- **Architecture**: Rust backend handles CLI, ACP driver, scene store, MCP server; React frontend handles editor and renderer.
- **Scene persistence**: Saved to `.drawgent/scene.json`, auto git-ignored.
- **Limits**: Chrome required; Claude attach is a fork not live-session injection; one scene per workspace.

## 🧠 First Principles & Mental Models

- **[[Direct Manipulation]]**: By letting the agent act on a visible, editable canvas rather than text files alone, drawgent applies the direct manipulation principle — the representation of interest (the diagram) is the control surface, reducing the translation cost between intent and action.
- **[[Locality of Reference]]**: Inline `AGENT:` annotations keep instructions co-located with the shapes they describe, minimising context-switching and ambiguity compared to detached chat prompts.

## 🃏 Review Questions

**Q1**: What is the core capability drawgent adds to AI coding agents?
**A**: It connects AI coding agents to a live Excalidraw canvas so they can view, edit, and respond to diagrams in real time, using the whiteboard as both a visual workspace and an instruction medium.

**Q2**: How does the laser-zone interaction mode work?
**A**: The user circles elements on the canvas with Excalidraw's laser tool; this opens the chat panel with a chip listing the covered elements, and the trace clears automatically once the agent finishes responding.

**Q3**: How could a developer use drawgent to improve an architecture review session?
**A**: They could draw a system diagram in Excalidraw, annotate components with `AGENT:` questions or refactor requests, and have the agent edit the diagram and respond inline — keeping all architectural reasoning spatially anchored to the diagram itself.
