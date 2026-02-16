# Single Source of Truth (SSOT)

> This document points to the authoritative location for every category of project data.
> When in doubt, the MASTER-PLAN.md at repo root is the ultimate authority.

## Authoritative Files

| Category | File | Owner |
|----------|------|-------|
| Master plan & rules | `/MASTER-PLAN.md` | Lead |
| Project instructions | `/CLAUDE.md` | Lead |
| Story continuity | `/docs/STORY-BIBLE.md` | Writer (updated per chapter) |
| Source classification | `/references/source-registry.yml` | Researcher |
| Bibliography | `/references/sources.bib` | Researcher |
| Prediction data | `/data/prediction-scorecard.csv` | Researcher |
| METR benchmarks | `/data/metr-benchmarks.csv` | Researcher |
| SWE-bench data | `/data/swe-bench.csv` | Researcher |
| Model releases | `/data/model-releases.csv` | Researcher |
| AI timeline | `/data/ai-timeline.csv` | Researcher |
| Design system | `/references/design-reference.html` | Visual Designer |
| Brand tokens | `/_brand.yml` | Visual Designer |

## Authoritative Numbers

When prose and CSV disagree, **CSV wins**. Fix the prose.

## Build Profiles

| Profile | Command | Output |
|---------|---------|--------|
| Web (HTML) | `quarto render --profile web` | `_book/` |
| Ebook (EPUB) | `quarto render --profile ebook` | `_book/*.epub` |
| Print (KDP PDF) | `quarto render --profile print-kdp` | `_book/*.pdf` |

## Validation Gates

All 6 scripts must EXIT 0 before tagging a release:

1. `scripts/verify_counts.py`
2. `scripts/source_audit.py`
3. `scripts/voice_audit.py`
4. `scripts/image_dpi_check.py`
5. `scripts/quote_audit.py`
6. `scripts/preflight_kdp.sh`
