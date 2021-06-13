OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,cv.pdf coverletter.pdf)

CC = xelatex
CV_DIR = cv
CV_SRCS = $(shell find $(CV_DIR) -name '*.tex')

cv.pdf: cv.tex $(CV_SRCS)
	$(CC) -output-directory=$(OBJDIR) $<

coverletter.pdf: coverletter.tex
	$(CC) -output-directory=$(OBJDIR) $<

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	rm -rf $(OBJDIR)
