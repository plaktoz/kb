# 1. Base Session Settings
set-option prefix C-a
bind-key C-a send-prefix
set-option mouse on

#open a standard interactive shell
set -g default-command "${SHELL}"

# 2. Inject Your Environment Exports Globally
# set-environment -t "$SESSION_NAME" ANTHROPIC_BASE_URL "https://api.nextgen-beta.ica.ibm.com/ica"

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
