# QUALITY INSPECTION REPORT v4
## "Something Big Already Happened"
### Inspection Date: 2026-02-13, Post-QA-v3-Fixes

---

## Executive Summary

The v3 report's **1 Significant** issue (verbatim quote repetition) has been **largely fixed** -- 4 of 5 flagged quotes now properly paraphrase in later chapters with `@sec-` cross-references. Ch12's citation density has been **dramatically improved** from 9 to 32 citations (28 unique, 86% Tier 1--2). PDF chapter numbering is **correct** (1--14 across 5 parts). Ch6's three human profiles are all backed by **Tier-1 sources**.

However, this deeper inspection uncovered **3 new Significant issues**: a prediction realization score contradiction (70% vs 35%) between chapters, inconsistent titles for Mike Krieger across three chapters, and a `repo-url` pointing to a nonexistent GitHub organization. These are data integrity and consistency problems that should be resolved before publication.

**Overall Quality Score: 8.8 / 10** (down from 9.0 -- new data integrity issues offset improvements)

| Area | Score | Change from v3 |
|------|------:|----------------|
| Content Quality | 8.5/10 | -0.5 (new data inconsistencies found) |
| Source Quality | 9.5/10 | +1.0 (Ch12 dramatically improved) |
| Data & Visual Assets | 9.0/10 | -0.5 (scorecard CSV vs text mismatch) |
| Build Infrastructure (HTML) | 9.5/10 | -0.5 (repo-url wrong) |
| Build Infrastructure (other) | 3.5/10 | +0.5 (PDF renders correctly now) |
| CI/CD Pipeline | 8/10 | Unchanged |

**Issues: 0 Critical | 3 Significant | 13 Minor**

---

## 0. v3 Fix Verification

### SIGNIFICANT Issues

| v3 Issue | Status | Evidence |
|----------|--------|----------|
| 2.1 Verbatim quote repetition (5 quotes across Ch2/7/9/10) | **MOSTLY FIXED** | 4/5 quotes fully resolved. Ch7/Ch9/Ch10 now use paraphrases + `@sec-voices-of-warning` cross-refs. Daniela Amodei quotes still verbatim in Ch6 (see Minor 2.7) |

### v3 Minor Issues -- Status Check

| v3 Issue | Status |
|----------|--------|
| 2.2 Ch12 low citation density (9 citations) | **FIXED** -- now 32 citations, 28 unique keys (see Section 3) |
| 2.3 Rogue color `#1A1A3E` in components.css | **PERSISTS** |
| 2.4 276,000 figure in Ch2 before Ch6 primary treatment | **PERSISTS** |
| 2.5 Chart font mismatch (DejaVu Sans) | **PERSISTS** |
| 2.6 PDF `mainfont` set to Playfair Display | **PERSISTS** |
| 2.7 Duplicate `ai-investment.png` in Ch5/Ch11 | **PERSISTS** |
| 2.8 Typst template not Quarto-compatible | **PERSISTS** |
| 2.9 Missing editorial briefs for Ch9--14 | **PERSISTS** |
| 2.10 CLAUDE.md references `00-introduction.qmd` | **PERSISTS** |
| 2.11 `docs/` directory stale | **FIXED** -- updated with latest build and PDF |

---

## 1. Targeted Verification Results

### 1.1 PDF Chapter Numbering -- PASS

PDF rendered successfully via `quarto render --to pdf`. Chapter numbering verified via `pdftotext`:

| Part | Chapters | Numbers |
|------|----------|---------|
| Part I: The Predictions | Ch1--2 | 1, 2 |
| Part II: The Evidence | Ch3--6 | 3, 4, 5, 6 |
| Part III: The Inflection | Ch7--10 | 7, 8, 9, 10 |
| Part IV: The Broader Impact | Ch11--12 | 11, 12 |
| Part V: What Comes Next | Ch13--14 | 13, 14 |

**All 14 chapters numbered sequentially. No gaps, duplicates, or misnumbering.**

