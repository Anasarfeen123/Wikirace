#!/usr/bin/env bash
# Run the WikiRace human web UI
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$SCRIPT_DIR/.venv"

BOLD="\033[1m"; GREEN="\033[92m"; YELLOW="\033[93m"; RED="\033[91m"; RESET="\033[0m"; DIM="\033[2m"

confirm() {
    local action="$1"
    local description="$2"
    echo -e "\n${BOLD}${YELLOW}→ ${action}${RESET}"
    echo -e "${DIM}${description}${RESET}"
    read -p "Allow this? [y/N] " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}Aborted by user.${RESET}"
        exit 1
    fi
}

if [ ! -d "$VENV" ]; then
    echo "First-time setup is needed. This may take a few minutes."
    bash "$SCRIPT_DIR/setup.sh"
fi

confirm "Start WikiRace" "This will launch the web server and open the game in your browser."

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
