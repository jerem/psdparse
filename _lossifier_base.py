# python module
"""Baseclass for Lossifiers"""

import sys, os, os.path # standard

class Lossifier_Base:
    
    def __init__(self, opts):
        self.opts = opts
    
    def lossy_filename(self, fn_in, suffix=""):
        return os.path.splitext(fn_in)[0] + suffix + "." + self.lossy_extension()
    
    def lossless_filename(self, fn_in):
        return os.path.splitext(fn_in)[0] + "." + self.lossless_extension()

#eof
