#include "png.h"

enum{RAWDATA,RLECOMP};

/* Photoshop's mode constants */
#define ModeBitmap     0
#define ModeGrayScale    1
#define ModeIndexedColor 2
#define ModeRGBColor     3
#define ModeCMYKColor    4
#define ModeHSLColor     5
#define ModeHSBColor     6
#define ModeMultichannel 7
#define ModeDuotone    8
#define ModeLabColor     9
#define ModeGray16    10
#define ModeRGB48     11
#define ModeLab48     12
#define ModeCMYK64    13
#define ModeDeepMultichannel 14
#define ModeDuotone16   15

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
  // following fields are for our purposes, not actual header fields
  long colormodepos;
};
struct layer_info{
  long top;
  long left;
  long bottom;
  long right;
  short channels;
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

FILE* pngsetupwrite(FILE *psd, char *dir, char *name, int width, int height, 
                    int channels, int merged,struct psd_header *h);
int pngwriteimage(FILE *psd, int comp[], long **rowpos,
                  int channels,int rows,int cols,int depth);

int unpackbits(unsigned char *outp,unsigned char *inp,int rowbytes,int inlen);

#ifdef macintosh
int mkdir(char *s,int mode);
#endif
