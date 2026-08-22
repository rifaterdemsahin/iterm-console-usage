#!/usr/bin/env bash
#
# Helper runner for iTerm2 manager CLI.
# Automatically creates a lightweight virtualenv with 'iterm2' if needed.
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

# Ensure venv exists with iterm2 installed
if [ ! -f "$VENV_DIR/bin/python3" ]; then
    echo "⚙️  Initializing virtual environment at $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
    "$VENV_DIR/bin/pip" install --quiet --upgrade pip
    "$VENV_DIR/bin/pip" install --quiet iterm2
fi

# Ensure iterm2 package is present
if ! "$VENV_DIR/bin/python3" -c "import iterm2" 2>/dev/null; then
    echo "📦 Installing iterm2 Python package..."
    "$VENV_DIR/bin/pip" install --quiet iterm2
fi

# Execute manager script
exec "$VENV_DIR/bin/python3" "$SCRIPT_DIR/iterm2_manager.py" "$@"
