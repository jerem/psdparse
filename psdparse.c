/*
	This file is part of "psdparse"
    Copyright (C) 2004 Toby Thain, toby@telegraphics.com.au

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
*/
#include <stdio.h>
#include <stdlib.h>

//#include "pigeneral.h"

#pragma options align=mac68k
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
#pragma options align=reset

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
	
	comp = get2B(f);
	printf("  compression method = %d (%s)\n",comp,comp==1 ? "RLE" : (comp ? "???" : "raw"));

	rb = (channels*cols*depth + 7)/8;
	rawdata = (long)channels*rows*rb;
	printf("  uncompressed size is %ld bytes (row bytes = %d)\n",rawdata,rb);

	rowbuf = malloc(rb*2); /* slop for possible RLE overhead */
	if(comp == 1){
		n = channels*rows;
		rlebuf = malloc(n*2);
		for(j=0;j<n && !feof(f);++j)
			rlebuf[j] = get2B(f);
		if(j < n)
			fatal("# couldn't read RLE counts");
	}

	for(ch=scanline=compdata=0;ch<channels;++ch){
		if(channels>1)
			printf("  channel %d:\n",ch);
		for(j=0;j<rows;++j){
			if(rows>15){
				if(j==rows-5) 
					printf("  ...%d rows not shown...\n",rows-10);
				dumpit = j<5 || j>=rows-5;
			}else 
				dumpit = 1;
			if(comp == 1){ /* RLE */
				n = rlebuf[scanline++];
				compdata += n;
				if(fread(rowbuf,1,n,f) == n){
					if(dumpit){
						printf("  %4d: <%4d> ",j,n);
						dumprow(rowbuf,n);
					}
				}else fatal("# couldn't read row!\n");
			}else if(comp == 0){ /* raw */
				if(fread(rowbuf,1,rb,f) == rb){
					if(dumpit){
						printf("  %4d: ",j);
						dumprow(rowbuf,rb);
					}
				}else fatal("# couldn't read row!\n");
			}else fatal("# bad compression value\n");
		}
	}
	putchar('\n');	

	if(comp == 1)
		free(rlebuf);
	free(rowbuf);
}

void dolayermaskinfo(FILE *f,struct psd_header *h){
	long miscstart,misclen,layerlen,chlen,skip;
	short nlayers;
	int i,j,chid;
	struct layer_info linfo;
	
	if(misclen = get4B(f)){
		miscstart = ftell(f);
		if(layerlen = get4B(f)){
			nlayers = get2B(f);
			printf("  nlayers = %d \n",nlayers);
			if(nlayers<0){
				nlayers = -nlayers;
				puts("  (first alpha channel is transparency data for merged image)");
			}
		
			for(i=0;i<nlayers;++i){
				linfo.top = get4B(f);
				linfo.left = get4B(f);
				linfo.bottom = get4B(f);
				linfo.right = get4B(f);
				linfo.channels = get2B(f);

				printf("  layer %d: (%d,%d,%d,%d), %d channels (%d rows x %d cols)\n",
					i,linfo.top,linfo.left,linfo.bottom,linfo.right,linfo.channels,
					linfo.bottom-linfo.top,linfo.right-linfo.left);
	
				for(j=0;j<linfo.channels;++j){
					chid = get2B(f);
					chlen = get4B(f);
					printf("  channel %d: id=%d, %d bytes\n",j,chid,chlen);
				}
				
				fseek(f,12,SEEK_CUR); // skip rest of layer info
				skipblock(f,"layer info: extra data");
	
				for(j=0;j<linfo.channels;++j){
					printf("  layer %d channel %d:\n",i,j);
					dochannel(f,1,linfo.bottom-linfo.top,linfo.right-linfo.left,h->depth);
				}
		
			}
		}else puts("  (layer info section is empty)");
		
		skipblock(f,"global layer mask info");

		skip = miscstart+misclen - ftell(f);
		if(skip){
			fprintf(stderr,"# warning: skipped %d spurious bytes at end of misc data?\n",skip);
			fseek(f,skip,SEEK_CUR);
		}
		
	}else puts("  (misc info section is empty)");
	
}

int main(int argc,char *argv[]){
	struct psd_header h;
	FILE *f;
	int i;

	for( i=1 ; i<argc ; ++i ){
		printf("\"%s\"\n",argv[i]);
		if( f = fopen(argv[i],"rb") ){

			h.sig = get4B(f);
			h.version = get2B(f);
			get4B(f); 
			get2B(f); // reserved[6];
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
				skipblock(f,"image resources");
				//skipblock(f,"layer & mask info");
				dolayermaskinfo(f,&h);
				
				printf("\n  image data @ offset %ld:\n",ftell(f));
				dochannel(f,h.channels,h.rows,h.cols,h.depth);

				puts("  END");
			}else fatal("# couldn't read header, is not a PSD, or version is not 1!\n");
			fclose(f);
		}else fatal("# couldn't open!\n");
	}
	return EXIT_SUCCESS;
}
