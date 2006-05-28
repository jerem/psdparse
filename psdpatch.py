#!/usr/bin/env python
# using some python 2.5 features.

# standard
import sys, os, os.path, math
from stat import *
from struct import pack, unpack, calcsize
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
    if OPTS.verbose or OPTS.very_verbose:
        print >>sys.stderr, msg

def warn(msg):
    print >>sys.stderr, "Warning:", msg

def PAD2(i):
    """same or next even"""
    return (i+1)/2*2

def PAD4(i):
    """same or next multiple of 4"""
    return (i+3)/4*4

class Any(object):
    """container for any struct data, easy to access via names and printing"""
    def __str__(self):
        return "%s" % self.__dict__

def readf(f, format):
    """read a struct from file structure according to format"""
    return unpack(format, f.read(calcsize(format)))

def writef(f, format, *data):
    """writes a struct from according to format"""
    f.write(pack(format, *data))

def copyf(f, g, format):
    data_tuple = readf(f, format)
    writef(g, format, *data_tuple)
    return data_tuple


def make_filename(fn_stub, ext):
    global OPTS
    fn = os.path.join(OPTS.output_dir2, OPTS.file_prefix, fn_stub+"."+ext)
    verbose("  filename: '%s'" % fn)
    return fn


######################################################################
# Main

def copyblock(f_in, f_out, desc):
    progress("* %s" %desc)
    (n,) = readf(f_in, ">L") # (n,) is a 1-tuple.
    writef(f, ">L", n) 
    if n:
        f_out.write(f_in.read(n))
    info("  - copied 4+%d bytes" % n)


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

def _handle_saved(li, chid, fn_orig, img_orig, lossifier):
    global OPTS
    if OPTS.presets_compare:
        # do all 10 levels
        presets = range(10)
        # with different filenames
        func_lossify = lambda p: lossifier.lossify(fn_orig, p, suffix="-%d"%p)
    else:
        # one preset only, calced from layer properties
        presets = [ OPTS.preset ]
        if li.layernum == 0: # bg layer
            if chid >= 0: # real channel, not mask or transparency
                presets = [ OPTS.preset_bgchannel ]
        # with one filename
        func_lossify = lambda p: lossifier.lossify(fn_orig, p)
    
    # do lossify, 1 or 10 times        
    for preset in presets:
        fn_lossy = func_lossify(preset)
        sz_lossy = os.stat(fn_lossy)[ST_SIZE]
        if sz_lossy < 50:
            raise "Lossified file to small: %d bytes" % sz_lossy
        _snoise = ""
        if OPTS.safe:
            _noise = calc_noise(img_orig, fn_lossy, lossifier)
            if _noise < OPTS.noise_limit:
                raise "Noise:%5.2f lesser then limit:%5.2f" %(_noise, OPTS.noise_limit)
            _snoise = "%5.2f" % _noise
        progress("   lossified-%s (%5dk): %s %s" % (preset, sz_lossy/1024, fn_lossy, _snoise))
    #
    os.remove(fn_orig)
    info("     removed    %5s  : %s" % ("",fn_orig))
    return


