# python module
"""convert to and from jpeg2000 via Jasper executable

According to 
  http://www.compression.ru/video/codec_comparison/jpeg2000_codecs_comparison_en.html
Jasper has a medium compression compared to some other (mostly commercial) products.

A testsuite cycle of 90 compression executions took 22 seconds, and is therefore
slightly faster then OpenJpeg (20%).
"""

import sys, os, os.path # standard

from _lossifier_base import Lossifier_Base

""" {0..9} to jasper-options """
_PRESETS = {
    0: "-O rate=0.002",
    1: "-O rate=0.005",
    2: "-O rate=0.01",  # quite ok already
    3: "-O rate=0.02",
    4: "-O rate=0.035",
    5: "-O rate=0.06",
    6: "-O rate=0.1",
    7: "-O rate=0.15",
    8: "-O rate=0.2",
    9: "",
    }

""" jasper-option if not found in _PRESETS """
_PRESET_DEFAULT = "-O rate=0.06"
   

class Lossifier_Jasper(Lossifier_Base):

    def __init__(self, opts):
        Lossifier_Base.__init__(self, opts)
        self.lossify_exe = "jasper.exe" if not opts.lossify_exe else opts.lossify_exe
        self.unlossify_exe = "jasper.exe" if not opts.unlossify_exe else opts.unlossify_exe        


    def lossify(self, fn_in, preset, suffix=""):
        fn_out = self.lossy_filename(fn_in, suffix=suffix)
        _more = _PRESETS.get(preset, _PRESET_DEFAULT)
        cmd = "%(exe)s --input %(fn_in)s --output %(fn_out)s %(more)s -t pnm -T jp2" % {
            'exe': self.lossify_exe,
            'more': _more,
            'fn_in': fn_in,
            'fn_out': fn_out,
            }
        ret = os.system(cmd)
        if ret: # some error, probably
            raise "Command execute error (%d): '%s'" % (ret, cmd)
        return fn_out

    def unlossify(self, fn_in):
        fn_out = self.lossless_filename(fn_in)
        _more = ''
        cmd = "%(exe)s --input %(fn_in)s --output %(fn_out)s %(more)s -t jp2 -T pnm" % {
            'exe': self.unlossify_exe,
            'more': _more,
            'fn_in': fn_in,
            'fn_out': fn_out,
            }
        ret = os.system(cmd)
        if ret: # some error, probably
            raise "Command execute error (%d): '%s'" % (ret, cmd)
        return fn_out

    def lossy_extension(self):
        """preferred extension for lossified files"""
        return 'jp2'

    def lossless_extension(self):
        """preferred extension for unlossified files"""
        return 'pgm'

    #  end class

class _Any:
    pass

def _test_module():
    fn0, fn1, fn2 = "c:\\temp_test.pgm", "", ""
    try:
        opts = _Any()
        opts.lossify_exe = "contrib\\jasper.exe"
        opts.unlossify_exe = "contrib\\jasper.exe"
        l = Lossifier_Jasper(opts)
        # create some document
        import PIL.Image as Image
        p = Image.new("L", (320,200))
        p.save(fn0)
        del p
        # check if created ok
        import photoshopy9 as pspy
        ps = pspy.Application()
        doc = ps.Open(fn0)
        assert abs(doc.Width-320)<1 and abs(doc.Height-200)<1 # failed to create test file?
        doc.Close()    
        # test lossify
        fn1 = l.lossify(fn0, 0)
        doc = ps.Open(fn1)
        assert abs(doc.Width-320)<1 and abs(doc.Height-200)<1 
        doc.Close()
        # test unlossify
        fn2 = l.unlossify(fn1)
        doc = ps.Open(fn2)
        assert abs(doc.Width-320)<1 and abs(doc.Height-200)<1 
        doc.Close()
        return True
    finally:
        import os
        for fn in [ fn0, fn1, fn2 ]:
            try: os.remove(fn)
            except OSError: pass

def _test_rates():
    cmd = (
        "for i in 001 002 005 01 024 04 06 09 12 16 20 50 ; do"
        "  ./contrib/jasper.exe -f Background.pnm -F j$i.jp2 -t pnm -T jp2 -O rate=0.$i ;"
        "  ./contrib/jasper.exe -f j$i.jp2 -t jp2 -F k$i.pnm -T pnm ;"
        "done"
        )
    print cmd
    os.system(cmd)

    
if __name__ == '__main__':
    print "Test result: ", _test_module()
    
