# WikiRace

WikiRace is a Python/Flask implementation of the classic Wikipedia navigation game. Players start on one Wikipedia article and try to reach a target article by following only links inside article content. The project includes a browser UI, a terminal interface, and a JSON-line bot protocol for automated players.

## Features

- Browser-based human game with random and custom article pairs
- Terminal mode for quick local play and testing
- Bot mode with JSON commands over stdin/stdout
- Live Wikipedia data through the Wikimedia API
- Click counter, timer, path tracking, give-up flow, and win detection
- Shared game logic in `game_core.py`
- Vercel-compatible Flask entry point in `api/index.py`

## Requirements

- Python 3.9 or newer
- Internet access for dependency installation and Wikipedia API requests
- A player/contact email for Wikimedia API identification

Python dependencies are listed in `requirements.txt`.

## Quick Start

### Windows

1. Open the project folder.
2. Double-click `START_HERE_WINDOWS.bat`.
3. Keep the terminal window open while playing.

The first run installs the required Python packages. Later runs should start faster.

### macOS / Linux

From the project root:

```bash
bash start_here.sh
```

The game runs at:

```text
http://127.0.0.1:5000
```

If the browser does not open automatically, open that URL manually. Stop the app with `Ctrl+C` in the terminal.

## Manual Setup

Run setup once:

```bash
# macOS / Linux
bash setup.sh

# Windows
setup.bat
```

Optional AI model warmup:

```bash
# macOS / Linux
.venv/bin/python 0_warmup.py

# Windows
.venv\Scripts\python 0_warmup.py
```

Start the browser game:

```bash
# macOS / Linux
bash run_human.sh

# Windows
run_human.bat
```

Start the terminal game:

```bash
# macOS / Linux
bash run_bot.sh

# Windows
run_bot.bat
```

Start a preset terminal game:

```bash
bash run_bot.sh --start "Banana" --stop "Black hole"
```

Start with random terminal articles immediately:

```bash
bash run_bot.sh --random
```

## How to Play

1. Enter an email address for Wikimedia API identification.
2. Choose a random game or enter custom start and target articles.
3. Read the current article and click blue article links.
4. Reach the target article in as few clicks and as little time as possible.

The email entered in the web UI is used only as the contact value in the User-Agent header sent to Wikimedia API requests for that session.

## Bot Mode

Bot mode reads one JSON object per line from stdin and writes one JSON response per line to stdout.

```bash
bash run_bot.sh --bot
```

Bot mode can also start with command-line articles:

```bash
bash run_bot.sh --bot --start "Banana" --stop "Black hole"
bash run_bot.sh --bot --random
```

### Commands

| Command | Description |
| --- | --- |
| `{"cmd": "new_game"}` | Start a random game |
| `{"cmd": "new_game", "start": "X", "target": "Y"}` | Start a custom game |
| `{"cmd": "state"}` | Return the current game state |
| `{"cmd": "links"}` | Return links from the current article |
| `{"cmd": "navigate", "article": "Fruit"}` | Navigate to a linked article |
| `{"cmd": "give_up"}` | End the current game as given up |
| `{"cmd": "quit"}` | Exit bot mode |

### Response Example

```json
{
  "ok": true,
  "event": "navigated",
  "won": false,
  "state": {
    "game_id": "a1b2c3d4",
    "start_article": "Banana",
    "target_article": "Black hole",
    "current_article": "Fruit",
    "path": ["Banana", "Fruit"],
    "clicks": 1,
    "status": "playing",
    "elapsed": 12.34,
    "elapsed_str": "12.34",
    "start_time": 1700000000.0,
    "end_time": null
  }
}
```

`status` is one of `playing`, `won`, or `given_up`.

### Python Bot Example

```python
import json
import subprocess

proc = subprocess.Popen(
    ["bash", "run_bot.sh", "--bot"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
)


def send(command: dict) -> dict:
    proc.stdin.write(json.dumps(command) + "\n")
    proc.stdin.flush()
    return json.loads(proc.stdout.readline())


game = send({"cmd": "new_game", "start": "Banana", "target": "Black hole"})
print(game["state"]["current_article"], "->", game["state"]["target_article"])

links = send({"cmd": "links"})["links"]
result = send({"cmd": "navigate", "article": links[0]})
print(result["state"])

send({"cmd": "quit"})
```

## Web API

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | GET | Home page |
| `/new_game` | POST | Start a new game |
| `/game` | GET | Current game page |
| `/navigate/<title>` | GET | Navigate to an article |
| `/give_up` | POST | Give up the active game |
| `/quit` | GET | Clear the active game |
| `/api/state` | GET | Return JSON game state |
| `/api/random_pair` | GET | Return a random start/target pair |

For AJAX navigation, send `X-Requested-With: XMLHttpRequest` to receive JSON instead of a page redirect.

## Project Structure

```text
.
├── app.py                 # Local Flask launcher
├── api/index.py           # Flask app and Vercel entry point
├── game_core.py           # Shared game state and win logic
├── wiki_api.py            # Wikimedia API wrapper and HTML cleanup
├── bot_terminal.py        # Interactive terminal and bot protocol
├── embedding_bot.py       # AI-assisted bot support
├── 0_warmup.py            # Downloads the sentence-transformer model
├── requirements.txt       # Python dependencies
├── templates/             # Flask HTML templates
├── static/                # CSS and JavaScript
├── setup.sh / setup.bat   # One-time setup scripts
├── run_human.*            # Browser game launch scripts
└── run_bot.*              # Terminal and bot launch scripts
```

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `FLASK_SECRET_KEY` | Secret key for Flask session cookies; recommended for deployments |
| `SECRET_KEY` | Fallback Flask session secret |
| `WIKIRACE_CONTACT_EMAIL` | Contact email for bot/headless Wikimedia API requests |
| `WIKIMEDIA_CONTACT_EMAIL` | Alternative contact email variable |
| `WIKIMEDIA_USER_AGENT` | Full custom Wikimedia API User-Agent |

For browser play, each player enters their email in the UI. For bot or direct module usage, set `WIKIRACE_CONTACT_EMAIL` or `WIKIMEDIA_USER_AGENT`.

## Deployment

This repository can be deployed to Vercel as a Flask app. Vercel uses the `app` object exported from `api/index.py` and installs dependencies from `requirements.txt`.

1. Install the Vercel CLI:

   ```bash
   npm i -g vercel
   ```

2. Log in and link a project:

   ```bash
   vercel login
   vercel link
   ```

3. Set `FLASK_SECRET_KEY` in the Vercel dashboard.

4. Deploy:

   ```bash
   vercel
   vercel --prod
   ```

Do not commit `.vercel/project.json`; it contains local project linkage and is ignored by git.

## Troubleshooting

If the browser does not open, visit `http://127.0.0.1:5000` manually and make sure the terminal is still running.

If Python is missing, install it from `https://www.python.org/downloads/`. On Windows, enable "Add Python to PATH" during installation.

If dependency installation fails, check your internet connection and rerun the setup script.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
