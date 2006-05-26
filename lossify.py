# py module
"""module that wraps all lossifiers together"""

__all__ = [
    'lossify',
    'unlossify',
    'getLossifier',
    'killLossifier',
    ]

_lossifier = None

def getLossifier(OPTS):
    """note that changes to OPTS are ignored, only the first counts"""
    global _lossifier
    if _lossifier is None:
        if OPTS.lossifier.lower() == "photoshopcom":
            from _lossifier_photoshopy import Lossifier_PhotoshopCOM as LSF
        elif OPTS.lossifier.lower() == "jasper":
            from _lossifier_jasper import Lossifier_Jasper as LSF
        elif OPTS.lossifier.lower() == "openjpeg":
            from _lossifier_openjpeg import Lossifier_OpenJpeg as LSF
        else:
            raise "Unknown lossifier:'%s' specified" % OPTS.lossifier
        _lossifier = LSF(OPTS)
    return _lossifier


def lossify(fn_in, quality_step, OPTS, suffix=""):
    """params:
    in_fn -- in filename
    quality step -- from '0 = very lossy' to '8 = a bit lossy' or '9 = lossless'
    OPTS -- further options from module optparse
    """
    return getLossifier().lossify(fn_in, quality_step, OPTS, suffix)


def unlossify(fn_in, OPTS):
    """params:
    in_fn -- in filename
    OPTS -- further options from module optparse
    """
    return getLossifier().unlossify(fn_in, OPTS)


def killLossifier():
    """after calling this getLossifier(opts) can recognizes new opts"""
    global _lossifier
    if _lossifier:
        del _lossifier
    _lossifier = None
    

class _Any:
    pass

def _test_module(engine="openjpeg", testimage=None):
    import os, os.path, stat
    import PIL.Image as Image
    import PIL.ImageChops as ImageChops
    import PIL.ImageStat as ImageStat
    import photoshopy9 as pspy # needed to check correctness of jp2 files
    # optparse mockup
    opts = _Any()
    opts.lossifier = engine
    opts.lossify_exe = ""
    opts.unlossify_exe = ""
    # init lossifier
    killLossifier()
    l = getLossifier(opts)
    fn0, fn1, fn2 = "atest_test-%s.%s" % (engine, l.lossless_extension()), "", ""
    try:
        # create some document
        if testimage:
            p = Image.open(testimage)
            p.save(fn0)
        else:
            p = Image.new("L", (320,200))
            for x in range(320):
                for y in range(200):
                    z = x/5
                    p.putpixel( (x,y), (z*z+x*y) % 255 )
            p.save(fn0)
        WIDTH, HEIGHT = p.size
        assert WIDTH>0 and HEIGHT>0
        sz0 = os.stat(fn0)[stat.ST_SIZE]
        # check base doc
        ps = pspy.Application()
        doc = ps.Open(os.path.abspath(fn0))
        assert abs(doc.Width-WIDTH)<1 and abs(doc.Height-HEIGHT)<1 # failed to create test file?
        doc.Close()
        for preset in range(10):
            # test lossify
            fn1 = l.lossify(fn0, preset, suffix="-%s" % preset)
            doc = ps.Open(os.path.abspath(fn1))
            assert abs(doc.Width-WIDTH)<1 and abs(doc.Height-HEIGHT)<1 
            doc.Close()
            sz1 = os.stat(fn1)[stat.ST_SIZE]
            # test unlossify
            fn2 = l.unlossify(fn1)
            doc = ps.Open(os.path.abspath(fn2))
            assert abs(doc.Width-WIDTH)<1 and abs(doc.Height-HEIGHT)<1 
            doc.Close()
            sz2 = os.stat(fn2)[stat.ST_SIZE]
            #
            q = Image.open(fn2)
            r = ImageChops.difference(p, q)
            istat = ImageStat.Stat(r)
            print "  %s: in=%8sb los=%8sb unl=%8sb  rms=%5.2f" % (preset, sz0, sz1, sz2, istat.rms[0])
        return True
    finally:
        import os
#        for fn in [ fn0, fn1, fn2 ]:
#            try: os.remove(fn)
#            except OSError: pass

    
if __name__ == '__main__':
    import sys
    testimage = sys.argv[1] if len(sys.argv)>1 else None
    for engine in [
        "openjpeg",
        "jasper",
        "photoshopcom",
        ]:
        print "=== Testing %s == " % engine
        try:
            x = _test_module(engine, testimage)
            print "Test Result:" , x
        except Exception, e:
            print e
            raise
    print "+++ DONE +++"
