# python module

__all__ = [
    "MODENAMES",
    "CHANNELSUFFIXES",
    "RDESC",
    "Modes",
    "Compressions",
    ]
    
"""header mode field meanings"""
MODENAMES = [
	"Bitmap", "GrayScale", "IndexedColor", "RGBColor",
	"CMYKColor", "HSLColor", "HSBColor", "Multichannel",
	"Duotone", "LabColor", "Gray16", "RGB48",
	"Lab48", "CMYK64", "DeepMultichannel", "Duotone16"
    ]

"""@todo docstring"""
CHANNELSUFFIXES = {
    -2:"layer mask", -1:"transparancy mask",
    3:"RGB",
    4:"CMYK", 5:"HSL", 6:"HSB", 
    9:"Lab", 11:"RGB",
    12:"Lab", 13:"CMYK",
    }

"""resource id descriptions"""
RDESC = {
	1000:"PS2.0 mode data",
	1001:"Macintosh print record",
	1003:"PS2.0 indexed color table",
	1005:"ResolutionInfo",
	1006:"Names of the alpha channels",
	1007:"DisplayInfo",
	1008:"Caption",
	1009:"Border information",
	1010:"Background color",
	1011:"Print flags",
	1012:"Grayscale/multichannel halftoning info",
	1013:"Color halftoning info",
	1014:"Duotone halftoning info",
	1015:"Grayscale/multichannel transfer function",
	1016:"Color transfer functions",
	1017:"Duotone transfer functions",
	1018:"Duotone image info",
	1019:"B&W values for the dot range",
	1021:"EPS options",
	1022:"Quick Mask info",
	1024:"Layer state info",
	1025:"Working path",
	1026:"Layers group info",
	1028:"IPTC-NAA record (File Info)",
	1029:"Image mode for raw format files",
	1030:"JPEG quality",
	1032:"Grid and guides info",
	1033:"Thumbnail resource",
	1034:"Copyright flag",
	1035:"URL",
	1036:"Thumbnail resource",
	1037:"Global Angle",
	1038:"Color samplers resource",
	1039:"ICC Profile",
	1040:"Watermark",
	1041:"ICC Untagged",
	1042:"Effects visible",
	1043:"Spot Halftone",
	1044:"Document specific IDs",
	1045:"Unicode Alpha Names",
	1046:"Indexed Color Table Count",
	1047:"Transparent Index",
	1049:"Global Altitude",
	1050:"Slices",
	1051:"Workflow URL",
	1052:"Jump To XPEP",
	1053:"Alpha Identifiers",
	1054:"URL List",
	1057:"Version Info",
	2999:"Name of clipping path",
	10000:"Print flags info",
    }

class Modes:
    Bitmap       =  0
    GrayScale    =  1
    IndexedColor =  2
    RGBColor     =  3
    CMYKColor    =  4
    HSLColor     =  5
    HSBColor     =  6
    Multichannel =  7
    Duotone      =  8
    LabColor     =  9
    Gray16       = 10
    RGB48        = 11
    Lab48        = 12
    CMYK64       = 13
    DeepMultichannel = 14
    Duotone16    = 15

class Compressions:
    Raw = 0
    RLE = 1
    ZIP = 2
    ZIPPrediction = 3
    
# eof
