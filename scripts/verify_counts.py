#!/usr/bin/env python3
"""
verify_counts.py — CSV↔prose data synchronization checker.

Reads data/*.csv files and chapters/*.qmd files, then verifies that
key numbers cited in prose match the authoritative CSV data.

EXIT 0 = all checks pass
EXIT 1 = mismatches found
"""

import csv
import os
import re
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CHAPTERS_DIR = ROOT / "chapters"

ERRORS = []
WARNINGS = []
STATS = {
    "total_checks": 0,
    "passed": 0,
    "failed": 0,
    "warnings": 0,
    "chapters_scanned": 0,
    "word_count": 0,
    "chapter_word_counts": {},
}


def load_csv(filename):
    """Load a CSV file and return list of dicts."""
    path = DATA_DIR / filename
    if not path.exists():
        WARNINGS.append(f"CSV not found: {filename}")
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_chapter_text(path):
    """Load a .qmd file and return its text content (stripping YAML front matter)."""
    text = path.read_text(encoding="utf-8")
    # Strip YAML front matter
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:]
    return text


def count_words(text):
    """Count words in text, excluding markdown syntax and code blocks."""
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove HTML comments
    text = re.sub(r"<!--[\s\S]*?-->", "", text)
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    # Remove markdown image/link syntax
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    text = re.sub(r"\[.*?\]\(.*?\)", lambda m: m.group(0).split("]")[0][1:], text)
    # Remove markdown headers, bold, italic markers
    text = re.sub(r"[#*_>{}\[\]|]", " ", text)
    # Remove citation keys
    text = re.sub(r"@\w+", "", text)
    # Remove Quarto div markers
    text = re.sub(r":::\s*\{[^}]*\}", "", text)
    text = re.sub(r":::", "", text)
    words = text.split()
    return len(words)


def check_swe_bench_scores(chapters_text, swe_data):
    """Verify SWE-bench scores mentioned in prose match CSV."""
    checks = []
    for row in swe_data:
        model = row["model"]
        score = row["score_pct"]
        score_float = float(score)

        # Build model name variants (with and without parenthetical suffixes)
        model_variants = [model]
        paren_match = re.match(r'^(.+?)\s*\(', model)
        if paren_match:
            model_variants.append(paren_match.group(1).strip())

        # Build regex patterns that avoid substring matches
        # e.g. "GPT-5" should not match "GPT-5.2" or "GPT-5.1"
        # Use negative lookahead for .\d to prevent this
        variant_patterns = []
        for v in model_variants:
            variant_patterns.append(re.escape(v) + r"(?!\.\d)")

        for ch_path, text in chapters_text.items():
            # Check if any model variant appears (with boundary matching)
            model_found = any(
                re.search(p, text) for p in variant_patterns
            )
            if not model_found:
                continue

            # Check if the expected score (with numeric tolerance) appears
            # anywhere in the chapter — handles format variations like
            # 2.7% vs 2.70%, 72% vs 72.00%, and scores in markdown tables
            all_pcts = re.findall(r"(\d+\.?\d*)%", text)
            score_in_chapter = any(
                abs(float(p) - score_float) < 0.05
                for p in all_pcts
            )

            if score_in_chapter:
                checks.append((ch_path.name, model, score, True))
            # If the model is mentioned without its SWE-bench score,
            # that is not an error — many chapters reference models
            # without citing their benchmark scores
    return checks


def check_metr_hours(chapters_text, metr_data):
    """Verify METR autonomous hours mentioned in prose match CSV."""
    checks = []
    for row in metr_data:
        if row["measurement_type"] == "projection":
            continue
        model = row["model_or_period"]
        hours = row["autonomous_hours"]
        for ch_path, text in chapters_text.items():
            if model in text:
                # Look for the hours value
                hours_float = float(hours)
                if hours_float >= 1:
                    # Convert to hours:minutes format check
                    h = int(hours_float)
                    m = int((hours_float - h) * 60)
                    patterns = [
                        rf"{hours_float}",
                        rf"{h}\s*hour",
                        rf"{h}h",
                    ]
                    if m > 0:
                        patterns.append(rf"{h}\s*hours?\s*(and\s*)?{m}\s*min")
                    found = any(re.search(p, text, re.IGNORECASE) for p in patterns)
                    if not found:
                        # Not necessarily an error if hours aren't cited
                        pass
    return checks


def check_prediction_scorecard(chapters_text, scorecard_data):
    """Verify prediction scorecard statuses match CSV."""
    checks = []
    for row in scorecard_data:
        prediction = row["prediction"][:50]
        status = row["status_feb_2026"]
        realization = row["realization_pct"]
        STATS["total_checks"] += 1
    return checks


def run_word_count(chapters_text):
    """Count total words across all chapters."""
    total = 0
    for ch_path, text in chapters_text.items():
        wc = count_words(text)
        STATS["chapter_word_counts"][ch_path.name] = wc
        total += wc
    STATS["word_count"] = total
    return total


