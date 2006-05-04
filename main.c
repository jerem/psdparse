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

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>

#include "psdparse.h"

#include "png.h"

enum{ 
	CONTEXTROWS = 3, 
	WARNLIMIT = 10
};

#define DIRSUFFIX "_png"

static struct resdesc rdesc[] = {
	{1000,"PS2.0 mode data"},
	{1001,"Macintosh print record"},
	{1003,"PS2.0 indexed color table"},
	{1005,"ResolutionInfo"},
	{1006,"Names of the alpha channels"},
	{1007,"DisplayInfo"},
	{1008,"Caption"},
	{1009,"Border information"},
	{1010,"Background color"},
	{1011,"Print flags"},
	{1012,"Grayscale/multichannel halftoning info"},
	{1013,"Color halftoning info"},
	{1014,"Duotone halftoning info"},
	{1015,"Grayscale/multichannel transfer function"},
	{1016,"Color transfer functions"},
	{1017,"Duotone transfer functions"},
	{1018,"Duotone image info"},
	{1019,"B&W values for the dot range"},
	{1021,"EPS options"},
	{1022,"Quick Mask info"},
	{1024,"Layer state info"},
	{1025,"Working path"},
	{1026,"Layers group info"},
	{1028,"IPTC-NAA record (File Info)"},
	{1029,"Image mode for raw format files"},
	{1030,"JPEG quality"},
	{1032,"Grid and guides info"},
	{1033,"Thumbnail resource"},
	{1034,"Copyright flag"},
	{1035,"URL"},
	{1036,"Thumbnail resource"},
	{1037,"Global Angle"},
	{1038,"Color samplers resource"},
	{1039,"ICC Profile"},
	{1040,"Watermark"},
	{1041,"ICC Untagged"},
	{1042,"Effects visible"},
	{1043,"Spot Halftone"},
	{1044,"Document specific IDs"},
	{1045,"Unicode Alpha Names"},
	{1046,"Indexed Color Table Count"},
	{1047,"Transparent Index"},
	{1049,"Global Altitude"},
	{1050,"Slices"},
	{1051,"Workflow URL"},
	{1052,"Jump To XPEP"},
	{1053,"Alpha Identifiers"},
	{1054,"URL List"},
	{1057,"Version Info"},
	{2999,"Name of clipping path"},
	{10000,"Print flags info"},
	{0,NULL}
};

char *mode_names[]={
	"Bitmap", "GrayScale", "IndexedColor", "RGBColor",
	"CMYKColor", "HSLColor", "HSBColor", "Multichannel",
	"Duotone", "LabColor", "Gray16", "RGB48",
	"Lab48", "CMYK64", "DeepMultichannel", "Duotone16"
};
char *channelsuffixes[]={
	"", "", "", "RGB",
	"CMYK", "HSL", "HSB", "",
	"", "Lab", "", "RGB",
	"Lab", "CMYK", "", ""
};

char dirsep[]={DIRSEP,0};
int verbose = DEFAULT_VERBOSE,quiet = 0,makedirs = 0;

static int mergedalpha = 0,help = 0,splitchannels = 0;
static char indir[PATH_MAX],*pngdir = indir;
static FILE *listfile = NULL;
#ifdef ALWAYS_WRITE_PNG
	// for the Windows console app, we want to be able to drag and drop a PSD
	// giving us no way to specify a destination directory, so use a default
	static int writepng = 1,writelist = 1;
#else
	static int writepng = 0,writelist = 0;
#endif

void fatal(char *s){
	fflush(stdout);
	fputs(s,stderr);
	exit(EXIT_FAILURE);
}

static int nwarns = 0;

void warn(char *fmt,...){
	char s[0x200];
	va_list v;

	if(nwarns == WARNLIMIT) fputs("#   (further warnings suppressed)\n",stderr);
	++nwarns;
	if(nwarns <= WARNLIMIT){
		va_start(v,fmt);
		vsnprintf(s,0x200,fmt,v);
		va_end(v);
		fflush(stdout);
		fprintf(stderr,"#   warning: %s\n",s);
	}
}

void alwayswarn(char *fmt,...){
	char s[0x200];
	va_list v;

	va_start(v,fmt);
	vsnprintf(s,0x200,fmt,v);
	va_end(v);
	fflush(stdout);
	fputs(s,stderr);
}

void *checkmalloc(long n){
	void *p = malloc(n);
	if(p) return p;
	else fatal("can't get memory");
	return NULL;
}

