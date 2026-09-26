# Mission: pstack for Development

## Why
A seasoned engineer using AI agents today still spends significant time re-orienting agents, accepting low-quality outputs, and losing context across sessions. pstack is a structured skill system that changes this: it routes tasks to the right workflow automatically, demands real verification rather than green builds, and — critically — improves itself over time through the `/reflect` loop. The outcome is an AI agent that behaves more like a reliable senior engineer and less like a context-amnesiac.

## Success looks like
- Installing and configuring pstack-claude in Claude Code and writing a correct `Done means` condition on the first attempt
- Recognising which pstack skill to invoke for any given development signal without consulting the docs
- Running `/arena` on a non-trivial design decision and synthesising a winning artifact from N candidates
- Running `/reflect` after a complex session and getting at least one approved skill edit that improves future agent behaviour
- Designing an overnight autonomous run with explicit done conditions, a decision log, and a rollback guard

## Constraints
- Learning from the pstack-claude port and associated SKILL.md definitions — not from a live Cursor installation
- Self-paced, one lesson at a time

## Out of scope
- Cursor-specific UI automations (deslop, control-cli, control-ui) not ported to pstack-claude
- Benny / software-factory automation (experimental, not production-ready)
- Graphite CLI stack management (shipping playbook dependency)
