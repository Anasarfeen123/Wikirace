# CLAUDE.md

Guidance for AI coding agents working in this repository.

## Project Overview

WikiRace is a Python/Flask game where players race from one Wikipedia article to another by clicking article links. The same core game logic is shared by:

- A browser UI served by Flask.
- A terminal interface for humans.
- A JSON stdin/stdout protocol for bots.

The application depends on live Wikipedia API calls, so many full-flow checks require network access.

## Active Code Paths

- `app.py` - Flask app, sessions, HTTP routes, and JSON endpoints.
- `game_core.py` - UI-independent game state and win/click/timer logic.
- `wiki_api.py` - Wikipedia API wrapper, title normalization, in-memory cache, and HTML cleanup/link rewriting.
- `bot_terminal.py` - interactive terminal mode and bot JSON protocol.
- `templates/index.html` - active Flask home/lobby template.
- `templates/game.html` - active Flask game template.
- `static/js/game.js` - active browser-side game behavior.
- `static/css/style.css` - active browser styles.
- `requirements.txt` - Python dependencies.
- `run_human.sh` / `run_human.bat` - launch browser UI.
- `run_bot.sh` / `run_bot.bat` - launch terminal/bot mode.
- `setup.sh` / `setup.bat` - create `.venv` and install dependencies.

There are also root-level `index.html`, `game.html`, `game.js`, and `style.css` files. Flask does not serve those as the active app assets. Prefer editing `templates/` and `static/` unless the task explicitly asks to update standalone/root files too.

## Common Commands

Set up dependencies:

```bash
bash setup.sh
```

Run the browser UI:

```bash
bash run_human.sh
```

Run the Flask app directly:

```bash
source .venv/bin/activate
python app.py
```

Run the terminal interface:

```bash
bash run_bot.sh
```

Run bot pipe mode:

```bash
bash run_bot.sh --bot
```

Run a deterministic terminal game:

```bash
bash run_bot.sh --start "Banana" --target "Black hole"
```

Basic syntax check:

```bash
python -m compileall app.py game_core.py wiki_api.py bot_terminal.py
```

There is no dedicated test suite in the repo yet. For risky changes, add targeted tests or at least run syntax checks plus a small manual flow.

## Bot JSON Protocol

In `--bot` mode, `bot_terminal.py` reads one JSON object per line from stdin and writes one JSON object per line to stdout.

Supported commands:

- `{"cmd": "new_game"}`
- `{"cmd": "new_game", "start": "Banana", "target": "Black hole"}`
- `{"cmd": "state"}`
- `{"cmd": "links"}`
- `{"cmd": "navigate", "article": "Fruit"}`
- `{"cmd": "give_up"}`
- `{"cmd": "quit"}`

Keep bot-mode stdout machine-readable. Human-facing logs should go through `_log()`, which is suppressed when `BOT_MODE` is true.

## Architecture Notes

- `GameState` in `game_core.py` is the source of truth for current article, path, clicks, status, and elapsed time.
- Title comparisons should use `titles_match()` instead of direct string equality.
- User-entered or route-derived titles should pass through `normalize_title()`.
- `wiki_api.get_article()` returns cleaned article HTML and main-namespace links. Avoid duplicating Wikipedia API parsing elsewhere unless there is a clear reason.
- `_clean_html()` rewrites valid `/wiki/...` links to `/navigate/...`; browser navigation depends on the `wikirace-link` class and `data-article` attribute.
- Flask stores game objects in the process-global `_games` dict and only stores `game_id` in the session. This is fine for local play, not production multi-process deployment.
- `app.secret_key` is hardcoded for local development. Do not treat it as production-ready.

## Frontend Notes

- Edit `templates/` and `static/` for the live Flask UI.
- `static/js/game.js` performs AJAX navigation by sending `X-Requested-With: XMLHttpRequest` to `/navigate/<title>`.
- When changing server responses for navigation, update both `app.py` and `static/js/game.js` together.
- Wikipedia article HTML is injected with `|safe` after cleanup in `wiki_api.py`; keep cleanup strict when expanding allowed markup.
- The UI references `/static/logo.png`. Make sure any logo asset needed by templates exists under `static/`.

## Style and Maintenance Guidelines

- Keep shared behavior in `game_core.py`; keep UI-specific behavior in Flask/templates/JS or `bot_terminal.py`.
- Preserve the bot protocol shape unless intentionally making a breaking change.
- Prefer small, explicit helpers over broad rewrites.
- Avoid adding persistent global state beyond the existing cache/game store unless the lifecycle is clear.
- Be careful with network-dependent code paths: Wikipedia requests can fail, time out, or return missing/error pages.
- Keep comments useful and sparse.
- Do not commit generated archives, virtual environments, caches, or `__pycache__`.

## Verification Checklist

For backend/game-logic changes:

```bash
source .venv/bin/activate
python -m compileall app.py game_core.py wiki_api.py bot_terminal.py
```

For web UI changes:

1. Start the app with `bash run_human.sh`.
2. Open `http://127.0.0.1:5000`.
3. Start a custom game with known articles.
4. Click at least one article link.
5. Verify clicks, path history, stopwatch, give-up, and win modal behavior as relevant.

For bot changes:

```bash
printf '{"cmd":"new_game","start":"Banana","target":"Black hole"}\n{"cmd":"state"}\n{"cmd":"quit"}\n' | bash run_bot.sh --bot
```

Confirm every output line is valid JSON.
