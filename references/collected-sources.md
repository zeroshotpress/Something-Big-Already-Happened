# Collected Sources for "Something Big Already Happened"

Compiled: 2026-02-13
Researcher: Phase 2 automated collection

> **Note on model-releases.csv**: The original CSV had 26 rows. Two missing models
> have been identified and added: **Grok 4.1** (Nov 17, 2025) and **Gemini 3 Deep Think**
> (Dec 4, 2025), bringing the total to 28 rows. Chapter text referencing
> "twenty-eight major models" is now accurate.

---

## Source 1: Fortune -- Boris Cherny / Roon on 100% AI-Written Code

**URL:** https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/
**Date:** January 29, 2026
**Author:** Fortune staff

### Key Quotes (Exact / Verbatim)

**Boris Cherny (Head of Claude Code, Anthropic):**
- "100% for two+ months now, I don't even make small edits by hand" [EXACT]
- "I shipped 22 PRs yesterday and 27 the day before, each one 100% written by Claude" [EXACT]
- "I have never had this much joy day to day in my work" [EXACT]
- "Engineers just feel unshackled, that they don't have to work on all the tedious stuff anymore" [EXACT]

**Roon (OpenAI researcher, pseudonym):**
- "100%, I don't write code anymore" [EXACT]
- "Programming always sucked. It was a requisite pain for ~everyone who wanted to manipulate computers into doing useful things, and I'm glad it's over" [EXACT]

### Key Data Points
- Anthropic company-wide AI code generation: 70-90% [EXACT RANGE]
- Claude Code specifically: ~90% of its own code is AI-written [EXACT]
- Microsoft (April 2025): ~30% AI-generated code [EXACT]
- GitHub study reference: ~29% of U.S. Python functions are AI-written [EXACT]

### Anthropic Hiring Shift (from same article)
- Anthropic now hiring generalists rather than specialists
- Quote attributed to Fortune article context: "Not all of the things people learned in the past translate to coding with LLMs" [PARAPHRASED -- exact source uncertain; may be editorial summary rather than direct quote]

---

## Source 2: Simon Willison -- StrongDM Software Factory Analysis

**URL:** https://simonwillison.net/2026/Feb/7/software-factory/
**Date:** February 7, 2026
**Author:** Simon Willison

### Key Quotes (Exact / Verbatim)

**Simon Willison:**
- Described "Code must not be reviewed by humans" as "the most interesting of these, without a doubt" [EXACT]
- "how can you prove that software you are producing works if both the implementation and the tests are being written for you by coding agents?" -- identified as "the most consequential question in software development right now" [EXACT]

