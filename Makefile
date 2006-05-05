#    This file is part of "psdparse"
#    Copyright (C) 2004-6 Toby Thain, toby@telegraphics.com.au
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License  
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# This program uses libpng, which in turn uses zlib.
# - on most Linux/UNIX systems, these are shared libraries preinstalled
#   or easily installed with a package manager.
# - on Windows, this makefile is set up to build them from source with MinGW
#   and static link.
# - on OS X, zlib is standard but libpng is not (unless you use a package
#   manager like Fink, http://fink.sourceforge.net/), so we build it ourselves
#   and static link to it.

# for OS X build, download and extract libpng archive, and define path to it:
PNGDIR = ../libpng-1.2.8
# (libpng can be downloaded via http://www.libpng.org/pub/png/libpng.html)

# The following line is only needed where libpng is typically not installed (OS X).
# Otherwise, this line should be commented out (and shared lib will be used):
#LIBPNGA = $(PNGDIR)/libpng.a

# if building with MinGW ('make exe'), extract zlib and libpng to these directories:
ZLIBDIRW32 = ../zlib-1.2.3_w32
PNGDIRW32  = ../libpng-1.2.8_w32
# (zlib can be downloaded via http://www.zlib.net/)

# define MinGW tools
MINGW_CC      = i386-mingw32msvc-gcc
MINGW_AR      = i386-mingw32msvc-ar
MINGW_RANLIB  = i386-mingw32msvc-ranlib
MINGW_WINDRES = i386-mingw32msvc-windres

CFLAGS   += -W -Wall -O2 -g
CPPFLAGS += -DDEFAULT_VERBOSE=0

SRC    = main.c writepng.c unpackbits.c constants.c
OBJ    = $(patsubst %.c, obj/%.o, $(SRC) )
OBJW32 = $(patsubst %.c, obj_w32/%.o, $(SRC) ) obj_w32/res.o

obj/%.o     : %.c ; $(CC)       -o $@ -c $< $(CFLAGS) $(CPPFLAGS)
obj_w32/%.o : %.c ; $(MINGW_CC) -o $@ -c $< $(CFLAGS) $(CPPFLAGS)

.PHONY : all clean test exe dist

all : psdparse

clean : ; rm -f psdparse psdparse.exe $(OBJ) $(OBJW32)

# fuzz testing. depends on 'garble' tool, 
# see http://www.telegraphics.com.au/svn/garble/trunk/
# supply your own orig.psd
test : orig.psd ../garble/garble
	cp orig.psd test.psd; \
	for (( i=1 ; i<20 ; ++i )) ; do \
		./psdparse -w -d _pass$$i test.psd; \
		../garble/garble test.psd 100; \
	done

psdparse : CPPFLAGS += -DDIRSEP="'/'" -I$(PNGDIR)
psdparse : $(OBJ) $(LIBPNGA)
	$(CC) -o $@ $(filter-out %.a,$^) -L$(PNGDIR) -lz -lpng

# Win32 EXE built by MinGW
# psdparse.exe - standard CLI tool
# psd2png.exe  - variant intended for drag'n'drop, that always writes PNGs and asset list
exe : psdparse.exe psd2png.exe

W32FLAGS = -DDIRSEP="'\\\\'" -I$(PNGDIRW32) -I$(ZLIBDIRW32)

psdparse.exe : CPPFLAGS += $(W32FLAGS)
psd2png.exe  : CPPFLAGS += $(W32FLAGS) -DALWAYS_WRITE_PNG 

psdparse.exe : $(ZLIBDIRW32)/libz.a $(PNGDIRW32)/libpng.a $(OBJW32)
	$(MINGW_CC) -s -o $@ $(filter-out %.a,$^) -L$(ZLIBDIRW32) -L$(PNGDIRW32) -lpng -lz
psd2png.exe : $(ZLIBDIRW32)/libz.a $(PNGDIRW32)/libpng.a \
			  $(subst main.o,main_psd2png.o,$(OBJW32))
	$(MINGW_CC) -s -o $@ $(filter-out %.a,$^) -L$(ZLIBDIRW32) -L$(PNGDIRW32) -lpng -lz

obj_w32/main_psd2png.o : main.c ; $(MINGW_CC) -o $@ -c $< $(CFLAGS) $(CPPFLAGS)

obj_w32/res.o : version.rc version.h ; $(MINGW_WINDRES) -o $@ -i $<

dist : psdparse-win.zip

psdparse-win.zip : README.txt gpl.html psdparse.exe psd2png.exe
	zip -9 $@ $^

# rule to build libpng

$(PNGDIR)/libpng.a : $(PNGDIR)/scripts/makefile.darwin
	cd $(PNGDIR) && $(MAKE) -f scripts/makefile.darwin libpng.a

# rules to build Win32 libraries

$(PNGDIRW32)/libpng.a : $(PNGDIRW32)/scripts/makefile.gcc
	cd $(PNGDIRW32); \
	$(MAKE) CC=$(MINGW_CC) CPPFLAGS="-I$(ZLIBDIRW32)" AR="$(MINGW_AR) rcs" RANLIB=$(MINGW_RANLIB) \
		-f scripts/makefile.gcc libpng.a

$(ZLIBDIRW32)/libz.a : $(ZLIBDIRW32)/configure
	cd $(ZLIBDIRW32); \
	CC=$(MINGW_CC) AR="$(MINGW_AR) rcs" RANLIB=$(MINGW_RANLIB) ./configure; \
	$(MAKE) libz.a

