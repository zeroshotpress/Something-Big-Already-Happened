# STORY-BIBLE.md
## Last updated: Phase 2 — Voice/pattern cleanup + micro-quotes (2026-02-14)

> Load this file BEFORE starting work on any chapter.
> Update it AFTER completing each chapter edit.

---

## Ch1 — Something Big Is Happening
- Characters: Matt Shumer (OthersideAI/HyperWrite CEO, Syracuse grad, essay author — used Claude to write it); Alexis Ohanian (Reddit co-founder, endorsed essay); David Haber (a16z GP, highlighted practical implications); Gary Marcus (NYU emeritus, "weaponized hype" critic); Jeremy Kahn (Fortune AI editor, "no compilers for law"); Vishal Misra (Columbia vice dean, "camera didn't kill painting"); Todd McLees (HumanSkills.AI, "floodwaters and a bucket")
- Key quotes: "this seems overblown phase of something much bigger than Covid"; "The future is already here"; "It did help a lot, and I think that's kind of the point" (Shumer on using Claude); "We are now confident we know how to build AGI" (Altman, altman2024_reflections)
- Blueprint: Cold Open (Shumer + Claude scene) ✓ | Claim ✓ | Evidence ✓ | Counterpoint ("The Case Against" — Marcus, Kahn, Misra + 3 falsification conditions) ✓ | Scorecard ✓ | Closing Hook ✓
- New framework: **The Confirmation Gap** explicitly named and defined in §sec-confirmation-gap. Three phases: capability inflection (Nov), behavioral proof (Dec-Jan), public confirmation (Feb).
- Closing hook: Who were the people making these predictions → leads to Ch2
- Unresolved: None

