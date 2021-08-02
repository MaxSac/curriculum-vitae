OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,cv.pdf coverletter.pdf)

CC = xelatex

cv.pdf: cv.tex
	$(CC) -output-directory=$(OBJDIR) $<

coverletter.pdf: coverletter.tex
	$(CC) -output-directory=$(OBJDIR) $<

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	rm -rf $(OBJDIR)
