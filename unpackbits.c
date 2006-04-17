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
#include <string.h>

#include "psdparse.h"

int unpackbits(unsigned char *outp,unsigned char *inp,int outlen,int inlen){
	int i,len,val;

	/* i counts output bytes; outlen = expected output size */
	for(i = 0 ; inlen > 0 && i < outlen ; ){
		len = *inp++; --inlen; /* get flag byte */
		if(len != 128){ /* ignore this flag value */
			if(len > 128){
				len = 1+256-len;
				val = *inp++; --inlen; /* get value to repeat */
				if((i+len) <= outlen)
					memset(outp,val,len);
				else{ 
					warn("unpacked RLE data would overflow row (repeat)");
					break;
				}
			}else{
				++len;
				if((i+len) <= outlen){
					memcpy(outp,inp,len); inp += len; inlen -= len; /* copy verbatim run */
				}else{
					warn("unpacked RLE data would overflow row (copy)");
					break;
				}
			}
			outp += len;
			i += len;
		}
	}
	if(inlen < 0) warn("not enough RLE data for row");
	return i;
}
