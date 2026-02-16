# QUALITY INSPECTION REPORT v3
## "Something Big Already Happened"
### Inspection Date: 2026-02-13, Post-QA-v2-Fixes

---

## Executive Summary

All **2 Critical** and **3 Significant** issues identified in QA v2 have been successfully fixed. The Ch1 reading guide now accurately describes 14 chapters across 5 parts, the scorecard distribution numbers match Ch14's authoritative table (7/10/6), all 16 figures and 4 tables have inline cross-references, and the November Revolution chart now includes Grok 4.1 with the correct "5 Frontier Models" title.

This v3 inspection found **0 Critical**, **1 Significant**, and **10 Minor** issues. The book is in substantially better shape than at v2 and is approaching publication readiness for the HTML format.

**Overall Quality Score: 9.0 / 10** (up from 8.4)

| Area | Score | Change from v2 |
|------|------:|----------------|
| Content Quality | 9.0/10 | +0.8 |
| Design System Compliance | 8.5/10 | -0.5 (new issue found) |
| Data & Visual Assets | 9.5/10 | +0.5 |
| Build Infrastructure (HTML) | 10/10 | Maintained |
| Build Infrastructure (other formats) | 3/10 | Unchanged |
| CI/CD Pipeline | 8/10 | Unchanged |

**Issues: 0 Critical | 1 Significant | 10 Minor**

---

## 0. v2 Fix Verification

### CRITICAL Issues -- ALL FIXED

| v2 Issue | Status | Evidence |
|----------|--------|----------|
| 2.1 Ch1 Reading Guide (12ch -> 14ch) | **FIXED** | Lines 150-164 now correctly describe 5 parts, 14 chapters with accurate chapter-to-content mapping |
| 2.2 Scorecard Distribution (3/9/7/4 -> 7/10/6) | **FIXED** | Line 122 now reads: "seven were scored at 50% realization or above... Ten were scored between 20% and 49%... Six were scored below 20%" |

### SIGNIFICANT Issues -- ALL FIXED

| v2 Issue | Status | Evidence |
|----------|--------|----------|
| 2.3 Ten Figures with no inline `@fig-` ref | **FIXED** | All 16 figures (14 PNG + 2 SVG) now have corresponding `@fig-` inline references |
| 2.4 Four Tables with no inline `@tbl-` ref | **FIXED** | All 4 tables (`tbl-swebench-scores`, `tbl-metr-horizons`, `tbl-metr-projections`, `tbl-full-scorecard`) now have `@tbl-` inline references |
| 2.5 November Revolution chart missing Grok 4.1 | **FIXED** | `generate_charts.py` line 692: title is "The November Revolution: 5 Frontier Models in 24 Days"; script plots all 5 models including Grok 4.1 (Nov 17) |

---

## 1. Content Analysis: Per-Chapter Summary

| Ch | Title | Words | Citations | Callouts | Figures | Tables | @sec- refs | Score |
|---:|:------|------:|----------:|---------:|--------:|-------:|-----------:|------:|
| 01 | Something Big Is Happening | 4,698 | 40 | 1 | 1 | 0 | 1 | 9/10 |
| 02 | The Chorus of Warnings | 4,329 | 38 | 2 | 1 | 0 | 1 | 9/10 |
| 03 | The Benchmark Revolution | 3,900 | 21 | 2 | 1 | 1 | 1 | 9/10 |
| 04 | The Autonomous Frontier | 3,839 | 14 | 2 | 1 | 2 | 2 | 9/10 |
| 05 | The Model Avalanche | 4,861 | 64 | 1 | 2 | 0 | 3 | 8/10 |
| 06 | The Human Cost | 4,750 | 35 | 2 | 1 | 0 | 3 | 9/10 |
| 07 | The Recursive Loop | 4,767 | 35 | 2 | 2 | 0 | 2 | 9/10 |
| 08 | The November Revolution | 3,912 | 23 | 2 | 1 | 0 | 1 | 9/10 |
| 09 | The Software Factory | 4,141 | 26 | 2 | 2 | 0 | 2 | 9/10 |
| 10 | The Compounding Teams | 4,043 | 24 | 2 | 2 | 0 | 4 | 8/10 |
| 11 | The Investment Tsunami | 3,925 | 15 | 1 | 1 | 0 | 3 | 8/10 |
| 12 | The Geopolitical Chessboard | 4,005 | 9 | 2 | 1 | 0 | 1 | 7/10 |
| 13 | The Science Acceleration | 4,049 | 12 | 1 | 1 | 0 | 3 | 8/10 |
| 14 | What Now? | 4,719 | 21 | 2 | 1 | 1 | 4 | 9/10 |