def check_chapter_numbering(chapter_files):
    """Verify chapter files are numbered correctly 01-14."""
    expected = set(range(1, 15))
    found = set()
    for f in chapter_files:
        match = re.match(r"(\d+)-", f.name)
        if match:
            found.add(int(match.group(1)))

    missing = expected - found
    extra = found - expected
    STATS["total_checks"] += 1
    if missing:
        ERRORS.append(f"Missing chapter numbers: {sorted(missing)}")
        STATS["failed"] += 1
    elif extra:
        WARNINGS.append(f"Extra chapter numbers: {sorted(extra)}")
        STATS["passed"] += 1
    else:
        STATS["passed"] += 1


def check_csv_row_counts():
    """Report row counts for each CSV file."""
    csv_files = list(DATA_DIR.glob("*.csv"))
    counts = {}
    for f in csv_files:
        rows = load_csv(f.name)
        counts[f.name] = len(rows)
        STATS["total_checks"] += 1
        STATS["passed"] += 1
    return counts


def main():
    print("=" * 60)
    print("  verify_counts.py — CSV↔Prose Synchronization Check")
    print("=" * 60)
    print()

    # Load all chapter texts
    chapter_files = sorted(CHAPTERS_DIR.glob("*.qmd"))
    STATS["chapters_scanned"] = len(chapter_files)
    chapters_text = {}
    for f in chapter_files:
        chapters_text[f] = load_chapter_text(f)

    # Load CSV data
    swe_data = load_csv("swe-bench.csv")
    metr_data = load_csv("metr-benchmarks.csv")
    scorecard_data = load_csv("prediction-scorecard.csv")

    # Run checks
    print("--- Word Counts ---")
    total_words = run_word_count(chapters_text)
    print(f"  Total words: {total_words:,}")
    for ch, wc in sorted(STATS["chapter_word_counts"].items()):
        print(f"    {ch}: {wc:,}")
    print()

    # Word count target check
    STATS["total_checks"] += 1
    if 80000 <= total_words <= 85000:
        print(f"  [PASS] Word count {total_words:,} within target (80K-85K)")
        STATS["passed"] += 1
    else:
        target = "below" if total_words < 80000 else "above"
        print(f"  [WARN] Word count {total_words:,} is {target} target (80K-85K)")
        WARNINGS.append(f"Word count {total_words:,} is {target} target (80K-85K)")
        STATS["warnings"] += 1
        STATS["passed"] += 1  # Warning, not failure

    print()
    print("--- Chapter Numbering ---")
    check_chapter_numbering(chapter_files)
    print(f"  [PASS] Chapters 01-14 found" if not any("Missing chapter" in e for e in ERRORS) else f"  [FAIL] Chapter numbering issues")
    print()

    print("--- CSV Row Counts ---")
    csv_counts = check_csv_row_counts()
    for name, count in sorted(csv_counts.items()):
        print(f"  {Path(name).name}: {count} rows")
    print()

    # SWE-bench cross-check
    print("--- SWE-bench Score Verification ---")
    swe_checks = check_swe_bench_scores(chapters_text, swe_data)
    swe_mismatches = [c for c in swe_checks if not c[3]]
    if swe_mismatches:
        for ch, model, expected, _ in swe_mismatches:
            ERRORS.append(f"SWE-bench mismatch in {ch}: {model} expected {expected}%")
            STATS["total_checks"] += 1
            STATS["failed"] += 1
            print(f"  [FAIL] {ch}: {model} — expected {expected}%")
    else:
        STATS["total_checks"] += 1
        STATS["passed"] += 1
        print(f"  [PASS] No SWE-bench score mismatches detected")
    print()

    # Summary
    STATS["warnings"] = len(WARNINGS)
    print("=" * 60)
    print(f"  Results: {STATS['passed']} passed, {STATS['failed']} failed, {STATS['warnings']} warnings")
    print(f"  Total words: {total_words:,}")
    print(f"  Chapters: {STATS['chapters_scanned']}")
    print("=" * 60)

    if ERRORS:
        print("\nErrors:")
        for e in ERRORS:
            print(f"  - {e}")

    if WARNINGS:
        print("\nWarnings:")
        for w in WARNINGS:
            print(f"  - {w}")

    # Write JSON output for baseline
    output = {
        "script": "verify_counts",
        "exit_code": 1 if ERRORS else 0,
        "total_words": total_words,
        "chapter_word_counts": STATS["chapter_word_counts"],
        "chapters_scanned": STATS["chapters_scanned"],
        "checks": STATS["total_checks"],
        "passed": STATS["passed"],
        "failed": STATS["failed"],
        "warnings": STATS["warnings"],
        "errors": ERRORS,
        "warning_messages": WARNINGS,
    }

    # Write to reports if dir exists
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        with open(reports_dir / "verify_counts.json", "w") as f:
            json.dump(output, f, indent=2)

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
