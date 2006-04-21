psdparse 
Copyright (C) 2004-6 Toby Thain, toby@telegraphics.com.au

This utility parses and prints a description of various structures
inside an Adobe Photoshop(TM) PSD format file.
It can optionally extract raster layers and spot/alpha channels to PNG files.

A reasonable amount of integrity checking is performed. Corrupt images may
still cause the program to give up, but it is usually much more robust
than Photoshop when dealing with damaged files: It is unlikely to crash,
and it recovers a more complete image.

Tested with PSDs created by PS 3.0, 5.5, 7.0, CS and CS2,
in Bitmap, Indexed, Grey Scale, CMYK and RGB Colour modes
and 8/16 bit depths, with up to 53 alpha channels.

This software uses zlib which is (C) Jean-loup Gailly and Mark Adler.

BUILDING

Prerequisites:
* zlib (usually preinstalled on Linux or OS X)
  Download via http://www.zlib.net/
  Extract alongside psdparse directory, see Makefile
* libpng
  Download via http://www.libpng.org/pub/png/libpng.html
  On OS X or Win32 (MinGW tools), Makefile statically links.
  Extract alongside psdparse directory.

If your system has these libraries as shared library packages,
you can use those with appropriate changes to the Makefile.

To build on a UNIX or UNIX compatible system, simply type "make" 
in the source directory. 

Mac OS X users: the Developer Tools must be installed 
(see the CDs that came with your Mac, or download from 
http://developer.apple.com/tools/download/).

MPW (Mac OS 7,8,9,Classic) users:
An MPW makefile is provided. Simply Build Program "psdparse".

Windows users: use Cygwin http://cygwin.com/, MinGW http://mingw.org/,
or upgrade to Linux. Alternatively, the code can probably be built 
with a freely downloadable toolset such as:
* http://www.borland.com/products/downloads/download_cbuilder.html
* http://www.openwatcom.org/download/download_licenses.html
* http://www.digitalmars.com/download/dmcpp.html

USING

To use the utility, run it giving the path name of the PSD file 
you want to inspect:
	./psdparse filename

* For a guide to options, './psdparse --help'
* For detailed output, use the --verbose option.
* To extract PNG files of raster layers, use the --writepng option.
* To specify a destination directory for PNGs, use the --pngdir=path option.
  (By default, a directory is created next to the source file, with '_png' appended.)
* To automatically create subdirectories when layer names include slashes,
  use the --makedirs option. 
  (e.g. "graphics/foo" will create "foo.png" in a subdirectory named "graphics").
  Without this option, slashes in filenames will be replaced by underscores (_).
  (N.B. In MPW, the directory separator is : instead of /.)
  Subdirectories may be arbitrarily deep.
* To write a text file describing layers, sizes and positions (list.txt),
  use option --list. This file is put in the same directory as PNGs.
* Normally, RGB images (and grey scale+alpha images) are written as composite
  PNG with channels combined in one file. To write individual PNG files
  for each channel, regardless of mode, use the --split option.

LICENSE

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
