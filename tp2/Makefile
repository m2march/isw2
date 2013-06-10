.PHONY: all clean
PDFS = notas.pdf cu.pdf riegos.pdf
TEX_MARKDOWNS = ${TEX_MARKDOWN_DIR}/dict.tex ${TEX_MARKDOWN_DIR}/riesgos.tex ${TEX_MARKDOWN_DIR}/cu.tex
PANDOC = pandoc
MD2PDF = ${PANDOC} 
TEX_MARKDOWN_DIR = ${INFORME_DIR}/markdowns
INFORME_DIR = informe
MARKDOWN_DIR = .
INFORME = ${INFORME_DIR}/informe.pdf
INFORME_DEPS = ${INFORME_DIR}/iterplan.tex ${INFORME_DIR}/wbs.tex ${INFORME_DIR}/gantt.tex ${ITEX_MARKDOWNS} 


all: ${TEX_MARKDOWNS} ${INFORME}

pdfs: ${PDFS}

informe: 
	cd ${INFORME_DIR}; 	pdflatex informe.tex

${INFORME_DIR}/informe.pdf: ${INFORME_DIR}/informe.tex ${INFORME_DEPS}
	cd ${INFORME_DIR}; 	pdflatex informe.tex

%.pdf: %.markdown
	${MD2PDF} -o $@ $^

${TEX_MARKDOWN_DIR}/%.tex: ${MARKDOWN_DIR}/%.markdown
	${PANDOC} $^ -t latex -o $@


clean:
	rm -f ${PDFS}
	rm -f ${TEX_MARKDOWNS}
	rm -f ${INFORME}
