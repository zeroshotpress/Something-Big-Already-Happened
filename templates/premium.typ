// ==========================================================================
// Something Big Already Happened — Premium Typst Template
// Dark-theme PDF edition with custom typography and layout
// ==========================================================================

// --- Color Palette ---
#let bg-primary = rgb("#0D0D1A")
#let bg-secondary = rgb("#1A1A2E")
#let bg-card = rgb("#16213E")
#let bg-code = rgb("#0A0A1A")
#let accent = rgb("#FF6B35")
#let accent-light = rgb("#FF9F6B")
#let accent2 = rgb("#6366F1")
#let accent2-light = rgb("#A5B4FC")
#let text-primary = rgb("#E8E8F0")
#let text-secondary = rgb("#9CA3AF")
#let text-muted = rgb("#6B7280")
#let border-color = rgb("#2D2D44")
#let success-color = rgb("#10B981")
#let warning-color = rgb("#F59E0B")
#let error-color = rgb("#EF4444")

// --- Font Definitions ---
#let font-heading = ("Playfair Display", "Georgia", "serif")
#let font-body = ("Inter", "Helvetica Neue", "sans-serif")
#let font-mono = ("JetBrains Mono", "Fira Code", "monospace")

// --- Page Setup ---
#set page(
  paper: "a4",
  margin: (
    top: 2.5cm,
    bottom: 2.5cm,
    inside: 3cm,
    outside: 2.5cm,
  ),
  fill: bg-primary,
  header: context {
    if counter(page).get().first() > 1 {
      set text(size: 8pt, fill: text-muted, font: font-mono)
      if calc.odd(counter(page).get().first()) {
        align(right)[Something Big Already Happened]
      } else {
        align(left)[Something Big Already Happened]
      }
      v(4pt)
      line(length: 100%, stroke: 0.3pt + border-color)
    }
  },
  footer: context {
    set text(size: 9pt, fill: text-muted, font: font-mono)
    let page-num = counter(page).get().first()
    if calc.odd(page-num) {
      align(right)[#page-num]
    } else {
      align(left)[#page-num]
    }
  },
)

// --- Base Typography ---
#set text(
  font: font-body,
  size: 11pt,
  fill: text-primary,
  lang: "en",
)

#set par(
  leading: 0.9em,
  first-line-indent: 0pt,
  justify: true,
)

// --- Heading Styles ---
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(3cm)
  block(width: 100%)[
    #set text(font: font-heading, size: 36pt, weight: 900, fill: white)
    #it.body
    #v(8pt)
    #line(length: 60pt, stroke: 2pt + accent)
  ]
  v(1cm)
}

#show heading.where(level: 2): it => {
  v(1.5cm)
  block(width: 100%)[
    #set text(font: font-heading, size: 22pt, weight: 700, fill: white)
    #it.body
    #v(4pt)
    #line(length: 40pt, stroke: 1.5pt + accent)
  ]
  v(0.6cm)
}

#show heading.where(level: 3): it => {
  v(1cm)
  block[
    #set text(font: font-body, size: 16pt, weight: 600, fill: accent2-light)
    #it.body
  ]
  v(0.4cm)
}

#show heading.where(level: 4): it => {
  v(0.8cm)
  block[
    #set text(font: font-body, size: 13pt, weight: 700, fill: text-primary)
    #it.body
  ]
  v(0.3cm)
}

// --- Links ---
#show link: it => {
  set text(fill: accent)
  underline(offset: 2pt, stroke: 0.5pt + accent, it)
}

// --- Inline Code ---
#show raw.where(block: false): it => {
  box(
    fill: bg-secondary,
    inset: (x: 4pt, y: 2pt),
    outset: (y: 2pt),
    radius: 3pt,
  )[
    #set text(font: font-mono, size: 0.85em, fill: accent2-light)
    #it
  ]
}

