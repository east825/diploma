TARGET?=	thesis
BIBFILE?=	thesis.bib
NOMFILE?=	thesis.nlo

TARGETFILES?=	preamble.tex \
		settings.tex \
		title.tex \
		abstract.tex \
		introduction.tex \
		chapter01.tex \
		chapter02.tex \
		chapter03.tex \
		chapter04.tex \
		chapter05.tex \
		conclusion.tex \
		appendix01.tex \
		appendix02.tex \
		appendix03.tex

PDF_VIEWER=	evince

default: pdf

preview-pdf: default
	$(PDF_VIEWER) $(TARGET).pdf

track-pdf: 
	latexmk -pdf -pvc $(TARGET)
	# $(PDF_VIEWER) $(TARGET).pdf

slides:	slides.tex
	$(PDFLATEX) slides.tex
	

include include/latex.mk
