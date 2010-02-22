Original name: psdparse 
Original author: Copyright (C) 2004-6 Toby Thain, toby@telegraphics.com.au

Forked in pure Python with the name of "psdparser"
Copyright (C) 2008-10 Jérémy Bethmont, jeremy.bethmont@gmail.com

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