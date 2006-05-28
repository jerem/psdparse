# python module
"""convert to and from jpeg2000 via OpenJpeg Executables.

OpenJpeg seems to compress a bit better (about 10%) at equal PSNR levels.

A testsuite cycle of 90 compression executions took 27 seconds, and is therefore
slightly slower then jasper (20%).

"""

import sys, os, os.path # standard

from _lossifier_base import Lossifier_Base

""" {0..9} rate options """
_PRESETS = {
    0: "-q 13",
    1: "-q 19",
    2: "-q 24",
    3: "-q 28",
    4: "-q 33",
    5: "-q 38",
    6: "-q 44",
    7: "-q 48",
    8: "-q 51",
    9: "-r 1",
    }

""" rate option if not found in _PRESETS """
_PRESET_DEFAULT = "-q 38"
   

class Lossifier_OpenJpeg(Lossifier_Base):

    def __init__(self, opts):
        Lossifier_Base.__init__(self, opts)
        self.lossify_exe = "image_to_j2k.exe" if not opts.lossify_exe else opts.lossify_exe
        self.unlossify_exe = "j2k_to_image.exe" if not opts.unlossify_exe else opts.unlossify_exe        


    def lossify(self, fn_in, preset, suffix=""):
        fn_out = self.lossy_filename(fn_in, suffix=suffix)
        _more = _PRESETS.get(preset, _PRESET_DEFAULT)
        cmd = "%(exe)s -i %(fn_in)s -o %(fn_out)s %(more)s" % {
            'exe': self.lossify_exe,
            'more': _more,
            'fn_in': fn_in,
            'fn_out': fn_out,
            }
        if 1:
            # use os.system(), dont capture streams, access to return code
            ret = os.system(cmd)
            if ret: # some error, probably
                raise "Command execute error (%d): '%s'" % (ret, cmd)
        elif 0:
            # use os.popen(), capture stdout, access to return code
            # -> alas, no success in capturing output
            cmdout = os.popen(cmd, "rt")
            output = cmdout.read()
            if cmdout.close() is not None:
                print output
                raise "Command execute error (%d): '%s'" % (ret, cmd)
        else:
            # use os.popen4(), capture stderr+stdout, no access to return code (on windows)
            # -> also no success in capturing output. strange. hrmph :-(
            (cmdin, cmdout) = os.popen4(cmd)
            output = cmdout.read()
            try:
                cmdin.close()
                cmdout.close()
            except IOError:
                print output
                raise "Command execute fail (%d): '%s'" % (ret, cmd)
            if output.find('[ERROR]') >= 0:
                print output
                raise "Command execute error (%d): '%s'" % (ret, cmd)
        return fn_out

    def unlossify(self, fn_in):
        fn_out = self.lossless_filename(fn_in)
        _more = ''
        cmd = "%(exe)s -i %(fn_in)s -o %(fn_out)s %(more)s" % {
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
        opts.lossify_exe = "contrib\\image_to_j2k.exe"
        opts.unlossify_exe = "contrib\\j2k_to_image.exe"
        l = Lossifier_OpenJpeg(opts)
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
        "for i in 13 19 24 28 33 38 44 48 51 ; do"
        "  ./contrib/image_to_j2k.exe -i Background.pnm -o x$i.jp2 -q $i ;"
        "done"
        )
    print cmd
    os.system(cmd)

    
if __name__ == '__main__':
    print "Test result: ", _test_module()
    
