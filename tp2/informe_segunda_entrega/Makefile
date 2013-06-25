all: informe.tex caratula.sty qa.markdown
	pandoc qa.markdown -o qa.tex
	pdflatex informe.tex -o informe.pdf

clean:
	rm -f informe.toc informe.aux informe.pdf qa.tex informe.out informe.log 
