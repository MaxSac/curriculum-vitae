OBJDIR := build
OBJS := cv.pdf coverletter.pdf

all: $(OBJS)

cv.pdf:
	make -C content $(OBJDIR)/$@

coverletter.pdf:
	make -C content $(OBJDIR)/$@

clean:
	make -C scripts clean
	make -C content clean
