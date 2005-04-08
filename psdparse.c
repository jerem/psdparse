/*
    This file is part of "psdparse"
    Copyright (C) 2004-5 Toby Thain, toby@telegraphics.com.au

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
*/
#include <stdio.h>
#include <stdlib.h>

#include "psdparse.h"

#define VERBOSE if(verbose) printf
#define UNQUIET if(!quiet) printf

enum{ CONTEXTROWS = 3 };

struct resdesc rdesc[] = {
  1000,"PS2.0 mode data",
  1001,"Macintosh print record",
  1003,"PS2.0 indexed color table",
  1005,"ResolutionInfo",
  1006,"Names of the alpha channels",
  1007,"DisplayInfo",
  1008,"caption",
  1009,"Border information",
  1010,"Background color",
  1011,"Print flags",
  1012,"Grayscale and multichannel halftoning info",
  1013,"Color halftoning info",
  1014,"Duotone halftoning info",
  1015,"Grayscale and multichannel transfer function",
  1016,"Color transfer functions",
  1017,"Duotone transfer functions",
  1018,"Duotone image info",
  1019,"black and white values for the dot range",
  1021,"EPS options",
  1022,"Quick Mask info",
  1024,"Layer state info",
  1025,"Working path",
  1026,"Layers group info",
  1028,"IPTC-NAA record (File Info)",
  1029,"Image mode for raw format files",
  1030,"JPEG quality",
  1032,"Grid and guides info",
  1033,"Thumbnail resource",
  1034,"Copyright flag",
  1035,"URL",
  1036,"Thumbnail resource",
  1037,"Global Angle",
  1038,"Color samplers resource",
  1039,"ICC Profile",
  1040,"Watermark",
  1041,"ICC Untagged",
  1042,"Effects visible",
  1043,"Spot Halftone",
  1044,"Document specific IDs",
  1045,"Unicode Alpha Names",
  1046,"Indexed Color Table Count",
  1047,"Transparent Index",
  1049,"Global Altitude",
  1050,"Slices",
  1051,"Workflow URL",
  1052,"Jump To XPEP",
  1053,"Alpha Identifiers",
  1054,"URL List",
  1057,"Version Info",
  2999,"Name of clipping path",
  10000,"Print flags info",
  0,NULL
};

char *mode_names[]={
	"Bitmap", "GrayScale", "IndexedColor", "RGBColor",
	"CMYKColor", "HSLColor", "HSBColor", "Multichannel",
	"Duotone", "LabColor", "Gray16", "RGB48",
	"Lab48", "CMYK64", "DeepMultichannel", "Duotone16"
};

int verbose = 0,quiet = 0,mergedalpha = 0,makedirs = 0;
char *pngdir = NULL;

void fatal(char *s){ fputs(s,stderr); exit(EXIT_FAILURE); }

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
	int k,m;
	m = n>25 ? 25 : n;
	for(k=0;k<m;++k) 
		VERBOSE("%02x",b[k]);
	if(n>m) VERBOSE(" ...%d more",n-m);
	VERBOSE("\n");
}

int dochannel(FILE *f,int channels,int rows,int cols,int depth,long rowpos[]){
	int j,k,n,rb,ch,dumpit;
	long scanline,compdata,pos;
	unsigned char *rowbuf;
	unsigned *rlebuf;
  static char *comptype[] = {"raw","RLE"};
	
  unsigned comp = get2B(f);
  VERBOSE("  compression = %d (%s)\n", comp,comp<2 ? comptype[comp] : "???");

  rb = (cols*depth + 7)/8;
  VERBOSE("  uncompressed size %ld bytes (row bytes = %d)\n",(long)channels*rows*rb,rb);

  rowbuf = malloc(rb*2); /* slop for worst case RLE overhead (usually (rb/127+1) ) */
  pos = ftell(f);
  if(comp == RLECOMP){
    rlebuf = malloc(channels*rows*sizeof(unsigned));
    pos += 2*channels*rows; /* skip over RLE counts */
    for(ch=k=0;ch<channels;++ch){
      for(j=0;j<rows && !feof(f);++j){
        rlebuf[k] = get2B(f);
        if(rowpos){ /* store file position of row's RLE data */
          //printf("RLE data row %4d @ %7ld\n",k,pos);
          rowpos[k] = pos;
          pos += rlebuf[k];
          ++k;
        }
      }
      if(rowpos) rowpos[k++] = pos;
      if(j < rows) fatal("# couldn't read RLE counts");
    }
  }else 
    if(rowpos){
      for(ch=k=0;ch<channels;++ch){
        for(j=0;j<rows;++j){ /* store file position of row's raw data */
          //printf("Raw data row %4d @ %7ld\n",k,pos);
          rowpos[k++] = pos;
          pos += rb;
        }
        rowpos[k++] = pos;
      }
    }

	for(ch = scanline = 0 ; ch < channels ; ++ch){
		if(channels>1) VERBOSE("    channel %d:\n",ch);
		for(j=0;j<rows;++j){
			if(rows > 3*CONTEXTROWS){
				if(j==rows-CONTEXTROWS) 
					VERBOSE("    ...%d rows not shown...\n",rows-2*CONTEXTROWS);
				dumpit = j<CONTEXTROWS || j>=rows-CONTEXTROWS;
			}else 
				dumpit = 1;
        
			if(comp == RLECOMP){
				n = rlebuf[scanline++];
				if(fread(rowbuf,1,n,f) == n){
					if(dumpit){
						VERBOSE("    %4d: <%4d> ",j,n);
						dumprow(rowbuf,n);
					}
				}else fatal("# couldn't read RLE row!\n");
			}else if(comp == RAWDATA){
				if(fread(rowbuf,1,rb,f) == rb){
					if(dumpit){
						VERBOSE("    %4d: ",j);
						dumprow(rowbuf,rb);
					}
				}else fatal("# couldn't read raw row!\n");
			}else fatal("# bad compression value\n");
		}
	}
	VERBOSE("\n");

	if(comp == RLECOMP) free(rlebuf);
	free(rowbuf);
  
  return comp;
}

