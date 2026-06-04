# Wikirace.ai — Complete Workshop Playbook v4.0
### A 2–3 Hour Online Beginner-Friendly AI/ML Workshop
*by Anas Arfeen · Microsoft Innovation Club · MicroCraft: The Summer of Building*

> **Changelog v4.0:** Updated to match the final 23-slide Canva deck (Wikirace_ai-3.pdf).
> The "Loading…" pre-show slide replaces "Get Ready." Two BRB break slides are now confirmed in the deck.
> Bot Psychology (Slides 11–16), Failure Analysis (17), Search Algorithms (18), and Attention (19) are all now live slides — updated from "suggested additions" to confirmed scripts.
> Closing logo slide (23) added. All slide numbers now match the deck exactly.

---

> **How to use this document:**
> Section 1 = master timeline and phase structure
> Section 2 = slide-by-slide design reference (all 23 slides)
> Section 3 = complete word-for-word speaking script
> Section 4 = demo and Codespace flow
> Section 5 = beginner confusion guide
> Section 6 = live failure recovery guide
> Section 7 = energy and engagement guide
> Appendix A = quick-reference cheat card
> Appendix B = all resources with drop timing
> Appendix C = remaining slide improvement suggestions

---

# SECTION 1 — COMPLETE WORKSHOP STRUCTURE

## The Philosophy of This Workshop

Most AI workshops do this:
```
Here are embeddings. Here is code. Done.
```

This one does this:
```
Human Game (feel the problem)
    ↓
Human Thinking Debrief (how do YOU navigate meaning?)
    ↓
Semantic Meaning (how does AI represent meaning?)
    ↓
Embeddings (what do the numbers look like?)
    ↓
⏸ BREAK 1 (BRB Slide)
    ↓
Bot Psychology — 4 personalities (what decision does each bot make?)
    ↓
Exploration vs Exploitation (the big reveal)
    ↓
Failure Analysis (why does a smart bot still fail?)
    ↓
Search Algorithms (should AI look one step or many?)
    ↓
Attention — the "it" Exercise (how does AI know which words matter?)
    ↓
⏸ BREAK 2 (BRB Slide)
    ↓
Coding + Parameter Tuning (training behavior, not writing code)
    ↓
Bot Tournament (competition with stakes)
    ↓
Thank You + Logo Outro
```

Almost none of the depth requires code.
It requires **experiments, predictions, failures, and debates.**
That's what makes a 2–3 hour workshop feel like a real AI education
rather than a glorified demo.

---

## The Complete 23-Slide Deck Map

| Slide # | Title | Phase | Type |
|---------|-------|-------|------|
| 1 | Loading… (MicroCraft) | Pre-show | Holding |
| 2 | Wikirace.ai Title | Opening | Cinematic |
| 3 | Human Game — Question | Phase 2 | Interactive |
| 4 | Human Game — Bad Path | Phase 2 | Reveal |
| 5 | Human Game — Re-challenge | Phase 2 | Interactive |
| 6 | Human Game — Good Path | Phase 2 | Reveal |
| 7 | Humans Think Weirdly | Phase 3 | Debrief |
| 8 | How AI Understands Meaning? | Phase 4 | Visual |
| 9 | Embeddings | Phase 5 | Technical |
| 10 | Be Right Back (Break 1) | Break | Pause |
| 11 | Bot Psychology: Meet the Bots | Phase 6 | Overview |
| 12 | Greedy Bot | Phase 6 | Deep Dive |
| 13 | Explorer Bot | Phase 6 | Deep Dive |
| 14 | Random Bot | Phase 6 | Deep Dive |
| 15 | Looping Bot | Phase 6 | Deep Dive |
| 16 | Exploration vs Exploitation | Phase 6 | Big Reveal |
| 17 | Failure Analysis | Phase 7 | Analysis |
| 18 | Search Algorithms | Phase 8 | Concept |
| 19 | Attention: The "it" Exercise | Phase 9 | Surprise |
| 20 | Be Right Back (Break 2) | Break | Pause |
| 21 | IT'S CODING TIME | Phase 11 | Transition |
| 22 | Thank You | Phase 14 | Close |
| 23 | Wikirace.ai Logo Outro | Phase 14 | Outro |

---

## Master Timeline (3-Hour Full Version)

```
PRE-SHOW     │  Slide 1: Loading… + vibe            T-15 min
─────────────┼──────────────────────────────────────────────
PHASE 1      │  Slide 2: Title                      0:00–0:05
PHASE 2      │  Slides 3–6: Human Game              0:05–0:22
PHASE 3      │  Slide 7: Human Thinking Debrief     0:22–0:28
PHASE 4      │  Slide 8: Semantic Meaning           0:28–0:40
PHASE 5      │  Slide 9: Embeddings                 0:40–0:50
─────────────┼──────────────────────────────────────────────
             │  ⏸ BREAK 1 — Slide 10 (BRB)         0:50–0:58
─────────────┼──────────────────────────────────────────────
PHASE 6      │  Slides 11–16: Bot Psychology        0:58–1:22
PHASE 7      │  Slide 17: Failure Analysis          1:22–1:34
PHASE 8      │  Slide 18: Search Algorithms         1:34–1:47
PHASE 9      │  Slide 19: Attention Exercise        1:47–1:57
─────────────┼──────────────────────────────────────────────
             │  ⏸ BREAK 2 — Slide 20 (BRB)         1:57–2:07
─────────────┼──────────────────────────────────────────────
PHASE 11     │  Slide 21: Coding Time + Onboarding  2:07–2:22
PHASE 12     │  Bot Runs + Parameter Tuning         2:22–2:42
PHASE 13     │  Bot Tournament                      2:42–3:02
PHASE 14     │  Slides 22–23: Thank You + Outro     3:02–3:10
```

## Condensed Timeline (2-Hour Version)

Cut Phases 8–9 and the Research Discussion. Use this:
```
PRE-SHOW     │  T-10 min
PHASE 1–3    │  Slides 2–7: Human Game + Debrief   0:00–0:25
PHASE 4–5    │  Slides 8–9: Meaning + Embeddings   0:25–0:42
             │  ⏸ BREAK — Slide 10                 0:42–0:50
PHASE 6      │  Slides 11–16: Bot Psychology       0:50–1:10
PHASE 7      │  Slide 17: Failure Analysis         1:10–1:20
PHASE 11–12  │  Slides 20–21: Coding + Tuning      1:20–1:48
PHASE 13–14  │  Tournament + Wrap                  1:48–2:00
```

---

## Phase-by-Phase Summary

### PHASE 1 — Title (Slide 2, 0:00–0:05)
Energy: maximum. Silence for 5 seconds. Then one sentence. Go.

### PHASE 2 — The Human Game (Slides 3–6, 0:05–0:22)
Four slides, one story: Snake → Internet. Run it as a game show. Never advance before chat responds.

### PHASE 3 — Human Thinking Debrief (Slide 7, 0:22–0:28)
Side-by-side comparison. Bridge from "humans think weirdly" to "here's how AI thinks."

### PHASE 4 — Semantic Meaning (Slide 8, 0:28–0:40)
The semantic map. Visual, exploratory, cluster-guessing game. First "wow" moment. Slow down. Let it breathe.

### PHASE 5 — Embeddings (Slide 9, 0:40–0:50)
Cat = [0.70, 0.20, 0.10, 0.60]. Connect numbers to the map. End with the Embedding Surgery exercise (verbal, no slide needed). Transition to BRB.

### BREAK 1 — Slide 10: Be Right Back
Show the BRB slide. Drop Codespace link, drop embedding tool link. 8 minutes.

### PHASE 6 — Bot Psychology (Slides 11–16, 0:58–1:22)
Six confirmed slides. Four bot personalities — Greedy, Explorer, Random, Looping. Each has its own deep-dive slide. Run each with a question before showing the visual. Reveal Exploration vs Exploitation only AFTER all four bots. This is the most conceptually rich phase.

### PHASE 7 — Failure Analysis (Slide 17, 1:22–1:34)
Bot path that goes Snake → Reptile → Animal → Life → Existence → Philosophy → ❌. Students diagnose the failure. They become AI researchers.

### PHASE 8 — Search Algorithms (Slide 18, 1:34–1:47)
Three panels: Greedy, Beam, A*. No math. All intuition. Students vote on which approach they'd add to the bot.

### PHASE 9 — Attention (Slide 19, 1:47–1:57)
The pronoun exercise. Two sentences. One flip. The cognitive surprise is the lesson.

### BREAK 2 — Slide 20: Be Right Back
Show the second BRB slide. Drop Galaxy WikiLoop and 3D embedding links. 10 minutes.

### PHASE 11 — IT'S CODING TIME (Slide 21, 2:07–2:22)
Come back loud. Onboard into Codespace. First live run.

### PHASE 12 — Parameter Tuning as Personality Training (2:22–2:42)
Students vote on parameter values. Observe what personality emerges. They are not writing code — they are training behavior.

