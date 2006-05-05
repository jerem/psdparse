#!/usr/bin/env python
# using some python 2.5 features.

import sys
from struct import unpack, calcsize

from psddata import *

######################################################################
# Helpers

def progress(msg):
    print >>sys.stderr, msg

def verbose(msg):
    if 0:
        print >>sys.stderr, "  #", msg

def info(msg):
    print >>sys.stderr, msg

def warn(msg):
    print >>sys.stderr, "Warning:", msg

def PAD2(i):
    """same or next even"""
    return (i+1)/2*2

class Any:
    """container for any struct data, easy to access via names and printing"""
    def __str__(self):
        return "%s" % self.__dict__

def readf(f, format):
    """read a strct from file structure according to format"""
    return unpack(format, f.read(calcsize(format)))


######################################################################
# Main

def skipblock(f, desc):
    (n,) = readf(f, ">L") # (n,) is a 1-tuple.
    if n:
        f.seek(n, 1) # 1: relative
    progress("Skipped %s with %s bytes" %(desc, n))
        
def doirb(f):
    """return total bytes in block"""
    r = Any()
    r.at = f.tell()
    (r.type, r.id, r.namelen) = readf(f, ">4s H B")
    n = PAD2(r.namelen+1)-1
    (r.name,) = readf(f, ">%ds"%n)
    r.short = r.name[:20]
    (r.size,) = readf(f, ">L")
    f.seek(PAD2(r.size), 1) # 1: relative
    r.rdesc = "[%s]" % RDESC.get(r.id, "?")
    verbose("Resource: %s" % r)
    info((" 0x%(at)06x| type:%(type)s, id:%(id)5d, "
          "size:0x%(size)04x %(rdesc)s "
          "'%(short)s'"
          ) % r.__dict__)
    return 4+2+PAD2(1+r.namelen)+4+PAD2(r.size)
    

def doimageresources(f):
    progress("Ressources...")
    (n,) = readf(f, ">L") # (n,) is a 1-tuple.
    while n>0:
        n -= doirb(f)
    if n != 0:
        warn("Image resources overran expected size by %d bytes" % (-n))
        

def dolayermaskinfo(f,h):
    progress("Layers & Masks...")
    mergedalpha = False
    (misclen,) = readf(f, ">L")
    if misclen:
        miscstart = f.tell()        
        # process layer info section
        (layerlen,) = readf(f, ">L")
        if layerlen:
            # layers structure
            nlayers = readf(f,">H")
            if nlayers<0:
                nlayers = -nlayers
                verbose("  (first alpha is transparency for merged image)")
                mergedalpha = True
            info("  layer info for %d layers:" % nlayers)
            linfo = [ ]
            lname = [ ]
            
            for i in range(nlayers):
                l.idx = i
                #
                # Layer Info
                #
                (l.top, l.left, l.bottom, l.right, l.channels
                 ) = readf(f, ">LLLLH")
                l.rows, l.cols = l.bottom - l.top, l.right - l.left
                # print info
                info(("  layer %(idx)d: (%(top)4d,%4(left)4d,%(bottom)4d,%(right)4d),"
                      " %(channels)d channels (%(rows)4d rows x %(cols)4d cols)"
                      ) % l.__dict__ )                
                # read channel infos
                l.chlengths = []
                l.chids  = []
                for j in range(channels):
                    chid, chlen = readf(f, ">HL")
                    l.chids.append(chid)
                    l.chlengths.append(chlen)
                    info("    channel %2d: id=%2d, %5d bytes" % (j,chid,chlen))
                # put channel info into connection
                linfo.append( l ) 
    
                #
                # Blending mode
                #
                bm = Any()
                # read
                (bm.sig, bm.key, bm.opacity, bm.clipping, bm.flags, bm.filler,
                 ) = readf(f, ">4s4sBBBB")
                bm.opacp = (bm.opacity*100+127)/255
                bm.clipname = bm.clipping and "non-base" or "base"
                # print
                info(("  blending mode: sig=%(sig)s key=%(key)s opacity=%(opacity)d(%(opacp)d%%)"
                     " clipping=%(clipping)d(%(clipname)s) flags=%(flags)x"
                     ) % bm.__dict__ )
                #
                (extralen,) = readf(f, ">L")
                extrastart = f.tell()
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
				
			for(i=0;i<nlayers;++i){
				long pixw = linfo[i].right-linfo[i].left,
					 pixh = linfo[i].bottom-linfo[i].top;
				VERBOSE("\n  layer %d (\"%s\"):\n",i,lname[i]);
			  
				if(listfile && pixw && pixh)
					fprintf(listfile,"\t\"%s\" = { pos={%4ld,%4ld}, size={%4ld,%4ld} },\n",
							lname[i], linfo[i].left, linfo[i].top, pixw, pixh);
		
				doimage(f, linfo+i, lname[i], 0/*not merged*/, linfo[i].channels, 
						pixh, pixw, h);
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


   
    
def main(fn):
    progress("Opening '%s'..." % fn)
    f = open(fn, "rb")
    try:
        progress("Reading header...")
        h = Any()
        C_PSD_HEADER = ">4sH 6B HLLHH" # see psdparse.h
        s = f.read(calcsize(C_PSD_HEADER))
        (h.sig, h.version, h.r0,h.r1,h.r2,h.r3,h.r4,h.r5, h.channels, 
            h.rows, h.cols, h.depth, h.mode) = readf(f, C_PSD_HEADER)
        if h.sig != "8BPS": raise "Not a PSD signature:%s" % h.sig
        if h.version != 1: raise "Can not handle PSD version:%d" % h.version
        h.modename = MODENAMES[h.mode] if 0<=h.mode<16 else "(%s)"%h.mode
        verbose("Header: %s" % h.__dict__)
        info(("channels:%(channels)d, rows:%(rows)d, cols:%(cols)d, "
              "depth:%(depth)d, mode:%(mode)d [%(modename)s]"
              ) % h.__dict__)
        # remember position
        h.colormodepos = f.tell()
        skipblock(f, "color mode data")
        # recurse into resources
        doimageresources(f)  # //skipblock(f,"image resources");
        # and more data
        dolayermaskinfo(f,h) # //skipblock(f,"layer & mask info");
	# now process image data
        #base = strrchr(argv[i],DIRSEP);
        #doimage(f,base ? base+1 : argv[i],1/*merged*/,h.channels,h.rows,h.cols,&h);
    finally:
        f.close()


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        main(fn)
        
