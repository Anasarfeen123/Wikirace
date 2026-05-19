# WikiRace 🏁

Navigate Wikipedia by clicking links. Race from a **start article** to a **target article** as fast as possible — with as few clicks as possible.

---

## Quick Start for Non-Coders

Use this section if you only want to play the game and do not know coding.

### What You Need

- A computer with internet access.
- Python 3.9 or newer.
- The WikiRace project folder.

If Python is missing, the setup script will tell you where to install it from.

### Windows

1. Download or unzip the WikiRace folder.
2. Open the folder.
3. Double-click `START_HERE_WINDOWS.bat`.
4. Keep the black terminal window open while playing.

The first launch installs what WikiRace needs. Later launches are faster because setup is already done.

If Windows shows a security warning, choose **More info** and then **Run anyway** only if you trust where you got this folder from.

### macOS / Linux

1. Open the WikiRace folder.
2. Open a terminal in that folder.
3. Run:

```bash
bash start_here.sh
```

Keep that terminal window open while playing.

The game opens at `http://127.0.0.1:5000`. If your browser does not open automatically, copy that address into your browser.

### Stopping the Game

Close the browser tab, then close the terminal window. You can also press `Ctrl+C` in the terminal.

---

## Troubleshooting

### The game does not open

Open this address manually in your browser:

```text
http://127.0.0.1:5000
```

Make sure the terminal window is still open.

### Setup says Python is missing

Install Python from:

```text
https://www.python.org/downloads/
```

On Windows, check **Add Python to PATH** during installation. After installing Python, run the starter file again.

### Setup fails while installing dependencies

Check your internet connection, then run the starter file again. If it still fails, copy the error message from the terminal and send it to the person helping you.

---

## Manual Setup

If you prefer to set up and run separately:

### 1. Setup (run once)

| System | Command |
|--------|---------|
| macOS / Linux | `bash setup.sh` |
| Windows | `setup.bat` |

This installs dependencies into a `.venv` folder inside the project.

### 2. Play in Browser

| System | Command |
|--------|---------|
| macOS / Linux | `bash run_human.sh` |
| Windows | `run_human.bat` |

The browser UI opens automatically at `http://127.0.0.1:5000`.

### 3. Bot Terminal

**Interactive mode** (for testing or playing in the terminal):
```bash
bash run_bot.sh
# or
bash run_bot.sh --start "Banana" --target "Black hole"
```

**Bot / pipe mode** (JSON protocol over stdin/stdout, for your bots):
```bash
bash run_bot.sh --bot
```

---

## How to Play

1. A **start article** and **target article** are displayed.
2. Click **blue links** in the article text to jump to other Wikipedia pages.
3. Reach the **target article** as quickly as possible.
4. The **stopwatch** tracks your time, and every click is counted.

The web UI asks each player for their email address before loading Wikipedia data. That email is used only as the contact value in the User-Agent header sent to Wikimedia API requests for that player's session, following Wikimedia's API identification policy.

### Modes
| Mode | Description |
|------|-------------|
| Random | Two random articles chosen automatically |
| Custom | You type both the start and target articles |

---

## Project Structure

```
wikirace/
├── app.py              # Local Flask launcher
├── api/index.py        # Flask web application (human UI + Vercel entrypoint)
├── bot_terminal.py     # Terminal interface (human + bots)
├── game_core.py        # Core game state & logic (shared)
├── wiki_api.py         # Wikipedia API wrapper with caching
├── requirements.txt    # Python dependencies
│
├── templates/
│   ├── index.html      # Home / lobby page
│   └── game.html       # Game page
│
├── static/
│   ├── css/style.css   # All styles
│   └── js/game.js      # Client-side: stopwatch, AJAX navigation, confetti
│
├── setup.sh / setup.bat        # One-time setup
├── run_human.sh / run_human.bat  # Launch browser UI
└── run_bot.sh / run_bot.bat    # Launch bot terminal
```

---

## Bot Interface — JSON Protocol

Run in pipe mode:
```bash
bash run_bot.sh --bot
```

Send one JSON command per line to **stdin**; receive one JSON response per line from **stdout**.

### Commands

