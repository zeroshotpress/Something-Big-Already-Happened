# Format Specifications

> Technical specifications for all output formats.
> See MASTER-PLAN.md §9 for authoritative specs.

## HTML (Web / GitHub Pages)

- Dark theme with design system colors
- Interactive charts via Quarto/Observable
- Responsive layout
- Table of contents: depth 3
- Search enabled
- Code folding enabled

## EPUB (KDP Ebook)

- Reflowable content
- Static PNG images at 300 DPI
- TOC depth: 2
- No JavaScript or interactive elements
- Must pass `epubcheck` with 0 errors

## PDF (KDP Paperback)

### Page Setup
- Paper: 6" x 9"
- Document class: `scrbook` (KOMA-Script)
- Class options: `openany`
- Engine: `lualatex`
- Font size: 11pt
- Line stretch: 1.2
- Indent: yes

### Margins
- Inner: 0.55"
- Outer: 0.45"
- Top: 0.60"
- Bottom: 0.70"

### Typography
- Main font: TeX Gyre Pagella
- Microtype enabled (kerning + character protrusion)
- xurl for safe URL line-breaking
- Club penalty: 10000 (no orphans)
- Widow penalty: 10000 (no widows)

### Images
- Format: PDF (vector) preferred, PNG at 300+ DPI
- Chart line thickness: >= 0.75pt
- No large-area background colors (ink coverage)
- Float positioning: `H` (here)

### KDP Requirements
- No crop marks or annotations
- File size <= 650MB
- All fonts embedded
- 24-828 pages for 6x9 format
- No MOBI (deprecated since 2025)

### Targets
- Page count: 190-210
- Words per page: 380-420
- Total words: 80K-85K

## Typst (Premium Edition)

- Custom template: `templates/premium.typ`
- TOC depth: 2
- Vector figures preferred