long get4B(FILE *f){
	long n = fgetc(f)<<24;
	n |= fgetc(f)<<16;
	n |= fgetc(f)<<8;
	return n | fgetc(f);
}

short get2B(FILE *f){
	short n = fgetc(f)<<8;
	return n | fgetc(f);
}

void skipblock(FILE *f,char *desc){
	long n = get4B(f);
	if(n){
		fseek(f,n,SEEK_CUR);
		VERBOSE("  ...skipped %s (%ld bytes)\n",desc,n);
	}else
		VERBOSE("  (%s is empty)\n",desc);
}

void dumprow(unsigned char *b,int n){
	int k,m = n>25 ? 25 : n;
	for(k=0;k<m;++k) 
		VERBOSE("%02x",b[k]);
	if(n>m) VERBOSE(" ...%d more",n-m);
	VERBOSE("\n");
}

int dochannel(FILE *f, struct layer_info *li, int idx, int channels,
			  int rows, int cols, int depth, long **rowpos){
	int j,k,ch,dumpit,comp;
	long pos,chpos = ftell(f);
	unsigned char *rowbuf;
	unsigned rb,n,*rlebuf = NULL;
	static char *comptype[] = {"raw","RLE"};
	long chlen = li ? li->chlengths[idx] : 0;

	if(li){
		VERBOSE(">>> dochannel %d/%d filepos=%7ld bytes=%7ld\n",idx,channels,chpos,li->chlengths[idx]);
	}else{
		VERBOSE(">>> dochannel %d/%d filepos=%7ld\n",idx,channels,chpos);
	}

	if(li && chlen < 2){
		alwayswarn("## channel too short (%d bytes)\n",chlen);
		if(chlen > 0)
			fseek(f, chlen, SEEK_CUR); // skip it anyway, but not backwards
	}

	comp = get2B(f);
	chlen -= 2;
	if(comp < RAWDATA || comp > RLECOMP){
		alwayswarn("## bad compression type %d, can't process channel\n",comp);
		if(li){
			alwayswarn("## skipping rest of channel data (%d bytes)\n",chlen);
			fseek(f, chlen, SEEK_CUR);
		}else 
			fatal("## occurred in merged image, must abort\n");
		return comp;
	}
	VERBOSE("    compression = %d (%s)\n",comp,comptype[comp]);

	rb = (cols*depth + 7)/8;
	VERBOSE("    uncompressed size %ld bytes (row bytes = %d)\n",(long)channels*rows*rb,rb);

	rowbuf = checkmalloc(rb*2); /* slop for worst case RLE overhead (usually (rb/127+1) ) */
	pos = ftell(f);

	if(comp == RLECOMP){
		int rlecounts = 2*channels*rows;
		if(li && chlen < rlecounts)
			alwayswarn("## channel too short for RLE row counts (need %d bytes, have %d bytes)\n",rlecounts,chlen);
			
		pos += rlecounts; /* image data starts after RLE counts */
		rlebuf = checkmalloc(channels*rows*sizeof(unsigned));
		/* accumulate RLE counts, to make array of row start positions */
		for( ch = k = 0 ; ch < channels ; ++ch ){
			for( j = 0 ; j < rows && !feof(f) ; ++j, ++k ){
				rlebuf[k] = (unsigned short)get2B(f);
				//printf("rowpos[%d][%3d]=%6d\n",ch,j,pos);
				if(rowpos) rowpos[ch][j] = pos;
				pos += rlebuf[k];
			}
			if(rowpos) rowpos[ch][j] = pos; /* = end of last row */
			if(j < rows) fatal("# couldn't read RLE counts");
		}
	}else if(rowpos){
		/* make array of row start positions (uncompressed; each row is rb bytes) */
		for(ch=0;ch<channels;++ch){
			for(j=0;j<rows;++j){
				rowpos[ch][j] = pos;
				pos += rb;
			}
			rowpos[ch][j] = pos; /* = end of last row */
		}
	}

	for(ch = k = 0 ; ch < channels ; ++ch){
		VERBOSE(">>>   ... %d/%d, filepos= %ld\n",ch,channels,ftell(f));
		
		if(channels>1) VERBOSE("\n    channel %d:\n",ch);

		for( j = 0 ; j < rows ; ++j ){
			if(rows > 3*CONTEXTROWS){
				if(j==rows-CONTEXTROWS) 
					VERBOSE("    ...%d rows not shown...\n",rows-2*CONTEXTROWS);
				dumpit = j<CONTEXTROWS || j>=rows-CONTEXTROWS;
			}else 
				dumpit = 1;

			if(comp == RLECOMP){
				n = rlebuf[k++];
				//VERBOSE("rle count[%5d] = %5d\n",j,n);
				if(n > 2*rb){
					warn("bad RLE count %5d @ row %5d",n,j);
					n = 2*rb;
				}
				if(fread(rowbuf,1,n,f) == n){
					if(dumpit){
						VERBOSE("   %5d: <%5d> ",j,n);
						dumprow(rowbuf,n);
					}
				}else{
					memset(rowbuf,0,n);
					warn("couldn't read RLE row!");
				}
			}
			else if(comp == RAWDATA){
				if(fread(rowbuf,1,rb,f) == rb){
					if(dumpit){
						VERBOSE("   %5d: ",j);
						dumprow(rowbuf,rb);
					}
				}else{
					memset(rowbuf,0,rb);
					warn("couldn't read raw row!");
				}
			}

		}

	}
	
	if(li && ftell(f) != (chpos+2+chlen)){
		alwayswarn("### currentpos = %ld, should be %ld !!\n",ftell(f),chpos+2+chlen);
		fseek(f,chpos+2+chlen,SEEK_SET);
	}

	if(comp == RLECOMP) free(rlebuf);
	free(rowbuf);

	return comp;
}