### PHASE 13 — Bot Tournament (2:42–3:02)
Same race. Different configs. Announce like a sports commentator. Chaos Bot finale.

### PHASE 14 — Thank You + Outro (Slides 22–23, 3:02–3:10)
Slide 22: warm, brief. Slide 23: logo holds on screen as people leave.

---

---

# SECTION 2 — SLIDE-BY-SLIDE DESIGN REFERENCE

All 23 slides are confirmed from the Canva deck. Notes describe what is on-screen plus presenter context.

---

### SLIDE 1 — Loading… (MicroCraft: The Summer of Building)
**What's on screen:** MicroCraft logo top-center, cute planet/loading character with sparkles, "LOADING…." text bottom-center. Purple-to-crimson gradient background.
**Purpose:** Pre-show holding slide. Creates atmosphere while people join.
**Presenter action:** Play music. Drop Codespace link in chat. Read names casually. Keep energy warm but calm.
**Improvement note:** The "Loading…" character is charming and sets an approachable tone. No changes needed.

---

### SLIDE 2 — Wikirace.ai Title
**What's on screen:** Large "Wikirace.ai" title with ".ai" in teal/cyan. "Navigate knowledge. Faster than humans." subtitle. Floating path labels orbiting the Wikipedia globe: Chess→Game Theory, Python→Black Hole, Cricket→Neural Networks, Elon Musk→SpaceX, Music→Fourier Transform, Machine Learning→Google. Circuit board corner decorations. Microsoft Innovation Club logo top-right.
**Purpose:** Formal opening. Hook the room.
**Presenter action:** 5 full seconds of silence. Then: "Today you're going to build an AI."
**Animation suggestion:** Path labels should type-in one by one on loop.

---

### SLIDE 3 — The Human Game (Question): Snake → ? → Internet
**What's on screen:** Title "The Human Game." Snake icon left. Internet/person icon right. Large animated question mark in center. Caption: "What path should we take?"
**Purpose:** Pose the challenge. Get chat active before anything is revealed.
**Interaction:** Do not advance until 5+ chat responses. Read each one aloud.

---

### SLIDE 4 — The Human Game (Bad Path): Snake → Hyper-Carnivorous → Spider → Spider-web → WWW → Internet 😭
**What's on screen:** Same layout but the full bad path revealed with labeled icons and arrows. Caption: "This is what I took 😭!"
**Critical animation note:** Each hop must reveal on a separate click. Not all at once. This is the most important single animation in the deck.
**Purpose:** Comedic reveal. Build empathy. The laugh is the lesson.

---

### SLIDE 5 — The Human Game (Re-Challenge): Snake → ? → Internet
**What's on screen:** Visually similar to Slide 3. Caption: "What other path can we take?"
**Improvement note:** Add a Round 2 signal (gold question mark, or a "Round 2 →" badge top-right) so students know this isn't a repeat.
**Interaction:** Wait 2 minutes. Read suggestions. React.

---

### SLIDE 6 — The Human Game (Good Path): Snake → Venomous Snake → List of fatal snake bites → New York City → AI → Internet Traffic → Internet
**What's on screen:** Full good path with labeled icons and arrows. Caption: "This is what my friend took 🙌!"
**Purpose:** Smart path reveal. Longer in clicks but semantically coherent.
**Animation note:** Each hop reveals separately, same as Slide 4.

---

### SLIDE 7 — Humans Think Weirdly
**What's on screen:** Two labeled paths side by side:
- "Mine" (green/italic): Snake→Hyper-Carnivorous→Spider→Web→WWW→Internet 😭
- "My Friend's" (purple/italic): Snake→Venomous snake→List of fatal snake bites…→Internet
**Purpose:** Debrief. Bridge to AI. The contrast sets up the semantic meaning section.
**Improvement note:** Add a small annotation on Friend's path: "each hop is semantically related to the next."

---

### SLIDE 8 — How Does AI Understand Meaning?
**What's on screen:** Semantic scatter plot on black background. Words plotted as colored dots in clusters: Dog, Cat, Snake near each other; Car, Truck, Bicycle, Motorcycle in another cluster; Internet, World Wide Web near each other; Spider, Spider-web nearby. Color-coded cluster legend top-right. Caption: "Dog ≈ Cat"
**Purpose:** First visual "wow" moment. Cluster-guessing game.
**Improvement note:** Draw faint dotted arrow trails for both human paths on the map so students see their routes through meaning space.

---

### SLIDE 9 — Embeddings
**What's on screen:** Two query vector panels:
- "cat" selected: [0.70, 0.20, 0.10, 0.60] · animal · pet · soft
- "dog" selected: [0.70, 0.30, 0.10, 0.50] · animal · pet · loud
Caption: "These coordinates are called embeddings."
**Purpose:** Connect the visual map to actual numbers.
**Improvement note:** Add a third contrasting word (Car or Guitar) to make the numerical difference visually obvious.

---

### SLIDE 10 — Be Right Back (Break 1)
**What's on screen:** Illustration of person at desk with checklist and coffee cup. Code visible on monitor. Text: "Be Right Back" in pink gradient script. Bottom note: "Italian Breakfast" (references a checklist item on the paper in the illustration).
**Purpose:** Official break slide 1. Signals a pause without just going dark.
**Presenter action:** Drop Codespace link, drop semicolony embedding tool. Say the three break tasks. Set a timer. Come back in 8 minutes.

---

### SLIDE 11 — Bot Psychology: Meet the Bots
**What's on screen:** Title "Bot Psychology: Meet the Bots." Four rows, each with an icon + bold name + one-line description:
- 💰 Greedy Bot — "Always picks the highest score"
- 🧭 Explorer Bot — "Willing to score lower to go further"
- 🎲 Random Bot — "Chooses randomly."
- ♾ Looping Bot — "Gets trapped. Can't escape"
**Purpose:** Overview. Students see all four personalities before diving in.
**Animation:** Cards reveal one by one on click. Ask for predictions before revealing each.

---

### SLIDE 12 — Greedy Bot
**What's on screen:** Title "Greedy Bot." Decision tree diagram with numbered nodes. The greedy path highlighted in pink/red — it goes 7→12→6→9, following the highest value at each node. "Missed!" label with green arrow pointing to the 99 node that it skipped. "Too greedy?" label with red arrow on the node it got stuck at.
**Purpose:** Visual proof that always picking highest value locally misses globally better options.
**Key visual:** The 99 node is right there, but the greedy path never reaches it because it always turned toward the next-highest local node.

---

### SLIDE 13 — Explorer Bot
**What's on screen:** Title "Explorer Bot." BFS (breadth-first search) tree visualization. Nodes 1–5 highlighted in light blue as explored nodes, with remaining nodes shown as outlines. The path explores multiple branches (1→2→3→4, then 2→5) rather than committing to one.
**Purpose:** Visual contrast to Greedy Bot — breadth-first style means the Explorer considers multiple paths simultaneously.

---

### SLIDE 14 — Random Bot
**What's on screen:** Title "Random Bot." 6×6 grid of dots (nodes). A random walk path traced in red/pink — the path wanders erratically, going down and sideways with no clear directional logic, ending at the bottom-right.
**Purpose:** Shows that randomness has no direction — but its erratic path occasionally stumbles into new territory.

---

### SLIDE 15 — Looping Bot
**What's on screen:** Title "Looping Bot." Linked list diagram with nodes 0→1→2→3→4, then a cycle: 4→5→6→7→8→9→10→11→12→4 (back to 4). Node 6 highlighted in orange (labeled "h" for head of cycle). The loop is clearly visible.
**Purpose:** Shows the trap — the bot keeps circling the same nodes because it lacks memory or a diversity penalty.
**Credit note:** Diagram credited to InterviewBit (shown bottom-left).

---

### SLIDE 16 — Exploration vs Exploitation
**What's on screen:** Title "Exploration vs Exploitation." Subtitle: "One of the most fundamental concepts in all of AI" in purple italic. Large double-headed hand-drawn arrow across the center: "Exploration" on the left, "Exploitation" on the right.
**Purpose:** THE big reveal. This slide appears AFTER all four bot discussions. Students already understand the concept intuitively — now they get the vocabulary.
**Critical timing note:** Do not show this slide until all four bots have been discussed. The power is that students already understand the concept before hearing the term.

---

### SLIDE 17 — Failure Analysis
**What's on screen:** Title "Failure Analysis." A path chain with icons and labels: Snake→Reptile→Animal→Life→Existence→Philosophy. A red ✕ mark sits between Philosophy and Internet (the target). Internet is on the right side with the person icon. The path clearly went in the wrong direction despite looking locally reasonable.
**Purpose:** Students diagnose why a seemingly reasonable path fails. They become AI researchers.

---

