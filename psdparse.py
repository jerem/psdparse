#!/usr/bin/env python
# using some python 2.5 features.

# standard
import sys, os, os.path, math
from stat import *
from struct import unpack, calcsize
# PIL
import PIL.Image as Image
import PIL.ImageChops as ImageChops
import PIL.ImageStat as ImageStat
# own
from psddata import *
from lossify import getLossifier

######################################################################
# Helpers

def progress(msg):
    global OPTS
    if not OPTS.quiet:
        print >>sys.stderr, msg

def verbose(msg):
    global OPTS
    if OPTS.very_verbose:
        print >>sys.stderr, "  #", msg

def info(msg):
    global OPTS
    if OPTS.verbose:
        print >>sys.stderr, msg

def warn(msg):
    print >>sys.stderr, "Warning:", msg

def PAD2(i):
    """same or next even"""
    return (i+1)/2*2

def PAD4(i):
    """same or next multiple of 4"""
    return (i+3)/4*4

class Any:
    """container for any struct data, easy to access via names and printing"""
    def __str__(self):
        return "%s" % self.__dict__

def readf(f, format):
    """read a strct from file structure according to format"""
    return unpack(format, f.read(calcsize(format)))

def make_filename(fn_stub, ext):
    global OPTS
    fn = os.path.join(OPTS.output_dir2, OPTS.file_prefix, fn_stub+"."+ext)
    verbose("  filename: '%s'" % fn)
    return fn


######################################################################
# Main

def skipblock(f, desc):
    (n,) = readf(f, ">L") # (n,) is a 1-tuple.
    if n:
        f.seek(n, 1) # 1: relative
    info("Skipped %s with %s bytes" %(desc, n))
        
