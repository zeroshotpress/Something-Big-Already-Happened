#!/usr/bin/env python3
"""
voice_audit.py — Writing style and AI-voice vocabulary checker.

Checks for:
  1. Banned AI-voice words (delve, moreover, etc.)
  2. Banned repetitive patterns (> 2 uses per chapter)
  3. Burstiness (sentence-length stdev target > 8)

EXIT 0 = all checks pass
EXIT 1 = violations found
"""

import os
import re
import sys
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters"

ERRORS = []
WARNINGS = []

# Banned AI-voice words (case-insensitive)
BANNED_WORDS = [
    "delve",
    "moreover",
    "furthermore",
    "it is worth noting",
    "it is important to consider",
    "robust",
    "comprehensive",
    "crucial",
    "landscape",
    "navigate",
    "leverage",
    "multifaceted",
    "tapestry",
    "serves as a testament",
    "in the ever-evolving",
    "pivotal",
    "underscore",
    "nuanced",
    "paradigm shift",
    "at the heart of",
    "in an era where",
    "vibrant",
]

# Banned patterns (max 2 per chapter)
BANNED_PATTERNS = [
    r"was not merely .{1,30}\. It was",
    r"[Tt]he implication was (stark|sharp|clear)",
    r"[Tt]his was not .{1,30}\. [Tt]his was",
]

STATS = {
    "chapters_scanned": 0,
    "total_banned_words": 0,
    "total_pattern_violations": 0,
    "burstiness_failures": 0,
    "chapter_details": {},
}


def strip_frontmatter(text):
    """Remove YAML front matter."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:]
    return text


def strip_code_and_comments(text):
    """Remove code blocks, inline code, and HTML comments."""
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"<!--[\s\S]*?-->", "", text)
    return text


def get_sentences(text):
    """Split text into sentences."""
    # Remove markdown headers
    text = re.sub(r"^#{1,6}\s+.*$", "", text, flags=re.MULTILINE)
    # Remove callout divs
    text = re.sub(r":::\s*\{[^}]*\}", "", text)
    text = re.sub(r":::", "", text)
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    # Remove citation keys
    text = re.sub(r"\[@[^\]]+\]", "", text)
    # Split on sentence boundaries
    sentences = re.split(r"(?<=[.!?])\s+", text)
    # Filter out very short fragments
    sentences = [s.strip() for s in sentences if len(s.strip().split()) >= 3]
    return sentences


def count_word_occurrences(text, word):
    """Count case-insensitive occurrences of a word/phrase in text."""
    return len(re.findall(re.escape(word), text, re.IGNORECASE))


def check_banned_words(text, chapter_name):
    """Check for banned AI-voice words."""
    findings = []
    for word in BANNED_WORDS:
        count = count_word_occurrences(text, word)
        if count > 0:
            findings.append({"word": word, "count": count})
            STATS["total_banned_words"] += count
    return findings


def check_banned_patterns(text, chapter_name):
    """Check for banned repetitive patterns (max 2 per chapter)."""
    violations = []
    for pattern in BANNED_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if len(matches) > 2:
            violations.append({
                "pattern": pattern,
                "count": len(matches),
                "limit": 2,
            })
            STATS["total_pattern_violations"] += 1
    return violations


def measure_burstiness(text):
    """Measure sentence-length burstiness (stdev of word counts)."""
    sentences = get_sentences(text)
    if len(sentences) < 5:
        return 0.0, len(sentences)
    lengths = [len(s.split()) for s in sentences]
    stdev = statistics.stdev(lengths)
    return stdev, len(sentences)


def audit_chapter(ch_path):
    """Audit a single chapter."""
    text = ch_path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    clean_text = strip_code_and_comments(text)

    chapter_name = ch_path.name
    result = {
        "file": chapter_name,
        "banned_words": [],
        "pattern_violations": [],
        "burstiness_stdev": 0.0,
        "sentence_count": 0,
        "pass": True,
    }

    # Check banned words
    banned = check_banned_words(clean_text, chapter_name)
    result["banned_words"] = banned
    if banned:
        result["pass"] = False

    # Check banned patterns
    patterns = check_banned_patterns(clean_text, chapter_name)
    result["pattern_violations"] = patterns
    if patterns:
        result["pass"] = False

    # Measure burstiness
    stdev, sentence_count = measure_burstiness(clean_text)
    result["burstiness_stdev"] = round(stdev, 2)
    result["sentence_count"] = sentence_count
    if stdev < 8.0 and sentence_count >= 10:
        result["burstiness_fail"] = True
        STATS["burstiness_failures"] += 1
    else:
        result["burstiness_fail"] = False

    return result


def main():
    print("=" * 60)
    print("  voice_audit.py — Writing Style & AI-Voice Check")
    print("=" * 60)
    print()

    chapter_files = sorted(CHAPTERS_DIR.glob("*.qmd"))
    STATS["chapters_scanned"] = len(chapter_files)

    all_results = []
    has_errors = False

    for ch_path in chapter_files:
        result = audit_chapter(ch_path)
        all_results.append(result)
        STATS["chapter_details"][result["file"]] = result

        status = "PASS" if result["pass"] and not result.get("burstiness_fail") else "FAIL"
        if status == "FAIL":
            has_errors = True

        print(f"  [{status}] {result['file']}")

        if result["banned_words"]:
            for bw in result["banned_words"]:
                print(f"         Banned word: \"{bw['word']}\" x{bw['count']}")
                ERRORS.append(f"{result['file']}: banned word \"{bw['word']}\" ({bw['count']}x)")

        if result["pattern_violations"]:
            for pv in result["pattern_violations"]:
                print(f"         Pattern violation: {pv['count']}x (limit: {pv['limit']})")
                ERRORS.append(f"{result['file']}: pattern exceeded limit ({pv['count']}x)")

        print(f"         Burstiness: stdev={result['burstiness_stdev']} "
              f"({'OK' if not result.get('burstiness_fail') else 'LOW'}) "
              f"[{result['sentence_count']} sentences]")

        if result.get("burstiness_fail"):
            WARNINGS.append(f"{result['file']}: burstiness stdev {result['burstiness_stdev']} < 8.0")

    print()
    print("=" * 60)
    print(f"  Banned words found: {STATS['total_banned_words']}")
    print(f"  Pattern violations: {STATS['total_pattern_violations']}")
    print(f"  Low burstiness: {STATS['burstiness_failures']} chapters")
    print(f"  Result: {'FAIL' if has_errors else 'PASS'}")
    print("=" * 60)

    # Write JSON output
    output = {
        "script": "voice_audit",
        "exit_code": 1 if has_errors else 0,
        "chapters_scanned": STATS["chapters_scanned"],
        "total_banned_words": STATS["total_banned_words"],
        "total_pattern_violations": STATS["total_pattern_violations"],
        "burstiness_failures": STATS["burstiness_failures"],
        "chapter_details": {
            k: {
                "banned_words": v["banned_words"],
                "pattern_violations": v["pattern_violations"],
                "burstiness_stdev": v["burstiness_stdev"],
                "burstiness_fail": v.get("burstiness_fail", False),
            }
            for k, v in STATS["chapter_details"].items()
        },
        "errors": ERRORS,
        "warnings": [str(w) for w in WARNINGS],
    }
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        with open(reports_dir / "voice_audit.json", "w") as f:
            json.dump(output, f, indent=2)

    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
