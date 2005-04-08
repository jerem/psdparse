#include <stdio.h>
#include <stdlib.h>

#include "psdparse.h"

png_structp png_ptr;
png_infop info_ptr;

extern char *mode_names[];

FILE* pngsetupwrite(FILE *psd, char *dir, char *name, int width, int height, 
                    int channels, int merged, struct psd_header *h){
  char pngname[0x100],*last,d[0x100];
  static char dirsep[]={DIRSEP,0};
  FILE *f = NULL;
  unsigned char *palette,*p;
  png_color *pngpal;
  int i,n,color_type = -1;
  long savepos;
  extern int makedirs;
  
  if(width && height){
    
    mkdir(dir,0755);

    if(strchr(name,DIRSEP)){
      if(!makedirs) 
        fprintf(stderr,"# warning: replaced %c's in filename (use -makedirs if you want subdirectories)\n",DIRSEP);
      for(last=name;last=strchr(last+1,'/');)
        if(makedirs){
          last[0] = 0;
          strcpy(d,dir);
          strcat(d,dirsep);
          strcat(d,name);
          if(!mkdir(d,0755)) VERBOSE("# made subdirectory \"%s\"\n",d);
          last[0] = DIRSEP;
        }else 
          last[0] = '_';
    }

    strcpy(pngname,dir);
    strcat(pngname,dirsep);
    strcat(pngname,name);
    strcat(pngname,".png");

    switch(h->mode){
    case ModeBitmap:
    case ModeGrayScale:
    case ModeGray16:
      if     (channels == 1) color_type = PNG_COLOR_TYPE_GRAY;
      else if(channels == 2) color_type = PNG_COLOR_TYPE_GRAY_ALPHA;
      break;
    case ModeIndexedColor:
      if     (channels == 1) color_type = PNG_COLOR_TYPE_PALETTE;
      break;
    case ModeRGBColor:
    case ModeRGB48:
      if     (channels == 3) color_type = PNG_COLOR_TYPE_RGB;
      else if(channels == 4) color_type = PNG_COLOR_TYPE_RGB_ALPHA;
      break;
    }
    if(color_type == -1){
      fprintf(stderr,"## can't write PNG of %d channels (%s)\n", 
        channels, mode_names[h->mode]);
      return NULL;
    }else
    {
            
      if(f = fopen(pngname,"wb")){
        
        UNQUIET("# writing PNG (%3dx%3d, depth=%d, type=%d) \"%s\" \n", 
          width,height,h->depth,color_type,pngname);
        
        png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
        if(!png_ptr){
          fclose(f);
          return NULL;
        }
    
        info_ptr = png_create_info_struct(png_ptr);
        if(!info_ptr){
          png_destroy_write_struct(&png_ptr, (png_infopp)NULL);
          fclose(f);
          return NULL;
        }
  
        if(setjmp(png_jmpbuf(png_ptr)))
        { /* If we get here, we had a problem writing the file */
          fputs("### Fatal error in pnglib\n",stderr);
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
          palette = malloc(n);
          fread(palette,1,n,psd);
          fseek(psd,savepos,SEEK_SET);
          n /= 3;
          pngpal = malloc(sizeof(png_color)*n);
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
  
        // png_set_invert_alpha(png_ptr);
        /* swap location of alpha bytes from ARGB to RGBA */
        if(!merged) png_set_swap_alpha(png_ptr);
        
      }else fprintf(stderr,"# problem opening \"%s\" for writing\n",pngname);
    }
  }else fprintf(stderr,"### skipping layer \"%s\" (%dx%d)\n",name,width,height);
  
  return f;
}

int pngwriteimage(FILE *psd, int comp[], long **rowpos, 
                  int channels, int rows, int cols, int depth){
  int i,j,k,n,ch,rb = (depth*cols+7)/8;
  unsigned char *rowbuf,*inrows[4],*rledata,*p;
  long savepos = ftell(psd);
      
  if( (rowbuf = malloc(rb*channels)) && (rledata = malloc(2*rb)) ){
    for(ch=0;ch<channels;++ch)
      if( !(inrows[ch] = malloc(rb)) )
        return 0; /* FIXME: yes, this will leak memory on failure */
      //else printf("[%d] inrows=%#x rowpos=%#x\n",ch,inrows[ch],rowpos[ch]);
    
    for(j=0;j<rows;++j){
      for(ch=0;ch<channels;++ch){
        /* get row data, either raw or compressed */
        //printf("rowpos[%d][%4d] = %7d\n",ch,j,rowpos[ch][j]);
        if(fseek(psd,rowpos[ch][j],SEEK_SET) == -1){
          fprintf(stderr,"# error seeking to %ld\n",rowpos[ch][j]);
          return 0;
        }
        if(comp[ch] == RAWDATA){
          if(fread(inrows[ch],1,rb,psd) != rb){
            fprintf(stderr,"# error reading row data (raw) @ %ld\n",rowpos[ch][j]);
            return 0;
          }
        }else{
          n = rowpos[ch][j+1]-rowpos[ch][j];
          if(fread(rledata,1,n,psd) != n){
            fprintf(stderr,"# error reading row data (RLE) @ %ld\n",rowpos[ch][j]);
            return 0;
          }
          unpackbits(inrows[ch],rledata,rb,n);
        }
      }
      
      if(ch>1){ /* interleave channels */
        if(depth == 8)
          for(i=0,p = rowbuf;i<cols;++i)
            for(ch=0;ch<channels;++ch)
              *p++ = inrows[ch][i];
        else
          for(i=0,p = rowbuf;i<cols;++i)
            for(ch=0;ch<channels;++ch)
              *((short*)p)++ = ((short*)inrows[ch])[i];
      }else 
        memcpy(rowbuf,inrows[0],rb);
          
      png_write_row(png_ptr, rowbuf);
    }
    png_write_end(png_ptr, NULL /*info_ptr*/);
    png_destroy_write_struct(&png_ptr, &info_ptr);
    
    free(rowbuf);
    for(ch=0;ch<channels;++ch)
      free(inrows[ch]);
  }
  fseek(psd,savepos,SEEK_SET);
  
  return 0;
}

