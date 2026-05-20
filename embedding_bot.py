import subprocess
import json
import sys
import os
import random


#**********************************************************
from sentence_transformers import SentenceTransformer, util
#**********************************************************

print("Loading transformer model (this takes a few seconds)...")

#**********************************************************
# This downloads a highly optimized, state-of-the-art semantic similarity model
model = SentenceTransformer("all-MiniLM-L6-v2")
#**********************************************************


def start_bot_process():
    env = os.environ.copy()
    env["WIKIRACE_CONTACT_EMAIL"] = "bot@example.com"

    return subprocess.Popen(
        ["python", "bot_terminal.py", "--bot"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        env=env,
    )


def send_cmd(proc, cmd: dict) -> dict:
    proc.stdin.write(json.dumps(cmd) + "\n")
    proc.stdin.flush()
    response = proc.stdout.readline()
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        print(f"\n[ERROR] Crash in bot terminal:\n{response}")
        sys.exit(1)


def play_game():
    proc = start_bot_process()

    res = send_cmd(proc, {"cmd": "new_game"})
    if not res.get("ok"):
        print("Failed to start game:", res)
        return

    state = res["state"]
    target_article = state["target_article"]
    print(f"\n🏎️  RACING: {state['start_article']}  ->  {target_article}\n")

    # Encode the target into a dense vector
    target_emb = model.encode(target_article)
    target_words = set(target_article.lower().split())

    visited = set([state["start_article"]])
    path_history = [state["start_article"]]

    while state["status"] == "playing":
        links_res = send_cmd(proc, {"cmd": "links"})
        links = links_res.get("links", [])
        unvisited_links = [link for link in links if link not in visited]

        if not unvisited_links:
            print("Dead end reached! Giving up.")
            send_cmd(proc, {"cmd": "give_up"})
            break

        # Anti-Rabbit Hole: Penalize words we've seen a lot recently
        recent_articles = path_history[-4:]
        overused_words = {}
        for article in recent_articles:
            for word in article.lower().split():
                if len(word) > 3 and word not in target_words:
                    overused_words[word] = overused_words.get(word, 0) + 1

        best_link = None
        best_score = -100.0

        # Calculate similarity for ALL unvisited links at once (super fast!)
        link_embeddings = model.encode(unvisited_links)

        # Calculate Cosine Similarity between the target and all links
        cosine_scores = util.cos_sim(target_emb, link_embeddings)[0]

        for i, link in enumerate(unvisited_links):
            score = cosine_scores[i].item()  # Base transformer similarity

            # String Overlap Fallback
            link_words = set(link.lower().split())
            overlap = len(target_words.intersection(link_words))
            if overlap > 0:
                score += overlap * 0.3

            # Apply Diversity Penalty
            for word in link_words:
                if word in overused_words:
                    score -= overused_words[word] * 0.15

            if score > best_score:
                best_score = score
                best_link = link

        # Escape Hatch
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


if __name__ == "__main__":
    play_game()
