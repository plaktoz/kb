# herdr Setup & Reference (macOS · One Dark)

Everything needed to install herdr, apply the One Dark "beast mode" config, and use it day to day.

**Contents**
1. [Installation](#1-installation)
2. [Mac settings](#2-mac-settings)
3. [Cheat sheet](#3-cheat-sheet)
4. [One Dark config.toml](#4-one-dark-configtoml)

---

## 1. Installation

```bash
# herdr + the extra tools this config uses
brew install herdr terminal-notifier lazygit btop yazi
# if brew can't find herdr:
#   curl -fsSL https://herdr.dev/install.sh | sh

# put the config in place (paste section 4 into this file)
mkdir -p ~/.config/herdr
nano ~/.config/herdr/config.toml

# start herdr
herdr
```

**Everyday commands**

```bash
herdr                           # start, or re-attach to a running session
herdr server reload-config      # apply config changes (or Ctrl+b then Shift+r)
herdr --default-config          # print the full default config
herdr update                    # update (only if installed with the curl script)
brew upgrade herdr              # update (if installed with Homebrew)
```

If herdr shows a warning when it starts, that one setting falls back to its default and the rest still works.
Logs are in `~/.config/herdr/herdr.log`.

## 2. Mac settings

- **Option key:** the `Alt` shortcuts need "Use Option as Meta/Alt" turned on in your
  terminal (iTerm2 / Terminal.app: Settings → Profiles → Keyboard).
- **Mission Control:** if `Ctrl+Alt+arrows` do nothing, macOS may be using them.
  Check System Settings → Keyboard → Keyboard Shortcuts → Mission Control.
- **Terminal:** Ghostty, iTerm2 or WezTerm show the colors best.

---

## 3. Cheat sheet

**Prefix = `Ctrl+b`**: press it, let go, then press the next key.
Below, "`b` then `v`" means `Ctrl+b`, then `v`.

## Must-know

| Keys | Does |
|---|---|
| `b` then `?` | Show every shortcut |
| `b` then `g` | Jump to any workspace, tab or agent |
| `b` then `o` | Go straight to the agent that just notified you |
| `b` then `z` | Make the current pane full-screen (press again to undo) |
| `b` then `t` | Scratch terminal pop-up (`exit` to close) |

## Agents

| Keys | Does |
|---|---|
| `Ctrl+Alt+↓` / `Ctrl+Alt+↑` | Next / previous agent (no prefix) |
| `b` then `Alt+1…9` | Jump to agent 1–9 |

Sidebar status colors: **red** = blocked (needs you) · **yellow** = working · **green** = done · **grey** = idle

## Panes (splits inside a tab)

| Keys | Does |
|---|---|
| `b` then `v` | Split side by side |
| `b` then `-` | Split stacked |
| `b` then `h` `j` `k` `l` | Move to the pane left / down / up / right |
| `b` then `Shift+h/j/k/l` | Swap the pane in that direction |
| `b` then `Tab` / `Shift+Tab` | Cycle through panes |
| `` b then ` `` | Back to the last pane you used |
| `Ctrl+Shift+Alt+arrows` | Resize the pane (no prefix) |
| `b` then `r` | Resize mode (arrows, then `Esc`) |
| `b` then `x` | Close the pane |
| `b` then `Shift+p` | Rename the pane |

## Tabs

| Keys | Does |
|---|---|
| `b` then `c` | New tab |
| `b` then `1…9` | Go to tab 1–9 |
| `b` then `n` / `p`, or `Ctrl+Alt+→` / `Ctrl+Alt+←` | Next / previous tab |
| `b` then `Shift+t` | Rename the tab |
| `b` then `Shift+x` | Close the tab |

## Workspaces (one per project)

| Keys | Does |
|---|---|
| `b` then `Shift+n` | New workspace |
| `b` then `Shift+1…9` | Go to workspace 1–9 |
| `b` then `w` | Workspace picker (`↑`/`↓` to choose, `h` `j` `k` `l` to pick a pane) |
| `b` then `Shift+w` | Rename the workspace |
| `b` then `Shift+d` | Close the workspace |
| `b` then `Shift+g` | New git worktree from this workspace |

## Pop-up tools

| Keys | Opens | To close |
|---|---|---|
| `b` then `t` | Scratch terminal | `exit` or `Ctrl+d` |
| `b` then `Alt+g` | lazygit (commit, push, diffs) | `q` |
| `b` then `m` | btop (CPU, memory, processes) | `q` |
| `b` then `f` | yazi (file manager) | `q` (`Q` = quit without saving the folder) |

> **Stuck in a pop-up?** `Esc` goes to the tool, not to herdr, so it only cancels a
> search or selection inside the tool. Press `Esc` once to clear, then `q`
> (or `Ctrl+c`) to quit the tool, and the pop-up closes.

## Copy and scrollback

| Keys | Does |
|---|---|
| `b` then `[` | Copy mode (select text with the keyboard) |
| `b` then `e` | Open the pane's history in your editor to search it |
| Drag with the mouse | Copies automatically |
| `Ctrl`+click | Open a link |

## Layout and session

| Keys | Does |
|---|---|
| `b` then `b` | Hide or show the sidebar |
| `b` then `s` | Settings |
| `b` then `Shift+r` | Reload the config after editing |
| `b` then `q` | Detach (everything keeps running; type `herdr` to come back) |

**Daily flow:** one workspace per project, one agent per tab. When a notification
arrives, press `b` then `o`, deal with it, and use `` b then ` `` to jump back.

---

## 4. One Dark config.toml

Save as `~/.config/herdr/config.toml`, then run `herdr server reload-config`.
Colors come from the [akamud One Dark](https://marketplace.visualstudio.com/items?itemName=akamud.vscode-theme-onedark) VS Code theme.

```toml
# ─────────────────────────────────────────────────────────────
#  herdr — BEAST MODE (macOS, One Dark, productivity)
#  Location: ~/.config/herdr/config.toml
#  Apply live: herdr server reload-config   (or prefix+shift+r)
#  Help overlay with every active key: prefix+?
# ─────────────────────────────────────────────────────────────

# ── Theme: One Dark (akamud/vscode-theme-onedark palette) ───
[theme]
name = "catppuccin"            # herdr has no built-in One Dark, so every
auto_switch = false            # colour below is overridden to One Dark's

[theme.custom]
panel_bg      = "#282c34"      # editor background
sidebar_bg    = "#21252b"      # sidebar background
active_row_bg = "#2c313a"      # list active selection
selection_bg  = "#3e4451"      # editor selection
surface0      = "#333842"      # activity bar
surface1      = "#3e4451"      # selection
surface_dim   = "#21252b"      # sidebar / status bar
overlay0      = "#5c6370"      # comment grey
overlay1      = "#636d83"      # line numbers
text          = "#abb2bf"      # foreground
subtext0      = "#636d83"      # secondary labels
accent        = "#528bff"      # focus border blue
mauve         = "#c678dd"      # purple
blue          = "#61afef"      # blue
teal          = "#56b6c2"      # cyan
green         = "#98c379"      # green  → done
yellow        = "#e5c07b"      # yellow → working
peach         = "#d19a66"      # orange
red           = "#e06c75"      # red    → blocked

# ── Shell / panes ────────────────────────────────────────────
[terminal]
shell_mode = "auto"            # login shells on macOS → Homebrew PATH works
new_cwd    = "follow"          # new panes open where you already are

[advanced]
scrollback_limit_bytes = 50000000   # 50 MB per pane (default 10 MB)

[session]
resume_agents_on_restore = true

# ── UI: dashboard-first layout ───────────────────────────────
[ui]
accent                  = "#528bff"
sidebar_width           = 32
sidebar_max_width       = 42
status_indicators       = "symbols"   # shape + color per agent state
agent_panel_sort        = "priority"  # blocked agents float to the top
pane_borders            = "always"
show_agent_labels_on_pane_borders = true
prompt_new_workspace_name = true
prompt_new_tab_name     = true
mouse_scroll_lines      = 5
tab_bar_position        = "top"
window_title            = "🐑 {workspace} › {tab}"
tab_bar_right_separator = "  │  "
tab_bar_right = [
  { type = "zoom" },
  { type = "command", command = "pmset -g batt | grep -Eo '[0-9]+%' | head -1 | sed 's/^/🔋 /'", interval_seconds = 60, timeout_seconds = 2 },
  { type = "command", command = "git -C \"$HERDR_ACTIVE_PANE_CWD\" branch --show-current 2>/dev/null | sed 's/^/⎇ /'", interval_seconds = 5, timeout_seconds = 2 },
  { type = "datetime", format = "%a %d %b  %H:%M" },
]

# Colorful agent rows: state text changes color by status
[ui.sidebar.agents]
row_gap = 1
rows = [
  ["state_icon",
   { token = "agent", fg = "#c678dd", bold = true },
   { token = "state_text", rules = [
       { equals = "blocked", fg = "#e06c75", bold = true },
       { equals = "working", fg = "#e5c07b" },
       { equals = "done",    fg = "#98c379", bold = true },
       { equals = "idle",    fg = "#5c6370" },
   ] }],
  [{ token = "workspace", fg = "#61afef" }, { token = "tab", fg = "#56b6c2" }],
  [{ token = "terminal_title_stripped", fg = "#5c6370" }],
]

[ui.sidebar.spaces]
row_gap = 0
rows = [
  ["state_icon", { token = "workspace", fg = "#c678dd", bold = true }],
  [{ token = "branch", fg = "#d19a66" }, "git_status"],
]

# ── Notifications: know the moment an agent needs you ────────
[ui.toast]
delivery      = "system"       # macOS Notification Center (install terminal-notifier)
delay_seconds = 1

[ui.toast.clipboard]
enabled  = true
position = "bottom-center"

[ui.sound]
enabled = true

# ── Keys: tmux-style prefix + fast direct chords ─────────────
[keys]
prefix = "ctrl+b"

# splits: v = side-by-side, - = stacked
split_vertical   = "prefix+v"
split_horizontal = "prefix+minus"
zoom             = "prefix+z"

# jump anywhere
goto             = "prefix+g"
switch_tab       = "prefix+1..9"
switch_workspace = "prefix+shift+1..9"
focus_agent      = "prefix+alt+1..9"
last_pane        = "prefix+backtick"

# no-prefix power moves (need Option-as-Alt in your terminal)
next_agent        = "ctrl+alt+down"
previous_agent    = "ctrl+alt+up"
next_tab          = ["prefix+n", "ctrl+alt+right"]
previous_tab      = ["prefix+p", "ctrl+alt+left"]
resize_pane_left  = "ctrl+shift+alt+left"
resize_pane_down  = "ctrl+shift+alt+down"
resize_pane_up    = "ctrl+shift+alt+up"
resize_pane_right = "ctrl+shift+alt+right"

# ── Popup tools (brew install lazygit btop yazi) ─────────────
[[keys.command]]
key = "prefix+t"
type = "popup"
command = "exec \"${SHELL:-sh}\""
description = "scratch terminal"
width = "80%"
height = "80%"

[[keys.command]]
key = "prefix+alt+g"
type = "popup"
command = "lazygit"
description = "lazygit"
width = "90%"
height = "90%"

[[keys.command]]
key = "prefix+m"
type = "popup"
command = "btop"
description = "system monitor"
width = "90%"
height = "85%"

[[keys.command]]
key = "prefix+f"
type = "popup"
command = "yazi"
description = "file manager"
width = "85%"
height = "85%"
```

---

**Sources:** [herdr docs](https://herdr.dev/docs/) · [Config reference](https://herdr.dev/docs/config-reference/) · [One Dark theme source](https://github.com/akamud/vscode-theme-onedark)
