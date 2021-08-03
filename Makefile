OBJDIR := build
OBJS := $(addprefix $(OBJDIR)/,cv.pdf coverletter.pdf)

CC = xelatex

all: $(OBJS)

fonts:
	ln -s Awesome-CV/fonts .

scripts/colors.tex:
	make -C scripts colors.tex

$(OBJDIR)/%.pdf: content/%.tex scripts/colors.tex fonts
	$(CC) -output-directory=$(OBJDIR) content/$*.tex

$(OBJS): | $(OBJDIR)

$(OBJDIR):
	mkdir $(OBJDIR)

clean:
	make -C scripts clean
	rm -rf $(OBJDIR) fonts
