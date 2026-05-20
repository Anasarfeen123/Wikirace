#!/usr/bin/env bash
# ════════════════════════════════════════════════════════
#  WikiRace — Setup Script (macOS / Linux)
#  Run once: bash setup.sh
# ════════════════════════════════════════════════════════

set -e
BOLD="\033[1m"
GREEN="\033[92m"
YELLOW="\033[93m"
RED="\033[91m"
RESET="\033[0m"
DIM="\033[2m"
log() { echo -e "${GREEN}[setup]${RESET} $*"; }
warn() { echo -e "${YELLOW}[warn]${RESET}  $*"; }
err() {
  echo -e "${RED}[error]${RESET} $*"
  exit 1
}

confirm() {
  local action="$1"
  local description="$2"
  echo -e "\n${BOLD}${YELLOW}→ ${action}${RESET}"
  echo -e "${DIM}${description}${RESET}"
  read -p "Allow this step? [y/N] " -n 1 -r
  echo ""
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${RED}Aborted by user.${RESET}"
    exit 1
  fi
}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

on_error() {
  echo ""
  echo -e "${RED}${BOLD}Setup did not finish.${RESET}"
  echo "Please copy the error above and send email to /"codecrusader07@gmail.com/"."
  echo "Most setup problems are caused by Python missing from the computer or by no internet connection."
  exit 1
}
trap on_error ERR

echo ""
echo -e "${BOLD}╔═══════════════════════════════════════╗${RESET}"
echo -e "${BOLD}║       WikiRace — Setup (Unix)         ║${RESET}"
echo -e "${BOLD}╚═══════════════════════════════════════╝${RESET}"
echo ""
echo "This script prepares WikiRace on this computer. It may take a few minutes."
echo "You only need to run setup once."
echo ""

# ── 1. Python ────────────────────────────────────────────
PYTHON=""
for cmd in python3.12 python3.11 python3.10 python3.9 python3 python; do
  if command -v "$cmd" &>/dev/null; then
    VER=$("$cmd" -c 'import sys; print(sys.version_info[:2])')
    if "$cmd" -c 'import sys; sys.exit(0 if sys.version_info >= (3,9) else 1)' 2>/dev/null; then
      PYTHON="$cmd"
      break
    fi
  fi
done

if [ -z "$PYTHON" ]; then
  confirm "Install Python" "Python 3.9+ not found. Attempting to install via system package manager…"
  if command -v brew &>/dev/null; then
    log "Installing Python via Homebrew…"
    brew install python@3.12
    PYTHON="python3.12"
  elif command -v apt-get &>/dev/null; then
    log "Installing Python via apt…"
    sudo apt-get update -y && sudo apt-get install -y python3 python3-pip python3-venv
    PYTHON="python3"
  elif command -v dnf &>/dev/null; then
    log "Installing Python via dnf…"
    sudo dnf install -y python3 python3-pip
    PYTHON="python3"
  else
    err "Could not install Python automatically. Please install Python 3.9+ from https://python.org and re-run this script."
  fi
fi

log "Using Python: $($PYTHON --version)"

# ── 2. Virtual environment ────────────────────────────────
VENV_DIR="$SCRIPT_DIR/.venv"
if [ ! -d "$VENV_DIR" ]; then
  confirm "Create Virtual Environment" "This will create an isolated folder (.venv) to store the project dependencies."
  log "Creating virtual environment at .venv …"
  "$PYTHON" -m venv "$VENV_DIR"
else
  log "Virtual environment already exists."
fi

# Activate
source "$VENV_DIR/bin/activate"

# ── 3. pip / dependencies ─────────────────────────────────
confirm "Upgrade pip" "This will update the Python package installer to the latest version."
log "Upgrading pip…"
pip install --upgrade pip --quiet

confirm "Install dependencies" "This will install the libraries WikiRace needs to run."
log "Installing dependencies from requirements.txt…"
pip install -r "$SCRIPT_DIR/requirements.txt" --quiet

confirm "AI Warmup" "This will download the AI model used by the bot. This is a one-time download (approx. 80MB)."
python "$SCRIPT_DIR/0_warmup.py"

echo ""
echo -e "${GREEN}${BOLD}✔  Setup complete!${RESET}"
echo ""
echo "  To play WikiRace in your browser:"
echo "    bash run_human.sh"
echo ""
echo "  To use the bot terminal:"
echo "    bash run_bot.sh"
echo ""
