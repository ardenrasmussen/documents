DOT_FILES = $(shell find -name "*.dot")
PNG_FILES = $(DOT_FILES:%.dot=%.png)

all: $(PNG_FILES)
	pdfmk

graphs: $(PNG_FILES)

clean:
	pdfmk -c
	rm $(PNG_FILES)

%.png: %.dot
	dot -Tpng $< -o $@
