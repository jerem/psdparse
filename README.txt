psdparse 
Copyright (C) 2004-5 Toby Thain, toby@telegraphics.com.au

This utility parses and prints a description of various structures
inside an Adobe Photoshop(TM) PSD format file.
It can optionally extract raster layers to PNG files
in most Photoshop modes.

A reasonable amount of integrity checking is performed,
but corrupt images may still cause the program to give up.

Tested with PSDs created by PS 5.5, 7.0 and CS,
in Bitmap, Indexed, Grey Scale and RGB Colour modes
and 8/16 bit depths.

BUILDING

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
	
* For detailed output, use the -v option.
* To extract PNG files of raster layers, use the -pngdir=path option.
* To automatically create subdirectories when layer names include slashes,
  use the -makedirs option. Subdirectories may be arbitrarily deep.
  (e.g. "graphics/foo" will create "foo.png" in a subdirectory named "graphics").
  Without this option, slashes in filenames will be replaced by underscores (_).
  (N.B. In MPW, the directory separator is : instead of /.)

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
