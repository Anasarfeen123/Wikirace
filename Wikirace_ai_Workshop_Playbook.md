# Wikirace.ai — Complete Workshop Playbook
### A 2–3 Hour Online Beginner-Friendly AI/ML Workshop
*by Anas Arfeen · Microsoft Innovation Club*

---

> **How to use this document:** Read Section 1 first for the big picture. Then use the slide-by-slide script (Section 3) as your live presenter guide. Keep Sections 5–7 open in a second window as a cheat sheet during the event.

---

# SECTION 1 — COMPLETE WORKSHOP STRUCTURE

## Big Picture Flow

```
PHASE 0  |  Pre-Workshop Setup          (15 min before start)
PHASE 1  |  Hook & Human WikiRace       (0:00 – 0:20)
PHASE 2  |  The Problem + AI 101        (0:20 – 0:45)
PHASE 3  |  Embeddings Visualized       (0:45 – 1:05)
──────── |  ⏸ BREAK                     (1:05 – 1:12)
PHASE 4  |  The Bot Arrives             (1:12 – 1:30)
PHASE 5  |  Hands-On Codespace Lab      (1:30 – 2:00)
PHASE 6  |  Bot Races + Tuning          (2:00 – 2:30)
PHASE 7  |  Wrap-Up + What's Next       (2:30 – 2:45)
```

---

## PHASE 0 — Pre-Workshop Setup (15 min before)

**Presenter actions:**
- Share the GitHub repo link in chat 10 minutes before start
- Pin a message: "Click the green **Code** button → **Codespaces** → **Create codespace on main**. Wait for it to load — takes ~2 min. If stuck, just watch for now!"
- Have `embedding_bot.py` open in your own Codespace, ready to run
- Have `visualize.py` pre-run — screenshot of `ai_brain_map.png` ready as backup
- Test your screen share — share the **browser tab** with the Codespace, not your whole screen
- Cue up the Wikirace.ai title slide

**Vibe check:** Play lofi/chill music. Put a "loading…" gif on screen. Make it feel like an arcade waiting room.

---

## PHASE 1 — Hook & Human WikiRace (0:00 – 0:20)

| Time | Activity | Mode |
|------|----------|------|
| 0:00 | Title slide + energy intro | Slide |
| 0:03 | "What is WikiRace?" — show the live site | Live demo |
| 0:06 | Human race: you vs. audience | Interactive |
| 0:13 | Debrief: how did YOU navigate? | Discussion |
| 0:17 | "What if an AI could do this?" | Slide |

**Pacing note:** Go fast here. This phase should feel like a game show, not a class.

**Chat interactions:** "Type your strategy in chat!" / "What article did you start from?"

---

## PHASE 2 — The Problem + AI 101 (0:20 – 0:45)

| Time | Activity | Mode |
|------|----------|------|
| 0:20 | The Core Problem slide | Slide |
| 0:24 | "Cats vs. Dogs" analogy | Slide + discussion |
| 0:28 | What is NLP? | Slide |
| 0:32 | Word embeddings — the GPS analogy | Slide |
| 0:38 | Traditional vs. Modern NLP | Slide |
| 0:43 | Transition: "Let's SEE the AI brain" | Slide |

**Pacing note:** Keep each concept to ~3 minutes max. If energy dips, throw a poll.

---

## PHASE 3 — Embeddings Visualized (0:45 – 1:05)

| Time | Activity | Mode |
|------|----------|------|
| 0:45 | Live visualize.py run OR screenshot | Demo/Slide |
| 0:49 | Walk through the semantic map | Interactive |
| 0:53 | "Guess the cluster!" game | Audience game |
| 0:58 | Cosine similarity explained visually | Slide |
| 1:02 | Real-world systems using this | Slide |

**Pacing note:** This is the "wow" phase. Milk it. Let students react. Don't rush.

---

## ⏸ BREAK (1:05 – 1:12)

- Tell students: "While you're on break — look at the file `embedding_bot.py` in your Codespace. Just read the comments. Don't run anything yet."
- Show a slide: "The AI bot is loading… 🤖"
- Keep the music going

---

## PHASE 4 — The Bot Arrives (1:12 – 1:30)

| Time | Activity | Mode |
|------|----------|------|
| 1:12 | Bot architecture overview | Slide |
| 1:15 | First bot run — LIVE | Demo |
| 1:18 | Watch it navigate — audience predicts | Interactive |
| 1:22 | Explain the scoring logic | Slide + code |
| 1:26 | "What if we break it?" — chaos mode | Demo |

**Pacing note:** The first bot run is THE moment of the workshop. Build anticipation before running it.

---

## PHASE 5 — Hands-On Codespace Lab (1:30 – 2:00)

| Time | Activity | Mode |
|------|----------|------|
| 1:30 | Codespace onboarding (together) | Live guided |
| 1:38 | Students run their first bot | Student lab |
| 1:45 | Tweak experiment #1: overlap bonus | Lab |
| 1:52 | Tweak experiment #2: diversity penalty | Lab |
| 1:58 | Share results in chat | Discussion |

**Pacing note:** Have a co-host or helper monitoring chat for students who are stuck. Never leave students silent for more than 3 minutes.

---

## PHASE 6 — Bot Races + Tuning (2:00 – 2:30)

| Time | Activity | Mode |
|------|----------|------|
| 2:00 | Bot race setup: same start/target | Demo |
| 2:03 | Race 1: Default bot vs. Greedy bot | RACE |
| 2:08 | Audience votes: who wins? | Poll |
| 2:10 | Race 2: Student-tuned configs | RACE |
| 2:16 | "Why did the bot fail?" analysis | Discussion |
| 2:22 | Chaos bot for laughs | Demo |
| 2:26 | Hall of fame: best student configs | Showcase |

**Pacing note:** This is the most energetic phase. Keep the pace fast, celebrate wins and failures equally.

---

## PHASE 7 — Wrap-Up (2:30 – 2:45)

| Time | Activity | Mode |
|------|----------|------|
| 2:30 | "What did we actually build?" | Slide |
| 2:33 | Concepts recap | Slide |
| 2:36 | What's next / how to go deeper | Slide |
| 2:40 | Q&A | Discussion |
| 2:44 | Closing + resources | Slide |

---

---

# SECTION 2 — COMPLETE PPT SLIDE OVERVIEW

## SLIDE 1 — Title Slide
**Objective:** First impression. Set the energy and vibe.

**Visuals:**
- The existing Wikirace.ai title slide works perfectly
- Animated Wikipedia globe at center
- Flowing article path animations around it (Chess→Game Theory, Cricket→Neural Networks, etc.)
- Circuit board background

