.PHONY: all
PDFS = notas.pdf cu.pdf riegos.pdf
MD2PDF = pandoc 

all: ${PDFS}

%.pdf: %.markdown
	${MD2PDF} -o $@ $^
