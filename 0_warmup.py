#!/usr/bin/env python3
"""Download the AI model before the first bot run."""

from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def main() -> None:
    print("WikiRace AI warmup")
    print(f"Downloading/loading model: {MODEL_NAME}")
    print("This can take a few minutes on slow internet. Please keep this window open.")
    SentenceTransformer(MODEL_NAME)
    print("")
    print("Warmup complete. The AI model is ready for the bot.")


if __name__ == "__main__":
    main()
