# This file is part of "psdparse"
# Copyright (C) 2004-6 Toby Thain, toby@telegraphics.com.au

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License  
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

PNGDIR = ::libpng-1.2.8:
PNGOBJ = ¶
	{PNGDIR}png.c.x {PNGDIR}pngerror.c.x {PNGDIR}pnggccrd.c.x {PNGDIR}pngget.c.x ¶
	{PNGDIR}pngmem.c.x {PNGDIR}pngpread.c.x {PNGDIR}pngread.c.x {PNGDIR}pngrio.c.x ¶
	{PNGDIR}pngrtran.c.x {PNGDIR}pngrutil.c.x {PNGDIR}pngset.c.x {PNGDIR}pngtest.c.x ¶
	{PNGDIR}pngtrans.c.x {PNGDIR}pngvcrd.c.x {PNGDIR}pngwio.c.x {PNGDIR}pngwrite.c.x ¶
	{PNGDIR}pngwtran.c.x {PNGDIR}pngwutil.c.x 

ZLIBDIR = ::zlib-1.2.2:
ZLIBOBJ = ¶
	{ZLIBDIR}adler32.c.x {ZLIBDIR}compress.c.x {ZLIBDIR}crc32.c.x ¶
	{ZLIBDIR}deflate.c.x {ZLIBDIR}example.c.x {ZLIBDIR}gzio.c.x {ZLIBDIR}infback.c.x ¶
	{ZLIBDIR}inffast.c.x {ZLIBDIR}inflate.c.x {ZLIBDIR}inftrees.c.x ¶
	{ZLIBDIR}trees.c.x {ZLIBDIR}uncompr.c.x {ZLIBDIR}zutil.c.x

OBJ =	main.c.x writepng.c.x unpackbits.c.x mkdir_unimpl.c.x {PNGOBJ} {ZLIBOBJ}

LIB =	"{SharedLibraries}InterfaceLib" ¶
		"{SharedLibraries}StdCLib" ¶
		"{SharedLibraries}MathLib" ¶
		"{PPCLibraries}StdCRuntime.o" ¶
		"{PPCLibraries}PPCCRuntime.o" ¶
		"{PPCLibraries}PPCToolLibs.o"

# "-enum int -d STDC" are needed to make zlib build happily
CFLAGS = -enum int -i {PNGDIR},{ZLIBDIR} -w 2 ¶
	-d STDC -d MAC_ENV -d DEFAULT_VERBOSE=0 -d DIRSEP=¶':¶'

.c.x  Ä  .c
	{PPCC} {depDir}{default}.c -o {targDir}{default}.c.x {CFLAGS}

psdparse  ÄÄ  {OBJ} {LIB}
	PPCLink -o {Targ} {OBJ} {LIB} -d -t 'MPST' -c 'MPS '