**Text:** Minimal. Just the title + tagline "Navigate knowledge. Faster than humans."

**Do NOT include:** Your name in big text, long subtitles, bullet points, event logistics

**Animation:** The article path labels should animate in one by one, floating in from different directions

**Interaction:** Play music as people join. Say nothing for the first 10 seconds after going live — let the visual do the work.

---

## SLIDE 2 — The Human WikiRace Demo Setup
**Objective:** Hook the audience with an actual game before teaching anything.

**Visuals:**
- Large screenshot of the live Wikirace.ai site (wikirace.ai or local URL)
- Two bold article names: START ← → TARGET
- A countdown timer graphic (optional)

**Text:** Just the two article names and "Can YOU find the path?"

**Interaction:** Ask chat to type their first click. Run the race live on screen. This is not a "slide" — switch to browser.

---

## SLIDE 3 — Debrief: How Did You Navigate?
**Objective:** Surface the human intuition that the bot will later replicate.

**Visuals:**
- Split panel: HUMAN BRAIN icon vs STRATEGY list
- Simple question mark visual

**Text:** 3–4 word bullet fragments max:
- "Broad topics first?"
- "Spotted a keyword?"
- "Followed gut feeling?"

**Interaction:** "Type in chat: what was your strategy?"

---

## SLIDE 4 — The Core Problem
**Objective:** Set up why AI can't just "feel" meaning like humans do.

**Visuals:**
- Left panel: Cat + Dog cartoon images (cute, not stock)
- Right panel: Two numerical vector arrays (from the existing slide)
- The two vectors for "Dogs" and "Cats" shown on screen

**Text:** Single question at bottom: "How do we represent meaning mathematically?"

**Do NOT include:** Technical jargon, formulas, wall of text

**Interaction:** "Quick poll — on a scale 1-5, how related are 'cat' and 'dog'?"

---

## SLIDE 5 — Language Models & Embeddings (Overview)
**Objective:** Orient beginners to the 3 key concepts without overwhelming them.

**Visuals:**
- Three cards: LLM, NLP, Word Embeddings (existing slide layout is good)
- Keep the neural network diagram, the NLP Venn diagram, and the word embedding chart

**Text:** Each card has a 1-line description max

**Animation:** Cards slide in one at a time — let the audience absorb each before revealing the next

**Talking point emphasis:** "Don't memorize these. Just know they exist."

---

## SLIDE 6 — Traditional NLP vs Modern NLP
**Objective:** Show the evolution — why older methods failed, what changed.

**Visuals:**
- The existing slide layout (left = Traditional, right = Modern, vine divider in center)
- Red "LIMITATIONS" box on Traditional side
- Keep it exactly as designed — it's clean

**Text:** Existing text is good — just make sure Modern NLP items animate in AFTER limitations are shown

**Interaction:** "Has anyone heard of ChatGPT? Raise your hand in reactions. ChatGPT uses this — the 'Modern' side."

---

## SLIDE 7 — The GPS Analogy (New Slide — Key Concept)
**Objective:** Make embeddings click intuitively before showing any math.

**Visuals:**
- A 2D coordinate grid
- Words plotted as dots: "Dog", "Cat", "Car", "Truck", "Apple", "Banana"
- Lines connecting similar words
- GPS/map aesthetic

**Text:** Big headline: "Words have addresses in AI's mind"
Subtext: "Similar meaning = close coordinates"

**Do NOT include:** Vector math, dimensions count, technical terms

**Interaction:** "If 'Dog' and 'Cat' are neighbors on this map — where would 'Wolf' be? Type in chat!"

---

## SLIDE 8 — Semantic Map LIVE (Demo Slide)
**Objective:** Make the abstract GPS analogy concrete and visual.

**Visuals:**
- Full-screen display of `ai_brain_map.png` (from visualize.py)
- Color-coded clusters: animals together, vehicles together, fruits together
- Large, dark background, cyan dots

**Text:** None on slide. You narrate.

**Do NOT include:** Any text at all. Let the image breathe.

**Interaction:** "Guess the cluster game" — point to a cluster and ask "What do these have in common?"

**Live demo option:** Run `visualize.py` live in Codespace terminal. If it works → wow moment. If not → show screenshot.

---

## SLIDE 9 — Cosine Similarity (Intuition Only)
**Objective:** Explain how the AI scores "closeness" without trigonometry.

**Visuals:**
- Two arrows on a dark background pointing in similar directions = HIGH score
- Two arrows pointing away from each other = LOW score
- Score displayed as 0.0 to 1.0

**Text:** "Score: 0 = completely different. Score: 1 = identical."
Below: "The AI asks: are these two arrows pointing the same way?"

**Do NOT include:** Cosine formula, dot products, unit vectors

**Interaction:** "Quick game — I'll show two words, you guess the similarity score (0-10). Cat vs Dog? Car vs Guitar?"

---

## SLIDE 10 — You Use This Every Day (Real-World Systems)
**Objective:** Connect embeddings to things students already love.

**Visuals:**
- Icon grid: Spotify, YouTube, Netflix, Instagram Explore, Google Search, TikTok, ChatGPT
- Each icon has a 3-word caption

**Text:** Big headline: "This technology is everywhere"
Captions: "Spotify: finds your vibe" / "TikTok: predicts your scroll" / "ChatGPT: understands your question"

**Animation:** Icons pop in one at a time

**Interaction:** "Which of these have you used today? React in chat!"

---

## SLIDE 11 — Meet the Bot (Architecture Reveal)
**Objective:** Introduce the bot in a fun, dramatic way. Make it feel like a character.

**Visuals:**
- Dark slide, single glowing robot/circuit icon center
- Title: "Meet the WikiRace AI 🤖"
- 4 capabilities listed as glowing chips/tags (not bullets): EMBEDDINGS · SIMILARITY · HEURISTICS · STRATEGY

**Text:** Minimal. Let the visual land.

**Animation:** Bot "powers up" — components light up one by one

**Interaction:** "What do you think it'll do first? Navigate randomly? Or go straight for the target? Type your guess!"

---

## SLIDE 12 — Bot Decision Logic (Simplified)
**Objective:** Show the bot's brain without overwhelming with code.

**Visuals:**
- Simple flowchart: 
  Current Article → Get all links → Score each link → Pick highest score → Navigate → Repeat
- Each step has a 2-3 word label
- Highlight the "Score each link" step

**Text:** Flowchart labels only. No paragraphs.

**Do NOT include:** Actual code on slide, math, technical method names

**Interaction:** "What could go wrong with this strategy? Think about it for 10 seconds."

---

## SLIDE 13 — The Scoring Formula (Conceptual)
**Objective:** Show the three ingredients that make the bot smart (or dumb).

