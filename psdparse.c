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
*/
#include <stdio.h>
#include <stdlib.h>

//#include "pigeneral.h"

enum{ MAXLAYERS = 64, CONTEXTROWS = 3 };

#define PAD2(x) (((x)+1) & -2) // same or next even
#define PAD4(x) (((x)+3) & -4) // same or next multiple of 4

struct psd_header{
	long sig;
	short version;
	char reserved[6];
	short channels;
	long rows;
	long cols;
	short depth;
	short mode;
};
struct layer_info{
	long top;
	long left;
	long bottom;
	long right;
	short channels;
};
struct layer_info2{
	long blendmodesig;
	long blendmodekey;
	char opacity;
	char clipping;
	char flags;
	char filler;
	//long extradatasize;
};

struct resdesc {
  int id;
  char *str;
} rdesc[] = {
  1000,"PS2.0 mode data", // Obsolete—Photoshop 2.0 only. Contains five 2 byte values:
  // number of channels, rows, columns, depth, and mode.
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
		printf("  ...skipped %s (%ld bytes)\n",desc,n);
	}else
		printf("  (%s is empty)\n",desc);
}

void dumprow(unsigned char *b,int n){
	int k,m;
	m = n>25 ? 25 : n;
	for(k=0;k<m;++k) 
		printf("%02x",b[k]);
	if(n>m) printf(" ...%d more",n-m);
	putchar('\n');
}

void dochannel(FILE *f,int channels,int rows,int cols,int depth){
	int j,n,comp,rb,ch,dumpit;
	long scanline,compdata,rawdata;
	unsigned char *rowbuf;
	unsigned short *rlebuf;
  enum{RAWDATA,RLECOMP};
	
	comp = get2B(f);
	printf("  compression = %d (%s)\n",
    comp,comp==RLECOMP ? "RLE" : (comp==RAWDATA ? "raw" : "???"));

	rb = (channels*cols*depth + 7)/8;
	rawdata = (long)channels*rows*rb;
	printf("  uncompressed size %ld bytes (row bytes = %d)\n",rawdata,rb);

	rowbuf = malloc(rb*2); /* slop for possible RLE overhead */
	if(comp == RLECOMP){
		n = channels*rows;
		rlebuf = malloc(n*sizeof(short));
		for(j=0;j<n && !feof(f);++j)
			rlebuf[j] = get2B(f);
		if(j < n)
			fatal("# couldn't read RLE counts");
	}

	for(ch=scanline=compdata=0 ; ch < channels ; ++ch){
		if(channels>1)
			printf("    channel %d:\n",ch);
		for(j=0;j<rows;++j){
			if(rows > 3*CONTEXTROWS){
				if(j==rows-CONTEXTROWS) 
					printf("    ...%d rows not shown...\n",rows-2*CONTEXTROWS);
				dumpit = j<CONTEXTROWS || j>=rows-CONTEXTROWS;
			}else 
				dumpit = 1;
        
			if(comp == RLECOMP){
				n = rlebuf[scanline++];
				compdata += n;
				if(fread(rowbuf,1,n,f) == n){
					if(dumpit){
						printf("    %4d: <%4d> ",j,n);
						dumprow(rowbuf,n);
					}
				}else fatal("# couldn't read RLE row!\n");
			}else if(comp == RAWDATA){
				if(fread(rowbuf,1,rb,f) == rb){
					if(dumpit){
						printf("    %4d: ",j);
						dumprow(rowbuf,rb);
					}
				}else fatal("# couldn't read raw row!\n");
			}else fatal("# bad compression value\n");
		}
	}
	putchar('\n');	

	if(comp == RLECOMP) free(rlebuf);
	free(rowbuf);
}