## Ch2 — Voices of Warning
- Characters: Dario Amodei (Anthropic CEO, Davos predictions); Demis Hassabis (DeepMind CEO, Nobel laureate, 50% AGI by 2030); Sam Altman (OpenAI CEO, AGI during Trump's term); Jensen Huang (NVIDIA CEO, "insatiable demand"); Daniela Amodei (Anthropic co-founder, hiring generalists); Mike Krieger (Anthropic CPO, co-founder Instagram, "Claude writing Claude"); Boris Cherny (Anthropic, 22 PRs/day); Roon (OpenAI, 100% AI code); Matt Shumer
- Blueprint: Cold Open (Amodei vs Hassabis at Davos) ✓ | Claim ✓ | Evidence ✓ | Counterpoint ("The Incentive Problem" — financial interests, Marcus critique, timing skepticism + falsification) ✓ | Scorecard ("The Prediction Convergence" table) ✓ | Closing Hook (meta-irony: Shumer used Claude, discourse shaped by beneficiaries) ✓
- Key thread: Historical parallel to atomic scientists' warnings (Oppenheimer, Fermi)
- Micro-quote: Musk "There's a 10% to 20% chance that it goes bad" (musk2024_fii)
- Closing hook: From predictions to evidence → Ch3

## Ch3 — Benchmark Revolution
- Characters: (Primarily data-driven; references to organizations: Epoch AI, SWE-bench maintainers)
- Blueprint: Cold Open ✓ | Claim ✓ | Evidence (SWE-bench progression 2.7% → 79.2%) ✓ | Counterpoint ("The Benchmark's Blind Spots") ✓ | Scorecard ("The Benchmark Assessment Tool" table) ✓ | Closing Hook (→ Ch4 autonomy) ✓
- Key data: 79.2% SWE-bench Verified (Claude Opus 4.5); 29% of Python on GitHub AI-written; experience gap finding
- Micro-quote: Pichai "the most profound technology humanity is ever working on" (pichai2025_bbc)
- Training pipeline concern: AI eliminating the apprenticeship that creates senior engineers

## Ch4 — Autonomous Frontier
- Characters: Beth Barnes (METR founder, ex-OpenAI); Paul Christiano (ARC founder); Birgitta Boeckeler (ThoughtWorks)
- Blueprint: Cold Open (Barnes checking Dec 2025 METR data: 4hr 49min) ✓ | Claim ✓ | Evidence (METR exponential curve) ✓ | Counterpoint ("When Autonomy Fails" — METR RCT: 19% slower; ThoughtWorks enterprise failures + 3 falsification conditions) ✓ | Scorecard ("Autonomy Scorecard" table) ✓ | Closing Hook (→ Ch5 model releases) ✓
- Key data: 2 min (2019) → 4hr 49min (Dec 2025); METR RCT: developers 19% slower with AI but believed 20% faster
- Micro-quote: Barnes "I am an expert telling you you should freak out" (barnes2025_80k)
- Endurance vs accuracy distinction: tool → agent threshold

## Ch5 — Model Avalanche
- Characters: (Model release chronology; references to xAI, Google DeepMind, Anthropic, OpenAI)
- Blueprint: Cold Open ✓ | Claim ✓ | Evidence (28 major model releases) ✓ | Counterpoint ("The Diminishing Returns Question" + "The Model Shelf Life") ✓ | Scorecard ("Practitioner's Tool: When to Switch Models") ✓ | Closing Hook ✓
- Key data: November Cluster documented; Gemini 3 Deep Think IMO gold; GPT-5.2 variants
- Micro-quote: LeCun "LLMs are useful, but they are an off ramp" (lecun2024_offramp)

## Ch6 — Human Cost
- Characters: (Industry-wide; layoff data; hiring paradox participants)
- Blueprint: Cold Open ✓ | Claim ✓ | Evidence (55,000 AI-cited layoffs) ✓ | Counterpoint ("The Other Side of Displacement" + "Falsification Conditions") ✓ | Scorecard (implicit in data tables) ✓ | Closing Hook ✓
- Key data: Amazon 14,000 cuts; Salesforce 4,000 support cuts; hiring paradox (senior roles growing while junior roles shrink)
- Micro-quote: D. Amodei "humanity is about to be handed almost unimaginable power" (amodei2026)

## Ch7 — Recursive Loop
- Characters: Mike Krieger (Claude writing Claude); Dario Amodei ("country of geniuses in a datacenter")
- Blueprint: Cold Open ✓ | Claim ✓ | Evidence (GPT-5.3-Codex self-improvement, Claude-on-Claude) ✓ | Counterpoint ("The Limits of Recursion") ✓ | Scorecard ("Recursive Improvement Scorecard" table) ✓ | Closing Hook ✓
- Micro-quote: Altman "We are beginning to turn our aim beyond that, to superintelligence" (altman2024_reflections)
- Confirmation Gap thread: recursive loop is the mechanism that widens the gap

## Ch8 — November Revolution
- Characters: Anonymous Google DeepMind researcher (opening — LMArena); Yoshua Bengio (AI Safety Report); Stuart Russell (UC Berkeley, FLI Safety Index)
- Blueprint: Cold Open (DeepMind researcher + LMArena leaderboard moment) ✓ | Claim ✓ | Evidence ✓ | Counterpoint ("The Case for Skepticism" — SWE-bench limits, FLI Safety Index, Bengio report + 3 falsification conditions) ✓ | Scorecard ("November by the Numbers" table + "What Changed in Practice" section) ✓ | Closing Hook (→ Ch9 software factory) ✓
- Micro-quote: Russell "You can't fetch the coffee if you're dead" (russell2019_humancompatible)
- Confirmation Gap: §sec-confirmation-gap-ch8 deepened — information asymmetry with economic consequences; three-month early-adopter advantage
- Key addition: "What Changed in Practice" — engineering teams experimenting, bottleneck shift from implementation to specification

## Ch9 — Software Factory
- Characters: Justin McCarthy (StrongDM CTO, 20+ year veteran, ex-CTO Rafter, co-inventor textbook rental); Jay Taylor; Navan Chauhan; Simon Willison (analyst); Dan Shapiro (Five Levels framework); Francesco Bonacci (vibe coding paralysis)
- Blueprint: Cold Open (McCarthy's background + founding moment July 14, 2025) ✓ | Claim ✓ | Evidence (StrongDM manifesto, Attractor, DTU, Five Levels) ✓ | Counterpoint ("When the Factory Breaks" — vibe coding paralysis, technical debt, verification paradox + falsification) ✓ | Scorecard ("The Factory Scorecard" Level 0-5 table) ✓ | Closing Hook (→ Ch10 compounding teams) ✓
- Key addition: Historical parallel (assembly → high-level languages); broader implications for law, medicine, accounting
- Micro-quote: McCarthy "Code must not be written by humans" (strongdm2026_factory)
- Token economics: $1,000/day/engineer = 200-300 invocations

## Ch10 — Compounding Teams
- Characters: Sam Schillace (Microsoft Deputy CTO, Google Docs creator); Boris Cherny (22 PRs/day); Roon; Mike Krieger; Francesco Bonacci; Daniela Amodei
- Blueprint: Cold Open (Schillace September 2025 Substack post) ✓ | Claim ✓ | Evidence (linear vs compounding, experience paradox from Science study) ✓ | Counterpoint ("The Compounding Illusion" — survivorship bias, knowledge concentration + falsification) ✓ | Scorecard ("The Compounding Assessment Tool" table) ✓ | Closing Hook (→ Ch11 investment) ✓
- Key additions: "Team-of-Five Phenomenon" (YC batch data); statistical argument for automated testing; senior engineer psychological transition; programming as "bottleneck masquerading as a skill"
- Micro-quote: Schillace "The teams that are compounding aren't writing code at all" (schillace2025_compounding)
- Science study: 29% Python AI-written; experienced devs +6.2% productivity, inexperienced no gain

## Ch11 — Investment Tsunami
- Characters: Sam Altman; Masayoshi Son; Donald Trump (Stargate announcement); Jensen Huang
- Blueprint: Cold Open (Stargate Project announcement, Jan 21, 2025) ✓ | Claim ✓ | Evidence (funding rounds, infrastructure buildout) ✓ | Counterpoint (dot-com comparison + DeepSeek paradox + bubble analysis + falsification) ✓ | Scorecard ("The Bubble Scorecard" table) ✓ | Closing Hook (→ Ch12 geopolitics) ✓
- Key additions: NVIDIA crash scene ($589B single day, largest in history); "The Nuclear Bet" section (Three Mile Island, Amazon nuclear, Google SMR); energy/climate tension; railroad analogy extended; investor psychology (consensus trade)
- Micro-quote: Huang "Trillions of dollars of AI infrastructure needs to be built" (huang2026_davos)
- New source: cnbc2025_nvidia_crash

## Ch12 — Geopolitical Chessboard
- Characters: Gina Raimondo (Commerce Secretary, Reagan National Defense Forum Dec 2023 — cold open); Dario Amodei (Davos); Demis Hassabis (Davos); Jensen Huang ("insatiable demand"); Donald Trump (EO revoking Biden AI framework)
- Blueprint: Cold Open (Raimondo at Reagan Library, "We cannot let China get these chips") ✓ | Claim ✓ | Evidence (US/EU/China approaches, export controls, TSMC) ✓ | Counterpoint ("The Case for Multipolarity" — Bruegel analysis, 4 falsification tests) ✓ | Scorecard ("The Geopolitical Scorecard" table) ✓ | Closing Hook (→ Ch13 science) ✓
- Key additions: Raimondo cold open scene (Phase 5); historical parallel (telegraph/railroad/internet as geopolitical forces); collision tangible (rare earth retaliation, compliance asymmetry); Davos Huang appearance; California regulatory arbitrage; Taiwan closing paragraph
- Micro-quote: Raimondo "We cannot let China get these chips. Period" (fortune2023_raimondo_chips)
- Three scenarios: US dominance, EU trust, Chinese leapfrog

## Ch13 — Science Acceleration
- Characters: Demis Hassabis (Nobel laureate Oct 2024, phone call from Stockholm — now cold open); Dario Amodei (Nobel-level AI research in ~2 years); John Jumper (AlphaFold co-creator); David Baker (protein design Nobel co-recipient)
- Blueprint: Cold Open (Hassabis Nobel phone call from Stockholm, Oct 9 2024) ✓ | Claim ✓ | Evidence (AlphaFold, drug discovery, math, materials) ✓ | Counterpoint ("The Physical Bottleneck" — 90% trial failure rate, reproducibility crisis + falsification) ✓ | Scorecard ("The Acceleration Scorecard" 7-domain table) ✓ | Closing Hook (→ Ch14 what now) ✓
- Key additions: Hassabis Nobel scene moved to cold open (Phase 5); drug pipeline attrition math (0.02% → 0.32% even with AI doubling); historical tool analogy (telescope, microscope); deep expertise as quality control; math capability trajectory (2020 algebra → 2025 IMO gold)
- Micro-quote: Bengio "I've reoriented my research to try to make AI safe by design" (bengio2025_time)
- Fixed: "navigate" → "live in" (banned word)

## Ch14 — What Now
- Characters: Matt Shumer (bookend cold open — watching essay go viral, Feb 9 2026, New York desk); references to all major figures
- Blueprint: Cold Open (Shumer watching "Something Big Is Happening" go viral, 50M+ views, bookend with Ch1) ✓ | Scorecard (full prediction scorecard) ✓ | Case for Caution ✓ | Living Thesis (Confirmation Gap as narrative spine) ✓ | What Would Change My Mind (6 specific falsification conditions) ✓ | Closing ✓
- Key additions: "What Would Change My Mind" section (§sec-what-would-change-my-mind) with 6 time-bound conditions; confirmation gap as through-line across all chapters; accountability mechanism ("too many prophets, too few accountants")
- Micro-quote: Zuckerberg "Open source is necessary for a positive AI future" (zuckerberg2024_opensource)
- Confirmation Gap: resolved — the gap is real, persistent, growing; each chapter manifests it differently

---

## Cross-Chapter Threads
- **The Confirmation Gap**: Ch1 (named, §sec-confirmation-gap) → Ch8 (deepened, §sec-confirmation-gap-ch8) → Ch14 (resolved, §sec-living-thesis)
- **Recursive improvement**: Ch1 (GPT-5.3-Codex) → Ch7 (theory + evidence) → Ch9 (practice)
- **Job displacement**: Ch2 (warnings) → Ch6 (human stories) → Ch14 (what now)
- **METR doubling**: Ch4 (data + exponential) → Ch8 (November jump) → Ch13 (projection)
- **SWE-bench climb**: Ch3 (history, 2.7% → 79.2%) → Ch8 (79.2% significance) → Ch9 (implications)
- **Investment/bubble**: Ch11 (data) → Ch12 (geopolitics) → Ch14 (falsification test)
- **Counterpoint/falsification**: Every chapter now has counterpoint section + specific falsification conditions
- **Compounding pattern**: Ch9 (software factory) → Ch10 (compounding teams) → Ch11 (investment justification)

## Named Characters Registry
| Name | Role | First Appears | Source |
|------|------|--------------|--------|
| Matt Shumer | OthersideAI/HyperWrite CEO, essay author | Ch1 | shumer2026 |
| Alexis Ohanian | Reddit co-founder | Ch1 | fortune2026_reactions |
| David Haber | a16z General Partner | Ch1 | fortune2026_reactions |
| Gary Marcus | NYU emeritus professor, AI skeptic | Ch1 | marcus2026_shumer |
| Jeremy Kahn | Fortune AI editor | Ch1 | kahn2026_flawed |
| Vishal Misra | Columbia University Vice Dean | Ch1 | fortune2026_reactions |
| Todd McLees | HumanSkills.AI founder | Ch1 | fortune2026_reactions |
| Dario Amodei | Anthropic CEO | Ch1, Ch2 | amodei2026 |
| Sam Altman | OpenAI CEO | Ch1, Ch2 | altman2024 |
| Demis Hassabis | DeepMind CEO, Nobel laureate | Ch1, Ch2, Ch13 | hassabis2025 |
| Jensen Huang | NVIDIA CEO | Ch2, Ch11, Ch12 | huang2025 |
| Daniela Amodei | Anthropic co-founder | Ch2, Ch10 | damodei2026_generalists |
| Mike Krieger | Anthropic CPO, Instagram co-founder | Ch2, Ch7, Ch10 | krieger2026_claudewritesclaude |
| Boris Cherny | Claude Code head, Anthropic | Ch2, Ch10 | cherny2026_aicode |
| Roon | OpenAI researcher (pseudonymous) | Ch2, Ch10 | cherny2026_aicode |
| Beth Barnes | METR founder | Ch4 | metr2025_timehorizons |
| Dan Shapiro | Glowforge CEO, Five Levels framework | Ch9 | shapiro2026_fivelevels |
| Justin McCarthy | StrongDM CTO, software factory founder | Ch9 | strongdm2026_factory |
| Simon Willison | Software analyst | Ch9 | willison2026_softwarefactory |
| Francesco Bonacci | Cua founder, vibe coding paralysis | Ch9, Ch10 | bonacci2026_vibeparalysis |
| Sam Schillace | Microsoft Deputy CTO, Google Docs creator | Ch10 | schillace2025_compounding |
| Masayoshi Son | SoftBank CEO | Ch11 | openai2025_stargate |
| Yoshua Bengio | International AI Safety Report lead | Ch8 | bengio2025_safety |
| John Jumper | DeepMind, AlphaFold co-creator | Ch13 | hassabis2025 |
| David Baker | UW, protein design Nobel co-recipient | Ch13 | hassabis2025 |
| Gina Raimondo | U.S. Commerce Secretary, chip export controls | Ch12 | fortune2023_raimondo_chips |
| Elon Musk | xAI/Tesla CEO, AI risk assessor | Ch2 | musk2024_fii |
| Sundar Pichai | Google CEO | Ch3 | pichai2025_bbc |
| Yann LeCun | Meta Chief AI Scientist, Turing Award | Ch5 | lecun2024_offramp |
| Stuart Russell | UC Berkeley professor, AI safety author | Ch8 | russell2019_humancompatible |
| Mark Zuckerberg | Meta CEO, open-source AI advocate | Ch14 | zuckerberg2024_opensource |
