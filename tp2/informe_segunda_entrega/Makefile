.PHONY: informe.tex caratula.sty qa.markdown cu.markdown dict.markdown comparacion.tex introduccion.tex arquitectura.tex
PANDOC = ../utils/pandoc

all: informe.tex caratula.sty qa.markdown cu.markdown dict.markdown comparacion.tex introduccion.tex arquitectura.tex
	${PANDOC} qa.markdown -o qa.tex
	${PANDOC} cu.markdown -o cu.tex
	${PANDOC} dict.markdown -o dict.tex
	pdflatex informe.tex -o informe.pdf
	pdflatex informe.tex -o informe.pdf

clean:
	rm -f informe.toc informe.aux informe.pdf informe.out informe.log qa.tex cu.tex dict.tex