**Visuals:**
- Three labeled boxes connected by + signs:
  SIMILARITY SCORE + OVERLAP BONUS − DIVERSITY PENALTY = FINAL SCORE
- Each box has an icon (magnifying glass, puzzle pieces, warning sign)
- Color coded: green for bonuses, red for penalties

**Text:** Box labels and a 1-line description each. No math.

**Interaction:** "Which of these three do you think matters most? Vote: A, B, or C in chat."

---

## SLIDE 14 — CODESPACE ONBOARDING (Transition Slide)
**Objective:** Get everyone into the coding environment without chaos.

**Visuals:**
- Step-by-step screenshot guide: 3 panels showing GitHub → Code → Codespaces → terminal
- Large arrows between each step
- Reassuring subtitle: "If it loads, you're already set up. No installs needed."

**Text:** 3 numbered steps only. Big font.

**Interaction:** "Thumbs up emoji when your Codespace is open!"

---

## SLIDE 15 — Experiment Card: Overlap Bonus
**Objective:** Guide the first student experiment clearly.

**Visuals:**
- Code block (just 1 line highlighted): `if overlap > 0: score += overlap * 0.3`
- Slider visual showing 0.0 → 0.3 → 0.5 → 1.0
- "What happens when you increase this?"

**Text:** The code line + "Try changing 0.3 to 0.8. What do you expect?"

**Interaction:** "Before you run it — predict: will the bot get smarter or dumber? Type your bet!"

---

## SLIDE 16 — Experiment Card: Diversity Penalty
**Objective:** Guide the second experiment.

**Visuals:**
- Code block: `score -= overused_words[word] * 0.15`
- Two path diagrams: one with a loop (penalty = 0), one that escapes (penalty = high)
- "Anti-Rabbit Hole Protection" label

**Text:** Experiment instruction + prediction prompt

---

## SLIDE 17 — Bot Race Setup
**Objective:** Frame the race as exciting — not just a demo.

**Visuals:**
- Racing flag graphic
- Two bots on a split screen: BOT A vs BOT B
- Same START → TARGET shown for both

**Text:** "Same race. Different brains. Who wins?"

**Animation:** Countdown: 3… 2… 1… GO!

**Interaction:** Live poll: "Who do you think wins? A or B?"

---

## SLIDE 18 — What Did We Actually Build?
**Objective:** Help students realize how much they learned.

**Visuals:**
- Word map connecting: Wikipedia → Embeddings → Cosine Similarity → Heuristics → Bot → Strategy
- All concepts visually linked

**Text:** "You just built an AI that navigates knowledge using meaning."

---

## SLIDE 19 — Concepts Recap (Lightning Round)
**Objective:** Lock in the key terms before students leave.

**Visuals:**
- 5 cards animate in one by one: EMBEDDINGS · COSINE SIMILARITY · SEMANTIC SPACE · HEURISTICS · TRANSFORMERS
- Each has a 5-word definition

**Text:** 5-word definitions only

**Interaction:** "For each one — 1 word that describes it. Go."

---

## SLIDE 20 — What's Next / Go Deeper
**Objective:** Send students home with clear next steps that don't feel overwhelming.

**Visuals:**
- 3 paths illustrated:
  1. 🎮 Keep playing the game (link to deployed site)
  2. 🔧 Hack the bot further (GitHub link)
  3. 📚 Go deeper (resources card)

**Text:** 3 paths, each with 1 action sentence

---

## SLIDE 21 — Closing / Thank You
**Objective:** End on energy and community.

**Visuals:**
- Wikirace.ai title slide style — circuit board, animated paths
- QR code to GitHub repo
- Workshop hashtag / social handle

---

---

# SECTION 3 — COMPLETE SPEAKING SCRIPT

> 💡 **Format guide:** Normal text = what you say. *[Italics]* = stage direction. **Bold** = key words to emphasize.

---

## SLIDE 1 — Title Slide

*[Go live with music playing. Let the title animation run for 10 seconds. Then speak.]*

"Hey everyone — welcome. I'm going to give you exactly ten seconds to read what's on screen right now, because this is the only chance you'll get to just sit and absorb something before we start doing things."

*[Pause 5 seconds.]*

"Okay. So. My name is Anas, and today you're going to do something that most people think requires a computer science degree. You're going to build an AI. Not a chatbot. Not a filter. An AI that actually *navigates knowledge* — the same way you would — except it does it by doing math on meaning."

"Before I explain what that means, I want to show you something."

*[Transition to browser — WikiRace site.]*

---

## SLIDE 2 — Human WikiRace Demo

"Has anyone played WikiRace before? Type yes or no in chat."

*[Wait 5 seconds for responses.]*

"For those who haven't — here's the game. You start on one Wikipedia article. You click links inside that article to jump to other articles. The goal: reach a target article as fast as possible. That's it."

"Let me show you what I mean. I'm going to start at… **[pick something fun — 'Cricket']** and I need to reach **[pick a weird target — 'Black Hole']**."

*[Start the game live. Navigate 2-3 clicks. Keep narrating.]*

"Okay I'm going to click 'India' because India has everything… then 'Space exploration'… then — oh wait, there's 'Astrophysics'… okay one more — 'Black Hole!' Got it in 4 clicks."

"Now I want YOU to try. I'm going to put the start and target in the chat. You have 60 seconds. Use Wikipedia on your own tab. Your score is how many clicks it takes. Go!"

*[Drop the challenge in chat. Set a 60-second timer. While they play, keep narrating.]*

"While you're playing, notice something — notice HOW you're thinking. Are you picking links that look similar to the target? Are you jumping to broad topics first? Are you following a gut feeling? We're going to come back to this."

*[After 60 seconds.]*

"Okay, time! Type your click count in chat. How many?"

*[React to responses.]*

"Beautiful. Some of you got it in 4 clicks, some took 15. And that's okay, because you all used the same tool — human intuition. The question we're going to answer today is: can we give a computer that same intuition?"

---

## SLIDE 3 — Debrief: How Did You Navigate?

"Before we jump into AI stuff, I want to know — seriously — how did you navigate? What was going through your head?"

"Type in chat: what was your strategy? Did you go for broad topics first? Did you spot a keyword that matched? Did you just click randomly and hope for the best?"

*[Read a few responses aloud.]*

"Right — and notice something interesting. Almost everyone who did well used some version of the same strategy: **follow what feels related**. 'Black Hole' sounds like space, so go to space, then astronomy, then physics. You were doing semantic reasoning. And you didn't even know it."

"That's exactly what we're going to teach the AI to do."

---

## SLIDE 4 — The Core Problem

