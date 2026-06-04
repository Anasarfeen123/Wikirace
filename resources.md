# Wikirace.ai — Resources

*Microsoft Innovation Club · MicroCraft: The Summer of Building*

> A curated list of tools, visualizers, papers, and reading material that pair with the Wikirace.ai workshop. Organized by category and difficulty. Drop the relevant links in chat at the right moment — timing column included.

---

## 🎮 Play the Game

| Resource | Link | What it is |
|----------|------|------------|
| **Wikirace.ai** | [wikirace-web.vercel.app](https://wikirace-web.vercel.app) | The live deployed game built in this workshop. Play human vs human or watch the bot. |
| **Wiki Race** | [wiki.halilb.dev](https://wiki.halilb.dev/) | An alternative WikiRace implementation. Good for cross-referencing or side-by-side competition. |

**When to drop:** Pre-show and at the end. Let students play during the pre-show window while waiting for others to join.

---

## 🗺️ Visualize Embeddings

*These tools let you see the semantic space the bot is navigating. Use them to reinforce the semantic map discussion.*

---

### Embedding Projector — Google

[projector.tensorflow.org](https://projector.tensorflow.org/)

Google's official high-dimensional data visualizer. Upload a list of words and watch the AI cluster them in 3D space. You can rotate, zoom, and search for nearest neighbors. Uses the same underlying principles as the model in our bot.

**Best for:** Showing clustering visually after Slide 8. Students can upload the same word list from `visualize.py` and see it in 3D.
**Difficulty:** Beginner

---

### Vector Embedding Simulator

[semicolony.dev/simulators/vector-embedding](https://semicolony.dev/simulators/vector-embedding/)

The exact interactive tool shown on Slide 9. Type a word — cat, dog, car, etc. — and see its query vector with semantic dimension labels (animal · pet · soft). Perfect for students to explore on their own.

**Best for:** Reinforcing the Embeddings slide. Students can type in any word and see how similar or different the coordinates are.
**Difficulty:** Beginner

---

### Word Embeddings Explorer

[embeddings.reiniss.com](https://embeddings.reiniss.com/)

Interactive embedding explorer with a clean interface. Lets you type words and see how they cluster relative to each other. Good for comparing multiple words at once.

**Best for:** Exploring word relationships. Try typing the words from the Human Game — Snake, Spider, Internet — and see how far apart they are.
**Difficulty:** Beginner

---

### Wordviz — Word Embedding Explorer

[wordviz.berrry.app](https://wordviz.berrry.app/)

Visual word embedding explorer. More intuitive interface, great for beginners who find the raw vector numbers intimidating. Shows relationships as visual connections.

**Best for:** Beginners who want a more visual, less numerical take on embeddings.
**Difficulty:** Beginner

---

### Word Embeddings Visualizer (University of Bern)

[word-embeddings.wbkolleg.unibe.ch](https://word-embeddings.wbkolleg.unibe.ch/)

Academic word embedding visualizer with a clean, uncluttered UI. Useful for comparing specific word pairs and seeing similarity scores alongside the visualization.

**Best for:** Students who want to see numerical similarity scores next to the visual.
**Difficulty:** Beginner–Intermediate

---

### Embeddings Viz

[github.com/arindam-sharma/embeddings-viz](https://github.com/arindam-sharma/embeddings-viz)

Open-source embedding visualizer on GitHub. Relevant for students who want to understand how these visualizers are built — or who want to build their own version.

**Best for:** Students who want to go beyond using tools and start building them.
**Difficulty:** Intermediate

---

### Embedding Space Explorer

[williankeller.github.io/embedding-space-explorer](https://williankeller.github.io/embedding-space-explorer/)

Another embedding space visualization tool with interactive controls. Good for exploring the geometry of the space — how words cluster, how far apart concepts are.

**Best for:** Students curious about the geometry of semantic space.
**Difficulty:** Beginner–Intermediate

---

## 🌌 Explore the Wikipedia Knowledge Graph

*See the actual graph the bot is navigating — in 3D.*

---

### Galaxy WikiLoop — 3D Wikipedia Graph

[galaxy.wikiloop.org](https://galaxy.wikiloop.org/)

A 3D visualization of the Wikipedia knowledge graph. You can literally fly through the space that the bot is navigating — articles as nodes, links as edges. One of the most visually stunning resources in this list.

**Difficulty:** Beginner (just explore) · Intermediate (trace specific paths)

---

### Wikipedia 3D Embeddings

[briansunter.github.io/wikipedia-3d-embeddings](https://briansunter.github.io/wikipedia-3d-embeddings/)

Wikipedia articles embedded in 3D space — specifically showing how the AI model would position articles relative to each other. Direct complement to what the bot does internally.

**Difficulty:** Beginner

---

## 📚 Learn the Concepts

*Reading material to go deeper after the workshop. Ordered by difficulty.*

---

### AI Wiki: Embeddings

[aiwiki.ai/wiki/embeddings](https://aiwiki.ai/wiki/embeddings)

Clean, beginner-friendly written explanation of embeddings. Covers the intuition, the math (gently), and real-world applications. The best first reading recommendation for students who want to go deeper after the workshop.

**Best for:** Any student who wants to solidify what they learned today in written form.
**Difficulty:** Beginner

---

### N-grams in NLP — GeeksForGeeks

[geeksforgeeks.org/nlp/n-gram-in-nlp](https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/)

Explains n-grams — one of the traditional NLP approaches that modern embeddings replaced. Reading this helps students understand *why* the old approach had limitations and *what specifically* embeddings improved on.

**Best for:** Students who want historical context — what did AI use before embeddings?
**Difficulty:** Beginner–Intermediate

---

### Attention Is All You Need — Original Paper

[research.google/pubs/attention-is-all-you-need](https://research.google/pubs/attention-is-all-you-need/)

The 2017 paper that introduced transformers — the architecture behind the model used in this workshop, behind ChatGPT, and behind most modern AI systems. Not beginner-friendly in full, but the abstract and introduction are readable.

**Difficulty:** Advanced (full paper) · Intermediate (abstract + intro)

---

### Google Cloud AI Whitepapers

[cloud.google.com/whitepapers](https://cloud.google.com/whitepapers)

Industry-grade explanations of AI concepts, architectures, and best practices. Shows how companies actually deploy the systems that use embeddings, transformers, and semantic search at scale.

**Best for:** Students interested in the engineering and production side — how does this go from a Python script to a product used by millions?
**Difficulty:** Intermediate–Advanced

---

## 🔧 Code and Build

---

### Wikirace.ai GitHub Repository

[github.com/Anasarfeen123/Wikirace](https://github.com/Anasarfeen123/Wikirace)

The full source code for everything built in this workshop. Flask app, bot logic, embedding model integration, visualizer, and Codespace configuration. Fork it and start hacking.

**Things to try after the workshop:**

- Add a new heuristic to the scoring function
- Implement Beam Search instead of Greedy
- Add a visited-article memory with a longer window
- Build a leaderboard for bot race results
- Swap in a different embedding model and compare performance

**Difficulty:** Beginner (tweaking parameters) · Intermediate (new features) · Advanced (architecture changes)

---

### sentence-transformers Library

[sbert.net](https://www.sbert.net/)

The Python library powering the bot's AI brain. Excellent documentation, dozens of pre-trained models, and clear examples. The model we used (`all-MiniLM-L6-v2`) is listed here with benchmarks and comparisons.

**Things to explore:**

- Compare `all-MiniLM-L6-v2` against larger models
- Try multilingual models for non-English WikiRace
- Read the semantic similarity benchmarks

**Difficulty:** Intermediate

---

### Hugging Face — all-MiniLM-L6-v2

[huggingface.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

The model card for the exact AI model used in this workshop. Shows training data, benchmark scores, intended uses, limitations, and how to load it. Reading a model card is a core skill for anyone working with AI.

**Difficulty:** Beginner (reading the card) · Intermediate (understanding the benchmarks)

---

## 📋 Quick Drop Schedule

*When to paste each link into workshop chat, in order.*

| Time | What to drop | Link |
|------|-------------|------|
| Pre-show (T-10) | Live game | wikirace-web.vercel.app |
| Pre-show (T-10) | Alternative game | wiki.halilb.dev |
| Break 1 | Vector simulator | semicolony.dev/simulators/vector-embedding |
| Break 1 | Embeddings explorer | embeddings.reiniss.com |
| Break 1 | Wordviz | wordviz.berrry.app |
| After Slide 8 | Embedding Projector | projector.tensorflow.org |
| Break 2 | Wikipedia 3D Graph | galaxy.wikiloop.org |
| Break 2 | Wikipedia 3D Embeddings | briansunter.github.io/wikipedia-3d-embeddings |
| After Attention section | Original transformer paper | research.google/pubs/attention-is-all-you-need |
| Thank You slide | GitHub repo | github.com/Anasarfeen123/Wikirace |
| Thank You slide | AI Wiki embeddings | aiwiki.ai/wiki/embeddings |
| Thank You slide | Model card | huggingface.co/sentence-transformers/all-MiniLM-L6-v2 |

---

## 🗂️ All Links at a Glance

```
PLAY
  wikirace-web.vercel.app
  wiki.halilb.dev

VISUALIZE EMBEDDINGS
  projector.tensorflow.org
  semicolony.dev/simulators/vector-embedding
  embeddings.reiniss.com
  wordviz.berrry.app
  word-embeddings.wbkolleg.unibe.ch
  github.com/arindam-sharma/embeddings-viz
  williankeller.github.io/embedding-space-explorer

EXPLORE WIKIPEDIA GRAPH
  galaxy.wikiloop.org
  briansunter.github.io/wikipedia-3d-embeddings

READ
  aiwiki.ai/wiki/embeddings
  geeksforgeeks.org/nlp/n-gram-in-nlp
  research.google/pubs/attention-is-all-you-need
  cloud.google.com/whitepapers

CODE
  github.com/Anasarfeen123/Wikirace
  sbert.net
  huggingface.co/sentence-transformers/all-MiniLM-L6-v2
```

---

*Wikirace.ai · Microsoft Innovation Club · MicroCraft: The Summer of Building*
