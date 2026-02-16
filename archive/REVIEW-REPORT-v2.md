# QUALITY INSPECTION REPORT v2
## "Something Big Already Happened"
### Inspection Date: 2026-02-13, Post-Expansion

---

## Executive Summary

The book has been expanded from **8 chapters / 18,061 words** to **14 chapters / 61,020 words** across 5 parts. The expansion introduced 6 new chapters, 6 new charts, 2 SVG diagrams, 12 new bibliography sources, and the "November Revolution" thesis. HTML build is fully functional and deployed.

**Overall Quality Score: 8.4 / 10** (up from previous assessment)

| Area | Score | Change |
|------|------:|--------|
| Content Quality | 8.2/10 | New assessment |
| Design System Compliance | 9/10 | Maintained |
| Data & Visual Assets | 9/10 | New assessment |
| Build Infrastructure (HTML) | 10/10 | Maintained |
| Build Infrastructure (other formats) | 3/10 | Known limitation |
| CI/CD Pipeline | 8/10 | Improved |

**Critical issues found: 2 | Significant: 3 | Minor: 6**

---

## 1. Content Analysis: Per-Chapter Summary

| Ch | Title | Words | Citations | Callouts | Figures | Score | Key Issues |
|----|-------|------:|----------:|---------:|--------:|------:|:-----------|
| 01 | The Prediction | 4,722 | 42 | 1 | 1 | 7/10 | Reading guide wrong (12 ch, not 14); scorecard distribution mismatch |
| 02 | Voices of Warning | 4,442 | 40 | 2 | 1 | 9/10 | 276K figure before Ch6 primary treatment |
| 03 | Benchmark Revolution | 4,049 | 23 | 2 | 1 | 9/10 | Clean |
| 04 | Autonomous Frontier | 3,994 | 17 | 2 | 1 | 9/10 | Clean |
| 05 | Model Avalanche | 4,937 | 69 | 1 | 2 | 9/10 | Clean |
| 06 | Human Cost | 4,809 | 38 | 2 | 1 | 8/10 | Figure not cross-referenced inline |
| 07 | Recursive Loop | 4,800 | 38 | 2 | 2 | 9/10 | Clean |
| 08 | November Revolution | 3,967 | 24 | 2 | 1 | 9/10 | Figure not cross-referenced inline |
| 09 | Software Factory | 4,175 | 28 | 2 | 2 | 9/10 | 2 figures not cross-referenced |
| 10 | Compounding Teams | 4,078 | 28 | 2 | 2 | 8/10 | 2 figures not cross-referenced |
| 11 | Investment Tsunami | 3,984 | 18 | 1 | 1 | 8/10 | Figure not cross-referenced; 1 callout only |
| 12 | Geopolitical Chessboard | 4,052 | 10 | 2 | 1 | 7/10 | **Lowest citation density** (10); figure not cross-referenced |
| 13 | Science Acceleration | 4,109 | 15 | 1 | 1 | 8/10 | Figure not cross-referenced |
| 14 | What Now? | 4,902 | 26 | 2 | 1 | 8/10 | Scorecard distribution mismatch with Ch1 |

**Totals: 61,020 words | 456 citations | 25 callouts | 18 figure references**

---

## 2. Issues Found (Priority Order)

### CRITICAL

#### 2.1 Ch1 Reading Guide Describes Wrong Chapter Structure
**File:** `chapters/01-the-prediction.qmd`, Section `{#sec-reading-guide}`
**Problem:** The reading guide describes a **12-chapter** book but the actual book has **14 chapters**. From Part III onward, every chapter description points to the wrong chapter:

| Reading Guide Says | Actual Chapter |
|---|---|
| Part III Ch6-8: "The Transformation" | Part III Ch7-10: "The Inflection" |
| Ch8 = "StrongDM's dark software factory" | Ch8 = November Revolution |
| Part IV Ch9 = "policy landscape, EU AI Act" | Ch9 = Software Factory |
| Part IV Ch10 = "market response, selloff" | Ch10 = Compounding Teams |
| Part V Ch11 = "predictions confirmed" | Ch11 = Investment Tsunami |
| Part V Ch12 = "living through transition" | Ch12 = Geopolitical Chessboard |
| Ch13, Ch14 = not mentioned | Ch13 = Science Acceleration, Ch14 = What Now? |

**Fix required:** Rewrite the reading guide to describe the correct 5-part, 14-chapter structure.

#### 2.2 Scorecard Distribution Mismatch Between Ch1 and Ch14
**File:** `chapters/01-the-prediction.qmd`, line ~122
**Problem:** Ch1 states the scorecard distribution as:
- "three scored at 50% or above" -- **actual: seven**
- "nine scored between 20% and 49%" -- **actual: ten**
- "seven scored below 20%" -- **actual: six**
- "four on track relative to timeline" -- **actual: zero** (no such category in Ch14)

