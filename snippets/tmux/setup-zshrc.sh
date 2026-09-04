# ==========================================
# 🚀 PATH CONFIGURATION
# ==========================================

# Homebrew setup (handles both Apple Silicon M1/M2/M3 and Intel Macs)
if [[ -f /opt/homebrew/bin/brew ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
elif [[ -f /usr/local/bin/brew ]]; then
    eval "$(/usr/local/bin/brew shellenv)"
fi

# ==========================================
# 🛠️ QUALITY OF LIFE & TERMINAL OPTIONS
# ==========================================

# Enable interactive completion features
autoload -Uz compinit && compinit

# Case-insensitive autocomplete matching (type 'cd dev' to get 'Developer')
zstyle ':completion:*' matcher-list 'm:{a-zA-z}={A-Za-z}'

# Save a massive command history across sessions
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt SHARE_HISTORY      # Share history across all open terminal windows
setopt HIST_IGNORE_DUPS   # Don't record duplicate consecutive entries

# ==========================================
# 💡 CUSTOM ALIASES
# ==========================================

# Navigation shortcuts
alias dev="cd ~/Developer"
alias kbdir="cd ~/Developer/kb"
alias vsclaude="~/bin/start-vscode-with-claude.sh"
alias 4panes="~/bin/start-tmux.sh"

alias .zsh="nano ~/.zshrc"
alias reload="source ~/.zshrc"

# Safety nets & enhancements
alias ll="ls -lahG"       # List all files with sizes, permissions, and colors
alias rm="rm -i"          # Ask for confirmation before deleting files
alias mkdir="mkdir -p"    # Create nested directories safely

# Git shortcuts
alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gp="git push"
