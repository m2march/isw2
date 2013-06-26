all: informe.tex caratula.sty qa.markdown cu.markdown comparacion.tex introduccion.tex arquitectura.tex
	pandoc qa.markdown -o qa.tex
	pandoc cu.markdown -o cu.tex
	pdflatex informe.tex -o informe.pdf

clean:
	rm -f informe.toc informe.aux informe.pdf informe.out informe.log qa.tex cu.tex