### 1.2 Ch6 Human Profiles -- PASS (with minor notes)

Three profile sections found in `chapters/06-human-cost.qmd`, lines 156--173:

| Profile | Citation Key | Source | Tier | Bib Entry | Complete |
|---------|-------------|--------|:----:|:---------:|:--------:|
| Kenneth Kang (line 158) | `@bbc2025_kang_cs_grad` | BBC News | **1** | Yes | Yes |
| Dropbox layoffs (line 164) | `@cnbc2025_dropbox_layoffs` | CNBC | **1** | Yes | Yes |
| Psychological Toll (line 170) | `@sharma2025_ai_displacement_psych` | *Int'l J. Qualitative Studies on Health & Well-being* (Taylor & Francis / PubMed Central) | **1** | Yes | Yes |

**All 3 profiles backed by Tier-1 sources.** Two editorial notes:
- The psychology study (Sharma et al.) specifically examined *Indian* IT professionals. Ch6 omits this geographic qualifier -- readers may assume a global sample.
- The Dropbox section references anonymous Blind forum posts without a separate citation. This is standard journalistic practice but means those specific claims are not independently verifiable through the bibliography.

### 1.3 Ch12 Source Quality -- DRAMATICALLY IMPROVED

| Metric | v3 | v4 | Change |
|--------|---:|---:|--------|
| Total citation instances | 9 | **32** | **+23** |
| Unique citation keys | 9 | **28** | **+19** |
| Tier-1 sources | ~3 | **10** (35.7%) | **+7** |
| Tier-2 sources | ~4 | **14** (50.0%) | **+10** |
| Tier-3 sources | ~2 | **4** (14.3%) | **+2** |
| Sections with zero citations | 3+ | **1** (intro only) | **Resolved** |

19 new sources were added (confirmed by `sources.bib` section header: `% Ch12 Geopolitical Sources (Added 2026-02-13, QA v3 Fix)`).

**Tier-1 highlights:** White House EO, EU AI Act, BIS export controls, CRS report, GAO audit, Chinese State Council NGAIDP, Bloomberg, CNBC, Federal Reserve FEDS Notes, peer-reviewed journal article.

**Tier-2 highlights:** CSIS, CNAS, Bruegel, Stanford HAI, Tony Blair Institute, Fortune, DLA Piper, TechInsights, SEMI.

**Remaining weaknesses:**
- 2 DeepSeek sources cite Wikipedia instead of primary technical reports
- TSMC market share cites Carbon Credits (niche site) instead of TrendForce/Counterpoint
- "American Approach" section (lines 14--31) has only 2 citations for 18 lines of policy analysis
- "California Experiment" section (lines 105--116) has only 1 citation for 12 lines

### 1.4 Quote Deduplication -- PASS (4/5 fully resolved)

| # | Quote | Ch2 | Ch7 | Ch9 | Ch10 | Result |
|:-:|-------|:---:|:---:|:---:|:----:|:------:|
| 1 | Cherny "22 PRs in a single day" | Verbatim | Paraphrase + xref | N/A | Paraphrase + xref | **PASS** |
| 2 | Cherny "never had this much joy" | Verbatim | Paraphrase + xref | N/A | Paraphrase + xref | **PASS** |
| 3 | Roon "100%, I don't write code" | Verbatim | Paraphrase + xref | N/A | Paraphrase + xref | **PASS** |
| 4 | Krieger "Claude is now writing Claude" | Verbatim | Paraphrase + xref | N/A | Paraphrase + xref | **PASS** |
| 5 | Daniela Amodei humanities/hiring | Verbatim | N/A | Paraphrase + xref | Paraphrase + xref | **PASS** (within scope) |

**Ch2 retains all original verbatim quotes. Ch7, Ch9, Ch10 consistently use paraphrases with `@sec-voices-of-warning` cross-references.**

**Caveat:** Daniela Amodei's three verbatim quotes appear identically in both Ch2 (lines 90--94) and Ch6 (lines 116--124). Ch6's treatment is editorially distinct (workforce context vs. voices-of-warning context), but the verbatim duplication remains. See Minor issue 2.7.

