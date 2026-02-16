# Something Big Already Happened

**Tracking the AI Predictions That Came True**

A living, evidence-first narrative tracking how AI predictions convert into measurable reality --- month by month --- using 229 primary sources, reproducible data, and falsifiable scorecards.

## Author

**S.H. Ash**

## Formats

- **Web edition:** [zeroshotpress.github.io/Something-Big-Already-Happened](https://zeroshotpress.github.io/Something-Big-Already-Happened/)
- **EPUB:** Included in repository (`Something-Big-Already-Happened.epub`)
- **PDF:** Available in `docs/Something-Big-Already-Happened.pdf`

## Building

This project uses [Quarto](https://quarto.org/).

```bash
# Web edition
quarto render --profile web

# EPUB
quarto render --profile ebook

# Print-ready PDF (KDP)
quarto render --profile print-kdp
```

## Quality Gates

```bash
python scripts/verify_counts.py      # CSV↔prose sync
python scripts/source_audit.py       # Citation enforcement
python scripts/voice_audit.py        # Banned words + burstiness
python scripts/image_dpi_check.py    # 300 DPI check
python scripts/quote_audit.py        # Quote length limits
bash scripts/preflight_kdp.sh        # KDP file hygiene
```

## Contact

- **Email:** SomethingBigAlreadyHappened@zeroshotpress.com
- **Source:** [github.com/zeroshotpress/Something-Big-Already-Happened](https://github.com/zeroshotpress/Something-Big-Already-Happened)

## License

Text content © 2026 S.H. Ash. All rights reserved.
Code, data, and scripts are released under the MIT License. See [LICENSE](LICENSE) for details.