**Totals: ~59,938 words | 377 citations | 24 callouts | 18 figures | 4 tables | 31 @sec- refs**

*Note: Word counts exclude YAML frontmatter and Quarto structural markup. Citation counts treat each `@key` inside bracket citations individually.*

---

## 2. Issues Found (Priority Order)

### CRITICAL

*None.*

### SIGNIFICANT

#### 2.1 Excessive Verbatim Quote Repetition Across 3--4 Chapters
**Affected:** Ch2, Ch7, Ch9, Ch10
**Problem:** Several key quotes appear verbatim in 3--4 different chapters:

| Quote | Ch2 | Ch7 | Ch9 | Ch10 |
|-------|:---:|:---:|:---:|:----:|
| Boris Cherny "22 PRs in a single day" | line 113 | line 121 | -- | line 63 |
| Cherny "I have never had this much joy" | line 115 | line 123 | -- | line 67 |
| Roon "100%, I don't write code anymore" | line 117 | line 125 | -- | line 77 |
| Krieger "Claude is now writing Claude" | line 101 | line 115 | -- | line 81 |
| Daniela Amodei humanities/hiring quotes | lines 91-93 | -- | line 149 | line 175 |

While some cross-chapter repetition is expected, verbatim duplication of the same extended quotes across 3+ chapters undermines the reading experience and weakens the impact of each quotation. Later chapters should reference the earlier treatment with shorter paraphrases or `@sec-` cross-references rather than repeating the full text.

### MINOR

