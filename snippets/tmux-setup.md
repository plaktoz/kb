Here is the complete setup tool to package your workspace. This includes an automated installer script to handle the file placement and a security strategy to keep your private API keys safe.
## Part 1: The Automated Installer Script (install.sh)
Instead of copying and pasting files manually, you can use this script to build your entire 4-pane system in one click.
Create a file named install.sh and paste this code:

#!/bin/bash

echo "🚀 Starting 4-Pane Tmux Environment Installer..."
# 1. Create the local binary folder if it doesn't exist
mkdir -p "$HOME/bin"
# 2. Write the Tmux layout file (~/.four-panes.tmux)
cat << 'EOF' > "$HOME/.four-panes.tmux"
# Base Session Settings
set-option prefix C-a
bind-key C-a send-prefix
set-option mouse on

# [SECURE] Load environment variables from a private local file instead of hardcoding
if-shell "[ -f ~/.env.tmux ]" "source-file ~/.env.tmux"

# Create the 4-Pane Geometry Layout
split-window -h
select-pane -t 0
split-window -v
select-pane -t 2
split-window -v
select-layout tiled

# Bind a Quick Exit key
bind X kill-session
EOF
echo "✅ Created layout file at ~/.four-panes.tmux"
# 3. Write the startup controller script (~/bin/start-tmux.sh)
cat << 'EOF' > "$HOME/bin/start-tmux.sh"
#!/bin/bash
SESSION_NAME="four-panes"

# Wipe out any old session cleanly
tmux kill-session -t "$SESSION_NAME" 2>/dev/null

# Create the session and load the layout file internally
tmux new-session -d -s "$SESSION_NAME" "tmux source-file \$HOME/.four-panes.tmux; bash"

# Open the session
tmux attach-session -t "$SESSION_NAME"
EOF
# Make the startup script executable
chmod +x "$HOME/bin/start-tmux.sh"
echo "✅ Created executable startup script at ~/bin/start-tmux.sh"
# 4. Safely add the aliases to ~/.zshrc if they aren't already there
ZSHRC="$HOME/.zshrc"
touch "$ZSHRC"
if ! grep -q "alias 4panes=" "$ZSHRC"; then
    echo -e "\n# --- Tmux 4-Pane Workspace Aliases ---" >> "$ZSHRC"
    echo 'alias 4panes="$HOME/bin/start-tmux.sh"' >> "$ZSHRC"
    echo 'alias tmuxkill="tmux kill-server"' >> "$ZSHRC"
    echo "✅ Added '4panes' and 'tmuxkill' aliases to ~/.zshrc"else
    echo "⏭️ Aliases already exist in ~/.zshrc, skipping."fi

echo "🎉 Installation complete! Please run 'source ~/.zshrc' or open a new terminal window."

## How to run the installer:

   1. Save the code into install.sh.
   2. Run chmod +x install.sh to give it permission.
   3. Run ./install.sh.

------------------------------
## Part 2: How to Safely Hide Sensitive Passwords
Notice that in Step 2 of the installer script above, we removed the hardcoded set-environment API_KEY "12345" text. Instead, we added a line that searches for a secret file: if-shell "[ -f ~/.env.tmux ]" "source-file ~/.env.tmux".
This allows you to separate your code from your secrets.
## 1. Create your private secrets file
Create a new file in your home folder that will only live on your local machine:

nano ~/.env.tmux

## 2. Add your secrets inside it

set-environment API_KEY "your_real_super_secret_api_key_here"
set-environment NODE_ENV "development"
set-environment MY_VAR "hello"

Save and close the file.
## 3. Why this protects you

* No accidental leaks: You can safely share your installer script, your ~/.four-panes.tmux layout, or upload your entire project to a public GitHub repository.
* Safe configuration: Your main code files only say "look for a file called ~/.env.tmux". As long as you never upload your personal ~/.env.tmux file to the internet, your secrets stay 100% safe inside your local machine.

If you would like, let me know:

* Do you want to try adding a custom design/theme color to the bottom bar of your Tmux session using the installer?
* Do you want your Zsh history to sync up smoothly across all 4 panes when you run commands?

I can add those refinements directly to your setup files!