---

## 2. Issues Found (Priority Order)

### CRITICAL

*None.*

### SIGNIFICANT

#### 2.1 Prediction Realization Score Contradiction: 70% vs 35% (NEW)

**Affected files:**
- `chapters/01-the-prediction.qmd`, line 131: *"the 90% AI-coded threshold at Anthropic (70%)"*
- `chapters/02-voices-of-warning.qmd`, line 33: *"90% of code AI-written | ... | 70%"*
- `chapters/14-what-now.qmd`, line 31: *"90% AI-written code by end of 2025 | 35%"*
- `data/prediction-scorecard.csv`, line 7: *"35%"* with explanation: *"True at Anthropic itself but not industry-wide; most companies at 25-40%"*

**Problem:** The "90% of code AI-written by end of 2025" prediction is scored at **70% realization** in Ch1 and Ch2 but at **35%** in Ch14's authoritative scorecard table and the CSV source data. This is a direct data integrity contradiction. The CSV explanation makes 35% the correct figure. Ch1 and Ch2 must be updated to match.

#### 2.2 Mike Krieger Title Inconsistent Across Three Chapters (NEW)

**Affected files:**
- `chapters/02-voices-of-warning.qmd`, line 100: *"Chief of its Labs division"*
- `chapters/07-recursive-loop.qmd`, line 114: *"Chief Product Officer"*
- `chapters/10-compounding-teams.qmd`, line 80: *"Chief of Labs"*

**Problem:** Three different titles for the same person. His actual Anthropic title is **Chief Product Officer** (per public reporting). All three chapters must use this title consistently.

#### 2.3 `repo-url` Points to Nonexistent GitHub Organization (NEW)

**File:** `_quarto.yml`, line 14
**Problem:** `repo-url: https://github.com/sbah-research/Something-Big-Already-Happened` but the actual git remote is `https://github.com/zeroshotpress/Something-Big-Already-Happened`. All "Edit this page" and "Report an issue" links in the HTML output point to a nonexistent repository.

### MINOR

#### 2.4 Rogue Color `#1A1A3E` in components.css (Persists from v3)
**File:** `styles/components.css`, lines 14 and 123
**Problem:** Near-miss typo for `#1A1A2E` (`--bg-secondary`).

#### 2.5 276,000 Layoff Figure in Ch2 Before Ch6 Primary Treatment (Persists from v3)
**File:** `chapters/02-voices-of-warning.qmd`, line 80

#### 2.6 Chart Font Mismatch (Persists from v3)
**File:** `scripts/generate_charts.py`, line 61 -- DejaVu Sans instead of Inter.

#### 2.7 Daniela Amodei Quotes Verbatim in Both Ch2 and Ch6 (Residual from v3 2.1)
**Files:** `chapters/02-voices-of-warning.qmd` lines 90--94, `chapters/06-human-cost.qmd` lines 116--124
**Problem:** Three identical verbatim quotes appear in both chapters. Ch6 should either paraphrase with `@sec-voices-of-warning` cross-ref, or (if the editorial decision is to keep them in Ch6 as primary treatment for the workforce context) Ch2 should shorten to a preview.

#### 2.8 PDF `mainfont` Set to Heading Font (Persists from v3)
**File:** `_quarto.yml`, line 90 -- Playfair Display instead of Inter for body text.

#### 2.9 Duplicate `prediction-scorecard.png` in Ch1 and Ch14 (NEW)
**Files:** `chapters/01-the-prediction.qmd` line 123, `chapters/14-what-now.qmd` line 16
**Problem:** Same image file with different figure IDs (`#fig-prediction-overview` and `#fig-prediction-scorecard`). Same class of issue as the Ch5/Ch11 `ai-investment.png` duplicate. Consider generating a simplified overview for Ch1 or explicitly noting the bookend design.

