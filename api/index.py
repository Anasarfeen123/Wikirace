"""
app.py — Flask web application (human player UI).
Run with:  python app.py
"""

import os
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    session,
    request,
    jsonify,
)
from game_core import new_game, GameState
from wiki_api import (
    get_random_pair,
    get_article,
    article_exists,
    normalize_title,
    titles_match,
)

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static",
    static_url_path="/static",
)
app.secret_key = (
    os.environ.get("FLASK_SECRET_KEY")
    or os.environ.get("SECRET_KEY")
    or "wikirace-secret-do-change-in-prod"
)

# ── In-memory game store (game_id → GameState) ────────────────────────────────
# For a multi-user deployment swap this for Redis / DB.
_games: dict[str, GameState] = {}


# ─── Helpers ──────────────────────────────────────────────────────────────────


def _get_game() -> GameState | None:
    gid = session.get("game_id")
    if gid and gid in _games:
        return _games[gid]

    data = session.get("game_state")
    if not isinstance(data, dict):
        return None

    game = _game_from_dict(data)
    if not game:
        return None

    _games[game.game_id] = game
    session["game_id"] = game.game_id
    return game


def _save_game(game: GameState) -> None:
    _games[game.game_id] = game
    session["game_id"] = game.game_id
    session["game_state"] = game.to_dict()
    session.modified = True


def _game_from_dict(data: dict) -> GameState | None:
    try:
        return GameState(
            game_id=data["game_id"],
            start_article=data["start_article"],
            target_article=data["target_article"],
            current_article=data["current_article"],
            path=list(data.get("path") or []),
            start_time=float(data["start_time"]),
            end_time=data.get("end_time"),
            clicks=int(data.get("clicks", 0)),
            status=data.get("status", "playing"),
        )
    except (KeyError, TypeError, ValueError):
        return None


# ─── Routes ───────────────────────────────────────────────────────────────────


@app.route("/")
def index():
    game = _get_game()
    return render_template("index.html", active_game=game)


@app.route("/new_game", methods=["POST"])
def start_new_game():
    mode = request.form.get("mode", "random")

    if mode == "random":
        start_info, target_info = get_random_pair()
        start = start_info["title"]
        target = target_info["title"]
    else:
        start = normalize_title(request.form.get("start", "").strip())
        target = normalize_title(request.form.get("target", "").strip())
        if not start or not target:
            return render_template(
                "index.html",
                error="Please enter both a start and a target article.",
                active_game=_get_game(),
            )
        if titles_match(start, target):
            return render_template(
                "index.html",
                error="Start and target must be different articles.",
                active_game=_get_game(),
            )
        if not article_exists(start):
            return render_template(
                "index.html",
                error=f'Article not found: "{start}"',
                active_game=_get_game(),
            )
        if not article_exists(target):
            return render_template(
                "index.html",
                error=f'Article not found: "{target}"',
                active_game=_get_game(),
            )

    game = new_game(start, target)
    _save_game(game)
    return redirect(url_for("game"))


@app.route("/game")
def game():
    g = _get_game()
    if not g:
        return redirect(url_for("index"))

    article = get_article(g.current_article)
    if not article:
        return render_template(
            "game.html",
            game=g,
            article=None,
            error=f"Could not load article: {g.current_article}",
        )
    return render_template("game.html", game=g, article=article)


@app.route("/navigate/<path:raw_title>")
def navigate(raw_title: str):
    """
    Called when the player clicks a wiki link.
    Supports both AJAX (returns JSON) and regular GET (returns page).
    """
    g = _get_game()
    if not g:
        return redirect(url_for("index"))
    if g.is_over:
        return redirect(url_for("game"))

    title = normalize_title(raw_title)
    won = g.navigate(title)
    _save_game(g)

    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        if won:
            return jsonify(
                {
                    "status": "won",
                    "state": g.to_dict(),
                }
            )
        article = get_article(g.current_article)
        return jsonify(
            {
                "status": "playing",
                "article_html": article["html"] if article else "",
                "display_title": article["display_title"] if article else title,
                "state": g.to_dict(),
            }
        )

    # Non-AJAX fallback
    return redirect(url_for("game"))


@app.route("/give_up", methods=["POST"])
def give_up():
    g = _get_game()
    if g and not g.is_over:
        g.give_up()
        _save_game(g)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    if is_ajax:
        return jsonify({"status": "given_up", "state": g.to_dict() if g else {}})
    return redirect(url_for("game"))


@app.route("/api/state")
def api_state():
    g = _get_game()
    if not g:
        return jsonify({"error": "No active game"}), 404
    return jsonify(g.to_dict())


@app.route("/api/random_pair")
def api_random_pair():
    s, t = get_random_pair()
    return jsonify({"start": s["title"], "target": t["title"]})


@app.route("/quit")
def quit_game():
    gid = session.pop("game_id", None)
    session.pop("game_state", None)
    if gid:
        _games.pop(gid, None)
    return redirect(url_for("index"))


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import webbrowser
    import threading
    import time as _time

    def _open_browser():
        _time.sleep(1.2)
        webbrowser.open("http://127.0.0.1:5000")

    threading.Thread(target=_open_browser, daemon=True).start()
    print("\n  🌐  WikiRace is starting — opening your browser…")
    print("      If it doesn't, open this in the webbrowser: http://127.0.0.1:5000\n")
    app.run(debug=False, port=5000)
