#include <stdio.h>
#include <string.h>

int unpackbits(unsigned char *outp,unsigned char *inp,int outlen,int inlen){
  int j,i,len,val;
  
  /* i counts output bytes; outlen = expected output size */
	for(i = 0 ; inlen > 0 && i < outlen ; ){
		len = *inp++; --inlen; /* get flag byte */
	  if(len == 128)
			; /* ignore this flag value */
		else{
			if(len > 128){
				len = 1+256-len;
				val = *inp++; --inlen; /* get value to repeat */
        if((i+len) <= outlen)
					memset(outp,val,len);
				else{ 
					fputs("# unpacked RLE data would overflow row (repeat)\n",stderr);
					break;
				}
			}else{
				++len;
				if((i+len) <= outlen){
          memcpy(outp,inp,len); inp += len; inlen -= len; /* copy verbatim run */
				}else{
					fputs("# unpacked RLE data would overflow row (copy)\n",stderr);
					break;
				}
			}
			outp += len;
			i += len;
		}
	}
  if(inlen < 0) fputs("# not enough RLE data for row\n",stderr);
  return i;
}