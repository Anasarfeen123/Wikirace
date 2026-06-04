#!/usr/bin/env python3
"""
bot_terminal.py — Beginner-friendly terminal interface for WikiRace.

════════════════════════════════════════════════════════════════════════════
  INTERACTIVE MODE (for humans / testing)
    python bot_terminal.py

  RANDOM GAME
    python bot_terminal.py --random

  CUSTOM GAME
    python bot_terminal.py --start "Python (programming language)" --stop "Albert Einstein"

  BOT / PIPE MODE  (read JSON commands from stdin, write JSON to stdout)
    python bot_terminal.py --bot

  BOT / PIPE MODE WITH A CUSTOM GAME
    python bot_terminal.py --bot --start "Banana" --stop "Black hole"
════════════════════════════════════════════════════════════════════════════

JSON PROTOCOL
─────────────
Commands (one JSON object per line, written to stdin):

  {"cmd": "new_game"}
  {"cmd": "new_game", "start": "Banana", "target": "Black hole"}
  {"cmd": "state"}
  {"cmd": "links"}
  {"cmd": "navigate", "article": "Fruit"}
  {"cmd": "give_up"}
  {"cmd": "quit"}

Responses (one JSON object per line, written to stdout):

  {"ok": true,  "event": "game_started", "state": {...}}
  {"ok": true,  "event": "navigated",    "state": {...}, "won": false}
  {"ok": true,  "event": "won",          "state": {...}}
  {"ok": true,  "event": "links",        "links": ["Article A", ...]}
  {"ok": false, "error": "No active game."}
"""

import sys
import json
import argparse
import readline  # noqa: F401 — enables arrow-key history in interactive mode

from game_core import new_game, GameState
from wiki_api  import get_random_pair, get_article_links, article_exists, normalize_title, titles_match


# ── ANSI colours ──────────────────────────────────────────────────────────────
# These escape codes make the interactive terminal easier to read.
# They are automatically disabled in bot mode so JSON output stays clean.
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    RED    = "\033[91m"
    WHITE  = "\033[97m"

BOT_MODE = False  # Set by --bot. When True, print only machine-readable JSON.


def _c(code: str, text: str) -> str:
    """Apply terminal colour in interactive mode; return plain text in bot mode."""
    return f"{code}{text}{C.RESET}" if not BOT_MODE else text


# ── State ─────────────────────────────────────────────────────────────────────
# The terminal runs one game at a time. All commands read or update this object.
game: GameState | None = None


# ── Command handlers ─────────────────────────────────────────────────────────

def cmd_new_game(start: str = "", target: str = "") -> dict:
    """Start a new game, either custom or random."""
    global game

    # Custom game: the user/bot provided both article names.
    if start and target:
        start  = normalize_title(start)
        target = normalize_title(target)
        if not article_exists(start):
            return _err(f"Article not found: '{start}'")
        if not article_exists(target):
            return _err(f"Article not found: '{target}'")

    # Random game: no custom pair was provided, so ask Wikipedia for two pages.
    else:
        _log("⏳  Fetching random article pair…")
        s_info, t_info = get_random_pair()
        start, target  = s_info["title"], t_info["title"]

    game = new_game(start, target)
    _log(f"\n  {_c(C.CYAN, 'START')}  {_c(C.WHITE+C.BOLD, game.start_article)}")
    _log(f"  {_c(C.YELLOW, 'TARGET')} {_c(C.WHITE+C.BOLD, game.target_article)}")
    _log(f"  {_c(C.DIM, 'Game ID:')} {game.game_id}\n")
    return {"ok": True, "event": "game_started", "state": game.to_dict()}


def cmd_state() -> dict:
    """Show the current game details."""
    if not game:
        return _err("No active game.")
    _print_state()
    return {"ok": True, "event": "state", "state": game.to_dict()}


def cmd_links() -> dict:
    """List valid links from the current article."""
    if not game:
        return _err("No active game.")
    _log(f"⏳  Loading links from '{game.current_article}'…")
    links = get_article_links(game.current_article)
    _log(f"\n  {_c(C.DIM, f'{len(links)} links available:')}")
    if not BOT_MODE:
        for i, lnk in enumerate(links[:30], 1):
            print(f"    {_c(C.DIM, str(i).rjust(3))}  {lnk}")
        if len(links) > 30:
            _log(f"    … and {len(links) - 30} more.")
    _log("")
    return {"ok": True, "event": "links", "links": links}