def patch_psd(fn_psd_in, fn_psd_out):
    f_in = open(fn_psd_in, "rb")
    f_out = open(fn_psd_out, "wb")
    #
    # Header
    #
    progress("* Headers")
    C_PSD_HEADER = ">4sH 6B HLLHH" # see psdparse.h
    h = Any()
    (h.sig, h.version, h.r0,h.r1,h.r2,h.r3,h.r4,h.r5, h.channels, 
     h.rows, h.cols, h.depth, h.mode) = copyf(f_in, f_out, C_PSD_HEADER)
    if h.sig != "8BPS":
        raise ValueError("Not a PSD signature: '%s'" % h.sig)
    if h.version != 1:
        raise ValueError("Can not handle PSD version:%d" % h.version)
    if h.depth != 8 and not OPTS.experimental_16_bit:
        warn("Can not handle depth:%s properly, yet" % h.depth)
        return False
    #
    # Color Modes
    #
    copyblock(f_in, f_out, "* Color Mode Data")
    #
    # image resources
    #
    copyblock(f_in, f_out, "* Image Resources")
    #
    # Layers (including their interesting CHANNLES, MASK and TRANSPARENCY)
    #
    progress("* Layers")
    h._misclen_pos = f_in.tell() # remember, because 'misclen' must be corrected later
    misclen_old, = copyf(f_in, f_out, ">L") # dummy! will be overriden later
    h._len_diff = 0              # will decrement/increment with each patched channel
    h.mergedalpha = False
    if misclen_old == 0:
        info("  - Misc data length is 0 (improbable)")
    else:
        h._layerlen_pos = f_in.tell() # remember for patching later
        layerlen_old, = copyf(f_in, f_out, ">L")
        if layerlen_old == 0:
            info("  - Layer data length is 0 (16bit?)") # TODO handle 16bit files
        else:
            (nlayers,) = copyf(f_in, ">H")
            if nlayers<0:
                nlayers = -nlayers
                verbose("  (first alpha is transparency for merged image)")
                h.mergedalpha = True
            assert nlayers*(18+6*h.channels) <= layerlen_old
            linfos = []
            for layernum in range(layers):
                #
                # A Layer
                #
                l = Any()
                l.layernum = layernum
                # * Layer Info
                (l.top, l.left, l.bottom, l.right, l.channels
                 ) = copyf(f_in, f_out, ">LLLLH")
                l.rows, l.cols = l.bottom - l.top, l.right - l.left
                assert not(l.bottom < l.top or l.right < l.left or l.channels > 64)
                l.channel_patch_infos = []
                for chnum in range(l.channels):
                    # * Channel Info
                    # - chid
                    _chid, = copyf(f_in, f_out, ">h")
                    chids.append( _chid )
                    assert -2 <= _chid < l.channels
                    # - chlen
                    _lp = f_in.tell()
                    _cl, = copyf(f_in, f_out, ">L")
                    # remember!
                    cpi = ChannelPatchInfo(layernum,chnum, _chid, _lp, _cl)
                    l.channel_patch_infos.append( cpi )
                # - Blend Mode
                _data = copyf(f_in, f_out, ">4s4sBBBB")
                # - layer extra data (lxd)
                layer_extra_start = f_in.tell()
                layer_extra_len, = copyf(f_in, f_out, ">L") 
                # . - lxd: layer mask data
                _lm_len, = copyf(f_in, f_out, ">L") # 0, 20 or 36
                if _lm_len:
                    (l.mtop, l.mleft, l.mbottom, l.mright, _dc, l.mflags,
                     ) = readf(f, ">LLLLBB")
                else:
                    (l.mtop, l.mleft, l.mbottom, l.mright, _dc, l.mflags,
                     ) = 0,0,0,0,None,0
                l.mrows, l.mcols = l.mbottom-l.mtop, l.mright-l.mleft
                # . - lxd: copy rest of layer mask data
                if _lm_len-18 > 0:
                    f.write(f_in.read(_len-18))
                # . - lxd: blending ranges
                copyblock(f_in, f_out, "- layer blending ranges")
                # . - lxd: layer name
                namelen, = copyf(f_in, f_out,">B")
                l.name, = copyf(f_in, f_out, ">%ds" % (PAD4(1+l.namelen)-2) )
                progress("  - Layer '%s' contains channels: %s" % (
                    l.name, l.chids) )
                # . - lxd: copy unknown rest, like adjustment layer info
                _rest = layer_extra_start + layer_extra_len - f_in.tell()
                assert rest >= 0
                if _rest > 0:
                    f_out.write(f_in.read(_rest))
                #
                linfos.append( l )
                
            #
            # Layer Pixel data
            #
            for linfo in linfos:
                patch_image(f_in, f_out, h, linfo)
                
        patch_extra_data()
        
    return
                

def patch_image(f_in, f_out, h, linfo):
    if linfo.layernum >= 0:
        # a layer from the layer&mask section
        for cpi in linfo.channel_patch_infos:
            patch_channel(f_in, f_out, h, linfo, cpi)
    else:
        patch_channel(f_in, f_out, h, linfo, cpi)


class Patcher_Base(object):
    pass

class Patcher_ClearOut(Patcher_Base):
    def __init__(self, lossifier):
        self.lossifier = lossifier
        self.ll_ext = lossifier.lossless_extension()
        
    def getCompressionTag(self, isLayer):
        """blocktype: 'layer' or 'merged'"""
        return Compressions.Raw
    
    def getChannelData(self, img, li, chid): 
        # save p as a file suitable for lossifier
        fn_orig = make_filename("%s_%02d" % (li.fname, chid), self.ll_ext)
        img.save(fn_orig)
        sz_orig = os.stat(fn_orig)[ST_SIZE]
        progress("    from rle   (%5dk): %s" % (sz_orig/1024, fn_orig))
        # lossify
        _handle_saved(li, chid, fn_orig, img, lossifier)
        # clear image
        img.paste(0, (img.0,img.0, img.size[0],img.size[1]))
        return "", img.tostring("raw", "L", 0, 1) # 0:stride-padding=0, 1:orientation=up


