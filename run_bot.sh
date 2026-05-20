#!/usr/bin/env bash
# Run the WikiRace bot terminal
# Options:
#   --bot               pipe-mode (JSON stdin/stdout)
#   --start X --target Y  start with specific articles
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

confirm "Start Bot Terminal" "This will open an interactive terminal where you can play WikiRace or run bots."

source "$VENV/bin/activate"
cd "$SCRIPT_DIR"
exec python bot_terminal.py "$@"