#define BITSTR(f) ((f) ? "(1)" : "(0)")

void writechannels(FILE *f, char *dir, char *name, int chcomp[], long **rowpos, 
				   int startchan, int channels, int alphalast, int rows, int cols, struct psd_header *h){
	char pngname[FILENAME_MAX];
	int i,ch;
	FILE *png;

	for( i = 0 ; i < channels ; ++i ){
		// build PNG file name
		strcpy(pngname,name);
		ch = startchan + i - !alphalast;
		if(ch == -1)
			strcat(pngname,".alpha");
		else if(ch < strlen(channelsuffixes[h->mode]))
			sprintf(pngname+strlen(pngname),".%c",channelsuffixes[h->mode][ch]);
		else
			sprintf(pngname+strlen(pngname),".%d",ch);
			
		if( (png = pngsetupwrite(f,dir,pngname,cols,rows,0,PNG_COLOR_TYPE_GRAY,0,h)) )
			pngwriteimage(f,chcomp,rowpos,startchan+i,1,rows,cols,h->depth);
	}
}

void doimage(FILE *f, struct layer_info *li, char *name,
			 int channels, int rows, int cols, struct psd_header *h){
	int ch,comp,startchan,pngchan,color_type,
		*chcomp = checkmalloc(sizeof(int)*channels);
	long **rowpos = checkmalloc(sizeof(long*)*channels);
	FILE *png = NULL; /* handle to the output PNG file */

	for( ch = 0 ; ch < channels ; ++ch ) 
		rowpos[ch] = checkmalloc(sizeof(long)*(rows+1));

	pngchan = color_type = 0;
	switch(h->mode){
	case ModeBitmap:
	case ModeGrayScale:
	case ModeGray16:
	case ModeDuotone:
	case ModeDuotone16:
		if(channels == 1 || (!li && !mergedalpha)){
			color_type = PNG_COLOR_TYPE_GRAY;
			pngchan = 1;
		}
		else if(channels >= 2){
			color_type = PNG_COLOR_TYPE_GRAY_ALPHA;
			pngchan = 2;
		}
		break;
	case ModeIndexedColor:
		color_type = PNG_COLOR_TYPE_PALETTE;
		pngchan = 1;
		break;
	case ModeRGBColor:
	case ModeRGB48:
		if(channels == 3 || (!li && !mergedalpha)){
			color_type = PNG_COLOR_TYPE_RGB;
			pngchan = 3;
		}
		else if(channels >= 4){
			color_type = PNG_COLOR_TYPE_RGB_ALPHA;
			pngchan = 4;
		}
		break;
	}

	if(!li){
		VERBOSE("\n  merged channels:\n");
		
		// The 'merged' or 'composite' image is where the flattened image is stored
		// when 'Maximise Compatibility' is used.
		// It consists of:
		// - the alpha channel for merged image (if mergedalpha is TRUE)
		// - the merged image (1 or 3 channels)
		// - any remaining alpha or spot channels.
		// For an identifiable image mode (Bitmap, GreyScale, Duotone, Indexed or RGB), 
		// we should ideally 
		// 1) write the first 1[2] or 3[4] channels in appropriate PNG format
		// 2) write the remaining channels as extra GRAY PNG files.
		// (For multichannel (and maybe other?) modes, we should just write all
		// channels per step 2)
		
		comp = dochannel(f,li,0/*no index*/,channels,rows,cols,h->depth,rowpos);
		for( ch=0 ; ch < channels ; ++ch ) 
			chcomp[ch] = comp; /* merged channels share same compression type */
		
		if(writepng){
			nwarns = 0;
			startchan = 0;
			if(pngchan && !splitchannels){
				// recognisable PNG mode, so spit out the merged image
				if( (png = pngsetupwrite(f, pngdir, name, 
										 cols, rows, pngchan, color_type, 0/*ARGB*/, h)) )
					pngwriteimage(f,chcomp,rowpos,0,pngchan,rows,cols,h->depth);
				startchan += pngchan;
			}
			if(startchan < channels){
				if(!pngchan)
					UNQUIET("# writing %s image as split channels...\n",mode_names[h->mode]);
				writechannels(f, pngdir, name, chcomp, rowpos, 
							  startchan, channels-startchan, 1/*alphalast*/, rows, cols, h);
			}
		}
	}else{
		// Process layer:
		// for each channel, store its row pointers sequentially 
		// in the rowpos[] array, and its compression type in chcomp[] array
		// (pngwriteimage() will take care of interleaving this data for libpng)
		for( ch=0 ; ch < channels ; ++ch ){
			VERBOSE("  channel %d:\n",ch);
			chcomp[ch] = dochannel(f,li,ch,1/*count*/,rows,cols,h->depth,rowpos+ch);
		}
		if(writepng){
			nwarns = 0;
			if(pngchan){
				if( (png = pngsetupwrite(f, pngdir, name, 
										 cols, rows, channels, color_type, 1/*RGBA*/, h)) )
					pngwriteimage(f,chcomp,rowpos,0,pngchan,rows,cols,h->depth);
			}else{
				UNQUIET("# writing layer as split channels...\n");
				writechannels(f, pngdir, name, chcomp, rowpos, 
							  0, channels, 0/*alpha first*/, rows, cols, h);
			}
		}
	}

	for(ch=0;ch<channels;++ch) 
		free(rowpos[ch]);
	free(rowpos);
	free(chcomp);
}