// --- Code Blocks ---
#show raw.where(block: true): it => {
  block(
    width: 100%,
    fill: bg-code,
    stroke: 0.5pt + border-color,
    radius: 6pt,
    inset: 14pt,
  )[
    #set text(font: font-mono, size: 9pt, fill: accent2-light)
    #set par(leading: 0.7em)
    #it
  ]
}

// --- Blockquotes ---
#show quote: it => {
  v(8pt)
  block(
    width: 100%,
    fill: bg-card,
    stroke: (left: 3pt + accent, rest: none),
    radius: (right: 6pt),
    inset: (left: 16pt, rest: 14pt),
  )[
    #set text(fill: text-secondary, style: "italic")
    #it.body
    #if it.attribution != none {
      v(4pt)
      set text(fill: accent, style: "normal", weight: 600, size: 9pt)
      [--- #it.attribution]
    }
  ]
  v(8pt)
}

// --- Tables ---
#set table(
  fill: (_, y) => if y == 0 { bg-card } else if calc.odd(y) { bg-secondary.lighten(5%) } else { none },
  stroke: 0.5pt + border-color,
)

#show table.cell.where(y: 0): set text(
  fill: accent,
  weight: 600,
  size: 9pt,
)

// --- Lists ---
#set list(marker: text(fill: accent)[--])
#set enum(numbering: n => text(fill: accent, weight: 600)[#n.])

// ==========================================================================
// Custom Components
// ==========================================================================

// --- Chapter Title Page ---
#let chapter-title(number: none, title: "", subtitle: none) = {
  pagebreak(weak: true)
  v(4cm)
  if number != none {
    set text(font: font-mono, size: 10pt, fill: accent, weight: 600)
    upper[Chapter #number]
    v(12pt)
  }
  block(width: 100%)[
    #set text(font: font-heading, size: 42pt, weight: 900, fill: white)
    #title
  ]
  if subtitle != none {
    v(10pt)
    set text(size: 14pt, fill: text-secondary, weight: 300)
    subtitle
  }
  v(8pt)
  line(length: 80pt, stroke: 2pt + accent)
  v(2cm)
}

// --- Stat Card ---
#let stat-card(number: "", label: "", date: none) = {
  block(
    width: 100%,
    fill: bg-card,
    stroke: (top: 2pt + accent, rest: 0.5pt + border-color),
    radius: 8pt,
    inset: 14pt,
  )[
    #align(center)[
      #set text(font: font-body, size: 28pt, weight: 900, fill: accent)
      #number
      #v(4pt)
      #set text(size: 9pt, weight: 400, fill: text-secondary)
      #label
      #if date != none {
        v(2pt)
        set text(font: font-mono, size: 7pt, fill: text-muted)
        date
      }
    ]
  ]
}

// --- Stat Grid (3 columns) ---
#let stat-grid(..cards) = {
  v(12pt)
  grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 10pt,
    ..cards
  )
  v(12pt)
}

// --- Timeline Item ---
#let timeline-item(year: "", title: "", desc: "", highlighted: false) = {
  let dot-color = if highlighted { accent } else { accent2 }
  let title-size = if highlighted { 16pt } else { 13pt }

  block(
    width: 100%,
    inset: (left: 24pt),
  )[
    #place(left + top, dx: -20pt, dy: 4pt)[
      #circle(radius: 4pt, fill: dot-color)
    ]
    #set text(font: font-mono, size: 9pt, fill: accent, weight: 600)
    #year
    #v(2pt)
    #set text(font: font-body, size: title-size, weight: 700, fill: white)
    #title
    #v(2pt)
    #set text(size: 10pt, weight: 400, fill: text-secondary)
    #desc
  ]
  v(10pt)
}

// --- Timeline Wrapper ---
#let timeline(..items) = {
  v(12pt)
  block(
    width: 100%,
    inset: (left: 8pt),
    stroke: (left: 1pt + border-color, rest: none),
  )[
    #for item in items.pos() {
      item
    }
  ]
  v(12pt)
}

