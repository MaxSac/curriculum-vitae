URL := "https://www.gfz-potsdam.de/fileadmin/gfz/medien_kommunikation/pics/LOGO-GFZ-de-mitFreistellungsraum_RGB_24bit_300dpi_546x390-jpg.jpg"

colors.tex: color_picker.py
	python $< --url $(URL) --build_dir $$(pwd)

clean:
	rm -rf colors.tex
