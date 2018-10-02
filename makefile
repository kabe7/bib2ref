SRCS = $(wildcard *.bib)

all: references.pdf

references.pdf: tmp.dvi
	dvipdfmx tmp.dvi -o references.pdf
	rm -rf tmp.*
	open references.pdf

tmp.dvi: tmp.tex tmp.aux
	bibtex tmp.aux
	platex tmp.tex
	platex tmp.tex

tmp.aux: tmp.tex
	platex tmp

tmp.tex: makeRef.py
	python makeRef.py $(SRCS)

clean:
	rm -rf tmp.*
	rm references.pdf