void dolayermaskinfo(FILE *f,struct psd_header *h){
	long miscstart,misclen,layerlen,chlen,skip,extrastart,extralen;
	short nlayers;
	int i,j,chid,namelen;
  char name[0x100];
	struct layer_info linfo[MAXLAYERS];
	
	if(misclen = get4B(f)){
		miscstart = ftell(f);
    
    // process layer info section
		if(layerlen = get4B(f)){
      // layers structure
			nlayers = get2B(f);
			if(nlayers<0){
				nlayers = -nlayers;
				puts("  (first alpha is transparency for merged image)");
			}
      printf("  nlayers = %d\n",nlayers);
      
			for(i=0;i<nlayers;++i){
        // process layer record
				linfo[i].top = get4B(f);
				linfo[i].left = get4B(f);
				linfo[i].bottom = get4B(f);
				linfo[i].right = get4B(f);
				linfo[i].channels = get2B(f);

				printf("\n  layer %d: (%d,%d,%d,%d), %d channels (%d rows x %d cols)\n",
					i, linfo[i].top, linfo[i].left, linfo[i].bottom, linfo[i].right, linfo[i].channels,
					linfo[i].bottom-linfo[i].top, linfo[i].right-linfo[i].left);
	
				for( j=0 ; j < linfo[i].channels ; ++j ){
					chid = get2B(f);
					chlen = get4B(f);
					printf("    channel %2d: id=%2d, %5d bytes\n",j,chid,chlen);
				}
				
				fseek(f,12,SEEK_CUR); // skip blending sig, key, opacity
				//skipblock(f,"layer info: extra data");
        extralen = get4B(f);
        extrastart = ftell(f);
        //printf("  (extra data: %d bytes @ %d)\n",extralen,extrastart);

        skipblock(f,"layer mask data");
        skipblock(f,"layer blending ranges");
        // layer name
        namelen = fgetc(f);
        fread(name,1,PAD4(1+namelen),f);
        name[namelen] = 0;
        printf("  layer name: \"%s\"\n",name);
        
        fseek(f,extrastart+extralen,SEEK_SET); // skip over any extra data
			}
      
      for(i=0;i<nlayers;++i){
        for( j=0 ; j < linfo[i].channels ; ++j ){
          printf("  layer %d channel %d:\n",i,j);
          dochannel(f,1,linfo[i].bottom-linfo[i].top,linfo[i].right-linfo[i].left,h->depth);
        }
      }
		}else puts("  (layer info section is empty)");
		
    // process global layer mask info section
		skipblock(f,"global layer mask info");

		skip = miscstart+misclen - ftell(f);
		if(skip){
			fprintf(stderr,"# warning: skipped %d spurious bytes at end of misc data?\n",skip);
			fseek(f,skip,SEEK_CUR);
		}
		
	}else puts("  (misc info section is empty)");
	
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
    
    printf("  resource '%c%c%c%c' (%5d,\"%s\"):%5ld bytes",
      type[0],type[1],type[2],type[3],id,name,size);
    if( d = finddesc(id) ) printf(" [%s]",d);
    putchar('\n');
    
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

	for( i=1 ; i<argc ; ++i ){
		printf("\"%s\"\n",argv[i]);
		if( f = fopen(argv[i],"rb") ){

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

				printf("  channels = %d, rows = %ld, cols = %ld, depth = %d, mode = %d (%s)\n",
					h.channels, h.rows, h.cols, h.depth,
					h.mode, h.mode >= 0 && h.mode < 16 ? mode_names[h.mode] : "???");

				skipblock(f,"color mode data");
				doimageresources(f); //skipblock(f,"image resources");
				dolayermaskinfo(f,&h); //skipblock(f,"layer & mask info");
        
				// now process image data
				printf("\n  (merged) image data @ offset %ld:\n",ftell(f));
				dochannel(f,h.channels,h.rows,h.cols,h.depth);

				puts("  END");
			}else fatal("# couldn't read header, is not a PSD, or version is not 1!\n");
			fclose(f);
		}else fatal("# couldn't open!\n");
	}
	return EXIT_SUCCESS;
}
