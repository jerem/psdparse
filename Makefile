CFLAGS = -O2 -DMAC_ENV # -I../PhotoshopAPI/Photoshop -I../PhotoshopAPI/Pica_SP

all : psdparse

clean : 
	rm -f psdparse psdparse.o

SRCARCHIVE = psdparse.zip

src : $(SRCARCHIVE)

$(SRCARCHIVE) : Makefile psdparse.c ../netpbmformats/dist/gpl.html
	zip -9 psdparse.zip $^

psdparse : psdparse.o