### SLIDE 18 — Search Algorithms
**What's on screen:** Title "Search Algorithms." Three panels side by side separated by decorative stands:
- "Greedy Search" (left): graph with red-highlighted node A(5) and path going A→B
- "Beam Search" (center): full tree with multiple expanding paths
- "A* Search" (right): same graph as Greedy but with B(3) highlighted — the algorithm considered the total cost, not just the next step
**Purpose:** Visual comparison of three search strategies. No math. Just the pattern.

---

### SLIDE 19 — Attention: The "it" Exercise
**What's on screen:** Title "Attention: The 'it' Exercise." Two large italic sentences:
- "The animal didn't fit in the suitcase because **it** was too big."
- "The suitcase didn't fit in the car because **it** was too big."
"it" is underlined/bold in both sentences. No answer on the slide — it's the question.
**Purpose:** Teach the core intuition of the Attention mechanism through a cognitive surprise. Two sentences. One flip. The experience IS the explanation.

---

### SLIDE 20 — Be Right Back (Break 2)
**What's on screen:** Same visual as Slide 10 (person at desk, code on screen, coffee). Text: "Be Right Back."
**Purpose:** Official break slide 2. Signals transition from conceptual to coding mode.
**Presenter action:** Drop Galaxy WikiLoop and 3D embedding links. Say: "When you come back, we're switching from watching to doing." 10 minutes.

---

### SLIDE 21 — IT'S CODING TIME
**What's on screen:** Pink/yellow bold blocky text "ITS' CODING TIME." Confetti cannon left. Astronaut floating right, holding a glowing terminal screen. Code symbols at bottom: {} </> >_() ✦.
**Purpose:** Full energy mode-switch. From audience to participants.
**Presenter action:** Come back from break loud. Read the slide out loud. Drop Codespace link. Ask for 🚀 in chat.

---

### SLIDE 22 — Thank You
**What's on screen:** Large white cursive "Thank You" text. Yellow rose. Red/pink floating hearts. Circuit board corners. Wikirace.ai branding bottom-left. Microsoft Innovation Club logo bottom-right.
**Purpose:** Warm close. Let it breathe for 3 seconds before speaking.

---

### SLIDE 23 — Wikirace.ai Logo Outro
**What's on screen:** Pitch black background. Only the "Wikirace.ai" logo centered in white/teal with the spark mark. Nothing else.
**Purpose:** Clean, minimal close. Holds on screen as people leave or take screenshots. No text. No distractions.
**Presenter action:** Leave this on screen after saying your final words. No need to narrate it. Let the room close naturally.

---

---

# SECTION 3 — COMPLETE SPEAKING SCRIPT

> Normal text = say this.
> *[Italics in brackets]* = stage directions.
> **Bold** = words to emphasize.
> 💬 = chat interaction moment.

---

## PRE-SHOW — SLIDE 1 (Loading…)

*[Music playing. Loading slide on screen. Welcome people casually as they join.]*

"Hey — if you can hear me, drop a 👋 in chat."

*[Read names. Keep it casual.]*

"GitHub link is pinned. Click Code → Codespaces → Create codespace on main. Takes 2 minutes. Do it now so it's ready when we need it. No setup required on your end — everything is pre-installed."

*[If early: drop the live game link.]*
"While we wait — that link is the actual WikiRace game. Try it. Snake → Internet. See how many clicks you need."

---

## SLIDE 2 — Wikirace.ai Title

*[Wait 5 seconds on the title slide. Full silence.]*

"Today you're going to build an AI."

*[Pause.]*

"Before I explain a single thing about how it works, I want you to play the game that inspired it. Because the best way to understand what we built is to feel the problem yourself first."

---

## SLIDES 3–6 — The Human Game

### Slide 3

"WikiRace. You start on one Wikipedia article, click links to jump to others, and try to reach a target article in as few clicks as possible. No search bar. Only links."

"Today's challenge: **Snake** to **Internet**."

"You're on the Snake Wikipedia page right now. What is your **first click?** Type it in chat."

💬 *[Wait. Read responses. React to each one by name.]*

"Someone said 'Reptile.' Solid. Someone said 'Venom.' Love it. Someone said 'Python' — as in the programming language? That's actually interesting — we'll come back to that."

*[After 3 minutes of chat.]*

"Okay. Here's what I did."

---

### Slide 4 — Bad Path (reveal each hop on a separate click)

*[Click once. First hop appears.]*

"I clicked… **Hyper-Carnivorous**."

*[Wait for reactions.]*

"Because snakes eat things. And the Hyper-Carnivorous article is about animals that primarily eat meat. Logic: impeccable. Direction: completely useless."

*[Click. Second hop.]*

"From Hyper-Carnivorous, I clicked **Spider**. Also a predator. Still following animal behavior logic. Still very wrong."

*[Click. Third hop.]*

"**Spider-web**."

*[Click. Fourth hop.]*

"**World Wide Web**."

*[Let the silence land. Students see where this is going.]*

*[Click. Final hop.]*

"**Internet**."

*[Pause.]*

"I made it. 5 clicks. Snake → Hyper-Carnivorous → Spider → Spider-web → World Wide Web → Internet. 😭"

"I navigated from a reptile to the internet by following a chain of predators until I accidentally stumbled into a computer science metaphor."

💬 "Type in chat: would you have thought of this path?"

*[Read responses. Laugh with them.]*

"Now — you've seen what doesn't work. Can you do better?"

---

### Slide 5 — Re-Challenge

"Round 2. Same race. Type your first click — but this time, knowing what you know."

💬 *[Wait 2 minutes. Read suggestions.]*

"Someone said 'Venomous snake.' Interesting. Someone said 'Biology.' Classic broad-topic move. Someone said 'Internet Protocol' — wait, are you on Wikipedia right now? Stop cheating."

*[Laugh. Move on.]*

"Here's what my friend did."

---

### Slide 6 — Good Path (reveal each hop separately)

*[Reveal each hop individually.]*

"**Venomous snake.** Why? It's a sub-article of Snake that immediately gets more specific."

"**List of fatal snake bites in the United States.** Why? A list article about deaths in the US will have geography links."

"**New York City.** Major US geography — makes total sense."

"**Artificial intelligence.** New York has a massive AI industry and Wikipedia reflects that."

"**Internet traffic.** AI and Internet traffic are deeply connected — AI runs on the internet."

"**Internet.** Done."

*[Pause.]*

"7 clicks. Mine was 5. My friend's path is **longer**. But which one feels **smarter**?"

💬 "Type A for mine, B for my friend's."

*[Read results.]*

"Almost everyone says my friend's. Why? We'll answer that in the next few minutes."

---

## SLIDE 7 — Humans Think Weirdly

"Look at both paths on screen."

"My path worked by **coincidence** — predator logic accidentally found a vocabulary bridge to tech. If the English language didn't use the word 'web' for both spider webs and the World Wide Web, my path fails completely."

"My friend's path worked by **meaning** — every hop follows semantic coherence. Venomous snakes and fatal bites are genuinely related. Fatal bites and US geography are genuinely related. US geography and New York are related. New York and AI are related."

"My friend followed **meaning chains**. I followed **word association chains**. They look similar but they're completely different strategies."

"Here's the question: how do we teach an AI to follow meaning chains?"

💬 "Type in chat: one word for the strategy my friend used."

*[Common answers: 'semantic,' 'logical,' 'topic,' 'meaning,' 'connected.']*

"Someone said 'semantic.' That's the exact word. Semantic means 'related to meaning.' And the answer to how AI does this is that it converts every word into coordinates — so that words with similar meanings end up close to each other in space."

---

## SLIDE 8 — How Does AI Understand Meaning?

*[Let the semantic map sit for 5 full seconds of silence.]*

"Nobody labeled these clusters. Nobody told this AI that Snake, Wolf, and Spider belong together. Nobody told it that Car and Truck are related. The AI figured this out by reading billions of sentences and noticing which words appear in similar contexts."

"And then — this is the key move — it gave every word **coordinates**. Like GPS. Words with similar meanings end up close together on this map."

"Dog ≈ Cat. Their coordinates are so similar they're almost touching on the plot."

"Cluster guessing game. I'll point, you type."

💬 *[Point to animal cluster: Dog, Cat, Wolf, Snake.]*
"This cluster — one word. What do these share?"
→ Animals.

💬 *[Point to vehicle cluster: Car, Truck, Bicycle, Motorcycle.]*
→ Vehicles / Transport.

💬 *[Point to web/internet cluster: Internet, World Wide Web, Spider-web.]*
"Now THIS one is interesting. What do these share?"
→ Web / network / connected.

"Notice something: Spider-web is close to World Wide Web on this map. That's why my terrible path actually worked — it was **geographically valid** in meaning space. Just not the most direct route."

"My path was like taking a detour through a related neighborhood. My friend's path was the highway."

---

## SLIDE 9 — Embeddings

"Here's what the coordinates actually look like as numbers."

