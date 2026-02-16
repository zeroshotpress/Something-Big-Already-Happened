# Something Big Already Happened -- Book Outline

## Narrative Arc

The book follows a three-act structure: **Prediction, Evidence, Reckoning**.

**Act I -- The Predictions (Chapters 1-2)** opens in the white heat of February 2026, when Matt Shumer's essay goes viral, then pulls back to show that for years a growing chorus of CEOs, researchers, and engineers had been warning the world. The reader should feel the mounting urgency of voices shouting into the wind.

**Act II -- The Evidence (Chapters 3-6)** turns the camera on the data. Each chapter takes one axis of AI progress -- coding benchmarks, autonomous task duration, model releases, and the human consequences -- and shows, with charts and primary sources, how the predictions became reality faster than almost anyone expected.

**Act III -- The Reckoning (Chapters 7-8)** confronts what comes next: the recursive self-improvement loop that is now operational, and the societal choices that remain. The final chapter synthesizes the evidence and frames the questions humanity must answer.

The emotional arc moves from alarm to evidence to urgency. The reader begins with a gut feeling that something big is happening, is shown proof that something big *already happened*, and finishes facing the question: What do we do now?

---

## Chapter Summaries

### Chapter 1: "Something Big Is Happening"
Matt Shumer's February 9, 2026 essay serves as the book's inciting event. Viewed more than 20 million times in its first week, it crystallized a feeling that had been building for months: the AI revolution was not coming -- it was here. This chapter unpacks his core claims (nothing done on a computer is safe; AI is bigger than Covid; a century of medical research compressed into a decade) and lays out the prediction scorecard the rest of the book will track.

### Chapter 2: "The Chorus of Warnings"
Before Shumer's essay went viral, a remarkable convergence of voices had already sounded the alarm. Dario Amodei warned of 50% entry-level job losses within 1-5 years, Sam Altman predicted AGI during Trump's term, Demis Hassabis gave transformative AGI a 50% chance by 2030. This chapter traces the timeline of CEO predictions from Davos 2024 through Davos 2026, showing how the warnings escalated in both specificity and urgency.

### Chapter 3: "The Benchmark Revolution"
SWE-bench Verified became the yardstick of AI coding capability. In January 2024, GPT-4 with RAG scored 2.7%. By February 2026, the best models exceeded 79%. This chapter follows the benchmark's exponential ascent month by month, explaining what each leap meant in practical terms -- from fixing trivial bugs to autonomously resolving complex, multi-file engineering problems.

### Chapter 4: "The Autonomous Frontier"
METR's research on AI task completion time horizons revealed the most striking exponential in all of AI: autonomous task duration was doubling every seven months, possibly accelerating to every four months. From two minutes in 2019 to nearly five hours by late 2025, this chapter charts the curve that implies AI will sustain day-long autonomous work by 2027 and week-long work by 2028.

### Chapter 5: "The Model Avalanche"
Between March 2024 and February 2026, at least 27 frontier models were released by five major labs. The pace was not just fast -- it was accelerating. This chapter catalogs the avalanche: Claude 3 through Opus 4.6, GPT-4o through GPT-5.3-Codex, Gemini 1.5 through Gemini 3, DeepSeek-V3 and R1, and Meta's Llama 3.1. It shows how each release pushed the frontier and compressed the timeline between breakthroughs.

### Chapter 6: "The Human Cost"
The numbers are already grim: 276,000+ tech layoffs in 2024-2025, 55,000 job cuts directly attributed to AI in 2025, worker concern about AI job loss rising from 28% to 40%. Meanwhile, 5 million white-collar jobs identified as facing extinction. This chapter grounds the abstract in the personal, tracing how the model avalanche and benchmark revolution translated into real unemployment, policy upheaval, and trillion-dollar market shifts.

### Chapter 7: "The Recursive Loop"
On February 5, 2026, OpenAI released GPT-5.3-Codex -- the first model "instrumental in creating itself." It debugged its own training, managed its own deployment, and diagnosed its own evaluations. Amodei had predicted AI would be 1-2 years from autonomously building the next generation. It arrived ahead of schedule. This chapter examines the recursive self-improvement loop, Amodei's "Adolescence of Technology" essay, and the concept of a "country of geniuses in a datacenter."

