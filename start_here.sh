#!/usr/bin/env bash
# Friendly one-command launcher for people who do not use the terminal often.
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "WikiRace starter"
echo "This will set up WikiRace if needed, then open the game in your browser."
echo ""

bash "$SCRIPT_DIR/run_human.sh"
