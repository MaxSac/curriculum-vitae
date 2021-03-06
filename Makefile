OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,coverletter.pdf cv.pdf united.pdf cv_attached.pdf)
URL := "https://www.gfz-potsdam.de/fileadmin/gfz/medien_kommunikation/pics/LOGO-GFZ-de-mitFreistellungsraum_RGB_24bit_300dpi_546x390-jpg.jpg"

all: $(OBJS)

scripts/colors.tex: scripts/color_picker.py
	make -C scripts colors.tex URL=$(URL)

$(OBJDIR)/%.pdf: content/%.tex scripts/colors.tex fonts
	xelatex -output-directory=$(OBJDIR) content/$*.tex

$(OBJDIR)/bachelor_zeugnis.pdf: images/bachelor_zeugnis.pdf images/bachelor_detail.pdf
	pdfunite images/bachelor_zeugnis.pdf images/bachelor_detail.pdf $(OBJDIR)/zeugnis_high_res.pdf
	gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$@ $(OBJDIR)/zeugnis_high_res.pdf

$(OBJDIR)/cv_attached.pdf: $(addprefix $(OBJDIR)/,cv.pdf bachelor_zeugnis.pdf) images/master_uebersicht.pdf
	pdfunite $(OBJDIR)/cv.pdf images/master_uebersicht.pdf $(OBJDIR)/bachelor_zeugnis.pdf $@

$(OBJDIR)/united.pdf: $(addprefix $(OBJDIR)/,coverletter.pdf cv_attached.pdf)
	pdfunite $(addprefix $(OBJDIR)/,coverletter.pdf cv_attached.pdf) $@

fonts:
	ln -s Awesome-CV/$@ $@

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	make -C scripts clean
	rm -rf $(OBJDIR) fonts
	rm scripts/colors.tex