| Command | Description |
|---------|-------------|
| `{"cmd": "new_game"}` | Start game with random articles |
| `{"cmd": "new_game", "start": "X", "target": "Y"}` | Start with specific articles |
| `{"cmd": "state"}` | Get current game state |
| `{"cmd": "links"}` | List all links in the current article |
| `{"cmd": "navigate", "article": "Fruit"}` | Navigate to an article |
| `{"cmd": "give_up"}` | Give up the current game |
| `{"cmd": "quit"}` | Exit the process |

### Response format

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

`status` values: `playing` | `won` | `given_up`

### Example bot script (Python)

```python
import subprocess, json

proc = subprocess.Popen(
    ["bash", "run_bot.sh", "--bot"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
)

def send(cmd: dict) -> dict:
    proc.stdin.write(json.dumps(cmd) + "\n")
    proc.stdin.flush()
    return json.loads(proc.stdout.readline())

# Start a game
r = send({"cmd": "new_game"})
print("Start:", r["state"]["start_article"])
print("Target:", r["state"]["target_article"])

# Get links
r = send({"cmd": "links"})
links = r["links"]

# Navigate to first link
r = send({"cmd": "navigate", "article": links[0]})
print("Navigated to:", r["state"]["current_article"])
print("Won?", r.get("won"))
```

---

## Web API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/new_game` | POST | Start new game |
| `/game` | GET | Current game page |
| `/navigate/<title>` | GET | Navigate (AJAX or redirect) |
| `/give_up` | POST | Give up |
| `/quit` | GET | Abandon game |
| `/api/state` | GET | JSON game state |
| `/api/random_pair` | GET | JSON random article pair |

For AJAX calls add header `X-Requested-With: XMLHttpRequest` — the server returns JSON instead of HTML.

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web framework for the human UI |
| `requests` | Wikipedia API HTTP calls |
| `beautifulsoup4` + `lxml` | Clean & transform Wikipedia HTML |

---

## Deploy to Vercel

This repo is ready to deploy as a Flask app on Vercel. Vercel uses the `app` object in `api/index.py` and installs dependencies from `requirements.txt`.

Each deployer should use their own Vercel account. Do not share or commit `.vercel/project.json`; it is local Vercel project linkage and is ignored by git.

### 1. Install and log in with your Vercel account

```bash
npm i -g vercel
vercel login
```

### 2. Link or create your own Vercel project

From the project root:

```bash
vercel link
```

Choose your own account/team and project. This creates a local `.vercel/project.json` for your machine only.

### 3. Set a production session secret

In the Vercel dashboard, add this environment variable:

```text
FLASK_SECRET_KEY=<a long random secret>
```

`FLASK_SECRET_KEY` is used to sign Flask session cookies. The app can start without it, but Vercel cold starts may invalidate active sessions, so setting it is recommended.

Players enter their own email in the web UI. That player email is included in the User-Agent sent to Wikimedia API requests for their session, so the deployed app does not use the deployer's email for everyone.

For bot/headless usage, set `WIKIRACE_CONTACT_EMAIL` or a full `WIKIMEDIA_USER_AGENT` in the environment before making Wikipedia API calls.

### 4. Deploy

From the project root:

```bash
vercel
```

For production:

```bash
vercel --prod
```

Notes:

- Static assets are served from the single canonical `static/` directory.
- Game state is mirrored into the signed Flask session for Vercel's serverless runtime. Very long paths may exceed browser cookie limits; use Redis or another external store if you need production-scale persistence.
- The app fetches live Wikipedia data, so deployed games require outbound network access.

---

## Tips for Bot Builders

- **`links` command** returns every main-namespace link in the current article — use this as your action space.
- **`elapsed`** in the state is server-side elapsed seconds — useful for time-budget strategies.
- Wikipedia article links form a **directed graph**. BFS / greedy category-climbing tend to work well.
- The `game_core.py` and `wiki_api.py` modules can be imported directly in your bot code without using the JSON protocol:

```python
from game_core import new_game
from wiki_api  import get_random_pair, get_article_links

start, target = get_random_pair()
game = new_game(start["title"], target["title"])

links = get_article_links(game.current_article)
won   = game.navigate(links[0])
print(game.to_dict())
```

---

## License

MIT — do what you like.
