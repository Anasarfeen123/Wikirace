#!/usr/bin/env bash
# Run the WikiRace bot terminal
# Options:
#   --bot               pipe-mode (JSON stdin/stdout)
#   --start X --target Y  start with specific articles
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV" ]; then
    echo "First-time setup is needed. This may take a few minutes."
    bash "$SCRIPT_DIR/setup.sh"
fi

source "$VENV/bin/activate"
cd "$SCRIPT_DIR"
exec python bot_terminal.py "$@"