### Chapter 8: "What Now?"
The evidence is in. The predictions came true faster than expected. The recursive loop is operational. So what now? This chapter synthesizes the data from all prior chapters, assesses which predictions remain unfulfilled, and examines the policy landscape (EU AI Act, Trump's deregulation, state-level AI laws). It closes with the questions that will define the next five years: How do we manage the transition? Who benefits? And can we steer a technology that is beginning to steer itself?

---

## Key Data Points by Chapter

| Chapter | Required Data |
|---------|--------------|
| Ch 1 | Shumer essay metrics (20M+ views); core claims scorecard; Feb 2026 market reaction ($1T+ selloff) |
| Ch 2 | Full prediction-scorecard.csv; timeline of CEO statements (2024-2026); Davos 2024 vs 2026 contrast |
| Ch 3 | Complete swe-bench.csv progression (2.7% to 79.2%); SWE-bench Verified introduction; model-by-model scores |
| Ch 4 | Complete metr-benchmarks.csv (2min to ~5hrs); doubling time (7 months, accelerating to 4); projections to 2027 |
| Ch 5 | Full model-releases.csv (27 models, 5 labs); context window evolution (128K to 1M); price drops; capability jumps |
| Ch 6 | Layoff numbers (276K+, 55K AI-cited); unemployment rise to 4.4%; worker concern 28% to 40%; software stock crash; $500B+ investment vs job losses |
| Ch 7 | GPT-5.3-Codex self-improvement; Amodei "Adolescence" essay; 90% AI-written code at Anthropic; recursive loop evidence |
| Ch 8 | Prediction realization rates across scorecard; EU AI Act timeline; policy divergence (EU vs US); remaining unfulfilled predictions |

---

## Cross-Reference Map

```
Ch1 (Shumer Essay)
 +-- references --> Ch2 (CEO predictions Shumer cited)
 +-- claims tested in --> Ch3 (coding benchmarks)
 +-- claims tested in --> Ch4 (autonomous AI)
 +-- claims tested in --> Ch6 (human cost)

Ch2 (CEO Warnings)
 +-- predictions verified by --> Ch3 (Amodei's "90% code" claim)
 +-- predictions verified by --> Ch4 (METR data Hassabis cited)
 +-- predictions verified by --> Ch5 (model release pace)
 +-- predictions verified by --> Ch6 (Amodei's 50% job loss warning)
 +-- predictions verified by --> Ch7 (Amodei's recursive AI prediction)

Ch3 (SWE-bench)
 +-- driven by models in --> Ch5 (model releases)
 +-- implications for --> Ch6 (job displacement in coding)
 +-- enables --> Ch7 (AI writing AI code)

Ch4 (METR Autonomy)
 +-- measured models from --> Ch5 (model releases)
 +-- implications for --> Ch6 (autonomous work replacing humans)
 +-- enables --> Ch7 (recursive improvement requires autonomy)

Ch5 (Model Releases)
 +-- powers benchmarks in --> Ch3 (SWE-bench scores)
 +-- powers autonomy in --> Ch4 (METR time horizons)
 +-- drives layoffs in --> Ch6 (human cost)
 +-- culminates in --> Ch7 (GPT-5.3-Codex self-improving)

Ch6 (Human Cost)
 +-- caused by --> Ch3, Ch4, Ch5 (capability gains)
 +-- demands response in --> Ch8 (policy and action)

Ch7 (Recursive Loop)
 +-- builds on --> Ch3, Ch4, Ch5 (all capability evidence)
 +-- raises stakes for --> Ch8 (what now?)

Ch8 (What Now?)
 +-- synthesizes --> All prior chapters
 +-- evaluates --> Ch2 predictions (scorecard final tally)
 +-- proposes --> Framework for navigating what comes next
```

---

## Structural Notes

- **Word count targets**: ~2,000-3,000 words per chapter; ~18,000-24,000 words total
- **Every chapter** must include at least one chart or data visualization
- **Every factual claim** must cite a source from sources.bib
- **Tone**: Authoritative but accessible -- longform journalism, not academic paper
- **Timestamps**: All claims and data points must be anchored to specific dates
- **Recurring motif**: The gap between public perception and documented reality