"Here's the thing though. Humans are born knowing that 'cat' and 'dog' are related. You've seen them, touched them, heard people talk about them together. Your brain has built a map of how concepts connect."

"A computer? Has none of that. None. To a computer, the word 'cat' and the word 'banana' look equally meaningless. They're both just sequences of letters."

*[Point to the slide.]*

"On the right, that's what 'Dog' looks like to an AI — a list of numbers. That's what 'Cat' looks like — another list of numbers. Just from looking at these, can YOU tell they're related?"

*[Pause.]*

"No. Neither can a basic computer. So the big question is: how do we encode meaning into numbers in a way that actually preserves relationships?"

"This is the problem that kept AI researchers stuck for decades. And then, around 2013-2018, some brilliant people figured it out. We're going to see how today."

---

## SLIDE 5 — Language Models & Embeddings Overview

"Three terms you're going to hear today. You don't need to memorize them, you just need to have heard them so when you see them elsewhere you go 'oh yeah, I know what that is.'"

"**NLP** — Natural Language Processing. Basically, teaching computers to understand human language. Everything from autocorrect to ChatGPT falls under this."

"**LLMs** — Large Language Models. This is ChatGPT, this is Gemini, this is Claude. Huge AI systems trained on massive amounts of text. They're what happens when you take NLP very, very far."

"**Word Embeddings** — This is the thing we're actually building with today. The idea of representing words and sentences as coordinates in space. We'll see exactly what this means in about 5 minutes."

"One thing to notice on this slide — on the left you have 1-of-N encoding. Dog gets [0, 0, 0, 1, 0]. Cat gets [0, 0, 1, 0, 0]. These are just arbitrary tags. The numbers say nothing about meaning."

"On the right — word embeddings. Dog and Cat are *close to each other* in space. Run and Jump are close to each other. Tree and Flower are close. The numbers now capture something real."

"That's the revolution."

---

## SLIDE 6 — Traditional NLP vs Modern NLP

"Let's put this in context. Before modern AI, people tried to make computers understand language using rules."

"Bag of words: just count how many times each word appears. Ignore the order, ignore the context."

"TF-IDF: count words but give bonus points to rare words. Still ignoring meaning."

"Rule-based systems: literally write out grammar rules by hand. 'If you see a noun followed by a verb, it means X.' You can imagine how well that scales."

"These approaches had a big problem." *[Point to the red LIMITATIONS box.]*

"'Cat' and 'feline' are synonyms, but to these systems they're completely different words. Zero overlap. 'I didn't love the movie' and 'I hated the movie' mean the same thing — but these systems would treat them as very different."

"Modern NLP fixed all of this. Embeddings capture meaning. Transformers understand context. The word 'bank' near 'river' gets treated differently from 'bank' near 'money'."

"ChatGPT is built on this. Google Search is built on this. Spotify recommendations are built on this."

*[Pause for effect.]*

"And today? We're building something on this too."

---

## SLIDE 7 — The GPS Analogy

"Okay, let me make embeddings completely concrete with one analogy. GPS."

"Every city on earth has coordinates. London is at 51°N, 0°W. New York is at 40°N, 74°W. Paris is 48°N, 2°E."

"Now — if I show you those coordinates, you can figure out which cities are close to each other. London and Paris are neighbors. New York and London are far apart."

"Word embeddings do the exact same thing for meaning. Every word gets coordinates — not 2 numbers like GPS, but 384 numbers. And in that 384-dimensional space, words that mean similar things end up close to each other."

"Dog might be at coordinates [0.2, -0.1, 0.8, …]. Cat might be at [0.3, -0.2, 0.7, …]. Slightly different, but nearby. Car might be at [-0.5, 0.9, -0.3, …] — completely different neighborhood."

"The amazing thing: nobody told the AI that dogs and cats are related. It figured this out by reading billions of sentences and noticing they appear in similar contexts."

"One more thing before we visualize this — quick chat question: if 'Dog' and 'Cat' are neighbors on this map, where do you think 'Wolf' would be? Type your answer!"

*[Read responses. Validate: yes, Wolf would be near Dog, Cat, and other animals.]*

---

## SLIDE 8 — Semantic Map LIVE

*[Switch to terminal or show the pre-generated image.]*

*[If running live:]*

"I'm going to run our little script right now. It's going to load a real AI model — the same type used in ChatGPT, just smaller — and use it to calculate coordinates for 12 words. Then it's going to plot those coordinates."

```bash
python visualize.py
```

"While it loads, any guesses? I've got: Dog, Cat, Wolf, Tiger, Car, Truck, Bicycle, Motorcycle, Apple, Banana, Orange, Strawberry. What clusters do you expect?"

*[Wait for the image to generate. Open `ai_brain_map.png`.]*

"Look at this. Without me telling it ANYTHING about the world — just by learning from text — the AI grouped animals together, vehicles together, fruits together."

"This is a 2D projection of a 384-dimensional space. It's like flattening a 3D globe onto a flat map — there's some distortion, but the clusters survive."

*[Point to clusters.]*

"Guess the cluster game: I'll point, you type what these have in common. Ready?"

*[Point to animal cluster.]*
*[Point to vehicle cluster.]*
*[Point to fruit cluster.]*

"Now — the bot uses this to navigate Wikipedia. When it's at an article about 'Cricket', it looks at all the linked articles, calculates their coordinates, and picks the one closest to 'Black Hole'. That's the whole strategy. Let's see how well it works."

---

## SLIDE 9 — Cosine Similarity

"One more concept before the bot demo, and I'll make it fast."

"How does the AI *measure* closeness? It uses something called cosine similarity. Sounds scary, but the intuition is dead simple."

*[Point to arrows on slide.]*

"Imagine these are two arrows. If they point in almost the same direction, similarity score is close to 1. If they point in completely different directions, score is close to 0. If they point exactly opposite ways, score is -1."

"That's it. The AI converts every piece of text into an arrow. Then it measures how similar those arrows are."

"Quick game — I'll say two things. You guess the similarity score from 0 to 10."

"Cat vs Dog — what's your guess?"
*[Take responses. The actual score is ~0.7 or so, so 7/10 is correct.]*

"Car vs Guitar?"
*[Lower — ~0.2–0.3, so 2/10.]*

"This is literally what the AI does — thousands of times per second, for every link on every Wikipedia page."

---

## SLIDE 10 — You Use This Every Day

"Before we jump into the bot — I want you to appreciate something."

"Every system on this slide uses embeddings."

"Spotify: your listening history gets embedded. New songs get embedded. It recommends songs that are close to your taste in embedding space."

"TikTok: videos get embedded. Your watch time tells it about your preferences. It serves you the closest match."

"Google: your search query gets embedded. Web pages get embedded. It returns the most similar pages."

