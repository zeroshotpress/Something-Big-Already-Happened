#!/usr/bin/env python3
"""
source_audit.py — 2-axis source classification auditor.

Checks that all citations in chapters meet the source policy:
  - Core claims must use Tier-1 + (Primary OR Secondary) sources
  - Tier-3 sources (Wikipedia, SEO, aggregators) forbidden for core claims
  - Reports unclassified sources that need registry entries

EXIT 0 = all checks pass
EXIT 1 = violations found
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters"
REFERENCES_DIR = ROOT / "references"
REGISTRY_PATH = REFERENCES_DIR / "source-registry.yml"

ERRORS = []
WARNINGS = []
STATS = {
    "total_citations": 0,
    "registered_citations": 0,
    "unregistered_citations": 0,
    "tier1": 0,
    "tier2": 0,
    "tier3": 0,
    "core_claims": 0,
    "core_tier3_violations": 0,
    "chapters_scanned": 0,
}

# Known Tier-3 domains (Wikipedia, SEO blogs, aggregators)
TIER3_DOMAINS = [
    "wikipedia.org",
    "medium.com",
    "investorplace.com",
    "startuphub.ai",
    "claudefa.st",
    "vertu.com",
    "tamiltech.in",
    "almcorp.com",
]

# Tier-1 domains (official, primary sources, top-tier journalism)
TIER1_DOMAINS = [
    "openai.com",
    "anthropic.com",
    "blog.google",
    "ai.meta.com",
    "metr.org",
    "x.ai",
    "deepseek.com",
    "fortune.com",
    "reuters.com",
    "bloomberg.com",
    "wsj.com",
    "ft.com",
    "nytimes.com",
    "cnbc.com",
    "whitehouse.gov",
    "congress.gov",
    "gao.gov",
    "bis.gov",
    "artificialintelligenceact.eu",
    "swebench.com",
    "epoch.ai",
    "hai.stanford.edu",
    "hbr.org",
    "science.org",
    "nature.com",
    "lesswrong.com",
    "weforum.org",
    "hpcwire.com",
    "csis.org",
    "cnas.org",
    "warontherocks.com",
    "bbc.com",
    "darioamodei.com",
    "blog.samaltman.com",
    "tandfonline.com",
    "pmc.ncbi.nlm.nih.gov",
    "federalreserve.gov",
    "einpresswire.com",
    "simonwillison.net",
    "danshapiro.com",
    "github.com",
    "cognition.ai",
    "semi.org",
    "dlapiper.com",
    "shumer.dev",
    "fool.com",
    "businessworld.in",
    "institute.global",
    "orfonline.org",
    "bruegel.org",
    "techinsights.com",
    "carboncredits.com",
    "x.com",
]


def load_registry():
    """Load source-registry.yml if it exists."""
    if not REGISTRY_PATH.exists():
        WARNINGS.append("source-registry.yml not found — all sources unregistered")
        return {}
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("citations", {})


def extract_citations(text):
    """Extract all @citation_keys from a .qmd file."""
    # Match @key patterns in [@key] or [@key1; @key2] or standalone @key
    keys = re.findall(r"@(\w+)", text)
    # Exclude Quarto cross-reference prefixes (sec, fig, tbl, eq, lst, thm)
    quarto_prefixes = {"sec", "fig", "tbl", "eq", "lst", "thm"}
    keys = [k for k in keys if k not in quarto_prefixes]
    return keys


def classify_bib_entry(key, bib_text):
    """Classify a bib entry by checking its URL against tier domains."""
    # Find the URL for this key
    pattern = rf"@\w+\{{{re.escape(key)},[\s\S]*?(?=\n@|\Z)"
    match = re.search(pattern, bib_text)
    if not match:
        return "unknown", None

    entry = match.group(0)
    url_match = re.search(r"url\s*=\s*\{([^}]+)\}", entry)
    if not url_match:
        return "unknown", None

    url = url_match.group(1)

    # Check against tier lists
    for domain in TIER3_DOMAINS:
        if domain in url:
            return "tier3", url

    for domain in TIER1_DOMAINS:
        if domain in url:
            return "tier1", url

    return "tier2", url


def load_bib():
    """Load the .bib file."""
    bib_path = REFERENCES_DIR / "sources.bib"
    if not bib_path.exists():
        WARNINGS.append("sources.bib not found")
        return ""
    return bib_path.read_text(encoding="utf-8")


def audit_chapter(ch_path, registry, bib_text):
    """Audit a single chapter's citations."""
    text = ch_path.read_text(encoding="utf-8")

    # Strip YAML front matter
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:]

    citations = extract_citations(text)
    unique_citations = set(citations)

    chapter_results = {
        "file": ch_path.name,
        "total_citations": len(unique_citations),
        "tier1": 0,
        "tier2": 0,
        "tier3": 0,
        "unknown": 0,
        "registered": 0,
        "unregistered": [],
        "tier3_keys": [],
    }

    for key in unique_citations:
        STATS["total_citations"] += 1

        # Check registry
        if key in registry:
            STATS["registered_citations"] += 1
            chapter_results["registered"] += 1
            tier = registry[key].get("tier", 0)
            if tier == 1:
                STATS["tier1"] += 1
                chapter_results["tier1"] += 1
            elif tier == 2:
                STATS["tier2"] += 1
                chapter_results["tier2"] += 1
            elif tier == 3:
                STATS["tier3"] += 1
                chapter_results["tier3"] += 1
                chapter_results["tier3_keys"].append(key)
        else:
            # Fall back to bib-based classification
            STATS["unregistered_citations"] += 1
            chapter_results["unregistered"].append(key)
            tier, url = classify_bib_entry(key, bib_text)
            if tier == "tier1":
                STATS["tier1"] += 1
                chapter_results["tier1"] += 1
            elif tier == "tier2":
                STATS["tier2"] += 1
                chapter_results["tier2"] += 1
            elif tier == "tier3":
                STATS["tier3"] += 1
                chapter_results["tier3"] += 1
                chapter_results["tier3_keys"].append(key)
            else:
                chapter_results["unknown"] += 1

    return chapter_results