Ch14's scorecard table is authoritative (23 rows with specific percentages). Ch1's summary must be updated to match.

### SIGNIFICANT

#### 2.3 Ten Figures Defined But Never Cross-Referenced Inline
**Affected chapters:** Ch6, Ch7, Ch8, Ch9, Ch10, Ch11, Ch12, Ch13
**Problem:** These chapters define figures with `{#fig-...}` labels but never reference them via `@fig-...` in the running text. Without inline references, Quarto will not generate numbered figure references, and readers cannot be directed to specific figures.

| Chapter | Unreferenced Figure |
|---------|-------------------|
| Ch6 | `{#fig-job-displacement}` |
| Ch7 | `{#fig-recursive-loop-diagram}` |
| Ch8 | `{#fig-november-revolution}` |
| Ch9 | `{#fig-five-levels}`, `{#fig-software-factory-arch}` |
| Ch10 | `{#fig-ai-code-pct}`, `{#fig-compounding-linear}` |
| Ch11 | `{#fig-ai-investment-ch11}` |
| Ch12 | `{#fig-geopolitical-approaches}` |
| Ch13 | `{#fig-science-acceleration}` |

**Fix required:** Add at least one `@fig-...` reference in the text near each figure.

#### 2.4 Four Tables Defined But Never Cross-Referenced
**Problem:** `{#tbl-swebench-scores}` (Ch3), `{#tbl-metr-horizons}` (Ch4), `{#tbl-metr-projections}` (Ch4), `{#tbl-full-scorecard}` (Ch14) are defined but never referenced via `@tbl-...`.

#### 2.5 November Revolution Chart Title Mismatch
**File:** `images/generated/november-revolution-timeline.png`
**Problem:** The chart title says "4 Frontier Models in 24 Days" but the chapter text in Ch8 says "five frontier models in 24 days." The chart only plots 4 events (Gemini 3, Opus 4.5, Deep Think, GPT-5.2) but is missing Grok 4.1 (Nov 17) which the chapter counts as the fifth.

### MINOR

#### 2.6 Ch12 Low Citation Density
Ch12 (Geopolitical Chessboard) has only 10 citations -- the lowest in the book. Several geopolitical claims about China's AI ecosystem, export controls, and TSMC's market share lack citations. Other chapters average 33 citations.

#### 2.7 276,000 Layoff Figure Repetition
The full "276,000" figure appears in Ch2 (line 80) before its primary treatment in Ch6. Consider replacing with "hundreds of thousands" in Ch2 with a forward reference to `@sec-human-cost`.

#### 2.8 Chart Font Mismatch
`scripts/generate_charts.py` uses `"DejaVu Sans"` as the font family (line 61) because Google Fonts (Inter, Playfair Display) are not installed for matplotlib. Chart text fonts do not match document fonts.

#### 2.9 Typst Template Not Quarto-Compatible
`templates/premium.typ` lacks the `#show: doc => ...` entry point Quarto expects. Also sets paper to A4 instead of 6x9 KDP format. `make pdf-typst` will fail.

#### 2.10 Missing Editorial Briefs for New Chapters
Only `briefs/ch01-brief.md` through `ch08-brief.md` exist. Chapters 9-14 have no corresponding brief files.

#### 2.11 CLAUDE.md References Non-Existent File
CLAUDE.md project structure lists `chapters/00-introduction.qmd` which does not exist. The book uses `index.qmd` as the landing page instead.

---

## 3. Cross-Chapter Consistency

### Citation Integrity
- **67 unique citation keys** used across 14 chapters
- **ALL resolve** to entries in `references/sources.bib` (75 total entries, 8 unused)
- **No broken citations anywhere**
- **No duplicate bib keys**

### Cross-Reference Integrity
- **11 unique `@sec-` references** -- all resolve correctly
- **8 unique `@fig-` inline references** -- all resolve correctly
- **10 defined figures** never referenced inline (see Issue 2.3)
- **4 defined tables** never referenced inline (see Issue 2.4)
- **All 16 image file paths** resolve to existing files on disk

### Number Consistency
| Item | Expected | Status |
|------|----------|--------|
| "twenty-three predictions" | Consistent across Ch1, Ch7, Ch14 | PASS |
| "twenty-eight major models" | Consistent across Ch1, Ch4, Ch5, Ch6 | PASS |
| "79.2%" SWE-bench | 21 occurrences across 7 chapters | PASS |
| "4 hours 49 minutes" METR | Consistent across Ch1, Ch4, Ch5, Ch8 | PASS |

