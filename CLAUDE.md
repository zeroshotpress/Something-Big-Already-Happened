# Something Big Already Happened

A living, evidence-first narrative tracking how AI predictions convert into
measurable reality — month by month — using primary sources, reproducible data,
and falsifiable scorecards.

## SSOT

**MASTER-PLAN.md is the absolute reference.** Read it before any work.

## Current Status

- Book exists: 14 chapters, ~61K words, deployed to GitHub Pages
- Phase 0 complete: 6 gate scripts created, baseline measured
- Gates: 2/6 PASS (image_dpi, preflight), 4/6 FAIL
- Target: 80-85K words, all 6 gates EXIT 0

## Project Structure

```
/
├── MASTER-PLAN.md               # SSOT — read this first
├── CLAUDE.md                    # This file — agent rules
├── _quarto.yml                  # Quarto project config
├── _quarto-web.yml              # Web profile
├── _quarto-ebook.yml            # EPUB profile
├── _quarto-print-kdp.yml        # Print KDP profile
├── chapters/                    # Chapter .qmd files
├── data/                        # CSV/JSON data files
├── images/
│   ├── generated/               # matplotlib/seaborn charts
│   └── diagrams/                # SVG diagrams
├── references/
│   ├── sources.bib              # Bibliography
│   ├── source-registry.yml      # 2-axis citation manifest
│   └── design-reference.html    # Visual design reference
├── styles/                      # CSS and design system
├── templates/
│   └── print-header.tex         # LaTeX header (microtype, xurl, widow/orphan)
├── scripts/
│   ├── verify_counts.py         # CSV↔prose sync
│   ├── source_audit.py          # 2-axis citation enforcement
│   ├── voice_audit.py           # Banned words + burstiness
│   ├── image_dpi_check.py       # 300 DPI check
│   ├── quote_audit.py           # 25 words/quote, 200 words/source
│   └── preflight_kdp.sh         # KDP file hygiene
├── docs/
│   ├── SSOT.md
│   ├── SOURCE-POLICY.md
│   ├── FORMAT-SPECS.md
│   ├── VOICE-STYLEGUIDE.md
│   └── STORY-BIBLE.md           # Narrative continuity tracker
├── reports/                     # Phase review reports
└── .github/workflows/           # CI/CD
```

## File Ownership Rules (CRITICAL)

Each agent MUST only modify files they own. No exceptions.

| Agent      | Owns                                                          |
|------------|---------------------------------------------------------------|
| Researcher | references/sources.bib, references/source-registry.yml, data/ |
| Editor     | docs/STORY-BIBLE.md, scripts/ (tuning only)                   |
| Writer     | chapters/*.qmd                                                |
| Art Director | images/generated/*, images/diagrams/*                       |
| Visual Designer | styles/*, templates/*, _brand.yml                        |
| Proofreader | chapters/*.qmd (post-Writer review pass only)                |
| Producer   | _quarto*.yml, scripts/preflight_kdp.sh, .github/*, Makefile  |
| Lead       | CLAUDE.md, MASTER-PLAN.md, reports/, final commits            |

## Quality Gates (6 scripts, all must EXIT 0)

1. `python scripts/verify_counts.py` — data↔prose sync
2. `python scripts/source_audit.py` — Tier-3 core claims = 0
3. `python scripts/voice_audit.py` — banned words = 0, burstiness OK
4. `python scripts/image_dpi_check.py` — all images ≥ 300 DPI
5. `python scripts/quote_audit.py` — ≤ 25 words/quote, ≤ 200 words/source
6. `bash scripts/preflight_kdp.sh` — KDP file hygiene

## Anti-Hallucination Protocol (CRITICAL)

1. Adding any person/scene/quote → MUST web search to verify first
2. DO NOT invent names, quotes, or events
3. After every new scene/quote, insert:
   `<!-- PROOF: url=... | accessed=YYYY-MM-DD | key=citation_key -->`
4. If search fails after sufficient attempts:
   Insert `[TODO: HUMAN-RESEARCH-REQUIRED]` and move on
5. Anonymous archetypes OK only with media source + date

## 2-Axis Citation Policy

### Core Claims (gate-enforced)
Anything with: numbers, dates, benchmarks, releases, valuations,
market share, policy/regulation, export controls, employment stats

### Rules
- Core claims → Tier-1 AND (Primary OR Secondary). Tier-3 forbidden.
- Secondary quotes: only those that directly quote the primary source
- source-registry.yml must have: tier, type, scope, paywalled, url, notes

## Quote Hygiene
- Direct quotes: max 25 words each
- Same source total: max 200 words
- Excess → FAIL via quote_audit.py

## Chapter Blueprint (6 steps, all chapters)

1. Cold Open Scene (300-600 words) — person + place + date + sensory detail
2. Claim (1-2 sentences)
3. Evidence (70-75% of chapter)
4. Counterpoint (200-400 words) — "why this might be wrong" + falsification conditions
5. Prediction Scorecard + So-what Tool (300-500 words)
6. Closing Hook (1-2 paragraphs)

## Voice Rules

### Banned Words (voice_audit.py enforces)
delve, moreover, furthermore, it is worth noting, robust, comprehensive,
crucial, landscape, navigate, leverage, multifaceted, tapestry,
serves as a testament, in the ever-evolving, pivotal, underscore,
nuanced, paradigm shift, at the heart of, in an era where, vibrant

### Required
- Burstiness stdev > 8
- Contractions, incomplete sentences
- Expand via scenes/characters/tools, NOT analysis

## Iteration Rules

1. Edit chapters ONE BY ONE (Ch1 → Ch8 first, then Ch3-7, then Ch9-14)
2. After each chapter: update docs/STORY-BIBLE.md
3. Before starting next chapter: read STORY-BIBLE.md
4. Gate fail → read stderr → fix → retry until EXIT 0
5. After each Phase: write reports/REVIEW-REPORT-phaseN.md

## The Confirmation Gap (Narrative Spine)

- Capability inflection: Nov 17 → Dec 11, 2025
- Behavioral proof: Dec 2025 → Jan 2026
- Public confirmation: Feb 5, 2026
- Named in Ch1, deepened in Ch8, resolved in Ch14

## Design Reference

Based on references/design-reference.html:
- Dark premium theme (bg: #0D0D1A, accent: #FF6B35)
- Typography: Playfair Display (headings), Inter (body), JetBrains Mono (code)
- Components: stat cards, timeline, callout boxes, scorecard tables
- Print: grayscale safe, 0.75pt line minimum, no large background fills
