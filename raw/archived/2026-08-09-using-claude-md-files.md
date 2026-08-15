# Using CLAUDE.md Files: Customizing Claude Code for Your Codebase

Source: https://claude.com/blog/using-claude-md-files

## What is a CLAUDE.md File?

A CLAUDE.md file is a project-specific configuration file that provides Claude with persistent context. It's automatically incorporated into every conversation, eliminating repeated explanations of architecture, conventions, and workflows.

**Placement options:**
- Repository root (shared with team)
- Parent directories (for monorepos)
- Home folder (universal application)

**What to include:**
- Common bash commands
- Code style guidelines
- Testing instructions
- Repository conventions
- Developer environment setup
- Project-specific warnings

---

## Getting Started with /init

Run `/init` in any Claude Code session to auto-generate a starter CLAUDE.md:

```bash
cd your-project
claude
/init
```

Claude analyzes your codebase and generates a tailored file. Review the output, add workflow-specific instructions, remove irrelevant content, and commit to version control.

---

## Structuring Your CLAUDE.md

### 1. Give Claude a Map
Include a project summary and directory structure so Claude understands where components live and can make better decisions about code location.

### 2. Connect Claude to Your Tools
Document custom tools with usage examples. Claude supports MCP (Model Context Protocol) servers for extended capabilities.

### 3. Define Standard Workflows
Prompt Claude to think before acting by defining workflows. A solid default addresses four questions:
1. Does this require investigation first?
2. Is a detailed plan needed before implementation?
3. What information is missing?
4. How will effectiveness be tested?

---

## Additional Tips

| Technique | Purpose |
|-----------|---------|
| `/clear` | Reset context between distinct tasks |
| Subagents | Isolate context for distinct phases (e.g., implementation vs. security review) |
| Custom slash commands | Store repetitive prompts as `.claude/commands/*.md` files |

Custom commands support arguments via `$ARGUMENTS` or `$1`, `$2` placeholders. Ask Claude to generate command files for you directly.

---

## Key Principles

- **Keep it concise** — the file loads every session; verbose files waste context
- **Never include secrets** — no API keys, credentials, or connection strings
- **Break up large files** — reference separate markdown files from within CLAUDE.md
- **Iterate over time** — treat it as living documentation, not a one-time setup

The most effective CLAUDE.md files solve *real* problems: documenting repeated commands, capturing architectural context, and establishing workflows that prevent rework.
