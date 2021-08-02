OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,cv.pdf coverletter.pdf)
URL := "https://www.gfz-potsdam.de/fileadmin/gfz/medien_kommunikation/pics/LOGO-GFZ-de-mitFreistellungsraum_RGB_24bit_300dpi_546x390-jpg.jpg"

CC = xelatex

cv.pdf: cv.tex $(OBJDIR)/colors.tex
	$(CC) -output-directory=$(OBJDIR) $<

coverletter.pdf: coverletter.tex $(OBJDIR)/colors.tex
	$(CC) -output-directory=$(OBJDIR) $<

$(OBJDIR)/colors.tex: color_picker.py
	python color_picker.py --url $(URL)

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	rm -rf $(OBJDIR)
