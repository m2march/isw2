.PHONY: all clean
PDFS = notas.pdf cu.pdf riegos.pdf
TEX_MARKDOWNS = ${TEX_MARKDOWN_DIR}/dict.tex ${TEX_MARKDOWN_DIR}/riesgos.tex ${TEX_MARKDOWN_DIR}/cu.tex
PANDOC = pandoc
MD2PDF = ${PANDOC} 
TEX_MARKDOWN_DIR = ${INFORME_DIR}/markdowns
INFORME_DIR = informe
MARKDOWN_DIR = .


all: ${PDFS} ${TEX_MARKDOWNS}

%.pdf: %.markdown
	${MD2PDF} -o $@ $^

${TEX_MARKDOWN_DIR}/%.tex: ${MARKDOWN_DIR}/%.markdown
	${PANDOC} $^ -t latex -o $@


clean:
	rm -f ${PDFS}
	rm -f ${TEX_MARKDOWNS}