### Repetition Rules Compliance
| Rule | Status |
|------|--------|
| "instrumental in creating itself" only in Ch7 | PASS -- only in Ch7 line 9 |
| 79.2% detailed analysis only in Ch3 | PASS -- brief references elsewhere |
| 276,000 detailed analysis only in Ch6 | PARTIAL -- full number also in Ch2 and Ch14 |

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
| prediction-scorecard.csv | 23 | 23 | PASS -- all realization percentages match chapter text |
| model-releases.csv | 28 | 28 | PASS -- Grok 4.1 and Gemini 3 Deep Think present |
| swe-bench.csv | 25 | 25+ | PASS -- key scores match Ch3 table |
| metr-benchmarks.csv | 21 | 20+ | PASS -- data matches Ch4 |
| ai-timeline.csv | 60 | 50+ | PASS -- all key events present |

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
| 9 | november-revolution-timeline | 122 KB | 26 KB | Ch8 |
| 10 | five-levels | 197 KB | 28 KB | Ch9 |
| 11 | ai-code-percentage | 177 KB | 27 KB | Ch10 |
| 12 | compounding-vs-linear | 204 KB | 27 KB | Ch10 |
| 13 | geopolitical-approaches | 410 KB | 27 KB | Ch12 |
| 14 | science-acceleration | 199 KB | 30 KB | Ch13 |

- All 14 PNG + 14 PDF files present. No broken files (all > 10 KB).
- **Orphaned images: 0** | **Missing images: 0**

### SVG Diagrams (2)

| Diagram | Size | Design System Colors | Referenced By |
|---------|------|---------------------|--------------|
| ai-recursive-loop.svg | 81 lines | PASS (#0D0D1A, #FF6B35, #6366F1) | Ch7 |
| software-factory-architecture.svg | 133 lines | PASS (all 9 tokens) | Ch9 |

### Bibliography
- **75 entries** in `references/sources.bib`
- **12 new sources** added in this expansion (all verified present)
- **0 duplicate keys**
- **67 entries used** by chapters, 8 unused reference entries

---

## 5. Design & Build Infrastructure

### Design System Compliance: 9/10
- All 9 color tokens match across CLAUDE.md, theme.css, _brand.yml, premium.typ
- All 3 font families (Playfair Display, Inter, JetBrains Mono) consistent
- All required components implemented (hero, stat cards, timeline, blockquotes, callouts, scorecard, chart containers, code blocks, chapter nav)
- **Deduction:** Chart font mismatch (DejaVu Sans vs Inter in matplotlib)

### Build Status

| Format | Status | Notes |
|--------|--------|-------|
| HTML | **BUILT** | All 14 chapters rendered, search index, all assets |
| GitHub Pages | **DEPLOYED** | docs/ directory complete with .nojekyll |
| EPUB | Not built | Configured but never executed |
| PDF/LaTeX | Not built | Configured but never executed |
| PDF/Typst | **Will fail** | Template lacks Quarto entry point |

### CI/CD Pipeline: 8/10
- Trigger: push to main + manual dispatch
- Steps: checkout -> Quarto setup -> Python setup -> pip install -> chart generation -> render HTML -> deploy
- Proper permissions and concurrency group
- **Missing:** pip caching for faster builds

---

## 6. Comparison: v1 vs v2

| Metric | v1 (Pre-Expansion) | v2 (Post-Expansion) | Change |
|--------|-------------------:|--------------------:|--------|
| Chapters | 8 | 14 | +75% |
| Total words | 18,061 | 61,020 | +238% |
| Avg words/chapter | 2,258 | 4,358 | +93% |
| Total citations | ~120 | 456 | +280% |
| Callout boxes | ~12 | 25 | +108% |
| Figure references | 8 | 18 | +125% |
| Charts (PNG+PDF) | 16 | 28 | +75% |
| SVG diagrams | 0 | 2 | New |
| Bibliography entries | ~50 | 75 | +50% |
| CSV data rows | ~157 | ~157 | Same |
| Parts | 3 | 5 | +67% |
| New thesis (November) | None | 5 chapters | New |

---

## 7. Recommended Fix Priority

### Must Fix Before Publication
1. **Rewrite Ch1 reading guide** to describe correct 14-chapter, 5-part structure
2. **Fix Ch1 scorecard distribution** numbers to match Ch14 table (7/10/6, not 3/9/7/4)
3. **Add inline figure cross-references** (`@fig-...`) for all 10 unreferenced figures

### Should Fix
4. Fix November Revolution chart to include Grok 4.1 and update title to "5 Frontier Models"
5. Add inline table cross-references (`@tbl-...`) for 4 unreferenced tables
6. Increase Ch12 citation density (add sources for geopolitical claims)

### Nice to Have
7. Replace "276,000" in Ch2 with vaguer reference
8. Create editorial briefs for Ch9-14
9. Fix Typst template for Quarto compatibility
10. Add pip caching to CI/CD
11. Update CLAUDE.md to remove 00-introduction.qmd reference