def doirb(f):
    """return total bytes in block"""
    global OPTS
    r = Any()
    r.at = f.tell()
    (r.type, r.id, r.namelen) = readf(f, ">4s H B")
    n = PAD2(r.namelen+1)-1
    (r.name,) = readf(f, ">%ds"%n)
    r.name = r.name[:-1] # skim off trailing 0byte
    r.short = r.name[:20]
    (r.size,) = readf(f, ">L")
    f.seek(PAD2(r.size), 1) # 1: relative
    r.rdesc = "[%s]" % RDESC.get(r.id, "?")
    verbose("Resource: %s" % r)
    if OPTS.list_irb:
        progress((" 0x%(at)06x| type:%(type)s, id:%(id)5d, "
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


def calc_noise(orig_image, fn_lossy, lossifier):
    """returns noise of lossy image-file by unlossifying and comparing to orig-image''"""
    fn_lossless = lossifier.unlossify(fn_lossy)
    q = Image.open(fn_lossless)
    r = ImageChops.difference(orig_image, q)
    istat = ImageStat.Stat(r)
    # - see: http://en.wikipedia.org/wiki/PSNR
    # - and: http://en.wikipedia.org/wiki/Root_mean_square
    _sqrt_mse = istat.rms[0]
    
    _psnr = 20.0 * math.log10(255.0 / _sqrt_mse) if _sqrt_mse!=0 else 1000*1000
    del q
    del r
    return _psnr
    

def dochannel(f, li, idx, count, rows, cols, depth):
    """params:
    f -- open psd file file, read pointer on data
    li -- layer info struct
    idx -- channel number
    count -- number of channels to process ???
    rows, cols -- dimensions
    depth -- bits
    """
    chlen = li.chlengths[idx]
    if chlen is not None  and  chlen < 2:
        raise "not enough channel data: %s" % chlen
    if li.chids[idx] == -2:
        rows, cols = li.mask.rows, li.mask.cols
    rb = (cols*depth+7) / 8 # round to next byte
    # channel header
    chpos = f.tell()
    (comp,) = readf(f, ">H")
    if chlen:
        chlen -= 2
    if comp == Compressions.Raw:
        verbose("handling raw uncompressed data")
    elif comp == Compressions.RLE:
        verbose("handling RLE compressed data")
    else:
        raise "## bad compression type: %s" % comp
        # TODO: maybe just skip channel...:
        #   f.seek(chlen, SEEK_CUR)
        #   return
    pos = f.tell()
    if comp == Compressions.RLE:
        lossifier = getLossifier(OPTS)
        rlecounts = 2 * count * rows
        if chlen and chlen < rlecounts:
            raise "channel too short for RLE row counts (need %d bytes, have %d bytes)" % (rlecounts,chlen)
        pos += rlecounts # image data starts after RLE counts
        rlecounts_data = readf(f, ">%dH" % (count*rows) )
        for ch in range(count):
            # read rle data
            rlelen_for_channel = sum(rlecounts_data[ch*rows:(ch+1)*rows])
            data = f.read(rlelen_for_channel)
            p = Image.fromstring("L", (cols,rows), data, "packbits", "L" )
            # save p as a file suitable for lossifier
            _ext = lossifier.lossless_extension()
            fn_orig = make_filename("%s_%02d" % (li.fname, li.chids[idx+ch]), _ext)
            p.save(fn_orig)
            sz_orig = os.stat(fn_orig)[ST_SIZE]
            progress("       saved   (%5dk): %s" % (sz_orig/1024, fn_orig))
            if OPTS.presets_compare:
                for preset in range(10):
                    fn_lossy = lossifier.lossify(fn_orig, preset, suffix="-%d"%preset)
                    sz_lossy = os.stat(fn_lossy)[ST_SIZE]
                    if sz_lossy < 50:
                        raise "Lossified file to small: %d bytes" % sz_lossy
                    _snoise = ""
                    if OPTS.safe:
                        _noise = calc_noise(p, fn_lossy, lossifier)
                        if _noise < OPTS.noise_limit:
                            raise "Noise:%5.2f lesser then limit:%5.2f" %(_noise, OPTS.noise_limit)
                        _snoise = "%5.2f" % _noise
                    progress("   lossified-%s (%5dk): %s %s" % (preset, sz_lossy/1024, fn_lossy, _snoise))
            else:
                _preset = OPTS.preset
                if li.layernum == 0: # bg layer
                    if li.chids[idx+ch] >= 0: # real channel, not mask or transparency
                        _preset = OPTS.preset_bgchannel
                fn_lossy = lossifier.lossify(fn_orig, _preset)
                sz_lossy = os.stat(fn_lossy)[ST_SIZE]
                if sz_lossy < 50:
                    raise "Lossified file to small: %d bytes" % sz_lossy
                _snoise = ""
                if OPTS.safe:
                    _noise = calc_noise(p, fn_lossy, lossifier)
                    if _noise < OPTS.noise_limit:
                        raise "Noise:%5.2f lesser then limit:%5.2f" %(_noise, OPTS.noise_limit)
                    _snoise = "%5.2f" % _noise
                progress("   lossified-%s (%5dk): %s %s" % (_preset, sz_lossy/1024, fn_lossy, _snoise))
            del p                
            os.remove(fn_orig)
            info("     removed    %5s  : %s" % ("",fn_orig))
    elif comp == Compressions.Raw:
        raise "Compressions.Raw nyi"
    else:
        raise "program flow error"

    if (chlen is not None) and (f.tell() != chpos+2+chlen):
        warn("currentpos:%d should be:%d!" % (f.tell(), chpos+2+chlen))
        f.seek(chpos+2+chlen, 0) # 0: SEEK_SET

    return
    
    
        
def doimage(f, li, h, isLayer=True):
    progress("Image: %s/%d" % (li.fname, li.channels))
    # channels
    if isLayer:
        for ch in range(li.channels):
            dochannel(f, li, ch, 1, li.rows, li.cols, h.depth)
    else:
        dochannel(f, li, 0, li.channels, li.rows, li.cols, h.depth) 
    return


def dolayermaskinfo(f, h):
    progress("Layers & Masks...")
    h.mergedalpha = False
    (misclen,) = readf(f, ">L")
    if misclen:
        miscstart = f.tell()        
        # process layer info section
        (layerlen,) = readf(f, ">L")
        if layerlen:
            # layers structure
            (nlayers,) = readf(f,">H")
            if nlayers<0:
                nlayers = -nlayers
                verbose("  (first alpha is transparency for merged image)")
                h.mergedalpha = True
            info("  layer info for %d layers:" % nlayers)
            if nlayers*(18+6*h.channels) > layerlen:
                raise ValueError("Unlikely number of %s layers for %s channels with %s layerlen. Giving up." %
                                 (nlayers, h.channels, layerlen) )

            linfo = [ ] # collect header infos here
            
            for i in range(nlayers):
                l = Any()
                l.idx = i
                #
                # Layer Info
                #
                (l.top, l.left, l.bottom, l.right, l.channels
                 ) = readf(f, ">LLLLH")
                l.rows, l.cols = l.bottom - l.top, l.right - l.left
                # print info
                info(("  layer %(idx)d: (%(top)4d,%(left)4d,%(bottom)4d,%(right)4d),"
                      " %(channels)d channels (%(rows)4d rows x %(cols)4d cols)"
                      ) % l.__dict__ )
                # sanity
                if l.bottom < l.top or l.right < l.left or l.channels > 64:
                    warn("### something's not right about that, trying to skip layer.");
                    f.seek(6*l.channels+12, 1) # 1: SEEK_CUR
                    skipblock(f,"layer info: extra data");
                    continue # next layer

                # read channel infos
                l.chlengths = []
                l.chids  = []
                # - 'hackish': addressing with -1 and -2 will wrap around to the two extra channels
                l.chindex = [ -1 ] * (l.channels+2)
                for j in range(l.channels):
                    chid, chlen = readf(f, ">hL")
                    l.chids.append(chid)
                    l.chlengths.append(chlen)
                    info("    channel %2d: id=%2d, %5d bytes" % (j, chid, chlen))
                    if -2 <= chid < l.channels:
                        # pythons negative list-indexs: [ 0, 1, 2, 3, ... -2, -1]
                        l.chindex[chid] = j
                    else:
                        warn("unexpected channel id %d" % chid)
                    l.chidstr = CHANNELSUFFIXES.get(chid, "?")

                # put channel info into connection
                linfo.append( l ) 

                #
                # Blend mode
                #
                bm = Any()
                # read
                (bm.sig, bm.key, bm.opacity, bm.clipping, bm.flags, bm.filler,
                 ) = readf(f, ">4s4sBBBB")
                bm.opacp = (bm.opacity*100+127)/255
                bm.clipname = bm.clipping and "non-base" or "base"
                l.blend_mode = bm
                # print
                info(("  blending mode: sig=%(sig)s key=%(key)s opacity=%(opacity)d(%(opacp)d%%)"
                     " clipping=%(clipping)d(%(clipname)s) flags=%(flags)x"
                     ) % bm.__dict__ )

                # remember position for skipping unrecognized data
                (extralen,) = readf(f, ">L")
                extrastart = f.tell()

                # layer mask data
                m = Any()
                (m.size,) = readf(f, ">L")
                if m.size:
                    (m.top, m.left, m.bottom, m.right, m.default_color, m.flags,
                     ) = readf(f, ">LLLLBB")
                    # skip remainder
                    f.seek(m.size-18, 1) # 1: SEEK_CUR
                    m.rows, m.cols = m.bottom-m.top, m.right-m.left
                l.mask = m

                skipblock(f,"layer blending ranges");

                # layer name
                (l.namelen,) = readf(f,">B")
                # - "-1": one byte traling 0byte. "-1": one byte garble.
                (l.name,) = readf(f, ">%ds" % (PAD4(1+l.namelen)-2) ) 
                #@todo: handle filename-harming names here?
                l.fname = l.name
                info("    name: '%s'" % l.name);                    

                # skip over any extra data
                f.seek(extrastart + extralen, 0) # 0: SEEK_SET

            for i in range(nlayers):
                linfo[i].layernum = i
                doimage(f, linfo[i], h, isLayer=True)

        else:
            info("  (layer info section is empty)")

        skip = miscstart+misclen - f.tell()
        if(skip):
            warn("skipped %d bytes at end of misc data?" % skip)
            f.seek(skip, 1) # 1: SEEK_CUR
    else:
        info("  (misc info section is empty)")

   
    
def main(fn):
    # create dir
    if not OPTS.output_dir:
        OPTS.output_dir2 = os.path.splitext(fn)[0]
    else:
        OPTS.output_dir2 = OPTS.output_dir
    if os.path.exists(OPTS.output_dir2):
        if os.path.isdir(OPTS.output_dir2):
            pass
        else:
            raise "there exists a non-dir '%s'" % OPTS.output_dir2
    else:
        os.makedirs(os.path.abspath(OPTS.output_dir2)) # raises on arror
    # go
    progress("Opening '%s'..." % fn)
    f = open(fn, "rb")
    try:
        progress("Reading header...")
        h = Any()
        C_PSD_HEADER = ">4sH 6B HLLHH" # see psdparse.h
        (h.sig, h.version, h.r0,h.r1,h.r2,h.r3,h.r4,h.r5, h.channels, 
            h.rows, h.cols, h.depth, h.mode) = readf(f, C_PSD_HEADER)
        if h.sig != "8BPS":
            raise ValueError("Not a PSD signature: '%s'" % h.sig)
        if h.version != 1:
            raise ValueError("Can not handle PSD version:%d" % h.version)
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
        li = Any()
        li.chids = range(h.channels)
        li.chlengths = [ None ] * h.channels # dummy data
        (li.fname, li.channels, li.rows, li.cols) = (
            "merged", h.channels, h.rows, h.cols)
        li.layernum = -1
        doimage(f, li, h, isLayer=False)
    finally:
        f.close()


def cyg_to_win(cyg_fn):
    return cyg_fn.replace("/d/", "D:/")


if __name__ == "__main__":
    #
    # parse OPTS
    #
    from optparse import OptionParser
    parser = OptionParser(usage = "usage: %prog [OPTS] PSDFILE.psd")
    po = parser.add_option
    # verbosity, demos, etc
    #po("-D","--demo", type="int", default=None,
    #   help="Run as demo with predefined paramter set")
    po("-V","--very-verbose", default=False, action="store_true")
    po("-v","--verbose", default=False, action="store_true")
    po("-Q","--quiet", default=False, action="store_true")
    po("-I","--list-irb", default=False, action="store_true",       
       help="List image resource block content")
    po("--presets-compare", default=False, action="store_true",
       help="creates lossified files for all presets 0..9 for you to compare")
    # files and names
    po("-d","--output-dir", default="",
       help="override 'psdfile/' as output location")
    po("-P","--file-prefix", default="",
       help="prefix string inside in output-dir for all created files")
    # operation modes
    po("-L","--lossifier", default="openjpeg", type="choice",
       choices=["openjpeg","jasper","photoshopcom"],
       help=("Lossifier to use [%default]. Executables must be in path or "
             "provided by the --[un]lossify-exe options"))
    po("--lossify-exe", default="", 
       help="Where to find the lossifying executable (default is lossifier-dependent)")
    po("--unlossify-exe", default="", 
       help="Where to find the unlossifying executable (default is lossifier-dependent)")
    po("-p","--preset", default=5, type="int",
       help="Lossify with preset '0' (worst) to '8' (best) or '9' (lossless) [%default]")
    po("-b","--preset-bgchannel", default=8, type="int",
       help="Lossify background with this preset (see -p) [%default]")
    po("-s","--safe", default=False, action="store_true",
       help="Safe mode, check intermediate results before destructive operation")
    po("--noise-limit", default=20.0, type="float",
       help=("Upper noise limit when processing is stopped in safe mode (-s). "
             "This 'PSNR' is measured on a "
             "log10 scale. Typical noises are inf (no), 60 (silent), 30-40 (normal), "
             "20 (noisy). i.e. with '100' almost no noise would be allowed, and 0 would allow "
             "any lossy result picture. [%default]"))
       # do it!
    (OPTS, args) = parser.parse_args()
    #
    # some opt preprocessing
    #
    if len(args) == 0:
        if 0:
            parser.print_help()
            sys.exit(-1)
        else: # exec with C-c C-c in emacs
            args = [ r'd:\foto\psdparse\ErrCheck3a.psd' ]        
    if OPTS.output_dir and len(args) != 1:
        print "can only use --output-dir option with one psdfile"
        sys.exit(-1)
    #
    # run
    #
    for fn in map(cyg_to_win, args):
        main(fn)
        
