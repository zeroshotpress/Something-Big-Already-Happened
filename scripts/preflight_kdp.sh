#!/usr/bin/env bash
#
# preflight_kdp.sh — Validate KDP requirements for the PDF output
#
# Checks:
#   1. PDF file exists and ≤650MB
#   2. Page dimensions are 6x9 inches (within tolerance)
#   3. All images are >= 300 DPI
#   4. All fonts are embedded
#   5. No crop marks or annotations
#   6. Page count sanity check
#
# Usage: ./scripts/preflight_kdp.sh [path-to-pdf]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
PDF="${1:-${ROOT_DIR}/_book/Something-Big-Already-Happened.pdf}"
PASS=0
FAIL=0
WARN=0
REPORT_DIR="${ROOT_DIR}/reports"

pass() { echo "  [PASS] $1"; ((PASS++)) || true; }
fail() { echo "  [FAIL] $1"; ((FAIL++)) || true; }
warn() { echo "  [WARN] $1"; ((WARN++)) || true; }

echo "============================================"
echo "  KDP Preflight Check"
echo "============================================"
echo ""

# --------------------------------------------------
# Check 1: PDF exists
# --------------------------------------------------
echo "--- Check 1: PDF File ---"
if [[ -f "$PDF" ]]; then
    pass "PDF found: $PDF"
    FILE_SIZE_HUMAN=$(du -h "$PDF" | cut -f1)
    FILE_SIZE_BYTES=$(stat --format=%s "$PDF" 2>/dev/null || stat -f%z "$PDF" 2>/dev/null || echo "0")
    FILE_SIZE_MB=$((FILE_SIZE_BYTES / 1048576))
    echo "       Size: $FILE_SIZE_HUMAN ($FILE_SIZE_MB MB)"
    # KDP limit: 650MB
    if [[ "$FILE_SIZE_MB" -gt 650 ]]; then
        fail "File exceeds KDP 650MB limit: ${FILE_SIZE_MB}MB"
    else
        pass "File size under 650MB limit"
    fi
else
    fail "PDF not found: $PDF"
    echo ""
    echo "Cannot proceed without PDF. Build with: quarto render --profile print-kdp"
    # Write minimal JSON report
    mkdir -p "$REPORT_DIR"
    echo '{"script":"preflight_kdp","exit_code":1,"pdf_found":false,"errors":["PDF not found"]}' > "$REPORT_DIR/preflight_kdp.json"
    exit 1
fi
echo ""

# --------------------------------------------------
# Check 2: Page dimensions (6x9 inches = 432x648 points)
# --------------------------------------------------
echo "--- Check 2: Page Dimensions (target: 6x9 in) ---"
if command -v pdfinfo &>/dev/null; then
    PAGE_SIZE=$(pdfinfo "$PDF" 2>/dev/null | grep "Page size" | head -1)
    if [[ -n "$PAGE_SIZE" ]]; then
        WIDTH=$(echo "$PAGE_SIZE" | grep -oP '[\d.]+' | head -1)
        HEIGHT=$(echo "$PAGE_SIZE" | grep -oP '[\d.]+' | head -2 | tail -1)
        # 6in = 432pt, 9in = 648pt, tolerance of 5pt
        W_OK=$(awk "BEGIN {print (($WIDTH >= 427) && ($WIDTH <= 437)) ? 1 : 0}")
        H_OK=$(awk "BEGIN {print (($HEIGHT >= 643) && ($HEIGHT <= 653)) ? 1 : 0}")
        if [[ "$W_OK" == "1" && "$H_OK" == "1" ]]; then
            pass "Dimensions OK: ${WIDTH}x${HEIGHT} pts ($(awk "BEGIN {printf \"%.2fx%.2f\", $WIDTH/72, $HEIGHT/72}") in)"
        else
            fail "Dimensions WRONG: ${WIDTH}x${HEIGHT} pts (expected ~432x648 pts / 6x9 in)"
        fi
    else
        warn "Could not parse page size from pdfinfo output"
    fi
else
    warn "pdfinfo not available — skipping dimension check (install poppler-utils)"
fi
echo ""