### November 2025 Inflection Point
- "Claude Opus 4.5 and GPT 5.2 appeared to turn the corner on how reliably a coding agent could follow instructions" [EXACT -- Willison's characterization]

### Historical Timeline (from Willison's analysis)
- "with the second revision of Claude 3.5 (October 2024), long-horizon agentic coding workflows began to compound correctness rather than error" [EXACT]
- "By December of 2024, the model's long-horizon coding performance was unmistakable via Cursor's YOLO mode" [EXACT]

---

## Source 3: StrongDM Software Factory

**URL:** https://factory.strongdm.ai/
**Date:** Published 2025-2026 (exact date unclear)
**Authors:** Justin McCarthy (CTO), Jay Taylor, Navan Chauhan

### Core Principles (Exact / Verbatim)
- "Code **must not be** written by humans" [EXACT]
- "Code **must not be** reviewed by humans" [EXACT]
- "If you haven't spent at least **$1,000 on tokens today** per human engineer, your software factory has room for improvement" [EXACT]

### Team Details
- Founded July 14, 2025 by Justin McCarthy (co-founder, CTO), Jay Taylor, and Navan Chauhan [EXACT -- 3-person team]

### Digital Twin Universe (DTU)
- "behavioral clones of the third-party services our software depends on" [EXACT]
- Clones created for: Okta, Jira, Slack, Google Docs, Google Drive, Google Sheets [EXACT]
- DTU enables "thousands of scenarios per hour without hitting rate limits, triggering abuse detection, or accumulating API costs" [EXACT]

### Scenario-Based Testing
- A "scenario" represents an end-to-end user story, "often stored outside the codebase (similar to a 'holdout' set in model training)" [EXACT]
- Success metric shifted from boolean to probabilistic: "satisfaction" -- the fraction of observed trajectories likely satisfying user requirements [EXACT]

### Attractor Tool
- Non-interactive coding agent that composes models, prompts, and tools into a graph-structured pipeline [PARAPHRASED]
- Operates end-to-end once work is fully specified [PARAPHRASED]
- GitHub repo (github.com/strongdm/attractor) contains NO code -- only three markdown spec files [EXACT]
- Pipeline authors define multi-stage AI workflows as directed graphs using Graphviz DOT syntax [PARAPHRASED]
- Markdown specs serve as the source of truth; feed them into your coding agent to build your own version [PARAPHRASED]

### Key Catalyst
- Breakthrough arrived with Claude 3.5 (October 2024 revision), when "long-horizon agentic coding workflows began to compound correctness rather than error" [EXACT]

---

## Source 4: Dan Shapiro -- The Five Levels: from Spicy Autocomplete to the Dark Factory

**URL:** https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/
**Date:** January 2026
**Author:** Dan Shapiro (CEO of Glowforge)
**Secondary coverage:** https://simonwillison.net/2026/Jan/28/the-five-levels/

### The Five Levels Framework (Exact / Verbatim where quoted)

**Level 0 -- Spicy Autocomplete:**
"Level Zero is your parents' Volvo, maybe with an automatic transmission. Whether it's vi or Visual Studio, not a character hits the disk without your approval. You might use AI as a search engine on steroids or occasionally hit tab to accept a suggestion, but the code is unmistakably yours." [EXACT]

**Level 1 -- The Coding Intern:**
"At Level 1, you've got lanekeeping and cruise control. You're writing the important stuff, but you offload specific, discrete tasks to your AI intern." [EXACT]

**Level 2 -- The Junior Developer:**
"At Level 2, you've got Autopilot on the highway. You've got a junior buddy to hand off all your boring stuff to. This is where 90% of 'AI-native' developers are living right now." [EXACT]
- Key stat: **90% of AI-native developers are at Level 2** [EXACT]

**Level 3 -- The Developer (Human as Manager):**
"Level 3 is a Waymo with a safety driver. You're not a senior developer anymore; that's your AI's job. You are... a manager. You are the human in the loop." [EXACT]

**Level 4 -- The Engineering Team:**
"More of an engineering manager or product/program/project manager. You collaborate on specs and plans, the agents do the work." [EXACT from Willison's summary]

**Level 5 -- The Dark Software Factory:**
"Like a factory run by robots where the lights are out because robots don't need to see." [EXACT]
"At level 5, it's not really a car any more...your software process isn't really a software process any more. It's a black box that turns specs into software." [EXACT]

### Simon Willison's commentary on Level 5 teams:
- "Nobody reviews AI-produced code, ever. They don't even look at it." [EXACT]
- "The goal of the system is to prove that the system works." [EXACT]
- Teams consist of experienced developers focusing on system design and agent effectiveness demonstration [PARAPHRASED]

---

## Source 5: Sam Schillace -- "I Have Seen the Compounding Teams"

**URL:** https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams
**Date:** September 28, 2025
**Author:** Sam Schillace (Deputy CTO, Microsoft)
**Publication:** Sunday Letters (Substack)

### Key Observations (Mixed exact and paraphrased -- Substack was access-restricted)

**Compounding vs. Linear Teams:**
- Teams using AI tools for short-term productivity get a linear boost; compounding teams have built entire frameworks around models [PARAPHRASED from search summaries]
- Compounding teams "aren't writing code at all" -- they've built frameworks (like the "Amplifier framework") around a model [PARAPHRASED]

**Technical Architecture of Compounding Teams:**
- Systems have plumbing similar to Claude Code or Codex with callback hooks, tool calling, and flow control [PARAPHRASED]
- Systems are more proactive with strategies, tools, opinions, and behaviors for independent operation [PARAPHRASED]
- Extensive use of low-level programming tools giving the system access to itself: filesystem, git, markdown, Kubernetes, XML [PARAPHRASED]

**Code Review as "Firing Offense":**
- Teams with shipping products have not directly touched code in multiple months [PARAPHRASED]
- One team jokingly considers a code review a "firing offense" because it means you're in the way of the tool [PARAPHRASED -- reported in search results as from this article]

**Bottleneck Shift:**
- These highly productive teams are now overwhelmed with ideas because the new bottleneck is human attention [PARAPHRASED]
- "Productivity was never the real bottleneck. The bottleneck was always coherence." [REPORTED QUOTE -- could not verify exact wording due to paywall]

**Scale:**
- Schillace observed this pattern twice in one week and suspected many more teams finding the same patterns [PARAPHRASED]
- Article published September 28, 2025 [EXACT date from search]

> **Writer note:** The specific quotes "build a tool for making a tool," "5-10 parallel processes," and "hundreds of dollars daily API cost" could not be independently verified from available search results. Writers should verify these against the original Substack post before using as direct quotes.

---

## Source 6: Francesco Bonacci -- "Vibe Coding Paralysis"

**URL:** https://x.com/francedot/status/2017858253439345092
**Date:** Approximately February 2026
**Author:** Francesco Bonacci (@francedot on X, founder of Cua, YC X25)

### Key Quotes (Exact / Verbatim from search results)

**Definition:**
- "Vibe Coding Paralysis: When Infinite Productivity Breaks Your Brain" [EXACT -- post title]
- "the syndrome of wanting to do so much -- and being able to do so much -- that you end up finishing nothing" [EXACT]

**The Paralysis Scenario:**
- "an hour later, you have five worktrees, three half-implemented features running in parallel, and you can't remember what the original task was" [EXACT]

**The Capability Paradox:**
- "the more capability you have, the more you feel compelled to use it. The more you use it, the more fragmented your attention becomes. The more fragmented your attention, the less you actually ship." [EXACT]

**Confidence Erosion:**
- "when Claude Code writes most of the code, a question starts nagging: Do I actually understand what's happening here?" [EXACT]

**Related Phenomena:**
- "The Context Collapse" -- losing track of what each worktree/branch is doing [PARAPHRASED]
- "The Confidence Spiral" -- deepening uncertainty about one's own understanding [PARAPHRASED]
- Prompting becomes "a crutch, then a habit, then an addiction" [EXACT]
- Discusses intentional vs. reactive parallelization as a coping strategy [PARAPHRASED]

---

## Source 7: Dario Amodei -- Davos 2026 on AI Replacing Software Engineers

**URL (primary):** https://fortune.com/2026/01/27/at-davos-ceos-said-ai-isnt-coming-for-jobs-as-fast-as-anthropic-ceo-dario-amodei-thinks/
**URL (secondary):** https://www.entrepreneur.com/business-news/ai-ceo-says-software-engineers-could-be-replaced-in-months/502087
**Date:** January 20-21, 2026 (interview); January 27-30, 2026 (articles)
**Event:** World Economic Forum, Davos
**Interview conducted by:** The Economist

### Key Quotes (Exact / Verbatim)

**On AI replacing software engineers:**
- AI models could do "most, maybe all" of what software engineers currently do within six to twelve months [EXACT]

**On current practice at Anthropic:**
- "I have engineers within Anthropic who say I don't write any code anymore. I just let the model write the code, I edit it" [EXACT]

**On intelligence scaling:**
- "We basically have a Moore's Law for intelligence where the model is getting more and more cognitively capable every few months" [EXACT]

### Additional Context
- Amodei acknowledged uncertainty: some components like chip manufacturing and model training cannot yet be automated [PARAPHRASED]
- Reiterated earlier prediction that by 2026-2027, advanced AI systems could conduct research comparable to Nobel Prize winners [PARAPHRASED]

> **Note:** The existing sources.bib already has an entry `amodei2026_davos` for this source.

---

## Source 8: Daniela Amodei -- Anthropic Hiring Generalists / Humanities

**URL:** https://fortune.com/2026/02/07/anthropic-cofounder-daniela-amodei-humanities-majors-soft-skills-hiring-ai-stem/
**Date:** February 7, 2026
**Author:** Fortune staff

### Key Quotes (Exact / Verbatim)

**On hiring priorities:**
- "When we look to hire people at Anthropic today, we look for people who are great communicators, who have excellent EQ and people skills, who are kind and compassionate and curious and want to help other people." [EXACT]

**On humanities:**
- "I actually think studying the humanities is going to be more important than ever." [EXACT]
- "A lot of these models are actually very good at STEM. But I think this idea that there are things that make us uniquely human -- understanding ourselves, understanding history, understanding what makes us tick -- I think that will always be really, really important." [EXACT]

**On broader implications:**
- "The things that make us human will become much more important instead of much less important." [EXACT]

> **Note:** The specific quote "Not all of the things people learned in the past translate to coding with LLMs" was NOT found in this article. It may be from a different source or may be a paraphrase. Writers should attribute carefully.

---

## Source 9: Science Journal Study -- 29% of GitHub Python Functions AI-Written

**URL:** https://www.science.org/doi/10.1126/science.adz9311
**Secondary coverage:** https://techxplore.com/news/2026-01-ai-software-code.html
**Date:** Published January 22, 2026 in *Science*
**Lead Researcher:** Simone Daniotti (Complexity Science Hub / Utrecht University)
**Title:** "Who is using AI to code? Global diffusion and impact of generative AI"

### Key Data Points (Exact)
- **Methodology:** Neural classifier trained to detect AI-generated Python functions across 30+ million GitHub commits by ~160,000 developers [EXACT]
- **U.S. adoption:** Rose from 5% (2022) to 29% (late 2024 / early 2025) [EXACT]
- **International comparisons:**
  - United States: 29%
  - France: 24%
  - Germany: 23%
  - India: 20%
  - Russia: 15%
  - China: 12%
- **Productivity impact:** 3.6% overall increase in quarterly output (measured in online code contributions) [EXACT]
- **Economic value:** Estimated $23-38 billion in annual economic value for U.S. programming tasks [EXACT]

### Experience-Level Findings (Exact)
- Less experienced programmers use AI in 37% of their code [EXACT]
- Experienced developers use it in 27% of their code [EXACT]
- Productivity gains accrue almost exclusively to experienced developers (6.2% increase in commit rates at 29% adoption) [EXACT]
- No statistically significant productivity effect among inexperienced users [EXACT]
- Key finding: "The technology widens rather than narrows skill-based disparities in the profession" [PARAPHRASED from study conclusions]

---

## Source 10: Claude Code Writes 90% of Its Own Code

**URL (primary):** https://technewsday.com/anthropic-says-ai-now-writes-over-90-of-the-code-behind-claude/
**URL (secondary):** https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/
**Date:** Various, January-February 2026

### Key Quotes and Data (Exact / Verbatim)

**Dario Amodei (CEO):**
- "Within Anthropic and within a number of companies that we work with, that is absolutely true now" (October 2025, confirming the 90% prediction) [EXACT]
- "If Claude is writing 90% of the code, what that means, usually, is you need just as many software engineers. They can focus on the 10% that's editing the code." [EXACT]
- Earlier prediction (March 2025): "I think we'll be there in three to six months -- where AI is writing 90% of the code." [EXACT]
- Previously predicted AI could write "essentially all" code by March 2026 [PARAPHRASED]

**Mike Krieger (Anthropic Labs Chief, speaking at Cisco AI Summit, February 3, 2026):**
- "Claude is now writing Claude" [EXACT]
- "Right now for most products at Anthropic it's effectively 100% just Claude writing, and then what we've done is created all the right scaffolds around it to let us trust it." [EXACT]

**Boris Cherny (Claude Code creator):**
- Every line of code he personally shipped in December 2025 was written by Claude [EXACT -- from late-2025 disclosure]

### Additional Industry Data
- Y Combinator: Quarter of 2025 winter batch founders generate up to 95% of code with AI [EXACT]
- Stanford study: Entry-level software employment dropped nearly 20% since late 2022 [EXACT]
- Cowork feature built in roughly ten days using Claude Code [EXACT]

---

## Source 11: Grok 4.1 Release (for model-releases.csv)

**URL:** https://x.ai/news/grok-4-1
**Model card:** https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf
**Date:** November 17, 2025
**Organization:** xAI

### Key Data Points
- Released November 17, 2025 as the default model for all consumer-facing xAI applications [EXACT]
- LMArena Text Arena: Grok 4.1 Thinking holds #1 overall at 1483 Elo [EXACT]
- Non-reasoning mode: #2 at 1465 Elo [EXACT]
- EQ-Bench: 1586 in Thinking mode (highest) [EXACT]
- Hallucination rate: 4.22% (65% reduction from previous version) [EXACT]
- Three pillars: higher emotional intelligence, lower hallucination, creative capabilities boost [PARAPHRASED]
- Silent A/B rollout November 1-14, 2025; users preferred Grok 4.1 over 4.0 more than 64% of the time [EXACT]

---

## Source 12: Gemini 3 Deep Think (for model-releases.csv)

**URL:** https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/
**Date:** December 4, 2025 (rollout to AI Ultra subscribers)
**Organization:** Google DeepMind

### Key Data Points
- Announced November 18, 2025 alongside Gemini 3 Pro; rolled out December 4, 2025 [EXACT]
- Gold-medal level on International Math Olympiad 2025 [EXACT]
- Gold-medal level on written sections of 2025 International Physics Olympiad and Chemistry Olympiad [EXACT]
- Humanity's Last Exam: 41.0% without tools [EXACT]
- GPQA Diamond: 93.8% [EXACT]
- ARC-AGI-2: 45.1% with code execution [EXACT]
- Available via Gemini app (AI Ultra subscribers) and Gemini API (select researchers/engineers/enterprises) [EXACT]

---

## Additional Cross-Reference Notes for Writers

### Timeline of Key Events (verified dates)
- **Oct 2024:** Claude 3.5 Sonnet revision -- "long-horizon agentic coding workflows began to compound correctness"
- **Dec 2024:** Cursor YOLO mode makes long-horizon coding "unmistakable"
- **Jan 20, 2025:** DeepSeek-R1 released (open-source reasoning)
- **Mar 2025:** Amodei predicts 90% AI code in 3-6 months
- **May 22, 2025:** Claude Opus 4 / Sonnet 4 released
- **Jul 14, 2025:** StrongDM Software Factory founded (3-person team)
- **Aug 7, 2025:** GPT-5 released
- **Sep 28, 2025:** Schillace publishes "compounding teams" essay
- **Nov 17, 2025:** Grok 4.1 released (xAI)
- **Nov 18, 2025:** Gemini 3 released (Google DeepMind)
- **Nov 24, 2025:** Claude Opus 4.5 released (Anthropic)
- **Dec 4, 2025:** Gemini 3 Deep Think rolled out
- **Dec 11, 2025:** GPT-5.2 released (OpenAI)
- **Jan 20-21, 2026:** Amodei at Davos: "6-12 months" prediction
- **Jan 22, 2026:** Science journal: 29% of U.S. Python code AI-written
- **Jan 27, 2026:** Amodei publishes "The Adolescence of Technology"
- **Jan 29, 2026:** Fortune: Cherny/Roon 100% AI-written code article
- **Feb 3, 2026:** Krieger at Cisco AI Summit: "Claude is now writing Claude"
- **Feb 5, 2026:** Claude Opus 4.6 + GPT-5.3-Codex released
- **Feb 7, 2026:** Willison publishes StrongDM software factory analysis
- **Feb 9, 2026:** Matt Shumer publishes "Something Big Is Happening"

### Unverified Quotes (Writers Must Verify)
The following quotes were requested but could not be independently confirmed from available web sources:
1. "build a tool for making a tool" (attributed to Schillace) -- may be in the paywalled Substack
2. "5-10 parallel processes" (attributed to Schillace) -- not found in search results
3. "hundreds of dollars daily API cost" (attributed to Schillace) -- not found; StrongDM uses "$1,000/day per engineer"
4. "Not all of the things people learned in the past translate to coding with LLMs" -- not found as exact quote; may be editorial paraphrase
5. "re-planning replacing actual work" (attributed to Bonacci) -- concept present but exact phrase not confirmed
