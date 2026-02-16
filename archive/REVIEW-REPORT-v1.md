# QUALITY REVIEW REPORT

**Project:** *Something Big Already Happened*
**Date:** 2026-02-13
**Scope:** Full project quality inspection (no modifications made)
**Reviewers:** Content Analysis, Design Analysis, Data/Visual/Infrastructure Analysis

---

## 1. CONTENT ANALYSIS

### 1.1 Chapter-by-Chapter Summary

| Chapter | Words | Unique Cites | Blockquotes | Figures | Tables | Callouts |
|:--------|------:|:------------:|:-----------:|:-------:|:------:|:--------:|
| Index | 376 | 0 | 0 | 0 | 0 | 2 |
| Ch1: The Prediction | 2,162 | 14 | 0 | 1 | 0 | 1 |
| Ch2: Voices of Warning | 2,399 | 17 | 0 | 1 | 1 | 2 |
| Ch3: Benchmark Revolution | 2,148 | 10 | 0 | 1 | 1 | 2 |
| Ch4: Autonomous Frontier | 2,184 | 6 | 0 | 1 | 2 | 2 |
| Ch5: Model Avalanche | 2,192 | 24 | 0 | 2 | 0 | 1 |
| Ch6: Human Cost | 1,996 | 10 | 0 | 1 | 0 | 2 |
| Ch7: Recursive Loop | 2,040 | 5 | 1 | 1 | 0 | 2 |
| Ch8: What Now? | 2,564 | 5 | 0 | 1 | 1 | 2 |
| **TOTALS** | **18,061** | **~52 unique** | **1** | **10** | **5** | **14** |

### 1.2 Key Findings

- **Citation density is uneven.** Ch5 has 24 unique keys while Ch7 has only 5. The chapters making the biggest claims (recursive loop, societal impact) tend to have the fewest citations.
- **Direct quotes are almost absent.** Only 1 blockquote across 8 chapters. For a book about what powerful people *said*, this is a significant missed opportunity.
- **Ch6 is the shortest chapter (1,996 words)** despite covering the most consequential topic for most readers (human cost / job displacement). It needs more depth on human experience, international comparisons, and tabular presentation of layoff data.
- **Ch8 is the longest chapter (2,564 words)**, which is appropriate for the synthesis chapter.
- **No `00-introduction.qmd` exists** despite being listed in CLAUDE.md project structure. A methodological introduction would strengthen the book's credibility.

### 1.3 Shumer Essay Claim Coverage

| # | Shumer Core Claim | Primary Chapter(s) | Adequacy |
|--:|:---|:---|:---|
| 1 | Nothing on a computer is safe (medium-term) | Ch1, Ch3 (SWE-bench evidence) | Strong |
| 2 | AI is bigger than Covid in societal impact | Ch1, Ch6 (human cost) | Adequate |
| 3 | AI can compress century of medical research to decade | Ch1, Ch7 (scientific acceleration) | **Moderate -- thin on specific evidence** |
| 4 | Recursive AI self-improvement is happening now | Ch1, Ch7 (dedicated chapter) | Strong |
| 5 | Gap between expert understanding and public awareness | Ch1, Ch2 (convergence section) | Strong |
| 6 | Job displacement will accelerate sharply | Ch1, Ch6 (dedicated chapter) | Strong |
| 7 | Traditional software businesses face existential threat | Ch1, Ch6 (stock crash) | Adequate |

**Verdict:** All 7 core claims addressed. Claim 3 (medical research compression) is the weakest -- only a few paragraphs without specific citations beyond AlphaFold.

### 1.4 Story Flow Evaluation

**Part I (Chapters 1--2): The Predictions** -- Effective. Ch1 is event-driven (what happened Feb 5-9, 2026). Ch2 is character-driven (who said what). The two complement each other without redundancy.

**Part II (Chapters 3--6): The Evidence** -- Strong structure. Each chapter addresses a distinct dimension: coding benchmarks, autonomous duration, model releases, and human impact. Logical progression from narrow technical measurement to broad societal consequence.