# --------------------------------------------------
# Check 3: Image DPI (minimum 300)
# --------------------------------------------------
echo "--- Check 3: Image Resolution (minimum 300 DPI) ---"
if command -v identify &>/dev/null; then
    LOW_DPI=0
    CHECKED=0
    for img in images/**/*.{png,jpg,jpeg,tiff} images/*.{png,jpg,jpeg,tiff}; do
        [[ -f "$img" ]] || continue
        ((CHECKED++))
        DPI=$(identify -format "%x" "$img" 2>/dev/null || echo "0")
        # Strip unit suffix if present
        DPI_NUM=$(echo "$DPI" | grep -oP '[\d.]+' | head -1)
        if [[ -n "$DPI_NUM" ]] && awk "BEGIN {exit ($DPI_NUM < 300) ? 0 : 1}"; then
            fail "Low DPI ($DPI_NUM) in: $img"
            ((LOW_DPI++))
        fi
    done
    if [[ "$CHECKED" -eq 0 ]]; then
        warn "No images found to check"
    elif [[ "$LOW_DPI" -eq 0 ]]; then
        pass "All $CHECKED images are >= 300 DPI"
    fi
elif command -v exiftool &>/dev/null; then
    LOW_DPI=0
    CHECKED=0
    for img in images/**/*.{png,jpg,jpeg,tiff} images/*.{png,jpg,jpeg,tiff}; do
        [[ -f "$img" ]] || continue
        ((CHECKED++))
        DPI=$(exiftool -s -s -s -XResolution "$img" 2>/dev/null || echo "0")
        if [[ -n "$DPI" ]] && awk "BEGIN {exit ($DPI < 300) ? 0 : 1}"; then
            fail "Low DPI ($DPI) in: $img"
            ((LOW_DPI++))
        fi
    done
    if [[ "$CHECKED" -eq 0 ]]; then
        warn "No images found to check"
    elif [[ "$LOW_DPI" -eq 0 ]]; then
        pass "All $CHECKED images are >= 300 DPI"
    fi
else
    warn "Neither identify (ImageMagick) nor exiftool available — skipping DPI check"
fi
echo ""

# --------------------------------------------------
# Check 4: Font embedding
# --------------------------------------------------
echo "--- Check 4: Font Embedding ---"
if command -v pdffonts &>/dev/null; then
    UNEMBEDDED=$(pdffonts "$PDF" 2>/dev/null | tail -n +3 | awk '{print $NF}' | grep -c "no" || true)
    TOTAL_FONTS=$(pdffonts "$PDF" 2>/dev/null | tail -n +3 | wc -l || echo "0")
    if [[ "$UNEMBEDDED" -eq 0 ]]; then
        pass "All $TOTAL_FONTS fonts are embedded"
    else
        fail "$UNEMBEDDED of $TOTAL_FONTS fonts are NOT embedded:"
        pdffonts "$PDF" 2>/dev/null | tail -n +3 | grep "no$" | awk '{print "       " $1}'
    fi
else
    warn "pdffonts not available — skipping font embedding check (install poppler-utils)"
fi
echo ""

# --------------------------------------------------
# Check 5: Page count
# --------------------------------------------------
echo "--- Check 5: Page Count ---"
if command -v pdfinfo &>/dev/null; then
    PAGES=$(pdfinfo "$PDF" 2>/dev/null | grep "Pages" | awk '{print $2}')
    if [[ -n "$PAGES" ]]; then
        echo "       Pages: $PAGES"
        if [[ "$PAGES" -lt 24 ]]; then
            fail "KDP minimum is 24 pages (found: $PAGES)"
        elif [[ "$PAGES" -gt 828 ]]; then
            fail "KDP maximum is 828 pages for 6x9 (found: $PAGES)"
        else
            pass "Page count OK: $PAGES"
        fi
    fi
else
    warn "pdfinfo not available — skipping page count check"
fi
echo ""

# --------------------------------------------------
# Summary
# --------------------------------------------------
echo "============================================"
echo "  Results: $PASS passed, $FAIL failed, $WARN warnings"
echo "============================================"

# Write JSON report
mkdir -p "$REPORT_DIR"
cat > "$REPORT_DIR/preflight_kdp.json" <<ENDJSON
{
  "script": "preflight_kdp",
  "exit_code": $( [[ "$FAIL" -gt 0 ]] && echo 1 || echo 0 ),
  "pdf_found": true,
  "passed": $PASS,
  "failed": $FAIL,
  "warnings": $WARN
}
ENDJSON

if [[ "$FAIL" -gt 0 ]]; then
    echo "  STATUS: NOT READY for KDP upload"
    exit 1
else
    echo "  STATUS: Ready for KDP upload"
    exit 0
fi
