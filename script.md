# Wikirace.ai — Complete Workshop Playbook

### A 2–3 Hour Beginner-Friendly AI/ML Workshop

*By Anas Arfeen | Microsoft Innovation Club*

---

> **How to use this playbook:** Read through it fully once before presenting.
> During the workshop, use the "SCRIPT" sections as your talking track —
> but don't read them word-for-word. They're a safety net. Your own energy is the superpower.

---

## MASTER TIMELINE AT A GLANCE

| Phase | Section | Duration |
|---|---|---|
| 0 | Setup & Pre-show | 10 min before |
| 1 | Hook & Cold Open | 10 min |
| 2 | The Core Problem | 15 min |
| 3 | Embeddings — How AI Thinks | 20 min |
| 4 | DEMO: The Bot Plays WikiRace | 20 min |
| 5 | How the Bot Works | 20 min |
| — | BREAK | 10 min |
| 6 | The Bot Zoo — Strategies | 15 min |
| 7 | LIVE EXPERIMENT: Tune the Bot | 30 min |
| 8 | Why This Matters | 10 min |
| 9 | Takeaways & Q&A | 10 min |
| **Total** | | **~2h 30min** |

---

## PHASE 0: PRE-SHOW SETUP (10 min before start)

**What to have ready:**

- Terminal open, `run_bot.sh --bot` ready but not started
- Browser tab: English Wikipedia, random article
- `embedding_bot.py` ready to run
- `visualize.py` ready to run
- Slide deck in presentation mode
- If possible: background music playing (lo-fi / synthwave — fits the vibe)

**Slide to show while people file in:**
A screensaver slide with the Wikirace.ai logo, the tagline "Navigate knowledge. Faster than humans.", and a few floating example routes (Chess → Game Theory, Cricket → Neural Networks, etc.) — slow animation, dark theme.

**Tip:** As people sit down, casually ask:
> "Hey quick show of hands — who here has used ChatGPT? Cool. Who has used Google? Also ChatGPT. We're going to understand HOW that actually works today."

---

## PHASE 1 — THE HOOK (Slides 1–3)

### Duration: ~10 minutes

---

### SLIDE 1: Title Slide

**Title:** Wikirace.ai — Navigate Knowledge. Faster Than Humans.

**Visuals:**

- Full-bleed dark background (matching the existing slide aesthetic)
- The Wikirace.ai logo centered
- Floating route examples around it (already in your deck)
- Subtle animated circuit lines / glowing dots

**Text on slide:** Almost none. Just the logo and tagline.
**What NOT to include:** Bullet points, long descriptions, agenda

---

#### SCRIPT — SLIDE 1

