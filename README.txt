psdparse 
Copyright (C) 2004-5 Toby Thain, toby@telegraphics.com.au

This utility parses and prints a description of various structures
inside an Adobe Photoshop(TM) PSD format file.
It could be extended in order to extract layers, metadata and other parts
of PSD images. Tested with PSDs created by PS 5.5 and PS 7.0.

BUILDING

To build, simply type "make" in the source directory. 
A UNIX or UNIX-compatible environment is required (e.g. Linux or OS X).

OS X users: the Developer Tools must be installed 
(see the CDs that came with your Mac, or download from 
http://developer.apple.com/tools/download/).

Windows users: use Cygwin http://cygwin.com/, MinGW http://mingw.org/,
or upgrade to Linux.

USING

To use the utility, run it giving the path name of the PSD file 
you want to inspect:
	./psdparse filename

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