"ChatGPT: every message, every word gets embedded. That's how it knows what you mean, even when you say it weirdly."

"You've been using AI powered by embeddings literally every day. We're just lifting the hood today."

*[Pause.]*

"Okay. Break time. 7 minutes. When you come back, the bot is going to be racing."

---

## ⏸ BREAK SLIDE

"Before you go — open your Codespace. Look at the file called `embedding_bot.py`. Just *read the comments*. Don't run anything. Look for the line that says `score += overlap * 0.3` and the line that says `score -= overused_words[word] * 0.15`. We'll be changing those numbers in a bit."

"Back in 7 minutes!"

---

## SLIDE 11 — Meet the Bot

*[Come back with energy.]*

"Okay, welcome back. It's time to meet the star of today's workshop."

*[Pause dramatically.]*

"This is a Python bot. It has no hardcoded knowledge about Wikipedia. It doesn't know what a Black Hole is. It doesn't know what Cricket is. It has never seen these articles."

"But it can read. And it has an AI brain — the same `all-MiniLM-L6-v2` transformer model that companies use in real production systems."

"It reads the current Wikipedia article, gets all the links, asks its AI brain 'which of these is closest to my destination?', and clicks the best one."

"Four capabilities:" 

*[Reveal each one:]*

"Embeddings — it can represent any text as coordinates.
Similarity — it can score how close two texts are.
Heuristics — it has bonus rules to be smarter.
Strategy — it can avoid loops, dead ends, and rabbit holes."

"Let's race."

---

## SLIDE 12 — Bot Decision Logic

*[Brief slide before the demo.]*

"Just so you know what's happening when we run it. The bot loop is simple:"

"Get current article. Get all links. Score every link against the target. Pick the highest score. Navigate. Repeat."

"The magic is in step 3 — how it scores. Let's watch."

---

## DEMO — First Bot Run

*[Switch to terminal.]*

"I'm going to set a specific race — Banana to Black Hole. Why? Because it's a great test. Very different topics."

*[In terminal:]*

"Let's set the start and target in the code… actually let me just run it with whatever random pair it picks."

```bash
python embedding_bot.py
```

*[As it runs, narrate in real time:]*

"Okay, it's loading the model first. That model is 90 megabytes of AI knowledge compressed. Done."

"Race starts. It's at the starting article. Reading all links… calculating scores… 

*[Read output lines:]*

'Clicking: [article] with score 0.342' — okay, that makes sense.
'Clicking: [article] with score 0.418' — getting closer!

Come on, come on… ooh this is tense. Is it going to loop? Is it going to get confused?"

*[React genuinely to whatever happens.]*

**If it wins:** "YES! It won! Look at that path! It navigated from [X] to [Y] in [N] clicks! An AI that had never seen these articles just figured out a path using nothing but word embeddings!"

**If it fails or loops:** "Okay it hit a dead end! Look — it's going in circles. This is actually *interesting* — it means the embedding space has some local maxima where the bot gets trapped. This is a real problem in AI navigation. How do we fix this? The diversity penalty! Let's look at that."

---

## SLIDE 13 — The Scoring Formula

"Now I want to show you what's actually happening inside the bot. Here are the three ingredients."

*[Point to each:]*

"**Similarity Score** — the base embedding similarity. How close is this link to the target? This comes from the AI model."

"**Overlap Bonus** — a little cheat. If the link title literally contains words from the target, give it a bonus. If the target is 'Black Hole' and a link says 'Hole' something, bump it up. Simple string matching on top of AI."

"**Diversity Penalty** — the anti-rabbit-hole protection. If the bot has been visiting articles about the same topic for 4 steps in a row, penalize new links from that topic. Force it to explore."

"These three numbers add up to a final score. Highest score = next click."

"Here's the fun part: YOU get to change these numbers."

---

## SLIDE 14 — Codespace Onboarding

