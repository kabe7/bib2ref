SRCS = $(wildcard *.bib)

all: references.pdf

references.pdf: tmp.dvi
	dvipdfmx tmp.dvi -o references.pdf
	rm -rf *.aux *.tex *.out *.dvi *.blg
	open references.pdf

tmp.dvi: tmp.tex tmp.aux
	bibtex tmp.aux
	latex tmp.tex
	latex tmp.tex

tmp.aux: tmp.tex
	latex tmp

tmp.tex: makeRef.py
	python makeRef.py $(SRCS)

clean:
	rm -rf tmp.*
	rm references.pdf