"Cat: [0.70, 0.20, 0.10, 0.60]. Labeled: animal, pet, soft."

"Dog: [0.70, 0.30, 0.10, 0.50]. Labeled: animal, pet, loud."

"Look at the first number. 0.70 for both. That's the dimension that captures 'animal-ness.' Cat and dog score the same on that dimension."

"The last number differs: 0.60 vs 0.50. One dimension where their personality differs — soft vs loud."

"These coordinates are called **embeddings**. Every Wikipedia article in our bot gets embedded — converted to a list of numbers like this, but 384 numbers instead of 4. The bot picks its next click by asking: which linked article's coordinates are closest to the target?"

💬 "Quick prediction: if I embedded the word 'Python,' would it be closer to Snake, or closer to Computer? Type S for Snake, C for Computer."

*[Read responses. A split is perfect — this is the key insight.]*

"The answer is: **it depends on context.** Python the snake → near Snake. Python the programming language → near Computer. The same word gets different coordinates depending on what surrounds it. That's called **contextual understanding** — and it's why modern AI works so much better than older systems."

---

### Embedding Surgery (verbal exercise — no slide needed, or use Slide 9 still on screen)

"Before we break, a quick experiment. I call it Embedding Surgery."

"Five words: Dog, Cat, Wolf, Tiger, Lion."

💬 "Which one doesn't belong?"

*[Students will disagree — domestic vs wild, canine vs feline. Multiple valid answers.]*

"Interesting — people disagree, and that's the point. Dog and Cat would form a tiny cluster within the animal cluster because they appear in domestic contexts. Wolf, Tiger, Lion appear in wild contexts."

"Now: Dog, Cat, Wolf, **Python**, Tiger."

💬 "What happened to this cluster? What's different?"

*[Students notice Python.]*

"Exactly. Python's embedding gets pulled toward both the animal cluster AND the programming cluster. It's sitting between two neighborhoods in meaning space. That's not a bug — that's the AI correctly capturing that Python genuinely has dual meaning."

"Fix: give the AI more context. 'Python programming language' vs 'Python constrictor snake.' Context collapses the ambiguity."

---

## SLIDE 10 — Be Right Back (Break 1)

*[Show the BRB slide.]*

"7–8 minutes. Three tasks while you're out:"

"One: make sure your Codespace is open — link is pinned."

"Two: open `embedding_bot.py`. Find the line that says `score += overlap * 0.3`. Just look at it."

"Three: try this link — it's the interactive embedding tool shown on the Embeddings slide. Type in some words and see their vectors."