*(Walk in confidently. Don't start talking immediately. Let the logo sit for 3 seconds.)*

"Okay. So.

Before I explain anything, I want to play a game with you all.

*(Bring up a Wikipedia article — doesn't matter which one. Something random like 'Accordion'.)*

Does anyone know what WikiRace is? *(Pause, take hands.)*

For those who don't — WikiRace is a game where you start on one Wikipedia article and you have to reach a completely different, totally unrelated article. But here's the rule: you can ONLY click the blue links inside the article. No searching. No cheating.

So if I start on 'Accordion' and I need to reach 'Black Hole'... I have to click my way there. Link by link. Just using my brain and intuition.

*(Click around live — make it feel spontaneous, even if you practiced.)*

Humans are surprisingly good at this. We use associations. We think — 'okay, Accordion → Music → Sound waves → Physics → Black Hole.' Done.

But here's my question. Can an AI do that?

Not Google Search. Not looking something up. Pure AI reasoning — navigating Wikipedia the same way you just did.

That's what we're building today."

*(Pause for effect.)*

"And by the end of this session — you're going to understand EXACTLY how it works. And more importantly... you're going to break it, fix it, and make it smarter."

*(Click to next slide.)*

---

### SLIDE 2: "What Even Is This?" — The Game Explained

**Title:** What Is WikiRace?

**Visuals:**

- Two Wikipedia article screenshots side by side, connected by a path of arrows
- A simple path visualization: Article A → Article B → Article C → Target
- Maybe 3–4 example routes (already in your existing slides)

**Text on slide:** Minimal. Just the two endpoints per example. No explanations — let the visuals speak.

**Interaction:** Ask for a volunteer to try a live WikiRace round (30 seconds max).

---

#### SCRIPT — SLIDE 2

"Alright, let me make this concrete.

*(Show examples: Chess → Game Theory, Python → Black Hole, Cricket → Neural Networks)*

Look at these. Chess to Game Theory. Cricket to Neural Networks. Elon Musk to SpaceX — okay that one's easy. But Music to Fourier Transform? That's wild.

Can I get a volunteer? *(Pick someone enthusiastic.)*

You have 60 seconds. Start on... *(pick something fun like 'Banana')* and get to *(something fun like 'World War II')*.

*(Let them try live on Wikipedia.)*

Look at what they're doing. They're not reading every word. They're SCANNING for familiar words. They're pattern-matching. They're thinking: 'What do I know about Banana that connects to something bigger?'

That intuition? That's actually really interesting. And it's exactly what we're going to teach our AI to do.

But first — let's understand WHY AI can't just do this naturally."

---

### SLIDE 3: The Challenge

**Title:** Humans vs. Machines

**Visuals:**

- Split screen: human brain on left, computer circuit on right
- Left side: "Cat" and "Dog" with warm colors, showing connection
- Right side: Cat = `[-0.0145, -0.0144, 0.0273...]`, Dog = `[-0.0189, 0.0082...]`

**Text on slide:**

- Left: "Humans: feel relationships"
- Right: "Computers: see symbols"
- One question at bottom: "How do we represent meaning mathematically?"

**What NOT to include:** Long technical explanations, formulas

---

#### SCRIPT — SLIDE 3

"Here's the problem.

You and I, when we hear 'Cat' and 'Dog' — we immediately FEEL they're related. Pets. Furry. Four legs. Possible rivals. *(Laugh)*

But to a computer? 'Cat' is just... the letters C, A, T. It's a string. It's data. The computer has ZERO idea that a cat and a dog are similar unless we somehow tell it.

So how do we tell a machine that 'Cat' and 'Dog' are closer in meaning than 'Cat' and 'Spaceship'?

That's the core problem of all AI language understanding. It's not about making computers fast. They're already fast. It's about making them understand *meaning*.

And the solution is... actually kind of beautiful.

We turn words into coordinates.

Stick with me. This is going to click in about 3 minutes."

---

## PHASE 2 — THE CORE PROBLEM (Slides 4–6)

### Duration: ~15 minutes

---

### SLIDE 4: Traditional NLP — What We Used to Do

**Title:** Traditional NLP — The Old Way

**Visuals:**

- Left column: list of old methods (Bag-of-Words, TF-IDF, N-grams, Rule-Based)
- Red warning box: "Limitations" with 4 bullets
- Right column: empty or grayed out (you fill it in later)

**Text on slide:** Just the method names + one-line descriptions. Already in your deck.

**Interaction:** Quick quiz — ask the audience to guess what's wrong with these methods.

---

#### SCRIPT — SLIDE 4

"So before modern AI, here's how computers used to handle language.

**Bag of Words.** You take a sentence, and you just... count the words. Forget order. Forget meaning. Just count. So 'The dog bit the man' and 'The man bit the dog' are IDENTICAL to the computer. *(Pause for laughs.)* Yeah. Not great.

**TF-IDF.** Slightly fancier. You say important words appear more. But still — no actual understanding of meaning.

**Rule-based systems.** Literal humans writing rules. Like... 'if the sentence contains the word 'happy', mark it as positive.' Can you imagine writing a rule for every word in every language? That's how we used to do AI.

**N-grams.** Takes sequences of words. A bit better. Still has no idea that 'automobile' and 'car' mean the same thing.

Can anyone guess what the big problems are? *(Take 2–3 answers.)*

Right. All of these treat words as isolated symbols. They have no semantic understanding. A synonym? Fails. A word used in a different context? Fails. A sentence where word order matters? Kind of fails.

Modern AI had to do something completely different.

It had to learn to put words in space."

---

### SLIDE 5: The Big Idea — Word Embeddings

**Title:** What If Words Had Coordinates?

**Visuals:**

- A 2D scatter plot with words plotted as dots
- Similar words clustered together: {dog, cat, wolf, tiger} in one cluster, {car, truck, bicycle} in another, {apple, banana, orange} in another
- Lines connecting similar words
- Large, clean, colorful — feels like a map

**Text on slide:** Essentially none. The visual IS the slide.

**Interaction:** Ask "Which word is closest to 'cat'?" before revealing the chart.

---

#### SCRIPT — SLIDE 5

"Okay here's the big idea. And I want you to actually feel this, not just hear it.

What if instead of treating 'Dog' as just letters, we gave it *coordinates*?

Like, imagine a map. *(Point to the scatter plot.)*

Every word gets a location on that map. Words that are *similar in meaning* are physically *close* to each other on the map. Words that are completely different are far apart.

So... *(point to clusters)* ... over here we have the animal cluster. Dog, cat, wolf, tiger — they're all near each other.

Over here — vehicles. Car, truck, bicycle. Close together.

Over here — fruits.

And now — magic happens. The computer doesn't need anyone to tell it 'cat and dog are similar.' It can MEASURE that similarity. It just looks at how close the dots are.

*(Build moment.)*

This is called a **Word Embedding**. You're taking a word — something abstract — and embedding it into a mathematical space.

And the beautiful part? We don't choose where the words go. The AI *learns* the positions by reading millions of sentences and figuring out: 'words that appear in similar contexts probably mean similar things.'

Dog and cat both appear near 'pet', 'fur', 'owner'. So they end up near each other. Automatically.

Quick question — *(ask the room)* — in this map, where do you think 'wolf' would sit? Near dog? Far from cat? *(Let them answer.)* Let's see..."

*(If you have the visualize.py demo ready, this is a great spot to run it live and show the actual AI-generated map.)*

---

### SLIDE 6: From 2D to 384 Dimensions

**Title:** The AI Brain — 384 Dimensions

**Visuals:**

- The same scatter plot, but with a label: "This is a 2D simplification"
- A visual of a 384-dimensional vector (just the numbers, not scary — more like "whoa, look at all this data")
- A simple analogy visual: GPS coordinates (2D) vs AI word coordinates (384D)

**Text on slide:**

- "In reality: 384 coordinates per word"
- "PCA collapses 384D → 2D so WE can see it"
- "The AI operates in the full 384D space"

---

#### SCRIPT — SLIDE 6

"Now I have a confession.

That beautiful 2D map I just showed you? That's a lie. Well — a simplification.

In reality, the AI doesn't put words in 2D space. It puts them in **384 dimensions**.

*(Pause for reaction.)*

I know. What does 384 dimensions even mean? You can't picture it. Neither can I. Neither can anyone. But here's the thing — you don't have to picture it.

Think about it this way. A GPS coordinate has 2 numbers: latitude and longitude. That's enough to tell you exactly where you are on Earth in 2D.

Now imagine if instead of just location, you wanted to capture EVERYTHING about a place. Its altitude. Its temperature. Its population density. Its noise level. Its culture. Its cuisine. You'd need hundreds of numbers.

That's what an embedding does for a word. It captures 384 different aspects of meaning. Things like: Is this word animate? Is it abstract? Is it related to science? To emotion? To time?

Each word becomes a list of 384 numbers. A coordinate in a 384-dimensional universe.

And when we want to *visualize* it — *(point to the scatter plot)* — we use a technique called PCA that squishes 384 dimensions down to 2, kind of like flattening a 3D globe into a flat map. You lose some detail, but the main structure stays.

The AI, though, operates in the full 384D space. And that's why it's so much better at understanding meaning than any of the old methods.

Does that make sense? Quick thumbs up if that clicked, thumbs sideways if you're still processing. *(Read the room, spend 30 extra seconds if needed.)*

Okay. Let's see this in action."

---

## PHASE 3 — HOW AI THINKS (Slides 7–9)

### Duration: ~20 minutes

---

### SLIDE 7: Semantic Similarity — The Key Concept

**Title:** How Similar Are Two Things?

**Visuals:**

- Three pairs, shown side by side with a "similarity score":
  - Cat / Dog → High similarity (0.87)
  - Dog / Spaceship → Low similarity (0.12)
  - King / Queen → Medium-high (0.75)
- A simple slider or bar showing "similarity"
- The word "cosine similarity" appears but is NOT explained yet

**Text on slide:** Just the pairs and scores. One line: "How do we measure closeness in 384D space?"

**Interaction:** Ask the audience to rank similarity before revealing scores.

---

#### SCRIPT — SLIDE 7

"Alright. We've got words as coordinates. Now — how do we measure if two things are *similar*?

Let me play a quick game with you. I'm going to say two words, and I want you to shout out a number from 0 to 10 for how similar they are. 0 is 'totally different', 10 is 'basically the same.'

Ready?

Cat. Dog. *(Get answers — should be high, 7–9.)*
Dog. Spaceship. *(Get answers — should be low, 1–2.)*
King. Queen. *(Get answers — interesting discussion.)*
Hot dog. Dog. *(This one's funny — people will argue.)*

Okay. The AI needs to do exactly what you just did. But mathematically. With coordinates.

The way it does that is with a concept called **cosine similarity**. I'm going to explain it with zero math, I promise.

*(Next beat.)*"

---

### SLIDE 8: Cosine Similarity — The Intuition

**Title:** Cosine Similarity — The Direction of Meaning

**Visuals:**

- Two arrows pointing in different directions from a center point
- Arrow 1 labeled "Dog" pointing upper-right
- Arrow 2 labeled "Cat" pointing upper-right (almost same direction) → "Similar!"
- Arrow 3 labeled "Spaceship" pointing lower-left → "Different!"
- The *angle* between arrows is highlighted
- No formulas. Just arrows and angles.

**Text on slide:**

- "Words as arrows from origin"
- "Small angle = similar meaning"
- "Large angle = different meaning"

**What NOT to include:** cos(θ) formula, dot product notation, mathematical derivation

---

#### SCRIPT — SLIDE 8

"Think of every word as an arrow — pointing in a specific direction in that 384-dimensional space.

*(Point to the diagram.)*

'Dog' points... let's say, upper right.
'Cat' also points... almost upper right. Nearly the same direction.
'Spaceship' points somewhere completely different. Lower left.

Now — how similar are two arrows? You measure the *angle* between them.

Dog and Cat have a small angle. Very similar direction. **High similarity.**
Dog and Spaceship have a huge angle. Totally different direction. **Low similarity.**

That's cosine similarity. The smaller the angle, the more similar the meaning.

*(Audience question:)* Why 'cosine'? Because in math, cosine is a function that gives you 1 when the angle is 0 degrees — same direction, maximum similarity — and 0 when the angle is 90 degrees — perpendicular, no relationship. Negative when opposite. But honestly — we don't need the math. We just need the intuition: **same direction = similar meaning.**

And this is exactly how our WikiRace bot decides where to navigate.

It looks at the current article. It looks at all the links. And it asks: 'Which link's title points in the most similar direction to the target article?'

Boom. That's the whole algorithm. Let me show you."

---

### SLIDE 9: LIVE DEMO SETUP — Embedding Visualization

**Title:** [No title needed — just the terminal]

**Visuals:**

- Switch to live terminal / IDE
- Run `visualize.py` live

**What to show:**

- The AI encoding words
- The scatter plot appearing
- Clusters forming

**Interaction:** Let students call out words to add to the plot

---

#### SCRIPT — SLIDE 9

*(Switch to terminal/IDE)*

"Okay. Theory over. Let's make the AI do something real.

*(Open `visualize.py`)*

This script is doing something deceptively simple. It's taking a list of words, running each through an AI model — specifically a model called `all-MiniLM-L6-v2`, which has been trained on billions of sentences — and getting 384-dimensional coordinates for each one.

Then it collapses those 384 dimensions down to 2 using PCA, and draws a map.

*(Run it.)*

Look at that. *(Let the plot appear.)*

Did anyone tell the AI that dog and cat are related? *(No.)* Did anyone tell it that apple and banana are both fruits? *(No.)* The AI figured this out just by reading text — by noticing that these words appear in similar contexts.

*(Interactive moment:)* Okay — who wants to add a word? Shout something out.

*(Take 3–5 suggestions. Add them to the `words` list. Re-run. React to where they land.)*

Did 'pizza' land near 'food'? Did 'internet' land near 'computer'? What happened with 'love'? *(These moments of surprise are gold.)*

This. This right here. This is how the AI 'understands' language.

Now — let's put it to work on WikiRace."

---

## PHASE 4 — THE BOT IN ACTION (Slides 10–12)

### Duration: ~20 minutes

---

### SLIDE 10: The WikiRace Bot — Architecture

**Title:** How the Bot Plays WikiRace

**Visuals:**

- A clean flowchart (not code) showing:
  1. Bot is at Article A
  2. Gets all links on the page (list)
  3. Encodes target article as embedding
  4. Encodes each link as embedding
  5. Computes cosine similarity for all
  6. Picks highest similarity link
  7. Navigate → repeat
- Arrows connecting the steps, clean and visual
- No code on this slide

**Text on slide:** Just the 7 steps, one line each. Clean and readable.

---

#### SCRIPT — SLIDE 10

"So here's how the bot thinks. Step by step.

Step 1: The bot is on a Wikipedia article. It fetches all the blue links — could be 200, 300 links.

Step 2: It takes the *target* article — say, 'Black Hole' — and runs it through the AI model. It gets a 384-dimensional vector. A direction in space.

Step 3: It does the same for EVERY link on the current page. Every single one.

Step 4: It computes cosine similarity between the target and each link. Basically asking: 'Which of these 300 links is pointing in the most similar direction to Black Hole?'

Step 5: It picks the winner. Navigate.

Step 6: Repeat. New page. New links. Same process.

That's it. The bot is a greedy navigator. It always picks the link that FEELS most similar to the target. No planning ahead. No strategy. Just: 'what's closest right now?'

Sounds simple. Let's see if it actually works.

*(Transition to terminal.)*"

---

### SLIDE 11: LIVE DEMO — Bot vs. Human

**Title:** [Switch to terminal — no slide needed]

**What to do:**

1. Run `embedding_bot.py`
2. Watch the bot navigate live
3. Read each step aloud
4. React to the choices

**Interaction:** Before each step, ask the audience "Where do you think it'll go next?"

---

#### SCRIPT — SLIDE 11

*(Terminal is open. `embedding_bot.py` is ready to run.)*

"Alright. Bot versus Wikipedia. Let's go.

*(Run it.)*

Okay — it's picked a start and target. *(Read them aloud.)*

Start: [X]. Target: [Y].

Before it moves — show of hands — who thinks the bot is going to WIN? *(Count hands.)* Who thinks it's going to get lost or loop forever? *(Count hands.)* Alright. Let's see.

*(Bot starts navigating — read each step aloud as it outputs.)*

It's on '[Article]'. It chose '[Link]'. Why? Because '[Link]' is apparently the most semantically similar thing to '[Target]' on that page. Interesting.

*(Keep commentary going — this is the heart of the demo.)*

Oh! It just jumped to '[Unexpected Article]'. Did anyone see that coming? This is the bot being... well, a little dumb. It found a word that sounded similar but it's going in the wrong direction.

*(If it wins:)* IT WON! *(Clap.)*

*(If it fails/loops:)* Interesting! It gave up. Why? Let's think about what went wrong.

*(Turn this into a discussion — what could have confused the bot? What did it optimize for that ended up being wrong? This is great learning.)*"

---

### SLIDE 12: Understanding the Bot's Failures

**Title:** When the Bot Breaks

**Visuals:**

- Three failure modes illustrated:
  1. **The Rabbit Hole**: Bot keeps navigating deeper into one specific topic and can't get out (e.g., stuck on Medieval History)
  2. **False Friends**: A link that SOUNDS similar but isn't (e.g., "Python" the snake vs "Python" the language)
  3. **Dead End**: All remaining links have been visited

**Text on slide:** Just the 3 failure names + one emoji each. No long text.

**Interaction:** Ask students to explain each failure in their own words after you describe it.

---

#### SCRIPT — SLIDE 12

"So the bot sometimes fails. And that's actually really interesting — because the failures tell us a lot about what the AI is and isn't doing.

Failure #1: The Rabbit Hole.

The bot gets really interested in one topic. Like... it's trying to reach 'Albert Einstein' and it stumbles onto 'Mathematics'. Now every link on the Mathematics page is also mathematical. So it goes deeper and deeper into math and can't find a way out. It's committed. Stubbornly committed. *(Laughter.)* Sound like anyone you know?

Failure #2: False Friends.

This is my favorite. Say the target is 'Python programming language'. The bot might navigate to an article about snakes because 'Python' appears in a similar context as 'snake'. It doesn't know that Python-the-language and Python-the-animal are completely different things in this context.

Humans wouldn't do this. You have context. The AI doesn't — at least not this version.

Failure #3: The Dead End.

The bot marks visited pages to avoid loops. But sometimes it visits so many pages that all the best links are already visited and it's stuck.

*(To audience:)* Quick question — how would you fix each of these? Just brainstorm.

*(Take answers — students often come up with penalty scores, backtracking, lookahead — which is exactly what the bot does! Set this up for the next section.)*"

---

## PHASE 5 — INSIDE THE ALGORITHM (Slides 13–16)

### Duration: ~20 minutes

---

### SLIDE 13: The Scoring Formula

**Title:** The Bot's Decision Formula

**Visuals:**

- A visual "recipe card" (not a math formula — a cooking-style recipe):
  - Base ingredient: Cosine Similarity (the main thing)
  - Bonus: Overlap of words with target (+0.3 per matching word)
  - Penalty: Words you've seen a lot recently (-0.15 each)
  - Emergency exit: If score is too low → pick randomly

**Text on slide:** The recipe card visual. Nothing else.

**What NOT to include:** Code, math notation, Python syntax

---

#### SCRIPT — SLIDE 13

"Let me show you the bot's brain. Not code — a recipe.

*(Point to the recipe card.)*

Main ingredient: cosine similarity. This is the foundation. How similar does this link *feel* to the target?

First bonus: word overlap. If some of the actual words in the link title appear in the target, we add a little bonus. Because even before the AI thinks, there's a simple hint: 'if the words literally overlap, that's probably a good sign.'

Penalty: diversity tax. If the bot has been visiting lots of articles that all contain the same word — like it's been visiting music-related articles for 4 steps in a row — it gets *penalized* for picking another music article. This is the anti-rabbit-hole mechanism.

Emergency escape: If the best score is basically zero — meaning nothing on this page is related to the target — the bot just picks randomly. A Hail Mary.

That's it. That's the whole scoring function in English.

Now — and this is the fun part — all those numbers? The +0.3, the -0.15, the score threshold? Those are *tunable parameters*. And you're going to tune them."

---

### SLIDE 14: Looking at the Code (Gently)

**Title:** The Bot's Brain — A Quick Peek

**Visuals:**

- A screenshot of the key section of `embedding_bot.py`, highlighting (not explaining) these 3 lines:

  ```python
  score += overlap * 0.3         # word overlap bonus
  score -= overused_words[word] * 0.15  # diversity penalty
  if best_score <= 0.05:         # escape hatch
  ```

- Large font, high contrast, rest of code is dimmed
- Arrows pointing to the 3 highlighted lines with simple labels

**Text on slide:** Just the 3 labels (Word Overlap Bonus, Diversity Penalty, Escape Hatch)

---

#### SCRIPT — SLIDE 14

"I know we said no heavy coding. And I meant it. But I want to show you something for just 60 seconds.

*(Point to the highlighted code.)*

These three lines are the tunable parts of the bot. That's it. The rest of the code is infrastructure — fetching Wikipedia, running the bot, handling errors. Plumbing.

But these three numbers?

`overlap * 0.3` — what happens if we change 0.3 to 1.0? The bot becomes obsessed with literal word matches. Maybe better, maybe worse.

`overused_words[word] * 0.15` — what if we change 0.15 to 0.5? The bot becomes *very* eager to explore new territory.

`best_score <= 0.05` — what if we raise this to 0.2? The bot gives up on promising paths faster and randomizes more often.

None of you need to understand Python to understand this. These are just dials. And in a few minutes, you're going to turn them.

But first — let me show you the different *personalities* a bot can have based on how these are set."

---

### SLIDE 15: The Bot Zoo — Different Strategies

**Title:** Meet the Bot Zoo

**Visuals:**

- 4 "character cards" (like Pokémon cards or character select screens):
  1. **The Greedy Bot** — Only cosine similarity, no penalties, no bonuses. Goes purely on vibes.
  2. **The Cautious Bot** — High diversity penalty. Never revisits similar territory. Explores widely.
  3. **The Keyword Bot** — Heavy overlap bonus. Only trusts literal word matches. Ignores semantics.
  4. **The Chaotic Bot** — Low escape threshold. Randomizes frequently. Unpredictable but sometimes genius.
- Each card has a personality description, a strength, and a weakness
- Fun, game-like visual style

**Text on slide:** The 4 character cards. Light, fun style.

**Interaction:** Ask students to vote on which bot they think will win.

---

#### SCRIPT — SLIDE 15

"Let me introduce you to the Bot Zoo.

*(Reveal each card dramatically.)*

**The Greedy Bot.** Purely cosine similarity. No bonuses, no penalties. It just always picks whatever feels most similar. Fast, decisive. But it falls into rabbit holes HARD.

**The Cautious Bot.** Heavy diversity penalty. Every time it goes near a topic it's visited recently, it backs off. It's the bot that never gets stuck — but sometimes it wanders so far from the target that it loses its way entirely.

**The Keyword Bot.** Doesn't really trust the AI model. It mostly cares about literal word overlap. If the target is 'Neural Networks', it will ONLY pick links that contain the word 'Neural' or 'Network'. Sometimes brilliant. Often myopic.

**The Chaotic Bot.** Low confidence threshold. If nothing scores above 0.2, it picks randomly. You'd think this is terrible. But sometimes randomness is exactly what gets you out of a local trap.

*(Poll the room:)* Which bot wins most often? Vote!

*(After votes:)* Here's the twist — there is no single winner. It *depends* on the start and target. Against some pairs, the Greedy Bot crushes it. Against others, the Chaotic Bot flukes a win in 3 steps.

This is the key insight of the workshop: **AI behavior is not fixed. It's a set of design choices.**

And that's what makes AI engineering interesting. Not just understanding the math. But understanding the *tradeoffs*."

---

### SLIDE 16: Quick Recap Before Break

**Title:** What You Now Know

**Visuals:**

- Simple 5-point recap, each with an icon:
  1. 🧠 Words can be represented as coordinates (embeddings)
  2. 📐 Closeness in embedding space = semantic similarity
  3. 📏 Cosine similarity measures that closeness
  4. 🤖 The bot navigates by always picking the "closest" link
  5. 🎛️ Tunable parameters change bot personality

**Text on slide:** The 5 bullets, clean and visual. Nothing more.

---

#### SCRIPT — SLIDE 16

"Before we break — let me check what's in your brain right now.

*(Go through the 5 points quickly, pointing at each.)*

Words as coordinates — did that make sense? Thumbs up.

Cosine similarity — we're measuring the angle between word arrows. Make sense?

The bot's decision process — greedy, pick the most similar link.

And here's the most important one: the parameters are tunable. You're not just observers here. You're the AI engineers.

After the break, you're going to actually tune these bots. Run experiments. See which strategies work. And compete against each other.

Ten-minute break. Get water. Stretch. And think about which bot personality you'd design."

---

## — 10 MINUTE BREAK —

*During break: reset terminal, have `embedding_bot.py` open and ready to modify, maybe show a fun bot failure GIF on the screen.*

*Energy re-setter when people come back:* "Okay! Welcome back. Quick question before we start — did anyone think of a bot strategy during the break? Anyone? No? That's fine, you're going to in about 2 minutes."

---

## PHASE 6 — LIVE EXPERIMENTS (Slides 17–20)

### Duration: ~30 minutes + 15 min for explanations

---

### SLIDE 17: The Experiment Lab

**Title:** You Are Now the AI Engineer

**Visuals:**

- A clean "experiment lab" style slide
- 3 experiments listed:
  1. Greedy vs Balanced — same route, compare results
  2. Overlap Tuning — slide the overlap bonus and observe
  3. Escape Rate Tuning — how random should the bot be?
- Each experiment has a simple hypothesis: "We think that..."
- A leaderboard placeholder

**Text on slide:** The 3 experiment names + one-line hypothesis each.

**What NOT to include:** Instructions, code snippets, step-by-step

---

#### SCRIPT — SLIDE 17

"Welcome to the experiment lab.

For the next 30 minutes, you're going to do what AI researchers do: form a hypothesis, run an experiment, observe results, and update your thinking.

We have three experiments. They're all run by tweaking a couple of numbers in `embedding_bot.py`. That's it. No writing code from scratch.

*(Walk through the three experiments.)*

**Experiment 1: Greedy vs Balanced.** We'll run the bot on the same route twice. Once as a pure greedy bot (no penalties, no bonuses). Once as a balanced bot (moderate penalties and bonuses). Same starting point. Who wins?

**Experiment 2: Overlap Bonus.** We'll slide the `0.3` overlap bonus up and down. What happens at `0.0`? At `1.5`? At what point does over-trusting word matches hurt the bot?

**Experiment 3: Escape Rate.** We'll raise and lower the escape threshold. At what point does adding randomness actually help instead of hurt?

*(To the room:)* Before we start — I want you to form predictions. Don't just run the code and watch. Think about what YOU expect to happen first. That's the scientific method. And it's also how AI researchers actually work."

---

### SLIDE 18: Experiment 1 — Greedy Bot

**Title:** [Terminal / Live Demo]

**What to do:**

1. Comment out the overlap bonus and diversity penalty
2. Run the bot on route "Banana → Albert Einstein"
3. Record steps and result
4. Un-comment, run again
5. Compare

**Interaction:** Students call out predictions. Record on whiteboard or sticky notes.

---

#### SCRIPT — SLIDE 18

*(Switch to `embedding_bot.py`)*

"Alright. Experiment 1. I'm going to comment out the overlap bonus and the diversity penalty. This is now the pure greedy bot. Only cosine similarity.

Route: Banana → Albert Einstein.

Predictions? How many steps do you think?

*(Collect predictions.)*

Running...

*(Read results aloud as they appear. React genuinely to choices. Pause when something surprising happens.)*

Okay! *(Share result.)*

Now I'm going to un-comment the bonuses. Same route. Let's compare.

*(Run again.)*

Interesting! *(Compare the two.)*

What does this tell us? *(Open discussion.)*

The key thing I want you to notice: sometimes more 'intelligence' — more tuning — doesn't automatically mean better results. The greedy bot sometimes wins because it's fast and decisive. The balanced bot sometimes wins because it avoids traps. **There is no universal winner.**

This is exactly like designing any AI system. You have to test. You have to observe. You have to adapt."

---

### SLIDE 19: Experiment 2 — Overlap Bonus Tuning

**Title:** [Terminal / Live Demo]

**Guided parameter sweep:**

- `overlap * 0.0` (pure semantics)
- `overlap * 0.3` (default)
- `overlap * 1.0` (strong bias toward literal word match)
- `overlap * 2.0` (almost completely relying on keyword match)

**Record results on a shared whiteboard or screen.**

---

#### SCRIPT — SLIDE 19

"Now let's tune that overlap bonus.

Current value: 0.3. Default. Moderate trust in literal word overlap.

What I'm asking: at what value does this make the bot smarter? And at what value does it backfire?

Let's run the experiment. I'll change the value, you tell me what you predict.

*(Go through each value. Run, record, compare.)*

At 0.0 — purely AI-driven semantics. No keyword cheating. How does it do?

At 1.0 — strong keyword bias. Does the bot start making dumber choices or smarter ones?

At 2.0 — keyword obsession. Watch for the False Friend problem I mentioned earlier. Will the bot get confused by words that overlap but don't actually help?

*(After running all four:)*

Anyone want to guess the optimal value? *(Take guesses.)*

And here's the meta-lesson: this process — trying values, observing, adjusting — is called **hyperparameter tuning**. It's literally what AI engineers do every day. In way more complex systems. But the principle is identical.

You just did hyperparameter tuning. Without knowing it. *(Let that land.)*"

---

### SLIDE 20: Experiment 3 — Student Bot Design

**Title:** Design Your Own Bot

**Visuals:**

- A blank "Bot Design Card" template:
  - Bot name
  - Overlap bonus value
  - Diversity penalty value
  - Escape threshold
  - Expected strength
  - Expected weakness

**Interaction:** Each student / pair fills out a card, then we run a "bot race" — same route, different configs, who gets there fastest?

---

#### SCRIPT — SLIDE 20

"Okay. Final experiment. This one's yours.

I want each of you — individually or in pairs — to design your own bot.

*(Hand out / display the Bot Design Card.)*

Pick your overlap bonus. Pick your diversity penalty. Pick your escape threshold. Name your bot. Give it a personality.

You have 5 minutes. *(Actually give them 5 minutes.)*

Then we're going to run a bot race. Same route for everyone. We're going to see whose bot wins.

*(After 5 minutes, collect configs or have students type their values in live.)*

Bot race time!

*(Run each config on the same route. Record results. Build to a winner.)*

*(Declare winner with fanfare.)*

Congrats to the [bot name] — which was designed by [student name(s)]!

*(Ask the winner:)* What was your reasoning? Why did you pick those values?

*(This creates a moment of ownership — the student explains their AI design choice to the room. That's a powerful feeling.)*"

---

## PHASE 7 — THE BIG PICTURE (Slides 21–23)

### Duration: ~10 minutes

---

### SLIDE 21: From WikiRace to the Real World

**Title:** Same Technology. Much Bigger Scale.

**Visuals:**

- 6 boxes, each with a logo/icon and a one-line description:
  - **Spotify** — "Embeddings of songs and listener preferences → recommendation"
  - **Google Search** — "Embeddings of your query and billions of pages → relevance"
  - **ChatGPT** — "Embeddings of conversation context → next word prediction"
  - **Netflix** — "Embeddings of viewing history → 'you might also like'"
  - **GitHub Copilot** — "Embeddings of your code → autocomplete"
  - **Instagram Explore** — "Embeddings of what you engage with → feed"

**Text on slide:** Just the 6 boxes. Very visual.

---

#### SCRIPT — SLIDE 21

"Let me zoom out for a second.

What you built today — or rather, what you tuned today — is a real technique called **semantic search**. And it's the backbone of almost everything you use.

*(Go through the 6 boxes.)*

Spotify recommendations? Embeddings. Your listening history is converted to a point in embedding space. Every song is a point. The recommendation system finds songs that are 'close' to you.

Google Search? When you type a query, Google converts it to an embedding and finds web pages with embeddings close to yours. Not just keyword matching — *meaning* matching. That's why 'cheap flights' and 'affordable airfare' both return the same results.

ChatGPT? Transformers — the model family I mentioned earlier — process your entire conversation as embeddings. Every token becomes a vector. The model predicts the next token by looking at what's 'nearby' in that space.

Netflix, Instagram, GitHub Copilot — all the same underlying idea, just tuned for different domains.

You have used embeddings thousands of times today alone. You just didn't know it had a name.

*(Pause.)*

Now you do."

---

### SLIDE 22: What Makes a Good AI Engineer

**Title:** What You Actually Learned Today

**Visuals:**

- Three columns:
  1. **Build** — Understand how components connect
  2. **Observe** — Watch the AI fail and succeed
  3. **Tune** — Adjust parameters and iterate
- Below that: "This is 80% of real AI work"

**Text on slide:** The three words and descriptions. Clean.

---

#### SCRIPT — SLIDE 22

"I want to be honest with you about something.

A lot of workshops about AI will show you math equations and expect you to be amazed. Or they'll show you a chat demo and act like you built something.

Today we did something different.

We looked at an actual AI system. We understood how its components work — conceptually, not just 'it does AI stuff.' We watched it fail. We asked WHY it failed. We tuned it. We compared strategies.

*(Point to the three columns.)*

Build. Observe. Tune.

That loop? That IS AI engineering. Whether you're working at Google on a search system or building a recommendation engine at a startup — it's the same loop. You build a system, you watch how it behaves, and you tune it.

The math gets harder. The scale gets bigger. But the loop never changes.

And you just did it. With Wikipedia, a sentence transformer model, and those 3 numbers in a Python file.

*(Beat.)*

That's not small."

---

### SLIDE 23: What's Next

**Title:** Where to Go From Here

**Visuals:**

- A path / roadmap visual:
  - Step 1: Run the bot on new routes (tonight)
  - Step 2: Try replacing the scoring function entirely
  - Step 3: Look into `sentence-transformers` documentation
  - Step 4: Learn about BFS/graph search for a smarter bot
  - Step 5: Build something with embeddings (search engine, recommendation system)

**Text on slide:** Just the 5 steps, minimal.

---

#### SCRIPT — SLIDE 23

"If you want to go further — and I hope you do — here's the path.

*(Walk through the roadmap.)*

Start tonight. Run the bot on routes you pick. See what happens with weird combos — 'Pizza to Philosophy'. 'Taylor Swift to Nuclear Physics'.

Then try rewriting the scoring function. What if you used a different model? What if you looked ahead 2 steps instead of 1?

The `sentence-transformers` library that powers all of this has incredible documentation. It's free. It's Python. The model we used — `all-MiniLM-L6-v2` — runs on a laptop in under 5 seconds.

If you want to go deeper, look into BFS — breadth-first search — as a way for the bot to plan ahead instead of being purely greedy. That's actually how a lot of game-playing AI works.

And if you want to build something real — a search engine, a recommendation system, a document finder — embeddings are your foundation. Everything else builds on what you learned today."

---

## PHASE 8 — WRAP UP (Slides 24–25)

### Duration: ~10 minutes

---

### SLIDE 24: The One-Sentence Summary

**Title:** [Large text, almost no design]

> **"Words are coordinates. Similarity is distance. Intelligence is navigation."**

**Visuals:**

- Just the quote. Big. On a dark background. Nothing else.

---

#### SCRIPT — SLIDE 24

"If you take one thing from today, let it be this.

*(Read it aloud slowly.)*

**Words are coordinates. Similarity is distance. Intelligence is navigation.**

That's it. That's modern NLP. That's how ChatGPT reasons about language. That's how Spotify finds your next favorite song. That's how Google understands that 'cheap flights' and 'affordable airfare' mean the same thing.

It sounds simple when you say it out loud. But the hard part was convincing the world this was possible — and training models big enough to actually do it well.

The concepts you learned today? You'd cover these in a third-year university AI course. And you understood them in two and a half hours because we used a real system and played around with it.

That's how learning works. You don't need to memorize. You need to *touch the system*."

---

### SLIDE 25: Q&A + Credits

**Title:** Questions? Let's Talk.

**Visuals:**

- Wikirace.ai logo
- GitHub repo link / QR code
- Contact / social info
- Microsoft Innovation Club branding

**Interaction:** Open Q&A — but seed 2–3 good questions in case the room is quiet.

---

#### SCRIPT — SLIDE 25

"That's the workshop! Before Q&A — huge thanks to Microsoft Innovation Club for hosting this.

The GitHub repo for this project is linked here. Everything we ran today is in there. The bot, the visualizer, the whole game. It's all yours to play with.

*(Seed questions if the room is quiet:)*

Actually — I know some of you have questions you're too shy to ask. So let me ask them for you.

'Is the bot cheating by using an AI model?' — Great question. No. It's using the same tool humans have access to: understanding of language. We just formalized it mathematically.

'Could you make a bot that ALWAYS wins WikiRace?' — Maybe. With a BFS algorithm and a large enough graph, yes. But it wouldn't be learning — it would be searching. There's a difference.

'Is this how ChatGPT works?' — Partially yes. ChatGPT uses a much more complex version of these same ideas. Transformers, attention mechanisms, much larger embeddings. But the core intuition — turn language into a navigable space — is exactly the same.

*(Open the floor for real questions.)*

Any questions? Nothing is too simple. The best questions I've gotten in workshops like this have been 'wait, what's actually a token?' and 'why can't the bot just cheat and search?' So please — ask anything.

*(Handle questions naturally. For things you don't know: 'That's a great question and I genuinely don't know — let's look it up together' is always the right answer.)*"

---

## APPENDIX A: HANDLING COMMON PROBLEMS

### If the demo fails live

"Okay, so the bot just crashed. Which is... actually perfect? Because now we can debug it live. This is what working with AI systems is actually like. Something breaks, and you have to figure out why."

- Check if Wikipedia API is rate-limiting (common)
- Have a pre-recorded terminal session as backup
- Reframe it as a live debugging exercise — students love it

### If a student asks something you can't answer

"That's genuinely a great question and I don't want to guess. Let me say what I think is happening, and we can verify it together." Then either Google it live or table it for after.

### If the room is too quiet

- Direct questions to specific people: "Hey, you — yes you with the blue hoodie — what do YOU think happens if we set the penalty to zero?"
- Introduce a tiny competition: "First person to correctly predict what the bot does next wins a point"
- Switch to a pair activity: "Talk to the person next to you for 60 seconds — what's the most surprising thing so far?"

### If you're running late

Cuts to make:

- Shorten Experiment 2 (overlap tuning) — just run 2 values instead of 4
- Skip Experiment 3 (student bot design) or do it as a thought exercise rather than live
- Cut the "What's Next" slide

### If you're running early

Extensions to add:

- Run a "bot race" with students suggesting route pairs
- Show what happens with a completely wrong model (e.g., what if we gave all embeddings a value of zero — how would the bot behave?)
- Discuss what a transformer is at a high level using the attention mechanism analogy

---

## APPENDIX B: KEY ANALOGIES REFERENCE SHEET

| Concept | Best Analogy |
|---|---|
| Embeddings | GPS coordinates for meaning |
| High-dimensional space | More descriptors = more accurate address |
| Cosine similarity | The angle between two arrows |
| Semantic similarity | "Cat and dog point in almost the same direction" |
| PCA / dimensionality reduction | Flattening a globe to a 2D map |
| Hyperparameter tuning | Adjusting seasoning in a recipe |
| Greedy algorithm | Always taking the nearest-looking road |
| Rabbit hole failure | Getting absorbed in a Wikipedia spiral |
| Bag-of-words | Judging a book by counting its words |
| Transformer model | A very well-read entity that learned from billions of books |

---

## APPENDIX C: ENERGY MANAGEMENT GUIDE

| Workshop Phase | Energy Level | Technique |
|---|---|---|
| Hook (Phase 1) | 🔥 HIGH | Live demo, volunteer, surprises |
| Core Problem (Phase 2) | 📚 Medium | Short, punchy explanations |
| Embeddings (Phase 3) | 🎯 Medium-High | Interactive quiz, live visualization |
| Bot Demo (Phase 4) | 🔥 HIGH | React genuinely, keep commentary going |
| Algorithm Deep-dive (Phase 5) | 📚 Medium | Keep it recipe-like, avoid jargon |
| Break | 💤 Reset | Loud music, funny slide |
| Experiments (Phase 6) | 🔥 HIGH | Competition, collaboration, prizes |
| Big Picture (Phase 7) | 🎯 Medium-High | Real-world connections, personal relevance |
| Wrap-up (Phase 8) | 🌟 Warm | One big insight, gratitude, Q&A |

---

## APPENDIX D: PRE-WORKSHOP CHECKLIST

- [ ] Repo cloned and dependencies installed (`pip install -r requirements.txt`)
- [ ] `0_warmup.py` run at least once (model downloaded)
- [ ] `visualize.py` tested — scatter plot generates correctly
- [ ] `embedding_bot.py` tested on at least one route
- [ ] `bot_terminal.py --bot` tested with a JSON command
- [ ] Wikipedia accessible (check firewall/network)
- [ ] Terminal font size increased (minimum 18pt)
- [ ] Slides in presentation mode, speaker notes hidden from audience
- [ ] Backup terminal session recorded (in case of live failure)
- [ ] Extra routes prepared: 5–6 interesting start/target pairs ready
- [ ] Timer on phone or laptop for break
- [ ] Water on table (you'll be talking a lot)

**Good route pairs for demos:**

- Banana → Albert Einstein (fun, usually works)
- Chess → Neural Networks (thematic)
- Cricket → Quantum Mechanics (long but interesting)
- Pizza → Philosophy (surprisingly connected)
- Bicycle → Space Station (fun failure modes)

---

## APPENDIX E: STUDENT TAKEAWAY CARD

*Print this or put it on the last slide as a photo moment:*

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Wikirace.ai Workshop — What You Learned
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Words are coordinates. (Embeddings)
  Closeness is similarity. (Cosine similarity)
  Intelligence is navigation. (Semantic search)

  The model: all-MiniLM-L6-v2
  The library: sentence-transformers (pip install)
  The loop: Build → Observe → Tune → Repeat

  GitHub: [your repo link]

  "You didn't just watch AI. You tuned it."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*End of Playbook — Workshop by Anas Arfeen | Microsoft Innovation Club*
