OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,colors.tex cv.pdf coverletter.pdf)

CC = xelatex

$(OBJDIR)/colors.tex:
	make -C $$(pwd)/../scripts $@
	ln -s $$(pwd)/../scripts/$@ $@

$(OBJDIR)/%.pdf: %.tex $(OBJDIR)/colors.tex
	$(CC) -output-directory=$(OBJDIR) $<

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	rm -rf $(OBJDIR)