*[Drop: https://semicolony.dev/simulators/vector-embedding/]*

"Back in 8."

---

## PHASE 6 — BOT PSYCHOLOGY

## SLIDE 11 — Bot Psychology: Meet the Bots

*[Come back from break at medium energy — save the big energy for the coding transition.]*

"Welcome back. We've been talking about how AI understands meaning. Now: **how AI makes decisions.**"

"Even if the AI perfectly understands what every word means — it still has to decide: which word to go to next?"

"The answer to that question defines the bot's **personality**."

"I'm going to show you four bots. Each has a different strategy. Your job: predict what goes wrong with each one before I show you."

*[Reveal each bot card individually.]*

"Greedy Bot. Explorer Bot. Random Bot. Looping Bot."

"Each one is a real AI decision-making strategy. Each one has a specific flaw. Let's find them."

---

## SLIDE 12 — Greedy Bot

*[Show the tree diagram. Students see the "Too greedy?" label and the missed 99 node.]*

"The Greedy Bot's rule: at every step, pick the link with the highest similarity score to the target. Maximum score. Always."

💬 "Before I explain what happens — is this smart or shortsighted? Type S for Smart, SH for Shortsighted."

*[Read responses. Let both sides speak.]*

"Here's what the tree is showing us. The bot starts at 7. It sees two children: 3 and 12. 12 is higher — it goes there. From 12, it sees 6 and 5. 6 is higher — goes there. From 6, it sees 2 and 9. 9 is higher — goes there."

"But look over on the left. Node 1 leads to 99. The actual best possible leaf. The greedy bot never got there because it always turned right toward the locally higher option."

"**Shortsighted.** It optimized perfectly at every individual step and failed at the global level. This is called a **local optimum** — it thought it was at the top of the mountain, but it was actually on a small hill."

💬 "Real-life example: a decision that seems smart locally but fails globally. Type one."

*[Read: investing in one stock, specializing too early, taking a shortcut that's actually longer.]*

"Exactly. The Greedy Bot makes the AI equivalent of those decisions."

---

## SLIDE 13 — Explorer Bot

*[Show the BFS tree. Blue nodes representing explored paths spreading across multiple branches.]*

"The Explorer Bot has a different rule. It's willing to deliberately take a lower-scoring step sometimes, to avoid getting trapped."

💬 "Why would intentionally making WORSE choices help? Think for 10 seconds, then type."

*[Read responses.]*

"The tree shows it. Instead of always going one path deep, the Explorer keeps multiple options alive — it expands level by level. It goes 1→2, 1→3, 1→4 before diving deeper on any of them."

"Hiking analogy: Greedy Bot always walks uphill. It gets to the top of the nearest hill, which might not be the actual summit. Explorer Bot sometimes walks sideways to find a better path to the real peak."

"In the bot code: this is the **diversity penalty**. When the bot has been visiting the same type of article too many steps in a row, it deliberately weights those article types lower — forcing itself to explore."

💬 "Is the Explorer always better than the Greedy Bot? Type yes, no, or 'it depends.'"

*[Most say 'it depends.']*

"Exactly. Short races with a clear semantic path — Greedy wins because it's faster. Long races across disconnected topics — Explorer wins because it doesn't get trapped."

"You just described the **exploration-exploitation tradeoff.** We'll name it properly in a moment."

---

## SLIDE 14 — Random Bot

*[Show the grid random walk. The red path wanders erratically across the grid.]*

"The Random Bot. It reads all the links. Calculates zero scores. Picks randomly."

"Look at that path. Down, sideways, down, sideways again. No direction. Pure chaos."

💬 "Can randomness ever be useful in AI? Type yes, no, or explain."

*[Read responses.]*

"Most instincts say no. Here's the surprising truth: **randomness is useful in AI constantly.**"

"Random restarts: when an AI is stuck in a local optimum, the best fix is often to reset and try from scratch randomly."

"Random initialization: neural networks start with random weights before training. Starting at zero, they'd all learn the same thing — randomness breaks the symmetry."

"Epsilon-greedy: some reinforcement learning systems choose the best option 90% of the time, and choose randomly 10% of the time. That 10% randomness discovers things it never would have found otherwise."

"The Random Bot alone? Useless. A tiny injection of randomness into a smart bot? Often what makes it actually work."

---

## SLIDE 15 — Looping Bot

*[Show the linked list with the cycle. Nodes 0→1→2→3→4, then the cycle 4→5→6→7→8→9→10→11→12→4 repeating.]*

"The Looping Bot. It uses similarity scores, has no diversity penalty, and ends up visiting the same articles over and over."

"This diagram shows exactly what happens — it progresses linearly for a while, then hits a cycle. Node 6 is the trap — highlighted in orange, labeled as the head of the loop. Once it enters the cycle, it spins forever."

💬 "Why is it repeating itself? What's missing? Just from thinking about it — type your answer."

*[Read responses.]*

"Two things are missing: **memory** and **penalty**."

"Memory — without tracking visited nodes, the bot can literally return to the same article twice. Our bot has a visited set, which prevents exact repeats."

"But even with a visited set, you can get *soft loops* — visiting different articles within the same semantic cluster repeatedly because they all score similarly relative to the target. Nothing blocks you from circling the same neighborhood of ideas."

"The diversity penalty solves soft loops. We'll tune that in the lab."

💬 "Quick poll: which bot most resembles how you navigated in the human game? Greedy, Explorer, Random, or Looping? Type G, E, R, or L."

*[Read results. Comment on the split.]*

"Most humans are actually **Explorer bots** — they follow high-scoring paths but take lateral steps when stuck. The bot we built tries to replicate that."

---

## SLIDE 16 — Exploration vs Exploitation

*[Hold this slide for 3 seconds before speaking.]*

"Let me give you the name for what you just spent 20 minutes figuring out."

*[Reveal or gesture to the slide.]*

"**Exploration vs Exploitation.**"

"Exploitation: use what you know works. Pick the highest score. Go for the best you've found."

"Exploration: risk going somewhere worse in hopes of finding something better."

"This tradeoff is fundamental to almost every AI system that makes decisions over time:"

"Game-playing AI: exploit known good moves vs explore new strategies."
"Recommendation systems: show you what you've liked before vs recommend something new."
"Drug discovery AI: test variations of known compounds vs explore completely new structures."
"Wikipedia navigation: go toward the target vs escape a bad cluster."

"You just taught yourself one of the core concepts of AI. Without a single equation."

💬 "In one sentence — when should you exploit, and when should you explore? Type your answer."

*[Read a few responses. Validate.]*

---

## PHASE 7 — FAILURE ANALYSIS

## SLIDE 17 — Failure Analysis

"Most workshops only show you when AI succeeds. I want to show you when it **fails** — and why."

*[Walk through the path chain, one step at a time.]*

"The bot started at Snake. Target: Internet. Similarity score: 0.21. Low — expected, they're far apart."

"Clicked Reptile. Score: 0.24. Went up. Looks like progress."

"Clicked Animal. Score: 0.28. Still climbing."

"Clicked Life. Score: 0.25. Went down slightly. But the diversity penalty wasn't high enough to redirect."

"Clicked Existence. Score: 0.22."

"Clicked Philosophy. Score: 0.19."

"❌. Every link from Philosophy has even lower scores. The bot is stuck in abstract philosophy — as far from 'Internet' as it can get in meaning space."

*[Pause. Let the failure land.]*

💬 "Why did it fail? Every step looked reasonable. The score was always locally decent. What went wrong? Type your diagnosis."

*[Read responses. Guide toward three root causes:]*

"**Root cause 1:** The bot was climbing a gentle hill in the **wrong direction**. Each step was slightly better than the last, but the entire direction was wrong."

"**Root cause 2:** The similarity between 'Animal' and 'Internet' is non-zero — it looked like progress even when it wasn't."

"**Root cause 3:** No look-ahead. If the bot could see two steps ahead, it would know that Life→Existence→Philosophy is a dead zone."

"Students become AI researchers when they look at a failure and ask 'why' instead of just 'it broke.' You just did that."

"The fix: better diversity penalty — or look-ahead search. Which brings us to the next section."

---

## PHASE 8 — SEARCH ALGORITHMS

## SLIDE 18 — Search Algorithms

"Let's talk about how the bot searches."

"Right now, the bot does this:"

```
Current article → score all links → pick best → move → repeat
```

"It only looks **one step ahead**. That's Greedy Search. And as we just saw, it can fail."

💬 "Quick vote: should AI look one step ahead, or many? Type 1 or M."

*[Read responses.]*

"Great intuition. The answer is: many, if you can afford it. Here's how three search strategies compare."

*[Point to the three panels on screen.]*

"**Greedy Search.** Left panel. Look one step ahead. Pick the best. Fast. Sometimes gets trapped. That's our current bot."

"**Beam Search.** Center panel. Instead of keeping just one best candidate at each step, keep the top 3 simultaneously. Explore all three paths. Drop the worst. Keep the best 3 for the next step. Slower — but far less likely to get trapped."

"**A\\*** — right panel. Instead of scoring just the next step, estimate the **total path cost** to the destination. Factor in both 'how good is this step?' and 'how far am I from the goal overall?' Finds optimal paths. Very powerful."

"Notice the A* panel highlights B(3) instead of just A(5). It chose based on total estimated cost, not just the local score."

"All three are used in real AI systems — video game pathfinding, Google Maps, protein folding."

💬 "If Beam Search is better, why not always use it? What's the tradeoff? Think for 10 seconds, then type."

*[Students figure out: slower, more memory, more compute.]*

"Exactly. Every smarter search algorithm costs more to run. That's the fundamental engineering tension in AI: **accuracy vs efficiency**. There's no free lunch."

---

## PHASE 9 — ATTENTION: THE "IT" EXERCISE

## SLIDE 19 — Attention: The "it" Exercise

*[Read the first sentence out loud slowly.]*

"'The animal didn't fit in the suitcase because **it** was too big.'"

💬 "What is 'it' referring to? Type A for animal, S for suitcase."

*[Almost everyone says A — the animal was too big.]*

"Almost everyone says animal. Why? You used context. The sentence is about fitting an animal INTO a suitcase — if something is too big, it's probably the thing being put in."

*[Read the second sentence.]*

"'The suitcase didn't fit in the car because **it** was too big.'"

💬 "What is 'it' now? Same question."

*[Almost everyone says S — the suitcase.]*

"Now it's the suitcase. Same sentence structure. Different answer. Because the context flipped."

"As a human, you processed the entire sentence simultaneously. You understood the relationship between animal, suitcase, and car all at once."

"A traditional AI reading left to right, one word at a time, would struggle with this. It needs a mechanism to look at ALL words simultaneously and figure out which words are most relevant for understanding each other."

"That mechanism is called **Attention**."

"Attention lets the AI ask: to understand what 'it' means here, which other words in this sentence should I focus on? For sentence one — focus on 'animal' and 'suitcase.' For sentence two — focus on 'suitcase' and 'car.'"

"Transformers — the technology behind the embedding model we're using today, and behind ChatGPT — are built entirely on Attention. The paper that introduced them is literally called 'Attention Is All You Need.'"

"No equations. No diagrams. Just two sentences and a pronoun. That's the intuition for modern AI."

💬 "Type one thing that AI needs Attention for, other than WikiRace."

*[Read responses. Validate creative answers.]*

---

## SLIDE 20 — Be Right Back (Break 2)

*[Show the second BRB slide.]*

"10 minutes. When you come back, we're switching from watching to doing."

"Two tasks:"
"One: make sure Codespace is open. If not, open it now — link is pinned."
"Two: check these links in chat — you can literally fly through the space our bot is navigating in 3D."

*[Drop: https://galaxy.wikiloop.org/ and https://briansunter.github.io/wikipedia-3d-embeddings/]*

"Back in 10."

---

## SLIDE 21 — IT'S CODING TIME

*[Come back LOUD. Full energy.]*

"WE ARE BACK. IT. IS. CODING. TIME."

*[Let the slide land for 3 seconds.]*

"Drop a 🚀 in chat if your Codespace is open."

💬 *[Wait for rockets. Read names.]*

"For anyone still loading — it's pinned in chat. Takes 2 minutes. The rest of us will get oriented while you wait."

*[Switch to Codespace screen share.]*

"Here's what you're looking at:"

"Left panel: file explorer. File we care about: `embedding_bot.py`."
"Middle: code editor."
"Bottom: terminal. This is where we run things."

"Open `embedding_bot.py`. Find this line — it's around line 28:"

```python
model = SentenceTransformer('all-MiniLM-L6-v2')
```

"That's the AI brain. Same type of model used in production systems — just smaller and faster. Pre-downloaded when your Codespace set up."

"Now scroll to find:"

```python
score += overlap * 0.3
```

"And a bit further:"

```python
score -= overused_words[word] * 0.15
```

"Two lines. Two numbers. That's today's lab. And we're not going to call it coding."

---

## PHASE 12 — PARAMETER TUNING AS PERSONALITY TRAINING

"We're going to call it **training behavior**."

"Because that's what you're doing. You're deciding what **personality** this bot has."

"A bot with `overlap * 2.0` is obsessed with keyword matching. It charges toward any link that shares a word with the target."

"A bot with `overlap * 0.0` ignores keyword overlap entirely. It relies purely on the AI model's embeddings."

"These aren't just numbers. They're **personality dials**."

"Let's vote on what to try first."

💬 "For the overlap bonus — vote: 0.0, 0.3, 1.0, or 2.0. Type your vote."

*[Tally results. Run the winning value.]*

```bash
python embedding_bot.py
```

*[Narrate the run step by step.]*

"Score at step 1: [X]. With your overlap setting of [value], the keyword component of that score was [overlap × value]. With the default 0.3, it would have been [overlap × 0.3]. Different decision."

"Your vote changed the bot's behavior."

💬 "Did it work better or worse than you expected? Type B for better, W for worse, S for same."

*[Discuss. Then repeat for the diversity penalty.]*

💬 "Now for the diversity penalty — vote: 0.0, 0.15, 0.4, or 0.8?"

*[Run the winner.]*

---

## PHASE 13 — BOT TOURNAMENT

"Tournament time. Format:"

"Everyone has their own Codespace. You've been experimenting. Commit to a final configuration."

"Race route: **Snake → Internet**. Same start, same target. Fewest clicks wins."

"Set your final values. Post in chat:"
"`My config: overlap=[value], diversity=[value]`"

*[Give 3 minutes to finalize.]*

"Run it and post your result: number of clicks, or 'failed' if it didn't make it."

*[Run on presenter screen simultaneously. Track results.]*

"Hall of fame — top three configs get recognized."

---

### Chaos Bot Finale

"One final run. For comedy. I'm removing ALL the intelligence."

*[Comment out scoring, replace with:]*

```python
best_link = random.choice(unvisited_links)
print(f"➜ Chaos pick: '{best_link}' (no reason whatsoever)")
```

"Pure random. No embeddings. No similarity. No heuristics. Just vibes."

*[Run it.]*

"'[Random article].' Why? None. '[Another random article].' Why? Also none. This bot is living its best life with absolutely no direction."

"The contrast tells you everything. The intelligence we added — embeddings, similarity scoring, heuristics — is the difference between this and a bot that actually navigates. Every feature we added has a reason."

---

## SLIDE 22 — Thank You

*[Switch to Thank You slide. Let it breathe 3 seconds.]*

"That's it."

"Today you played a game. You broke an AI. You fixed it. You taught it a personality. You diagnosed its failures. And you raced it."

"That's not watching AI. That's working with it."

"Links to everything are in chat and on screen. Go build something."

---

## SLIDE 23 — Wikirace.ai Logo Outro

*[Leave the logo slide on screen as people leave. No narration needed. Let the room close naturally.]*

---

---

# SECTION 4 — DEMO FLOW DESIGN

## Complete Mode-Switching Map

```
SLIDE 1  (Loading…)          → casual, music, chat
SLIDE 2  (Title)             → slides, 5 sec silence
SLIDES 3–6 (Human Game)      → slides, highly interactive
SLIDE 7  (Debrief)           → slides + discussion
SLIDE 8  (Semantic Map)      → slides + cluster game
SLIDE 9  (Embeddings)        → slides + verbal exercise
SLIDE 10 (BRB Break 1)       → break, drop links
SLIDES 11–16 (Bot Psych)     → slides, vote before each bot
SLIDE 17 (Failure Analysis)  → slides, diagnosis discussion
SLIDE 18 (Search Algorithms) → slides, vote
SLIDE 19 (Attention)         → slides, cognitive surprise
SLIDE 20 (BRB Break 2)       → break, drop links
SLIDE 21 (Coding Time)       → SWITCH to Codespace immediately
Bot Demo                     → Codespace terminal
Experiments                  → Codespace (students + presenter)
Tournament                   → Codespace terminal
SLIDE 22 (Thank You)         → back to slides
SLIDE 23 (Logo Outro)        → holds on screen
```

## Codespace Onboarding Message (pin in chat at Break 1)

```
🔧 CODESPACE SETUP — do this now:
1. GitHub repo → link pinned above
2. Click green "Code" button
3. Click "Codespaces" tab
4. Click "Create codespace on main"
5. Wait ~2 min (auto-installs everything)
6. Open embedding_bot.py from the left panel
👍 Thumb up when you're in!
```

**Say while people set up:** "The reason it's instant is that the repo has a `.devcontainer` config — a pre-built environment. Python 3.12, all libraries, and the AI model are already installed. Containerized dev environments like this are standard at Google, Microsoft, Meta. You're using production-grade tooling."

## Bot Run Commands

```bash
# Standard run (random pair)
python embedding_bot.py

# Forced pair for tournament (edit inside play_game()):
# res = send_cmd(proc, {"cmd": "new_game", "start": "Snake", "target": "Internet"})

# Semantic map
python visualize.py

# Raw model demo
python demo.py
```

## Chaos Bot Code

```python
# Replace the scoring for loop with:
best_link = random.choice(unvisited_links)
print(f"➜ Chaos pick: '{best_link}' (no reason)")
```

## Recommended Race Pairs by Difficulty

| Level | Start | Target | Notes |
|-------|-------|--------|-------|
| Tutorial | Snake | Internet | Used in human game — satisfying callback |
| Easy | Python | Computer | Clean semantic path |
| Medium | Cricket | Black Hole | Cross-domain, requires bridges |
| Hard | Banana | Quantum Mechanics | Very disconnected |
| Chaos | Spaghetti | NASA | Maximum difficulty |

## Parameter Tuning Reference

| Parameter | Code | Default | Effect of increasing |
|-----------|------|---------|---------------------|
| Overlap bonus | `overlap * 0.3` | 0.3 | Bot chases keyword matches more aggressively |
| Diversity penalty | `overused_words[word] * 0.15` | 0.15 | Bot escapes clusters faster |
| Escape threshold | `best_score <= 0.05` | 0.05 | Bot gives up and goes random earlier |
| History window | `path_history[-4:]` | 4 steps | Penalty looks further back |

---

---

# SECTION 5 — BEGINNER CONFUSION GUIDE

## The 12 Most Common Confusion Points

---

### CONFUSION 1 — "What are all these numbers in the vector?"
**When:** Slide 9 / Embeddings
**Recovery:** "Ignore the specific values. Think of them as GPS coordinates. You don't need to know what 40.71° means to know it points to New York. Same here — the numbers point to a location in meaning space. Close numbers = close location = similar meaning."

---

### CONFUSION 2 — "Is this the same as ChatGPT?"
**When:** Any point after mentioning the model
**Recovery:** "Similar technology — both use transformers. But different tasks. ChatGPT generates text: predicts the next word. Our model measures text: calculates how similar two pieces of text are. ChatGPT is a writer. Our model is a librarian who knows where everything is."

---

### CONFUSION 3 — "What is exploration vs exploitation really?"
**When:** After Slide 16
**Recovery:** "Exploitation: do what you know works. Eat at the restaurant you love. Choose the highest-scoring link. Exploration: try something new. Take a lower-scoring path to see if something better is on the other side. Every AI that makes decisions over time has to balance these. So does every human."

---

### CONFUSION 4 — "Why does the looping bot loop? Doesn't it know it visited that page?"
**When:** After Slide 15
**Two causes:**
1. No visited set: "If the code doesn't track visited articles, it can literally click the same article twice."
2. Soft loop: "With a visited set, it avoids exact repeats — but can still visit different articles within the same cluster repeatedly because each one is the 'best available' given the others are visited. The diversity penalty breaks this."

---

### CONFUSION 5 — "What's the difference between Greedy Search and just... being smart?"
**When:** After Slide 18
**Recovery:** "Greedy IS smart — locally. It makes the best possible decision at every single step. The problem is local best ≠ global best. A chess player who only thinks one move ahead will lose to someone who thinks five, even if every individual move was 'locally optimal.'"

---

### CONFUSION 6 — "How does the bot know what 'Internet' means without being told?"
**When:** After explaining the model
**Recovery:** "The model read billions of sentences. It learned what 'Internet' means by seeing how the word is used — what it appears near, what topics surround it. No definition needed. Just patterns. This is called self-supervised learning."

---

### CONFUSION 7 — "What does Attention actually compute?"
**When:** After Slide 19
**Recovery (keep intuitive):** "For every word in a sentence, Attention calculates how much that word should pay attention to every other word. In our 'it' example — the attention score between 'it' and 'animal' ends up high, while 'it' and 'because' ends up low. The model learns these scores during training by reading massive amounts of text."

---

### CONFUSION 8 — "I changed the number and the bot got worse — did I break it?"
**When:** Parameter tuning
**Recovery:** "No — you discovered something! Write down what you changed and what happened. That's data. Try reverting to 0.3 and confirm it goes back to baseline. Then try 0.1. Science is observing what happens when you change one variable. You're doing science."

---

### CONFUSION 9 — "Can the bot beat a human at WikiRace?"
**Recovery:** "Sometimes yes, sometimes no. The bot is consistent — never panics, never gets distracted. Humans can be creative in ways the bot can't — like noticing 'Python' connects to both snakes and programming. For very disconnected route pairs, the bot often wins. For routes requiring lateral thinking, skilled humans often win."

---

### CONFUSION 10 — "Why 384 dimensions?"
**Recovery:** "384 is a design choice. More dimensions = more nuance captured = larger model = slower. 384 was this model's sweet spot for accuracy vs efficiency. GPT embeddings use 768. GPT-4 likely uses thousands. More dimensions → finer distinctions between meanings."

---

### CONFUSION 11 — "My Codespace won't open"
**Recovery steps in order:**
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Try in Chrome specifically
3. Check GitHub login
4. Delete failed Codespace, create a new one
5. Last resort: "Watch my screen — try locally after the workshop using the README instructions"

---

### CONFUSION 12 — "What's a heuristic?"
**Recovery:** "A shortcut rule. Not perfect, but good enough and fast. The overlap bonus is a heuristic — 'if the link title shares a word with the target, it's probably relevant.' Not always true, but true often enough to be useful. Almost all practical AI uses heuristics on top of the core model."

---

---

# SECTION 6 — LIVE FAILURE RECOVERY GUIDE

## The Core Principle
Every failure is content. Name it, explain it, learn from it, move on. Never dwell more than 60 seconds. Students should feel like seeing a crash was a bonus, not a problem.

---

## Bot Crashes

```
ModuleNotFoundError: No module named 'sentence_transformers'
```
→ "Library not installed — shouldn't happen in Codespace. Let me run `pip install sentence-transformers`. While that installs: what does ModuleNotFoundError mean? Python can't find code it needs — like trying to use an app that isn't installed yet."

```
requests.exceptions.ConnectionError
```
→ "Wikipedia is rate-limiting us — too many queries at once. Real production systems handle this with retry logic and caching. Our bot actually does cache — second visits to the same article are instant. Let me switch to a different article pair."

```
json.JSONDecodeError
```
→ "The bot's communication protocol broke. It talks to the game engine via JSON — structured text messages. Something corrupted the message. I'll restart the process."

```
KeyError / IndexError
```
→ "The bot hit a dead-end article with no valid links. Not all Wikipedia articles are richly connected. The bot needs a better escape hatch. Want to see how I'd add one live?"

**General reset:**
```bash
Ctrl+C                        # Kill process
git checkout embedding_bot.py  # Reset to original
python embedding_bot.py        # Restart
```

---

## Codespace Issues

**Won't load:** Hard refresh → try Chrome → delete and recreate → watch presenter's screen.
**"Port not found" error:** Normal — the bot runs in terminal, not a browser. Ignore.
**File changes not saving:** Check for the dot indicator on the filename tab. Ctrl+S.
**Wrong file open:** Make sure `embedding_bot.py` is open, not `app.py` or `bot_terminal.py`.

---

## visualize.py Won't Display

**Why:** Codespace has no display server.

**Fix:**
```bash
python visualize.py
# ai_brain_map.png saved in file explorer — click to open inline
```

**Backup:** Pre-generate `ai_brain_map.png` before the workshop and keep it available as a standalone image.

---

## Wikipedia API Slow

"We're hitting rate limits — all of us querying Wikipedia at the same time. Real systems solve this with caching and exponential backoff."

Fill time with: "While it loads — what's something you've used today that makes thousands of API calls per second? Spotify? Google Maps? TikTok?"

---

## Bot Wins Too Fast

"Too easy. Let's try something harder."

Hard pairs: Banana → Quantum Mechanics / Spaghetti → NASA / Yoga → Cold War

---

## Bot Loops Forever

"Classic local optimum trap. Let me increase the diversity penalty live."

```python
# Change: overused_words[word] * 0.15
# To:     overused_words[word] * 0.4
```

"Watch — with a stronger penalty, it should escape the cluster."

*[If it still loops: escalate to 0.8.]*

---

## You Break the Code While Live-Coding

"I broke it. Let me think out loud."

*[Narrate debugging.]*

"SyntaxError — typo. Line [X]… there it is."

*[Fix. Move on.]*

"Lesson: always make one change at a time and test before the next change. I violated that rule. Now you've seen a real debugging session — bonus content."

**Nuclear option:** `git checkout embedding_bot.py` — resets to original.

---

## BRB Slide Issue (Slide 10 or 20 not showing)

If the BRB slide doesn't show during break, just say: "We're taking a short break — 8 minutes. Links are in chat." No visual is strictly needed — the BRB slide is a nice-to-have that signals the pause, not a functional requirement.

---

---

# SECTION 7 — ENERGY AND ENGAGEMENT GUIDE

## The Attention Curve

```
HIGH  │████                        ██████            ████████
      │    █████    ████      ████       ████    ████        ████
LOW   │         ████    ██████               ████
      └───────────────────────────────────────────────────────▶
        P1  P2  P3  P4  P5  BR1 P6  P7  P8  P9  BR2 P11 P12 P13
       Hook     AI  Emb       Psych  Fail  Search  Attn  Lab  Race
```

Natural energy peaks: Human Game, Semantic Map, Bot Psychology (esp. Looping + reveal), Chaos Bot.
Natural valleys: AI explanation (P4–P5), Search Algorithms (P8).
Your job: don't let the valleys go too deep.

---

## Interaction Rhythm (Maximum 5 Minutes Between Asks)

| Type | Effort | Use when |
|------|--------|----------|
| Emoji react | 0 seconds | Transitions, loading |
| Single letter vote (A/B/S/SH/G/E/R/L) | 1 second | Predictions and polls |
| One word | 3 seconds | Concept checks |
| One sentence | 10 seconds | Analysis questions |
| Run code and post result | 3 minutes | Experiments |

---

## The 7 Must-Hit "Wow" Moments

### WOW 1 — Bad Path Reveal (Slide 4)
**Setup:** "Let me show you what I did."
**Reveal:** Hyper-Carnivorous → Spider → Spider-web
**Delivery:** Laugh at yourself. The 😭 should feel real.
**Why:** Students realize their own navigation might be just as bizarre.

### WOW 2 — Semantic Map (Slide 8)
**Setup:** "Nobody labeled these clusters."
**Reveal:** 5 seconds of silence. Let it land.
**Why:** The clusters are immediately obvious and the AI found them alone.

### WOW 3 — Greedy Bot "Missed!" (Slide 12)
**Setup:** "Is this smart or shortsighted?"
**Reveal:** Point to the 99 node. "The best possible answer was right there. The bot never reached it."
**Why:** The visual makes local vs global optima immediately tangible.

### WOW 4 — Exploration vs Exploitation Reveal (Slide 16)
**Setup:** "Let me give you the name for what you just figured out."
**Reveal:** The term, after 20+ minutes of intuitively understanding it.
**Why:** Students feel smart — they understood the concept before hearing the term.

### WOW 5 — The "it" Exercise (Slide 19)
**Setup:** Read sentence 1. Ask the question.
**Reveal:** Sentence 2 flips the answer.
**Why:** Genuine cognitive surprise. Students feel the difficulty firsthand.

### WOW 6 — First Bot Win
**Setup:** "I have no idea if it'll win. This is live."
**Reveal:** "🏆 WON THE RACE!"
**Why:** Genuine unpredictability. Students watched it make decisions and it worked.

### WOW 7 — Chaos Bot
**Setup:** "What if we remove ALL the intelligence?"
**Reveal:** Random, directionless picks narrated dramatically.
**Why:** The contrast shows exactly what the AI brain contributes. Comedy + lesson.

---

## Handling Dead Air

| Situation | Action |
|-----------|--------|
| Model loading | Ask a discussion question immediately |
| Waiting for chat | "10 more seconds… I see [name] typing" |
| Debugging live | Narrate your thought process out loud |
| Students running experiments | "Type 🟢 in chat when you're done" |
| Awkward silence after a reveal | "What surprised you? Just one word." |

---

## The Two BRB Slides — Pacing Notes

**Break 1 (Slide 10)** comes after Embeddings and before Bot Psychology. Energy should be medium at this point — students have absorbed the core concept and are ready for the decision-making section. Use the break to prime them: "When we come back, we're going to talk about how the bot actually makes decisions — and it's way more interesting than you'd expect."

**Break 2 (Slide 20)** comes after Attention and before Coding. This is the mode-shift break. Students should feel intellectually satisfied — they've understood embeddings, bot personalities, search strategies, and transformers intuitively. Use this break to shift their mindset: "From here on, we're not watching. You are the bot's trainer."

---

## Recovering a Disengaged Audience

Signs: chat goes silent, no emoji reactions, nobody responding to direct questions.

**Recovery ladder:**

1. Direct name call: "Hey [name who reacted recently] — what's your take?"
2. Provocative statement: "Actually I think the Greedy Bot is better than the Explorer. Change my mind."
3. Surprise action: "I'm going to run the chaos bot right now for no reason."
4. Physical break: "Everyone stand and stretch for 10 seconds. I'm serious. Go."
5. Explicit check: "Scale 1–5 in chat — how much of this is making sense?"

---

## Energy Management by Phase

| Phase | Target | Risk | Fix |
|-------|--------|------|-----|
| Human Game (2–6) | Loud, game-show | Rushing past chat | Wait for responses |
| AI explanation (7–8) | Medium, building | Going too abstract | Add analogy immediately |
| Semantic Map (8) | Slow, exploratory | Moving on too fast | 5 sec silence, then cluster game |
| Bot Psychology (11–16) | Medium-high | Too lecture-y | Vote before each bot reveal |
| Exploration vs Exploitation (16) | Dramatic pause | Understating the reveal | 3 sec silence before speaking |
| Failure Analysis (17) | Focused, investigative | Students get lost | Guide: "what was missing?" |
| Search Algorithms (18) | Medium | Sounds like CS class | "No math. Just intuition." |
| Attention (19) | High surprise | Students don't read the sentence | Read it yourself, slowly |
| Coding Time (21) | Maximum energy | Anti-climax | COME BACK LOUD |
| Experiments (12) | Student-paced | Confusion, silence | Check in every 3 minutes |
| Tournament (13) | High, sports-commentary | Technical slowdowns | Narrate even while waiting |
| Wrap-Up (22–23) | Warm, personal | Over-summarizing | 3 sentences max, then music |

---

---

# APPENDIX A — QUICK REFERENCE CHEAT CARD

*Print this or keep open in a second window during the event.*

## All 23 Slides

| # | Title | Phase | Time |
|---|-------|-------|------|
| 1 | Loading… (MicroCraft) | Pre-show | T-15 |
| 2 | Wikirace.ai Title | Opening | 0:00 |
| 3 | Human Game — Question | Interactive | 0:05 |
| 4 | Human Game — Bad Path | Reveal | 0:10 |
| 5 | Human Game — Re-challenge | Interactive | 0:14 |
| 6 | Human Game — Good Path | Reveal | 0:17 |
| 7 | Humans Think Weirdly | Debrief | 0:22 |
| 8 | How AI Understands Meaning? | Visual | 0:28 |
| 9 | Embeddings | Technical | 0:40 |
| 10 | Be Right Back (Break 1) | Break | 0:50 |
| 11 | Bot Psychology: Meet the Bots | Overview | 0:58 |
| 12 | Greedy Bot | Deep Dive | 1:02 |
| 13 | Explorer Bot | Deep Dive | 1:07 |
| 14 | Random Bot | Deep Dive | 1:12 |
| 15 | Looping Bot | Deep Dive | 1:16 |
| 16 | Exploration vs Exploitation | Big Reveal | 1:20 |
| 17 | Failure Analysis | Analysis | 1:22 |
| 18 | Search Algorithms | Concept | 1:34 |
| 19 | Attention: The "it" Exercise | Surprise | 1:47 |
| 20 | Be Right Back (Break 2) | Break | 1:57 |
| 21 | IT'S CODING TIME | Transition | 2:07 |
| 22 | Thank You | Close | 3:02 |
| 23 | Wikirace.ai Logo Outro | Outro | 3:07 |

## Key Commands

```bash
python embedding_bot.py        # Run the bot
python visualize.py            # Generate semantic map
python demo.py                 # Raw model demo
git checkout embedding_bot.py  # Reset code to original
```

## Key Parameters

```python
overlap * 0.3                  # Overlap bonus (try 0.0 to 2.0)
overused_words[word] * 0.15    # Diversity penalty (try 0.0 to 0.8)
best_score <= 0.05             # Escape threshold
path_history[-4:]              # History window
```

## Chat Checkpoints (every 5 min max)

- Slide 3 — First path suggestion
- Slide 4 — React to bad path reveal
- Slide 5 — Second suggestion (Round 2)
- Slide 6 — React to good path reveal
- Slide 7 — What made friend's path smarter?
- Slide 8 — Cluster guessing game (3 rounds)
- Slide 9 — Python: snake or language?
- Embedding Surgery — which doesn't belong?
- Slide 11 — Bot overview: which will win?
- Slide 12 — Greedy: Smart or Shortsighted? (S/SH)
- Slide 13 — Explorer: Why worse = better?
- Slide 14 — Random: Can randomness help?
- Slide 15 — Looping: Why is it repeating?
- Slide 15 — Which bot are you? (G/E/R/L)
- Slide 16 — Exploration vs Exploitation reveal
- Slide 17 — Failure diagnosis
- Slide 18 — 1 step or many? Vote (1/M)
- Slide 18 — Why not always use Beam Search?
- Slide 19 — "it" sentence 1 (A/S)
- Slide 19 — "it" sentence 2 (A/S)
- Experiment 1 — overlap vote
- Experiment 2 — diversity vote
- Tournament — config post
- Tournament — result post

## Race Pairs by Difficulty

| Level | Start | Target |
|-------|-------|--------|
| Tutorial | Snake | Internet |
| Easy | Python | Computer |
| Medium | Cricket | Black Hole |
| Hard | Banana | Quantum Mechanics |
| Chaos | Spaghetti | NASA |

---

---

# APPENDIX B — ALL RESOURCES WITH DROP TIMING

## Interactive Tools

| Tool | URL | Drop when |
|------|-----|-----------|
| Vector Embedding Simulator | https://semicolony.dev/simulators/vector-embedding/ | Break 1 (Slide 10) |
| Word Embeddings Explorer | https://embeddings.reiniss.com/ | Break 1 |
| Wordviz Explorer | https://wordviz.berrry.app/ | Break 1 |
| Word Embeddings (Academic) | https://word-embeddings.wbkolleg.unibe.ch/ | Break 1 |
| Embedding Projector (Google) | https://projector.tensorflow.org/ | After Slide 8 |
| Wikipedia 3D Embeddings | https://briansunter.github.io/wikipedia-3d-embeddings/ | Break 2 (Slide 20) |
| Galaxy WikiLoop (3D wiki graph) | https://galaxy.wikiloop.org/ | Break 2 |
| Embedding Space Explorer | https://williankeller.github.io/embedding-space-explorer/ | End |
| Embeddings Viz (GitHub) | https://github.com/arindam-sharma/embeddings-viz | End |

## Play and Code

| Resource | URL | Drop when |
|----------|-----|-----------|
| Live Game | https://wikirace-web.vercel.app | Pre-show (Slide 1) + End |
| Wiki Race (alternative) | https://wiki.halilb.dev/ | Pre-show |

## Learning Resources

| Resource | URL | Drop when |
|----------|-----|-----------|
| AI Wiki: Embeddings | https://aiwiki.ai/wiki/embeddings | End |
| Attention Is All You Need | https://research.google/pubs/attention-is-all-you-need/ | After Slide 19 |
| N-grams in NLP | https://www.geeksforgeeks.org/nlp/n-gram-in-nlp/ | End |
| Google Cloud AI Whitepapers | https://cloud.google.com/whitepapers | End |

---

---

# APPENDIX C — REMAINING SLIDE IMPROVEMENT SUGGESTIONS

*These slides are confirmed in the deck but can be improved further. All suggestions match the existing aesthetic.*

---

## HIGH PRIORITY

### 1. Slides 4 and 6 — Path Reveals Must Be Click-by-Click
**Status:** Most critical animation fix.
**Fix:** In Canva, set each arrow + icon group on these slides to "On Click" animation with a 0.3s delay between elements.
**Why:** The Hyper-Carnivorous reveal is only funny if it unfolds slowly with narration. If it appears all at once, the joke dies.

### 2. Slide 5 — Add a Round 2 Signal
**Status:** Currently looks identical to Slide 3.
**Fix:** Change the question mark to gold (vs blue in Slide 3), or add a small "Round 2 →" badge top-right.
**Why:** Without a visual signal, students think the presenter went back a slide accidentally.

### 3. Slide 22 (Thank You) — Add Actionable Next Steps
**Status:** Beautiful but a dead end.
**Fix:** Add small text in the lower third:
```
🎮 Play:  wikirace-web.vercel.app
🔧 Code:  github.com/[your-repo]
📚 Learn: aiwiki.ai/wiki/embeddings
```
Plus a GitHub QR code bottom-right.
**Why:** The workshop ends here. Students need somewhere to go.

---

## MEDIUM PRIORITY

### 4. Slide 8 — Overlay Human Paths on Semantic Map
**Fix:** Draw two faint dotted arrow trails:
- Mine: Snake → Spider → Spider-web → Internet (a visible detour through the web cluster)
- Friend's: Snake → exits animal cluster → Internet (more direct)
**Why:** Students spent 15 minutes on those paths. Seeing them on the map is the direct "aha."

### 5. Slide 9 — Add a Third Contrasting Word
**Fix:** Add a word like Car or Guitar with a completely different vector: [0.05, -0.40, 0.82, 0.15].
**Why:** Two similar words (cat, dog) shows similarity. A contrasting word makes the numerical difference obvious.

### 6. Slide 16 — Add a Slider Visual
**Fix:** Below the double-headed arrow, add a horizontal slider:
```
[EXPLORATION] ●━━━━━━━━━━━━━━━━━━━ [EXPLOITATION]
```
**Why:** Makes the tradeoff feel like a real tunable dial — which it is when students adjust parameters in the lab.

### 7. Slide 17 — Add Similarity Scores to the Path Chain
**Fix:** Add small score labels next to each hop:
```
Snake (0.21) → Reptile (0.24) → Animal (0.28) → Life (0.25) → Existence (0.22) → Philosophy (0.19) → ❌
```
**Why:** Students can see scores went UP then gradually DOWN — which is why the failure was subtle and hard to catch.

### 8. Interactive Footer on Chat Slides
**Fix:** On Slides 3, 5, 7, 8, 9, 11–16, 17, 18, 19 — add a small consistent footer: `💬 Type in chat ↓`
**Why:** Online audiences respond better to consistent visual cues than repeated verbal reminders.

---

## STRUCTURAL SUGGESTION

### A Four-Word Roadmap Slide (Optional)
**Position:** Between Slide 2 (Title) and Slide 3 (Human Game). Shows for 10 seconds.
```
Play  →  Understand  →  Build  →  Race
```
Four words. No bullets. Just sets the arc. Then immediately into the human game.

---

*End of Wikirace.ai Workshop Playbook v4.0*
*Updated to match the confirmed 23-slide Canva deck.*
*Slides 1 (Loading…), 10 (BRB), 11–16 (Bot Psychology), 17 (Failure Analysis), 18 (Search Algorithms), 19 (Attention), 20 (BRB), 23 (Logo Outro) all confirmed and scripted.*
*Microsoft Innovation Club · MicroCraft: The Summer of Building*