void dolayermaskinfo(FILE *f,struct psd_header *h){
	long miscstart,misclen,layerlen,chlen,skip,extrastart,extralen;
	int nlayers,i,j,chid,namelen;
	struct layer_info *linfo;
	char **lname,*chidstr,tmp[10];
	struct blend_mode_info bm;

	if( (misclen = get4B(f)) ){
		miscstart = ftell(f);

		// process layer info section
		if( (layerlen = get4B(f)) ){
			// layers structure
			nlayers = get2B(f);
			if(nlayers < 0){
				nlayers = -nlayers;
				VERBOSE("  (first alpha is transparency for merged image)\n");
				mergedalpha = 1;
			}
			UNQUIET("\n%d layers:\n",nlayers);
			
			if( nlayers*(18+6*h->channels) > layerlen ){ // sanity check
				alwayswarn("### ridiculous number of layers, giving up.\n");
				return;
			}
			
			linfo = checkmalloc(nlayers*sizeof(struct layer_info));
			lname = checkmalloc(nlayers*sizeof(char*));

			for( i=0 ; i < nlayers ; ++i ){
				// process layer record
				linfo[i].top = get4B(f);
				linfo[i].left = get4B(f);
				linfo[i].bottom = get4B(f);
				linfo[i].right = get4B(f);
				linfo[i].channels = get2B(f);
				
				VERBOSE("\n");
				UNQUIET("  layer %d: (%4ld,%4ld,%4ld,%4ld), %d channels (%4ld rows x %4ld cols)\n",
						i, linfo[i].top, linfo[i].left, linfo[i].bottom, linfo[i].right, linfo[i].channels,
						linfo[i].bottom-linfo[i].top, linfo[i].right-linfo[i].left);

				if( linfo[i].bottom < linfo[i].top || linfo[i].right < linfo[i].left || linfo[i].channels > 64 ){ // sanity check
					alwayswarn("### something's not right about that, giving up.\n");
					return;
				}

				linfo[i].chlengths = checkmalloc(sizeof(long) * linfo[i].channels);
	
				for( j=0 ; j < linfo[i].channels ; ++j ){
					chid = get2B(f);
					chlen = linfo[i].chlengths[j] = get4B(f);
					switch(chid){
					case -1: chidstr = " (transparency mask)"; break;
					case -2: chidstr = " (layer mask)"; break;
					default:
						if(chid < strlen(channelsuffixes[h->mode]))
							sprintf(chidstr = tmp, " (%c)", channelsuffixes[h->mode][chid]); // it's a mode-ish channel
						else
							chidstr = ""; // can't explain it
					}
					VERBOSE("    channel %2d: %7ld bytes, id=%2d %s\n",j,chlen,chid,chidstr);
				}

				fread(bm.sig,1,4,f);
				fread(bm.key,1,4,f);
				bm.opacity = fgetc(f);
				bm.clipping = fgetc(f);
				bm.flags = fgetc(f);
				bm.filler = fgetc(f);
				VERBOSE("  blending mode: sig='%c%c%c%c' key='%c%c%c%c' opacity=%d(%d%%) clipping=%d(%s)\n\
    flags=%#x(transp_prot%s visible%s bit4valid%s pixel_data_relevant%s)\n",
						bm.sig[0],bm.sig[1],bm.sig[2],bm.sig[3],
						bm.key[0],bm.key[1],bm.key[2],bm.key[3],
						bm.opacity,(bm.opacity*100+127)/255,
						bm.clipping,bm.clipping ? "non-base" : "base",
						bm.flags, BITSTR(bm.flags&1),BITSTR(bm.flags&2),BITSTR(bm.flags&8),BITSTR(bm.flags&16) );

				//skipblock(f,"layer info: extra data");
				extralen = get4B(f);
				extrastart = ftell(f);
				//printf("  (extra data: %d bytes @ %d)\n",extralen,extrastart);

				skipblock(f,"layer mask data");
				skipblock(f,"layer blending ranges");
				
				// layer name
				namelen = fgetc(f);
				lname[i] = checkmalloc(PAD4(1+namelen));
				fread(lname[i],1,PAD4(1+namelen),f);
				lname[i][namelen] = 0;
				UNQUIET("    name: \"%s\"\n",lname[i]);
		
				fseek(f,extrastart+extralen,SEEK_SET); // skip over any extra data
			}
      
			if(listfile) fputs("assetlist = {\n",listfile);
				
			for( i = 0 ; i < nlayers ; ++i ){
				long pixw = linfo[i].right-linfo[i].left,
					 pixh = linfo[i].bottom-linfo[i].top;
				VERBOSE("\n  layer %d (\"%s\"):\n",i,lname[i]);
			  
				if(listfile && pixw && pixh)
					fprintf(listfile,"\t\"%s\" = { pos={%4ld,%4ld}, size={%4ld,%4ld} },\n",
							lname[i], linfo[i].left, linfo[i].top, pixw, pixh);
		
				doimage(f, linfo+i, lname[i], linfo[i].channels, pixh, pixw, h);
			}

			if(listfile) fputs("}\n",listfile);
      
		}else VERBOSE("  (layer info section is empty)\n");
		
		// process global layer mask info section
		skipblock(f,"global layer mask info");

		skip = miscstart+misclen - ftell(f);
		if(skip){
			warn("skipped %d bytes at end of misc data?",skip);
			fseek(f,skip,SEEK_CUR);
		}
		
	}else VERBOSE("  (misc info section is empty)\n");
	
}