#define BITSTR(f) ((f) ? "(1)" : "(0)")

void doimage(FILE *f,char *name,int merged,int channels,
             int rows,int cols,struct psd_header *h){
  int i,ch,comp;
  long **rowpos = malloc(sizeof(long*) * channels);
  int *chcomp = malloc(sizeof(int) * channels);
  FILE *png = NULL; /* file handle to the output PNG file */
  
  if(pngdir)
    png = pngsetupwrite(f, pngdir, name, cols, rows, channels, merged, h);

  rowpos[0] = malloc(sizeof(long)*channels*(rows+1));
  for( ch=1 ; ch < channels ; ++ch )
    rowpos[ch] = rowpos[0] + ch*(rows+1);
    
  if(merged){
    VERBOSE("  merged channels:\n");
    comp = dochannel(f,channels,rows,cols,h->depth,rowpos[0]);
    for(ch=0;ch<channels;++ch) 
      chcomp[ch] = comp; /* compression same for each merged channel */
  }else
    for( ch=0 ; ch < channels ; ++ch ){
      VERBOSE("  channel %d:\n",ch);
      chcomp[ch] = dochannel(f,1,rows,cols,h->depth,rowpos[ch]);
    }
  
  if(png) pngwriteimage(f,chcomp,rowpos,channels,rows,cols,h->depth);
  
  /* free memory for row position data */
  free(rowpos[0]);
  free(rowpos);
  free(chcomp);
}