*[If students haven't opened Codespace yet:]*

"Okay, everyone open GitHub. The repo link is in chat. Click the green 'Code' button. Click 'Codespaces'. Click 'Create codespace on main'. Wait 2 minutes — it'll install everything automatically."

"When it opens, you'll see a terminal at the bottom and a file explorer on the left. That's it. No setup. No installs. We're already ready."

*[Give students 3 minutes to get in.]*

"Thumbs up emoji in chat when your Codespace is open. I'll wait."

*[Wait.]*

"Beautiful. Now open the file `embedding_bot.py` from the left panel."

---

## SLIDE 15 — Experiment #1: Overlap Bonus

"Find line that reads: `score += overlap * 0.3`"

"That `0.3` is the overlap bonus multiplier. Right now, every overlapping word adds 0.3 to the score."

"I want you to change it to `0.8`. Then run the bot. Prediction first — type in chat: will this make the bot better or worse? And why?"

*[Let students type predictions.]*

"Now run it! `python embedding_bot.py` in the terminal."

*[Give 3 minutes.]*

"What happened? Type your results! Did it win faster? Did it start doing weird things?"

*[Discussion. Common result: higher overlap bonus makes it too aggressive on surface-level word matching, sometimes misses the actual semantic path.]*

"Interesting. You just discovered that *more* isn't always better in AI. This is a real phenomenon called **overfitting a heuristic** — when you make a rule so strong it overrides the actual intelligence."

---

## SLIDE 16 — Experiment #2: Diversity Penalty

"Now find: `score -= overused_words[word] * 0.15`"

"Change `0.15` to `0.0` — effectively turn off the diversity penalty."

"Prediction: does the bot get better or worse without the penalty? Type A for better, B for worse."

*[Let students run and report.]*

"What did you see? Anyone notice the bot looping? The diversity penalty is what prevents the bot from getting stuck in an article cluster that's close-ish but can't reach the target. Without it, it can loop forever."

"This is called the **exploration-exploitation tradeoff** — a core concept in AI. You need some randomness to escape local traps, but too much randomness and you're not going anywhere."

"You didn't just tweak a number. You discovered one of the fundamental challenges in AI."

---

## SLIDE 17 — Bot Race Setup

"Alright. Race time."

"Here's the setup: both bots start at the same article, trying to reach the same target."

"Bot A: default settings (overlap = 0.3, penalty = 0.15)"
"Bot B: your most aggressive settings (whatever you tried)"

*[Poll:]*

"Who thinks the default bot wins? Type A. Who thinks your custom bot wins? Type B."

*[Run both in quick succession, or run simultaneously in split terminal.]*

"Let the race begin!"

*[Narrate like a sports commentator. Genuinely react to what happens.]*

"Bot A is ahead! But wait — Bot B just jumped to [article]? How did it— oh, overlap bonus is massive, it's gambling on keyword matches!"

*[If Bot B loses:]*
"And the tortoise wins! The careful, balanced default bot beat the aggressive one. Sometimes the boring strategy is the right strategy. In AI and in life."

*[If Bot B wins:]*
"YOUR BOT WON! Whatever you changed — it worked! Tell me in chat what settings you used!"

---

## DEMO — Chaos Bot

*[This is the comedy moment of the workshop.]*

"One more experiment. What happens if we make the bot completely random?"

"I'm going to comment out the entire scoring logic and replace it with `best_link = random.choice(unvisited_links)`. This is the Chaos Bot."

*[Run it.]*

"It has no strategy. No AI brain. Just vibes."

*[Narrate as it runs. It will probably take forever or fail.]*

"Look at this. 'Jumping to [random article].' Why? No reason. Just chaos. Now '[another random article].' Still no reason."

"The chaos bot is technically making progress sometimes — it won't revisit articles, so it has to keep exploring. But it has no direction. It might win eventually by accident. But it'll take forever."

"This is actually a perfect illustration of why embeddings matter. Without meaning, you're just clicking randomly. The AI brain is what makes the bot actually navigate instead of wander."

---

## SLIDE 18 — What Did We Actually Build?

"Let me take a step back. Look at what just happened in the last 2 hours."

"You ran an AI model. Not a pre-built chatbot. An AI model — `all-MiniLM-L6-v2` — that you called yourself."

"You changed how that AI makes decisions. You adjusted parameters. You ran experiments. You saw the results change."

"You discovered real AI concepts — heuristics, exploration-exploitation tradeoffs, local maxima — by *playing with them*, not by reading about them."

"That's research. That's engineering. That's what AI people do every day."

"And you did it in a Codespace, in a browser, with zero setup."

---

## SLIDE 19 — Concepts Recap

"Lightning round. I'm going to throw terms at you. If you recognize them, shout the analogy we used today."

"**Embeddings**?" → GPS coordinates for words

"**Cosine similarity**?" → How much two arrows point the same way

"**Semantic space**?" → The map where similar words live close together

"**Heuristics**?" → Bonus rules on top of the AI

"**Transformers**?" → The architecture behind the model we used

"You know these now. Not because you memorized them — because you *used* them."

---

## SLIDE 20 — What's Next

"If you want to go deeper, here are three paths."

"**Path 1 — Keep playing.** The game is live at [link]. Challenge your friends. Play human vs bot."

"**Path 2 — Hack the bot.** The full code is on GitHub. Can you make the bot smarter? Can you add a new heuristic? Can you make it faster?"

"**Path 3 — Go deeper.** The libraries we used — `sentence-transformers`, `sklearn`, `matplotlib` — have amazing documentation. The model we used (`all-MiniLM-L6-v2`) has a Hugging Face page with benchmarks and papers."

"If any of you build something cool with this, I want to see it. Seriously."

---

## SLIDE 21 — Closing

"That's a wrap. Thank you for being such a great audience — honestly, the energy in this chat made this workshop."

"The QR code goes to the GitHub repo. The link in chat is the live game."

"One last thing — if someone asks you 'what is an embedding', you can now actually answer that question. Most people with CS degrees can't explain it this clearly."

"You've got this. Go build something."

---

---

# SECTION 4 — DEMO FLOW DESIGN

## When to Switch Between Modes

```
SLIDES → BROWSER    : Human WikiRace demo (slide 2)
BROWSER → SLIDES    : After debrief (slide 3)
SLIDES → TERMINAL   : visualize.py demo (slide 8)
TERMINAL → SLIDES   : After semantic map discussion (slide 9)
SLIDES → TERMINAL   : First bot run (after slide 12)
TERMINAL → SLIDES   : Brief — show scoring formula (slide 13)
SLIDES → CODESPACE  : Student onboarding (slide 14)
CODESPACE → SLIDES  : Quick experiment debrief (slides 15-16)
SLIDES → TERMINAL   : Bot races (slide 17)
TERMINAL → SLIDES   : Wrap-up (slide 18)
```

## Codespace Onboarding Script

**Step 1 — The link message (pin in chat):**
```
GitHub repo: [LINK]
1. Click green "Code" button
2. Click "Codespaces" tab
3. Click "Create codespace on main"
4. Wait ~2 minutes (automatic setup!)
👍 Thumbs up when open!
```

**Step 2 — What to say while people set up:**
"While you're opening that, let me show you what you'll see. On the left — file explorer. In the middle — code editor. At the bottom — a terminal. The terminal is where we'll run stuff. Don't worry about the code yet — just open `embedding_bot.py` and look at the comments."

**Step 3 — Normalizing confusion:**
"If your Codespace is taking more than 3 minutes, try refreshing the page. If it still doesn't work, no worries — you can watch my screen and follow along. You can always clone it and try at home."

## Key Files to Reference

| File | When to show | What to highlight |
|------|-------------|-------------------|
| `embedding_bot.py` | Phase 4-6 | Lines ~35-75 (scoring logic) |
| `visualize.py` | Phase 3 | The whole file — it's only 30 lines |
| `demo.py` | Optional | For showing raw model usage |

## Bot Race Setup Commands

**Standard race (random pair):**
```bash
python embedding_bot.py
```

**Preset race (same pair for comparison):**
```python
# In embedding_bot.py, add to play_game():
res = send_cmd(proc, {"cmd": "new_game", "start": "Cricket", "target": "Black Hole"})
```

**Chaos bot modification:**
```python
# Comment out the scoring loop and replace with:
best_link = random.choice(unvisited_links)
print(f"➜ Chaos pick: '{best_link}'")
```

## Parameter Tuning Cheat Sheet

| Parameter | Default | Low effect | High effect |
|-----------|---------|-----------|-------------|
| Overlap bonus | 0.3 | Bot relies purely on AI | Bot keyword-matches aggressively |
| Diversity penalty | 0.15 | Bot can loop forever | Bot over-explores, misses good paths |
| Escape hatch threshold | 0.05 | Bot never gives up on low scores | Bot random-jumps too often |
| Recent articles lookback | 4 | Penalty applies to all history | Penalty only from very recent steps |

---

---

# SECTION 5 — BEGINNER CONFUSION GUIDE

## The 8 Most Common Confusion Points

### 1. "What is a vector / what are all these numbers?"
**Confusion:** Students see the embedding arrays and feel overwhelmed.

**Recovery script:** "Forget the specific numbers. Just think of them as coordinates on a map. Every word has a location. The numbers are the address. You don't need to understand what each number means — the AI figured that out automatically."

**Visual aid:** Point to the semantic map — "These dots ARE the vectors, just drawn in 2D."

---

### 2. "Why does it use 384 dimensions? Why not 2?"
**Confusion:** Students understand 2D maps but can't visualize 384D.

**Recovery script:** "Imagine you're describing a person. You could describe them in 2 dimensions — tall/short, heavy/light. But that loses so much information. What if you had 384 dimensions? Height, weight, hair color, personality traits, hobbies… each one adds nuance. Words are the same — 384 dimensions captures way more meaning than 2."

**Follow-up:** "We compressed it to 2D to *look* at it. But the AI uses the full 384 — which is why it's smarter than the picture."

---

### 3. "Is this the same as ChatGPT?"
**Confusion:** Students conflate embeddings with generative AI.

**Recovery script:** "Great question! ChatGPT generates text — it predicts the next word. Our model just calculates coordinates. Same underlying technology — transformers — but different task. ChatGPT is like a writer. Our model is like a librarian who knows where everything is."

---

### 4. "Why does the bot sometimes fail?"
**Confusion:** Students expect AI to always work perfectly.

**Recovery script:** "This is actually one of the most important things you can learn: AI fails. All the time. And it fails in *interesting ways*. The bot fails because the embedding space has local maxima — areas where everything nearby seems good, but you're actually stuck. This is the same reason that optimizing an AI recommendation algorithm sometimes makes it worse."

**Reframe:** "Every failure is data. What's it failing on? Why? That's the research question."

---

### 5. "What is the model actually trained on?"
**Confusion:** Students want to know where the AI knowledge comes from.

**Recovery script:** "The model — all-MiniLM-L6-v2 — was trained on over 1 billion sentence pairs. Web pages, Reddit discussions, academic papers, Wikipedia itself. It learned which sentences appear in similar contexts. That's it. No one labeled 'dog' and 'cat' as similar. It figured that out by seeing them used similarly."

---

### 6. "Can I break it?"
**Likely situation:** Students try weird parameter values (like 999.0) and get errors.

**Recovery script:** "Yes, you can break it! And that's good! When you break it, look at the error message. It's usually telling you what went wrong. Try to fix it. If you can't, revert to the default and try a smaller change."

**Prevention tip:** Tell students before experiments: "I'd recommend changes of 0.1 at a time, not 100."

---

### 7. "What's Codespaces? Is it safe to use?"
**Confusion:** Some students (or parents) may be wary of cloud coding environments.

**Recovery script:** "GitHub Codespaces is Microsoft's cloud coding environment — literally built by the company that makes Windows and Azure. It creates a temporary container in the cloud. It disappears when you close it. It doesn't access your personal files."

---

### 8. "I can't get my Codespace to open"
**Recovery:** 
1. Try a hard refresh (Ctrl+Shift+R)
2. Try in a different browser (Chrome tends to work best)
3. Check if they're signed into GitHub
4. As last resort: "Just watch my screen, and you can run it at home — the README has full instructions for local setup too."

---

---

# SECTION 6 — LIVE FAILURE RECOVERY GUIDE

## Rule #1: Never apologize excessively
One quick "oops, let me fix this" and keep moving. Long apologies kill momentum.

## Rule #2: Failures are content
Every crash, every loop, every wrong result is a teaching moment. Frame it that way immediately.

---

## Scenario: Bot crashes with an error

**What to do:**
1. Leave the error on screen for 5 seconds. Read it aloud.
2. "Okay, what does this error mean? Anyone want to guess?"
3. Most common errors:

```
ModuleNotFoundError: No module named 'sentence_transformers'
```
→ "The model isn't installed. This shouldn't happen in Codespace since it auto-installs. Let me try running `pip install sentence-transformers` real quick."

```
ConnectionError / TimeoutError
```
→ "Wikipedia is being rate-limited or slow. This is normal with public APIs. Let me switch to a different start article."

```
IndexError / KeyError
```
→ "The bot hit an article with no links — a dead end. This is actually interesting — it means the Wikipedia graph isn't fully connected everywhere. The bot needs an escape hatch here. Want to see how I'd add one?"

---

## Scenario: Codespace won't load for students

**What to say:**
"For those who can't get Codespace open — no worries at all. Follow along on my screen. All the important concepts are visible. After the workshop, the README has step-by-step local setup instructions, or you can try Codespace again on a different browser."

**Keep going.** Don't halt the workshop for setup issues.

---

## Scenario: visualize.py fails (matplotlib can't display)

**What to say:**
"Okay, the plot window isn't rendering in the browser environment — that's a Codespace limitation. But I have the output right here."

*[Show the pre-generated screenshot.]*

"This is what it would look like. Same result, different delivery."

**Backup:** Always have `ai_brain_map.png` pre-generated and ready as a slide.

---

## Scenario: Bot loops forever

**What to say:**
"Look at this — it's going in circles! Article A → Article B → Article C → Article A again. This is a classic AI failure mode called a **local optimum trap**. The bot thinks it's making good choices at each step, but it's stuck in a loop."

"This is exactly why the diversity penalty exists. Let's watch what happens when I increase it."

*[Live-adjust the penalty value and rerun.]*

"See — now it's escaping the loop. You just watched an AI parameter fix a real AI bug in real time."

---

## Scenario: Internet is slow — everything is sluggish

**What to say:**
"We're hitting a bit of network lag — Wikipedia API is getting some love from all of us at once. This is actually a real-world problem: rate limiting. Production AI systems deal with this constantly."

"While we wait — let me ask the room a question. [Insert any discussion question to fill time.] The demo will be back in about 30 seconds."

---

## Scenario: Bot wins immediately on the first try (anti-climax)

**What to say:**
"Wow, that was fast! Let's make it harder."

*[Immediately set a more challenging pair: 'Banana' → 'Quantum Mechanics' or 'Cricket' → 'Internet Protocol']*

"Let's see how it handles a bigger knowledge gap."

---

## Scenario: You accidentally break the bot while demoing

**What to say:**
"Okay, I broke it. This is very normal in live coding. Let me think…"

*[Keep narrating your debugging process out loud.]*

"I see the issue — I changed the wrong variable. Live coding lesson: always make one change at a time and test. I violated my own rule."

*[Fix it. Move on.]*

"Now you've seen both a working bot AND a debugging session. Bonus content."

---

---

# SECTION 7 — ENERGY & ENGAGEMENT GUIDE

## The Energy Curve

```
HIGH  │        ████    ██████       ████████
      │  ████        ██      █████          ████
LOW   │
      └──────────────────────────────────────────▶ Time
         P1    P2   P3   BREAK P4    P5    P6   P7
```

Energy naturally peaks at the human race, the semantic map reveal, and the bot races. Your job is to keep the valleys from going too low.

---

## Interaction Rhythm

**Rule:** Never go more than 5 minutes without asking for something from the audience.

**Tier 1 — Easy asks (0 effort):**
- "React with 👍 if you've used [platform]"
- "Type 1 for yes, 2 for no"
- "Give me an emoji for how you're feeling"

**Tier 2 — Quick text asks (5 seconds of effort):**
- "Type your guess in chat"
- "One word: describe what we just saw"
- "What surprised you?"

**Tier 3 — Active participation (30 seconds):**
- Prediction challenges
- Running code and reporting results
- Pair discussion: "Talk to the person next to you and come back with one question"

---

## Reading the Room Online

**Signs the audience is disengaging:**
- Chat goes silent
- No reactions to questions
- No emojis/polls being answered

**Recovery moves (in order of escalation):**
1. Direct chat question: "Hey [name who reacted earlier], what do you think?"
2. Surprise move: "I'm going to do something dumb right now — I'm going to delete this entire scoring function and see what happens"
3. Energy reset: "Okay everyone, stand up and stretch for literally 10 seconds. I'm serious. I'll wait."
4. Poll: Drop a Mentimeter/Slido poll or just a chat poll

---

## Pacing Rules

| Phase | Target pace | Warning signs | Adjustment |
|-------|-------------|---------------|------------|
| Phase 1 (Hook) | Fast, energetic | Audience too quiet | Ask a direct question |
| Phase 2 (AI 101) | Medium | Confusion in chat | Slow down, add analogy |
| Phase 3 (Visual) | Slow + exploratory | Moving too fast | Stay on semantic map longer |
| Phase 4 (Bot) | Build up → explode | Underwhelmed reaction | React bigger yourself |
| Phase 5 (Lab) | Student-led | Nobody finishing | Give them more time, reduce scope |
| Phase 6 (Race) | Fast, game-show | Too slow between races | Cut analysis short |
| Phase 7 (Wrap) | Measured | Running over time | Cut slides, keep energy high |

---

## The 5 Planned "Wow" Moments

These are the moments you want the audience to feel. Set them up explicitly.

### WOW #1 — The Semantic Map (Phase 3)
**Setup:** "Without anyone telling it anything, the AI…"
**Reveal:** Open `ai_brain_map.png`
**What to say after:** Nothing for 3 seconds. Let it land.

### WOW #2 — First Bot Win (Phase 4)
**Setup:** "I have no idea if it's going to win. This is live."
**Reveal:** Bot outputs "WON THE RACE!" 
**What to say after:** "That just worked. An AI that had never seen those articles figured out the path."

### WOW #3 — Student Changes Break It (Phase 5)
**Setup:** "What do you think will happen if you change this?"
**Reveal:** Student runs it and sees weird behavior
**What to say after:** "You just discovered a real AI engineering problem."

### WOW #4 — Bot Race Finish (Phase 6)
**Setup:** Announce the race like a sports commentator
**Reveal:** One bot wins dramatically
**What to say after:** Celebrate whoever won — bot or student config

### WOW #5 — Chaos Bot (Phase 6)
**Setup:** "What if we just make it completely random?"
**Reveal:** Chaos bot output is hilariously directionless
**What to say after:** "This is why AI needs meaning. Without embeddings, this is all you have."

---

## Handling Dead Air

Online workshops have more silence than in-person. Normalize it.

**Scripts for awkward pauses:**
- While running code: "Loading… and this is a good time to ask — has anyone here used an API before?"
- While waiting for chat: "I'll give you 10 more seconds on that. No wrong answers."
- While debugging: "I'm narrating my thought process out loud because this is actually what debugging looks like for everyone, including experienced engineers."

---

## Closing Energy

The last 5 minutes should feel like the end of a concert, not the end of a lecture.

- Don't summarize everything — just hit the 3 big feelings: "You ran AI. You broke it. You fixed it."
- Show the QR code to the repo
- Leave with one clear call to action: "Share what you built with me."
- End on the title slide with music playing again — bookend the experience.

---

---

# APPENDIX A — Quick Reference Card

*Print this or keep it open during the event.*

**Key files:**
- `embedding_bot.py` — the main bot (scoring logic: lines ~45-75)
- `visualize.py` — semantic map generator
- `demo.py` — raw model demo

**Key parameters to tweak:**
- Overlap bonus multiplier: `overlap * 0.3`
- Diversity penalty: `overused_words[word] * 0.15`
- Escape threshold: `best_score <= 0.05`
- Recent history window: `path_history[-4:]`

**Run commands:**
```bash
python embedding_bot.py          # Run the bot
python visualize.py              # Generate semantic map
```

**Interaction checkpoints (max 5 min apart):**
□ Slide 2 — Human race in chat
□ Slide 4 — Cat/Dog similarity poll
□ Slide 7 — Wolf placement game
□ Slide 8 — Cluster guessing game
□ Slide 9 — Similarity guessing game
□ Slide 10 — Platform reaction
□ Slide 11 — Bot prediction
□ Slide 13 — Which ingredient matters most?
□ Slide 15 — Experiment prediction
□ Slide 16 — Experiment prediction
□ Slide 17 — Race vote
□ Slide 19 — Lightning concept recap

**Backup plans:**
- Bot crashes → show pre-run terminal screenshot + narrate
- Codespace fails → direct students to watch, try local later
- visualize.py can't display → use pre-generated `ai_brain_map.png`
- Wikipedia slow → switch to pre-cached article pair

---

# APPENDIX B — Pre-Workshop Checklist

**48 hours before:**
- [ ] Test full run of `embedding_bot.py` in Codespace
- [ ] Run `visualize.py` and save `ai_brain_map.png` as backup
- [ ] Test the WikiRace site with a custom game
- [ ] Prepare 3 article pairs of varying difficulty
- [ ] Record a 10-second screen capture of the bot winning (emergency backup)

**Day of:**
- [ ] Share GitHub repo link in calendar/event chat 1 hour early
- [ ] Open your own Codespace (don't share screen until ready)
- [ ] Have `ai_brain_map.png` as a slide or window ready
- [ ] Have the "Chaos Bot" modified version ready to paste
- [ ] Test screen share — share browser tab only, not full screen
- [ ] Check audio — no echo, no background noise
- [ ] Prepare 3 interaction polls in Mentimeter or just in chat

**5 minutes before:**
- [ ] Title slide up, music playing
- [ ] Codespace open in another tab
- [ ] GitHub repo link in clipboard
- [ ] `embedding_bot.py` open in Codespace
- [ ] `ai_brain_map.png` image open in a tab
- [ ] Chat open to monitor

---

*End of Wikirace.ai Workshop Playbook*
*Version 1.0 — Built for Microsoft Innovation Club*
