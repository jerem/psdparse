/*
    This file is part of "psdparse"
    Copyright (C) 2004-6 Toby Thain, toby@telegraphics.com.au

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by  
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License  
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

/* version history:
  15-Oct-2004: 0.1 commenced
  19-Oct-2004: 0.1b1 released
  26-Mar-2005: 1.0b1 significant bugs in layer handling fixed
  01-Apr-2005: began code to create PNGs of layers
  05-Apr-2005: 1.1 last version of dump-only tool
  05-Apr-2005: 1.2 merge PNG extraction code
  10-Apr-2005: 1.3b1 ported to Win32 console app
  17-Apr-2006: 1.4b1 many cleanups
  20-Apr-2006: 1.5b1,2 improve handling of extra channels, uncommon modes, and corrupt files
  02-May-2006: 1.6b1 add ability to skip channels if data format error
*/
#define VERSION_STR "1.6b1"
#define VERSION_NUM 1,0x60,beta,1
#define VERS_RSRC \
	VERSION_NUM,\
	verAustralia,\
	VERSION_STR,\
	VERSION_STR ", Copyright (C) Toby Thain 2004-6 http://www.telegraphics.com.au/" 

/* formatted for Win32 VERSIONINFO resource */
#define VI_VERS_NUM 1,6,0,1
#define VI_FLAGS	VS_FF_PRERELEASE /* 0 for final, or any of VS_FF_DEBUG,VS_FF_PATCHED,VS_FF_PRERELEASE,VS_FF_PRIVATEBUILD,VS_FF_SPECIALBUILD */
#define VI_COMMENTS	"Beta.\r\n\r\nPlease contact support@telegraphics.com.au with any bug reports, suggestions or comments.\0"	/* null terminated Comments field */

/* wildcard signature in resources */
#define ANY '    '
