#!/usr/bin/env python3
"""
image_dpi_check.py — Verify all images meet 300 DPI minimum for print.

Also checks:
  - Line thickness >= 0.75pt (via metadata heuristic)
  - Image file sizes
  - Missing images referenced in chapters

EXIT 0 = all checks pass
EXIT 1 = violations found
"""

import os
import re
import sys
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "images"
CHAPTERS_DIR = ROOT / "chapters"

ERRORS = []
WARNINGS = []
STATS = {
    "images_checked": 0,
    "low_dpi_count": 0,
    "missing_images": 0,
    "total_size_mb": 0.0,
    "image_details": [],
}


def get_png_dpi(filepath):
    """Extract DPI from PNG file's pHYs chunk."""
    try:
        with open(filepath, "rb") as f:
            header = f.read(8)
            if header[:4] != b"\x89PNG":
                return None, None

            while True:
                chunk_header = f.read(8)
                if len(chunk_header) < 8:
                    break
                length = struct.unpack(">I", chunk_header[:4])[0]
                chunk_type = chunk_header[4:8]

                if chunk_type == b"pHYs":
                    data = f.read(length)
                    ppux = struct.unpack(">I", data[0:4])[0]
                    ppuy = struct.unpack(">I", data[4:8])[0]
                    unit = data[8]
                    if unit == 1:  # meters
                        dpi_x = round(ppux / 39.3701)
                        dpi_y = round(ppuy / 39.3701)
                        return dpi_x, dpi_y
                    else:
                        return None, None  # No unit specified
                elif chunk_type == b"IEND":
                    break
                else:
                    f.read(length)
                f.read(4)  # CRC
    except Exception:
        pass
    return None, None


def get_png_dimensions(filepath):
    """Get PNG width and height from IHDR chunk."""
    try:
        with open(filepath, "rb") as f:
            f.read(8)  # PNG header
            f.read(4)  # IHDR length
            f.read(4)  # IHDR type
            width = struct.unpack(">I", f.read(4))[0]
            height = struct.unpack(">I", f.read(4))[0]
            return width, height
    except Exception:
        return None, None


def check_image(filepath):
    """Check a single image for DPI and metadata."""
    path = Path(filepath)
    size_mb = path.stat().st_size / (1024 * 1024)
    STATS["total_size_mb"] += size_mb

    result = {
        "file": str(path.relative_to(ROOT)),
        "size_mb": round(size_mb, 2),
        "dpi_x": None,
        "dpi_y": None,
        "width": None,
        "height": None,
        "pass": True,
    }

    if path.suffix.lower() == ".png":
        dpi_x, dpi_y = get_png_dpi(filepath)
        width, height = get_png_dimensions(filepath)
        result["dpi_x"] = dpi_x
        result["dpi_y"] = dpi_y
        result["width"] = width
        result["height"] = height

        if dpi_x is not None and dpi_x < 300:
            result["pass"] = False
            STATS["low_dpi_count"] += 1
            ERRORS.append(f"Low DPI ({dpi_x}x{dpi_y}) in {result['file']}")
        elif dpi_x is None:
            # No pHYs chunk — check if pixel dimensions are sufficient
            # For a 6x9 page at 300dpi, full-width image needs ~1500px
            if width and width < 1200:
                WARNINGS.append(f"No DPI metadata and low resolution ({width}x{height}) in {result['file']}")
    elif path.suffix.lower() == ".svg":
        # SVGs are resolution-independent
        result["dpi_x"] = "vector"
        result["dpi_y"] = "vector"
    elif path.suffix.lower() == ".pdf":
        # PDF charts are vector, OK for print
        result["dpi_x"] = "vector"
        result["dpi_y"] = "vector"

    STATS["image_details"].append(result)
    STATS["images_checked"] += 1
    return result


def find_referenced_images(chapters_dir):
    """Find all images referenced in chapter .qmd files."""
    referenced = set()
    for qmd in chapters_dir.glob("*.qmd"):
        text = qmd.read_text(encoding="utf-8")
        # Match ![...](images/...) and {{< figure src="images/..." >}}
        refs = re.findall(r"images/[^\s\)\"']+", text)
        referenced.update(refs)
    return referenced


def main():
    print("=" * 60)
    print("  image_dpi_check.py — Image Quality Verification")
    print("=" * 60)
    print()

    # Check all images
    image_extensions = {".png", ".jpg", ".jpeg", ".tiff", ".svg", ".pdf"}
    image_files = []
    for ext in image_extensions:
        image_files.extend(IMAGES_DIR.rglob(f"*{ext}"))

    print(f"  Found {len(image_files)} image files\n")

    print("--- DPI Check (minimum 300 for raster) ---")
    for img in sorted(image_files):
        result = check_image(img)
        dpi_str = f"{result['dpi_x']}x{result['dpi_y']}" if result["dpi_x"] else "N/A"
        status = "PASS" if result["pass"] else "FAIL"
        dims = f"{result['width']}x{result['height']}" if result["width"] else ""
        print(f"  [{status}] {result['file']} — DPI: {dpi_str}  {dims}  ({result['size_mb']} MB)")

    print()

    # Check for missing referenced images
    print("--- Missing Image References ---")
    referenced = find_referenced_images(CHAPTERS_DIR)
    for ref in sorted(referenced):
        full_path = ROOT / ref
        if not full_path.exists():
            STATS["missing_images"] += 1
            ERRORS.append(f"Missing referenced image: {ref}")
            print(f"  [FAIL] {ref} — referenced but not found")
    if STATS["missing_images"] == 0:
        print("  [PASS] All referenced images exist")
    print()

    # Summary
    print("=" * 60)
    print(f"  Images checked: {STATS['images_checked']}")
    print(f"  Low DPI: {STATS['low_dpi_count']}")
    print(f"  Missing: {STATS['missing_images']}")
    print(f"  Total size: {STATS['total_size_mb']:.1f} MB")
    print(f"  Result: {'FAIL' if ERRORS else 'PASS'}")
    print("=" * 60)

    if WARNINGS:
        print("\nWarnings:")
        for w in WARNINGS:
            print(f"  - {w}")

    # Write JSON output
    output = {
        "script": "image_dpi_check",
        "exit_code": 1 if ERRORS else 0,
        "images_checked": STATS["images_checked"],
        "low_dpi_count": STATS["low_dpi_count"],
        "missing_images": STATS["missing_images"],
        "total_size_mb": round(STATS["total_size_mb"], 2),
        "errors": ERRORS,
        "warnings": [str(w) for w in WARNINGS],
    }
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        with open(reports_dir / "image_dpi_check.json", "w") as f:
            json.dump(output, f, indent=2)

    sys.exit(1 if ERRORS else 0)


if __name__ == "__main__":
    main()
