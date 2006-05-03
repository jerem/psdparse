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

#include <limits.h>

#ifndef PATH_MAX
	#define PATH_MAX FILENAME_MAX
#endif

enum{RAWDATA,RLECOMP};

/* Photoshop's mode constants */
#define ModeBitmap		 0
#define ModeGrayScale		 1
#define ModeIndexedColor 2
#define ModeRGBColor		 3
#define ModeCMYKColor		 4
#define ModeHSLColor		 5
#define ModeHSBColor		 6
#define ModeMultichannel 7
#define ModeDuotone		 8
#define ModeLabColor		 9
#define ModeGray16		10
#define ModeRGB48			11
#define ModeLab48			12
#define ModeCMYK64		13
#define ModeDeepMultichannel 14
#define ModeDuotone16		15

#define PAD2(x) (((x)+1) & -2) // same or next even
#define PAD4(x) (((x)+3) & -4) // same or next multiple of 4

#define VERBOSE if(verbose) printf
#define UNQUIET if(!quiet) printf

struct psd_header{
	char sig[4];
	short version;
	char reserved[6];
	short channels;
	long rows;
	long cols;
	short depth;
	short mode;
	// following fields are for our purposes, not actual header fields
	long colormodepos;
};
struct layer_info{
	long top;
	long left;
	long bottom;
	long right;
	short channels;
	
	// runtime data (not in file)
	long *chlengths; // array of channel lengths
};
struct blend_mode_info{
	char sig[4];
	char key[4];
	unsigned char opacity;
	unsigned char clipping;
	unsigned char flags;
	unsigned char filler;
};

struct resdesc {
	int id;
	char *str;
};

extern char *mode_names[],dirsep[];
extern int verbose,quiet,makedirs;

void fatal(char *s);
void warn(char *fmt,...);
void alwayswarn(char *fmt,...);
void *checkmalloc(long n);
long get4B(FILE *f);
short get2B(FILE *f);
void skipblock(FILE *f,char *desc);
void dumprow(unsigned char *b,int n);
int dochannel(FILE *f,struct layer_info *li,int idx,int channels,
			  int rows,int cols,int depth,long **rowpos);
void doimage(FILE *f,struct layer_info *li,char *name,int merged,int channels,
			 int rows,int cols,struct psd_header *h);
void dolayermaskinfo(FILE *f,struct psd_header *h);
char *finddesc(int id);
long doirb(FILE *f);
void doimageresources(FILE *f);

FILE* pngsetupwrite(FILE *psd, char *dir, char *name, int width, int height, 
					int channels, int color_type, int alphalast, struct psd_header *h);
void pngwriteimage(FILE *psd, int comp[], long **rowpos,
				   int startchan, int pngchan, int rows, int cols, int depth);

int unpackbits(unsigned char *outp,unsigned char *inp,int rowbytes,int inlen);

#ifdef WIN32
	#include <direct.h>
	#define MKDIR(name,mode) _mkdir(name) // laughable, isn't it.
#else
	#include <sys/stat.h>
	#define MKDIR mkdir
#endif

#ifdef macintosh
	int mkdir(char *s,int mode);
#endif