**Part III (Chapters 7--8): Synthesis** -- Appropriate scope. Ch7's six-step practical loop description is one of the best passages in the book. Ch8's three-tier scorecard analysis is clean and intellectually honest.

### 1.5 Gaps

1. **Counterarguments.** No chapter dedicates substantial space to the case that projections are wrong or overstated. Skeptical voices (Davos pushback, Stanford HAI's more measured tone, historical job creation patterns) are acknowledged but not explored.
2. **Medical/scientific acceleration.** Shumer's claim about compressing medical research tracked at 10% but receives only cursory treatment in Ch7.
3. **International dimension.** The geopolitical angle (DeepSeek, China, export controls) appears briefly in Ch5 and Ch6 but is not given sustained treatment.
4. **Safety/alignment.** Covered in Ch4 and Ch7, but not as a standalone thread despite Amodei's emphasis on existential risk.

### 1.6 Redundancies

Key data points repeated too many times across chapters:

| Data Point | Appearances | Primary Chapter |
|:-----------|:-----------:|:----------------|
| "276,000 tech layoffs" / "55,000 AI-cited" | Ch1, Ch2, Ch6, Ch8 | Ch6 |
| "79.2% SWE-bench" | Ch1, Ch2, Ch3, Ch5, Ch8 | Ch3 |
| "instrumental in creating itself" (verbatim) | Ch1, Ch3, Ch4, Ch5, Ch7, Ch8 | Ch7 |

The redundancy is partially by design (self-contained chapters), but creates a repetitive reading experience for someone reading straight through.

### CONTENT SCORE: 7.5 / 10

---

## 2. DESIGN ANALYSIS

### 2.1 CSS File Inventory

| File | Lines | Purpose |
|:-----|------:|:--------|
| `styles/theme.css` | 549 | Design tokens, global reset, base typography, Quarto overrides, responsive breakpoints |
| `styles/components.css` | 1,083 | Hero, stat cards, timeline, blockquote, callouts (8 variants), scorecard table, code blocks, chapter nav, comparison cards, prediction tracker, sidebar notes, drop cap, key figure, section dividers |
| `styles/print.css` | 587 | Light theme override, KDP 6x9 page setup, component print adaptations, font embedding declarations |
| **Total** | **2,219** | |

All 3 CSS files are correctly referenced in `_quarto.yml` (lines 46-48) in the correct load order.

### 2.2 `_brand.yml` Verification

| Category | Result |
|:---------|:-------|
| Color palette completeness | **19/19 colors mapped** -- all match CSS custom properties exactly |
| Typography definitions | **Fully defined** -- Playfair Display, Inter, JetBrains Mono with correct weights |
| Placeholder/dummy values | **None** -- all values are production-ready |
| Semantic token mappings | Bootstrap and Shiny defaults included |

### 2.3 Design Reference Fidelity

Comparison of `references/design-reference.html` against CSS implementation:

| Component | Status | Notes |
|:----------|:-------|:------|
| Hero section | IDENTICAL | CSS adds `::after` bottom fade-out (improvement) |
| Hero h1 gradient text | IDENTICAL | |
| Stat grid / stat cards | IDENTICAL | CSS adds shadow on hover (enhancement) |
| Timeline (vertical, glowing dots) | IDENTICAL | Highlight variant improved to class-based |
| Blockquote | ENHANCED | CSS adds decorative open-quote character |
| Callouts | SIGNIFICANTLY ENHANCED | 8 variants + Quarto integration (reference had 1) |
| Chart container | IDENTICAL | |
| Scorecard table + status badges | ENHANCED | 5 badge variants (reference had 3) |
| Code blocks | MINOR DIFFERENCE | Background #0A0A1A vs reference #0f0f23 |
| Chapter navigation | ENHANCED | Adds Quarto `.page-navigation` override |
| Responsive breakpoints | SIGNIFICANTLY ENHANCED | 3 breakpoints (reference had 1) |
| Accessibility | ENHANCED | `prefers-reduced-motion`, `:focus-visible` added |

**Components in CSS not in reference (8 additions):** lead paragraph, comparison cards, prediction tracker cards, sidebar notes, key figure, drop cap, section divider, figure caption decorator.

### 2.4 Typst Template (`templates/premium.typ`)

- **Lines:** 440
- **Color match:** 15/15 colors match CSS exactly (5 less-used colors omitted -- acceptable)
- **Font match:** All 3 font families match with correct fallbacks
- **Components:** 11 of 13 required components implemented

| Missing Component | Impact |
|:------------------|:-------|
| Comparison cards | Medium -- used in CSS but not Typst |
| Prediction tracker cards | Medium -- used in CSS but not Typst |

- **Page setup:** A4 paper (intentional for "premium edition"), proper recto/verso alternation, dark background

### 2.5 Issues Found

1. **PDF/LaTeX font mismatch.** `_quarto.yml` `pdf` format uses Linux Libertine O / Linux Biolinum O / DejaVu Sans Mono instead of design system fonts (Playfair Display / Inter / JetBrains Mono). Breaks design system for one of four build targets.
2. **Quarto theme conflict risk.** Loading Quarto's `darkly` Bootstrap theme underneath custom CSS may cause cascade conflicts. A `none` base theme with full custom override would be safer.
3. **Hero-label font size.** Reference uses 13px; CSS uses `--text-xs` (~11-12px). Minor.
4. **Code block background.** Reference #0f0f23 vs CSS #0A0A1A. Minor.

### DESIGN SCORE: 8.5 / 10

---

## 3. VISUAL ANALYSIS

### 3.1 Image Inventory

| # | Filename | PNG | PDF | PNG Size |
|--:|:---------|:---:|:---:|:--------:|
| 1 | swe-bench-timeline | Yes | Yes | 241K |
| 2 | metr-exponential | Yes | Yes | 178K |
| 3 | model-releases-timeline | Yes | Yes | 139K |
| 4 | prediction-scorecard | Yes | Yes | 542K |
| 5 | job-displacement | Yes | Yes | 176K |
| 6 | ai-investment | Yes | Yes | 203K |
| 7 | ai-timeline | Yes | Yes | 828K |
| 8 | recursive-loop | Yes | Yes | 331K |

**Total:** 8 charts x 2 formats = 16 files. ~2.9 MB total.

### 3.2 Chapter-Image Mapping

| Chapter | Image Referenced |
|:--------|:----------------|
| Ch1 | `prediction-scorecard.png` |
| Ch2 | `ai-timeline.png` (labeled `@fig-timeline-predictions`) |
| Ch3 | `swe-bench-timeline.png` |
| Ch4 | `metr-exponential.png` |
| Ch5 | `model-releases-timeline.png`, `ai-investment.png` |
| Ch6 | `job-displacement.png` |
| Ch7 | `recursive-loop.png` |
| Ch8 | `prediction-scorecard.png` |

- **Orphan images (on disk but not referenced):** None
- **Missing images (referenced but not on disk):** None
- **Dual references:** `prediction-scorecard.png` used in Ch1 and Ch8 (appropriate -- intro vs. final scorecard)

### 3.3 Chart Generation Script

`scripts/generate_charts.py` defines 8 chart functions matching exactly the 8 images on disk. Uses consistent dark theme matching design system tokens. Saves at 300 DPI with dual PNG + PDF output.

### 3.4 Issues Found

1. `images/diagrams/` directory mentioned in CLAUDE.md does not exist. No SVG diagrams have been created.
2. No cover image or hero image for the landing page / EPUB.

### VISUAL SCORE: 8 / 10

---

## 4. DATA ANALYSIS

### 4.1 CSV File Summary

| File | Rows | Columns | Empty Cells |
|:-----|-----:|--------:|:-----------:|
| `prediction-scorecard.csv` | 23 | 10 | None |
| `metr-benchmarks.csv` | 21 | 5 | None |
| `swe-bench.csv` | 25 | 5 | None |
| `model-releases.csv` | 26 | 8 | None |
| `ai-timeline.csv` | 60 | 6 | None |

### 4.2 Cross-Reference Verification

| Check | CSV Value | Chapter Text | Match? |
|:------|:----------|:-------------|:------:|
| SWE-bench top score | 79.2% | "79.2%" (Ch1, 2, 3, 5, 6, 8) | YES |
| METR Opus 4.5 time | 4.82 hrs | "4 hours 49 minutes" (4h 49m 12s) | YES |
| Prediction count | 23 rows | "twenty-three" (Ch1, 7, 8) | YES |
| Tech layoffs | 276,000 | "276,000" (Ch1, 2, 6, 8) | YES |
| **Model releases** | **26 rows** | **"twenty-eight" (Ch4, 5, 6)** | **NO** |

### 4.3 Critical Discrepancy

**Model releases count: text says "twenty-eight" but CSV has 26 rows.**

This discrepancy appears in at least 5 locations:
- `chapters/04-autonomous-frontier.qmd`
- `chapters/05-model-avalanche.qmd` (description, body text, and figure caption)
- `chapters/06-human-cost.qmd`

The chart generated from the 26-row CSV shows 26 data points, but its caption says "28 major models." Either 2 models are missing from the CSV, or the text should say "twenty-six."

### DATA SCORE: 7 / 10

---

## 5. INFRASTRUCTURE ANALYSIS

### 5.1 Build Targets

| Target | Configured in `_quarto.yml` | Makefile Target | Status |
|:-------|:---------------------------:|:---------------:|:------:|
| HTML | Yes | `make html` | Working |
| EPUB | Yes | `make epub` | Configured |
| PDF (LaTeX) | Yes | `make pdf-latex` | Configured |
| **PDF (Typst)** | **No** | `make pdf-typst` | **Will fail** |

### 5.2 CI/CD Pipeline

- **Trigger:** Push to `main` + manual dispatch
- **Build:** HTML only (appropriate for GitHub Pages)
- **Deployment:** GitHub Pages via `actions/deploy-pages@v4`
- **Caching:** `_freeze` and `.quarto` directories

**Missing from CI:**
- No Python step for chart generation (assumes pre-generated images committed)
- No system font installation step
- No EPUB/PDF builds (design choice, but means those formats are only tested locally)

### 5.3 KDP Preflight Script

`scripts/preflight_kdp.sh` checks: PDF existence/size, page dimensions (6x9 with 5pt tolerance), image DPI (300 minimum), font embedding. Well-written with proper error handling.

**Missing:** Page count limits, file size limits (KDP 650MB cap), bleed/trim validation.

### 5.4 Bibliography

- `references/sources.bib`: 48 entries, well-organized by section, all have URL fields
- `references/chicago-author-date.csl`: Present and referenced in `_quarto.yml`

### INFRASTRUCTURE SCORE: 7 / 10

---

## 6. BUG LIST

### Critical (must fix before publication)

| # | Category | Description | Location |
|--:|:---------|:------------|:---------|
| 1 | Data | Model releases count: text says "twenty-eight" but CSV has 26 rows | `chapters/05-model-avalanche.qmd` (lines 3, 9, 68, 70), `chapters/04-autonomous-frontier.qmd`, `chapters/06-human-cost.qmd` |

### High Priority

| # | Category | Description | Location |
|--:|:---------|:------------|:---------|
| 2 | Infrastructure | Typst format not defined in `_quarto.yml` -- `make pdf-typst` will fail | `_quarto.yml` |
| 3 | Content | Only 1 direct blockquote across 8 chapters -- underserves the book's premise of tracking what powerful people said | All chapters |
| 4 | Content | Ch6 (Human Cost) is the shortest chapter (1,996 words) for the most consequential topic | `chapters/06-human-cost.qmd` |

### Medium Priority

| # | Category | Description | Location |
|--:|:---------|:------------|:---------|
| 5 | Content | No counterarguments section -- book does not address why projections might be wrong | Absent |
| 6 | Content | Ch7 has lowest citation density (5 unique keys) despite making the book's biggest claim | `chapters/07-recursive-loop.qmd` |
| 7 | Design | PDF/LaTeX uses Linux Libertine fonts instead of design system fonts (Playfair Display/Inter/JetBrains Mono) | `_quarto.yml` lines 75-77 |
| 8 | Design | Typst template missing 2 components (comparison cards, prediction tracker) | `templates/premium.typ` |
| 9 | Infrastructure | CI/CD has no chart generation step | `.github/workflows/deploy.yml` |
| 10 | Content | Medical research compression claim (Shumer core claim #3) under-evidenced | `chapters/07-recursive-loop.qmd` |

### Low Priority

| # | Category | Description | Location |
|--:|:---------|:------------|:---------|
| 11 | Design | Code block background color: CSS #0A0A1A vs reference #0f0f23 | `styles/theme.css` |
| 12 | Design | Hero-label font size: CSS ~11-12px vs reference 13px | `styles/theme.css` |
| 13 | Design | Quarto `darkly` base theme may conflict with custom CSS | `_quarto.yml` line 38 |
| 14 | Visual | `images/diagrams/` directory does not exist (mentioned in CLAUDE.md) | Project structure |
| 15 | Content | `00-introduction.qmd` listed in CLAUDE.md but does not exist | Project structure |
| 16 | Content | Key data points repeated verbatim across 4-6 chapters (layoffs, SWE-bench, self-improvement quote) | Multiple chapters |

---

## 7. OVERALL EVALUATION

### Score Summary

| Category | Score | Weight | Weighted |
|:---------|------:|:------:|:--------:|
| Content | 7.5 | 30% | 2.25 |
| Design | 8.5 | 20% | 1.70 |
| Visual Assets | 8.0 | 15% | 1.20 |
| Data Quality | 7.0 | 15% | 1.05 |
| Infrastructure | 7.0 | 20% | 1.40 |
| **OVERALL** | | | **7.6 / 10** |

### Strengths

1. **Strong three-part structure.** Predictions -> Evidence -> Synthesis is clean and effective.
2. **Genuinely data-driven.** 52 unique citation keys, 5 tables, 10 figures, 48-entry bibliography.
3. **Design system excellence.** Near-pixel-perfect CSS implementation of reference design, comprehensive component library (20+ components), production-quality print stylesheet.
4. **Intellectual honesty.** Callout boxes consistently acknowledge limitations. Realization percentages are conservative rather than sensationalist.
5. **Dual-format charts.** All 8 charts available in PNG + PDF with no orphans.
6. **Living document design.** The scorecard methodology and open-source approach make the "living document" promise credible.

### Weaknesses

1. **Critical data discrepancy.** Model releases count (26 in CSV vs 28 in text) must be resolved.
2. **Typst build target broken.** No format definition in `_quarto.yml`.
3. **Direct quotes almost absent.** Only 1 blockquote undermines the book's voice-tracking premise.
4. **Uneven chapter depth.** Ch6 (Human Cost) is too short for its topic weight; Ch7 (Recursive Loop) is under-cited for its claim weight.
5. **No counterarguments.** The book does not adequately address why projections might be wrong.
6. **Cross-chapter repetition.** Key data points appear verbatim in too many chapters.

### Top 7 Recommendations (Priority Order)

1. **Fix model releases count.** Add 2 missing models to CSV or change "twenty-eight" to "twenty-six" in all affected chapters.
2. **Add Typst format to `_quarto.yml`.** Reference `templates/premium.typ` or remove `pdf-typst` Makefile target.
3. **Add direct quotes.** At minimum, Ch1, Ch2, Ch5, and Ch7 should include verbatim quotes from Shumer, Amodei, Altman, Hassabis, and Huang.
4. **Expand Ch6 (Human Cost).** Add 500-800 words covering deeper human stories, international comparison of displacement, and a layoff data table.
5. **Add a counterarguments section.** Either as a dedicated section in Ch8 or as a new short chapter between Ch7 and Ch8.
6. **Strengthen citations in Ch7 and Ch8.** These synthesis chapters make strong claims with the fewest citations.
7. **Add chart generation step to CI/CD and Makefile.**

---

*Report generated by automated quality review. No project files were modified during this analysis.*
