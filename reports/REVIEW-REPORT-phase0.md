# Phase 0 Review Report: Infrastructure

**Date:** 2026-02-13
**Phase:** 0 — Infrastructure
**Status:** COMPLETE

---

## What Was Done

### Scripts Created (6)
1. `scripts/verify_counts.py` — CSV↔prose data synchronization checker
2. `scripts/source_audit.py` — 2-axis source classification auditor
3. `scripts/voice_audit.py` — AI-voice vocabulary and burstiness checker
4. `scripts/image_dpi_check.py` — Image quality and DPI verifier
5. `scripts/quote_audit.py` — Quote length and per-source limit checker
6. `scripts/preflight_kdp.sh` — Enhanced with file size, page count, JSON output

### Templates
- `templates/print-header.tex` — TeX Gyre Pagella, microtype, xurl, widow/orphan penalties

### Documentation (5 files)
- `docs/SSOT.md` — Single Source of Truth pointer document
- `docs/SOURCE-POLICY.md` — 2-axis source classification rules
- `docs/FORMAT-SPECS.md` — Technical specs for HTML/EPUB/PDF
- `docs/VOICE-STYLEGUIDE.md` — Writing style rules and banned words
- `docs/STORY-BIBLE.md` — Chapter continuity tracker (template populated)

### References
- `references/source-registry.yml` — Initial registry with ~30 classified citations

### Quarto Profiles (3)
- `_quarto-web.yml` — HTML for GitHub Pages
- `_quarto-ebook.yml` — EPUB for KDP
- `_quarto-print-kdp.yml` — PDF for KDP paperback (6x9, scrbook, lualatex)

---

## Baseline Results

| Gate | Exit Code | Status |
|------|-----------|--------|
| verify_counts.py | 1 | FAIL |
| source_audit.py | 1 | FAIL |
| voice_audit.py | 1 | FAIL |
| image_dpi_check.py | 0 | PASS |
| quote_audit.py | 1 | FAIL |
| preflight_kdp.sh | 0 | PASS |

**Gates passing: 2/6**

---

## Key Metrics

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Total words | 61,597 | 80,000-85,000 | -18,403 |
| PDF pages | 240 | 190-210 | +30 (will compress with tighter margins) |
| Words/page | ~257 | 380-420 | Need density increase |
| Tier-3 core claims | 20 | 0 | Must replace all |
| AI banned words | 55 | 0 | Must purge all |
| Over-length quotes | 1 | 0 | Ch7 line 51 (50 words) |
| Images passing DPI | 30/30 | 30/30 | CLEAR |
| Fonts embedded | 9/9 | All | CLEAR |

---

## Phase 1 Priority Analysis

### P0 — Tier-3 Source Replacement (source_audit → EXIT 0)

**9 unique Tier-3 citation keys** used 20 times across 7 chapters:

| Key | Used In | Action |
|-----|---------|--------|
| `deepseek2024_v3` | Ch3, Ch5, Ch11, Ch12 | Replace with official DeepSeek blog/paper |
| `deepseek2025_r1` | Ch1, Ch3, Ch5, Ch11, Ch12 | Replace with official DeepSeek announcement |
| `wiki_gpt4` | Ch3, Ch5 | Replace with OpenAI announcement |
| `wiki_gpt4o` | Ch5 | Replace with OpenAI blog post |
| `wiki_gemini` | Ch5 | Replace with Google DeepMind blog |
| `wiki_claude` | Ch5 | Replace with Anthropic announcement |
| `microsoft2025_jobs` | Ch1, Ch2, Ch6 | Replace with original Microsoft Research paper |
| `altman2025_future` | Ch2 | Replace with primary source (ALM Corp → Sam Altman blog) |
| `openai2024_funding` | Ch5, Ch11 | Replace with official press release / Reuters |

### P1 — AI-Voice Purge (voice_audit → EXIT 0)

**55 banned words** across all 14 chapters. Top offenders:
- `landscape` (18x) — Ch1, Ch4, Ch5, Ch6, Ch8, Ch11, Ch12, Ch13
- `navigate` (9x) — Ch3, Ch4, Ch6, Ch14
- `comprehensive` (9x) — Ch4, Ch6, Ch9, Ch10, Ch12, Ch13
- `leverage` (7x) — Ch2, Ch10, Ch12(4x)
- `nuanced` (6x) — Ch3, Ch8, Ch9, Ch10, Ch11
- `crucial` (5x) — Ch4, Ch10, Ch11, Ch13

### P2 — Quote Fix (quote_audit → EXIT 0)

One over-length quote in Ch7 (50 words, limit 25). Split or paraphrase.

### P3 — verify_counts Tuning

19 "SWE-bench mismatches" are largely false positives — the script detects model names in chapters but the exact decimal scores aren't always cited in prose (e.g., "49%" vs "49.00%"). **Script refinement needed** to distinguish between actual mismatches and prose that correctly rounds/approximates.

---

## Recommended Phase 1 Execution Order

1. **Source replacement**: Web-search for official Tier-1 URLs for the 9 Tier-3 keys. Update `sources.bib` and `source-registry.yml`. Re-run `source_audit.py`.
2. **AI-voice purge**: Find-and-replace all 55 banned words with natural alternatives. Re-run `voice_audit.py`.
3. **Quote fix**: Split the Ch7 blockquote. Re-run `quote_audit.py`.
4. **verify_counts refinement**: Adjust the SWE-bench mismatch detection logic to handle rounding.
5. **Re-run all gates** to confirm 6/6 EXIT 0.

---

## Files Created This Phase

```
scripts/verify_counts.py          (NEW)
scripts/source_audit.py           (NEW)
scripts/voice_audit.py            (NEW)
scripts/image_dpi_check.py        (NEW)
scripts/quote_audit.py            (NEW)
scripts/preflight_kdp.sh          (UPDATED — added file size, page count, JSON)
templates/print-header.tex        (NEW)
references/source-registry.yml    (NEW)
docs/SSOT.md                      (NEW)
docs/SOURCE-POLICY.md             (NEW)
docs/FORMAT-SPECS.md              (NEW)
docs/VOICE-STYLEGUIDE.md          (NEW)
docs/STORY-BIBLE.md               (NEW)
_quarto-web.yml                   (NEW)
_quarto-ebook.yml                 (NEW)
_quarto-print-kdp.yml             (NEW)
reports/baseline.json             (NEW)
reports/REVIEW-REPORT-phase0.md   (NEW)
reports/verify_counts.json        (NEW)
reports/source_audit.json         (NEW)
reports/voice_audit.json          (NEW)
reports/image_dpi_check.json      (NEW)
reports/quote_audit.json          (NEW)
reports/preflight_kdp.json        (NEW)
```