// --- Callout Box ---
#let callout(title: "", body: [], variant: "info") = {
  let border = if variant == "warning" { warning-color }
    else if variant == "key-insight" { accent }
    else if variant == "success" { success-color }
    else { accent2 }

  let title-color = border

  v(8pt)
  block(
    width: 100%,
    fill: bg-card,
    stroke: (left: 3pt + border, rest: 0.5pt + border-color),
    radius: 6pt,
    inset: 14pt,
  )[
    #if title != "" {
      set text(weight: 700, fill: title-color, size: 11pt)
      title
      v(4pt)
    }
    #set text(fill: text-secondary, size: 10pt)
    #body
  ]
  v(8pt)
}

// --- Sidebar Note ---
#let sidebar-note(label: "Note", body: []) = {
  block(
    width: 100%,
    fill: bg-card,
    stroke: (left: 2pt + accent2, rest: none),
    radius: (right: 4pt),
    inset: (left: 12pt, rest: 10pt),
  )[
    #set text(font: font-mono, size: 7pt, fill: accent2-light, weight: 600)
    #upper(label)
    #v(2pt)
    #set text(font: font-body, size: 9pt, fill: text-secondary, weight: 400)
    #body
  ]
}

// --- Chart Container ---
#let chart-container(label: "", caption: none, body: []) = {
  v(12pt)
  block(
    width: 100%,
    fill: bg-secondary,
    stroke: 0.5pt + border-color,
    radius: 8pt,
    inset: 16pt,
  )[
    #if label != "" {
      set text(font: font-mono, size: 7pt, fill: accent, weight: 600)
      upper(label)
      v(8pt)
    }
    #body
    #if caption != none {
      v(8pt)
      align(right)[
        #set text(size: 8pt, fill: text-muted, style: "italic")
        #caption
      ]
    }
  ]
  v(12pt)
}

// --- Status Badge ---
#let status-badge(label: "", variant: "pending") = {
  let (bg, fg) = if variant == "confirmed" {
    (success-color.lighten(85%), success-color)
  } else if variant == "ahead" {
    (accent.lighten(85%), accent)
  } else if variant == "missed" {
    (error-color.lighten(85%), error-color)
  } else if variant == "partial" {
    (warning-color.lighten(85%), warning-color)
  } else {
    (accent2.lighten(85%), accent2)
  }

  box(
    fill: bg,
    radius: 10pt,
    inset: (x: 6pt, y: 2pt),
  )[
    #set text(size: 8pt, weight: 600, fill: fg)
    #label
  ]
}

// --- Drop Cap ---
#let drop-cap(letter, body) = {
  let cap = text(
    font: font-heading,
    size: 42pt,
    weight: 900,
    fill: accent,
  )[#letter]

  place(top + left, cap)
  h(36pt)
  body
}

// --- Section Divider ---
#let section-divider(label: none) = {
  v(1cm)
  align(center)[
    #line(length: 30%, stroke: 0.5pt + border-color)
    #if label != none {
      h(8pt)
      set text(font: font-mono, size: 8pt, fill: text-muted)
      label
      h(8pt)
    }
    #line(length: 30%, stroke: 0.5pt + border-color)
  ]
  v(1cm)
}

// --- Key Figure ---
#let key-figure(number: "", label: "", sublabel: none) = {
  v(16pt)
  align(center)[
    #set text(font: font-body, size: 48pt, weight: 900, fill: accent)
    #number
    #v(4pt)
    #set text(size: 14pt, weight: 400, fill: text-secondary)
    #label
    #if sublabel != none {
      v(2pt)
      set text(font: font-mono, size: 9pt, fill: text-muted)
      sublabel
    }
  ]
  v(16pt)
}

// ==========================================================================
// Document Entry Point (Quarto will use show rules)
// ==========================================================================

// This template is designed to be used with Quarto's Typst integration.
// Quarto will pass content through this template automatically.
// The custom components above can be used in .qmd files via Typst raw blocks.
