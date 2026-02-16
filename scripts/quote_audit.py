#!/usr/bin/env python3
"""
quote_audit.py — Quote hygiene checker.

Rules:
  - Direct quotes (blockquote) max 25 words each
  - Same source max 200 words total quoted
  - Shumer essay: only 2-3 direct quotes, rest paraphrased

EXIT 0 = all checks pass
EXIT 1 = violations found
"""

import os
import re
import sys
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters"

ERRORS = []
WARNINGS = []
STATS = {
    "chapters_scanned": 0,
    "total_quotes": 0,
    "over_limit_quotes": 0,
    "over_limit_sources": 0,
    "chapter_details": {},
}

MAX_WORDS_PER_QUOTE = 25
MAX_WORDS_PER_SOURCE = 200


def strip_frontmatter(text):
    """Remove YAML front matter."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:]
    return text


def extract_blockquotes(text):
    """Extract blockquote content and nearby citation keys."""
    quotes = []

    # Match > prefixed lines (markdown blockquotes)
    # Group consecutive > lines as one quote
    lines = text.split("\n")
    current_quote = []
    current_start = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith(">"):
            if current_start is None:
                current_start = i
            # Remove > prefix and any continuation >
            content = re.sub(r"^>\s*", "", stripped)
            current_quote.append(content)
        else:
            if current_quote:
                quote_text = " ".join(current_quote).strip()
                # Look for citation key in the quote or nearby lines
                citation_key = None
                context = "\n".join(lines[max(0, current_start - 2):min(len(lines), i + 3)])
                keys = re.findall(r"@(\w+)", context)
                if keys:
                    citation_key = keys[-1]  # Use the closest citation
                quotes.append({
                    "text": quote_text,
                    "word_count": len(quote_text.split()),
                    "line": current_start + 1,
                    "citation_key": citation_key,
                })
                current_quote = []
                current_start = None

    # Handle quote at end of file
    if current_quote:
        quote_text = " ".join(current_quote).strip()
        citation_key = None
        context = "\n".join(lines[max(0, current_start - 2):])
        keys = re.findall(r"@(\w+)", context)
        if keys:
            citation_key = keys[-1]
        quotes.append({
            "text": quote_text,
            "word_count": len(quote_text.split()),
            "line": current_start + 1,
            "citation_key": citation_key,
        })

    return quotes


def audit_chapter(ch_path):
    """Audit quotes in a single chapter."""
    text = ch_path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)

    quotes = extract_blockquotes(text)
    chapter_name = ch_path.name

    result = {
        "file": chapter_name,
        "total_quotes": len(quotes),
        "over_limit_quotes": [],
        "source_word_counts": defaultdict(int),
        "over_limit_sources": [],
    }

    for q in quotes:
        STATS["total_quotes"] += 1

        # Check individual quote length
        if q["word_count"] > MAX_WORDS_PER_QUOTE:
            result["over_limit_quotes"].append(q)
            STATS["over_limit_quotes"] += 1

        # Accumulate per-source word counts
        if q["citation_key"]:
            result["source_word_counts"][q["citation_key"]] += q["word_count"]

    # Check per-source limits
    for source, total_words in result["source_word_counts"].items():
        if total_words > MAX_WORDS_PER_SOURCE:
            result["over_limit_sources"].append({
                "source": source,
                "total_words": total_words,
                "limit": MAX_WORDS_PER_SOURCE,
            })
            STATS["over_limit_sources"] += 1

    # Convert defaultdict for JSON serialization
    result["source_word_counts"] = dict(result["source_word_counts"])
    return result


def main():
    print("=" * 60)
    print("  quote_audit.py — Quote Hygiene Checker")
    print("=" * 60)
    print()

    chapter_files = sorted(CHAPTERS_DIR.glob("*.qmd"))
    STATS["chapters_scanned"] = len(chapter_files)

    all_results = []
    has_errors = False

    # Aggregate source word counts across all chapters
    global_source_words = defaultdict(int)

    for ch_path in chapter_files:
        result = audit_chapter(ch_path)
        all_results.append(result)
        STATS["chapter_details"][result["file"]] = result

        # Aggregate global source counts
        for source, words in result["source_word_counts"].items():
            global_source_words[source] += words

        print(f"  {result['file']}: {result['total_quotes']} quotes")

        if result["over_limit_quotes"]:
            for q in result["over_limit_quotes"]:
                msg = f"{result['file']} line {q['line']}: {q['word_count']} words (limit: {MAX_WORDS_PER_QUOTE})"
                ERRORS.append(msg)
                has_errors = True
                preview = q["text"][:60] + "..." if len(q["text"]) > 60 else q["text"]
                print(f"    [FAIL] Line {q['line']}: {q['word_count']}w — \"{preview}\"")

    print()

    # Check global per-source limits
    print("--- Per-Source Word Totals (across all chapters) ---")
    global_over_limit = []
    for source, total in sorted(global_source_words.items(), key=lambda x: -x[1]):
        status = "FAIL" if total > MAX_WORDS_PER_SOURCE else "OK"
        print(f"  [{status}] @{source}: {total} words" +
              (f" (limit: {MAX_WORDS_PER_SOURCE})" if total > MAX_WORDS_PER_SOURCE else ""))
        if total > MAX_WORDS_PER_SOURCE:
            global_over_limit.append({"source": source, "total": total})
            ERRORS.append(f"Source @{source}: {total} quoted words exceeds {MAX_WORDS_PER_SOURCE} limit")
            has_errors = True

    print()

    # Special check: Shumer essay quote count
    print("--- Shumer Essay Quote Check ---")
    shumer_quotes = 0
    for r in all_results:
        for q_data in extract_blockquotes(
            (CHAPTERS_DIR / r["file"]).read_text(encoding="utf-8")
        ):
            if q_data.get("citation_key") == "shumer2026":
                shumer_quotes += 1
    if shumer_quotes > 3:
        WARNINGS.append(f"Shumer essay has {shumer_quotes} direct quotes (target: 2-3)")
        print(f"  [WARN] {shumer_quotes} direct quotes from Shumer essay (target: 2-3)")
    else:
        print(f"  [OK] {shumer_quotes} direct quotes from Shumer essay")
    print()

    # Summary
    print("=" * 60)
    print(f"  Total quotes: {STATS['total_quotes']}")
    print(f"  Over {MAX_WORDS_PER_QUOTE}-word limit: {STATS['over_limit_quotes']}")
    print(f"  Sources over {MAX_WORDS_PER_SOURCE}-word limit: {len(global_over_limit)}")
    print(f"  Result: {'FAIL' if has_errors else 'PASS'}")
    print("=" * 60)

    if WARNINGS:
        print("\nWarnings:")
        for w in WARNINGS:
            print(f"  - {w}")

    # Write JSON output
    output = {
        "script": "quote_audit",
        "exit_code": 1 if has_errors else 0,
        "chapters_scanned": STATS["chapters_scanned"],
        "total_quotes": STATS["total_quotes"],
        "over_limit_quotes": STATS["over_limit_quotes"],
        "over_limit_sources": len(global_over_limit),
        "global_source_words": dict(global_source_words),
        "global_over_limit": global_over_limit,
        "errors": ERRORS,
        "warnings": [str(w) for w in WARNINGS],
    }
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        with open(reports_dir / "quote_audit.json", "w") as f:
            json.dump(output, f, indent=2)

    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