def cmd_navigate(article: str) -> dict:
    """Move from the current article to another article link."""
    if not game:
        return _err("No active game.")
    if game.is_over:
        return _err("Game is already over.")
    article = normalize_title(article)
    links = get_article_links(game.current_article)
    if not any(titles_match(article, link) for link in links):
        return _err(
            f"Cannot navigate to '{article}'. "
            f"Choose one of the {len(links)} links on '{game.current_article}'."
        )
    try:
        won = game.navigate(article)
    except ValueError as e:
        return _err(str(e))

    _log(f"  → {_c(C.CYAN, article)}  "
         f"[{_c(C.BOLD, str(game.clicks))} click{'s' if game.clicks != 1 else ''}  |  "
         f"{_c(C.YELLOW, game.elapsed_str)}]")

    if won:
        _log(_c(C.GREEN + C.BOLD, "\n  🏆  YOU WIN!"))
        _print_path()
        _log(f"  Time:   {_c(C.WHITE+C.BOLD, game.elapsed_str)}")
        _log(f"  Clicks: {_c(C.WHITE+C.BOLD, str(game.clicks))}\n")
        return {"ok": True, "event": "won", "state": game.to_dict()}

    return {"ok": True, "event": "navigated", "won": False, "state": game.to_dict()}


def cmd_give_up() -> dict:
    """End the current game without winning."""
    if not game:
        return _err("No active game.")
    game.give_up()
    _log(_c(C.RED, "\n  ✗  You gave up."))
    _print_path()
    return {"ok": True, "event": "given_up", "state": game.to_dict()}