#### 2.10 Duplicate `ai-investment.png` in Ch5 and Ch11 (Persists from v3)
**Files:** `chapters/05-model-avalanche.qmd` line 159, `chapters/11-investment-tsunami.qmd` line 107

#### 2.11 BibTeX Key `anthropic2025_opus46` Year Mismatch (NEW)
**File:** `references/sources.bib`, line 323
**Problem:** Key says "2025" but entry `year = {2026}` (released Feb 5, 2026). Does not affect rendering but creates author confusion.

#### 2.12 Opus 4.5 Shares BibTeX Entry with Opus 4.6 (NEW)
**File:** `references/sources.bib`, line 331
**Problem:** Single entry covers two distinct releases (Opus 4.5 Nov 2025, Opus 4.6 Feb 2026). Chapters citing Opus 4.5 facts render as "Anthropic 2026" -- incorrect year for Nov 2025 claims.

#### 2.13 EPUB File Stale (NEW)
**File:** `Something-Big-Already-Happened.epub`
**Problem:** Timestamp (09:59) predates latest commit. Does not reflect recent edits.

#### 2.14 Typst Template Not Quarto-Compatible (Persists from v3)
**File:** `templates/premium.typ`

#### 2.15 Missing Editorial Briefs for Ch9--14 (Persists from v3)
**Directory:** `briefs/`

#### 2.16 CLAUDE.md References Non-Existent `00-introduction.qmd` (Persists from v3)
**File:** `CLAUDE.md`, line 14

---

## 3. Ch12 Source Tier Breakdown (Full Detail)

### Tier 1: Government Documents, Wire Services, Major Papers, Peer-Reviewed (10 sources, 35.7%)

| Key | Source |
|-----|--------|
| `whitehouse2025_ai` | The White House (Executive Order) |
| `eu_ai_act` | European Union (Official Legislation) |
| `bis2024_export_controls` | U.S. Bureau of Industry and Security |
| `sutter2025_crs_export_controls` | Congressional Research Service |
| `gao2026_chips_act` | U.S. Government Accountability Office |
| `digichina2017_ngaidp` | Chinese State Council (via Stanford DigiChina) |
| `bloomberg2025_huawei_smic` | Bloomberg |
| `cnbc2025_nvidia_smuggling` | CNBC |
| `haag2025_fed_ai_competition` | Federal Reserve Board (FEDS Notes) |
| `shrivastava2025_china_semiconductor_conundrum` | Taylor & Francis (peer-reviewed) |

### Tier 2: Major Tech/Business Outlets, Think Tanks (14 sources, 50.0%)

| Key | Source |
|-----|--------|
| `openai2025_stargate` | OpenAI (official announcement) |
| `openai2026_calaw` | Fortune |
| `amodei2026_davos` | Fortune |
| `businessworld2026_davos` | Business World |
| `dlapiper2025_eu_ai_act` | DLA Piper (intl. law firm) |
| `stanfordhai2025_ai_investment` | Stanford HAI AI Index |
| `shivakumar2025_csis_export_limits` | CSIS |
| `nie2025_cnas_export_loophole` | CNAS |
| `bruegel2025_deepseek_geopolitics` | Bruegel |
| `tbi2026_sovereignty_ai` | Tony Blair Institute |
| `batra2025_deepseek_moment` | Observer Research Foundation |
| `camba2026_burn_choke` | War on the Rocks |
| `techinsights2025_kirin9030_smic` | TechInsights |
| `semi2025_eighteen_fabs` | SEMI |

### Tier 3: Blogs, Wikipedia, Minor Outlets (4 sources, 14.3%)

| Key | Source | Upgrade Path |
|-----|--------|-------------|
| `deepseek2024_v3` | Wikipedia | Cite DeepSeek's arXiv paper |
| `deepseek2025_r1` | Wikipedia | Cite DeepSeek's arXiv paper |
| `meta2024_llama31` | Meta AI blog | Acceptable (primary company source) |
| `carboncredits2025_tsmc_market_share` | Carbon Credits (niche site) | Cite TrendForce or TSMC SEC filings |

