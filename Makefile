
# produce html files
*.html: *.svg
	@for g in $^; do \
		echo Creating $${g%.*}.html; \
		echo "<img src=\"$$g\"/>" > $${g%.*}.html; \
	done



# produce svg files
*.svg: *.plantuml
	@for f in $^; do  \
		echo Creating $${f%.*}.svg; \
		cat $$f | docker run --rm -i think/plantuml > $${f%.*}.svg; \
	done

# Check plantuml files timestamps
*.plantuml: 

