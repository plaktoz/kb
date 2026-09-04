#!/bin/bash
source ~/bin/config.sh

SESSION_NAME="four-panes"

# Wipe out any old session cleanly
tmux kill-session -t "$SESSION_NAME" 2>/dev/null

# Load the variables
source ~/bin/config.sh

# Create the session and instantly load the layout file
tmux new-session -d -s "$SESSION_NAME" "tmux source-file ~/bin/four-panes.tmux; bash"

# Open the session
tmux attach-session -t "$SESSION_NAME"
