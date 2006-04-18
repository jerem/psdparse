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

#include <stdio.h>
#include <stdlib.h>

#include "psdparse.h"
#include "png.h"

static png_structp png_ptr;
static png_infop info_ptr;

FILE* pngsetupwrite(FILE *psd, char *dir, char *name, int width, int height, 
					int channels, int color_type, int alphalast, struct psd_header *h){
	char pngname[PATH_MAX],*last,d[PATH_MAX],*pngtype = NULL;
	static FILE *f; // static, because it might get used post-longjmp()
	unsigned char *palette;
	png_color *pngpal;
	int i,n;
	long savepos;

	f = NULL;
	if(width && height){

		MKDIR(dir,0755);

		if(strchr(name,DIRSEP)){
			if(!makedirs) 
				fprintf(stderr,"# warning: replaced %c's in filename (use --makedirs if you want subdirectories)\n",DIRSEP);
			for( last=name ; (last=strchr(last+1,'/')) ; )
				if(makedirs){
					last[0] = 0;
					strcpy(d,dir);
					strcat(d,dirsep);
					strcat(d,name);
					if(!MKDIR(d,0755)) VERBOSE("# made subdirectory \"%s\"\n",d);
					last[0] = DIRSEP;
				}else 
					last[0] = '_';
		}

		strcpy(pngname,dir);
		strcat(pngname,dirsep);
		strcat(pngname,name);
		strcat(pngname,".png");

		switch(color_type){
		case PNG_COLOR_TYPE_GRAY:       pngtype="GRAY"; break;
		case PNG_COLOR_TYPE_GRAY_ALPHA: pngtype="GRAY_ALPHA"; break;
		case PNG_COLOR_TYPE_PALETTE:    pngtype="PALETTE"; break;
		case PNG_COLOR_TYPE_RGB:        pngtype="RGB"; break;
		case PNG_COLOR_TYPE_RGB_ALPHA:  pngtype="RGB_ALPHA"; break;
		}
		if(color_type == -1){
			fprintf(stderr,"## don't know how to write PNG of %d channels (%s)\n", 
					channels, mode_names[h->mode]);
			return NULL;
		}else
		{
			if( !(png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL)) ){
				fputs("### pngsetupwrite: png_create_write_struct failed\n",stderr);
				return NULL;
			}

			if( (f = fopen(pngname,"wb")) ){

				UNQUIET("# writing PNG \"%s\"\n",pngname);
				VERBOSE("#             %3dx%3d, depth=%d, channels=%d, type=%d(%s)\n", 
						width,height,h->depth,channels,color_type,pngtype);

				if( !(info_ptr = png_create_info_struct(png_ptr)) || setjmp(png_jmpbuf(png_ptr)) )
				{ /* If we get here, libpng had a problem */
					fputs("### pngsetupwrite: Fatal error in libpng\n",stderr);
					fclose(f);
					png_destroy_write_struct(&png_ptr, &info_ptr);
					return NULL;
				}

				png_init_io(png_ptr, f);

				png_set_IHDR(png_ptr, info_ptr, width, height, h->depth, color_type,
							 PNG_INTERLACE_NONE, PNG_COMPRESSION_TYPE_DEFAULT, PNG_FILTER_TYPE_DEFAULT);

				if(h->mode == ModeBitmap) 
					png_set_invert_mono(png_ptr);
				else if(h->mode == ModeIndexedColor){
					savepos = ftell(psd);
					fseek(psd,h->colormodepos,SEEK_SET);
					n = get4B(psd);
					palette = checkmalloc(n);
					fread(palette,1,n,psd);
					fseek(psd,savepos,SEEK_SET);
					n /= 3;
					pngpal = checkmalloc(sizeof(png_color)*n);
					for(i=0;i<n;++i){
						pngpal[i].red   = palette[i];
						pngpal[i].green = palette[i+n];
						pngpal[i].blue  = palette[i+2*n];
					}
					png_set_PLTE(png_ptr, info_ptr, pngpal, n);
					free(pngpal);
					free(palette);		 
				}

				png_write_info(png_ptr, info_ptr);
				
				png_set_compression_level(png_ptr,Z_BEST_COMPRESSION);

				/* swap location of alpha bytes from ARGB to RGBA */
				if(alphalast) png_set_swap_alpha(png_ptr);

			}else fprintf(stderr,"### can't open \"%s\" for writing\n",pngname);
		}
	}else fprintf(stderr,"### skipping layer \"%s\" (%dx%d)\n",name,width,height);

	return f;
}

void pngwriteimage(FILE *psd, int comp[], long **rowpos,
				   int startchan, int pngchan, int rows, int cols, int depth){
	int i,j,ch;
	unsigned n,rb = (depth*cols+7)/8;
	unsigned char *rowbuf,*inrows[4],*rledata,*p;
	short *q;
	long savepos = ftell(psd);

	rowbuf = checkmalloc(rb*pngchan);
	rledata = checkmalloc(2*rb);

	for(ch=0;ch<pngchan;++ch){
		inrows[ch] = checkmalloc(rb);
		//printf("[%d] inrows=%#x rowpos=%#x\n",ch,inrows[ch],rowpos[ch]);
	}

	if( setjmp(png_jmpbuf(png_ptr)) )
	{ /* If we get here, libpng had a problem writing the file */
		fputs("### pngwriteimage: Fatal error in libpng\n",stderr);

done:	/* put cleanup code here, so that we are sure to do it in case of a PNG error */
		free(rowbuf);
		free(rledata);
		for(ch=0;ch<pngchan;++ch)
			free(inrows[ch]);
	
		fseek(psd,savepos,SEEK_SET);

		png_destroy_write_struct(&png_ptr, &info_ptr);
		return;
	}

	for(j=0;j<rows;++j){
		for(i=0;i<pngchan;++i){
			ch = startchan+i;
			/* get row data */
			//printf("rowpos[%d][%4d] = %7d\n",ch,j,rowpos[ch][j]);

			if(fseek(psd,rowpos[ch][j],SEEK_SET) == -1){
				fprintf(stderr,"# error seeking to %ld\n",rowpos[ch][j]);
				memset(inrows[i],0,rb);
			}else{

				if(comp[ch] == RAWDATA){ /* uncompressed row */
					n = fread(inrows[i],1,rb,psd);
					if(n != rb){
						fprintf(stderr,"# error reading row data (raw) @ %ld\n",rowpos[ch][j]);
						memset(inrows[i]+n,0,rb-n);
					}
				}
				else{ /* RLE compressed row */
					n = rowpos[ch][j+1] - rowpos[ch][j];
					if(fread(rledata,1,n,psd) != n){
						fprintf(stderr,"# error reading row data (RLE) @ %ld\n",rowpos[ch][j]);
						memset(inrows[i],0,rb);
					}else
						unpackbits(inrows[i],rledata,rb,n);
				}

			}
		}

		if(pngchan>1){ /* interleave channels */
			if(depth == 8)
				for(i=0,p = rowbuf;i<cols;++i)
					for(ch=0;ch<pngchan;++ch)
						*p++ = inrows[ch][i];
			else
				for(i=0,q = (short*)rowbuf;i<cols;++i)
					for(ch=0;ch<pngchan;++ch)
						*q++ = ((short*)inrows[ch])[i];
		}else 
			memcpy(rowbuf,inrows[0],rb);

		png_write_row(png_ptr, rowbuf);
	}
	png_write_end(png_ptr, NULL /*info_ptr*/);

	goto done;
}