void dolayermaskinfo(FILE *f,struct psd_header *h){
	long miscstart,misclen,layerlen,chlen,skip,extrastart,extralen;
	short nlayers;
	int i,j,chid,namelen,rows,cols;
	struct layer_info *linfo;
  char **lname;
  struct blend_mode_info bm;
	
	if(misclen = get4B(f)){
		miscstart = ftell(f);
    
    // process layer info section
		if(layerlen = get4B(f)){
      // layers structure
			nlayers = get2B(f);
			if(nlayers<0){
				nlayers = -nlayers;
				VERBOSE("  (first alpha is transparency for merged image)");
        mergedalpha = 1;
			}
      UNQUIET("  nlayers = %d\n",nlayers);
    	if( !(linfo = malloc(nlayers*sizeof(struct layer_info)))
       || !(lname = malloc(nlayers*sizeof(char*))) ){
    		fputs("# couldn't get memory for layer info!\n",stderr);
    		exit(EXIT_FAILURE);
    	}
		
			for(i=0;i<nlayers;++i){
        // process layer record
				linfo[i].top = get4B(f);
				linfo[i].left = get4B(f);
				linfo[i].bottom = get4B(f);
				linfo[i].right = get4B(f);
				linfo[i].channels = get2B(f);

				UNQUIET("  layer %d: (%d,%d,%d,%d), %d channels (%d rows x %d cols)\n",
					i, linfo[i].top, linfo[i].left, linfo[i].bottom, linfo[i].right, linfo[i].channels,
					linfo[i].bottom-linfo[i].top, linfo[i].right-linfo[i].left);
	
				for( j=0 ; j < linfo[i].channels ; ++j ){
					chid = get2B(f);
					chlen = get4B(f);
					VERBOSE("    channel %2d: id=%2d, %5d bytes\n",j,chid,chlen);
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
        lname[i] = malloc(PAD4(1+namelen));
        fread(lname[i],1,PAD4(1+namelen),f);
        lname[i][namelen] = 0;
        UNQUIET("  layer name: \"%s\"\n",lname[i]);
        
        fseek(f,extrastart+extralen,SEEK_SET); // skip over any extra data
			}
      
      for(i=0;i<nlayers;++i){
        VERBOSE("  layer %d (\"%s\"):\n",i,lname[i]);
        doimage(f, lname[i], 0/*not merged*/, linfo[i].channels, 
                linfo[i].bottom-linfo[i].top, linfo[i].right-linfo[i].left, h);
      }
		}else VERBOSE("  (layer info section is empty)\n");
		
    // process global layer mask info section
		skipblock(f,"global layer mask info");

		skip = miscstart+misclen - ftell(f);
		if(skip){
			fprintf(stderr,"# warning: skipped %d bytes at end of misc data?\n",skip);
			fseek(f,skip,SEEK_CUR);
		}
		
	}else VERBOSE("  (misc info section is empty)\n");
	
}

char *finddesc(int id){
    /* dumb linear lookup of description string from resource id */
    /* assumes array ends with a NULL string pointer */
    struct resdesc *p = rdesc;
    if(id>=2000 && id<2999) return "path"; // special case
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
    if( d = finddesc(id) ) VERBOSE(" [%s]",d);
    VERBOSE("\n");
    
    return 4+2+PAD2(1+namelen)+4+PAD2(size); /* returns total bytes in block */
}

void doimageresources(FILE *f){
    long len = get4B(f);
    while(len>0)
      len -= doirb(f);
    if(len != 0) fprintf(stderr,"# warning: image resources overran expected size by %d bytes\n",-len);
}

int main(int argc,char *argv[]){
	struct psd_header h;
	FILE *f;
	int i;
  char *base;

  /* look for option flags */
  for(i=1;i<argc;++i)
    if(argv[i][0] == '-'){
      if(!strcmp(argv[i],"-v")) verbose = 1;
      if(!strcmp(argv[i],"-q")) quiet = 1;
      else if(!strncmp(argv[i],"-pngdir=",8)) pngdir = argv[i]+8;
      else if(!strcmp(argv[i],"-makedirs")) makedirs = 1;
      else fprintf(stderr,"# bad option %s\nusage: %s [-v] [-png] psdfile...\n\
  -v            verbose information\n\
  -q            work silently\n\
  -pngdir=path  write PNG files of raster layers into directory\n\
  -makedirs     create subdirectory for PNG if layer name has /'s\n", argv[i], argv[0]);
    }

	for( i=1 ; i<argc ; ++i ){
		if( argv[i][0] != '-' )
      if(f = fopen(argv[i],"rb")){
        UNQUIET("\"%s\"\n",argv[i]);
        // file header
  			h.sig = get4B(f);
  			h.version = get2B(f);
  			get4B(f); get2B(f); // reserved[6];
  			h.channels = get2B(f);
  			h.rows = get4B(f);
  			h.cols = get4B(f);
  			h.depth = get2B(f);
  			h.mode = get2B(f);
  
  			if(!feof(f) && h.sig == '8BPS' && h.version == 1){
  
  				UNQUIET("  channels = %d, rows = %ld, cols = %ld, depth = %d, mode = %d (%s)\n",
  					h.channels, h.rows, h.cols, h.depth,
  					h.mode, h.mode >= 0 && h.mode < 16 ? mode_names[h.mode] : "???");
  
          h.colormodepos = ftell(f);
  				skipblock(f,"color mode data");
  				doimageresources(f); //skipblock(f,"image resources");
  				dolayermaskinfo(f,&h); //skipblock(f,"layer & mask info");
          
  				// now process image data
          base = strrchr(argv[i],DIRSEP);
          doimage(f,base ? base+1 : argv[i],1/*merged*/,h.channels,h.rows,h.cols,&h);
  				//dochannel(f,h.channels,h.rows,h.cols,h.depth,NULL);
  
  				UNQUIET("  done.\n");
  			}else fprintf(stderr,"# \"%s\": couldn't read header, is not a PSD, or version is not 1!\n",argv[i]);
  			fclose(f);
  		}else fprintf(stderr,"# \"%s\": couldn't open\n",argv[i]);
	}
	return EXIT_SUCCESS;
}
