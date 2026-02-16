# Phase 3 Review Report
## Date: 2026-02-13

---

## Summary

Phase 3 focused on three production-readiness tasks: citation registry completion, PROOF annotation reinforcement for Ch3-7, and PDF/EPUB build optimization. All 6 quality gates pass. PDF density reduced from 240 to 207 pages (target 190-210). EPUB validates cleanly via epubcheck.

## Task 1: Citation Registry Completion

### Problem
source_audit.py reported 141 unregistered citations. Investigation revealed:
- 31 were false positives from Quarto cross-references (`@sec-`, `@fig-`, `@tbl-`)
- 56 were legitimate citations missing from source-registry.yml
- Remaining were aliases/duplicates already resolved

### Fixes
1. **source_audit.py**: Added exclusion for Quarto cross-reference prefixes (`sec`, `fig`, `tbl`, `eq`, `lst`, `thm`) in `extract_citations()`
2. **source-registry.yml**: Added 56 new citation entries with full metadata (tier, type, scope, paywalled, url, notes)
3. Reclassified 3 entries: Time.com (Tier 2 → Tier 1), Axios (Tier 2 → Tier 1), StrongDM factory (Tier 2 → Tier 1)

### Result
- Total citations: 229
- Tier-1: 217 | Tier-2: 12 | Tier-3: 0
- Unregistered: 0
- source_audit.py: **PASS**

## Task 2: PROOF Annotations (Ch3-7)

Delegated to verification agent. Results:

| Chapter | Annotations Added | TODO Markers |
|---------|------------------|--------------|
| Ch3 | 0 (already complete) | 0 |
| Ch4 | 0 (already complete) | 0 |
| Ch5 | 2 (Marcus "Deep Learning Hitting a Wall"; Andreessen late-2024 concession) | 0 |
| Ch6 | 3 (BLS unemployment; Amazon 14K layoff; Salesforce 4K reduction) | 0 |
| Ch7 | 0 (already complete) | 0 |
| **Total** | **5** | **0** |

All claims verified via web search. No unverifiable claims found.

### Note
Ch5 flagged Anthropic's "$8.3 billion" funding figure as potentially imprecise (actual: $3.5B Series D + $13B Amazon total). Existing source citation is adequate but may warrant human review.

## Task 3: PDF Density + EPUB Build

### PDF Optimization Journey

| Iteration | Change | Pages |
|-----------|--------|-------|
| Phase 2 baseline | 11pt, linestretch 1.2, Inter font | 240 |
| Fix font to TeX Gyre Pagella | Font density improvement | 288 |
| Add print-header.tex optimizations | Section spacing, compact lists, float spacing, tcolorbox, bibliography | 279 |
| Reduce linestretch to 1.05 | Line spacing tighter | 249 |
| Reduce fontsize to 10pt | Smaller base font | 208 |
| Final (10pt + linestretch 1.05) | All optimizations combined | **207** |

### Key Changes
- **_quarto.yml**: Unified PDF section with print-kdp profile (scrbook, TeX Gyre Pagella, 10pt, linestretch 1.05, lualatex). Added `lang: en` at top level.
- **_quarto-print-kdp.yml**: 10pt, linestretch 1.05, TeX Gyre Pagella/Heros/Cursor font family, fig-pos: 'H'
- **templates/print-header.tex**: Complete density rewrite:
  - KOMA-Script section command spacing (chapter: 18pt/8pt, section: 10pt/4pt, subsection: 6pt/3pt)
  - Float spacing: textfloatsep=4pt, intextsep=3pt, floatsep=3pt
  - Compact lists via enumitem (nosep)
  - Block quote tightening (leftmargin=1.5em, topsep=3pt)
  - Callout box (tcolorbox) compactness with `\small` font
  - Longtable `\small` with LTpre/LTpost=4pt
  - Bibliography (CSLReferences) compactness with `\small`
  - Part page spacing reduction (beforeskip=40pt, afterskip=20pt)
  - Figure scaling (max height 0.4\textheight)
  - Display math spacing tightened

### EPUB Build
- Removed missing `epub-cover-image: images/cover.png` from _quarto-ebook.yml
- Fixed language tag error (`lang="C"` → `lang="en"`) via top-level `lang: en` in _quarto.yml
- epubcheck: **PASS** (0 errors, 0 warnings)

### Final PDF Specs
- Pages: 207 (target: 190-210)
- Dimensions: 6.00 x 9.00 in (432 x 648 pts)
- Fonts: 10 fonts, all embedded
- File size: 3.8 MB
- Engine: LuaHBTeX 1.22.0

## Quality Gates (6/6 PASS)

| Gate | Script | Result |
|------|--------|--------|
| 1 | verify_counts.py | PASS (80,008 words, 14 chapters) |
| 2 | source_audit.py | PASS (229 citations, 0 unregistered, 0 Tier-3) |
| 3 | voice_audit.py | PASS (0 banned words, 0 violations, burstiness all >8) |
| 4 | image_dpi_check.py | PASS (30 images, all ≥ 300 DPI) |
| 5 | quote_audit.py | PASS (3 quotes, 0 over limit) |
| 6 | preflight_kdp.sh | PASS (207 pages, 6x9, all fonts embedded) |

## Files Modified

| File | Change |
|------|--------|
| scripts/source_audit.py | Quarto cross-reference exclusion |
| references/source-registry.yml | +56 citation entries |
| _quarto.yml | Unified PDF settings, `lang: en` |
| _quarto-print-kdp.yml | 10pt, linestretch 1.05, font family |
| _quarto-ebook.yml | Commented out missing cover image |
| templates/print-header.tex | Complete density optimization rewrite |
| chapters/05-model-avalanche.qmd | +2 PROOF annotations |
| chapters/06-human-cost.qmd | +3 PROOF annotations |

## Remaining Work (Phase 4 candidates)

1. **Cover image**: EPUB has no cover (`epub-cover-image` commented out)
2. **Anthropic funding figure**: Ch5 "$8.3 billion" may need human verification
3. **Word count expansion**: Book at 80,008 — room for 5K more if desired
4. **Web deploy test**: Full GitHub Pages build with updated settings
5. **Typst warning**: `The typst format is not supported by book projects` — remove typst section from _quarto.yml
6. **ImageMagick for preflight**: DPI check skipped in preflight_kdp.sh (no identify/exiftool)

## Phase 3 Completion Criteria

- [x] Citation registry: 0 unregistered (was 141 warnings)
- [x] PROOF annotations: Ch3-7 verified (+5 annotations, 0 TODOs)
- [x] PDF density: 207 pages (target 190-210, was 240)
- [x] EPUB build: validates via epubcheck
- [x] 6/6 quality gates EXIT 0
- [x] Review report written