char *finddesc(int id){
	/* dumb linear lookup of description string from resource id */
	/* assumes array ends with a NULL string pointer */
	struct resdesc *p = rdesc;
	if(id >= 2000 && id < 2999) return "path"; // special case
	while(p->str && p->id != id)
		++p;
	return p->str;
}

long doirb(FILE *f){
	char type[4],name[0x100],*d;
	int id,namelen;
	long size;

	fread(type,1,4,f);
	id = get2B(f);
	namelen = fgetc(f);
	fread(name,1,PAD2(1+namelen)-1,f);
	name[namelen] = 0;
	size = get4B(f);
	fseek(f,PAD2(size),SEEK_CUR);

	VERBOSE("  resource '%c%c%c%c' (%5d,\"%s\"):%5ld bytes",
			type[0],type[1],type[2],type[3],id,name,size);
	if( (d = finddesc(id)) ) 
		VERBOSE(" [%s]",d);
	VERBOSE("\n");

	return 4+2+PAD2(1+namelen)+4+PAD2(size); /* returns total bytes in block */
}

void doimageresources(FILE *f){
	long len = get4B(f);
	VERBOSE("\nImage resources (%ld bytes):\n",len);
	while(len>0)
		len -= doirb(f);
	if(len != 0) warn("image resources overran expected size by %d bytes\n",-len);
}