---

## 4. Cross-Chapter Consistency

### Number Consistency

| Item | Status | Notes |
|------|--------|-------|
| "twenty-three predictions" | **PASS** | Consistent across Ch1, Ch7, Ch14 |
| "twenty-eight major models" | **PASS** | Consistent across Ch1, Ch4, Ch5, Ch6 |
| "79.2%" SWE-bench | **PASS** | Consistent across 8 chapters |
| "4 hours 49 minutes" METR | **PASS** | Consistent |
| "276,000" layoffs | **PASS** | Consistent (one "276,000+" variant in Ch6) |
| "90% AI code" prediction score | **FAIL** | 70% in Ch1/Ch2, 35% in Ch14/CSV (see Issue 2.1) |
| Mike Krieger's title | **FAIL** | 3 different titles (see Issue 2.2) |

### Repetition Rules Compliance

| Rule | Status |
|------|--------|
| Verbatim quote dedup (Ch2 → Ch7/Ch9/Ch10) | **PASS** (4/5 fully fixed, Amodei residual in Ch6 only) |
| "instrumental in creating itself" only in Ch7 | **PASS** |
| 79.2% detailed analysis only in Ch3 | **PASS** |
| 276,000 detailed analysis only in Ch6 | **PARTIAL** -- full number still in Ch2 line 80 |

---

## 5. Comparison: v3 vs v4

| Metric | v3 | v4 | Change |
|--------|---:|:--:|--------|
| Overall Score | 9.0/10 | **8.8/10** | -0.2 (new issues offset fixes) |
| Critical Issues | 0 | **0** | Maintained |
| Significant Issues | 1 | **3** | +2 (new findings) |
| Minor Issues | 10 | **13** | +3 (deeper inspection) |
| v3 Significant fixed | -- | **1 of 1** | Mostly fixed |
| v3 Minor fixed | -- | **2 of 10** | Ch12 citations + docs/ |
| Ch12 citations | 9 | **32** | **+23** |
| Ch12 Tier-1+2 ratio | ~70% | **85.7%** | **+15.7pp** |
| Quote dedup compliance | FAIL | **PASS** (4/5) | Fixed |
| PDF chapter numbering | Not verified | **1--14 correct** | Verified |
| Ch6 profile sources | Not verified | **3/3 Tier-1** | Verified |

---

## 6. Recommended Fix Priority

### Must Fix Before Publication
1. **Fix prediction score contradiction** -- update Ch1 line 131 and Ch2 line 33 from 70% to 35% to match Ch14/CSV
2. **Standardize Mike Krieger's title** -- use "Chief Product Officer" consistently in Ch2, Ch7, Ch10
3. **Fix `repo-url`** in `_quarto.yml` -- change `sbah-research` to `zeroshotpress`

### Should Fix
4. Paraphrase Daniela Amodei quotes in Ch6 (or Ch2) to eliminate last verbatim duplication
5. Replace Ch12's 2 Wikipedia DeepSeek sources with arXiv primary sources
6. Fix rogue `#1A1A3E` → `#1A1A2E` in `styles/components.css`
7. Fix `_quarto.yml` PDF `mainfont` from Playfair Display to Inter
8. Split `anthropic2025_opus46` bib entry into separate Opus 4.5 and 4.6 entries
9. Regenerate EPUB

### Nice to Have
10. Replace "276,000" in Ch2 line 80 with vaguer reference + `@sec-human-cost`
11. Add geographic qualifier ("Indian IT professionals") to Ch6 psychology study reference
12. Fix Typst template for Quarto compatibility
13. Create editorial briefs for Ch9--14
14. Update CLAUDE.md to remove `00-introduction.qmd` reference
15. Deduplicate `prediction-scorecard.png` and `ai-investment.png` across chapters

---

*Report generated: 2026-02-13*
*Previous report archived to: `archive/REVIEW-REPORT-v3.md`*
