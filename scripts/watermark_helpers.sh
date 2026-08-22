#!/usr/bin/env bash
#
# Native iTerm2 Shell Functions for Badges, Headlines, Colors, and Titles.
# Sourcing this file (`source scripts/watermark_helpers.sh`) provides instant commands
# that work directly in any iTerm2 pane using OSC escape sequences without requiring the Python API.
#

# Set watermark badge text in the current pane
iterm_badge() {
    local text="$1"
    if [ -z "$text" ]; then
        echo "Usage: iterm_badge <text>"
        return 1
    fi
    local b64
    b64=$(printf "%s" "$text" | base64 | tr -d '\n')
    printf "\e]1337;SetBadgeFormat=%s\a" "$b64"
    echo "Badge set to '$text'"
}

# Clear watermark badge in the current pane
iterm_clear_badge() {
    printf "\e]1337;SetBadgeFormat=\a"
    echo "Badge cleared"
}

# Set tab / window title
iterm_title() {
    local title="$1"
    if [ -z "$title" ]; then
        echo "Usage: iterm_title <title>"
        return 1
    fi
    printf "\e]0;%s\a" "$title"
}

# Set tab background color (RGB 0-255)
iterm_tab_color() {
    local r="$1"
    local g="$2"
    local b="$3"
    if [ -z "$b" ]; then
        echo "Usage: iterm_tab_color <red 0-255> <green 0-255> <blue 0-255>"
        return 1
    fi
    printf "\e]6;1;bg;red;brightness;%d\a" "$r"
    printf "\e]6;1;bg;green;brightness;%d\a" "$g"
    printf "\e]6;1;bg;blue;brightness;%d\a" "$b"
}

# Reset tab color to default
iterm_reset_tab_color() {
    printf "\e]6;1;bg;*;default\a"
}

# Set background color using hex (e.g. #0d1b2a)
iterm_bg_color() {
    local hex="$1"
    if [ -z "$hex" ]; then
        echo "Usage: iterm_bg_color <#hex_color>"
        return 1
    fi
    printf "\e]11;%s\a" "$hex"
}

# Set foreground color using hex (e.g. #ffffff)
iterm_fg_color() {
    local hex="$1"
    if [ -z "$hex" ]; then
        echo "Usage: iterm_fg_color <#hex_color>"
        return 1
    fi
    printf "\e]10;%s\a" "$hex"
}
