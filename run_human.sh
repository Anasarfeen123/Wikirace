#!/usr/bin/env bash
# Run the WikiRace human web UI
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

if [ ! -d "$VENV" ]; then
    echo "First-time setup is needed. This may take a few minutes."
    bash "$SCRIPT_DIR/setup.sh"
fi

source "$VENV/bin/activate"
cd "$SCRIPT_DIR"

URL="http://127.0.0.1:5000"
echo ""
echo "Starting WikiRace..."
echo "Your browser should open automatically."
echo "If it does not, open this address yourself: $URL"
echo "Keep this terminal window open while playing."
echo ""

(
    sleep 2
    if command -v open >/dev/null 2>&1; then
        open "$URL" >/dev/null 2>&1 || true
    elif command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$URL" >/dev/null 2>&1 || true
    fi
) &

exec python app.py "$@"
