# py script
"""test photoshop interface"""

import sys

if __name__ == "__main__":
    #
    # pywin32
    #
    try:
        import pywintypes
    except ImportError:
        print >>sys.stderr, (
            "PyWin32 Package problem.\n"
            "  - Install pywin32, see http://www.python.org/\n"
            )
        raise
    #
    # photoshop typelib python interface
    #
    try:
        print "Testing for Python interface to Photoshop..."
        import photoshopy9 as pspy
    except ImportError:
        print >>sys.stderr, (
            "No PhotoshoPy interface to Photoshop CS2 installed. Please check:\n"
            "  - make sure Photoshop CS2 is installed\n"
            "  - make sure pywin32 is installed\n"
            "  - use makepy.py (from pywin32 package) to create a python interface\n"
            "    for the TypeLib 'Adobe Photoshop 9.0 Object Library'.\n"
            "  - move the created *.py file (win32com/gen_py/) to here\n"
            "    as photoshopy9.py and remove the *.pyc file.\n"
            )
        raise
    #
    # photoshop, JPEG2000
    #
    try:
        print "- found pylib version '%d.%d'" % (pspy.MajorVersion, pspy.MinorVersion)
        ps = pspy.Application()
        print "- found photoshop version '%s'" % ps.Version
        print "- found photoshop name '%s'" % ps.Name
        print "- found photoshop free memory '%s'MB" % (ps.FreeMemory/1024/1024)
        print "Check for jpeg2000 save possibility..."
        psid = ps.CharIDToTypeID
        #
        ps.Preferences.RulerUnits = pspy.constants.psPixels
        doc = ps.Documents.Add(Width=320, Height=200, Name="pytry", Mode=pspy.constants.psNewRGB)
        #
        ad_jp2opt = pspy.ActionDescriptor();
        ad_jp2opt.PutBoolean( psid( "JPLS" ), True );  # lossy (inverted "lossless" checkbox)
        ad_jp2opt.PutInteger( psid( "JPQL" ), 10 );    # quality
        ad_jp2opt.PutBoolean( psid( "JPFM" ), False ); # fast mode
        ad_jp2opt.PutBoolean( psid( "JPMD" ), False );
        ad_jp2opt.PutBoolean( psid( "JPTP" ), False );
        ad_jp2opt.PutBoolean( psid( "JPJC" ), True );
        ad_jp2opt.PutInteger( psid( "JPEH" ), 50 );    # grow enhance %
        ad_jp2opt.PutString( psid( "JPPO" ), "Growing Thumbnail" );
        #ad_jp2opt.PutString( psid( "JPRT" ), "14.4 Kbps (Cell Phone)" );
        ad_jp2opt.PutBoolean( psid( "JPCS" ), False );
        ad_jp2opt.PutString( psid( "JPCL" ), "General Device" );
        ad_jp2opt.PutString( psid( "JPWF" ), "Integer" );
        ad_jp2opt.PutString( psid( "JPTS" ), "1024 x 1024" );
        ad_jp2opt.PutBoolean( psid( "JPJX" ), False );
        ad_jp2opt.PutBoolean( psid( "JPXM" ), False );
        ad_jp2opt.PutBoolean( psid( "JPEX" ), False );
        ad_jp2opt.PutBoolean( psid( "JPIP" ), False );
        ad_jp2opt.PutBoolean( psid( "JPRP" ), False );
        ad_jp2opt.PutInteger( psid( "JPEV" ), 16 );
        ad_jp2opt.PutInteger( psid( "JPIS" ), 1 );
        ad_jp2opt.PutInteger( psid( "JPRS" ), 1 );
        ad_jp2 = pspy.ActionDescriptor()
        ad_jp2.PutObject( psid( "As  " ), ps.StringIDToTypeID( " JPEG 2000" ), ad_jp2opt );
        ad_jp2.PutPath( psid( "In  " ), "C:\\temp_pytry.jpf" );
        ad_jp2.PutBoolean( psid( "Cpy " ), True );
        ps.ExecuteAction( psid( "save" ), ad_jp2, pspy.constants.psDisplayNoDialogs );
        doc.Close()
        print "Check to load created jpeg2000 file..."
        doc = ps.Open("C:\\temp_pytry.jpf")
        if doc.Width != 320: raise "Reloaded file has unexpected width: %s" % doc.Width
        if doc.Height != 200: raise "Reloaded file has unexpected height: %s" % doc.Height
        doc.Close()
    except pywintypes.com_error:
        print >>sys.stderr, (
            "Problems handling using Photoshop and/or Jpeg2000. Please check:\n"
            "  - check that your Photoshop Version is CS2 (aka 9.0) compatible.\n"
            "  - check if you can save 'JPEG 2000' files as '*.jpf'; if not, consult\n"
            "    Photoshop documentation, maybe import filter from Photoshop CD is needed.\n"
            )
        raise
    #
    # PIL
    # 
    try:
        print "Testing for PIL availibiity..."
        import PIL.Image
        p = PIL.Image.new("L", (320,200))
        p.save("c:\\temp_pil.png")
    except ImportError:
        print >>sys.stderr, (
            "Problems importing PIL. Please check:\n"
            "  - make sure PIL (python image library) is installed\n"
            )
        raise
    except KeyError:
        print >>sys.stderr, (
            "Problems saving PNG with PIL. Please check:\n"
            "  - make sure your PIL version has PNG support\n"
            )
        raise
    print "All fine."
