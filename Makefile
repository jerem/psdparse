#    This file is part of "psdparse"
#    Copyright (C) 2004-5 Toby Thain, toby@telegraphics.com.au
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

CFLAGS = -O2 -DMAC_ENV # -I../PhotoshopAPI/Photoshop -I../PhotoshopAPI/Pica_SP

all : psdparse

clean : 
	rm -f psdparse psdparse.o

SRCARCHIVE = psdparse.zip

src : $(SRCARCHIVE)

$(SRCARCHIVE) : Makefile psdparse.c ../netpbmformats/dist/gpl.html
	zip -9 psdparse.zip $^

psdparse : psdparse.o


