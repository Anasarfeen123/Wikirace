#!/usr/bin/env bash
# Run the WikiRace bot terminal
# Options:
#   --bot               pipe-mode (JSON stdin/stdout)
#   --start X --target Y  start with specific articles
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV" ]; then
    echo "Virtual environment not found. Running setup first…"
    bash "$SCRIPT_DIR/setup.sh"
fi

source "$VENV/bin/activate"
cd "$SCRIPT_DIR"
exec python bot_terminal.py "$@"