def cmd_help() -> dict:
    """Print commands for people using the interactive terminal."""
    _log(f"""
  {_c(C.BOLD, 'WikiRace Bot Terminal')}  {_c(C.DIM, '— commands')}

  {_c(C.CYAN, 'new_game')}                  Start game with random articles
  {_c(C.CYAN, 'random')}                    Same as new_game
  {_c(C.CYAN, 'new_game <start> <stop>')}   Start game with specific articles
  {_c(C.CYAN, 'start <start> <stop>')}      Same as new_game <start> <stop>
  {_c(C.CYAN, 'state')}                      Show current game state
  {_c(C.CYAN, 'links')}                      List links in current article
  {_c(C.CYAN, 'navigate <article>')}         Navigate to an article
  {_c(C.CYAN, 'give_up')}                    Give up current game
  {_c(C.CYAN, 'help')}                       Show this help
  {_c(C.CYAN, 'quit')}                       Exit
""")
    return {"ok": True, "event": "help"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _err(msg: str) -> dict:
    """Return a standard error response and print it for humans."""
    _log(_c(C.RED, f"  ✗  {msg}"))
    return {"ok": False, "error": msg}


def _log(msg: str):
    """Print only in interactive mode. Bot mode must keep stdout as JSON only."""
    if not BOT_MODE:
        print(msg)


def _print_state():
    """Pretty-print the current game state for interactive users."""
    if not game:
        return
    _log(f"\n  {_c(C.DIM, 'Game')}     {game.game_id}")
    _log(f"  {_c(C.CYAN, 'Start')}    {game.start_article}")
    _log(f"  {_c(C.YELLOW, 'Target')}   {game.target_article}")
    _log(f"  {_c(C.WHITE, 'Current')}  {game.current_article}")
    _log(f"  {_c(C.DIM, 'Status')}   {game.status}")
    _log(f"  {_c(C.DIM, 'Time')}     {game.elapsed_str}")
    _log(f"  {_c(C.DIM, 'Clicks')}   {game.clicks}")
    _print_path()


def _print_path():
    """Print the full path taken so far."""
    if not game or not game.path:
        return
    _log(f"\n  {_c(C.DIM, 'Path:')}")
    for i, step in enumerate(game.path):
        connector = "┌" if i == 0 else ("└" if i == len(game.path)-1 else "├")
        col = C.CYAN if i == 0 else (C.YELLOW if i == len(game.path)-1 else C.WHITE)
        _log(f"    {_c(C.DIM, connector)} {_c(col, step)}")
    _log("")


# ── Interactive mode parser ───────────────────────────────────────────────────

def _parse_interactive(line: str) -> dict | None:
    """
    Convert a human command into the same dictionary shape used by bot mode.

    Examples:
      new_game
      random
      new_game Banana Black hole
      navigate Fruit
    """
    parts = line.strip().split(None, 2)
    if not parts:
        return None
    verb = parts[0].lower()

    if verb in ("q", "quit", "exit"):
        return {"cmd": "quit"}
    if verb in ("h", "help", "?"):
        return {"cmd": "help"}
    if verb in ("s", "state", "status"):
        return {"cmd": "state"}
    if verb in ("l", "links", "ls"):
        return {"cmd": "links"}
    if verb in ("g", "give_up", "giveup", "surrender"):
        return {"cmd": "give_up"}
    if verb in ("r", "random", "randomize"):
        return {"cmd": "new_game"}
    if verb in ("n", "new", "new_game", "start"):
        if len(parts) >= 3:
            return {"cmd": "new_game", "start": parts[1], "target": parts[2]}
        return {"cmd": "new_game"}
    if verb in ("go", "nav", "navigate", "visit", "click"):
        if len(parts) < 2:
            _log(_c(C.RED, "  Usage: navigate <article>"))
            return None
        return {"cmd": "navigate", "article": " ".join(parts[1:])}

    # Fallback: treat the whole line as an article name
    return {"cmd": "navigate", "article": line.strip()}


# ── Dispatch ──────────────────────────────────────────────────────────────────

def dispatch(cmd_obj: dict) -> dict:
    """Route one parsed command to the correct command handler."""
    cmd = cmd_obj.get("cmd", "").lower()
    if cmd == "new_game":
        return cmd_new_game(cmd_obj.get("start", ""), cmd_obj.get("target", ""))
    if cmd == "state":
        return cmd_state()
    if cmd == "links":
        return cmd_links()
    if cmd == "navigate":
        art = cmd_obj.get("article","").strip()
        if not art:
            return _err("'navigate' requires an 'article' field.")
        return cmd_navigate(art)
    if cmd == "give_up":
        return cmd_give_up()
    if cmd == "help":
        return cmd_help()
    if cmd == "quit":
        return {"ok": True, "event": "quit"}
    return _err(f"Unknown command: '{cmd}'")


# ── Entry points ──────────────────────────────────────────────────────────────

def _initial_game_command(random_game: bool, start: str, target: str) -> dict | None:
    """Build the optional command-line game that should run before the prompt."""
    if random_game:
        return {"cmd": "new_game"}
    if start and target:
        return {"cmd": "new_game", "start": start, "target": target}
    return None


def run_bot_mode(initial_command: dict | None = None):
    """Read JSON lines from stdin, write JSON lines to stdout."""
    if initial_command:
        print(json.dumps(dispatch(initial_command)), flush=True)

    for raw_line in sys.stdin:
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        try:
            cmd_obj = json.loads(raw_line)
        except json.JSONDecodeError as e:
            result = {"ok": False, "error": f"Invalid JSON: {e}"}
            print(json.dumps(result), flush=True)
            continue

        result = dispatch(cmd_obj)
        print(json.dumps(result), flush=True)

        if result.get("event") == "quit":
            break


def run_interactive_mode(initial_command: dict | None = None):
    """Run the colourful human terminal interface."""
    print(f"""
  ╔══════════════════════════════════════════╗
  ║  {_c(C.BOLD+C.CYAN, 'W')+_c(C.BOLD,'iki')+_c(C.BOLD+C.YELLOW,'Race')}  — Bot Terminal           ║
  ║  {_c(C.DIM, "type 'help' for commands")}                  ║
  ╚══════════════════════════════════════════╝
""")

    if initial_command:
        dispatch(initial_command)
    else:
        _log(_c(C.DIM, "  Tip: type 'random' to randomize articles, or 'start <start article> <stop article>'\n"))

    while True:
        try:
            prompt = ""
            if game and not game.is_over:
                current_title = game.current_article[:35] + "…" if len(game.current_article) > 35 else game.current_article
                target_title = game.target_article[:30] + "…" if len(game.target_article) > 30 else game.target_article
                prompt = (
                    f"\n  {_c(C.DIM,'[')}cur: {_c(C.CYAN, current_title)}"
                    f"  →  {_c(C.YELLOW, target_title)}"
                    f"  {_c(C.DIM, game.elapsed_str)}{_c(C.DIM,']')}\n"
                    f"  {_c(C.DIM,'>')} "
                )
            else:
                prompt = f"\n  {_c(C.DIM,'>')} "
            line = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print()
            _log(_c(C.DIM, "\n  Bye!\n"))
            break

        if not line.strip():
            continue

        # Try to parse as JSON first (useful for copy-pasting bot commands)
        cmd_obj = None
        try:
            cmd_obj = json.loads(line)
        except json.JSONDecodeError:
            cmd_obj = _parse_interactive(line)

        if cmd_obj is None:
            continue

        result = dispatch(cmd_obj)
        if result.get("event") == "quit":
            _log(_c(C.DIM, "\n  Bye!\n"))
            break


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    """Parse command-line options, then start either bot mode or interactive mode."""
    global BOT_MODE
    parser = argparse.ArgumentParser(
        description="WikiRace Terminal — for bots and humans.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--bot", action="store_true", help="Bot mode: read JSON from stdin and write JSON to stdout.")
    parser.add_argument("--random", action="store_true", help="Start with random start and stop articles.")
    parser.add_argument("--start", default="", help="Start article for a custom game.")
    parser.add_argument("--stop", default="", help="Stop/target article for a custom game.")
    parser.add_argument("--target", default="", help="Alias for --stop.")
    args = parser.parse_args()

    target = args.stop or args.target
    if args.stop and args.target and args.stop != args.target:
        parser.error("Use either --stop or --target, or give both the same value.")
    if args.random and (args.start or target):
        parser.error("--random cannot be combined with --start, --stop, or --target.")
    if bool(args.start) != bool(target):
        parser.error("Custom games need both --start and --stop. Example: --start Banana --stop \"Black hole\"")

    BOT_MODE = args.bot
    initial_command = _initial_game_command(args.random, args.start, target)

    if BOT_MODE:
        run_bot_mode(initial_command)
    else:
        run_interactive_mode(initial_command)


if __name__ == "__main__":
    main()
