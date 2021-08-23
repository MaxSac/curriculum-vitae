OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,coverletter.pdf cv.pdf)
URL := "https://www.gfz-potsdam.de/fileadmin/gfz/medien_kommunikation/pics/LOGO-GFZ-de-mitFreistellungsraum_RGB_24bit_300dpi_546x390-jpg.jpg"

all: $(OBJS)

scripts/colors.tex: scripts/color_picker.py
	make -C scripts colors.tex URL=$(URL)

$(OBJDIR)/%.pdf: content/%.tex scripts/colors.tex fonts
	xelatex -output-directory=$(OBJDIR) content/$*.tex

$(OBJDIR)/united.pdf: $(OBJS)
	pdfunite $(OBJS) $@

fonts:
	ln -s Awesome-CV/$@ $@

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	make -C scripts clean
	rm -rf $(OBJDIR) fonts
	rm scripts/colors.tex
