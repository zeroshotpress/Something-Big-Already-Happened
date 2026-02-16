.PHONY: all charts html epub pdf-latex pdf-typst clean preflight serve

all: charts html epub pdf-latex pdf-typst

charts:
	python scripts/generate_charts.py

html: charts
	quarto render --to html

epub: charts
	quarto render --to epub

pdf-latex: charts
	quarto render --to pdf

pdf-typst: charts
	quarto render --to typst

clean:
	rm -rf _book _freeze .quarto

preflight: pdf-latex
	bash scripts/preflight_kdp.sh

serve:
	quarto preview
