OBJDIR := build
OBJS := $(OBJDIR)/colors.tex

URL := "https://www.gfz-potsdam.de/fileadmin/gfz/medien_kommunikation/pics/LOGO-GFZ-de-mitFreistellungsraum_RGB_24bit_300dpi_546x390-jpg.jpg"

$(OBJDIR)/colors.tex: color_picker.py
	python $< --url $(URL)

OBJDIR: | $(OBJS)
	mkdir -p $(OBJDIR)

clean:
	rm -rf $(OBJDIR)