def patch_channel(f_in, f_out, h, linfo, channel_patch_info, count, patcher):
    isLayer = linfo.layernum>=0
    chlen = channel_patch_info.chlen  if isLayer else None
    rows, cols = h.rows, h.cols if chid!=-2 else linfo.mrows, linfo.mcols
    # channel header
    chpos = f_in.tell()
    compression_type, = readf(f_in, ">H")
    chlen = chlen-2  if isLayer else None
    writef(f_out, ">H", patcher.getCompressionTag(isLayer) )
    
    old_pixel_pos = f_in.tell()   
    new_pixel_pos = f_out.tell()
    
    PREDATA = [] 
    PIXELDATA = []

    # decode psd pixel data
    if compression_type == Compressions.RLE:
        # read all channels pre-data block (rlecounts)
        rlecounts = 2 * count * rows
        if isLayer and chlen < rlecounts:
            raise "channel too short for RLE row counts (need %d bytes, have %d bytes)" % (rlecounts,chlen)
        pixel_pos += rlecounts    # image data starts after RLE counts
        rlecounts_data = readf(f_in, ">%dH" % (count*rows) )
        for ch in range(count):
            chid = channel_patch_info.chid
            # read channels rle-data
            rlelen_for_channel = sum(rlecounts_data[ch*rows:(ch+1)*rows])
            if rlelen_for_channel == 0:
                progress("     0-length channel: %s skipped" % chid)
                continue            
            data = f_in.read(rlelen_for_channel)
            img_orig = Image.fromstring("L", (cols,rows), data, "packbits", "L" )
            #
            pre, pixel = patcher.getChannelData(img_orig)
            PREDATA.append( pre )
            PIXELDATA.append( pixel )            
            del img_orig

    elif compression_type == Compressions.Raw:
        for ch in range(count):
            chid = channel_patch_info.chid
            # read raw data
            datalen_for_channel = rows * cols
            if datalen_for_channel == 0:
                progress("     0-length channel: %s skipped" % _chid)
                continue            
            data = f.read(datalen_for_channel)
            img_orig = Image.fromstring("L", (cols,rows), data) #, "raw", "L" )
            #
            pre, pixel = patcher.getChannelData(img_orig)
            PREDATA.append( pre )
            PIXELDATA.append( pixel )            
            del img_orig

            # save p as a file suitable for lossifier
            _ext = lossifier.lossless_extension()
            fn_orig = make_filename("%s_%02d" % (li.fname, _chid), _ext)
            img_orig.save(fn_orig)
            sz_orig = os.stat(fn_orig)[ST_SIZE]
            progress("    from raw   (%5dk): %s" % (sz_orig/1024, fn_orig))
            # lossify
            _handle_saved(li, _chid, fn_orig, img_orig, lossifier)
            del img_orig

    elif compression_type == Compressions.ZIP:
        display_data(f, 10)
        raise "can not decode Zip"

    elif compression_type == Compressions.ZIPPrediction:
        display_data(f, 10)
        raise "can not decode ZipPrediction"
    
    else:
        raise "program flow error"

    # write new data
    # - pre-data blocks
    for chnum in range(count):
        if PREDATA[chnum]:
            f_out.write(PREDATA[chnum])
    # - pixel-data blocks
    for chnum in range(count):
        if PIXELDATA[chnum]:
            f_out.write(PIXELDATA[chnum])
    # - correct chlen in layer_info in new_file
    if isLayer:
        _pos = f_out.tell()
        new_len = len(PREDATA[0]) + len(PIXELDATA[0])
        f_out.seek(channel_patch_info.lenpos)
        writef(f_out, ">L", new_len)
        f_out.seek(_pos)
        h._len_diff =+ new_len - channel_patch_info.chlen       
    
    return
    
        
                        


class ChannelPatchInfo(object):
    __slots__ = ['lenpos',        # old position of channel length info
                 'chlen',         # old channel length
                 'chid',          # channel id, -2,-1,0,1,...
                 'layernum',      # layer sequence number
                 'chnum',         # channel sequence number in layer
                 ]
    def __init__(self, layernum, chnum, chid, lenpos, chlen):
        self.layernum = layernum
        self.chnum = chnum
        self.chid = chid
        self.lenpos = lenpos
        self.chlen = chlen
            

    
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
    patch_psd(...)

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
    # experimenting
    po("-X","--experimental-16-bit", default=False, action="store_true",       
       help="Experimental reading of 16bit-layers in PSD/7 files [%default]")
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
        
