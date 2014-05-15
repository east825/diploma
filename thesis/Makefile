.PHONY: preview build clean

preview: build
	evince thesis.pdf

build:
	pdflatex thesis.tex
	bibtex thesis.aux
	pdflatex thesis.tex
	pdflatex thesis.tex

clean:
	rm -f *.log *.aux *.pdf *.dvi *.toc *.bbl *.out *-blx.bib *.blg *.run.xml *.fdb_latexmk