int main(int argc,char *argv[]){
	struct psd_header h;
	FILE *f;
	int i,indexptr,opt;
	char *base,*ext;
	static struct option longopts[] = {
		{"verbose",  no_argument, &verbose, 1},
		{"quiet",    no_argument, &quiet, 1},
		{"help",     no_argument, &help, 1},
		{"pngdir",   required_argument, NULL, 'd'},
		{"writepng", no_argument, &writepng, 1},
		{"makedirs", no_argument, &makedirs, 1},
		{"list",     no_argument, &writelist, 1},
		{"split",    no_argument, &splitchannels, 1},
		{NULL,0,NULL,0}
	};

	while( (opt = getopt_long(argc,argv,"vqd:wmlsh",longopts,&indexptr)) != -1)
		switch(opt){
		case 'v': verbose = 1; break;
		case 'q': quiet = 1; break;
		case 'd': pngdir = optarg;
		case 'w': writepng = 1; break;
		case 'm': makedirs = 1; break;
		case 'l': writelist = 1; break;
		case 's': splitchannels = 1; break;
		case 'h':
		default:  help = 1; break;
		}

	if(help || optind >= argc)
		fprintf(stderr,"usage: %s [options] psdfile...\n\
  -h, --help         show this help\n\
  -v, --verbose      print more information\n\
  -q, --quiet        work silently\n\
  -w, --writepng     write PNG files of each raster layer (and merged composite)\n\
  -d, --pngdir dir   put PNGs in directory (implies --writepng)\n\
  -m, --makedirs     create subdirectory for PNG if layer name contains %c's\n\
  -l, --list         write an 'asset list' of layer sizes and positions\n\
  -s, --split        write each composite channel to individual (grey scale) PNG\n", argv[0],DIRSEP);

	for( i=optind ; i<argc ; ++i ){
		if( (f = fopen(argv[i],"rb")) ){
			nwarns = 0;

			UNQUIET("\"%s\"\n",argv[i]);

			strcpy(indir,argv[i]);
			ext = strrchr(indir,'.');
			ext ? strcpy(ext,DIRSUFFIX) : strcat(indir,DIRSUFFIX);

			if(writelist){
				char fname[FILENAME_MAX];

				strcpy(fname,pngdir);
				MKDIR(fname,0755);
				strcat(fname,dirsep);
				strcat(fname,"list.txt");
				if( (listfile = fopen(fname,"w")) )
					fprintf(listfile,"-- PSD file: %s\n",argv[i]);
			}

			// file header
			fread(h.sig,1,4,f);
			h.version  = get2B(f);
			get4B(f); get2B(f); // reserved[6];
			h.channels = get2B(f);
			h.rows     = get4B(f);
			h.cols     = get4B(f);
			h.depth    = get2B(f);
			h.mode     = get2B(f);

			if(!feof(f) && !memcmp(h.sig,"8BPS",4) && h.version == 1){
				UNQUIET("  channels = %d, rows = %ld, cols = %ld, depth = %d, mode = %d (%s)\n",
						h.channels, h.rows, h.cols, h.depth,
						h.mode, h.mode >= 0 && h.mode < 16 ? mode_names[h.mode] : "???");
				
				if(h.channels <= 0 || h.channels > 64 || h.rows <= 0 || 
					 h.cols <= 0 || h.depth < 0 || h.depth > 32 || h.mode < 0)
					alwayswarn("### something just isn't right about that header, giving up now.\n");
				else{
					h.colormodepos = ftell(f);
					skipblock(f,"color mode data");
					doimageresources(f); //skipblock(f,"image resources");
					dolayermaskinfo(f,&h); //skipblock(f,"layer & mask info");
	
					// now process image data
					base = strrchr(argv[i],DIRSEP);
					doimage(f,NULL,base ? base+1 : argv[i],h.channels,h.rows,h.cols,&h);
	
					UNQUIET("  done.\n\n");
				}
			}else
				alwayswarn("# \"%s\": couldn't read header, is not a PSD, or version is not 1!\n",argv[i]);

			if(listfile) fclose(listfile);
			fclose(f);
		}else
			alwayswarn("# \"%s\": couldn't open\n",argv[i]);
	}
	return EXIT_SUCCESS;
}
