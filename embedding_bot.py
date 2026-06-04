"""
embedding_bot.py - A beginner-friendly AI bot for WikiRace.

The bot tries to move from a start Wikipedia article to a stop/target article.
At every step it reads the links on the current page, scores each link by how
similar it is to the target article, then clicks the best-looking link.

Examples:
  python embedding_bot.py
  python embedding_bot.py --random
  python embedding_bot.py --start "Banana" --stop "Black hole"
"""

import argparse
import subprocess
import json
import sys
import os
import random

# The sentence-transformer library and model are loaded in main(), not at import
# time. This lets `python embedding_bot.py --help` run without AI model setup.
model = None
util = None


def start_bot_process():
    """Start bot_terminal.py in JSON pipe mode.

    This script does not talk to Wikipedia directly. Instead, it controls
    bot_terminal.py by sending JSON commands through stdin and reading JSON
    responses from stdout.
    """
    env = os.environ.copy()

    # Wikimedia asks scripts to identify themselves with contact information.
    # Change this email if you are running lots of requests.
    env["WIKIRACE_CONTACT_EMAIL"] = "bot@example.com"

    return subprocess.Popen(
        [sys.executable, "bot_terminal.py", "--bot"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        env=env,
    )


def send_cmd(proc, cmd: dict) -> dict:
    """Send one JSON command to bot_terminal.py and return its JSON response."""
    proc.stdin.write(json.dumps(cmd) + "\n")
    proc.stdin.flush()
    response = proc.stdout.readline()
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        print(f"\n[ERROR] Crash in bot terminal:\n{response}")
        sys.exit(1)


def build_new_game_command(start_article: str = "", stop_article: str = "") -> dict:
    """Create the command that starts either a custom game or a random game."""
    if start_article and stop_article:
        return {
            "cmd": "new_game",
            "start": start_article,
            "target": stop_article,
        }
    return {"cmd": "new_game"}


def play_game(start_article: str = "", stop_article: str = ""):
    """Play one WikiRace game using the embedding-based bot."""
    proc = start_bot_process()

    # Ask bot_terminal.py to start a game. If start/stop were not provided,
    # bot_terminal.py will choose a random pair of Wikipedia articles.
    new_game_cmd = build_new_game_command(start_article, stop_article)
    res = send_cmd(proc, new_game_cmd)
    if not res.get("ok"):
        print("Failed to start game:", res)
        send_cmd(proc, {"cmd": "quit"})
        proc.terminate()
        return

    state = res["state"]
    target_article = state["target_article"]
    print(f"\n🏎️  RACING: {state['start_article']}  ->  {target_article}\n")

    # Convert the target title into numbers the model can compare.
    # This vector is reused for every link we score.
    target_emb = model.encode(target_article)
    target_words = set(target_article.lower().split())

    visited = set([state["start_article"]])
    path_history = [state["start_article"]]

    while state["status"] == "playing":
        # Get every clickable Wikipedia link from the current article.
        links_res = send_cmd(proc, {"cmd": "links"})
        links = links_res.get("links", [])

        # Do not click the same article twice. That helps avoid loops.
        unvisited_links = [link for link in links if link not in visited]

        if not unvisited_links:
            print("Dead end reached! Giving up.")
            send_cmd(proc, {"cmd": "give_up"})
            break

        # Anti-rabbit-hole rule:
        # If we keep seeing the same words in recent article titles, reduce
        # scores for links with those words. This nudges the bot to explore.
        recent_articles = path_history[-4:]
        overused_words = {}
        for article in recent_articles:
            for word in article.lower().split():
                if len(word) > 3 and word not in target_words:
                    overused_words[word] = overused_words.get(word, 0) + 1

        best_link = None
        best_score = -100.0

        # Encode all candidate links in one batch. This is faster than calling
        # model.encode(...) separately for every link.
        link_embeddings = model.encode(unvisited_links)

        # Cosine similarity measures how close two embeddings are.
        # Higher score = the link title is more semantically related to target.
        cosine_scores = util.cos_sim(target_emb, link_embeddings)[0]

        for i, link in enumerate(unvisited_links):
            score = cosine_scores[i].item()

            # Simple keyword bonus:
            # If the link title shares words with the target title, boost it.
            # This catches easy cases like "Python" -> "Python programming".
            link_words = set(link.lower().split())
            overlap = len(target_words.intersection(link_words))
            if overlap > 0:
                score += overlap * 0.3

            # Diversity penalty:
            # Lower the score if the link repeats recent non-target words.
            for word in link_words:
                if word in overused_words:
                    score -= overused_words[word] * 0.15

            if score > best_score:
                best_score = score
                best_link = link

        # Escape hatch:
        # If no link looks related to the target, choose randomly. This can
        # escape bad local paths where every "smart" choice is weak.
        if best_score <= 0.05:
            best_link = random.choice(unvisited_links)
            print(f"➜ Picking randomly (No semantic match): '{best_link}'")
        else:
            print(f"➜ Clicking: '{best_link}' (Score: {best_score:.3f})")

        visited.add(best_link)
        path_history.append(best_link)

        nav_res = send_cmd(proc, {"cmd": "navigate", "article": best_link})
        state = nav_res["state"]

        if nav_res.get("won"):
            print("\n🏆 WON THE RACE!")
            print(f"Path length: {state['clicks']} clicks")
            print(f"Time: {state['elapsed_str']}")
            break

    send_cmd(proc, {"cmd": "quit"})
    proc.terminate()


def parse_args():
    """Read command-line options from the user."""
    parser = argparse.ArgumentParser(
        description="Run the embedding-based WikiRace bot.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python embedding_bot.py
  python embedding_bot.py --random
  python embedding_bot.py --start "Banana" --stop "Black hole"
        """,
    )
    parser.add_argument(
        "--start",
        default="",
        help="Start article for a custom race.",
    )
    parser.add_argument(
        "--stop",
        default="",
        help="Stop/target article for a custom race.",
    )
    parser.add_argument(
        "--target",
        default="",
        help="Alias for --stop.",
    )
    parser.add_argument(
        "--random",
        "--randomize",
        action="store_true",
        help="Randomize both the start and stop articles. This is also the default when no custom articles are provided.",
    )
    return parser.parse_args()


def main():
    """Validate options, load the model, then run the bot."""
    global model, util

    args = parse_args()
    stop_article = args.stop or args.target

    if args.stop and args.target and args.stop != args.target:
        sys.exit("Use either --stop or --target, or give both the same value.")
    if args.random and (args.start or stop_article):
        sys.exit("--random cannot be combined with --start, --stop, or --target.")
    if bool(args.start) != bool(stop_article):
        sys.exit(
            'Custom games need both articles. Example: --start "Banana" --stop "Black hole"'
        )

    print("Loading transformer model (this takes a few seconds)...")
    from sentence_transformers import SentenceTransformer, util as st_util

    model = SentenceTransformer("all-MiniLM-L6-v2")
    util = st_util

    play_game(args.start, stop_article)


if __name__ == "__main__":
    main()