## 4. actual files
### four-panes.tmux
```
# 1. Base Session Settings
set-option prefix C-a
bind-key C-a send-prefix
set-option mouse on

# 2. Inject Your Environment Exports Globally
set-environment -t "$SESSION_NAME" ANTHROPIC_BASE_URL "<your claude api url>"
set-environment -t "$SESSION_NAME" ANTHROPIC_MODEL "claude-sonnet-4-6"
set-environment -t "$SESSION_NAME" ANTHROPIC_AUTH_TOKEN "<your api key>"
set-environment -t "$SESSION_NAME" CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS "1"

# 3. Create the 4-Pane Geometry Layout
split-window -h
select-pane -t 0
split-window -v
select-pane -t 2
split-window -v
select-layout tiled

# 4. Bind a "Quick Exit" key just for this setup
# Press Prefix + X inside this session to close it instantly
bind X kill-session
```

### start-tmux.sh 
```
#!/bin/bash
SESSION_NAME="four-panes"

# Wipe out any old session cleanly
tmux kill-session -t "$SESSION_NAME" 2>/dev/null

# Create the session and instantly load the layout file
tmux new-session -d -s "$SESSION_NAME" "tmux source-file ~/bin/four-panes.tmux; bash"

# Open the session
tmux attach-session -t "$SESSION_NAME"
```

### start-vscode-with-claude.sh
To document here as a convenient place to reference
```
export ANTHROPIC_BASE_URL=https://api.nextgen-beta.ica.ibm.com/ica
export ANTHROPIC_MODEL=claude-sonnet-4-6
export ANTHROPIC_AUTH_TOKEN=<your api key>
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1


code -n &%
```


### ~/.zshrc
```
. "$HOME/.local/bin/env"
alias 4panes="~/bin/start-tmux.sh"
alias tmuxkill="tmux kill-server"
alias vsclaude="~/bin/start-vscode-with-claude.sh"
```

### install.sh
```
#!/bin/bash

echo "🚀 Starting 4-Pane Tmux Environment Installer..."

# 1. Create the local binary folder if it doesn't exist
mkdir -p "$HOME/bin"

# 2. Write the Tmux layout file (~/.four-panes.tmux)
cat << 'EOF' > "$HOME/.four-panes.tmux"
# Base Session Settings
set-option prefix C-a
bind-key C-a send-prefix
set-option mouse on

# [SECURE] Load environment variables from a private local file instead of hardcoding
if-shell "[ -f ~/.env.tmux ]" "source-file ~/.env.tmux"

# Create the 4-Pane Geometry Layout
split-window -h
select-pane -t 0
split-window -v
select-pane -t 2
split-window -v
select-layout tiled

# Bind a Quick Exit key
bind X kill-session
EOF
echo "✅ Created layout file at ~/.four-panes.tmux"

# 3. Write the startup controller script (~/bin/start-tmux.sh)
cat << 'EOF' > "$HOME/bin/start-tmux.sh"
#!/bin/bash
SESSION_NAME="four-panes"

# Wipe out any old session cleanly
tmux kill-session -t "$SESSION_NAME" 2>/dev/null

# Create the session and load the layout file internally
tmux new-session -d -s "$SESSION_NAME" "tmux source-file \$HOME/.four-panes.tmux; bash"

# Open the session
tmux attach-session -t "$SESSION_NAME"
EOF

# Make the startup script executable
chmod +x "$HOME/bin/start-tmux.sh"
echo "✅ Created executable startup script at ~/bin/start-tmux.sh"

# 4. Safely add the aliases to ~/.zshrc if they aren't already there
ZSHRC="$HOME/.zshrc"
touch "$ZSHRC"

if ! grep -q "alias 4panes=" "$ZSHRC"; then
    echo -e "\n# --- Tmux 4-Pane Workspace Aliases ---" >> "$ZSHRC"
    echo 'alias 4panes="$HOME/bin/start-tmux.sh"' >> "$ZSHRC"
    echo 'alias tmuxkill="tmux kill-server"' >> "$ZSHRC"
    echo "✅ Added '4panes' and 'tmuxkill' aliases to ~/.zshrc"
else
    echo "⏭️ Aliases already exist in ~/.zshrc, skipping."
fi

echo "🎉 Installation complete! Please run 'source ~/.zshrc' or open a new terminal window."

```