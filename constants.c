/*
    This file is part of "psdparse"
    Copyright (C) 2004-6 Toby Thain, toby@telegraphics.com.au

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by  
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License  
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

#include "psdparse.h"

struct resdesc rdesc[] = {
	{1000,"PS2.0 mode data"},
	{1001,"Macintosh print record"},
	{1003,"PS2.0 indexed color table"},
	{1005,"ResolutionInfo"},
	{1006,"Names of the alpha channels"},
	{1007,"DisplayInfo"},
	{1008,"Caption"},
	{1009,"Border information"},
	{1010,"Background color"},
	{1011,"Print flags"},
	{1012,"Grayscale/multichannel halftoning info"},
	{1013,"Color halftoning info"},
	{1014,"Duotone halftoning info"},
	{1015,"Grayscale/multichannel transfer function"},
	{1016,"Color transfer functions"},
	{1017,"Duotone transfer functions"},
	{1018,"Duotone image info"},
	{1019,"B&W values for the dot range"},
	{1021,"EPS options"},
	{1022,"Quick Mask info"},
	{1024,"Layer state info"},
	{1025,"Working path"},
	{1026,"Layers group info"},
	{1028,"IPTC-NAA record (File Info)"},
	{1029,"Image mode for raw format files"},
	{1030,"JPEG quality"},
	{1032,"Grid and guides info"},
	{1033,"Thumbnail resource"},
	{1034,"Copyright flag"},
	{1035,"URL"},
	{1036,"Thumbnail resource"},
	{1037,"Global Angle"},
	{1038,"Color samplers resource"},
	{1039,"ICC Profile"},
	{1040,"Watermark"},
	{1041,"ICC Untagged"},
	{1042,"Effects visible"},
	{1043,"Spot Halftone"},
	{1044,"Document specific IDs"},
	{1045,"Unicode Alpha Names"},
	{1046,"Indexed Color Table Count"},
	{1047,"Transparent Index"},
	{1049,"Global Altitude"},
	{1050,"Slices"},
	{1051,"Workflow URL"},
	{1052,"Jump To XPEP"},
	{1053,"Alpha Identifiers"},
	{1054,"URL List"},
	{1057,"Version Info"},
	{2999,"Name of clipping path"},
	{10000,"Print flags info"},
	{0,NULL}
};

char *mode_names[] = {
	"Bitmap", "GrayScale", "IndexedColor", "RGBColor",
	"CMYKColor", "HSLColor", "HSBColor", "Multichannel",
	"Duotone", "LabColor", "Gray16", "RGB48",
	"Lab48", "CMYK64", "DeepMultichannel", "Duotone16"
};

char *channelsuffixes[] = {
	"", "", "", "RGB",
	"CMYK", "HSL", "HSB", "",
	"", "Lab", "", "RGB",
	"Lab", "CMYK", "", ""
};