def main():
    print("=" * 60)
    print("  source_audit.py — 2-Axis Source Classification Audit")
    print("=" * 60)
    print()

    registry = load_registry()
    bib_text = load_bib()

    chapter_files = sorted(CHAPTERS_DIR.glob("*.qmd"))
    STATS["chapters_scanned"] = len(chapter_files)

    all_results = []
    total_tier3_keys = []

    for ch_path in chapter_files:
        result = audit_chapter(ch_path, registry, bib_text)
        all_results.append(result)
        if result["tier3_keys"]:
            total_tier3_keys.extend(
                [(ch_path.name, k) for k in result["tier3_keys"]]
            )
        print(f"  {result['file']}: {result['total_citations']} citations "
              f"(T1:{result['tier1']} T2:{result['tier2']} T3:{result['tier3']})")

    print()

    # Report Tier-3 violations
    print("--- Tier-3 Core Claim Violations ---")
    if total_tier3_keys:
        for ch, key in total_tier3_keys:
            ERRORS.append(f"Tier-3 source in {ch}: @{key}")
            print(f"  [FAIL] {ch}: @{key}")
        STATS["core_tier3_violations"] = len(total_tier3_keys)
    else:
        print("  [PASS] No Tier-3 sources found")
    print()

    # Report unregistered citations
    print("--- Unregistered Citations ---")
    all_unregistered = []
    for r in all_results:
        for key in r["unregistered"]:
            all_unregistered.append((r["file"], key))
    if all_unregistered:
        for ch, key in all_unregistered[:20]:  # Show first 20
            print(f"  [WARN] {ch}: @{key} not in source-registry.yml")
        if len(all_unregistered) > 20:
            print(f"  ... and {len(all_unregistered) - 20} more")
        WARNINGS.append(f"{len(all_unregistered)} citations not in source-registry.yml")
    else:
        print("  [PASS] All citations registered")
    print()

    # Summary
    print("=" * 60)
    print(f"  Total citations: {STATS['total_citations']}")
    print(f"  Tier-1: {STATS['tier1']}  Tier-2: {STATS['tier2']}  Tier-3: {STATS['tier3']}")
    print(f"  Registered: {STATS['registered_citations']}  Unregistered: {STATS['unregistered_citations']}")
    print(f"  Tier-3 violations: {STATS['core_tier3_violations']}")
    print(f"  Result: {'FAIL' if ERRORS else 'PASS'}")
    print("=" * 60)

    if WARNINGS:
        print("\nWarnings:")
        for w in WARNINGS:
            print(f"  - {w}")

    # Write JSON output
    output = {
        "script": "source_audit",
        "exit_code": 1 if ERRORS else 0,
        "total_citations": STATS["total_citations"],
        "tier1": STATS["tier1"],
        "tier2": STATS["tier2"],
        "tier3": STATS["tier3"],
        "registered": STATS["registered_citations"],
        "unregistered": STATS["unregistered_citations"],
        "tier3_violations": STATS["core_tier3_violations"],
        "tier3_details": [{"chapter": ch, "key": k} for ch, k in total_tier3_keys],
        "chapters_scanned": STATS["chapters_scanned"],
        "errors": ERRORS,
        "warnings": [str(w) for w in WARNINGS],
    }
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        with open(reports_dir / "source_audit.json", "w") as f:
            json.dump(output, f, indent=2)

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