#### 2.2 Ch12 Low Citation Density (Persists from v2)
**File:** `chapters/12-geopolitical-chessboard.qmd`
**Problem:** Only 9 citations -- the lowest in the book by a wide margin. Other chapters average 27. The entire "Three Scenarios" section and the final ~800 words have zero citations. Several geopolitical claims (China's GPU stockpiling, TSMC market position, EU AI Act enforcement timeline) lack sourcing.

#### 2.3 Rogue Color `#1A1A3E` in components.css (New)
**File:** `styles/components.css`, lines 14 and 123
**Problem:** Two instances of `#1A1A3E` appear in gradient backgrounds (`.hero` and `.stat-card`). This is NOT a defined design token -- it is a near-miss typo for `#1A1A2E` (`--bg-secondary`). The difference is subtle (last byte `3E` vs `2E`) but breaks design token consistency. Likely inherited from `references/design-reference.html`.

#### 2.4 276,000 Layoff Figure Repetition (Persists from v2)
**File:** `chapters/02-voices-of-warning.qmd`, line 80
**Problem:** The full "276,000" figure appears in Ch2 before its primary detailed treatment in Ch6. Could be replaced with "hundreds of thousands" plus a forward reference to `@sec-human-cost`.

#### 2.5 Chart Font Mismatch (Persists from v2)
**File:** `scripts/generate_charts.py`, line 61
**Problem:** `FONT_FAMILY = "DejaVu Sans"` -- charts use DejaVu Sans instead of Inter (body) or JetBrains Mono (data), because Google Fonts are not installed for matplotlib.

#### 2.6 PDF `mainfont` Set to Heading Font (New)
**File:** `_quarto.yml`, line 90
**Problem:** `mainfont: "Playfair Display"` makes the heading font the body font for PDF/LaTeX output. The design system specifies Inter for body text and Playfair Display only for headings. This means PDF/LaTeX builds will use the wrong body font.

#### 2.7 Duplicate Chart in Ch5 and Ch11 (New)
**Files:** `chapters/05-model-avalanche.qmd` line 159, `chapters/11-investment-tsunami.qmd` line 107
**Problem:** Both chapters embed the identical `ai-investment.png` chart with different figure IDs (`#fig-ai-investment` and `#fig-ai-investment-ch11`). Ch11 (Investment Tsunami) is the natural home. Ch5's usage could cross-reference Ch11's figure instead of duplicating it.

#### 2.8 Typst Template Not Quarto-Compatible (Persists from v2)
**File:** `templates/premium.typ`
**Problem:** Still lacks the `#show: doc => ...` entry point Quarto expects. Paper size is A4 (line 30) instead of 6x9 KDP format. Comments were added acknowledging this, but no functional fix. `make pdf-typst` will still fail.

#### 2.9 Missing Editorial Briefs for Ch9--14 (Persists from v2)
**Directory:** `briefs/`
**Problem:** Only `ch01-brief.md` through `ch08-brief.md` exist. Chapters 9--14 have no corresponding brief files.

#### 2.10 CLAUDE.md References Non-Existent File (Persists from v2)
**File:** `CLAUDE.md`, line 14
**Problem:** Project structure lists `chapters/00-introduction.qmd` which does not exist. The book uses `index.qmd` as the landing page.

#### 2.11 `docs/` Directory Potentially Stale (New)
**Problem:** `_quarto.yml` sets `output-dir: _book` and the CI pipeline deploys from `_book`. However, a `docs/` directory exists with a separate HTML build. This may be a stale legacy artifact from an earlier GitHub Pages configuration (deploy from `/docs` branch). If not manually maintained, it will drift from the CI-deployed version.

---

## 3. Cross-Chapter Consistency

### Citation Integrity
- **63 unique citation keys** used across 14 chapters
- **ALL resolve** to entries in `references/sources.bib` (75 total entries)
- **0 broken citations**
- **0 duplicate bib keys**
- **7 unused bib entries**: `claudefast2025`, `llmstats2025`, `medium2024_aidisasters`, `metr2025`, `metr2025_o3`, `metr2025_x`, `swebench2024`, `wef2024_davos`

### Cross-Reference Integrity
- **11 unique `@sec-` cross-references** -- all resolve correctly to defined `{#sec-}` anchors
- **16 unique `@fig-` inline references** -- all resolve correctly
- **4 unique `@tbl-` inline references** -- all resolve correctly
- **0 orphaned figures** (all defined figures are referenced)
- **0 orphaned tables** (all defined tables are referenced)
- **All 16 image file paths** resolve to existing files on disk

### Number Consistency

| Item | Locations | Status |
|------|-----------|--------|
| "twenty-three predictions" | 7 locations across Ch1, Ch7, Ch14 | **PASS** |
| "twenty-eight major models" | 7 locations across Ch1, Ch4, Ch5, Ch6 | **PASS** |
| "79.2%" SWE-bench | 20 locations across 8 chapters | **PASS** |
| "4 hours 49 minutes" METR | 10 locations across 5 chapters | **PASS** (minor format variation: with/without "and") |
| "276,000" layoffs | 5 locations across Ch2, Ch6, Ch14 | **PASS** (one "276,000+" variant in Ch6 line 17) |

### Repetition Rules Compliance

| Rule | Status |
|------|--------|
| "instrumental in creating itself" only in Ch7 | **PASS** |
| 79.2% detailed analysis only in Ch3 | **PASS** |
| 276,000 detailed analysis only in Ch6 | **PARTIAL** -- full number in Ch2 line 80 before Ch6 primary treatment |
| Verbatim quote deduplication | **FAIL** -- 5 quotes repeated across 3-4 chapters (see Issue 2.1) |

### November Thesis Coverage

| Required Chapter | Present | Quality |
|-----------------|---------|---------|
| Ch1 | Yes | Full section `{#sec-november-precedent}` |
| Ch5 | Yes | Full section `{#sec-model-november-cluster}` |
| Ch7 | Yes | Section "The November Acceleration" |
| Ch8 | Yes | **Entire chapter** dedicated to thesis |
| Ch14 | Yes | Section `{#sec-living-thesis}` |

**Assessment: PASS** -- November thesis effectively threaded throughout.

---

## 4. Data & Visual Assets

### CSV Data Files

| File | Rows | Expected | Status |
|------|-----:|----------|--------|
| prediction-scorecard.csv | 23 | 23 | **PASS** -- realization % range 10--95%, all reasonable |
| model-releases.csv | 28 | 28 | **PASS** -- Grok 4.1 and Gemini 3 Deep Think present |
| swe-bench.csv | 25 | 25+ | **PASS** -- 79.2% for Opus 4.5 confirmed |
| metr-benchmarks.csv | 22 | 20+ | **PASS** -- progression 0.03h to projected 32h |
| ai-timeline.csv | 61 | 50+ | **PASS** -- comprehensive Jan 2024 to Feb 2026 |

### Generated Charts (14 pairs)

| # | Chart | PNG | PDF | Referenced By |
|---|-------|-----|-----|--------------|
| 1 | swe-bench-timeline | 246 KB | 31 KB | Ch3 |
| 2 | metr-exponential | 181 KB | 31 KB | Ch4 |
| 3 | model-releases-timeline | 147 KB | 27 KB | Ch5 |
| 4 | prediction-scorecard | 554 KB | 33 KB | Ch1, Ch14 |
| 5 | job-displacement | 180 KB | 27 KB | Ch6 |
| 6 | ai-investment | 207 KB | 28 KB | Ch5, Ch11 |
| 7 | ai-timeline | 847 KB | 52 KB | Ch2 |
| 8 | recursive-loop | 340 KB | 39 KB | Ch7 |
| 9 | november-revolution-timeline | 135 KB | 27 KB | Ch8 |
| 10 | five-levels | 197 KB | 28 KB | Ch9 |
| 11 | ai-code-percentage | 177 KB | 27 KB | Ch10 |
| 12 | compounding-vs-linear | 204 KB | 27 KB | Ch10 |
| 13 | geopolitical-approaches | 410 KB | 27 KB | Ch12 |
| 14 | science-acceleration | 199 KB | 30 KB | Ch13 |

- All 14 PNG + 14 PDF files present. No broken files (all > 10 KB).
- **Orphaned images: 0** | **Missing images: 0**
- **November Revolution chart now includes 5 models (Grok 4.1 added)**

### SVG Diagrams (2)

| Diagram | Size | Design System Colors | Referenced By |
|---------|------|---------------------|--------------|
| ai-recursive-loop.svg | 81 lines | **PASS** (7 of 9 tokens used) | Ch7 |
| software-factory-architecture.svg | 133 lines | **PASS** (all 9 tokens used) | Ch9 |

### Bibliography
- **75 entries** in `references/sources.bib`
- **63 entries cited** by chapters (was 67 in v2 -- difference due to stricter counting methodology)
- **7 unused** entries (retained as background references)
- **0 duplicate keys** | **0 broken citations**

---

## 5. Design & Build Infrastructure

### Design System Compliance: 8.5/10

- **8 of 9 color tokens** consistent across CLAUDE.md, theme.css, _brand.yml, premium.typ
- **Deduction:** `components.css` uses rogue `#1A1A3E` in 2 gradient declarations (lines 14, 123) -- near-miss typo for `#1A1A2E` (`--bg-secondary`)
- **Deduction:** Chart fonts use DejaVu Sans instead of Inter
- All 3 font families (Playfair Display, Inter, JetBrains Mono) consistent across main config files
- All 9 required components implemented in `components.css`

### Required Components Coverage

| Component | Status |
|-----------|--------|
| Hero sections with gradient overlays | **PRESENT** (lines 10-91) |
| Stat cards (3-column grid, gradient bg, top accent border) | **PRESENT** (lines 115-170) |
| Timeline (vertical, left-aligned, glowing dots) | **PRESENT** (lines 176-253) |
| Blockquotes (card bg, left accent border) | **PRESENT** (lines 259-306) |
| Callout boxes (gradient bg, colored border) | **PRESENT** (lines 312-447) |
| Scorecard tables (custom styled, status badges) | **PRESENT** (lines 514-580) |
| Chart containers (dark bg, labeled, captioned) | **PRESENT** (lines 453-485) |
| Code blocks (darker bg, syntax coloring) | **PRESENT** (lines 586-633) |
| Chapter navigation | **PRESENT** (lines 639-726) |

### Build Status

| Format | Status | Notes |
|--------|--------|-------|
| HTML | **BUILT** | All 14 chapters rendered, search index, all assets |
| GitHub Pages | **DEPLOYED** | CI deploys from `_book`; legacy `docs/` may be stale |
| EPUB | Not built | Configured but never executed |
| PDF/LaTeX | Not built | Configured; `mainfont` set to Playfair Display (wrong) |
| PDF/Typst | **Will fail** | Template lacks Quarto entry point; paper is A4 not 6x9 |

### CI/CD Pipeline: 8/10
- Trigger: push to main + manual dispatch
- Steps: checkout -> Quarto setup -> Python setup -> pip install -> chart generation -> render HTML -> deploy
- Proper permissions, concurrency group, and Quarto/Python caching
- **Missing:** pip dependency caching for faster builds

---

## 6. Comparison: v2 vs v3

| Metric | v2 (Pre-Fix) | v3 (Post-Fix) | Change |
|--------|-------------:|:-------------:|--------|
| Overall Score | 8.4/10 | **9.0/10** | **+0.6** |
| Critical Issues | 2 | **0** | **-2** |
| Significant Issues | 3 | **1** | **-2** |
| Minor Issues | 6 | **10** | +4 (deeper inspection) |
| Figure cross-refs | 8 of 18 | **18 of 18** | **+10** |
| Table cross-refs | 0 of 4 | **4 of 4** | **+4** |
| Ch1 Reading Guide | Wrong (12ch) | **Correct (14ch)** | **Fixed** |
| Scorecard Distribution | Wrong (3/9/7/4) | **Correct (7/10/6)** | **Fixed** |
| Nov Revolution Chart | 4 models | **5 models** | **Fixed** |
| Broken citations | 0 | 0 | Maintained |
| Broken cross-refs | 0 | 0 | Maintained |
| Missing images | 0 | 0 | Maintained |

---

## 7. Recommended Fix Priority

### Must Fix Before Publication
1. **Deduplicate verbatim quotes** across Ch2, Ch7, Ch9, Ch10 -- use paraphrases or `@sec-` cross-references in later chapters

### Should Fix
2. Increase Ch12 citation density (add 10--15 citations for geopolitical claims)
3. Fix rogue `#1A1A3E` -> `#1A1A2E` in `styles/components.css` (lines 14, 123)
4. Fix `_quarto.yml` PDF `mainfont` from Playfair Display to Inter (line 90)
5. Replace verbatim "276,000" in Ch2 line 80 with vaguer reference + `@sec-human-cost`

### Nice to Have
6. Fix Typst template for Quarto compatibility (add entry point, change paper to 6x9)
7. Remove or update stale `docs/` directory
8. Create editorial briefs for Ch9--14
9. Install Inter font for matplotlib or accept DejaVu Sans as chart font
10. Update CLAUDE.md to remove `00-introduction.qmd` reference
11. Deduplicate `ai-investment.png` usage -- Ch5 should cross-reference Ch11's figure

---

*Report generated: 2026-02-13*
*Previous report archived to: `archive/REVIEW-REPORT-v2.md`*
