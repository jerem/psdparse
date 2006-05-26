# python module
"""convert to and from jpeg2000 via Windows COM TypeLib interface using Photoshop"""

import sys, os, os.path # standard

import pywintypes # pywin32
import photoshopy9 as pspy # generated from "Photoshop CS2" TypeLib with pywin32's makepy.py and renamed
from photoshopy9 import constants as pspyc

from _lossifier_base import Lossifier_Base

_LOSSY = True
_LOSSLESS = False
_FAST = True
_SLOW = False

""" {0..9} to 3-tuples of jpf-options """
_PRESETS = {
    0: (_LOSSY, 10, _FAST),
    1: (_LOSSY, 25, _FAST),
    2: (_LOSSY, 35, _FAST),
    3: (_LOSSY, 50, _FAST),
    4: (_LOSSY, 60, _FAST),
    5: (_LOSSY, 70, _SLOW),
    6: (_LOSSY, 80, _SLOW),
    7: (_LOSSY, 90, _SLOW),
    8: (_LOSSY, 100, _SLOW),
    9: (_LOSSLESS, 100, _SLOW),
    }

""" 3-tuple of jpf-option sif not found in _PRESETS """
_PRESET_DEFAULT = (_LOSSY, 80, _SLOW)
   

class Lossifier_PhotoshopCOM(Lossifier_Base):
    """Doesnt work! does not recognize the ad_j2opt oprtions. strange thing."""

    def __init__(self, opts):
        Lossifier_Base.__init__(self, opts)
    
    def lossify(self, fn_in, preset, suffix=""):
        fn_in = os.path.abspath(fn_in)
        fn_out = self.lossy_filename(fn_in, suffix=suffix)
        ps = pspy.Application()
        psid = ps.CharIDToTypeID
        #
        ps.Preferences.RulerUnits = pspy.constants.psPixels
        doc = ps.Open(fn_in)
        #
        _lossy, _qual, _fast = _PRESETS.get(preset, _PRESET_DEFAULT)
        #
        ad_jp2opt = pspy.ActionDescriptor()
        ad_jp2opt.PutBoolean( psid( "JPLS" ), _lossy ) # lossy (inverted "lossless" checkbox)
        ad_jp2opt.PutInteger( psid( "JPQL" ), _qual )  # quality
        ad_jp2opt.PutBoolean( psid( "JPFM" ), _fast )  # fast mode
        ad_jp2opt.PutBoolean( psid( "JPMD" ), False )
        ad_jp2opt.PutBoolean( psid( "JPTP" ), False )
        ad_jp2opt.PutBoolean( psid( "JPJC" ), False )
        ad_jp2opt.PutInteger( psid( "JPEH" ), 50 )    # grow enhance %
        ad_jp2opt.PutString( psid( "JPPO" ), "Growing Thumbnail" )
        #ad_jp2opt.PutString( psid( "JPRT" ), "14.4 Kbps (Cell Phone)" )
        ad_jp2opt.PutBoolean( psid( "JPCS" ), False )
        ad_jp2opt.PutString( psid( "JPCL" ), "General Device" )
        ad_jp2opt.PutString( psid( "JPWF" ), "Integer" )
        ad_jp2opt.PutString( psid( "JPTS" ), "1024 x 1024" )
        ad_jp2opt.PutBoolean( psid( "JPJX" ), False )
        ad_jp2opt.PutBoolean( psid( "JPXM" ), False )
        ad_jp2opt.PutBoolean( psid( "JPEX" ), False )
        ad_jp2opt.PutBoolean( psid( "JPIP" ), False )
        ad_jp2opt.PutBoolean( psid( "JPRP" ), False )
        ad_jp2opt.PutInteger( psid( "JPEV" ), 16 )
        ad_jp2opt.PutInteger( psid( "JPIS" ), 1 )
        ad_jp2opt.PutInteger( psid( "JPRS" ), 1 )
        if 0:
            for i in range(ad_jp2opt.Count):
                k = ad_jp2opt.GetKey(i)
                print "  XCV", k, ps.TypeIDToCharID(k),
                try: print ad_jp2opt.GetInteger(k)
                except:
                    try: print '"%s"'%ad_jp2opt.GetString(k)
                    except: print "?"
        ad_jp2 = pspy.ActionDescriptor()
        ad_jp2.PutObject( psid( "As  " ), ps.StringIDToTypeID( " JPEG 2000" ), ad_jp2opt )
        ad_jp2.PutPath( psid( "In  " ), fn_out )
        ad_jp2.PutBoolean( psid( "Cpy " ), False ) # True?
        ad_jp2.PutBoolean( psid( "AlpC" ), False )
        ps.ExecuteAction( psid( "save" ), ad_jp2, pspyc.psDisplayNoDialogs )
        doc.Close()
        return fn_out

    def unlossify(self, fn_in):
        fn_out = self.lossless_filename(fn_in)
        ps = pspy.Application()
        doc = ps.Open(fn_in)
        png_opts = pspy.PNGSaveOptions()
        png_opts.Interlaced = False
        doc.SaveAs(SaveIn=fn_out,  Options=png_opts)
        doc.Close()
        return fn_out

    def lossy_extension(self):
        """preferred extension for lossified files"""
        return 'jpf'

    def lossless_extension(self):
        """preferred extension for unlossified files"""
        return 'png'

    #  end class
    

def _test_module():
    fn0, fn1, fn2 = "c:\\temp_test.psd", "", ""
    try:
        ps = pspy.Application()
        ps.Preferences.RulerUnits = pspy.constants.psPixels
        # create some document
        doc = ps.Documents.Add(Width=320, Height=200, Name="temp_test", Mode=pspy.constants.psNewRGB)
        doc.SaveAs(fn0)
        doc.Close()
        doc = ps.Open(fn0)
        assert abs(doc.Width-320)<1 and abs(doc.Height-200)<1 # failed to create test file?
        doc.Close()    
        # test lossify
        l = Lossifier_PhotoshopCOM()
        fn1 = l.lossify(fn0, 0)
        doc = ps.Open(fn1)
        assert abs(doc.Width-320)<1 and abs(doc.Height-200)<1 
        doc.Close()
        # test unlossify
        l = Lossifier_PhotoshopCOM()
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

    
if __name__ == '__main__':
    print "Test result: ", _test_module()
    
