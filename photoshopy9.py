# -*- coding: mbcs -*-
# Created by makepy.py version 0.4.91
# By python version 2.3.5 (#62, Feb  8 2005, 16:23:02) [MSC v.1200 32 bit (Intel)]
# From type library 'ScriptingSupport.8li'
# On Fri Sep 30 18:52:17 2005
"""Adobe Photoshop 9.0 Object Library"""
makepy_version = '0.4.91'
python_version = 0x20305f0

import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing and pythoncom.Empty
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{E891EE9A-D0AE-4CB4-8871-F92C0109F18E}')
MajorVersion = 9
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	psAbsolute                    =0x2        # from enum PsAdjustmentReference
	psRelative                    =0x1        # from enum PsAdjustmentReference
	psBottomCenter                =0x8        # from enum PsAnchorPosition
	psBottomLeft                  =0x7        # from enum PsAnchorPosition
	psBottomRight                 =0x9        # from enum PsAnchorPosition
	psMiddleCenter                =0x5        # from enum PsAnchorPosition
	psMiddleLeft                  =0x4        # from enum PsAnchorPosition
	psMiddleRight                 =0x6        # from enum PsAnchorPosition
	psTopCenter                   =0x2        # from enum PsAnchorPosition
	psTopLeft                     =0x1        # from enum PsAnchorPosition
	psTopRight                    =0x3        # from enum PsAnchorPosition
	psCrisp                       =0x3        # from enum PsAntiAlias
	psNoAntialias                 =0x1        # from enum PsAntiAlias
	psSharp                       =0x2        # from enum PsAntiAlias
	psSmooth                      =0x5        # from enum PsAntiAlias
	psStrong                      =0x4        # from enum PsAntiAlias
	psManual                      =0x1        # from enum PsAutoKernType
	psMetrics                     =0x2        # from enum PsAutoKernType
	psOptical                     =0x3        # from enum PsAutoKernType
	psBMP16Bits                   =0x10       # from enum PsBMPDepthType
	psBMP1Bit                     =0x1        # from enum PsBMPDepthType
	psBMP24Bits                   =0x18       # from enum PsBMPDepthType
	psBMP32Bits                   =0x20       # from enum PsBMPDepthType
	psBMP4Bits                    =0x4        # from enum PsBMPDepthType
	psBMP8Bits                    =0x8        # from enum PsBMPDepthType
	psBMP_A1R5G5B5                =0x3d       # from enum PsBMPDepthType
	psBMP_A4R4G4B4                =0x40       # from enum PsBMPDepthType
	psBMP_A8R8G8B8                =0x43       # from enum PsBMPDepthType
	psBMP_R5G6B5                  =0x3e       # from enum PsBMPDepthType
	psBMP_R8G8B8                  =0x41       # from enum PsBMPDepthType
	psBMP_X1R5G5B5                =0x3c       # from enum PsBMPDepthType
	psBMP_X4R4G4B4                =0x3f       # from enum PsBMPDepthType
	psBMP_X8R8G8B8                =0x42       # from enum PsBMPDepthType
	psFolder                      =0x3        # from enum PsBatchDestinationType
	psNoDestination               =0x1        # from enum PsBatchDestinationType
	psSaveAndClose                =0x2        # from enum PsBatchDestinationType
	psCustomPattern               =0x5        # from enum PsBitmapConversionType
	psDiffusionDither             =0x3        # from enum PsBitmapConversionType
	psHalfThreshold               =0x1        # from enum PsBitmapConversionType
	psHalftoneScreen              =0x4        # from enum PsBitmapConversionType
	psPatternDither               =0x2        # from enum PsBitmapConversionType
	psHalftoneCross               =0x6        # from enum PsBitmapHalfToneType
	psHalftoneDiamond             =0x2        # from enum PsBitmapHalfToneType
	psHalftoneEllipse             =0x3        # from enum PsBitmapHalfToneType
	psHalftoneLine                =0x4        # from enum PsBitmapHalfToneType
	psHalftoneRound               =0x1        # from enum PsBitmapHalfToneType
	psHalftoneSquare              =0x5        # from enum PsBitmapHalfToneType
	psDocument16Bits              =0x10       # from enum PsBitsPerChannelType
	psDocument1Bit                =0x1        # from enum PsBitsPerChannelType
	psDocument32Bits              =0x20       # from enum PsBitsPerChannelType
	psDocument8Bits               =0x8        # from enum PsBitsPerChannelType
	psColorBlend                  =0x16       # from enum PsBlendMode
	psColorBurn                   =0x6        # from enum PsBlendMode
	psColorDodge                  =0xa        # from enum PsBlendMode
	psDarken                      =0x4        # from enum PsBlendMode
	psDifference                  =0x12       # from enum PsBlendMode
	psDissolve                    =0x3        # from enum PsBlendMode
	psExclusion                   =0x13       # from enum PsBlendMode
	psHardLight                   =0xe        # from enum PsBlendMode
	psHue                         =0x14       # from enum PsBlendMode
	psLighten                     =0x8        # from enum PsBlendMode
	psLinearBurn                  =0x7        # from enum PsBlendMode
	psLinearDodge                 =0xb        # from enum PsBlendMode
	psLinearLight                 =0x10       # from enum PsBlendMode
	psLuminosity                  =0x17       # from enum PsBlendMode
	psMultiply                    =0x5        # from enum PsBlendMode
	psNormalBlend                 =0x2        # from enum PsBlendMode
	psOverlay                     =0xc        # from enum PsBlendMode
	psPassThrough                 =0x1        # from enum PsBlendMode
	psPinLight                    =0x11       # from enum PsBlendMode
	psSaturationBlend             =0x15       # from enum PsBlendMode
	psScreen                      =0x9        # from enum PsBlendMode
	psSoftLight                   =0xd        # from enum PsBlendMode
	psVividLight                  =0xf        # from enum PsBlendMode
	psIBMByteOrder                =0x1        # from enum PsByteOrderType
	psMacOSByteOrder              =0x2        # from enum PsByteOrderType
	psCameraDefault               =0x0        # from enum PsCameraRAWSettingsType
	psCustomSettings              =0x2        # from enum PsCameraRAWSettingsType
	psSelectedImage               =0x1        # from enum PsCameraRAWSettingsType
	psExtraLargeCameraRAW         =0x4        # from enum PsCameraRAWSize
	psLargeCameraRAW              =0x3        # from enum PsCameraRAWSize
	psMaximumCameraRAW            =0x5        # from enum PsCameraRAWSize
	psMediumCameraRAW             =0x2        # from enum PsCameraRAWSize
	psMinimumCameraRAW            =0x0        # from enum PsCameraRAWSize
	psSmallCameraRAW              =0x1        # from enum PsCameraRAWSize
	psAllCaps                     =0x2        # from enum PsCase
	psNormalCase                  =0x1        # from enum PsCase
	psSmallCaps                   =0x3        # from enum PsCase
	psConvertToBitmap             =0x5        # from enum PsChangeMode
	psConvertToCMYK               =0x3        # from enum PsChangeMode
	psConvertToGrayscale          =0x1        # from enum PsChangeMode
	psConvertToIndexedColor       =0x6        # from enum PsChangeMode
	psConvertToLab                =0x4        # from enum PsChangeMode
	psConvertToMultiChannel       =0x7        # from enum PsChangeMode
	psConvertToRGB                =0x2        # from enum PsChangeMode
	psComponentChannel            =0x1        # from enum PsChannelType
	psMaskedAreaAlphaChannel      =0x2        # from enum PsChannelType
	psSelectedAreaAlphaChannel    =0x3        # from enum PsChannelType
	psSpotColorChannel            =0x4        # from enum PsChannelType
	PsColorBlendMode              =0x16       # from enum PsColorBlendMode
	psBehindBlend                 =0x18       # from enum PsColorBlendMode
	psClearBlend                  =0x19       # from enum PsColorBlendMode
	psColorBurnBlend              =0x6        # from enum PsColorBlendMode
	psColorDodgeBlend             =0xa        # from enum PsColorBlendMode
	psDarkenBlend                 =0x4        # from enum PsColorBlendMode
	psDifferenceBlend             =0x12       # from enum PsColorBlendMode
	psDissolveBlend               =0x3        # from enum PsColorBlendMode
	psExclusionBlend              =0x13       # from enum PsColorBlendMode
	psHardLightBlend              =0xe        # from enum PsColorBlendMode
	psHueBlend                    =0x14       # from enum PsColorBlendMode
	psLightenBlend                =0x8        # from enum PsColorBlendMode
	psLinearBurnBlend             =0x7        # from enum PsColorBlendMode
	psLinearDodgeBlend            =0xb        # from enum PsColorBlendMode
	psLinearLightBlend            =0x10       # from enum PsColorBlendMode
	psLuminosityBlend             =0x17       # from enum PsColorBlendMode
	psMultiplyBlend               =0x5        # from enum PsColorBlendMode
	psNormalBlendColor            =0x2        # from enum PsColorBlendMode
	psOverlayBlend                =0xc        # from enum PsColorBlendMode
	psPinLightBlend               =0x11       # from enum PsColorBlendMode
	psSaturationBlendColor        =0x15       # from enum PsColorBlendMode
	psScreenBlend                 =0x9        # from enum PsColorBlendMode
	psSoftLightBlend              =0xd        # from enum PsColorBlendMode
	psVividLightBlend             =0xf        # from enum PsColorBlendMode
	psCMYKModel                   =0x3        # from enum PsColorModel
	psGrayscaleModel              =0x1        # from enum PsColorModel
	psHSBModel                    =0x5        # from enum PsColorModel
	psLabModel                    =0x4        # from enum PsColorModel
	psNoModel                     =0x32       # from enum PsColorModel
	psRGBModel                    =0x2        # from enum PsColorModel
	psAdobeColorPicker            =0x1        # from enum PsColorPicker
	psAppleColorPicker            =0x2        # from enum PsColorPicker
	psPlugInColorPicker           =0x4        # from enum PsColorPicker
	psWindowsColorPicker          =0x3        # from enum PsColorPicker
	psCustom                      =0x3        # from enum PsColorProfileType
	psNo                          =0x1        # from enum PsColorProfileType
	psWorking                     =0x2        # from enum PsColorProfileType
	psAdaptive                    =0x2        # from enum PsColorReductionType
	psBlackWhiteReduction         =0x5        # from enum PsColorReductionType
	psCustomReduction             =0x4        # from enum PsColorReductionType
	psMacintoshColors             =0x7        # from enum PsColorReductionType
	psPerceptualReduction         =0x0        # from enum PsColorReductionType
	psRestrictive                 =0x3        # from enum PsColorReductionType
	psSFWGrayscale                =0x6        # from enum PsColorReductionType
	psSelective                   =0x1        # from enum PsColorReductionType
	psWindowsColors               =0x8        # from enum PsColorReductionType
	psAdobeRGB                    =0x0        # from enum PsColorSpaceType
	psColorMatchRGB               =0x1        # from enum PsColorSpaceType
	psProPhotoRGB                 =0x2        # from enum PsColorSpaceType
	psSRGB                        =0x3        # from enum PsColorSpaceType
	psCopyrightedWork             =0x1        # from enum PsCopyrightedType
	psPublicDomain                =0x2        # from enum PsCopyrightedType
	psUnmarked                    =0x3        # from enum PsCopyrightedType
	psDuplication                 =0x1        # from enum PsCreateFields
	psInterpolation               =0x2        # from enum PsCreateFields
	psArtBox                      =0x5        # from enum PsCropToType
	psBleedBox                    =0x3        # from enum PsCropToType
	psBoundingBox                 =0x0        # from enum PsCropToType
	psCropBox                     =0x2        # from enum PsCropToType
	psMediaBox                    =0x1        # from enum PsCropToType
	psTrimBox                     =0x4        # from enum PsCropToType
	psColorComposite              =0x3        # from enum PsDCSType
	psGrayscaleComposite          =0x2        # from enum PsDCSType
	psNoComposite                 =0x1        # from enum PsDCSType
	psImageHighlight              =0x4        # from enum PsDepthMapSource
	psLayerMask                   =0x3        # from enum PsDepthMapSource
	psNoSource                    =0x1        # from enum PsDepthMapSource
	psTransparencyChannel         =0x2        # from enum PsDepthMapSource
	psAliasType                   =0xb        # from enum PsDescValueType
	psBooleanType                 =0x5        # from enum PsDescValueType
	psClassType                   =0xa        # from enum PsDescValueType
	psDoubleType                  =0x2        # from enum PsDescValueType
	psEnumeratedType              =0x8        # from enum PsDescValueType
	psIntegerType                 =0x1        # from enum PsDescValueType
	psListType                    =0x6        # from enum PsDescValueType
	psObjectType                  =0x7        # from enum PsDescValueType
	psRawType                     =0xc        # from enum PsDescValueType
	psReferenceType               =0x9        # from enum PsDescValueType
	psStringType                  =0x4        # from enum PsDescValueType
	psUnitDoubleType              =0x3        # from enum PsDescValueType
	psDisplayAllDialogs           =0x1        # from enum PsDialogModes
	psDisplayErrorDialogs         =0x2        # from enum PsDialogModes
	psDisplayNoDialogs            =0x3        # from enum PsDialogModes
	psHorizontal                  =0x1        # from enum PsDirection
	psVertical                    =0x2        # from enum PsDirection
	psStretchToFit                =0x1        # from enum PsDisplacementMapType
	psTile                        =0x2        # from enum PsDisplacementMapType
	psDiffusion                   =0x2        # from enum PsDitherType
	psNoDither                    =0x1        # from enum PsDitherType
	psNoise                       =0x4        # from enum PsDitherType
	psPattern                     =0x3        # from enum PsDitherType
	psBackgroundColor             =0x2        # from enum PsDocumentFill
	psTransparent                 =0x3        # from enum PsDocumentFill
	psWhite                       =0x1        # from enum PsDocumentFill
	psBitmap                      =0x5        # from enum PsDocumentMode
	psCMYK                        =0x3        # from enum PsDocumentMode
	psDuotone                     =0x8        # from enum PsDocumentMode
	psGrayscale                   =0x1        # from enum PsDocumentMode
	psIndexedColor                =0x6        # from enum PsDocumentMode
	psLab                         =0x4        # from enum PsDocumentMode
	psMultiChannel                =0x7        # from enum PsDocumentMode
	psRGB                         =0x2        # from enum PsDocumentMode
	psConcise                     =0x2        # from enum PsEditLogItemsType
	psDetailed                    =0x3        # from enum PsEditLogItemsType
	psSessionOnly                 =0x1        # from enum PsEditLogItemsType
	psPlaceAfter                  =0x4        # from enum PsElementPlacement
	psPlaceAtBeginning            =0x1        # from enum PsElementPlacement
	psPlaceAtEnd                  =0x2        # from enum PsElementPlacement
	psPlaceBefore                 =0x3        # from enum PsElementPlacement
	psPlaceInside                 =0x0        # from enum PsElementPlacement
	psEvenFields                  =0x2        # from enum PsEliminateFields
	psOddFields                   =0x1        # from enum PsEliminateFields
	psIllustratorPaths            =0x1        # from enum PsExportType
	psSaveForWeb                  =0x2        # from enum PsExportType
	psLowercase                   =0x2        # from enum PsExtensionType
	psUppercase                   =0x3        # from enum PsExtensionType
	psDdmm                        =0x10       # from enum PsFileNamingType
	psDdmmyy                      =0xf        # from enum PsFileNamingType
	psDocumentNameLower           =0x2        # from enum PsFileNamingType
	psDocumentNameMixed           =0x1        # from enum PsFileNamingType
	psDocumentNameUpper           =0x3        # from enum PsFileNamingType
	psExtensionLower              =0x11       # from enum PsFileNamingType
	psExtensionUpper              =0x12       # from enum PsFileNamingType
	psMmdd                        =0xb        # from enum PsFileNamingType
	psMmddyy                      =0xa        # from enum PsFileNamingType
	psSerialLetterLower           =0x8        # from enum PsFileNamingType
	psSerialLetterUpper           =0x9        # from enum PsFileNamingType
	psSerialNumber1               =0x4        # from enum PsFileNamingType
	psSerialNumber2               =0x5        # from enum PsFileNamingType
	psSerialNumber3               =0x6        # from enum PsFileNamingType
	psSerialNumber4               =0x7        # from enum PsFileNamingType
	psYyddmm                      =0xe        # from enum PsFileNamingType
	psYymmdd                      =0xd        # from enum PsFileNamingType
	psYyyymmdd                    =0xc        # from enum PsFileNamingType
	psFontPreviewLarge            =0x3        # from enum PsFontPreviewType
	psFontPreviewMedium           =0x2        # from enum PsFontPreviewType
	psFontPreviewNone             =0x0        # from enum PsFontPreviewType
	psFontPreviewSmall            =0x1        # from enum PsFontPreviewType
	psBlackWhite                  =0x2        # from enum PsForcedColors
	psNoForced                    =0x1        # from enum PsForcedColors
	psPrimaries                   =0x3        # from enum PsForcedColors
	psWeb                         =0x4        # from enum PsForcedColors
	psOptimizedBaseline           =0x2        # from enum PsFormatOptionsType
	psProgressive                 =0x3        # from enum PsFormatOptionsType
	psStandardBaseline            =0x1        # from enum PsFormatOptionsType
	psConstrainBoth               =0x3        # from enum PsGalleryConstrainType
	psConstrainHeight             =0x2        # from enum PsGalleryConstrainType
	psConstrainWidth              =0x1        # from enum PsGalleryConstrainType
	psArial                       =0x1        # from enum PsGalleryFontType
	psCourierNew                  =0x2        # from enum PsGalleryFontType
	psHelvetica                   =0x3        # from enum PsGalleryFontType
	psTimesNewRoman               =0x4        # from enum PsGalleryFontType
	psBlackText                   =0x1        # from enum PsGallerySecurityTextColorType
	psCustomText                  =0x3        # from enum PsGallerySecurityTextColorType
	psWhiteText                   =0x2        # from enum PsGallerySecurityTextColorType
	psCentered                    =0x1        # from enum PsGallerySecurityTextPositionType
	psLowerLeft                   =0x3        # from enum PsGallerySecurityTextPositionType
	psLowerRight                  =0x5        # from enum PsGallerySecurityTextPositionType
	psUpperLeft                   =0x2        # from enum PsGallerySecurityTextPositionType
	psUpperRight                  =0x4        # from enum PsGallerySecurityTextPositionType
	psClockwise45                 =0x2        # from enum PsGallerySecurityTextRotateType
	psClockwise90                 =0x3        # from enum PsGallerySecurityTextRotateType
	psCounterClockwise45          =0x4        # from enum PsGallerySecurityTextRotateType
	psCounterClockwise90          =0x5        # from enum PsGallerySecurityTextRotateType
	psZero                        =0x1        # from enum PsGallerySecurityTextRotateType
	psCaption                     =0x5        # from enum PsGallerySecurityType
	psCopyright                   =0x4        # from enum PsGallerySecurityType
	psCredit                      =0x6        # from enum PsGallerySecurityType
	psCustomSecurityText          =0x2        # from enum PsGallerySecurityType
	psFilename                    =0x3        # from enum PsGallerySecurityType
	psNoSecurity                  =0x1        # from enum PsGallerySecurityType
	psTitle                       =0x7        # from enum PsGallerySecurityType
	psCustomThumbnail             =0x4        # from enum PsGalleryThumbSizeType
	psLarge                       =0x3        # from enum PsGalleryThumbSizeType
	psMedium                      =0x2        # from enum PsGalleryThumbSizeType
	psSmall                       =0x1        # from enum PsGalleryThumbSizeType
	psHeptagon                    =0x4        # from enum PsGeometry
	psHexagon                     =0x2        # from enum PsGeometry
	psOctagon                     =0x5        # from enum PsGeometry
	psPentagon                    =0x1        # from enum PsGeometry
	psSquareGeometry              =0x3        # from enum PsGeometry
	psTriangle                    =0x0        # from enum PsGeometry
	psGridDashedLine              =0x2        # from enum PsGridLineStyle
	psGridDottedLine              =0x3        # from enum PsGridLineStyle
	psGridSolidLine               =0x1        # from enum PsGridLineStyle
	psLargeGrid                   =0x4        # from enum PsGridSize
	psMediumGrid                  =0x3        # from enum PsGridSize
	psNoGrid                      =0x1        # from enum PsGridSize
	psSmallGrid                   =0x2        # from enum PsGridSize
	psGuideDashedLine             =0x2        # from enum PsGuideLineStyle
	psGuideSolidLine              =0x1        # from enum PsGuideLineStyle
	psAllPaths                    =0x2        # from enum PsIllustratorPathType
	psDocumentBounds              =0x1        # from enum PsIllustratorPathType
	psNamedPath                   =0x3        # from enum PsIllustratorPathType
	psAbsoluteColorimetric        =0x4        # from enum PsIntent
	psPerceptual                  =0x1        # from enum PsIntent
	psRelativeColorimetric        =0x3        # from enum PsIntent
	psSaturation                  =0x2        # from enum PsIntent
	psBeforeRunning               =0x3        # from enum PsJavaScriptExecutionMode
	psDebuggerOnError             =0x2        # from enum PsJavaScriptExecutionMode
	psNeverShowDebugger           =0x1        # from enum PsJavaScriptExecutionMode
	psCenter                      =0x2        # from enum PsJustification
	psCenterJustified             =0x5        # from enum PsJustification
	psFullyJustified              =0x7        # from enum PsJustification
	psLeft                        =0x1        # from enum PsJustification
	psLeftJustified               =0x4        # from enum PsJustification
	psRight                       =0x3        # from enum PsJustification
	psRightJustified              =0x6        # from enum PsJustification
	psBrazillianPortuguese        =0xd        # from enum PsLanguage
	psCanadianFrench              =0x4        # from enum PsLanguage
	psDanish                      =0x11       # from enum PsLanguage
	psDutch                       =0x10       # from enum PsLanguage
	psEnglishUK                   =0x2        # from enum PsLanguage
	psEnglishUSA                  =0x1        # from enum PsLanguage
	psFinnish                     =0x5        # from enum PsLanguage
	psFrench                      =0x3        # from enum PsLanguage
	psGerman                      =0x6        # from enum PsLanguage
	psItalian                     =0x9        # from enum PsLanguage
	psNorwegian                   =0xa        # from enum PsLanguage
	psNynorskNorwegian            =0xb        # from enum PsLanguage
	psOldGerman                   =0x7        # from enum PsLanguage
	psPortuguese                  =0xc        # from enum PsLanguage
	psSpanish                     =0xe        # from enum PsLanguage
	psSwedish                     =0xf        # from enum PsLanguage
	psSwissGerman                 =0x8        # from enum PsLanguage
	psRLELayerCompression         =0x1        # from enum PsLayerCompressionType
	psZIPLayerCompression         =0x2        # from enum PsLayerCompressionType
	psBrightnessContrastLayer     =0x9        # from enum PsLayerKind
	psChannelMixerLayer           =0xc        # from enum PsLayerKind
	psColorBalanceLayer           =0x8        # from enum PsLayerKind
	psCurvesLayer                 =0x7        # from enum PsLayerKind
	psGradientFillLayer           =0x4        # from enum PsLayerKind
	psGradientMapLayer            =0xd        # from enum PsLayerKind
	psHueSaturationLayer          =0xa        # from enum PsLayerKind
	psInversionLayer              =0xe        # from enum PsLayerKind
	psLevelsLayer                 =0x6        # from enum PsLayerKind
	psNormalLayer                 =0x1        # from enum PsLayerKind
	psPatternFillLayer            =0x5        # from enum PsLayerKind
	psPosterizeLayer              =0x10       # from enum PsLayerKind
	psSelectiveColorLayer         =0xb        # from enum PsLayerKind
	psSmartObjectLayer            =0x11       # from enum PsLayerKind
	psSolidFillLayer              =0x3        # from enum PsLayerKind
	psTextLayer                   =0x2        # from enum PsLayerKind
	psThresholdLayer              =0xf        # from enum PsLayerKind
	psArtLayer                    =0x1        # from enum PsLayerType
	psLayerSet                    =0x2        # from enum PsLayerType
	psMoviePrime                  =0x5        # from enum PsLensType
	psPrime105                    =0x3        # from enum PsLensType
	psPrime35                     =0x2        # from enum PsLensType
	psZoomLens                    =0x1        # from enum PsLensType
	psActualSize                  =0x0        # from enum PsMagnificationType
	psFitPage                     =0x1        # from enum PsMagnificationType
	psBackgroundColorMatte        =0x3        # from enum PsMatteType
	psBlackMatte                  =0x5        # from enum PsMatteType
	psForegroundColorMatte        =0x2        # from enum PsMatteType
	psNetscapeGrayMatte           =0x7        # from enum PsMatteType
	psNoMatte                     =0x1        # from enum PsMatteType
	psSemiGray                    =0x6        # from enum PsMatteType
	psWhiteMatte                  =0x4        # from enum PsMatteType
	psNewBitmap                   =0x5        # from enum PsNewDocumentMode
	psNewCMYK                     =0x3        # from enum PsNewDocumentMode
	psNewGray                     =0x1        # from enum PsNewDocumentMode
	psNewLab                      =0x4        # from enum PsNewDocumentMode
	psNewRGB                      =0x2        # from enum PsNewDocumentMode
	psGaussianNoise               =0x2        # from enum PsNoiseDistribution
	psUniformNoise                =0x1        # from enum PsNoiseDistribution
	psOffsetRepeatEdgePixels      =0x3        # from enum PsOffsetUndefinedAreas
	psOffsetSetToLayerFill        =0x1        # from enum PsOffsetUndefinedAreas
	psOffsetWrapAround            =0x2        # from enum PsOffsetUndefinedAreas
	psOpenCMYK                    =0x3        # from enum PsOpenDocumentMode
	psOpenGray                    =0x1        # from enum PsOpenDocumentMode
	psOpenLab                     =0x4        # from enum PsOpenDocumentMode
	psOpenRGB                     =0x2        # from enum PsOpenDocumentMode
	psAcrobatTouchUpImageOpen     =0x14       # from enum PsOpenDocumentType
	psAliasPIXOpen                =0x19       # from enum PsOpenDocumentType
	psBMPOpen                     =0x2        # from enum PsOpenDocumentType
	psCameraRAWOpen               =0x20       # from enum PsOpenDocumentType
	psCompuServeGIFOpen           =0x3        # from enum PsOpenDocumentType
	psEPSOpen                     =0x16       # from enum PsOpenDocumentType
	psEPSPICTPreviewOpen          =0x17       # from enum PsOpenDocumentType
	psEPSTIFFPreviewOpen          =0x18       # from enum PsOpenDocumentType
	psElectricImageOpen           =0x1a       # from enum PsOpenDocumentType
	psFilmstripOpen               =0x5        # from enum PsOpenDocumentType
	psJPEGOpen                    =0x6        # from enum PsOpenDocumentType
	psPCXOpen                     =0x7        # from enum PsOpenDocumentType
	psPDFOpen                     =0x15       # from enum PsOpenDocumentType
	psPICTFileFormatOpen          =0xa        # from enum PsOpenDocumentType
	psPICTResourceFormatOpen      =0xb        # from enum PsOpenDocumentType
	psPNGOpen                     =0xd        # from enum PsOpenDocumentType
	psPhotoCDOpen                 =0x9        # from enum PsOpenDocumentType
	psPhotoshopDCS_1Open          =0x12       # from enum PsOpenDocumentType
	psPhotoshopDCS_2Open          =0x13       # from enum PsOpenDocumentType
	psPhotoshopEPSOpen            =0x4        # from enum PsOpenDocumentType
	psPhotoshopOpen               =0x1        # from enum PsOpenDocumentType
	psPhotoshopPDFOpen            =0x8        # from enum PsOpenDocumentType
	psPixarOpen                   =0xc        # from enum PsOpenDocumentType
	psPortableBitmapOpen          =0x1b       # from enum PsOpenDocumentType
	psRawOpen                     =0xe        # from enum PsOpenDocumentType
	psSGIRGBOpen                  =0x1d       # from enum PsOpenDocumentType
	psScitexCTOpen                =0xf        # from enum PsOpenDocumentType
	psSoftImageOpen               =0x1e       # from enum PsOpenDocumentType
	psTIFFOpen                    =0x11       # from enum PsOpenDocumentType
	psTargaOpen                   =0x10       # from enum PsOpenDocumentType
	psWavefrontRLAOpen            =0x1c       # from enum PsOpenDocumentType
	psWirelessBitmapOpen          =0x1f       # from enum PsOpenDocumentType
	psOS2                         =0x1        # from enum PsOperatingSystem
	psWindows                     =0x2        # from enum PsOperatingSystem
	psLandscape                   =0x1        # from enum PsOrientation
	psPortrait                    =0x2        # from enum PsOrientation
	psPreciseOther                =0x2        # from enum PsOtherPaintingCursors
	psStandardOther               =0x1        # from enum PsOtherPaintingCursors
	psPDF13                       =0x1        # from enum PsPDFCompatibilityType
	psPDF14                       =0x2        # from enum PsPDFCompatibilityType
	psPDF15                       =0x3        # from enum PsPDFCompatibilityType
	psPDF16                       =0x4        # from enum PsPDFCompatibilityType
	psPDFJPEG                     =0x2        # from enum PsPDFEncodingType
	psPDFJPEG2000HIGH             =0x9        # from enum PsPDFEncodingType
	psPDFJPEG2000LOSSLESS         =0xe        # from enum PsPDFEncodingType
	psPDFJPEG2000LOW              =0xd        # from enum PsPDFEncodingType
	psPDFJPEG2000MED              =0xb        # from enum PsPDFEncodingType
	psPDFJPEG2000MEDHIGH          =0xa        # from enum PsPDFEncodingType
	psPDFJPEG2000MEDLOW           =0xc        # from enum PsPDFEncodingType
	psPDFJPEGHIGH                 =0x4        # from enum PsPDFEncodingType
	psPDFJPEGLOW                  =0x8        # from enum PsPDFEncodingType
	psPDFJPEGMED                  =0x6        # from enum PsPDFEncodingType
	psPDFJPEGMEDHIGH              =0x5        # from enum PsPDFEncodingType
	psPDFJPEGMEDLOW               =0x7        # from enum PsPDFEncodingType
	psPDFNone                     =0x0        # from enum PsPDFEncodingType
	psPDFZip                      =0x1        # from enum PsPDFEncodingType
	psPDFZip4Bit                  =0x3        # from enum PsPDFEncodingType
	psNoResample                  =0x0        # from enum PsPDFResampleType
	psPDFAverage                  =0x1        # from enum PsPDFResampleType
	psPDFBicubic                  =0x3        # from enum PsPDFResampleType
	psPDFSubSample                =0x2        # from enum PsPDFResampleType
	psNoStandard                  =0x0        # from enum PsPDFStandardType
	psPDFX1A2001                  =0x1        # from enum PsPDFStandardType
	psPDFX1A2003                  =0x2        # from enum PsPDFStandardType
	psPDFX32002                   =0x3        # from enum PsPDFStandardType
	psPDFX32003                   =0x4        # from enum PsPDFStandardType
	psPICT16Bits                  =0x10       # from enum PsPICTBitsPerPixels
	psPICT2Bits                   =0x2        # from enum PsPICTBitsPerPixels
	psPICT32Bits                  =0x20       # from enum PsPICTBitsPerPixels
	psPICT4Bits                   =0x4        # from enum PsPICTBitsPerPixels
	psPICT8Bits                   =0x8        # from enum PsPICTBitsPerPixels
	psJPEGHighPICT                =0x5        # from enum PsPICTCompression
	psJPEGLowPICT                 =0x2        # from enum PsPICTCompression
	psJPEGMaximumPICT             =0x6        # from enum PsPICTCompression
	psJPEGMediumPICT              =0x4        # from enum PsPICTCompression
	psNoPICTCompression           =0x1        # from enum PsPICTCompression
	psBrushSize                   =0x3        # from enum PsPaintingCursors
	psPrecise                     =0x2        # from enum PsPaintingCursors
	psStandard                    =0x1        # from enum PsPaintingCursors
	psExact                       =0x1        # from enum PsPaletteType
	psLocalAdaptive               =0x8        # from enum PsPaletteType
	psLocalPerceptual             =0x6        # from enum PsPaletteType
	psLocalSelective              =0x7        # from enum PsPaletteType
	psMacOSPalette                =0x2        # from enum PsPaletteType
	psMasterAdaptive              =0xb        # from enum PsPaletteType
	psMasterPerceptual            =0x9        # from enum PsPaletteType
	psMasterSelective             =0xa        # from enum PsPaletteType
	psPreviousPalette             =0xc        # from enum PsPaletteType
	psUniform                     =0x5        # from enum PsPaletteType
	psWebPalette                  =0x4        # from enum PsPaletteType
	psWindowsPalette              =0x3        # from enum PsPaletteType
	psClippingPath                =0x2        # from enum PsPathKind
	psNormalPath                  =0x1        # from enum PsPathKind
	psTextMask                    =0x5        # from enum PsPathKind
	psVectorMask                  =0x4        # from enum PsPathKind
	psWorkPath                    =0x3        # from enum PsPathKind
	psLab16                       =0x4        # from enum PsPhotoCDColorSpace
	psLab8                        =0x3        # from enum PsPhotoCDColorSpace
	psRGB16                       =0x2        # from enum PsPhotoCDColorSpace
	psRGB8                        =0x1        # from enum PsPhotoCDColorSpace
	psExtraLargePhotoCD           =0x5        # from enum PsPhotoCDSize
	psLargePhotoCD                =0x4        # from enum PsPhotoCDSize
	psMaximumPhotoCD              =0x6        # from enum PsPhotoCDSize
	psMediumPhotoCD               =0x3        # from enum PsPhotoCDSize
	psMinimumPhotoCD              =0x1        # from enum PsPhotoCDSize
	psSmallPhotoCD                =0x2        # from enum PsPhotoCDSize
	psCaptionText                 =0x5        # from enum PsPicturePackageTextType
	psCopyrightText               =0x4        # from enum PsPicturePackageTextType
	psCreditText                  =0x6        # from enum PsPicturePackageTextType
	psFilenameText                =0x3        # from enum PsPicturePackageTextType
	psNoText                      =0x1        # from enum PsPicturePackageTextType
	psOriginText                  =0x7        # from enum PsPicturePackageTextType
	psUserText                    =0x2        # from enum PsPicturePackageTextType
	psCornerPoint                 =0x2        # from enum PsPointKind
	psSmoothPoint                 =0x1        # from enum PsPointKind
	psPostScriptPoints            =0x1        # from enum PsPointType
	psTraditionalPoints           =0x2        # from enum PsPointType
	psPolarToRectangular          =0x2        # from enum PsPolarConversionType
	psRectangularToPolar          =0x1        # from enum PsPolarConversionType
	psEightBitTIFF                =0x3        # from enum PsPreviewType
	psMonochromeTIFF              =0x2        # from enum PsPreviewType
	psNoPreview                   =0x1        # from enum PsPreviewType
	psAsciiEncoding               =0x3        # from enum PsPrintEncoding
	psBinaryEncoding              =0x1        # from enum PsPrintEncoding
	psJPEGEncoding                =0x2        # from enum PsPrintEncoding
	psAllCaches                   =0x4        # from enum PsPurgeTarget
	psClipboardCache              =0x3        # from enum PsPurgeTarget
	psHistoryCaches               =0x2        # from enum PsPurgeTarget
	psUndoCaches                  =0x1        # from enum PsPurgeTarget
	psAlways                      =0x1        # from enum PsQueryStateType
	psAsk                         =0x2        # from enum PsQueryStateType
	psNever                       =0x3        # from enum PsQueryStateType
	psSpin                        =0x1        # from enum PsRadialBlurMethod
	psZoom                        =0x2        # from enum PsRadialBlurMethod
	psRadialBlurBest              =0x3        # from enum PsRadialBlurQuality
	psRadialBlurDraft             =0x1        # from enum PsRadialBlurQuality
	psRadialBlurGood              =0x2        # from enum PsRadialBlurQuality
	psEntireLayer                 =0x5        # from enum PsRasterizeType
	psFillContent                 =0x3        # from enum PsRasterizeType
	psLayerClippingPath           =0x4        # from enum PsRasterizeType
	psLinkedLayers                =0x6        # from enum PsRasterizeType
	psShape                       =0x2        # from enum PsRasterizeType
	psTextContents                =0x1        # from enum PsRasterizeType
	psReferenceClassType          =0x7        # from enum PsReferenceFormType
	psReferenceEnumeratedType     =0x5        # from enum PsReferenceFormType
	psReferenceIdentifierType     =0x3        # from enum PsReferenceFormType
	psReferenceIndexType          =0x2        # from enum PsReferenceFormType
	psReferenceNameType           =0x1        # from enum PsReferenceFormType
	psReferenceOffsetType         =0x4        # from enum PsReferenceFormType
	psReferencePropertyType       =0x6        # from enum PsReferenceFormType
	psBicubic                     =0x4        # from enum PsResampleMethod
	psBicubicSharper              =0x5        # from enum PsResampleMethod
	psBicubicSmoother             =0x6        # from enum PsResampleMethod
	psBilinear                    =0x3        # from enum PsResampleMethod
	psNearestNeighbor             =0x2        # from enum PsResampleMethod
	psNoResampling                =0x1        # from enum PsResampleMethod
	psAllTools                    =0x2        # from enum PsResetTarget
	psAllWarnings                 =0x1        # from enum PsResetTarget
	psEverything                  =0x3        # from enum PsResetTarget
	psLargeRipple                 =0x3        # from enum PsRippleSize
	psMediumRipple                =0x2        # from enum PsRippleSize
	psSmallRipple                 =0x1        # from enum PsRippleSize
	psAlwaysSave                  =0x2        # from enum PsSaveBehavior
	psAskWhenSaving               =0x3        # from enum PsSaveBehavior
	psNeverSave                   =0x1        # from enum PsSaveBehavior
	psAliasPIXSave                =0x19       # from enum PsSaveDocumentType
	psBMPSave                     =0x2        # from enum PsSaveDocumentType
	psCompuServeGIFSave           =0x3        # from enum PsSaveDocumentType
	psElectricImageSave           =0x1a       # from enum PsSaveDocumentType
	psJPEGSave                    =0x6        # from enum PsSaveDocumentType
	psPCXSave                     =0x7        # from enum PsSaveDocumentType
	psPICTFileFormatSave          =0xa        # from enum PsSaveDocumentType
	psPICTResourceFormatSave      =0xb        # from enum PsSaveDocumentType
	psPNGSave                     =0xd        # from enum PsSaveDocumentType
	psPhotoshopDCS_1Save          =0x12       # from enum PsSaveDocumentType
	psPhotoshopDCS_2Save          =0x13       # from enum PsSaveDocumentType
	psPhotoshopEPSSave            =0x4        # from enum PsSaveDocumentType
	psPhotoshopPDFSave            =0x8        # from enum PsSaveDocumentType
	psPhotoshopSave               =0x1        # from enum PsSaveDocumentType
	psPixarSave                   =0xc        # from enum PsSaveDocumentType
	psPortableBitmapSave          =0x1b       # from enum PsSaveDocumentType
	psRawSave                     =0xe        # from enum PsSaveDocumentType
	psSGIRGBSave                  =0x1d       # from enum PsSaveDocumentType
	psScitexCTSave                =0xf        # from enum PsSaveDocumentType
	psSoftImageSave               =0x1e       # from enum PsSaveDocumentType
	psTIFFSave                    =0x11       # from enum PsSaveDocumentType
	psTargaSave                   =0x10       # from enum PsSaveDocumentType
	psWavefrontRLASave            =0x1c       # from enum PsSaveDocumentType
	psWirelessBitmapSave          =0x1f       # from enum PsSaveDocumentType
	psAscii                       =0x3        # from enum PsSaveEncoding
	psBinary                      =0x1        # from enum PsSaveEncoding
	psJPEGHigh                    =0x5        # from enum PsSaveEncoding
	psJPEGLow                     =0x2        # from enum PsSaveEncoding
	psJPEGMaximum                 =0x6        # from enum PsSaveEncoding
	psJPEGMedium                  =0x4        # from enum PsSaveEncoding
	psLogFile                     =0x2        # from enum PsSaveLogItemsType
	psLogFileAndMetadata          =0x3        # from enum PsSaveLogItemsType
	psMetadata                    =0x1        # from enum PsSaveLogItemsType
	psDoNotSaveChanges            =0x2        # from enum PsSaveOptions
	psPromptToSaveChanges         =0x3        # from enum PsSaveOptions
	psSaveChanges                 =0x1        # from enum PsSaveOptions
	psDiminishSelection           =0x3        # from enum PsSelectionType
	psExtendSelection             =0x2        # from enum PsSelectionType
	psIntersectSelection          =0x4        # from enum PsSelectionType
	psReplaceSelection            =0x1        # from enum PsSelectionType
	psShapeAdd                    =0x1        # from enum PsShapeOperation
	psShapeIntersect              =0x3        # from enum PsShapeOperation
	psShapeSubtract               =0x4        # from enum PsShapeOperation
	psShapeXOR                    =0x2        # from enum PsShapeOperation
	psSmartBlurEdgeOnly           =0x2        # from enum PsSmartBlurMode
	psSmartBlurNormal             =0x1        # from enum PsSmartBlurMode
	psSmartBlurOverlayEdge        =0x3        # from enum PsSmartBlurMode
	psSmartBlurHigh               =0x3        # from enum PsSmartBlurQuality
	psSmartBlurLow                =0x1        # from enum PsSmartBlurQuality
	psSmartBlurMedium             =0x2        # from enum PsSmartBlurQuality
	psDocumentSpace               =0x1        # from enum PsSourceSpaceType
	psProofSpace                  =0x2        # from enum PsSourceSpaceType
	psHorizontalSpherize          =0x2        # from enum PsSpherizeMode
	psNormalSpherize              =0x1        # from enum PsSpherizeMode
	psVerticalSpherize            =0x3        # from enum PsSpherizeMode
	psStrikeBox                   =0x3        # from enum PsStrikeThruType
	psStrikeHeight                =0x2        # from enum PsStrikeThruType
	psStrikeOff                   =0x1        # from enum PsStrikeThruType
	psCenterStroke                =0x2        # from enum PsStrokeLocation
	psInsideStroke                =0x1        # from enum PsStrokeLocation
	psOutsideStroke               =0x3        # from enum PsStrokeLocation
	psTarga16Bits                 =0x10       # from enum PsTargaBitsPerPixels
	psTarga24Bits                 =0x18       # from enum PsTargaBitsPerPixels
	psTarga32Bits                 =0x20       # from enum PsTargaBitsPerPixels
	psAdobeEveryLine              =0x2        # from enum PsTextComposer
	psAdobeSingleLine             =0x1        # from enum PsTextComposer
	psParagraphText               =0x2        # from enum PsTextType
	psPointText                   =0x1        # from enum PsTextType
	psBlocksTexture               =0x1        # from enum PsTextureType
	psCanvasTexture               =0x2        # from enum PsTextureType
	psFrostedTexture              =0x3        # from enum PsTextureType
	psTextureFile                 =0x5        # from enum PsTextureType
	psTinyLensTexture             =0x4        # from enum PsTextureType
	psNoTIFFCompression           =0x1        # from enum PsTiffEncodingType
	psTiffJPEG                    =0x3        # from enum PsTiffEncodingType
	psTiffLZW                     =0x2        # from enum PsTiffEncodingType
	psTiffZIP                     =0x4        # from enum PsTiffEncodingType
	psArtHistoryBrush             =0x9        # from enum PsToolType
	psBackgroundEraser            =0x4        # from enum PsToolType
	psBlur                        =0xb        # from enum PsToolType
	psBrush                       =0x2        # from enum PsToolType
	psBurn                        =0xe        # from enum PsToolType
	psCloneStamp                  =0x5        # from enum PsToolType
	psColorReplacementTool        =0x10       # from enum PsToolType
	psDodge                       =0xd        # from enum PsToolType
	psEraser                      =0x3        # from enum PsToolType
	psHealingBrush                =0x7        # from enum PsToolType
	psHistoryBrush                =0x8        # from enum PsToolType
	psPatternStamp                =0x6        # from enum PsToolType
	psPencil                      =0x1        # from enum PsToolType
	psSharpen                     =0xc        # from enum PsToolType
	psSmudge                      =0xa        # from enum PsToolType
	psSponge                      =0xf        # from enum PsToolType
	psBlindsHorizontal            =0x1        # from enum PsTransitionType
	psBlindsVertical              =0x2        # from enum PsTransitionType
	psBoxIn                       =0x4        # from enum PsTransitionType
	psBoxOut                      =0x5        # from enum PsTransitionType
	psDissolveTransition          =0x3        # from enum PsTransitionType
	psGlitterDown                 =0x6        # from enum PsTransitionType
	psGlitterRight                =0x7        # from enum PsTransitionType
	psGlitterRightDown            =0x8        # from enum PsTransitionType
	psNoTrasition                 =0x9        # from enum PsTransitionType
	psRandom                      =0xa        # from enum PsTransitionType
	psSplitHorizontalIn           =0xb        # from enum PsTransitionType
	psSplitHorizontalOut          =0xc        # from enum PsTransitionType
	psSplitVerticalIn             =0xd        # from enum PsTransitionType
	psSplitVerticalOut            =0xe        # from enum PsTransitionType
	psWipeDown                    =0xf        # from enum PsTransitionType
	psWipeLeft                    =0x10       # from enum PsTransitionType
	psWipeRight                   =0x11       # from enum PsTransitionType
	psWipeUp                      =0x12       # from enum PsTransitionType
	psBottomRightPixel            =0x9        # from enum PsTrimType
	psTopLeftPixel                =0x1        # from enum PsTrimType
	psTransparentPixels           =0x0        # from enum PsTrimType
	psTypeMM                      =0x4        # from enum PsTypeUnits
	psTypePixels                  =0x1        # from enum PsTypeUnits
	psTypePoints                  =0x5        # from enum PsTypeUnits
	psRepeatEdgePixels            =0x2        # from enum PsUndefinedAreas
	psWrapAround                  =0x1        # from enum PsUndefinedAreas
	psUnderlineLeft               =0x3        # from enum PsUnderlineType
	psUnderlineOff                =0x1        # from enum PsUnderlineType
	psUnderlineRight              =0x2        # from enum PsUnderlineType
	psCM                          =0x3        # from enum PsUnits
	psInches                      =0x2        # from enum PsUnits
	psMM                          =0x4        # from enum PsUnits
	psPercent                     =0x7        # from enum PsUnits
	psPicas                       =0x6        # from enum PsUnits
	psPixels                      =0x1        # from enum PsUnits
	psPoints                      =0x5        # from enum PsUnits
	psFour                        =0x4        # from enum PsUrgency
	psHigh                        =0x8        # from enum PsUrgency
	psLow                         =0x1        # from enum PsUrgency
	psNone                        =0x0        # from enum PsUrgency
	psNormal                      =0x5        # from enum PsUrgency
	psSeven                       =0x7        # from enum PsUrgency
	psSix                         =0x6        # from enum PsUrgency
	psThree                       =0x3        # from enum PsUrgency
	psTwo                         =0x2        # from enum PsUrgency
	psArc                         =0x2        # from enum PsWarpStyle
	psArcLower                    =0x3        # from enum PsWarpStyle
	psArcUpper                    =0x4        # from enum PsWarpStyle
	psArch                        =0x5        # from enum PsWarpStyle
	psBulge                       =0x6        # from enum PsWarpStyle
	psFish                        =0xb        # from enum PsWarpStyle
	psFishEye                     =0xd        # from enum PsWarpStyle
	psFlag                        =0x9        # from enum PsWarpStyle
	psInflate                     =0xe        # from enum PsWarpStyle
	psNoWarp                      =0x1        # from enum PsWarpStyle
	psRise                        =0xc        # from enum PsWarpStyle
	psShellLower                  =0x7        # from enum PsWarpStyle
	psShellUpper                  =0x8        # from enum PsWarpStyle
	psSqueeze                     =0xf        # from enum PsWarpStyle
	psTwist                       =0x10       # from enum PsWarpStyle
	psWave                        =0xa        # from enum PsWarpStyle
	psSine                        =0x1        # from enum PsWaveType
	psSquare                      =0x3        # from enum PsWaveType
	psTriangular                  =0x2        # from enum PsWaveType
	psAsShot                      =0x0        # from enum PsWhiteBalanceType
	psAuto                        =0x1        # from enum PsWhiteBalanceType
	psCloudy                      =0x3        # from enum PsWhiteBalanceType
	psCustomCameraSettings        =0x8        # from enum PsWhiteBalanceType
	psDaylight                    =0x2        # from enum PsWhiteBalanceType
	psFlash                       =0x7        # from enum PsWhiteBalanceType
	psFluorescent                 =0x6        # from enum PsWhiteBalanceType
	psShade                       =0x4        # from enum PsWhiteBalanceType
	psTungsten                    =0x5        # from enum PsWhiteBalanceType
	psAroundCenter                =0x1        # from enum PsZigZagType
	psOutFromCenter               =0x2        # from enum PsZigZagType
	psPondRipples                 =0x3        # from enum PsZigZagType

from win32com.client import DispatchBaseClass
class ArtLayer(DispatchBaseClass):
	"""any layer that can contain data"""
	CLSID = IID('{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}')
	coclass_clsid = None

	def AdjustBrightnessContrast(self, Brightness=defaultNamedNotOptArg, Contrast=defaultNamedNotOptArg):
		"""adjust brightness and constrast"""
		return self._oleobj_.InvokeTypes(1097084980, LCID, 1, (24, 0), ((3, 1), (3, 1)),Brightness, Contrast)

	def AdjustColorBalance(self, Shadows=defaultNamedOptArg, Midtones=defaultNamedOptArg, Highlights=defaultNamedOptArg, PreserveLuminosity=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1097084981, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17)),Shadows, Midtones, Highlights, PreserveLuminosity)

	def AdjustCurves(self, CurveShape=defaultNamedNotOptArg):
		"""adjust curves of the selected channels"""
		return self._oleobj_.InvokeTypes(1097084979, LCID, 1, (24, 0), ((12, 1),),CurveShape)

	def AdjustLevels(self, InputRangeStart=defaultNamedNotOptArg, InputRangeEnd=defaultNamedNotOptArg, InputRangeGamma=defaultNamedNotOptArg, OutputRangeStart=defaultNamedNotOptArg, OutputRangeEnd=defaultNamedNotOptArg):
		"""adjust levels of the selected channels"""
		return self._oleobj_.InvokeTypes(1097084977, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1), (3, 1), (3, 1)),InputRangeStart, InputRangeEnd, InputRangeGamma, OutputRangeStart, OutputRangeEnd)

	def ApplyAddNoise(self, Amount=defaultNamedNotOptArg, Distribution=defaultNamedNotOptArg, Monochromatic=defaultNamedNotOptArg):
		"""apply the add noise filter"""
		return self._oleobj_.InvokeTypes(1177563448, LCID, 1, (24, 0), ((5, 1), (3, 1), (11, 1)),Amount, Distribution, Monochromatic)

	def ApplyAverage(self):
		"""apply the average filter"""
		return self._oleobj_.InvokeTypes(1177563959, LCID, 1, (24, 0), (),)

	def ApplyBlur(self):
		"""apply the blur filter"""
		return self._oleobj_.InvokeTypes(1177563185, LCID, 1, (24, 0), (),)

	def ApplyBlurMore(self):
		"""apply the blur more filter"""
		return self._oleobj_.InvokeTypes(1177563186, LCID, 1, (24, 0), (),)

	def ApplyClouds(self):
		"""apply the clouds filter"""
		return self._oleobj_.InvokeTypes(1177563953, LCID, 1, (24, 0), (),)

	def ApplyCustomFilter(self, Characteristics=defaultNamedNotOptArg, Scale=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg):
		"""apply the custom filter"""
		return self._oleobj_.InvokeTypes(1177563702, LCID, 1, (24, 0), ((12, 1), (3, 1), (3, 1)),Characteristics, Scale, Offset)

	def ApplyDeInterlace(self, EliminateFields=defaultNamedNotOptArg, CreateFields=defaultNamedNotOptArg):
		"""apply the De-Interlace filter"""
		return self._oleobj_.InvokeTypes(1177563957, LCID, 1, (24, 0), ((3, 1), (3, 1)),EliminateFields, CreateFields)

	def ApplyDespeckle(self):
		"""apply the despeckle filter"""
		return self._oleobj_.InvokeTypes(1177563449, LCID, 1, (24, 0), (),)

	def ApplyDifferenceClouds(self):
		"""apply the difference clouds filter"""
		return self._oleobj_.InvokeTypes(1177563954, LCID, 1, (24, 0), (),)

	def ApplyDiffuseGlow(self, Graininess=defaultNamedNotOptArg, GlowAmount=defaultNamedNotOptArg, ClearAmount=defaultNamedNotOptArg):
		"""apply the diffuse glow filter"""
		return self._oleobj_.InvokeTypes(1177563190, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Graininess, GlowAmount, ClearAmount)

	def ApplyDisplace(self, HorizontalScale=defaultNamedNotOptArg, VerticalScale=defaultNamedNotOptArg, DisplacementType=defaultNamedNotOptArg, UndefinedAreas=defaultNamedNotOptArg, DisplacementMapFile=defaultNamedNotOptArg):
		"""apply the displace filter"""
		return self._oleobj_.InvokeTypes(1177563445, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (8, 1)),HorizontalScale, VerticalScale, DisplacementType, UndefinedAreas, DisplacementMapFile)

	def ApplyDustAndScratches(self, Radius=defaultNamedNotOptArg, Threshold=defaultNamedNotOptArg):
		"""apply the dust and scratches filter"""
		return self._oleobj_.InvokeTypes(1177563696, LCID, 1, (24, 0), ((3, 1), (3, 1)),Radius, Threshold)

	def ApplyGaussianBlur(self, Radius=defaultNamedNotOptArg):
		"""apply the Gaussian blur filter"""
		return self._oleobj_.InvokeTypes(1195535474, LCID, 1, (24, 0), ((5, 1),),Radius)

	def ApplyGlassEffect(self, Distortion=defaultNamedNotOptArg, Smoothness=defaultNamedNotOptArg, Scaling=defaultNamedNotOptArg, Invert=defaultNamedOptArg, Texture=defaultNamedOptArg, TextureFile=defaultNamedOptArg):
		"""apply the glass filter"""
		return self._oleobj_.InvokeTypes(1177563191, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (12, 17), (12, 17), (12, 17)),Distortion, Smoothness, Scaling, Invert, Texture, TextureFile)

	def ApplyHighPass(self, Radius=defaultNamedNotOptArg):
		"""apply the high pass filter"""
		return self._oleobj_.InvokeTypes(1177563952, LCID, 1, (24, 0), ((5, 1),),Radius)

	def ApplyLensBlur(self, Options=defaultNamedOptArg):
		"""apply the Lens blur filter"""
		return self._oleobj_.InvokeTypes(1282294380, LCID, 1, (24, 0), ((12, 17),),Options)

	def ApplyLensFlare(self, Brightness=defaultNamedNotOptArg, FlareCenter=defaultNamedNotOptArg, LensType=defaultNamedNotOptArg):
		"""apply the lens flare filter"""
		return self._oleobj_.InvokeTypes(1177563955, LCID, 1, (24, 0), ((3, 1), (12, 1), (3, 1)),Brightness, FlareCenter, LensType)

	def ApplyMaximum(self, Radius=defaultNamedNotOptArg):
		"""apply the maximum filter"""
		return self._oleobj_.InvokeTypes(1177563703, LCID, 1, (24, 0), ((5, 1),),Radius)

	def ApplyMedianNoise(self, Radius=defaultNamedNotOptArg):
		"""apply the median noise filter"""
		return self._oleobj_.InvokeTypes(1177563697, LCID, 1, (24, 0), ((5, 1),),Radius)

	def ApplyMinimum(self, Radius=defaultNamedNotOptArg):
		"""apply the minimum filter"""
		return self._oleobj_.InvokeTypes(1177563704, LCID, 1, (24, 0), ((5, 1),),Radius)

	def ApplyMotionBlur(self, Angle=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg):
		"""apply the motion blur filter"""
		return self._oleobj_.InvokeTypes(1177563187, LCID, 1, (24, 0), ((3, 1), (5, 1)),Angle, Radius)

	def ApplyNTSC(self):
		"""apply the NTSC colors filter"""
		return self._oleobj_.InvokeTypes(1177563958, LCID, 1, (24, 0), (),)

	def ApplyOceanRipple(self, Size=defaultNamedNotOptArg, Magnitude=defaultNamedNotOptArg):
		"""apply the ocean ripple filter"""
		return self._oleobj_.InvokeTypes(1177563192, LCID, 1, (24, 0), ((3, 1), (3, 1)),Size, Magnitude)

	def ApplyOffset(self, Horizontal=defaultNamedNotOptArg, Vertical=defaultNamedNotOptArg, UndefinedAreas=defaultNamedNotOptArg):
		"""apply the offset filter"""
		return self._oleobj_.InvokeTypes(1177563705, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),Horizontal, Vertical, UndefinedAreas)

	def ApplyPinch(self, Amount=defaultNamedNotOptArg):
		"""apply the pinch filter"""
		return self._oleobj_.InvokeTypes(1177563193, LCID, 1, (24, 0), ((3, 1),),Amount)

	def ApplyPolarCoordinates(self, Conversion=defaultNamedNotOptArg):
		"""apply the polar coordinates filter"""
		return self._oleobj_.InvokeTypes(1177563440, LCID, 1, (24, 0), ((3, 1),),Conversion)

	def ApplyRadialBlur(self, Amount=defaultNamedNotOptArg, BlurMethod=defaultNamedNotOptArg, BlurQuality=defaultNamedNotOptArg):
		"""apply the radial blur filter"""
		return self._oleobj_.InvokeTypes(1177563188, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Amount, BlurMethod, BlurQuality)

	def ApplyRipple(self, Amount=defaultNamedNotOptArg, Size=defaultNamedNotOptArg):
		"""apply the ripple filter"""
		return self._oleobj_.InvokeTypes(1177563441, LCID, 1, (24, 0), ((3, 1), (3, 1)),Amount, Size)

	def ApplySharpen(self):
		"""apply the sharpen filter"""
		return self._oleobj_.InvokeTypes(1177563698, LCID, 1, (24, 0), (),)

	def ApplySharpenEdges(self):
		"""apply the sharpen edges filter"""
		return self._oleobj_.InvokeTypes(1177563699, LCID, 1, (24, 0), (),)

	def ApplySharpenMore(self):
		"""apply the sharpen more filter"""
		return self._oleobj_.InvokeTypes(1177563700, LCID, 1, (24, 0), (),)

	def ApplyShear(self, Curve=defaultNamedNotOptArg, UndefinedAreas=defaultNamedNotOptArg):
		"""apply the shear filter"""
		return self._oleobj_.InvokeTypes(1177563442, LCID, 1, (24, 0), ((12, 1), (3, 1)),Curve, UndefinedAreas)

	def ApplySmartBlur(self, Radius=defaultNamedNotOptArg, Threshold=defaultNamedNotOptArg, BlurQuality=defaultNamedNotOptArg, Mode=defaultNamedNotOptArg):
		"""apply the smart blur filter"""
		return self._oleobj_.InvokeTypes(1177563189, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1), (3, 1)),Radius, Threshold, BlurQuality, Mode)

	def ApplySpherize(self, Amount=defaultNamedNotOptArg, Mode=defaultNamedNotOptArg):
		"""apply the spherize filter"""
		return self._oleobj_.InvokeTypes(1177563443, LCID, 1, (24, 0), ((3, 1), (3, 1)),Amount, Mode)

	def ApplyStyle(self, StyleName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1097878643, LCID, 1, (24, 0), ((8, 1),),StyleName)

	def ApplyTextureFill(self, TextureFile=defaultNamedNotOptArg):
		"""apply the texture fill filter"""
		return self._oleobj_.InvokeTypes(1177563956, LCID, 1, (24, 0), ((8, 1),),TextureFile)

	def ApplyTwirl(self, Angle=defaultNamedNotOptArg):
		"""apply the twirl filter"""
		return self._oleobj_.InvokeTypes(1177563444, LCID, 1, (24, 0), ((3, 1),),Angle)

	def ApplyUnSharpMask(self, Amount=defaultNamedNotOptArg, Radius=defaultNamedNotOptArg, Threshold=defaultNamedNotOptArg):
		"""apply the unsharp mask filter"""
		return self._oleobj_.InvokeTypes(1177563701, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),Amount, Radius, Threshold)

	def ApplyWave(self, GeneratorNumber=defaultNamedNotOptArg, MinimumWavelength=defaultNamedNotOptArg, MaximumWavelength=defaultNamedNotOptArg, MinimumAmplitude=defaultNamedNotOptArg, MaximumAmplitude=defaultNamedNotOptArg, HorizontalScale=defaultNamedNotOptArg, VerticalScale=defaultNamedNotOptArg, WaveType=defaultNamedNotOptArg, UndefinedAreas=defaultNamedNotOptArg, RandomSeed=defaultNamedNotOptArg):
		"""apply the wave filter"""
		return self._oleobj_.InvokeTypes(1177563446, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),GeneratorNumber, MinimumWavelength, MaximumWavelength, MinimumAmplitude, MaximumAmplitude, HorizontalScale, VerticalScale, WaveType, UndefinedAreas, RandomSeed)

	def ApplyZigZag(self, Amount=defaultNamedNotOptArg, Ridges=defaultNamedNotOptArg, Style=defaultNamedNotOptArg):
		"""apply the zigzag filter"""
		return self._oleobj_.InvokeTypes(1177563447, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Amount, Ridges, Style)

	def AutoContrast(self):
		"""adjust contrast of the selected channels automatically"""
		return self._oleobj_.InvokeTypes(1097084978, LCID, 1, (24, 0), (),)

	def AutoLevels(self):
		"""adjust levels of the selected channels using auto levels option"""
		return self._oleobj_.InvokeTypes(1094856753, LCID, 1, (24, 0), (),)

	def Clear(self):
		return self._oleobj_.InvokeTypes(1296117809, LCID, 1, (24, 0), (),)

	def Copy(self, Merge=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), ((12, 17),),Merge)

	def Cut(self):
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		"""delete the object"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Desaturate(self):
		return self._oleobj_.InvokeTypes(1097084982, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		"""create a duplicate of the object"""
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None, UnicodeToString=0)
		return ret

	def Equalize(self):
		"""equalize the levels"""
		return self._oleobj_.InvokeTypes(1097084985, LCID, 1, (24, 0), (),)

	def Invert(self):
		"""inverts the currently selected layer or channels"""
		return self._oleobj_.InvokeTypes(1767272302, LCID, 1, (24, 0), (),)

	def Link(self, With=defaultNamedNotOptArg):
		"""link the layer with another layer"""
		return self._oleobj_.InvokeTypes(1818973295, LCID, 1, (24, 0), ((9, 1),),With)

	# Result is of type ArtLayer
	def Merge(self):
		"""merges the layer down. This will remove the layer from the document. The method returns a reference to the art layer that this layer is merged into"""
		ret = self._oleobj_.InvokeTypes(1298615386, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Merge', '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}', UnicodeToString=0)
		return ret

	def MixChannels(self, OutputChannels=defaultNamedNotOptArg, Monochrome=defaultNamedOptArg):
		"""only valid for RGB or CMYK documents"""
		return self._oleobj_.InvokeTypes(1097084984, LCID, 1, (24, 0), ((12, 1), (12, 17)),OutputChannels, Monochrome)

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		"""move the object"""
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		"""Move the PageItem in behind object"""
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		"""Move the PageItem in front of object"""
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		"""Move the PageItem to beginning of container"""
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		"""Move the PageItem to end of container"""
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container)

	def PhotoFilter(self, FillColor=defaultNamedOptArg, Density=defaultNamedOptArg, PreserveLuminosity=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1097085234, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),FillColor, Density, PreserveLuminosity)

	def Posterize(self, Levels=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1097085232, LCID, 1, (24, 0), ((3, 1),),Levels)

	def Rasterize(self, Target=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1383298162, LCID, 1, (24, 0), ((3, 1),),Target)

	def Resize(self, Horizontal=defaultNamedOptArg, Vertical=defaultNamedOptArg, Anchor=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1399024741, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Horizontal, Vertical, Anchor)

	def Rotate(self, Angle=defaultNamedNotOptArg, Anchor=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1383036001, LCID, 1, (24, 0), ((5, 1), (12, 17)),Angle, Anchor)

	def SelectiveColor(self, SelectionMethod=defaultNamedNotOptArg, Reds=defaultNamedOptArg, Yellows=defaultNamedOptArg, Greens=defaultNamedOptArg, Cyans=defaultNamedOptArg, Blues=defaultNamedOptArg, Magentas=defaultNamedOptArg, Whites=defaultNamedOptArg, Neutrals=defaultNamedOptArg, Blacks=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1097084983, LCID, 1, (24, 0), ((3, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),SelectionMethod, Reds, Yellows, Greens, Cyans, Blues, Magentas, Whites, Neutrals, Blacks)

	def ShadowHighlight(self, ShadowAmount=defaultNamedOptArg, ShadowWidth=defaultNamedOptArg, ShadowRaduis=defaultNamedOptArg, HighlightAmount=defaultNamedOptArg, HighlightWidth=defaultNamedOptArg, HighlightRaduis=defaultNamedOptArg, ColorCorrection=defaultNamedOptArg, MidtoneContrast=defaultNamedOptArg, BlackClip=defaultNamedOptArg, WhiteClip=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1397239857, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ShadowAmount, ShadowWidth, ShadowRaduis, HighlightAmount, HighlightWidth, HighlightRaduis, ColorCorrection, MidtoneContrast, BlackClip, WhiteClip)

	def Threshold(self, Level=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1097085233, LCID, 1, (24, 0), ((3, 1),),Level)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg):
		"""moves the position relative to its current position"""
		return self._oleobj_.InvokeTypes(1299599475, LCID, 1, (24, 0), ((12, 17), (12, 17)),DeltaX, DeltaY)

	def Unlink(self):
		"""unlink the layer"""
		return self._oleobj_.InvokeTypes(1433169515, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AllLocked": (1097616483, 2, (11, 0), (), "AllLocked", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'ArtLayer' returns object of type 'ArtLayer'
		"ArtLayer": (1279358028, 2, (9, 0), (), "ArtLayer", '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}'),
		"BlendMode": (1114393956, 2, (3, 0), (), "BlendMode", None),
		"Bounds": (1114530931, 2, (12, 0), (), "Bounds", None),
		"FillOpacity": (1179611235, 2, (5, 0), (), "FillOpacity", None),
		"Grouped": (1883731792, 2, (11, 0), (), "Grouped", None),
		"IsBackgroundLayer": (1147292786, 2, (11, 0), (), "IsBackgroundLayer", None),
		"Kind": (1265200740, 2, (3, 0), (), "Kind", None),
		"Layer": (1396927603, 2, (9, 0), (), "Layer", None),
		# Method 'LayerSet' returns object of type 'LayerSet'
		"LayerSet": (1279358042, 2, (9, 0), (), "LayerSet", '{C1C35524-2AA4-4630-80B9-011EFE3D5779}'),
		"LayerType": (1954115685, 2, (3, 0), (), "LayerType", None),
		"LinkedLayers": (1282106724, 2, (12, 0), (), "LinkedLayers", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Opacity": (1332765556, 2, (5, 0), (), "Opacity", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PixelsLocked": (1350061155, 2, (11, 0), (), "PixelsLocked", None),
		"PositionLocked": (1349799011, 2, (11, 0), (), "PositionLocked", None),
		# Method 'TextItem' returns object of type 'TextItem'
		"TextItem": (1884058196, 2, (9, 0), (), "TextItem", '{E7A940CD-9AC7-4D76-975D-24D6BA0FDD16}'),
		"TransparentPixelsLocked": (1416645731, 2, (11, 0), (), "TransparentPixelsLocked", None),
		"Visible": (1884705634, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"AllLocked": ((1097616483, LCID, 4, 0),()),
		"BlendMode": ((1114393956, LCID, 4, 0),()),
		"FillOpacity": ((1179611235, LCID, 4, 0),()),
		"Grouped": ((1883731792, LCID, 4, 0),()),
		"IsBackgroundLayer": ((1147292786, LCID, 4, 0),()),
		"Kind": ((1265200740, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Opacity": ((1332765556, LCID, 4, 0),()),
		"PixelsLocked": ((1350061155, LCID, 4, 0),()),
		"PositionLocked": ((1349799011, LCID, 4, 0),()),
		"TransparentPixelsLocked": ((1416645731, LCID, 4, 0),()),
		"Visible": ((1884705634, LCID, 4, 0),()),
	}

class ArtLayers(DispatchBaseClass):
	CLSID = IID('{EC6A366C-F901-488D-A2C3-9E2E78B72DC6}')
	coclass_clsid = None

	# Result is of type ArtLayer
	def Add(self):
		"""create a new object"""
		ret = self._oleobj_.InvokeTypes(1665354858, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type ArtLayer
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}', UnicodeToString=0)
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		"""Delete an element from the collection"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Channel(DispatchBaseClass):
	"""A channel in a document. Can be either a component channel representing a color of the document color model or an alpha channel"""
	CLSID = IID('{4B9E6B85-0613-4873-8AB7-575CD2226768}')
	coclass_clsid = None

	def Delete(self):
		"""delete the object"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	# Result is of type Channel
	def Duplicate(self, TargetDocument=defaultNamedOptArg):
		"""duplicate the channel"""
		ret = self._oleobj_.InvokeTypes(1148207976, LCID, 1, (9, 0), ((12, 17),),TargetDocument)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{4B9E6B85-0613-4873-8AB7-575CD2226768}', UnicodeToString=0)
		return ret

	def Merge(self):
		"""merge a spot channel into the component channels"""
		return self._oleobj_.InvokeTypes(1296849475, LCID, 1, (24, 0), (),)

	def SetColor(self, arg0=defaultUnnamedArg):
		"""color of the channel (not valid for component channels)"""
		return self._oleobj_.InvokeTypes(1883456323, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'Color' returns object of type '_SolidColor'
		"Color": (1883456323, 2, (9, 0), (), "Color", '{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}'),
		"Histogram": (1214870388, 2, (12, 0), (), "Histogram", None),
		"Kind": (1265200740, 2, (3, 0), (), "Kind", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Opacity": (1332765556, 2, (5, 0), (), "Opacity", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Visible": (1884705634, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((1883456323, LCID, 4, 0),()),
		"Kind": ((1265200740, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Opacity": ((1332765556, LCID, 4, 0),()),
		"Visible": ((1884705634, LCID, 4, 0),()),
	}

class Channels(DispatchBaseClass):
	"""Channels of the document"""
	CLSID = IID('{2DC64F97-8C69-4016-A8EB-89A00217291F}')
	coclass_clsid = None

	# Result is of type Channel
	def Add(self):
		"""create a new object"""
		ret = self._oleobj_.InvokeTypes(1665353838, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{4B9E6B85-0613-4873-8AB7-575CD2226768}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type Channel
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4B9E6B85-0613-4873-8AB7-575CD2226768}', UnicodeToString=0)
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		"""Delete an element from the collection"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4B9E6B85-0613-4873-8AB7-575CD2226768}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{4B9E6B85-0613-4873-8AB7-575CD2226768}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Document(DispatchBaseClass):
	"""A document"""
	CLSID = IID('{B1ADEFB6-C536-42D6-8A83-397354A769F8}')
	coclass_clsid = None

	def ChangeMode(self, DestinationMode=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""change the mode of the document"""
		return self._oleobj_.InvokeTypes(1130906483, LCID, 1, (24, 0), ((3, 1), (12, 17)),DestinationMode, Options)

	def Close(self, Saving=defaultNamedOptArg):
		"""close the document"""
		return self._oleobj_.InvokeTypes(1668050803, LCID, 1, (24, 0), ((12, 17),),Saving)

	def ConvertProfile(self, DestinationProfile=defaultNamedNotOptArg, Intent=defaultNamedNotOptArg, BlackPointCompensation=defaultNamedOptArg, Dither=defaultNamedOptArg):
		"""convert the document from using one color profile to using an other"""
		return self._oleobj_.InvokeTypes(1131827314, LCID, 1, (24, 0), ((8, 1), (3, 1), (12, 17), (12, 17)),DestinationProfile, Intent, BlackPointCompensation, Dither)

	def Crop(self, Bounds=defaultNamedNotOptArg, Angle=defaultNamedOptArg, Width=defaultNamedOptArg, Height=defaultNamedOptArg):
		"""crop the document"""
		return self._oleobj_.InvokeTypes(1131573104, LCID, 1, (24, 0), ((12, 1), (12, 17), (12, 17), (12, 17)),Bounds, Angle, Width, Height)

	# Result is of type Document
	def Duplicate(self):
		"""create a duplicate of the object"""
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{B1ADEFB6-C536-42D6-8A83-397354A769F8}', UnicodeToString=0)
		return ret

	def Export(self, ExportIn=defaultNamedNotOptArg, ExportAs=defaultNamedOptArg, Options=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1165521010, LCID, 1, (24, 0), ((8, 1), (12, 17), (12, 17)),ExportIn, ExportAs, Options)

	def Flatten(self):
		"""flatten all layers in the document"""
		return self._oleobj_.InvokeTypes(1181512814, LCID, 1, (24, 0), (),)

	def FlipCanvas(self, Direction=defaultNamedNotOptArg):
		"""flip the canvas horizontally or vertically"""
		return self._oleobj_.InvokeTypes(1181500278, LCID, 1, (24, 0), ((3, 1),),Direction)

	def ImportAnnotations(self, File=defaultNamedNotOptArg):
		"""import annotations into the document"""
		return self._oleobj_.InvokeTypes(1232093550, LCID, 1, (24, 0), ((8, 1),),File)

	def MergeVisibleLayers(self):
		"""flatten all visible layers in the document"""
		return self._oleobj_.InvokeTypes(1299608418, LCID, 1, (24, 0), (),)

	# Result is of type ArtLayer
	def Paste(self, IntoSelection=defaultNamedOptArg):
		"""paste contents of clipboard into the document"""
		ret = self._oleobj_.InvokeTypes(1885434740, LCID, 1, (9, 0), ((12, 17),),IntoSelection)
		if ret is not None:
			ret = Dispatch(ret, 'Paste', '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}', UnicodeToString=0)
		return ret

	def PrintOut(self, PostScriptEncoding=defaultNamedOptArg, SourceSpace=defaultNamedOptArg, PrintSpace=defaultNamedOptArg, Intent=defaultNamedOptArg, BlackPointCompensation=defaultNamedOptArg):
		"""print the document"""
		return self._oleobj_.InvokeTypes(1349731152, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),PostScriptEncoding, SourceSpace, PrintSpace, Intent, BlackPointCompensation)

	def RasterizeAllLayers(self):
		"""rasterize all layers"""
		return self._oleobj_.InvokeTypes(1383743852, LCID, 1, (24, 0), (),)

	def ResizeCanvas(self, Width=defaultNamedOptArg, Height=defaultNamedOptArg, Anchor=defaultNamedOptArg):
		"""change the size of the canvas"""
		return self._oleobj_.InvokeTypes(1383744374, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Width, Height, Anchor)

	def ResizeImage(self, Width=defaultNamedOptArg, Height=defaultNamedOptArg, Resolution=defaultNamedOptArg, ResampleMethod=defaultNamedOptArg):
		"""change the size of the image"""
		return self._oleobj_.InvokeTypes(1383745901, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17)),Width, Height, Resolution, ResampleMethod)

	def RevealAll(self):
		"""expand document to show clipped sections"""
		return self._oleobj_.InvokeTypes(1383481708, LCID, 1, (24, 0), (),)

	def RotateCanvas(self, Angle=defaultNamedNotOptArg):
		"""rotate canvas of document"""
		return self._oleobj_.InvokeTypes(1383351158, LCID, 1, (24, 0), ((5, 1),),Angle)

	def Save(self):
		"""save the document"""
		return self._oleobj_.InvokeTypes(1346589558, LCID, 1, (24, 0), (),)

	def SaveAs(self, SaveIn=defaultNamedNotOptArg, Options=defaultNamedOptArg, AsCopy=defaultNamedOptArg, ExtensionType=defaultNamedOptArg):
		"""save the document with specific save options"""
		return self._oleobj_.InvokeTypes(1400258931, LCID, 1, (24, 0), ((8, 1), (12, 17), (12, 17), (12, 17)),SaveIn, Options, AsCopy, ExtensionType)

	def SplitChannels(self):
		"""split channels of the document"""
		return self._ApplyTypes_(1399866216, 1, (12, 0), (), 'SplitChannels', None,)

	def Trap(self, Width=defaultNamedNotOptArg):
		"""apply trap to a CMYK document"""
		return self._oleobj_.InvokeTypes(1416782192, LCID, 1, (24, 0), ((3, 1),),Width)

	def Trim(self, Type=defaultNamedOptArg, Top=defaultNamedOptArg, Left=defaultNamedOptArg, Bottom=defaultNamedOptArg, Right=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1416784237, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Type, Top, Left, Bottom, Right)

	_prop_map_get_ = {
		"ActiveChannels": (1145269868, 2, (12, 0), (), "ActiveChannels", None),
		# Method 'ActiveHistoryBrushSource' returns object of type 'HistoryState'
		"ActiveHistoryBrushSource": (1145266802, 2, (9, 0), (), "ActiveHistoryBrushSource", '{EDC373C3-FE30-40BA-A31C-0251CA7456F1}'),
		# Method 'ActiveHistoryState' returns object of type 'HistoryState'
		"ActiveHistoryState": (1145268339, 2, (9, 0), (), "ActiveHistoryState", '{EDC373C3-FE30-40BA-A31C-0251CA7456F1}'),
		"ActiveLayer": (1668435058, 2, (9, 0), (), "ActiveLayer", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'ArtLayers' returns object of type 'ArtLayers'
		"ArtLayers": (1665354866, 2, (9, 0), (), "ArtLayers", '{EC6A366C-F901-488D-A2C3-9E2E78B72DC6}'),
		# Method 'BackgroundLayer' returns object of type 'ArtLayer'
		"BackgroundLayer": (1147292786, 2, (9, 0), (), "BackgroundLayer", '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}'),
		"BitsPerChannel": (1145201512, 2, (3, 0), (), "BitsPerChannel", None),
		# Method 'Channels' returns object of type 'Channels'
		"Channels": (1665353838, 2, (9, 0), (), "Channels", '{2DC64F97-8C69-4016-A8EB-89A00217291F}'),
		"ColorProfileName": (1147367502, 2, (8, 0), (), "ColorProfileName", None),
		"ColorProfileType": (1147367508, 2, (3, 0), (), "ColorProfileType", None),
		"ComponentChannels": (1128493171, 2, (12, 0), (), "ComponentChannels", None),
		"FullName": (1148220520, 2, (8, 0), (), "FullName", None),
		"Height": (1214736500, 2, (5, 0), (), "Height", None),
		"Histogram": (1214870388, 2, (12, 0), (), "Histogram", None),
		# Method 'HistoryStates' returns object of type 'HistoryStates'
		"HistoryStates": (1665692532, 2, (9, 0), (), "HistoryStates", '{69172A3F-E06E-42E6-B733-4DC36E2AC948}'),
		# Method 'Info' returns object of type 'DocumentInfo'
		"Info": (1147760230, 2, (9, 0), (), "Info", '{746FEF90-A182-4BD0-A4F6-BB6BBAE87A78}'),
		# Method 'LayerComps' returns object of type 'LayerComps'
		"LayerComps": (1279471665, 2, (9, 0), (), "LayerComps", '{726B458C-74B0-47AE-B390-99753B55DF2E}'),
		# Method 'LayerSets' returns object of type 'LayerSets'
		"LayerSets": (1665948276, 2, (9, 0), (), "LayerSets", '{323DD2BC-0205-4A44-9F8E-0CF2556F00DF}'),
		# Method 'Layers' returns object of type 'Layers'
		"Layers": (1665956210, 2, (9, 0), (), "Layers", '{DDA16C46-15B2-472D-A659-41AA7BFDC4FD}'),
		"Managed": (1682794340, 2, (11, 0), (), "Managed", None),
		"Mode": (1330472037, 2, (3, 0), (), "Mode", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Path": (1146123368, 2, (8, 0), (), "Path", None),
		# Method 'PathItems' returns object of type 'PathItems'
		"PathItems": (1347694643, 2, (9, 0), (), "PathItems", '{91B5F8AE-3CC5-4775-BCD3-FF1E0724BB01}'),
		"PixelAspectRatio": (1147744822, 2, (5, 0), (), "PixelAspectRatio", None),
		"QuickMaskMode": (1364020580, 2, (11, 0), (), "QuickMaskMode", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"Saved": (1146320484, 2, (11, 0), (), "Saved", None),
		# Method 'Selection' returns object of type 'Selection'
		"Selection": (1936026725, 2, (9, 0), (), "Selection", '{09DA6B10-9684-44EE-A575-01F54660BDDC}'),
		"Width": (1466201192, 2, (5, 0), (), "Width", None),
		# Method 'XMPMetadata' returns object of type 'XMPMetadata'
		"XMPMetadata": (1666731364, 2, (9, 0), (), "XMPMetadata", '{DC865034-A587-4CC4-8A5A-453032562BE4}'),
	}
	_prop_map_put_ = {
		"ActiveChannels": ((1145269868, LCID, 4, 0),()),
		"ActiveHistoryBrushSource": ((1145266802, LCID, 4, 0),()),
		"ActiveHistoryState": ((1145268339, LCID, 4, 0),()),
		"ActiveLayer": ((1668435058, LCID, 4, 0),()),
		"BitsPerChannel": ((1145201512, LCID, 4, 0),()),
		"ColorProfileName": ((1147367502, LCID, 4, 0),()),
		"ColorProfileType": ((1147367508, LCID, 4, 0),()),
		"PixelAspectRatio": ((1147744822, LCID, 4, 0),()),
		"QuickMaskMode": ((1364020580, LCID, 4, 0),()),
	}

class DocumentInfo(DispatchBaseClass):
	"""Document information"""
	CLSID = IID('{746FEF90-A182-4BD0-A4F6-BB6BBAE87A78}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Author": (1147744817, 2, (8, 0), (), "Author", None),
		"AuthorPosition": (1147744819, 2, (8, 0), (), "AuthorPosition", None),
		"Caption": (1147744305, 2, (8, 0), (), "Caption", None),
		"CaptionWriter": (1147744306, 2, (8, 0), (), "CaptionWriter", None),
		"Category": (1147744310, 2, (8, 0), (), "Category", None),
		"City": (1147744565, 2, (8, 0), (), "City", None),
		"CopyrightNotice": (1147744816, 2, (8, 0), (), "CopyrightNotice", None),
		"Copyrighted": (1147744569, 2, (3, 0), (), "Copyrighted", None),
		"Country": (1147744567, 2, (8, 0), (), "Country", None),
		"CreationDate": (1147744564, 2, (8, 0), (), "CreationDate", None),
		"Credit": (1147744561, 2, (8, 0), (), "Credit", None),
		"EXIF": (1147744821, 2, (12, 0), (), "EXIF", None),
		"Headline": (1147744307, 2, (8, 0), (), "Headline", None),
		"Instructions": (1147744308, 2, (8, 0), (), "Instructions", None),
		"JobName": (1147744820, 2, (8, 0), (), "JobName", None),
		"Keywords": (1147744309, 2, (12, 0), (), "Keywords", None),
		"OwnerUrl": (1884648044, 2, (8, 0), (), "OwnerUrl", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"ProvinceState": (1147744566, 2, (8, 0), (), "ProvinceState", None),
		"Source": (1147744562, 2, (8, 0), (), "Source", None),
		"SupplementalCategories": (1147744311, 2, (12, 0), (), "SupplementalCategories", None),
		"Title": (1147744818, 2, (8, 0), (), "Title", None),
		"TransmissionReference": (1147744568, 2, (8, 0), (), "TransmissionReference", None),
		"Urgency": (1147744312, 2, (3, 0), (), "Urgency", None),
	}
	_prop_map_put_ = {
		"Author": ((1147744817, LCID, 4, 0),()),
		"AuthorPosition": ((1147744819, LCID, 4, 0),()),
		"Caption": ((1147744305, LCID, 4, 0),()),
		"CaptionWriter": ((1147744306, LCID, 4, 0),()),
		"Category": ((1147744310, LCID, 4, 0),()),
		"City": ((1147744565, LCID, 4, 0),()),
		"CopyrightNotice": ((1147744816, LCID, 4, 0),()),
		"Copyrighted": ((1147744569, LCID, 4, 0),()),
		"Country": ((1147744567, LCID, 4, 0),()),
		"CreationDate": ((1147744564, LCID, 4, 0),()),
		"Credit": ((1147744561, LCID, 4, 0),()),
		"Headline": ((1147744307, LCID, 4, 0),()),
		"Instructions": ((1147744308, LCID, 4, 0),()),
		"JobName": ((1147744820, LCID, 4, 0),()),
		"Keywords": ((1147744309, LCID, 4, 0),()),
		"OwnerUrl": ((1884648044, LCID, 4, 0),()),
		"ProvinceState": ((1147744566, LCID, 4, 0),()),
		"Source": ((1147744562, LCID, 4, 0),()),
		"SupplementalCategories": ((1147744311, LCID, 4, 0),()),
		"Title": ((1147744818, LCID, 4, 0),()),
		"TransmissionReference": ((1147744568, LCID, 4, 0),()),
		"Urgency": ((1147744312, LCID, 4, 0),()),
	}

class Documents(DispatchBaseClass):
	"""A collection of documents"""
	CLSID = IID('{662506C7-6AAE-4422-ACA4-C63627CB1868}')
	coclass_clsid = None

	# Result is of type Document
	def Add(self, Width=defaultNamedOptArg, Height=defaultNamedOptArg, Resolution=defaultNamedOptArg, Name=defaultNamedOptArg, Mode=defaultNamedOptArg, InitialFill=defaultNamedOptArg, PixelAspectRatio=defaultNamedOptArg):
		"""a document"""
		ret = self._oleobj_.InvokeTypes(1685021557, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Width, Height, Resolution, Name, Mode, InitialFill, PixelAspectRatio)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{B1ADEFB6-C536-42D6-8A83-397354A769F8}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type Document
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B1ADEFB6-C536-42D6-8A83-397354A769F8}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B1ADEFB6-C536-42D6-8A83-397354A769F8}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{B1ADEFB6-C536-42D6-8A83-397354A769F8}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class HistoryState(DispatchBaseClass):
	"""A history state for the document"""
	CLSID = IID('{EDC373C3-FE30-40BA-A31C-0251CA7456F1}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Snapshot": (1213425780, 2, (11, 0), (), "Snapshot", None),
	}
	_prop_map_put_ = {
	}

class HistoryStates(DispatchBaseClass):
	"""History states associated with the document"""
	CLSID = IID('{69172A3F-E06E-42E6-B733-4DC36E2AC948}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type HistoryState
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EDC373C3-FE30-40BA-A31C-0251CA7456F1}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EDC373C3-FE30-40BA-A31C-0251CA7456F1}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{EDC373C3-FE30-40BA-A31C-0251CA7456F1}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class LayerComp(DispatchBaseClass):
	"""A layer composition in a document"""
	CLSID = IID('{9A37A0AC-E951-4B16-A548-886B77338DE0}')
	coclass_clsid = None

	def Apply(self):
		"""apply the layer comp to the document"""
		return self._oleobj_.InvokeTypes(1346842673, LCID, 1, (24, 0), (),)

	def Delete(self):
		"""delete the object"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Recapture(self):
		"""recapture the current layer state(s) for this layer comp"""
		return self._oleobj_.InvokeTypes(1346842674, LCID, 1, (24, 0), (),)

	def ResetFromComp(self):
		"""reset the layer comp state to the document state"""
		return self._oleobj_.InvokeTypes(1346844210, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Appearance": (1279471667, 2, (11, 0), (), "Appearance", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Comment": (1279471666, 2, (12, 0), (), "Comment", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Position": (1332897646, 2, (11, 0), (), "Position", None),
		"Selected": (1279471670, 2, (11, 0), (), "Selected", None),
		"Visibility": (1279471669, 2, (11, 0), (), "Visibility", None),
	}
	_prop_map_put_ = {
		"Appearance": ((1279471667, LCID, 4, 0),()),
		"Comment": ((1279471666, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Position": ((1332897646, LCID, 4, 0),()),
		"Visibility": ((1279471669, LCID, 4, 0),()),
	}

class LayerComps(DispatchBaseClass):
	"""Layer compositions associated with the document"""
	CLSID = IID('{726B458C-74B0-47AE-B390-99753B55DF2E}')
	coclass_clsid = None

	# Result is of type LayerComp
	def Add(self, Name=defaultNamedNotOptArg, Comment=defaultNamedOptArg, Appearance=defaultNamedOptArg, Position=defaultNamedOptArg, Visibility=defaultNamedOptArg):
		"""a layer comp"""
		ret = self._oleobj_.InvokeTypes(1279471665, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17), (12, 17), (12, 17)),Name, Comment, Appearance, Position, Visibility)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{9A37A0AC-E951-4B16-A548-886B77338DE0}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type LayerComp
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9A37A0AC-E951-4B16-A548-886B77338DE0}', UnicodeToString=0)
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9A37A0AC-E951-4B16-A548-886B77338DE0}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{9A37A0AC-E951-4B16-A548-886B77338DE0}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class LayerSet(DispatchBaseClass):
	"""Layer set"""
	CLSID = IID('{C1C35524-2AA4-4630-80B9-011EFE3D5779}')
	coclass_clsid = None

	def Delete(self):
		"""delete the object"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		"""create a duplicate of the object"""
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None, UnicodeToString=0)
		return ret

	def Link(self, With=defaultNamedNotOptArg):
		"""link the layer with another layer"""
		return self._oleobj_.InvokeTypes(1818973295, LCID, 1, (24, 0), ((9, 1),),With)

	# Result is of type ArtLayer
	def Merge(self):
		"""merge layerset. Returns a reference to the art layer that is created by this method"""
		ret = self._oleobj_.InvokeTypes(1298615386, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Merge', '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}', UnicodeToString=0)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		"""move the object"""
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		"""Move the PageItem in behind object"""
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		"""Move the PageItem in front of object"""
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		"""Move the PageItem to beginning of container"""
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		"""Move the PageItem to end of container"""
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container)

	def Resize(self, Horizontal=defaultNamedOptArg, Vertical=defaultNamedOptArg, Anchor=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1399024741, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Horizontal, Vertical, Anchor)

	def Rotate(self, Angle=defaultNamedNotOptArg, Anchor=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1383036001, LCID, 1, (24, 0), ((5, 1), (12, 17)),Angle, Anchor)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg):
		"""moves the position relative to its current position"""
		return self._oleobj_.InvokeTypes(1299599475, LCID, 1, (24, 0), ((12, 17), (12, 17)),DeltaX, DeltaY)

	def Unlink(self):
		"""unlink the layer"""
		return self._oleobj_.InvokeTypes(1433169515, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AllLocked": (1097616483, 2, (11, 0), (), "AllLocked", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'ArtLayer' returns object of type 'ArtLayer'
		"ArtLayer": (1279358028, 2, (9, 0), (), "ArtLayer", '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}'),
		# Method 'ArtLayers' returns object of type 'ArtLayers'
		"ArtLayers": (1665354866, 2, (9, 0), (), "ArtLayers", '{EC6A366C-F901-488D-A2C3-9E2E78B72DC6}'),
		"BlendMode": (1114393956, 2, (3, 0), (), "BlendMode", None),
		"Bounds": (1114530931, 2, (12, 0), (), "Bounds", None),
		"EnabledChannels": (1164854120, 2, (12, 0), (), "EnabledChannels", None),
		"Layer": (1396927603, 2, (9, 0), (), "Layer", None),
		# Method 'LayerSet' returns object of type 'LayerSet'
		"LayerSet": (1279358042, 2, (9, 0), (), "LayerSet", '{C1C35524-2AA4-4630-80B9-011EFE3D5779}'),
		# Method 'LayerSets' returns object of type 'LayerSets'
		"LayerSets": (1665948276, 2, (9, 0), (), "LayerSets", '{323DD2BC-0205-4A44-9F8E-0CF2556F00DF}'),
		"LayerType": (1954115685, 2, (3, 0), (), "LayerType", None),
		# Method 'Layers' returns object of type 'Layers'
		"Layers": (1665956210, 2, (9, 0), (), "Layers", '{DDA16C46-15B2-472D-A659-41AA7BFDC4FD}'),
		"LinkedLayers": (1282106724, 2, (12, 0), (), "LinkedLayers", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Opacity": (1332765556, 2, (5, 0), (), "Opacity", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Visible": (1884705634, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"AllLocked": ((1097616483, LCID, 4, 0),()),
		"BlendMode": ((1114393956, LCID, 4, 0),()),
		"EnabledChannels": ((1164854120, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Opacity": ((1332765556, LCID, 4, 0),()),
		"Visible": ((1884705634, LCID, 4, 0),()),
	}

class LayerSets(DispatchBaseClass):
	CLSID = IID('{323DD2BC-0205-4A44-9F8E-0CF2556F00DF}')
	coclass_clsid = None

	# Result is of type LayerSet
	def Add(self):
		"""create a new object"""
		ret = self._oleobj_.InvokeTypes(1665948266, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{C1C35524-2AA4-4630-80B9-011EFE3D5779}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type LayerSet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C1C35524-2AA4-4630-80B9-011EFE3D5779}', UnicodeToString=0)
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		"""Delete an element from the collection"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C1C35524-2AA4-4630-80B9-011EFE3D5779}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{C1C35524-2AA4-4630-80B9-011EFE3D5779}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Layers(DispatchBaseClass):
	CLSID = IID('{DDA16C46-15B2-472D-A659-41AA7BFDC4FD}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None, UnicodeToString=0)
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		"""Delete an element from the collection"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None, UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),None)
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Notifier(DispatchBaseClass):
	"""The parameters of the notifie"""
	CLSID = IID('{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}')
	coclass_clsid = None

	def Delete(self):
		"""delete the object"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Event": (1162752052, 2, (8, 0), (), "Event", None),
		"EventClass": (1162752055, 2, (8, 0), (), "EventClass", None),
		"EventFile": (1162752053, 2, (8, 0), (), "EventFile", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}

class Notifiers(DispatchBaseClass):
	"""A collection of notifiers"""
	CLSID = IID('{861C9290-2A0C-4614-8606-706B31BFD45B}')
	coclass_clsid = None

	# Result is of type Notifier
	def Add(self, Event=defaultNamedNotOptArg, EventFile=defaultNamedNotOptArg, EventClass=defaultNamedOptArg):
		"""a notifier"""
		ret = self._oleobj_.InvokeTypes(1162752050, LCID, 1, (9, 0), ((8, 1), (8, 1), (12, 17)),Event, EventFile, EventClass)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type Notifier
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}', UnicodeToString=0)
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PathItem(DispatchBaseClass):
	"""An artwork path item"""
	CLSID = IID('{8B0CB532-4ACC-4BF3-9E42-0949B679D120}')
	coclass_clsid = None

	def Delete(self):
		"""delete the object"""
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Deselect(self):
		"""unselect this path item, no paths items are selected"""
		return self._oleobj_.InvokeTypes(1148415092, LCID, 1, (24, 0), (),)

	def Duplicate(self, Name=defaultNamedOptArg):
		"""duplicate this path"""
		return self._oleobj_.InvokeTypes(1668050798, LCID, 1, (24, 0), ((12, 17),),Name)

	def FillPath(self, FillColor=defaultNamedOptArg, Mode=defaultNamedOptArg, Opacity=defaultNamedOptArg, PreserveTransparency=defaultNamedOptArg, Feather=defaultNamedOptArg, AntiAlias=defaultNamedOptArg, WholePath=defaultNamedOptArg):
		"""fill the path with the following information"""
		return self._oleobj_.InvokeTypes(1347694900, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),FillColor, Mode, Opacity, PreserveTransparency, Feather, AntiAlias, WholePath)

	def MakeClippingPath(self, Flatness=defaultNamedOptArg):
		"""make this path item the clipping path for this document"""
		return self._oleobj_.InvokeTypes(1347694903, LCID, 1, (24, 0), ((12, 17),),Flatness)

	def MakeSelection(self, Feather=defaultNamedOptArg, AntiAlias=defaultNamedOptArg, Operation=defaultNamedOptArg):
		"""make a selection from this path"""
		return self._oleobj_.InvokeTypes(1347694899, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Feather, AntiAlias, Operation)

	def Select(self):
		"""make this path item the active or selected path item"""
		return self._oleobj_.InvokeTypes(1936483188, LCID, 1, (24, 0), (),)

	def StrokePath(self, Tool=defaultNamedOptArg, SimulatePressure=defaultNamedOptArg):
		"""stroke the path with the following information"""
		return self._oleobj_.InvokeTypes(1347694901, LCID, 1, (24, 0), ((12, 17), (12, 17)),Tool, SimulatePressure)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Kind": (1265200740, 2, (3, 0), (), "Kind", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'SubPathItems' returns object of type 'SubPathItems'
		"SubPathItems": (1347695667, 2, (9, 0), (), "SubPathItems", '{B7283EEC-23B1-49A6-B151-0E97E4AF353C}'),
	}
	_prop_map_put_ = {
		"Kind": ((1265200740, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
	}

class PathItems(DispatchBaseClass):
	"""art paths associated with this document"""
	CLSID = IID('{91B5F8AE-3CC5-4775-BCD3-FF1E0724BB01}')
	coclass_clsid = None

	# Result is of type PathItem
	def Add(self, Name=defaultNamedNotOptArg, EntirePath=defaultNamedNotOptArg):
		"""create a new path item"""
		ret = self._oleobj_.InvokeTypes(1347694643, LCID, 1, (9, 0), ((8, 1), (12, 1)),Name, EntirePath)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{8B0CB532-4ACC-4BF3-9E42-0949B679D120}', UnicodeToString=0)
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type PathItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8B0CB532-4ACC-4BF3-9E42-0949B679D120}', UnicodeToString=0)
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8B0CB532-4ACC-4BF3-9E42-0949B679D120}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{8B0CB532-4ACC-4BF3-9E42-0949B679D120}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PathPoint(DispatchBaseClass):
	"""A point on a path"""
	CLSID = IID('{7D14BA29-1672-482F-8F48-9DA1E94800FD}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Anchor": (1347694904, 2, (12, 0), (), "Anchor", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Kind": (1265200740, 2, (3, 0), (), "Kind", None),
		"LeftDirection": (1347694905, 2, (12, 0), (), "LeftDirection", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"RightDirection": (1347695152, 2, (12, 0), (), "RightDirection", None),
	}
	_prop_map_put_ = {
	}

class PathPoints(DispatchBaseClass):
	"""A collection of path points"""
	CLSID = IID('{8214A53C-0E67-49D4-A65A-D56F07B17D37}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type PathPoint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7D14BA29-1672-482F-8F48-9DA1E94800FD}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7D14BA29-1672-482F-8F48-9DA1E94800FD}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{7D14BA29-1672-482F-8F48-9DA1E94800FD}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Preferences(DispatchBaseClass):
	"""Preferences for Photoshop"""
	CLSID = IID('{288BC58E-AB6A-467C-B244-D225349E3EB3}')
	coclass_clsid = None

	_prop_map_get_ = {
		"AdditionalPluginFolder": (1349661493, 2, (8, 0), (), "AdditionalPluginFolder", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"AskBeforeSavingLayeredTIFF": (1349660980, 2, (11, 0), (), "AskBeforeSavingLayeredTIFF", None),
		"AutoUpdateOpenDocuments": (1349660724, 2, (11, 0), (), "AutoUpdateOpenDocuments", None),
		"BeepWhenDone": (1349660726, 2, (11, 0), (), "BeepWhenDone", None),
		"ColorChannelsInColor": (1349660982, 2, (11, 0), (), "ColorChannelsInColor", None),
		"ColorPicker": (1129343858, 2, (3, 0), (), "ColorPicker", None),
		"ColumnGutter": (1349661240, 2, (5, 0), (), "ColumnGutter", None),
		"ColumnWidth": (1349661239, 2, (5, 0), (), "ColumnWidth", None),
		"CreateFirstSnapshot": (1349661497, 2, (11, 0), (), "CreateFirstSnapshot", None),
		"DynamicColorSliders": (1349660727, 2, (11, 0), (), "DynamicColorSliders", None),
		"EditLogItems": (1349661751, 2, (3, 0), (), "EditLogItems", None),
		"ExportClipboard": (1349660721, 2, (11, 0), (), "ExportClipboard", None),
		"FontPreviewSize": (1179660340, 2, (3, 0), (), "FontPreviewSize", None),
		"GamutWarningOpacity": (1349661236, 2, (5, 0), (), "GamutWarningOpacity", None),
		"GridSize": (1349661233, 2, (3, 0), (), "GridSize", None),
		"GridStyle": (1349661489, 2, (3, 0), (), "GridStyle", None),
		"GridSubDivisions": (1349661491, 2, (3, 0), (), "GridSubDivisions", None),
		"GuideStyle": (1349661488, 2, (3, 0), (), "GuideStyle", None),
		"ImageCacheForHistograms": (1349661496, 2, (11, 0), (), "ImageCacheForHistograms", None),
		"ImageCacheLevels": (1349661495, 2, (3, 0), (), "ImageCacheLevels", None),
		"ImagePreviews": (1349660978, 2, (3, 0), (), "ImagePreviews", None),
		"Interpolation": (1232104545, 2, (3, 0), (), "Interpolation", None),
		"KeyboardZoomResizesWindows": (1349661747, 2, (11, 0), (), "KeyboardZoomResizesWindows", None),
		"MaxRAMuse": (1349661748, 2, (3, 0), (), "MaxRAMuse", None),
		"MaximizeCompatibility": (1884125251, 2, (3, 0), (), "MaximizeCompatibility", None),
		"NonLinearHistory": (1349661744, 2, (11, 0), (), "NonLinearHistory", None),
		"NumberOfHistoryStates": (1349660977, 2, (3, 0), (), "NumberOfHistoryStates", None),
		"OtherCursors": (1349661232, 2, (3, 0), (), "OtherCursors", None),
		"PaintingCursors": (1349660985, 2, (3, 0), (), "PaintingCursors", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PixelDoubling": (1349660984, 2, (11, 0), (), "PixelDoubling", None),
		"PointSize": (1349661241, 2, (3, 0), (), "PointSize", None),
		"RecentFileListLength": (1349660981, 2, (3, 0), (), "RecentFileListLength", None),
		"RulerUnits": (1349661237, 2, (3, 0), (), "RulerUnits", None),
		"SaveLogItems": (1349661750, 2, (3, 0), (), "SaveLogItems", None),
		"SaveLogItemsFile": (1349661752, 2, (8, 0), (), "SaveLogItemsFile", None),
		"SavePaletteLocations": (1349660728, 2, (11, 0), (), "SavePaletteLocations", None),
		"ShowAsianTextOptions": (1349660725, 2, (11, 0), (), "ShowAsianTextOptions", None),
		"ShowEnglishFontNames": (1349660729, 2, (11, 0), (), "ShowEnglishFontNames", None),
		"ShowSliceNumber": (1349661492, 2, (11, 0), (), "ShowSliceNumber", None),
		"ShowToolTips": (1349660723, 2, (11, 0), (), "ShowToolTips", None),
		"SmartQuotes": (1349661745, 2, (11, 0), (), "SmartQuotes", None),
		"TypeUnits": (1349661238, 2, (3, 0), (), "TypeUnits", None),
		"UseAdditionalPluginFolder": (1349661746, 2, (11, 0), (), "UseAdditionalPluginFolder", None),
		"UseDiffusionDither": (1349660983, 2, (11, 0), (), "UseDiffusionDither", None),
		"UseHistoryLog": (1349661749, 2, (11, 0), (), "UseHistoryLog", None),
		"UseLowerCaseExtension": (1884507235, 2, (11, 0), (), "UseLowerCaseExtension", None),
		"UseShiftKeyForToolSwitch": (1349660976, 2, (11, 0), (), "UseShiftKeyForToolSwitch", None),
		"UseVideoAlpha": (1349661235, 2, (11, 0), (), "UseVideoAlpha", None),
	}
	_prop_map_put_ = {
		"AdditionalPluginFolder": ((1349661493, LCID, 4, 0),()),
		"AskBeforeSavingLayeredTIFF": ((1349660980, LCID, 4, 0),()),
		"AutoUpdateOpenDocuments": ((1349660724, LCID, 4, 0),()),
		"BeepWhenDone": ((1349660726, LCID, 4, 0),()),
		"ColorChannelsInColor": ((1349660982, LCID, 4, 0),()),
		"ColorPicker": ((1129343858, LCID, 4, 0),()),
		"ColumnGutter": ((1349661240, LCID, 4, 0),()),
		"ColumnWidth": ((1349661239, LCID, 4, 0),()),
		"CreateFirstSnapshot": ((1349661497, LCID, 4, 0),()),
		"DynamicColorSliders": ((1349660727, LCID, 4, 0),()),
		"EditLogItems": ((1349661751, LCID, 4, 0),()),
		"ExportClipboard": ((1349660721, LCID, 4, 0),()),
		"FontPreviewSize": ((1179660340, LCID, 4, 0),()),
		"GamutWarningOpacity": ((1349661236, LCID, 4, 0),()),
		"GridSize": ((1349661233, LCID, 4, 0),()),
		"GridStyle": ((1349661489, LCID, 4, 0),()),
		"GridSubDivisions": ((1349661491, LCID, 4, 0),()),
		"GuideStyle": ((1349661488, LCID, 4, 0),()),
		"ImageCacheForHistograms": ((1349661496, LCID, 4, 0),()),
		"ImageCacheLevels": ((1349661495, LCID, 4, 0),()),
		"ImagePreviews": ((1349660978, LCID, 4, 0),()),
		"Interpolation": ((1232104545, LCID, 4, 0),()),
		"KeyboardZoomResizesWindows": ((1349661747, LCID, 4, 0),()),
		"MaxRAMuse": ((1349661748, LCID, 4, 0),()),
		"MaximizeCompatibility": ((1884125251, LCID, 4, 0),()),
		"NonLinearHistory": ((1349661744, LCID, 4, 0),()),
		"NumberOfHistoryStates": ((1349660977, LCID, 4, 0),()),
		"OtherCursors": ((1349661232, LCID, 4, 0),()),
		"PaintingCursors": ((1349660985, LCID, 4, 0),()),
		"PixelDoubling": ((1349660984, LCID, 4, 0),()),
		"PointSize": ((1349661241, LCID, 4, 0),()),
		"RecentFileListLength": ((1349660981, LCID, 4, 0),()),
		"RulerUnits": ((1349661237, LCID, 4, 0),()),
		"SaveLogItems": ((1349661750, LCID, 4, 0),()),
		"SaveLogItemsFile": ((1349661752, LCID, 4, 0),()),
		"SavePaletteLocations": ((1349660728, LCID, 4, 0),()),
		"ShowAsianTextOptions": ((1349660725, LCID, 4, 0),()),
		"ShowEnglishFontNames": ((1349660729, LCID, 4, 0),()),
		"ShowSliceNumber": ((1349661492, LCID, 4, 0),()),
		"ShowToolTips": ((1349660723, LCID, 4, 0),()),
		"SmartQuotes": ((1349661745, LCID, 4, 0),()),
		"TypeUnits": ((1349661238, LCID, 4, 0),()),
		"UseAdditionalPluginFolder": ((1349661746, LCID, 4, 0),()),
		"UseDiffusionDither": ((1349660983, LCID, 4, 0),()),
		"UseHistoryLog": ((1349661749, LCID, 4, 0),()),
		"UseLowerCaseExtension": ((1884507235, LCID, 4, 0),()),
		"UseShiftKeyForToolSwitch": ((1349660976, LCID, 4, 0),()),
		"UseVideoAlpha": ((1349661235, LCID, 4, 0),()),
	}

class Selection(DispatchBaseClass):
	"""The selection of the document"""
	CLSID = IID('{09DA6B10-9684-44EE-A575-01F54660BDDC}')
	coclass_clsid = None

	def Clear(self):
		"""clear selection"""
		return self._oleobj_.InvokeTypes(1296117809, LCID, 1, (24, 0), (),)

	def Contract(self, By=defaultNamedNotOptArg):
		"""contracts the selection"""
		return self._oleobj_.InvokeTypes(1396929650, LCID, 1, (24, 0), ((5, 1),),By)

	def Copy(self, Merge=defaultNamedOptArg):
		"""copy selection to the clipboard"""
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), ((12, 17),),Merge)

	def Cut(self):
		"""cut current selection to the clipboard"""
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Deselect(self):
		return self._oleobj_.InvokeTypes(1148415092, LCID, 1, (24, 0), (),)

	def Expand(self, By=defaultNamedNotOptArg):
		"""expand selection"""
		return self._oleobj_.InvokeTypes(1483763300, LCID, 1, (24, 0), ((5, 1),),By)

	def Feather(self, By=defaultNamedNotOptArg):
		"""feather edges of selection"""
		return self._oleobj_.InvokeTypes(1182034034, LCID, 1, (24, 0), ((5, 1),),By)

	def Fill(self, FillType=defaultNamedNotOptArg, Mode=defaultNamedOptArg, Opacity=defaultNamedOptArg, PreserveTransparency=defaultNamedOptArg):
		"""fills the selection"""
		return self._oleobj_.InvokeTypes(1181314156, LCID, 1, (24, 0), ((12, 1), (12, 17), (12, 17), (12, 17)),FillType, Mode, Opacity, PreserveTransparency)

	def Grow(self, Tolerance=defaultNamedNotOptArg, AntiAlias=defaultNamedNotOptArg):
		"""grow selection to include all adjacent pixels falling within the specified tolerance range"""
		return self._oleobj_.InvokeTypes(1198681975, LCID, 1, (24, 0), ((3, 1), (11, 1)),Tolerance, AntiAlias)

	def Invert(self):
		"""invert the selection"""
		return self._oleobj_.InvokeTypes(1232491372, LCID, 1, (24, 0), (),)

	def Load(self, From=defaultNamedNotOptArg, Combination=defaultNamedOptArg, Inverting=defaultNamedOptArg):
		"""load the selection from a channel"""
		return self._oleobj_.InvokeTypes(1281643372, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17)),From, Combination, Inverting)

	def MakeWorkPath(self, Tolerance=defaultNamedOptArg):
		"""make this selection item the work path for this document"""
		return self._oleobj_.InvokeTypes(1347694902, LCID, 1, (24, 0), ((12, 17),),Tolerance)

	def Resize(self, Horizontal=defaultNamedOptArg, Vertical=defaultNamedOptArg, Anchor=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1399024741, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Horizontal, Vertical, Anchor)

	def ResizeBoundary(self, Horizontal=defaultNamedOptArg, Vertical=defaultNamedOptArg, Anchor=defaultNamedOptArg):
		"""scale the boundary of selection"""
		return self._oleobj_.InvokeTypes(1399013988, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),Horizontal, Vertical, Anchor)

	def Rotate(self, Angle=defaultNamedNotOptArg, Anchor=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1383036001, LCID, 1, (24, 0), ((5, 1), (12, 17)),Angle, Anchor)

	def RotateBoundary(self, Angle=defaultNamedNotOptArg, Anchor=defaultNamedOptArg):
		"""rotates the boundary of selection"""
		return self._oleobj_.InvokeTypes(1383035970, LCID, 1, (24, 0), ((5, 1), (12, 17)),Angle, Anchor)

	def Select(self, Region=defaultNamedNotOptArg, Type=defaultNamedOptArg, Feather=defaultNamedOptArg, AntiAlias=defaultNamedOptArg):
		return self._oleobj_.InvokeTypes(1936483188, LCID, 1, (24, 0), ((12, 1), (12, 17), (12, 17), (12, 17)),Region, Type, Feather, AntiAlias)

	def SelectAll(self):
		return self._oleobj_.InvokeTypes(1399013740, LCID, 1, (24, 0), (),)

	def SelectBorder(self, Width=defaultNamedNotOptArg):
		"""select the border of the selection"""
		return self._oleobj_.InvokeTypes(1114793074, LCID, 1, (24, 0), ((5, 1),),Width)

	def Similar(self, Tolerance=defaultNamedNotOptArg, AntiAlias=defaultNamedNotOptArg):
		"""grow selection to include pixels throughout the image falling within the tolerance range"""
		return self._oleobj_.InvokeTypes(1399680114, LCID, 1, (24, 0), ((3, 1), (11, 1)),Tolerance, AntiAlias)

	def Smooth(self, Radius=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1347646568, LCID, 1, (24, 0), ((3, 1),),Radius)

	def Store(self, Into=defaultNamedNotOptArg, Combination=defaultNamedOptArg):
		"""save the selection as a channel"""
		return self._oleobj_.InvokeTypes(1400263532, LCID, 1, (24, 0), ((9, 1), (12, 17)),Into, Combination)

	def Stroke(self, StrokeColor=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Location=defaultNamedOptArg, Mode=defaultNamedOptArg, Opacity=defaultNamedOptArg, PreserveTransparency=defaultNamedOptArg):
		"""strokes the selection"""
		return self._oleobj_.InvokeTypes(1400138597, LCID, 1, (24, 0), ((12, 1), (3, 1), (12, 17), (12, 17), (12, 17), (12, 17)),StrokeColor, Width, Location, Mode, Opacity, PreserveTransparency)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg):
		"""moves the position relative to its current position"""
		return self._oleobj_.InvokeTypes(1299599475, LCID, 1, (24, 0), ((12, 17), (12, 17)),DeltaX, DeltaY)

	def TranslateBoundary(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg):
		"""moves the boundary of selection relative to its current position"""
		return self._oleobj_.InvokeTypes(1299595876, LCID, 1, (24, 0), ((12, 17), (12, 17)),DeltaX, DeltaY)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Bounds": (1114530931, 2, (12, 0), (), "Bounds", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}

class SubPathItem(DispatchBaseClass):
	"""An artwork sub path item"""
	CLSID = IID('{B6D22EB9-EC6D-46DB-B52A-5561433A1217}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Closed": (1347695920, 2, (11, 0), (), "Closed", None),
		"Operation": (1347694647, 2, (3, 0), (), "Operation", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathPoints' returns object of type 'PathPoints'
		"PathPoints": (1347694644, 2, (9, 0), (), "PathPoints", '{8214A53C-0E67-49D4-A65A-D56F07B17D37}'),
	}
	_prop_map_put_ = {
	}

class SubPathItems(DispatchBaseClass):
	"""art sub paths associated with the path item"""
	CLSID = IID('{B7283EEC-23B1-49A6-B151-0E97E4AF353C}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type SubPathItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B6D22EB9-EC6D-46DB-B52A-5561433A1217}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B6D22EB9-EC6D-46DB-B52A-5561433A1217}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{B6D22EB9-EC6D-46DB-B52A-5561433A1217}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class TextFont(DispatchBaseClass):
	"""An installed font"""
	CLSID = IID('{C88838E3-5A82-4EE7-A66C-E0360C9B0356}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Family": (1883653710, 2, (8, 0), (), "Family", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PostScriptName": (1884312398, 2, (8, 0), (), "PostScriptName", None),
		"Style": (1400142188, 2, (8, 0), (), "Style", None),
	}
	_prop_map_put_ = {
	}

class TextFonts(DispatchBaseClass):
	"""A collection of fonts"""
	CLSID = IID('{BBCE52D6-5D4B-4691-99E3-62C174BD2855}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr)

	# Result is of type TextFont
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C88838E3-5A82-4EE7-A66C-E0360C9B0356}', UnicodeToString=0)
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		"""get an element from the collection"""
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C88838E3-5A82-4EE7-A66C-E0360C9B0356}', UnicodeToString=0)
		return ret

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		return win32com.client.util.Iterator(ob)
	def _NewEnum(self):
		"Create an enumerator from this object"
		return win32com.client.util.WrapEnum(self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),()),'{C88838E3-5A82-4EE7-A66C-E0360C9B0356}')
	def __getitem__(self, index):
		"Allow this class to be accessed as a collection"
		if not self.__dict__.has_key('_enum_'):
			self.__dict__['_enum_'] = self._NewEnum()
		return self._enum_.__getitem__(index)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class TextItem(DispatchBaseClass):
	"""Text item contained in an art layer"""
	CLSID = IID('{E7A940CD-9AC7-4D76-975D-24D6BA0FDD16}')
	coclass_clsid = None

	def ConvertToShape(self):
		"""converts the text item and its containing layer to a fill layer with the text changed to a clipping path"""
		return self._oleobj_.InvokeTypes(1131819635, LCID, 1, (24, 0), (),)

	def CreatePath(self):
		"""creates a work path based on the text object"""
		return self._oleobj_.InvokeTypes(1129803892, LCID, 1, (24, 0), (),)

	def SetColor(self, arg0=defaultUnnamedArg):
		"""color of text"""
		return self._oleobj_.InvokeTypes(1413704771, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlternateLigatures": (1095529587, 2, (11, 0), (), "AlternateLigatures", None),
		"AntiAliasMethod": (1094808688, 2, (3, 0), (), "AntiAliasMethod", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"AutoKerning": (1097560686, 2, (3, 0), (), "AutoKerning", None),
		"AutoLeadingAmount": (1097621837, 2, (5, 0), (), "AutoLeadingAmount", None),
		"BaselineShift": (1114403688, 2, (5, 0), (), "BaselineShift", None),
		"Capitalization": (1130459251, 2, (3, 0), (), "Capitalization", None),
		# Method 'Color' returns object of type '_SolidColor'
		"Color": (1413704771, 2, (9, 0), (), "Color", '{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}'),
		"Contents": (1885564532, 2, (8, 0), (), "Contents", None),
		"DesiredGlyphScaling": (1148405619, 2, (5, 0), (), "DesiredGlyphScaling", None),
		"DesiredLetterScaling": (1148406899, 2, (5, 0), (), "DesiredLetterScaling", None),
		"DesiredWordScaling": (1148409715, 2, (5, 0), (), "DesiredWordScaling", None),
		"Direction": (1413769586, 2, (3, 0), (), "Direction", None),
		"FauxBold": (1182286444, 2, (11, 0), (), "FauxBold", None),
		"FauxItalic": (1182288244, 2, (11, 0), (), "FauxItalic", None),
		"FirstLineIndent": (1413900644, 2, (5, 0), (), "FirstLineIndent", None),
		"Font": (1665560180, 2, (8, 0), (), "Font", None),
		"HangingPuntuation": (1213227892, 2, (11, 0), (), "HangingPuntuation", None),
		"Height": (1214736500, 2, (5, 0), (), "Height", None),
		"HorizontalScale": (1215452003, 2, (3, 0), (), "HorizontalScale", None),
		"HyphenLimit": (1212968308, 2, (3, 0), (), "HyphenLimit", None),
		"HyphenateAfterFirst": (1212245620, 2, (3, 0), (), "HyphenateAfterFirst", None),
		"HyphenateBeforeLast": (1212311154, 2, (3, 0), (), "HyphenateBeforeLast", None),
		"HyphenateCapitalWords": (1212379251, 2, (11, 0), (), "HyphenateCapitalWords", None),
		"HyphenateWordsLongerThan": (1212970094, 2, (3, 0), (), "HyphenateWordsLongerThan", None),
		"Hyphenation": (1430810728, 2, (11, 0), (), "Hyphenation", None),
		"HyphenationZone": (1213886053, 2, (5, 0), (), "HyphenationZone", None),
		"Justification": (1886024564, 2, (3, 0), (), "Justification", None),
		"Kind": (1265200740, 2, (3, 0), (), "Kind", None),
		"Language": (1281453671, 2, (3, 0), (), "Language", None),
		"Leading": (1414292583, 2, (5, 0), (), "Leading", None),
		"LeftIndent": (1414293860, 2, (5, 0), (), "LeftIndent", None),
		"Ligatures": (1282699891, 2, (11, 0), (), "Ligatures", None),
		"MaximumGlyphScaling": (1299400563, 2, (5, 0), (), "MaximumGlyphScaling", None),
		"MaximumLetterScaling": (1298222195, 2, (5, 0), (), "MaximumLetterScaling", None),
		"MaximumWordScaling": (1298225011, 2, (5, 0), (), "MaximumWordScaling", None),
		"MinimumGlyphScaling": (1298745203, 2, (5, 0), (), "MinimumGlyphScaling", None),
		"MinimumLetterScaling": (1298746483, 2, (5, 0), (), "MinimumLetterScaling", None),
		"MinimumWordScaling": (1298749299, 2, (5, 0), (), "MinimumWordScaling", None),
		"NoBreak": (1315922539, 2, (11, 0), (), "NoBreak", None),
		"OldStyle": (1331975028, 2, (11, 0), (), "OldStyle", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Position": (1332897646, 2, (12, 0), (), "Position", None),
		"RightIndent": (1414687076, 2, (5, 0), (), "RightIndent", None),
		"Size": (1886679930, 2, (5, 0), (), "Size", None),
		"SpaceAfter": (1414750566, 2, (5, 0), (), "SpaceAfter", None),
		"SpaceBefore": (1414742630, 2, (5, 0), (), "SpaceBefore", None),
		"StrikeThru": (1347711605, 2, (3, 0), (), "StrikeThru", None),
		"TextComposer": (1413705843, 2, (3, 0), (), "TextComposer", None),
		"Tracking": (1416784750, 2, (5, 0), (), "Tracking", None),
		"Underline": (1433168238, 2, (3, 0), (), "Underline", None),
		"UseAutoLeading": (1097622631, 2, (11, 0), (), "UseAutoLeading", None),
		"VerticalScale": (1450464099, 2, (3, 0), (), "VerticalScale", None),
		"WarpBend": (1463971428, 2, (5, 0), (), "WarpBend", None),
		"WarpDirection": (1464101234, 2, (3, 0), (), "WarpDirection", None),
		"WarpHorizontalDistortion": (1464353907, 2, (5, 0), (), "WarpHorizontalDistortion", None),
		"WarpStyle": (1465087084, 2, (3, 0), (), "WarpStyle", None),
		"WarpVerticalDistortion": (1465271411, 2, (5, 0), (), "WarpVerticalDistortion", None),
		"Width": (1466201192, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"AlternateLigatures": ((1095529587, LCID, 4, 0),()),
		"AntiAliasMethod": ((1094808688, LCID, 4, 0),()),
		"AutoKerning": ((1097560686, LCID, 4, 0),()),
		"AutoLeadingAmount": ((1097621837, LCID, 4, 0),()),
		"BaselineShift": ((1114403688, LCID, 4, 0),()),
		"Capitalization": ((1130459251, LCID, 4, 0),()),
		"Color": ((1413704771, LCID, 4, 0),()),
		"Contents": ((1885564532, LCID, 4, 0),()),
		"DesiredGlyphScaling": ((1148405619, LCID, 4, 0),()),
		"DesiredLetterScaling": ((1148406899, LCID, 4, 0),()),
		"DesiredWordScaling": ((1148409715, LCID, 4, 0),()),
		"Direction": ((1413769586, LCID, 4, 0),()),
		"FauxBold": ((1182286444, LCID, 4, 0),()),
		"FauxItalic": ((1182288244, LCID, 4, 0),()),
		"FirstLineIndent": ((1413900644, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"HangingPuntuation": ((1213227892, LCID, 4, 0),()),
		"Height": ((1214736500, LCID, 4, 0),()),
		"HorizontalScale": ((1215452003, LCID, 4, 0),()),
		"HyphenLimit": ((1212968308, LCID, 4, 0),()),
		"HyphenateAfterFirst": ((1212245620, LCID, 4, 0),()),
		"HyphenateBeforeLast": ((1212311154, LCID, 4, 0),()),
		"HyphenateCapitalWords": ((1212379251, LCID, 4, 0),()),
		"HyphenateWordsLongerThan": ((1212970094, LCID, 4, 0),()),
		"Hyphenation": ((1430810728, LCID, 4, 0),()),
		"HyphenationZone": ((1213886053, LCID, 4, 0),()),
		"Justification": ((1886024564, LCID, 4, 0),()),
		"Kind": ((1265200740, LCID, 4, 0),()),
		"Language": ((1281453671, LCID, 4, 0),()),
		"Leading": ((1414292583, LCID, 4, 0),()),
		"LeftIndent": ((1414293860, LCID, 4, 0),()),
		"Ligatures": ((1282699891, LCID, 4, 0),()),
		"MaximumGlyphScaling": ((1299400563, LCID, 4, 0),()),
		"MaximumLetterScaling": ((1298222195, LCID, 4, 0),()),
		"MaximumWordScaling": ((1298225011, LCID, 4, 0),()),
		"MinimumGlyphScaling": ((1298745203, LCID, 4, 0),()),
		"MinimumLetterScaling": ((1298746483, LCID, 4, 0),()),
		"MinimumWordScaling": ((1298749299, LCID, 4, 0),()),
		"NoBreak": ((1315922539, LCID, 4, 0),()),
		"OldStyle": ((1331975028, LCID, 4, 0),()),
		"Position": ((1332897646, LCID, 4, 0),()),
		"RightIndent": ((1414687076, LCID, 4, 0),()),
		"Size": ((1886679930, LCID, 4, 0),()),
		"SpaceAfter": ((1414750566, LCID, 4, 0),()),
		"SpaceBefore": ((1414742630, LCID, 4, 0),()),
		"StrikeThru": ((1347711605, LCID, 4, 0),()),
		"TextComposer": ((1413705843, LCID, 4, 0),()),
		"Tracking": ((1416784750, LCID, 4, 0),()),
		"Underline": ((1433168238, LCID, 4, 0),()),
		"UseAutoLeading": ((1097622631, LCID, 4, 0),()),
		"VerticalScale": ((1450464099, LCID, 4, 0),()),
		"WarpBend": ((1463971428, LCID, 4, 0),()),
		"WarpDirection": ((1464101234, LCID, 4, 0),()),
		"WarpHorizontalDistortion": ((1464353907, LCID, 4, 0),()),
		"WarpStyle": ((1465087084, LCID, 4, 0),()),
		"WarpVerticalDistortion": ((1465271411, LCID, 4, 0),()),
		"Width": ((1466201192, LCID, 4, 0),()),
	}

class XMPMetadata(DispatchBaseClass):
	CLSID = IID('{DC865034-A587-4CC4-8A5A-453032562BE4}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"RawData": (1884441956, 2, (8, 0), (), "RawData", None),
	}
	_prop_map_put_ = {
		"RawData": ((1884441956, LCID, 4, 0),()),
	}

class _ActionDescriptor(DispatchBaseClass):
	CLSID = IID('{70A60330-E866-46AA-A715-ABF418C41453}')
	coclass_clsid = IID('{817C4CED-C2E7-4CE6-839B-812940E412B4}')

	def Clear(self):
		"""Clear the descriptor"""
		return self._oleobj_.InvokeTypes(1296117809, LCID, 1, (24, 0), (),)

	def Erase(self, Key=defaultNamedNotOptArg):
		"""Erase a key from the descriptor"""
		return self._oleobj_.InvokeTypes(1296117810, LCID, 1, (24, 0), ((3, 1),),Key)

	def GetBoolean(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type boolean"""
		return self._oleobj_.InvokeTypes(1296117811, LCID, 1, (11, 0), ((3, 1),),Key)

	def GetClass(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type class"""
		return self._oleobj_.InvokeTypes(1296117812, LCID, 1, (3, 0), ((3, 1),),Key)

	def GetDouble(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type double"""
		return self._oleobj_.InvokeTypes(1296117814, LCID, 1, (5, 0), ((3, 1),),Key)

	def GetEnumerationType(self, Key=defaultNamedNotOptArg):
		"""Get the enumeration type of a key"""
		return self._oleobj_.InvokeTypes(1296117815, LCID, 1, (3, 0), ((3, 1),),Key)

	def GetEnumerationValue(self, Key=defaultNamedNotOptArg):
		"""Get the enumeration value of a key"""
		return self._oleobj_.InvokeTypes(1296117816, LCID, 1, (3, 0), ((3, 1),),Key)

	def GetInteger(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type integer"""
		return self._oleobj_.InvokeTypes(1296117817, LCID, 1, (3, 0), ((3, 1),),Key)

	def GetKey(self, Index=defaultNamedNotOptArg):
		"""Get ID of the Nth key"""
		return self._oleobj_.InvokeTypes(1296118064, LCID, 1, (3, 0), ((3, 1),),Index)

	# Result is of type _ActionList
	def GetList(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type list"""
		ret = self._oleobj_.InvokeTypes(1296118065, LCID, 1, (9, 0), ((3, 1),),Key)
		if ret is not None:
			ret = Dispatch(ret, 'GetList', '{55031766-E456-4E54-A0D0-8E545601A2D8}', UnicodeToString=0)
		return ret

	def GetObjectType(self, Key=defaultNamedNotOptArg):
		"""Get the class ID of an object in a key of type object"""
		return self._oleobj_.InvokeTypes(1296118066, LCID, 1, (3, 0), ((3, 1),),Key)

	# Result is of type _ActionDescriptor
	def GetObjectValue(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type object"""
		ret = self._oleobj_.InvokeTypes(1296118067, LCID, 1, (9, 0), ((3, 1),),Key)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectValue', '{70A60330-E866-46AA-A715-ABF418C41453}', UnicodeToString=0)
		return ret

	def GetPath(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type Alias"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1296118068, LCID, 1, (8, 0), ((3, 1),),Key)

	# Result is of type _ActionReference
	def GetReference(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type ActionReference"""
		ret = self._oleobj_.InvokeTypes(1296118069, LCID, 1, (9, 0), ((3, 1),),Key)
		if ret is not None:
			ret = Dispatch(ret, 'GetReference', '{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}', UnicodeToString=0)
		return ret

	def GetString(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type string"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1296118070, LCID, 1, (8, 0), ((3, 1),),Key)

	def GetType(self, Key=defaultNamedNotOptArg):
		"""Get the type of a key"""
		return self._oleobj_.InvokeTypes(1296118071, LCID, 1, (3, 0), ((3, 1),),Key)

	def GetUnitDoubleType(self, Key=defaultNamedNotOptArg):
		"""Get the unit type of a key of type UnitDouble"""
		return self._oleobj_.InvokeTypes(1296118072, LCID, 1, (3, 0), ((3, 1),),Key)

	def GetUnitDoubleValue(self, Key=defaultNamedNotOptArg):
		"""Get the value of a key of type UnitDouble"""
		return self._oleobj_.InvokeTypes(1296118073, LCID, 1, (5, 0), ((3, 1),),Key)

	def HasKey(self, Key=defaultNamedNotOptArg):
		"""does the descriptor contain the provided key?"""
		return self._oleobj_.InvokeTypes(1296118320, LCID, 1, (11, 0), ((3, 1),),Key)

	def IsEqual(self, OtherDesc=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118321, LCID, 1, (11, 0), ((9, 1),),OtherDesc)

	def PutBoolean(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118322, LCID, 1, (24, 0), ((3, 1), (11, 1)),Key, Value)

	def PutClass(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118323, LCID, 1, (24, 0), ((3, 1), (3, 1)),Key, Value)

	def PutDouble(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118324, LCID, 1, (24, 0), ((3, 1), (5, 1)),Key, Value)

	def PutEnumerated(self, Key=defaultNamedNotOptArg, EnumType=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118325, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),Key, EnumType, Value)

	def PutInteger(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118326, LCID, 1, (24, 0), ((3, 1), (3, 1)),Key, Value)

	def PutList(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118327, LCID, 1, (24, 0), ((3, 1), (9, 1)),Key, Value)

	def PutObject(self, Key=defaultNamedNotOptArg, ClassID=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118328, LCID, 1, (24, 0), ((3, 1), (3, 1), (9, 1)),Key, ClassID, Value)

	def PutPath(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118329, LCID, 1, (24, 0), ((3, 1), (8, 1)),Key, Value)

	def PutReference(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118576, LCID, 1, (24, 0), ((3, 1), (9, 1)),Key, Value)

	def PutString(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118577, LCID, 1, (24, 0), ((3, 1), (8, 1)),Key, Value)

	def PutUnitDouble(self, Key=defaultNamedNotOptArg, UnitID=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118578, LCID, 1, (24, 0), ((3, 1), (3, 1), (5, 1)),Key, UnitID, Value)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1346462580, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1346462580, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _ActionList(DispatchBaseClass):
	CLSID = IID('{55031766-E456-4E54-A0D0-8E545601A2D8}')
	coclass_clsid = IID('{E56C890E-2974-463F-8D39-CEDEA8BED418}')

	def Clear(self):
		"""Clear the list"""
		return self._oleobj_.InvokeTypes(1296117809, LCID, 1, (24, 0), (),)

	def GetBoolean(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type boolean"""
		return self._oleobj_.InvokeTypes(1296117811, LCID, 1, (11, 0), ((3, 1),),Index)

	def GetClass(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type class"""
		return self._oleobj_.InvokeTypes(1296117812, LCID, 1, (3, 0), ((3, 1),),Index)

	def GetDouble(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type double"""
		return self._oleobj_.InvokeTypes(1296117814, LCID, 1, (5, 0), ((3, 1),),Index)

	def GetEnumerationType(self, Index=defaultNamedNotOptArg):
		"""Get the enumeration type of an item"""
		return self._oleobj_.InvokeTypes(1296117815, LCID, 1, (3, 0), ((3, 1),),Index)

	def GetEnumerationValue(self, Index=defaultNamedNotOptArg):
		"""Get the enumeration value of an item"""
		return self._oleobj_.InvokeTypes(1296117816, LCID, 1, (3, 0), ((3, 1),),Index)

	def GetInteger(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type integer"""
		return self._oleobj_.InvokeTypes(1296117817, LCID, 1, (3, 0), ((3, 1),),Index)

	# Result is of type _ActionList
	def GetList(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type list"""
		ret = self._oleobj_.InvokeTypes(1296118065, LCID, 1, (9, 0), ((3, 1),),Index)
		if ret is not None:
			ret = Dispatch(ret, 'GetList', '{55031766-E456-4E54-A0D0-8E545601A2D8}', UnicodeToString=0)
		return ret

	def GetObjectType(self, Index=defaultNamedNotOptArg):
		"""Get the class ID of an object in an item of type object"""
		return self._oleobj_.InvokeTypes(1296118066, LCID, 1, (3, 0), ((3, 1),),Index)

	# Result is of type _ActionDescriptor
	def GetObjectValue(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type object"""
		ret = self._oleobj_.InvokeTypes(1296118067, LCID, 1, (9, 0), ((3, 1),),Index)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectValue', '{70A60330-E866-46AA-A715-ABF418C41453}', UnicodeToString=0)
		return ret

	def GetPath(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type Alias"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1296118068, LCID, 1, (8, 0), ((3, 1),),Index)

	# Result is of type _ActionReference
	def GetReference(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type ActionReference"""
		ret = self._oleobj_.InvokeTypes(1296118069, LCID, 1, (9, 0), ((3, 1),),Index)
		if ret is not None:
			ret = Dispatch(ret, 'GetReference', '{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}', UnicodeToString=0)
		return ret

	def GetString(self, Index=defaultNamedNotOptArg):
		"""Get the value of an item of type string"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1296118070, LCID, 1, (8, 0), ((3, 1),),Index)

	def GetType(self, Index=defaultNamedNotOptArg):
		"""Get the type of an item"""
		return self._oleobj_.InvokeTypes(1296118071, LCID, 1, (3, 0), ((3, 1),),Index)

	def GetUnitDoubleType(self, Index=defaultNamedNotOptArg):
		"""Get the unit type of an item of type UnitDouble"""
		return self._oleobj_.InvokeTypes(1296118072, LCID, 1, (3, 0), ((3, 1),),Index)

	def GetUnitDoubleValue(self, Index=defaultNamedNotOptArg):
		"""Get the value of anm item of type UnitDouble"""
		return self._oleobj_.InvokeTypes(1296118073, LCID, 1, (5, 0), ((3, 1),),Index)

	def PutBoolean(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118322, LCID, 1, (24, 0), ((11, 1),),Value)

	def PutClass(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118323, LCID, 1, (24, 0), ((3, 1),),Value)

	def PutDouble(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118324, LCID, 1, (24, 0), ((5, 1),),Value)

	def PutEnumerated(self, EnumType=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118325, LCID, 1, (24, 0), ((3, 1), (3, 1)),EnumType, Value)

	def PutInteger(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118326, LCID, 1, (24, 0), ((3, 1),),Value)

	def PutList(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118327, LCID, 1, (24, 0), ((9, 1),),Value)

	def PutObject(self, ClassID=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118328, LCID, 1, (24, 0), ((3, 1), (9, 1)),ClassID, Value)

	def PutPath(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118329, LCID, 1, (24, 0), ((8, 1),),Value)

	def PutReference(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118576, LCID, 1, (24, 0), ((9, 1),),Value)

	def PutString(self, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118577, LCID, 1, (24, 0), ((8, 1),),Value)

	def PutUnitDouble(self, UnitID=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118578, LCID, 1, (24, 0), ((3, 1), (5, 1)),UnitID, Value)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Count": (1346462580, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1346462580, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _ActionReference(DispatchBaseClass):
	CLSID = IID('{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}')
	coclass_clsid = IID('{A7C190CF-534E-4D85-A844-726762F0FAFC}')

	# Result is of type _ActionReference
	def GetContainer(self):
		ret = self._oleobj_.InvokeTypes(1296118579, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetContainer', '{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}', UnicodeToString=0)
		return ret

	def GetDesiredClass(self):
		return self._oleobj_.InvokeTypes(1296118580, LCID, 1, (3, 0), (),)

	def GetEnumeratedType(self):
		"""Get type of enumeration of an ActionReference whose form is 'Enumerated'"""
		return self._oleobj_.InvokeTypes(1296118581, LCID, 1, (3, 0), (),)

	def GetEnumeratedValue(self):
		"""Get value of enumeration of an ActionReference whose form is 'Enumerated'"""
		return self._oleobj_.InvokeTypes(1296118582, LCID, 1, (3, 0), (),)

	def GetForm(self):
		"""Get form of ActionReference"""
		return self._oleobj_.InvokeTypes(1296118583, LCID, 1, (3, 0), (),)

	def GetIdentifier(self):
		"""Get identifier value for an ActionReference whoxse form is 'Identifier'"""
		return self._oleobj_.InvokeTypes(1296118584, LCID, 1, (3, 0), (),)

	def GetIndex(self):
		"""Get index value for an ActionReference whoxse form is 'Index'"""
		return self._oleobj_.InvokeTypes(1296118585, LCID, 1, (3, 0), (),)

	def GetName(self):
		"""Get name value for an ActionReference whoxse form is 'Name'"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1296118832, LCID, 1, (8, 0), (),)

	def GetOffset(self):
		"""Get offset value for an ActionReference whoxse form is 'Offset'"""
		return self._oleobj_.InvokeTypes(1296118833, LCID, 1, (3, 0), (),)

	def GetProperty(self):
		"""Get property ID value for an ActionReference whoxse form is 'Property'"""
		return self._oleobj_.InvokeTypes(1296118834, LCID, 1, (3, 0), (),)

	def PutClass(self, DesiredClass=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118835, LCID, 1, (24, 0), ((3, 1),),DesiredClass)

	def PutEnumerated(self, DesiredClass=defaultNamedNotOptArg, EnumType=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118836, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),DesiredClass, EnumType, Value)

	def PutIdentifier(self, DesiredClass=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118837, LCID, 1, (24, 0), ((3, 1), (3, 1)),DesiredClass, Value)

	def PutIndex(self, DesiredClass=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118838, LCID, 1, (24, 0), ((3, 1), (3, 1)),DesiredClass, Value)

	def PutName(self, DesiredClass=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118839, LCID, 1, (24, 0), ((3, 1), (8, 1)),DesiredClass, Value)

	def PutOffset(self, DesiredClass=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118840, LCID, 1, (24, 0), ((3, 1), (3, 1)),DesiredClass, Value)

	def PutProperty(self, DesiredClass=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1296118841, LCID, 1, (24, 0), ((3, 1), (3, 1)),DesiredClass, Value)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _Application(DispatchBaseClass):
	"""The Adobe Photoshop application"""
	CLSID = IID('{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}')
	coclass_clsid = IID('{16AA0B9E-79AC-43B5-86CA-AB961FBEED5F}')

	def Batch(self, InputFiles=defaultNamedNotOptArg, Action=defaultNamedNotOptArg, From=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""run the batch automation routine"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1112813617, LCID, 1, (8, 0), ((12, 1), (8, 1), (8, 1), (12, 17)),InputFiles, Action, From, Options)

	def ChangeColorSettings(self, Name=defaultNamedOptArg, File=defaultNamedOptArg):
		"""set Color Settings to a named set or to the contents of a settings file"""
		return self._oleobj_.InvokeTypes(1130906490, LCID, 1, (24, 0), ((12, 17), (12, 17)),Name, File)

	def CharIDToTypeID(self, CharID=defaultNamedNotOptArg):
		"""convert from a four character code to a runtime ID"""
		return self._oleobj_.InvokeTypes(1098002483, LCID, 1, (3, 0), ((8, 1),),CharID)

	def DoAction(self, Action=defaultNamedNotOptArg, From=defaultNamedNotOptArg):
		"""play an action from the Actions Palette"""
		return self._oleobj_.InvokeTypes(1148141923, LCID, 1, (24, 0), ((8, 1), (8, 1)),Action, From)

	def DoJavaScript(self, JavaScriptCode=defaultNamedNotOptArg, Arguments=defaultNamedOptArg, ExecutionMode=defaultNamedOptArg):
		"""execute JavaScript code"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1147828311, LCID, 1, (8, 0), ((8, 1), (12, 17), (12, 17)),JavaScriptCode, Arguments, ExecutionMode)

	def DoJavaScriptFile(self, JavaScriptFile=defaultNamedNotOptArg, Arguments=defaultNamedOptArg, ExecutionMode=defaultNamedOptArg):
		"""execute javascript file"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1147823703, LCID, 1, (8, 0), ((8, 1), (12, 17), (12, 17)),JavaScriptFile, Arguments, ExecutionMode)

	# Result is of type _ActionDescriptor
	def ExecuteAction(self, EventID=defaultNamedNotOptArg, Descriptor=defaultNamedOptArg, DisplayDialogs=defaultNamedOptArg):
		"""play an ActionManager event"""
		ret = self._oleobj_.InvokeTypes(1349280121, LCID, 1, (9, 0), ((3, 1), (12, 17), (12, 17)),EventID, Descriptor, DisplayDialogs)
		if ret is not None:
			ret = Dispatch(ret, 'ExecuteAction', '{70A60330-E866-46AA-A715-ABF418C41453}', UnicodeToString=0)
		return ret

	# Result is of type _ActionDescriptor
	def ExecuteActionGet(self, Reference=defaultNamedNotOptArg):
		"""obtain an action descriptor"""
		ret = self._oleobj_.InvokeTypes(1095198068, LCID, 1, (9, 0), ((9, 1),),Reference)
		if ret is not None:
			ret = Dispatch(ret, 'ExecuteActionGet', '{70A60330-E866-46AA-A715-ABF418C41453}', UnicodeToString=0)
		return ret

	def Load(self, Document=defaultNamedNotOptArg):
		"""load a support document"""
		return self._oleobj_.InvokeTypes(1281643372, LCID, 1, (24, 0), ((8, 1),),Document)

	def MakeContactSheet(self, InputFiles=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""create a contact sheet from multiple files"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1129599816, LCID, 1, (8, 0), ((12, 1), (12, 17)),InputFiles, Options)

	def MakePDFPresentation(self, InputFiles=defaultNamedNotOptArg, OutputFile=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""create a PDF presentation file"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1346651697, LCID, 1, (8, 0), ((12, 1), (8, 1), (12, 17)),InputFiles, OutputFile, Options)

	def MakePhotoGallery(self, InputFolder=defaultNamedNotOptArg, OutputFolder=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""create a web photo gallery"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(2004316263, LCID, 1, (8, 0), ((12, 1), (8, 1), (12, 17)),InputFolder, OutputFolder, Options)

	def MakePhotomerge(self, InputFiles=defaultNamedNotOptArg):
		"""merge multiple files into one, user interaction required"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1886678375, LCID, 1, (8, 0), ((12, 1),),InputFiles)

	def MakePicturePackage(self, InputFiles=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		"""create a picture package from multiple files"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1347702859, LCID, 1, (8, 0), ((12, 1), (12, 17)),InputFiles, Options)

	# Result is of type Document
	def Open(self, Document=defaultNamedNotOptArg, As=defaultNamedOptArg):
		"""open the specified document"""
		ret = self._oleobj_.InvokeTypes(1349731151, LCID, 1, (9, 0), ((8, 1), (12, 17)),Document, As)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{B1ADEFB6-C536-42D6-8A83-397354A769F8}', UnicodeToString=0)
		return ret

	def Purge(self, Target=defaultNamedNotOptArg):
		"""purges one or more caches"""
		return self._oleobj_.InvokeTypes(1349874279, LCID, 1, (24, 0), ((3, 1),),Target)

	def Quit(self):
		"""quit the application"""
		return self._oleobj_.InvokeTypes(1903520116, LCID, 1, (24, 0), (),)

	def SetBackgroundColor(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(1650934627, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetForegroundColor(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(1718043491, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetPlaybackParameters(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(1885499424, LCID, 8, (24, 0), ((9, 0),),arg0)

	def StringIDToTypeID(self, StringID=defaultNamedNotOptArg):
		"""convert from a string ID to a runtime ID"""
		return self._oleobj_.InvokeTypes(1098002481, LCID, 1, (3, 0), ((8, 1),),StringID)

	def TypeIDToCharID(self, TypeID=defaultNamedNotOptArg):
		"""convert from a runtime ID to a character ID"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1098002484, LCID, 1, (8, 0), ((3, 1),),TypeID)

	def TypeIDToStringID(self, TypeID=defaultNamedNotOptArg):
		"""convert from a runtime ID to a string ID"""
		# Result is a Unicode object - return as-is for this version of Python
		return self._oleobj_.InvokeTypes(1098002482, LCID, 1, (8, 0), ((3, 1),),TypeID)

	_prop_map_get_ = {
		# Method 'ActiveDocument' returns object of type 'Document'
		"ActiveDocument": (1883325539, 2, (9, 0), (), "ActiveDocument", '{B1ADEFB6-C536-42D6-8A83-397354A769F8}'),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'BackgroundColor' returns object of type '_SolidColor'
		"BackgroundColor": (1650934627, 2, (9, 0), (), "BackgroundColor", '{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}'),
		"ColorSettings": (1129988974, 2, (8, 0), (), "ColorSettings", None),
		"DisplayDialogs": (1096116556, 2, (3, 0), (), "DisplayDialogs", None),
		# Method 'Documents' returns object of type 'Documents'
		"Documents": (1685021557, 2, (9, 0), (), "Documents", '{662506C7-6AAE-4422-ACA4-C63627CB1868}'),
		# Method 'Fonts' returns object of type 'TextFonts'
		"Fonts": (1665560180, 2, (9, 0), (), "Fonts", '{BBCE52D6-5D4B-4691-99E3-62C174BD2855}'),
		# Method 'ForegroundColor' returns object of type '_SolidColor'
		"ForegroundColor": (1718043491, 2, (9, 0), (), "ForegroundColor", '{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}'),
		"FreeMemory": (1883655501, 2, (5, 0), (), "FreeMemory", None),
		"Locale": (1818452332, 2, (8, 0), (), "Locale", None),
		"MacintoshFileTypes": (1836344948, 2, (12, 0), (), "MacintoshFileTypes", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'Notifiers' returns object of type 'Notifiers'
		"Notifiers": (1162752050, 2, (9, 0), (), "Notifiers", '{861C9290-2A0C-4614-8606-706B31BFD45B}'),
		"NotifiersEnabled": (1162752054, 2, (11, 0), (), "NotifiersEnabled", None),
		"Path": (1884320872, 2, (8, 0), (), "Path", None),
		"PlaybackDisplayDialogs": (1885496420, 2, (3, 0), (), "PlaybackDisplayDialogs", None),
		# Method 'PlaybackParameters' returns object of type '_ActionDescriptor'
		"PlaybackParameters": (1885499424, 2, (9, 0), (), "PlaybackParameters", '{70A60330-E866-46AA-A715-ABF418C41453}'),
		# Method 'Preferences' returns object of type 'Preferences'
		"Preferences": (1884320358, 2, (9, 0), (), "Preferences", '{288BC58E-AB6A-467C-B244-D225349E3EB3}'),
		"PreferencesFolder": (1886545516, 2, (8, 0), (), "PreferencesFolder", None),
		"ScriptingVersion": (1884518003, 2, (8, 0), (), "ScriptingVersion", None),
		"Version": (1986359923, 2, (8, 0), (), "Version", None),
		"Visible": (1884640883, 2, (11, 0), (), "Visible", None),
		"WinColorSettings": (1129988973, 2, (8, 0), (), "WinColorSettings", None),
		"WindowsFileTypes": (2003723892, 2, (12, 0), (), "WindowsFileTypes", None),
	}
	_prop_map_put_ = {
		"ActiveDocument": ((1883325539, LCID, 4, 0),()),
		"BackgroundColor": ((1650934627, LCID, 4, 0),()),
		"DisplayDialogs": ((1096116556, LCID, 4, 0),()),
		"ForegroundColor": ((1718043491, LCID, 4, 0),()),
		"NotifiersEnabled": ((1162752054, LCID, 4, 0),()),
		"PlaybackDisplayDialogs": ((1885496420, LCID, 4, 0),()),
		"PlaybackParameters": ((1885499424, LCID, 4, 0),()),
		"Visible": ((1884640883, LCID, 4, 0),()),
	}

class _BMPSaveOptions(DispatchBaseClass):
	"""Settings related to saving a BMP document"""
	CLSID = IID('{4D40BE2D-FE11-4060-B52A-DE31C837D51D}')
	coclass_clsid = IID('{EBDBA1ED-D57D-4CCD-BD9E-CB60E5E6CB07}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Depth": (1145205613, 2, (3, 0), (), "Depth", None),
		"FlipRowOrder": (1181766255, 2, (11, 0), (), "FlipRowOrder", None),
		"OSType": (1884573523, 2, (3, 0), (), "OSType", None),
		"RLECompression": (1884441669, 2, (11, 0), (), "RLECompression", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"Depth": ((1145205613, LCID, 4, 0),()),
		"FlipRowOrder": ((1181766255, LCID, 4, 0),()),
		"OSType": ((1884573523, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RLECompression": ((1884441669, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _BatchOptions(DispatchBaseClass):
	"""options for the Batch command"""
	CLSID = IID('{B0D18870-EAC3-4D35-8612-6F734B3FA656}')
	coclass_clsid = IID('{6EF2BC9F-827B-455B-89C9-5AB3AA233790}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Destination": (1112813622, 2, (3, 0), (), "Destination", None),
		"DestinationFolder": (1112814391, 2, (8, 0), (), "DestinationFolder", None),
		"ErrorFile": (1112813875, 2, (8, 0), (), "ErrorFile", None),
		"FileNaming": (1112813624, 2, (12, 0), (), "FileNaming", None),
		"MacintoshCompatible": (1112813873, 2, (11, 0), (), "MacintoshCompatible", None),
		"OverrideOpen": (1112813619, 2, (11, 0), (), "OverrideOpen", None),
		"OverrideSave": (1112813623, 2, (11, 0), (), "OverrideSave", None),
		"StartingSerial": (1112813625, 2, (3, 0), (), "StartingSerial", None),
		"SuppressOpen": (1112813620, 2, (11, 0), (), "SuppressOpen", None),
		"SuppressProfile": (1112813621, 2, (11, 0), (), "SuppressProfile", None),
		"UnixCompatible": (1112813874, 2, (11, 0), (), "UnixCompatible", None),
		"WindowsCompatible": (1112813872, 2, (11, 0), (), "WindowsCompatible", None),
	}
	_prop_map_put_ = {
		"Destination": ((1112813622, LCID, 4, 0),()),
		"DestinationFolder": ((1112814391, LCID, 4, 0),()),
		"ErrorFile": ((1112813875, LCID, 4, 0),()),
		"FileNaming": ((1112813624, LCID, 4, 0),()),
		"MacintoshCompatible": ((1112813873, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"OverrideOpen": ((1112813619, LCID, 4, 0),()),
		"OverrideSave": ((1112813623, LCID, 4, 0),()),
		"StartingSerial": ((1112813625, LCID, 4, 0),()),
		"SuppressOpen": ((1112813620, LCID, 4, 0),()),
		"SuppressProfile": ((1112813621, LCID, 4, 0),()),
		"UnixCompatible": ((1112813874, LCID, 4, 0),()),
		"WindowsCompatible": ((1112813872, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _BitmapConversionOptions(DispatchBaseClass):
	"""Settings related to changing the document mode to Bitmap"""
	CLSID = IID('{643099A1-0B67-4920-9B14-E14BE8F63D5F}')
	coclass_clsid = IID('{B861C213-1A7F-4FE3-A19B-3927EBEA7BD8}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"Angle": (1097754476, 2, (5, 0), (), "Angle", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Frequency": (1181836153, 2, (5, 0), (), "Frequency", None),
		"Method": (1131826548, 2, (3, 0), (), "Method", None),
		"PatternName": (1348554349, 2, (8, 0), (), "PatternName", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"Shape": (1399018344, 2, (3, 0), (), "Shape", None),
	}
	_prop_map_put_ = {
		"Angle": ((1097754476, LCID, 4, 0),()),
		"Frequency": ((1181836153, LCID, 4, 0),()),
		"Method": ((1131826548, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PatternName": ((1348554349, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
		"Shape": ((1399018344, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _CMYKColor(DispatchBaseClass):
	"""A CMYK color specification"""
	CLSID = IID('{29C13F49-BCEF-4FE2-BFC7-6F03B82B726F}')
	coclass_clsid = IID('{41EBBED9-0E3C-45B8-8C78-7B07FAF46AD2}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Black": (1883458422, 2, (5, 0), (), "Black", None),
		"Cyan": (1883456374, 2, (5, 0), (), "Cyan", None),
		"Magenta": (1883458934, 2, (5, 0), (), "Magenta", None),
		"Yellow": (1883462006, 2, (5, 0), (), "Yellow", None),
	}
	_prop_map_put_ = {
		"Black": ((1883458422, LCID, 4, 0),()),
		"Cyan": ((1883456374, LCID, 4, 0),()),
		"Magenta": ((1883458934, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Yellow": ((1883462006, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _CameraRAWOpenOptions(DispatchBaseClass):
	"""Settings related to opening a camera RAW document"""
	CLSID = IID('{65D1B010-0D87-481C-B2E6-22EFB5A54129}')
	coclass_clsid = IID('{A35CD676-3F1A-405B-B97B-6FB59011E7E3}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"BitsPerChannel": (1145201512, 2, (3, 0), (), "BitsPerChannel", None),
		"BlueHue": (1129460530, 2, (3, 0), (), "BlueHue", None),
		"BlueSaturation": (1129460531, 2, (3, 0), (), "BlueSaturation", None),
		"Brightness": (1114141806, 2, (3, 0), (), "Brightness", None),
		"ChromaticAberrationBY": (1129460276, 2, (3, 0), (), "ChromaticAberrationBY", None),
		"ChromaticAberrationRC": (1129460275, 2, (3, 0), (), "ChromaticAberrationRC", None),
		"ColorNoiseReduction": (1129460274, 2, (3, 0), (), "ColorNoiseReduction", None),
		"ColorSpace": (1131172720, 2, (3, 0), (), "ColorSpace", None),
		"Contrast": (1129460025, 2, (3, 0), (), "Contrast", None),
		"Exposure": (1129460023, 2, (5, 0), (), "Exposure", None),
		"GreenHue": (1129460528, 2, (3, 0), (), "GreenHue", None),
		"GreenSaturation": (1129460529, 2, (3, 0), (), "GreenSaturation", None),
		"LuminanceSmoothing": (1129460273, 2, (3, 0), (), "LuminanceSmoothing", None),
		"RedHue": (1129460280, 2, (3, 0), (), "RedHue", None),
		"RedSaturation": (1129460281, 2, (3, 0), (), "RedSaturation", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"Saturation": (1884512628, 2, (3, 0), (), "Saturation", None),
		"Settings": (1884320358, 2, (3, 0), (), "Settings", None),
		"ShadowTint": (1129460279, 2, (3, 0), (), "ShadowTint", None),
		"Shadows": (1094004785, 2, (3, 0), (), "Shadows", None),
		"Sharpness": (1129460272, 2, (3, 0), (), "Sharpness", None),
		"Size": (1886679930, 2, (3, 0), (), "Size", None),
		"Temperature": (1129460021, 2, (3, 0), (), "Temperature", None),
		"Tint": (1129460022, 2, (3, 0), (), "Tint", None),
		"VignettingAmount": (1129460277, 2, (3, 0), (), "VignettingAmount", None),
		"VignettingMidpoint": (1129460278, 2, (3, 0), (), "VignettingMidpoint", None),
		"WhiteBalance": (1129460020, 2, (3, 0), (), "WhiteBalance", None),
	}
	_prop_map_put_ = {
		"BitsPerChannel": ((1145201512, LCID, 4, 0),()),
		"BlueHue": ((1129460530, LCID, 4, 0),()),
		"BlueSaturation": ((1129460531, LCID, 4, 0),()),
		"Brightness": ((1114141806, LCID, 4, 0),()),
		"ChromaticAberrationBY": ((1129460276, LCID, 4, 0),()),
		"ChromaticAberrationRC": ((1129460275, LCID, 4, 0),()),
		"ColorNoiseReduction": ((1129460274, LCID, 4, 0),()),
		"ColorSpace": ((1131172720, LCID, 4, 0),()),
		"Contrast": ((1129460025, LCID, 4, 0),()),
		"Exposure": ((1129460023, LCID, 4, 0),()),
		"GreenHue": ((1129460528, LCID, 4, 0),()),
		"GreenSaturation": ((1129460529, LCID, 4, 0),()),
		"LuminanceSmoothing": ((1129460273, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RedHue": ((1129460280, LCID, 4, 0),()),
		"RedSaturation": ((1129460281, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
		"Saturation": ((1884512628, LCID, 4, 0),()),
		"Settings": ((1884320358, LCID, 4, 0),()),
		"ShadowTint": ((1129460279, LCID, 4, 0),()),
		"Shadows": ((1094004785, LCID, 4, 0),()),
		"Sharpness": ((1129460272, LCID, 4, 0),()),
		"Size": ((1886679930, LCID, 4, 0),()),
		"Temperature": ((1129460021, LCID, 4, 0),()),
		"Tint": ((1129460022, LCID, 4, 0),()),
		"VignettingAmount": ((1129460277, LCID, 4, 0),()),
		"VignettingMidpoint": ((1129460278, LCID, 4, 0),()),
		"WhiteBalance": ((1129460020, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _ContactSheetOptions(DispatchBaseClass):
	"""options for the Contact Sheet command"""
	CLSID = IID('{064BBE94-396D-4B25-9071-AC5B14D0487F}')
	coclass_clsid = IID('{D765F6C2-748B-476B-8884-E5118E646179}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AcrossFirst": (1129525298, 2, (11, 0), (), "AcrossFirst", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"BestFit": (1129525301, 2, (11, 0), (), "BestFit", None),
		"Caption": (1147744305, 2, (11, 0), (), "Caption", None),
		"ColumnCount": (1346844471, 2, (3, 0), (), "ColumnCount", None),
		"Flatten": (1129525300, 2, (11, 0), (), "Flatten", None),
		"Font": (1665560180, 2, (3, 0), (), "Font", None),
		"FontSize": (1346844468, 2, (3, 0), (), "FontSize", None),
		"Height": (1214736500, 2, (3, 0), (), "Height", None),
		"Horizontal": (1215451002, 2, (3, 0), (), "Horizontal", None),
		"Mode": (1330472037, 2, (3, 0), (), "Mode", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"RowCount": (1346844472, 2, (3, 0), (), "RowCount", None),
		"UseAutoSpacing": (1129525299, 2, (11, 0), (), "UseAutoSpacing", None),
		"Vertical": (1450463098, 2, (3, 0), (), "Vertical", None),
		"Width": (1466201192, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"AcrossFirst": ((1129525298, LCID, 4, 0),()),
		"BestFit": ((1129525301, LCID, 4, 0),()),
		"Caption": ((1147744305, LCID, 4, 0),()),
		"ColumnCount": ((1346844471, LCID, 4, 0),()),
		"Flatten": ((1129525300, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"FontSize": ((1346844468, LCID, 4, 0),()),
		"Height": ((1214736500, LCID, 4, 0),()),
		"Horizontal": ((1215451002, LCID, 4, 0),()),
		"Mode": ((1330472037, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
		"RowCount": ((1346844472, LCID, 4, 0),()),
		"UseAutoSpacing": ((1129525299, LCID, 4, 0),()),
		"Vertical": ((1450463098, LCID, 4, 0),()),
		"Width": ((1466201192, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _DCS1_SaveOptions(DispatchBaseClass):
	"""Settings related to saving a Photoshop DCS 1.0 document"""
	CLSID = IID('{94C4A25A-2C91-4514-A783-3173AFC48430}')
	coclass_clsid = IID('{B1C1FEB9-C46D-4959-9B92-A962FA41C511}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"DCS": (1145271139, 2, (3, 0), (), "DCS", None),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"Encoding": (1164854116, 2, (3, 0), (), "Encoding", None),
		"HalftoneScreen": (1214665838, 2, (11, 0), (), "HalftoneScreen", None),
		"Interpolation": (1231898960, 2, (11, 0), (), "Interpolation", None),
		"Preview": (1349997635, 2, (3, 0), (), "Preview", None),
		"TransferFunction": (1416849010, 2, (11, 0), (), "TransferFunction", None),
		"VectorData": (1449346164, 2, (11, 0), (), "VectorData", None),
	}
	_prop_map_put_ = {
		"DCS": ((1145271139, LCID, 4, 0),()),
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"Encoding": ((1164854116, LCID, 4, 0),()),
		"HalftoneScreen": ((1214665838, LCID, 4, 0),()),
		"Interpolation": ((1231898960, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Preview": ((1349997635, LCID, 4, 0),()),
		"TransferFunction": ((1416849010, LCID, 4, 0),()),
		"VectorData": ((1449346164, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _DCS2_SaveOptions(DispatchBaseClass):
	"""Settings related to saving a Photoshop DCS 2.0 document"""
	CLSID = IID('{F1AF982E-2BBD-406D-9FD6-CA6C898A7FFE}')
	coclass_clsid = IID('{61DA6070-5785-4C7F-9785-C7036D01B1BE}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"DCS": (1145271139, 2, (3, 0), (), "DCS", None),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"Encoding": (1164854116, 2, (3, 0), (), "Encoding", None),
		"HalftoneScreen": (1214665838, 2, (11, 0), (), "HalftoneScreen", None),
		"Interpolation": (1231898960, 2, (11, 0), (), "Interpolation", None),
		"MultiFileDCS": (1145269606, 2, (11, 0), (), "MultiFileDCS", None),
		"Preview": (1349997635, 2, (3, 0), (), "Preview", None),
		"SpotColors": (1884509043, 2, (11, 0), (), "SpotColors", None),
		"TransferFunction": (1416849010, 2, (11, 0), (), "TransferFunction", None),
		"VectorData": (1449346164, 2, (11, 0), (), "VectorData", None),
	}
	_prop_map_put_ = {
		"DCS": ((1145271139, LCID, 4, 0),()),
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"Encoding": ((1164854116, LCID, 4, 0),()),
		"HalftoneScreen": ((1214665838, LCID, 4, 0),()),
		"Interpolation": ((1231898960, LCID, 4, 0),()),
		"MultiFileDCS": ((1145269606, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Preview": ((1349997635, LCID, 4, 0),()),
		"SpotColors": ((1884509043, LCID, 4, 0),()),
		"TransferFunction": ((1416849010, LCID, 4, 0),()),
		"VectorData": ((1449346164, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _EPSOpenOptions(DispatchBaseClass):
	"""Settings related to opening a generic EPS document"""
	CLSID = IID('{F715C957-54CE-4E55-9856-591D4CD082FD}')
	coclass_clsid = IID('{7468F85C-D655-4331-890E-4086C70CF67A}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AntiAlias": (1097744748, 2, (11, 0), (), "AntiAlias", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"ConstrainProportions": (1129345616, 2, (11, 0), (), "ConstrainProportions", None),
		"Height": (1214736500, 2, (5, 0), (), "Height", None),
		"Mode": (1330472037, 2, (3, 0), (), "Mode", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"Width": (1466201192, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"AntiAlias": ((1097744748, LCID, 4, 0),()),
		"ConstrainProportions": ((1129345616, LCID, 4, 0),()),
		"Height": ((1214736500, LCID, 4, 0),()),
		"Mode": ((1330472037, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
		"Width": ((1466201192, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _EPSSaveOptions(DispatchBaseClass):
	"""Settings related to saving an EPS document"""
	CLSID = IID('{D54491EF-6F09-4DE3-B49A-D57EDB2F40B8}')
	coclass_clsid = IID('{074B66CB-4BEF-4A83-A699-77F33D3CD5E0}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"Encoding": (1164854116, 2, (3, 0), (), "Encoding", None),
		"HalftoneScreen": (1214665838, 2, (11, 0), (), "HalftoneScreen", None),
		"Interpolation": (1231898960, 2, (11, 0), (), "Interpolation", None),
		"PSColorManagement": (1349731149, 2, (11, 0), (), "PSColorManagement", None),
		"Preview": (1349997635, 2, (3, 0), (), "Preview", None),
		"TransferFunction": (1416849010, 2, (11, 0), (), "TransferFunction", None),
		"TransparentWhites": (1416648552, 2, (11, 0), (), "TransparentWhites", None),
		"VectorData": (1449346164, 2, (11, 0), (), "VectorData", None),
	}
	_prop_map_put_ = {
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"Encoding": ((1164854116, LCID, 4, 0),()),
		"HalftoneScreen": ((1214665838, LCID, 4, 0),()),
		"Interpolation": ((1231898960, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PSColorManagement": ((1349731149, LCID, 4, 0),()),
		"Preview": ((1349997635, LCID, 4, 0),()),
		"TransferFunction": ((1416849010, LCID, 4, 0),()),
		"TransparentWhites": ((1416648552, LCID, 4, 0),()),
		"VectorData": ((1449346164, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _ExportOptionsIllustrator(DispatchBaseClass):
	"""Settings related to exporting Illustrator paths"""
	CLSID = IID('{FC08B435-5F19-49DF-ABE7-ADCE9F0729FF}')
	coclass_clsid = IID('{CACEC2F5-EC15-4DFD-8955-244D2A7EFE60}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Path": (1416056948, 2, (3, 0), (), "Path", None),
		"PathName": (1414557293, 2, (8, 0), (), "PathName", None),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Path": ((1416056948, LCID, 4, 0),()),
		"PathName": ((1414557293, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _ExportOptionsSaveForWeb(DispatchBaseClass):
	"""Settings related to exporting Save For Web files"""
	CLSID = IID('{91A3D47B-9579-4013-9206-7B6859439DA2}')
	coclass_clsid = IID('{D434C3C7-5BCA-4856-8A21-AF46C2147FD0}')

	def SetMatteColor(self, arg0=defaultUnnamedArg):
		"""defines colors to blend transparnet pixels against"""
		return self._oleobj_.InvokeTypes(1299477605, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Blur": (1177563185, 2, (5, 0), (), "Blur", None),
		"ColorReduction": (1395939124, 2, (3, 0), (), "ColorReduction", None),
		"Colors": (1884308302, 2, (3, 0), (), "Colors", None),
		"Dither": (1148474480, 2, (3, 0), (), "Dither", None),
		"DitherAmount": (1148469613, 2, (3, 0), (), "DitherAmount", None),
		"Format": (1718383728, 2, (3, 0), (), "Format", None),
		"IncludeProfile": (1395939129, 2, (11, 0), (), "IncludeProfile", None),
		"Interlaced": (1383550834, 2, (11, 0), (), "Interlaced", None),
		"Lossy": (1395939123, 2, (3, 0), (), "Lossy", None),
		# Method 'MatteColor' returns object of type '_RGBColor'
		"MatteColor": (1299477605, 2, (9, 0), (), "MatteColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		"Optimized": (1395939128, 2, (11, 0), (), "Optimized", None),
		"PNG8": (1395939122, 2, (11, 0), (), "PNG8", None),
		"Quality": (1366062201, 2, (3, 0), (), "Quality", None),
		"Transparency": (1416786019, 2, (11, 0), (), "Transparency", None),
		"TransparencyAmount": (1395939126, 2, (3, 0), (), "TransparencyAmount", None),
		"TransparencyDither": (1395939125, 2, (3, 0), (), "TransparencyDither", None),
		"WebSnap": (1395939127, 2, (3, 0), (), "WebSnap", None),
	}
	_prop_map_put_ = {
		"Blur": ((1177563185, LCID, 4, 0),()),
		"ColorReduction": ((1395939124, LCID, 4, 0),()),
		"Colors": ((1884308302, LCID, 4, 0),()),
		"Dither": ((1148474480, LCID, 4, 0),()),
		"DitherAmount": ((1148469613, LCID, 4, 0),()),
		"Format": ((1718383728, LCID, 4, 0),()),
		"IncludeProfile": ((1395939129, LCID, 4, 0),()),
		"Interlaced": ((1383550834, LCID, 4, 0),()),
		"Lossy": ((1395939123, LCID, 4, 0),()),
		"MatteColor": ((1299477605, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Optimized": ((1395939128, LCID, 4, 0),()),
		"PNG8": ((1395939122, LCID, 4, 0),()),
		"Quality": ((1366062201, LCID, 4, 0),()),
		"Transparency": ((1416786019, LCID, 4, 0),()),
		"TransparencyAmount": ((1395939126, LCID, 4, 0),()),
		"TransparencyDither": ((1395939125, LCID, 4, 0),()),
		"WebSnap": ((1395939127, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GIFSaveOptions(DispatchBaseClass):
	"""Settings related to saving a GIF document"""
	CLSID = IID('{89417281-E1AF-4800-B82A-9F37ED0478EF}')
	coclass_clsid = IID('{22F619C0-72B1-46FC-B04B-DC364CD0C33E}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Colors": (1884308302, 2, (3, 0), (), "Colors", None),
		"Dither": (1148474480, 2, (3, 0), (), "Dither", None),
		"DitherAmount": (1148469613, 2, (3, 0), (), "DitherAmount", None),
		"Forced": (1346790252, 2, (3, 0), (), "Forced", None),
		"Interlaced": (1383550834, 2, (11, 0), (), "Interlaced", None),
		"Matte": (1299477605, 2, (3, 0), (), "Matte", None),
		"Palette": (1347447924, 2, (3, 0), (), "Palette", None),
		"PreserveExactColors": (1146119544, 2, (11, 0), (), "PreserveExactColors", None),
		"Transparency": (1416786019, 2, (11, 0), (), "Transparency", None),
	}
	_prop_map_put_ = {
		"Colors": ((1884308302, LCID, 4, 0),()),
		"Dither": ((1148474480, LCID, 4, 0),()),
		"DitherAmount": ((1148469613, LCID, 4, 0),()),
		"Forced": ((1346790252, LCID, 4, 0),()),
		"Interlaced": ((1383550834, LCID, 4, 0),()),
		"Matte": ((1299477605, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Palette": ((1347447924, LCID, 4, 0),()),
		"PreserveExactColors": ((1146119544, LCID, 4, 0),()),
		"Transparency": ((1416786019, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GalleryBannerOptions(DispatchBaseClass):
	"""options for the web photo gallery banner options"""
	CLSID = IID('{5F168D2A-F9EA-4866-8C55-4875E0940622}')
	coclass_clsid = IID('{D5D9C71A-56DC-459D-A433-9B8C334165A5}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"ContactInfo": (1346843953, 2, (8, 0), (), "ContactInfo", None),
		"Date": (1346843954, 2, (8, 0), (), "Date", None),
		"Font": (1665560180, 2, (3, 0), (), "Font", None),
		"FontSize": (1346844468, 2, (3, 0), (), "FontSize", None),
		"Photographer": (1346843952, 2, (8, 0), (), "Photographer", None),
		"SiteName": (1346843705, 2, (8, 0), (), "SiteName", None),
	}
	_prop_map_put_ = {
		"ContactInfo": ((1346843953, LCID, 4, 0),()),
		"Date": ((1346843954, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"FontSize": ((1346844468, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Photographer": ((1346843952, LCID, 4, 0),()),
		"SiteName": ((1346843705, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GalleryCustomColorOptions(DispatchBaseClass):
	"""options for the web photo gallery colors"""
	CLSID = IID('{2EB2592D-F02D-4117-A22C-26E5CDFAEEE2}')
	coclass_clsid = IID('{6F3B0065-21DB-44A6-BF09-624D88ECF768}')

	def SetActiveLinkColor(self, arg0=defaultUnnamedArg):
		"""active link color"""
		return self._oleobj_.InvokeTypes(1346844723, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetBackgroundColor(self, arg0=defaultUnnamedArg):
		"""background color"""
		return self._oleobj_.InvokeTypes(1114063730, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetBannerColor(self, arg0=defaultUnnamedArg):
		"""banner color"""
		return self._oleobj_.InvokeTypes(1346844721, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetLinkColor(self, arg0=defaultUnnamedArg):
		"""link color"""
		return self._oleobj_.InvokeTypes(1346844724, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetTextColor(self, arg0=defaultUnnamedArg):
		"""text color"""
		return self._oleobj_.InvokeTypes(1346844722, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetVisitedLinkColor(self, arg0=defaultUnnamedArg):
		"""visited link color"""
		return self._oleobj_.InvokeTypes(1346844725, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'ActiveLinkColor' returns object of type '_RGBColor'
		"ActiveLinkColor": (1346844723, 2, (9, 0), (), "ActiveLinkColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'BackgroundColor' returns object of type '_RGBColor'
		"BackgroundColor": (1114063730, 2, (9, 0), (), "BackgroundColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		# Method 'BannerColor' returns object of type '_RGBColor'
		"BannerColor": (1346844721, 2, (9, 0), (), "BannerColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		# Method 'LinkColor' returns object of type '_RGBColor'
		"LinkColor": (1346844724, 2, (9, 0), (), "LinkColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		# Method 'TextColor' returns object of type '_RGBColor'
		"TextColor": (1346844722, 2, (9, 0), (), "TextColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		# Method 'VisitedLinkColor' returns object of type '_RGBColor'
		"VisitedLinkColor": (1346844725, 2, (9, 0), (), "VisitedLinkColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
	}
	_prop_map_put_ = {
		"ActiveLinkColor": ((1346844723, LCID, 4, 0),()),
		"BackgroundColor": ((1114063730, LCID, 4, 0),()),
		"BannerColor": ((1346844721, LCID, 4, 0),()),
		"LinkColor": ((1346844724, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"TextColor": ((1346844722, LCID, 4, 0),()),
		"VisitedLinkColor": ((1346844725, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GalleryImagesOptions(DispatchBaseClass):
	"""options for the web photo gallery images"""
	CLSID = IID('{46AB9A1D-1B32-4C59-8142-B223ECCF1F74}')
	coclass_clsid = IID('{26BB16C1-67D1-44A7-AA75-DD2F361352E3}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Border": (1346844208, 2, (3, 0), (), "Border", None),
		"Caption": (1147744305, 2, (11, 0), (), "Caption", None),
		"Dimension": (1346843959, 2, (3, 0), (), "Dimension", None),
		"Font": (1665560180, 2, (3, 0), (), "Font", None),
		"FontSize": (1346844468, 2, (3, 0), (), "FontSize", None),
		"ImageQuality": (1346843961, 2, (3, 0), (), "ImageQuality", None),
		"IncludeCopyright": (1346844213, 2, (11, 0), (), "IncludeCopyright", None),
		"IncludeCredits": (1346844211, 2, (11, 0), (), "IncludeCredits", None),
		"IncludeFilename": (1346844209, 2, (11, 0), (), "IncludeFilename", None),
		"IncludeTitle": (1346844212, 2, (11, 0), (), "IncludeTitle", None),
		"NumericLinks": (1346843957, 2, (11, 0), (), "NumericLinks", None),
		"ResizeConstraint": (1346843960, 2, (3, 0), (), "ResizeConstraint", None),
		"ResizeImages": (1346843958, 2, (11, 0), (), "ResizeImages", None),
	}
	_prop_map_put_ = {
		"Border": ((1346844208, LCID, 4, 0),()),
		"Caption": ((1147744305, LCID, 4, 0),()),
		"Dimension": ((1346843959, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"FontSize": ((1346844468, LCID, 4, 0),()),
		"ImageQuality": ((1346843961, LCID, 4, 0),()),
		"IncludeCopyright": ((1346844213, LCID, 4, 0),()),
		"IncludeCredits": ((1346844211, LCID, 4, 0),()),
		"IncludeFilename": ((1346844209, LCID, 4, 0),()),
		"IncludeTitle": ((1346844212, LCID, 4, 0),()),
		"NumericLinks": ((1346843957, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"ResizeConstraint": ((1346843960, LCID, 4, 0),()),
		"ResizeImages": ((1346843958, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GalleryOptions(DispatchBaseClass):
	"""options for the web photo gallery command"""
	CLSID = IID('{C2783141-B50D-4F0C-9E2E-BF76EA8A4E60}')
	coclass_clsid = IID('{B10D4055-8C78-4C7F-BAE7-5B5FFDED928A}')

	def SetBannerOptions(self, arg0=defaultUnnamedArg):
		"""options related to banner settings"""
		return self._oleobj_.InvokeTypes(1346843956, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetCustomColorOptions(self, arg0=defaultUnnamedArg):
		"""options related to custom color settings"""
		return self._oleobj_.InvokeTypes(1346843703, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetImagesOptions(self, arg0=defaultUnnamedArg):
		"""options related to images settings"""
		return self._oleobj_.InvokeTypes(1346843701, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetSecurityOptions(self, arg0=defaultUnnamedArg):
		"""options related to security settings"""
		return self._oleobj_.InvokeTypes(1346843704, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetThumbnailOptions(self, arg0=defaultUnnamedArg):
		"""options related to thumbnail settings"""
		return self._oleobj_.InvokeTypes(1346843702, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AddSizeAttributes": (1346843699, 2, (11, 0), (), "AddSizeAttributes", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'BannerOptions' returns object of type '_GalleryBannerOptions'
		"BannerOptions": (1346843956, 2, (9, 0), (), "BannerOptions", '{5F168D2A-F9EA-4866-8C55-4875E0940622}'),
		# Method 'CustomColorOptions' returns object of type '_GalleryCustomColorOptions'
		"CustomColorOptions": (1346843703, 2, (9, 0), (), "CustomColorOptions", '{2EB2592D-F02D-4117-A22C-26E5CDFAEEE2}'),
		"EmailAddress": (1346843449, 2, (8, 0), (), "EmailAddress", None),
		# Method 'ImagesOptions' returns object of type '_GalleryImagesOptions'
		"ImagesOptions": (1346843701, 2, (9, 0), (), "ImagesOptions", '{46AB9A1D-1B32-4C59-8142-B223ECCF1F74}'),
		"IncludeSubFolders": (1346843698, 2, (11, 0), (), "IncludeSubFolders", None),
		"LayoutStyle": (1346843448, 2, (8, 0), (), "LayoutStyle", None),
		"PreserveAllMetadata": (1346843955, 2, (11, 0), (), "PreserveAllMetadata", None),
		# Method 'SecurityOptions' returns object of type '_GallerySecurityOptions'
		"SecurityOptions": (1346843704, 2, (9, 0), (), "SecurityOptions", '{95D69B63-B319-44D3-8307-C988E96E7E58}'),
		# Method 'ThumbnailOptions' returns object of type '_GalleryThumbnailOptions'
		"ThumbnailOptions": (1346843702, 2, (9, 0), (), "ThumbnailOptions", '{46DFAF34-75E0-470E-8217-B0C763137DD0}'),
		"UseShortExtension": (1346843696, 2, (11, 0), (), "UseShortExtension", None),
		"UseUTF8Encoding": (1346843697, 2, (11, 0), (), "UseUTF8Encoding", None),
	}
	_prop_map_put_ = {
		"AddSizeAttributes": ((1346843699, LCID, 4, 0),()),
		"BannerOptions": ((1346843956, LCID, 4, 0),()),
		"CustomColorOptions": ((1346843703, LCID, 4, 0),()),
		"EmailAddress": ((1346843449, LCID, 4, 0),()),
		"ImagesOptions": ((1346843701, LCID, 4, 0),()),
		"IncludeSubFolders": ((1346843698, LCID, 4, 0),()),
		"LayoutStyle": ((1346843448, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PreserveAllMetadata": ((1346843955, LCID, 4, 0),()),
		"SecurityOptions": ((1346843704, LCID, 4, 0),()),
		"ThumbnailOptions": ((1346843702, LCID, 4, 0),()),
		"UseShortExtension": ((1346843696, LCID, 4, 0),()),
		"UseUTF8Encoding": ((1346843697, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GallerySecurityOptions(DispatchBaseClass):
	"""options for the web photo gallery security"""
	CLSID = IID('{95D69B63-B319-44D3-8307-C988E96E7E58}')
	coclass_clsid = IID('{6A0F1370-78FB-4FBC-B66B-D6A96C9FE7DF}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetTextColor(self, arg0=defaultUnnamedArg):
		"""web page security text color"""
		return self._oleobj_.InvokeTypes(1346844722, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Content": (1346844726, 2, (3, 0), (), "Content", None),
		"Font": (1665560180, 2, (3, 0), (), "Font", None),
		"FontSize": (1346844468, 2, (3, 0), (), "FontSize", None),
		"Opacity": (1332765556, 2, (3, 0), (), "Opacity", None),
		"Text": (1346844727, 2, (8, 0), (), "Text", None),
		# Method 'TextColor' returns object of type '_RGBColor'
		"TextColor": (1346844722, 2, (9, 0), (), "TextColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		"TextPosition": (1346844979, 2, (3, 0), (), "TextPosition", None),
		"TextRotate": (1346844980, 2, (3, 0), (), "TextRotate", None),
	}
	_prop_map_put_ = {
		"Content": ((1346844726, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"FontSize": ((1346844468, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Opacity": ((1332765556, LCID, 4, 0),()),
		"Text": ((1346844727, LCID, 4, 0),()),
		"TextColor": ((1346844722, LCID, 4, 0),()),
		"TextPosition": ((1346844979, LCID, 4, 0),()),
		"TextRotate": ((1346844980, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GalleryThumbnailOptions(DispatchBaseClass):
	"""options for the web photo gallery thumbnail creation"""
	CLSID = IID('{46DFAF34-75E0-470E-8217-B0C763137DD0}')
	coclass_clsid = IID('{DFF332ED-0C72-416B-B128-5CC5BD888865}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Border": (1346844208, 2, (3, 0), (), "Border", None),
		"Caption": (1147744305, 2, (11, 0), (), "Caption", None),
		"ColumnCount": (1346844471, 2, (3, 0), (), "ColumnCount", None),
		"Dimension": (1346843959, 2, (3, 0), (), "Dimension", None),
		"Font": (1665560180, 2, (3, 0), (), "Font", None),
		"FontSize": (1346844468, 2, (3, 0), (), "FontSize", None),
		"IncludeCopyright": (1346844213, 2, (11, 0), (), "IncludeCopyright", None),
		"IncludeCredits": (1346844211, 2, (11, 0), (), "IncludeCredits", None),
		"IncludeFilename": (1346844209, 2, (11, 0), (), "IncludeFilename", None),
		"IncludeTitle": (1346844212, 2, (11, 0), (), "IncludeTitle", None),
		"RowCount": (1346844472, 2, (3, 0), (), "RowCount", None),
		"Size": (1886679930, 2, (3, 0), (), "Size", None),
	}
	_prop_map_put_ = {
		"Border": ((1346844208, LCID, 4, 0),()),
		"Caption": ((1147744305, LCID, 4, 0),()),
		"ColumnCount": ((1346844471, LCID, 4, 0),()),
		"Dimension": ((1346843959, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"FontSize": ((1346844468, LCID, 4, 0),()),
		"IncludeCopyright": ((1346844213, LCID, 4, 0),()),
		"IncludeCredits": ((1346844211, LCID, 4, 0),()),
		"IncludeFilename": ((1346844209, LCID, 4, 0),()),
		"IncludeTitle": ((1346844212, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RowCount": ((1346844472, LCID, 4, 0),()),
		"Size": ((1886679930, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _GrayColor(DispatchBaseClass):
	"""A gray color specification"""
	CLSID = IID('{1B28B8CD-7578-415F-AC67-DC22A69F4C07}')
	coclass_clsid = IID('{F6AEF75A-66C3-49BF-92C9-4232320A2E47}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Gray": (1883730550, 2, (5, 0), (), "Gray", None),
	}
	_prop_map_put_ = {
		"Gray": ((1883730550, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _HSBColor(DispatchBaseClass):
	"""An HSB color specification"""
	CLSID = IID('{F91F9C5B-AC34-45B7-AFF2-871D9DD2E8EC}')
	coclass_clsid = IID('{F3831A80-1C6F-4AFF-B19A-13B32DAE9A28}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Brightness": (1114141806, 2, (5, 0), (), "Brightness", None),
		"Hue": (1883796837, 2, (5, 0), (), "Hue", None),
		"Saturation": (1884512628, 2, (5, 0), (), "Saturation", None),
	}
	_prop_map_put_ = {
		"Brightness": ((1114141806, LCID, 4, 0),()),
		"Hue": ((1883796837, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Saturation": ((1884512628, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _IndexedConversionOptions(DispatchBaseClass):
	"""Settings related to changing the document mode to Indexed"""
	CLSID = IID('{22D0B851-E811-40E2-9A79-E84EA602C9F1}')
	coclass_clsid = IID('{4F2F6ABF-E0AC-4377-8474-B60FCB8E7530}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Colors": (1884308302, 2, (3, 0), (), "Colors", None),
		"Dither": (1148474480, 2, (3, 0), (), "Dither", None),
		"DitherAmount": (1148469613, 2, (3, 0), (), "DitherAmount", None),
		"Forced": (1346790252, 2, (3, 0), (), "Forced", None),
		"Matte": (1299477605, 2, (3, 0), (), "Matte", None),
		"Palette": (1347447924, 2, (3, 0), (), "Palette", None),
		"PreserveExactColors": (1146119544, 2, (11, 0), (), "PreserveExactColors", None),
		"Transparency": (1416786019, 2, (11, 0), (), "Transparency", None),
	}
	_prop_map_put_ = {
		"Colors": ((1884308302, LCID, 4, 0),()),
		"Dither": ((1148474480, LCID, 4, 0),()),
		"DitherAmount": ((1148469613, LCID, 4, 0),()),
		"Forced": ((1346790252, LCID, 4, 0),()),
		"Matte": ((1299477605, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Palette": ((1347447924, LCID, 4, 0),()),
		"PreserveExactColors": ((1146119544, LCID, 4, 0),()),
		"Transparency": ((1416786019, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _JPEGSaveOptions(DispatchBaseClass):
	"""Settings related to saving a JPEG document"""
	CLSID = IID('{5148663B-F632-4AB0-9484-2DBC197CEA82}')
	coclass_clsid = IID('{D9BD1073-009B-48F0-9F6A-5A5FDAF64ABA}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"FormatOptions": (1246777200, 2, (3, 0), (), "FormatOptions", None),
		"Matte": (1299477605, 2, (3, 0), (), "Matte", None),
		"Quality": (1366062201, 2, (3, 0), (), "Quality", None),
		"Scans": (1399025267, 2, (3, 0), (), "Scans", None),
	}
	_prop_map_put_ = {
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"FormatOptions": ((1246777200, LCID, 4, 0),()),
		"Matte": ((1299477605, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Quality": ((1366062201, LCID, 4, 0),()),
		"Scans": ((1399025267, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _LabColor(DispatchBaseClass):
	"""An Lab color specification"""
	CLSID = IID('{F4D7F5C2-37DB-4DF7-8A7D-528902056596}')
	coclass_clsid = IID('{F01D4F29-35D6-47B5-9E29-74F033BB70D7}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"A": (1884054113, 2, (5, 0), (), "A", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"B": (1884054114, 2, (5, 0), (), "B", None),
		"L": (1884054092, 2, (5, 0), (), "L", None),
	}
	_prop_map_put_ = {
		"A": ((1884054113, LCID, 4, 0),()),
		"B": ((1884054114, LCID, 4, 0),()),
		"L": ((1884054092, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _LensBlurOptions(DispatchBaseClass):
	"""options for the lens blur filter"""
	CLSID = IID('{97488031-36F2-4E4B-BA38-64C01754BA64}')
	coclass_clsid = IID('{BDAAC887-CC96-406C-A0B4-32D453DF078A}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"Amount": (1097690740, 2, (3, 0), (), "Amount", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"BladeCurvature": (1279406387, 2, (3, 0), (), "BladeCurvature", None),
		"Brightness": (1114141806, 2, (3, 0), (), "Brightness", None),
		"Distribution": (1148417138, 2, (3, 0), (), "Distribution", None),
		"FocalDistance": (1279406385, 2, (3, 0), (), "FocalDistance", None),
		"InvertDepthMap": (1279406389, 2, (11, 0), (), "InvertDepthMap", None),
		"Monochromatic": (1296263282, 2, (11, 0), (), "Monochromatic", None),
		"Radius": (1382114409, 2, (3, 0), (), "Radius", None),
		"Rotation": (1279406388, 2, (3, 0), (), "Rotation", None),
		"Shape": (1279406390, 2, (3, 0), (), "Shape", None),
		"Source": (1147744562, 2, (3, 0), (), "Source", None),
		"Threshold": (1416129636, 2, (3, 0), (), "Threshold", None),
	}
	_prop_map_put_ = {
		"Amount": ((1097690740, LCID, 4, 0),()),
		"BladeCurvature": ((1279406387, LCID, 4, 0),()),
		"Brightness": ((1114141806, LCID, 4, 0),()),
		"Distribution": ((1148417138, LCID, 4, 0),()),
		"FocalDistance": ((1279406385, LCID, 4, 0),()),
		"InvertDepthMap": ((1279406389, LCID, 4, 0),()),
		"Monochromatic": ((1296263282, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Radius": ((1382114409, LCID, 4, 0),()),
		"Rotation": ((1279406388, LCID, 4, 0),()),
		"Shape": ((1279406390, LCID, 4, 0),()),
		"Source": ((1147744562, LCID, 4, 0),()),
		"Threshold": ((1416129636, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _NoColor(DispatchBaseClass):
	"""represents a missing color"""
	CLSID = IID('{750824C6-C347-4CDB-AA96-8ABA1EBDF9EA}')
	coclass_clsid = IID('{43E87BEF-112A-477C-A4E8-813081732C86}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PDFOpenOptions(DispatchBaseClass):
	"""Settings related to opening a generic PDF document"""
	CLSID = IID('{50D0174F-484D-4A2B-8BF0-A21B84167D82}')
	coclass_clsid = IID('{5FB84343-D1DB-42FA-B5FC-52032CC459C5}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AntiAlias": (1097744748, 2, (11, 0), (), "AntiAlias", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"BitsPerChannel": (1145201512, 2, (3, 0), (), "BitsPerChannel", None),
		"ConstrainProportions": (1129345616, 2, (11, 0), (), "ConstrainProportions", None),
		"CropPage": (1668445295, 2, (3, 0), (), "CropPage", None),
		"Height": (1214736500, 2, (5, 0), (), "Height", None),
		"Mode": (1330472037, 2, (3, 0), (), "Mode", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Page": (1884317518, 2, (3, 0), (), "Page", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"SuppressWarnings": (1936750450, 2, (11, 0), (), "SuppressWarnings", None),
		"UsePageNumber": (1884639335, 2, (11, 0), (), "UsePageNumber", None),
		"Width": (1466201192, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"AntiAlias": ((1097744748, LCID, 4, 0),()),
		"BitsPerChannel": ((1145201512, LCID, 4, 0),()),
		"ConstrainProportions": ((1129345616, LCID, 4, 0),()),
		"CropPage": ((1668445295, LCID, 4, 0),()),
		"Height": ((1214736500, LCID, 4, 0),()),
		"Mode": ((1330472037, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Page": ((1884317518, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
		"SuppressWarnings": ((1936750450, LCID, 4, 0),()),
		"UsePageNumber": ((1884639335, LCID, 4, 0),()),
		"Width": ((1466201192, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PDFSaveOptions(DispatchBaseClass):
	"""Settings related to saving a pdf document"""
	CLSID = IID('{F867E6C9-B5DB-4C5A-B3BA-63224D08A01B}')
	coclass_clsid = IID('{77BA575E-46FB-4D84-9CB2-968FCE815B62}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		"Annotations": (1884504430, 2, (11, 0), (), "Annotations", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"ColorConversion": (1346646832, 2, (11, 0), (), "ColorConversion", None),
		"ConvertToEightBit": (1346646577, 2, (11, 0), (), "ConvertToEightBit", None),
		"Description": (1346646583, 2, (8, 0), (), "Description", None),
		"DestinationProfile": (1346646578, 2, (8, 0), (), "DestinationProfile", None),
		"DownSample": (1346646325, 2, (3, 0), (), "DownSample", None),
		"DownSampleSize": (1346646584, 2, (5, 0), (), "DownSampleSize", None),
		"DownSampleSizeLimit": (1346646585, 2, (5, 0), (), "DownSampleSizeLimit", None),
		"DowngradeColorProfile": (1883531088, 2, (11, 0), (), "DowngradeColorProfile", None),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"EmbedFonts": (1164789364, 2, (11, 0), (), "EmbedFonts", None),
		"EmbedThumbnail": (1346646324, 2, (11, 0), (), "EmbedThumbnail", None),
		"Encoding": (1164854116, 2, (3, 0), (), "Encoding", None),
		"Interpolation": (1231898960, 2, (11, 0), (), "Interpolation", None),
		"JPEGQuality": (1347055719, 2, (3, 0), (), "JPEGQuality", None),
		"Layers": (1884507250, 2, (11, 0), (), "Layers", None),
		"OptimizeForWeb": (1346646582, 2, (11, 0), (), "OptimizeForWeb", None),
		"OutputCondition": (1346646579, 2, (8, 0), (), "OutputCondition", None),
		"OutputConditionID": (1346646580, 2, (8, 0), (), "OutputConditionID", None),
		"PDFCompatibility": (1346646071, 2, (3, 0), (), "PDFCompatibility", None),
		"PDFStandard": (1346646070, 2, (3, 0), (), "PDFStandard", None),
		"PreserveEditing": (1346646323, 2, (11, 0), (), "PreserveEditing", None),
		"PresetFile": (1885759852, 2, (8, 0), (), "PresetFile", None),
		"ProfileInclusionPolicy": (1346646833, 2, (11, 0), (), "ProfileInclusionPolicy", None),
		"RegistryName": (1346646581, 2, (8, 0), (), "RegistryName", None),
		"SpotColors": (1884509043, 2, (11, 0), (), "SpotColors", None),
		"TileSize": (1346646576, 2, (3, 0), (), "TileSize", None),
		"Transparency": (1416786019, 2, (11, 0), (), "Transparency", None),
		"UseOutlines": (1417170796, 2, (11, 0), (), "UseOutlines", None),
		"VectorData": (1449346164, 2, (11, 0), (), "VectorData", None),
		"View": (1346651702, 2, (11, 0), (), "View", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"Annotations": ((1884504430, LCID, 4, 0),()),
		"ColorConversion": ((1346646832, LCID, 4, 0),()),
		"ConvertToEightBit": ((1346646577, LCID, 4, 0),()),
		"Description": ((1346646583, LCID, 4, 0),()),
		"DestinationProfile": ((1346646578, LCID, 4, 0),()),
		"DownSample": ((1346646325, LCID, 4, 0),()),
		"DownSampleSize": ((1346646584, LCID, 4, 0),()),
		"DownSampleSizeLimit": ((1346646585, LCID, 4, 0),()),
		"DowngradeColorProfile": ((1883531088, LCID, 4, 0),()),
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"EmbedFonts": ((1164789364, LCID, 4, 0),()),
		"EmbedThumbnail": ((1346646324, LCID, 4, 0),()),
		"Encoding": ((1164854116, LCID, 4, 0),()),
		"Interpolation": ((1231898960, LCID, 4, 0),()),
		"JPEGQuality": ((1347055719, LCID, 4, 0),()),
		"Layers": ((1884507250, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"OptimizeForWeb": ((1346646582, LCID, 4, 0),()),
		"OutputCondition": ((1346646579, LCID, 4, 0),()),
		"OutputConditionID": ((1346646580, LCID, 4, 0),()),
		"PDFCompatibility": ((1346646071, LCID, 4, 0),()),
		"PDFStandard": ((1346646070, LCID, 4, 0),()),
		"PreserveEditing": ((1346646323, LCID, 4, 0),()),
		"PresetFile": ((1885759852, LCID, 4, 0),()),
		"ProfileInclusionPolicy": ((1346646833, LCID, 4, 0),()),
		"RegistryName": ((1346646581, LCID, 4, 0),()),
		"SpotColors": ((1884509043, LCID, 4, 0),()),
		"TileSize": ((1346646576, LCID, 4, 0),()),
		"Transparency": ((1416786019, LCID, 4, 0),()),
		"UseOutlines": ((1417170796, LCID, 4, 0),()),
		"VectorData": ((1449346164, LCID, 4, 0),()),
		"View": ((1346651702, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PICTFileSaveOptions(DispatchBaseClass):
	"""Settings related to saving a PICT document"""
	CLSID = IID('{D334A509-00F8-4092-A9AF-6E1176D06536}')
	coclass_clsid = IID('{C815086C-036F-4F99-84E0-B2FB14F0180E}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Compression": (1883467120, 2, (3, 0), (), "Compression", None),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"Resolution": (1382380364, 2, (3, 0), (), "Resolution", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"Compression": ((1883467120, LCID, 4, 0),()),
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PNGSaveOptions(DispatchBaseClass):
	"""Settings related to saving a PNG document"""
	CLSID = IID('{478BF855-E42A-4D63-8C9D-F562DE5FF7A8}')
	coclass_clsid = IID('{CAC33536-A1F7-4CD3-8E5A-443F4829A2E3}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Interlaced": (1383550834, 2, (11, 0), (), "Interlaced", None),
	}
	_prop_map_put_ = {
		"Interlaced": ((1383550834, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PathPointInfo(DispatchBaseClass):
	"""Path point information (returned by entire path dataClassProperty of path item class)"""
	CLSID = IID('{B3C35001-B625-48D7-9D3B-C9D66D9CF5F1}')
	coclass_clsid = IID('{0E2AE636-F285-4493-B504-EA9B96D00C8E}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"Anchor": (1347694904, 2, (12, 0), (), "Anchor", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Kind": (1265200740, 2, (3, 0), (), "Kind", None),
		"LeftDirection": (1347694905, 2, (12, 0), (), "LeftDirection", None),
		"RightDirection": (1347695152, 2, (12, 0), (), "RightDirection", None),
	}
	_prop_map_put_ = {
		"Anchor": ((1347694904, LCID, 4, 0),()),
		"Kind": ((1265200740, LCID, 4, 0),()),
		"LeftDirection": ((1347694905, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RightDirection": ((1347695152, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PhotoCDOpenOptions(DispatchBaseClass):
	"""Settings related to opening a PhotoCD document"""
	CLSID = IID('{68F15227-7568-47E1-A4F8-5615C24BDD28}')
	coclass_clsid = IID('{A55A5C39-4885-445E-A33F-C4376B87A8FF}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"ColorProfileName": (1147367502, 2, (8, 0), (), "ColorProfileName", None),
		"ColorSpace": (1131172720, 2, (3, 0), (), "ColorSpace", None),
		"Orientation": (1148154473, 2, (3, 0), (), "Orientation", None),
		"PixelSize": (1350069338, 2, (3, 0), (), "PixelSize", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
	}
	_prop_map_put_ = {
		"ColorProfileName": ((1147367502, LCID, 4, 0),()),
		"ColorSpace": ((1131172720, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Orientation": ((1148154473, LCID, 4, 0),()),
		"PixelSize": ((1350069338, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PhotoshopSaveOptions(DispatchBaseClass):
	"""Settings related to saving a Photoshop document"""
	CLSID = IID('{436CE722-7369-4395-ACC2-2DE7A09269DF}')
	coclass_clsid = IID('{6814BC96-ED0E-4794-90C8-C50B4C3B25EE}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		"Annotations": (1884504430, 2, (11, 0), (), "Annotations", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"Layers": (1884507250, 2, (11, 0), (), "Layers", None),
		"SpotColors": (1884509043, 2, (11, 0), (), "SpotColors", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"Annotations": ((1884504430, LCID, 4, 0),()),
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"Layers": ((1884507250, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SpotColors": ((1884509043, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PicturePackageOptions(DispatchBaseClass):
	"""options for the Picture Package command"""
	CLSID = IID('{ABD0F9CE-822B-4BB1-A811-3EC852B43C0F}')
	coclass_clsid = IID('{8F1E9C09-D03F-4E28-B16C-FBED7540FB92}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetTextColor(self, arg0=defaultUnnamedArg):
		"""text color"""
		return self._oleobj_.InvokeTypes(1346844722, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Content": (1346844726, 2, (3, 0), (), "Content", None),
		"Flatten": (1129525300, 2, (11, 0), (), "Flatten", None),
		"Font": (1665560180, 2, (3, 0), (), "Font", None),
		"FontSize": (1346844468, 2, (3, 0), (), "FontSize", None),
		"Layout": (1347432752, 2, (8, 0), (), "Layout", None),
		"Mode": (1330472037, 2, (3, 0), (), "Mode", None),
		"Opacity": (1332765556, 2, (3, 0), (), "Opacity", None),
		"Resolution": (1382380364, 2, (5, 0), (), "Resolution", None),
		"Text": (1346844727, 2, (8, 0), (), "Text", None),
		# Method 'TextColor' returns object of type '_RGBColor'
		"TextColor": (1346844722, 2, (9, 0), (), "TextColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		"TextPosition": (1346844979, 2, (3, 0), (), "TextPosition", None),
		"TextRotate": (1346844980, 2, (3, 0), (), "TextRotate", None),
	}
	_prop_map_put_ = {
		"Content": ((1346844726, LCID, 4, 0),()),
		"Flatten": ((1129525300, LCID, 4, 0),()),
		"Font": ((1665560180, LCID, 4, 0),()),
		"FontSize": ((1346844468, LCID, 4, 0),()),
		"Layout": ((1347432752, LCID, 4, 0),()),
		"Mode": ((1330472037, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Opacity": ((1332765556, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
		"Text": ((1346844727, LCID, 4, 0),()),
		"TextColor": ((1346844722, LCID, 4, 0),()),
		"TextPosition": ((1346844979, LCID, 4, 0),()),
		"TextRotate": ((1346844980, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PixarSaveOptions(DispatchBaseClass):
	"""Settings related to saving a Pixar document"""
	CLSID = IID('{94C016CD-178F-4FD7-85BB-F5925A34A122}')
	coclass_clsid = IID('{4EFD5560-B2A7-43E3-A763-86BFA256C871}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _PresentationOptions(DispatchBaseClass):
	"""options for the PDF presentation command"""
	CLSID = IID('{376C4F3B-0345-440B-90D9-FE78AECA249C}')
	coclass_clsid = IID('{3A3A8228-FBB4-414D-816B-38B5ADFE07C5}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetPDFFileOptions(self, arg0=defaultUnnamedArg):
		"""Options used when creating the PDF file"""
		return self._oleobj_.InvokeTypes(1346651764, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"AutoAdvance": (1346651703, 2, (11, 0), (), "AutoAdvance", None),
		"IncludeFilename": (1346844209, 2, (11, 0), (), "IncludeFilename", None),
		"Interval": (1346651704, 2, (3, 0), (), "Interval", None),
		"Loop": (1346651705, 2, (11, 0), (), "Loop", None),
		"Magnification": (1346651765, 2, (3, 0), (), "Magnification", None),
		# Method 'PDFFileOptions' returns object of type '_PDFSaveOptions'
		"PDFFileOptions": (1346651764, 2, (9, 0), (), "PDFFileOptions", '{F867E6C9-B5DB-4C5A-B3BA-63224D08A01B}'),
		"Presentation": (1346651701, 2, (11, 0), (), "Presentation", None),
		"Transition": (1346651745, 2, (3, 0), (), "Transition", None),
	}
	_prop_map_put_ = {
		"AutoAdvance": ((1346651703, LCID, 4, 0),()),
		"IncludeFilename": ((1346844209, LCID, 4, 0),()),
		"Interval": ((1346651704, LCID, 4, 0),()),
		"Loop": ((1346651705, LCID, 4, 0),()),
		"Magnification": ((1346651765, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PDFFileOptions": ((1346651764, LCID, 4, 0),()),
		"Presentation": ((1346651701, LCID, 4, 0),()),
		"Transition": ((1346651745, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _RGBColor(DispatchBaseClass):
	"""An RGB color specification"""
	CLSID = IID('{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}')
	coclass_clsid = IID('{878C878F-617C-46B9-84A7-0FA356D48EFE}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Blue": (1884439158, 2, (5, 0), (), "Blue", None),
		"Green": (1884440438, 2, (5, 0), (), "Green", None),
		"HexValue": (1884440696, 2, (8, 0), (), "HexValue", None),
		"Red": (1884443254, 2, (5, 0), (), "Red", None),
	}
	_prop_map_put_ = {
		"Blue": ((1884439158, LCID, 4, 0),()),
		"Green": ((1884440438, LCID, 4, 0),()),
		"HexValue": ((1884440696, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Red": ((1884443254, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _RawFormatOpenOptions(DispatchBaseClass):
	"""Settings related to opening a raw format document"""
	CLSID = IID('{6B785D83-5B5F-4402-A712-BAEBD8C5B812}')
	coclass_clsid = IID('{D0D08DD0-C5F8-4DC7-8D53-51310430C423}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"BitsPerChannel": (1145201512, 2, (3, 0), (), "BitsPerChannel", None),
		"ByteOrder": (1415987823, 2, (3, 0), (), "ByteOrder", None),
		"ChannelNumber": (1130909293, 2, (3, 0), (), "ChannelNumber", None),
		"HeaderSize": (1214534522, 2, (3, 0), (), "HeaderSize", None),
		"Height": (1214736500, 2, (3, 0), (), "Height", None),
		"InterleaveChannels": (1666147442, 2, (11, 0), (), "InterleaveChannels", None),
		"RetainHeader": (1383352420, 2, (11, 0), (), "RetainHeader", None),
		"Width": (1466201192, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"BitsPerChannel": ((1145201512, LCID, 4, 0),()),
		"ByteOrder": ((1415987823, LCID, 4, 0),()),
		"ChannelNumber": ((1130909293, LCID, 4, 0),()),
		"HeaderSize": ((1214534522, LCID, 4, 0),()),
		"Height": ((1214736500, LCID, 4, 0),()),
		"InterleaveChannels": ((1666147442, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RetainHeader": ((1383352420, LCID, 4, 0),()),
		"Width": ((1466201192, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _RawSaveOptions(DispatchBaseClass):
	"""Settings related to saving a document in raw format"""
	CLSID = IID('{D74B820F-AA86-42DD-8D85-F4D67A62F200}')
	coclass_clsid = IID('{0BA89C9F-38BD-4061-A23E-43C69E472BAE}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"SpotColors": (1884509043, 2, (11, 0), (), "SpotColors", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SpotColors": ((1884509043, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _SGIRGBSaveOptions(DispatchBaseClass):
	"""Settings related to saving a document in the SGI RGB format"""
	CLSID = IID('{01CD87DE-1F53-485D-A096-0D318611AB6D}')
	coclass_clsid = IID('{76DE9D01-4D38-4CB8-9C34-5A5E2142C8E2}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"SpotColors": (1884509043, 2, (11, 0), (), "SpotColors", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SpotColors": ((1884509043, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _SolidColor(DispatchBaseClass):
	"""A color value"""
	CLSID = IID('{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}')
	coclass_clsid = IID('{6946B6E1-F949-455F-97D6-9EA68BDA11C4}')

	def IsEqual(self, Color=defaultNamedNotOptArg):
		"""return true if the provided color is visually equal to this color"""
		return self._oleobj_.InvokeTypes(1129406828, LCID, 1, (11, 0), ((9, 1),),Color)

	def SetCMYK(self, arg0=defaultUnnamedArg):
		"""return a grayscale representation of the color"""
		return self._oleobj_.InvokeTypes(1665355126, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetGray(self, arg0=defaultUnnamedArg):
		"""return a grayscale representation of the color"""
		return self._oleobj_.InvokeTypes(1665626742, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetHSB(self, arg0=defaultUnnamedArg):
		"""return a grayscale representation of the color"""
		return self._oleobj_.InvokeTypes(1665679990, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetLab(self, arg0=defaultUnnamedArg):
		"""return a grayscale representation of the color"""
		return self._oleobj_.InvokeTypes(1665950326, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	def SetRGB(self, arg0=defaultUnnamedArg):
		"""return an rgb representation of the color"""
		return self._oleobj_.InvokeTypes(1666336630, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		# Method 'CMYK' returns object of type '_CMYKColor'
		"CMYK": (1665355126, 2, (9, 0), (), "CMYK", '{29C13F49-BCEF-4FE2-BFC7-6F03B82B726F}'),
		# Method 'Gray' returns object of type '_GrayColor'
		"Gray": (1665626742, 2, (9, 0), (), "Gray", '{1B28B8CD-7578-415F-AC67-DC22A69F4C07}'),
		# Method 'HSB' returns object of type '_HSBColor'
		"HSB": (1665679990, 2, (9, 0), (), "HSB", '{F91F9C5B-AC34-45B7-AFF2-871D9DD2E8EC}'),
		# Method 'Lab' returns object of type '_LabColor'
		"Lab": (1665950326, 2, (9, 0), (), "Lab", '{F4D7F5C2-37DB-4DF7-8A7D-528902056596}'),
		"Model": (1883458916, 2, (3, 0), (), "Model", None),
		# Method 'NearestWebColor' returns object of type '_RGBColor'
		"NearestWebColor": (1466057580, 2, (9, 0), (), "NearestWebColor", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
		# Method 'RGB' returns object of type '_RGBColor'
		"RGB": (1666336630, 2, (9, 0), (), "RGB", '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}'),
	}
	_prop_map_put_ = {
		"CMYK": ((1665355126, LCID, 4, 0),()),
		"Gray": ((1665626742, LCID, 4, 0),()),
		"HSB": ((1665679990, LCID, 4, 0),()),
		"Lab": ((1665950326, LCID, 4, 0),()),
		"Model": ((1883458916, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RGB": ((1666336630, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _SubPathInfo(DispatchBaseClass):
	"""Sub path information (returned by entire path dataClassProperty of path item class)"""
	CLSID = IID('{7E8F9046-9F8E-4594-A22C-9F6B4C227CD7}')
	coclass_clsid = IID('{92A24D3F-8A3F-4825-AF4F-5D429A975FFD}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"Closed": (1347695920, 2, (11, 0), (), "Closed", None),
		"EntireSubPath": (1347695926, 2, (12, 0), (), "EntireSubPath", None),
		"Operation": (1347694647, 2, (3, 0), (), "Operation", None),
	}
	_prop_map_put_ = {
		"Closed": ((1347695920, LCID, 4, 0),()),
		"EntireSubPath": ((1347695926, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Operation": ((1347694647, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _TargaSaveOptions(DispatchBaseClass):
	"""Settings related to saving a Target document"""
	CLSID = IID('{F4E21694-AEBF-44FB-90AB-EECD58C1B6F3}')
	coclass_clsid = IID('{AB314690-6BDD-438D-B7D7-C6AFC643BEE2}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"RLECompression": (1884441669, 2, (11, 0), (), "RLECompression", None),
		"Resolution": (1382380364, 2, (3, 0), (), "Resolution", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RLECompression": ((1884441669, LCID, 4, 0),()),
		"Resolution": ((1382380364, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

class _TiffSaveOptions(DispatchBaseClass):
	"""Settings related to saving a TIFF document"""
	CLSID = IID('{372B4D75-EB10-4D0A-8203-5778D521253D}')
	coclass_clsid = IID('{E9D36B87-BD83-4920-AA8B-66ACB95EE19A}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	_prop_map_get_ = {
		"AlphaChannels": (1884504419, 2, (11, 0), (), "AlphaChannels", None),
		"Annotations": (1884504430, 2, (11, 0), (), "Annotations", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}'),
		"ByteOrder": (1415987823, 2, (3, 0), (), "ByteOrder", None),
		"EmbedColorProfile": (1884505424, 2, (11, 0), (), "EmbedColorProfile", None),
		"ImageCompression": (1231897456, 2, (3, 0), (), "ImageCompression", None),
		"InterleaveChannels": (1666147442, 2, (11, 0), (), "InterleaveChannels", None),
		"JPEGQuality": (1347055719, 2, (3, 0), (), "JPEGQuality", None),
		"LayerCompression": (1283015536, 2, (3, 0), (), "LayerCompression", None),
		"Layers": (1884507250, 2, (11, 0), (), "Layers", None),
		"SaveImagePyramid": (1884313970, 2, (11, 0), (), "SaveImagePyramid", None),
		"SpotColors": (1884509043, 2, (11, 0), (), "SpotColors", None),
		"Transparency": (1416786019, 2, (11, 0), (), "Transparency", None),
	}
	_prop_map_put_ = {
		"AlphaChannels": ((1884504419, LCID, 4, 0),()),
		"Annotations": ((1884504430, LCID, 4, 0),()),
		"ByteOrder": ((1415987823, LCID, 4, 0),()),
		"EmbedColorProfile": ((1884505424, LCID, 4, 0),()),
		"ImageCompression": ((1231897456, LCID, 4, 0),()),
		"InterleaveChannels": ((1666147442, LCID, 4, 0),()),
		"JPEGQuality": ((1347055719, LCID, 4, 0),()),
		"LayerCompression": ((1283015536, LCID, 4, 0),()),
		"Layers": ((1884507250, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SaveImagePyramid": ((1884313970, LCID, 4, 0),()),
		"SpotColors": ((1884509043, LCID, 4, 0),()),
		"Transparency": ((1416786019, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0)

	# str(ob) and int(ob) will use __call__
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Photoshop.ActionDescriptor.9'
class ActionDescriptor(CoClassBaseClass): # A CoClass
	CLSID = IID('{817C4CED-C2E7-4CE6-839B-812940E412B4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ActionDescriptor,
	]
	default_interface = _ActionDescriptor

# This CoClass is known by the name 'Photoshop.ActionList.9'
class ActionList(CoClassBaseClass): # A CoClass
	CLSID = IID('{E56C890E-2974-463F-8D39-CEDEA8BED418}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ActionList,
	]
	default_interface = _ActionList

# This CoClass is known by the name 'Photoshop.ActionReference.9'
class ActionReference(CoClassBaseClass): # A CoClass
	CLSID = IID('{A7C190CF-534E-4D85-A844-726762F0FAFC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ActionReference,
	]
	default_interface = _ActionReference

# This CoClass is known by the name 'Photoshop.Application.9'
class Application(CoClassBaseClass): # A CoClass
	# The Adobe Photoshop application
	CLSID = IID('{16AA0B9E-79AC-43B5-86CA-AB961FBEED5F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Application,
	]
	default_interface = _Application

# This CoClass is known by the name 'Photoshop.BMPSaveOptions.9'
class BMPSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a BMP document
	CLSID = IID('{EBDBA1ED-D57D-4CCD-BD9E-CB60E5E6CB07}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_BMPSaveOptions,
	]
	default_interface = _BMPSaveOptions

# This CoClass is known by the name 'Photoshop.BatchOptions.9'
class BatchOptions(CoClassBaseClass): # A CoClass
	# options for the Batch command
	CLSID = IID('{6EF2BC9F-827B-455B-89C9-5AB3AA233790}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_BatchOptions,
	]
	default_interface = _BatchOptions

# This CoClass is known by the name 'Photoshop.BitmapConversionOptions.9'
class BitmapConversionOptions(CoClassBaseClass): # A CoClass
	# Settings related to changing the document mode to Bitmap
	CLSID = IID('{B861C213-1A7F-4FE3-A19B-3927EBEA7BD8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_BitmapConversionOptions,
	]
	default_interface = _BitmapConversionOptions

# This CoClass is known by the name 'Photoshop.CMYKColor.9'
class CMYKColor(CoClassBaseClass): # A CoClass
	# A CMYK color specification
	CLSID = IID('{41EBBED9-0E3C-45B8-8C78-7B07FAF46AD2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_CMYKColor,
	]
	default_interface = _CMYKColor

# This CoClass is known by the name 'Photoshop.CameraRAWOpenOptions.9'
class CameraRAWOpenOptions(CoClassBaseClass): # A CoClass
	# Settings related to opening a camera RAW document
	CLSID = IID('{A35CD676-3F1A-405B-B97B-6FB59011E7E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_CameraRAWOpenOptions,
	]
	default_interface = _CameraRAWOpenOptions

# This CoClass is known by the name 'Photoshop.ContactSheetOptions.9'
class ContactSheetOptions(CoClassBaseClass): # A CoClass
	# options for the Contact Sheet command
	CLSID = IID('{D765F6C2-748B-476B-8884-E5118E646179}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ContactSheetOptions,
	]
	default_interface = _ContactSheetOptions

# This CoClass is known by the name 'Photoshop.DCS1_SaveOptions.9'
class DCS1_SaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a Photoshop DCS 1.0 document
	CLSID = IID('{B1C1FEB9-C46D-4959-9B92-A962FA41C511}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_DCS1_SaveOptions,
	]
	default_interface = _DCS1_SaveOptions

# This CoClass is known by the name 'Photoshop.DCS2_SaveOptions.9'
class DCS2_SaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a Photoshop DCS 2.0 document
	CLSID = IID('{61DA6070-5785-4C7F-9785-C7036D01B1BE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_DCS2_SaveOptions,
	]
	default_interface = _DCS2_SaveOptions

# This CoClass is known by the name 'Photoshop.EPSOpenOptions.9'
class EPSOpenOptions(CoClassBaseClass): # A CoClass
	# Settings related to opening a generic EPS document
	CLSID = IID('{7468F85C-D655-4331-890E-4086C70CF67A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_EPSOpenOptions,
	]
	default_interface = _EPSOpenOptions

# This CoClass is known by the name 'Photoshop.EPSSaveOptions.9'
class EPSSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving an EPS document
	CLSID = IID('{074B66CB-4BEF-4A83-A699-77F33D3CD5E0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_EPSSaveOptions,
	]
	default_interface = _EPSSaveOptions

# This CoClass is known by the name 'Photoshop.ExportOptionsIllustrator.9'
class ExportOptionsIllustrator(CoClassBaseClass): # A CoClass
	# Settings related to exporting Illustrator paths
	CLSID = IID('{CACEC2F5-EC15-4DFD-8955-244D2A7EFE60}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsIllustrator,
	]
	default_interface = _ExportOptionsIllustrator

# This CoClass is known by the name 'Photoshop.ExportOptionsSaveForWeb.9'
class ExportOptionsSaveForWeb(CoClassBaseClass): # A CoClass
	# Settings related to exporting Save For Web files
	CLSID = IID('{D434C3C7-5BCA-4856-8A21-AF46C2147FD0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsSaveForWeb,
	]
	default_interface = _ExportOptionsSaveForWeb

# This CoClass is known by the name 'Photoshop.GIFSaveOptions.9'
class GIFSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a GIF document
	CLSID = IID('{22F619C0-72B1-46FC-B04B-DC364CD0C33E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GIFSaveOptions,
	]
	default_interface = _GIFSaveOptions

# This CoClass is known by the name 'Photoshop.GalleryBannerOptions.9'
class GalleryBannerOptions(CoClassBaseClass): # A CoClass
	# options for the web photo gallery banner options
	CLSID = IID('{D5D9C71A-56DC-459D-A433-9B8C334165A5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GalleryBannerOptions,
	]
	default_interface = _GalleryBannerOptions

# This CoClass is known by the name 'Photoshop.GalleryCustomColorOptions.9'
class GalleryCustomColorOptions(CoClassBaseClass): # A CoClass
	# options for the web photo gallery colors
	CLSID = IID('{6F3B0065-21DB-44A6-BF09-624D88ECF768}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GalleryCustomColorOptions,
	]
	default_interface = _GalleryCustomColorOptions

# This CoClass is known by the name 'Photoshop.GalleryImagesOptions.9'
class GalleryImagesOptions(CoClassBaseClass): # A CoClass
	# options for the web photo gallery images
	CLSID = IID('{26BB16C1-67D1-44A7-AA75-DD2F361352E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GalleryImagesOptions,
	]
	default_interface = _GalleryImagesOptions

# This CoClass is known by the name 'Photoshop.GalleryOptions.9'
class GalleryOptions(CoClassBaseClass): # A CoClass
	# options for the web photo gallery command
	CLSID = IID('{B10D4055-8C78-4C7F-BAE7-5B5FFDED928A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GalleryOptions,
	]
	default_interface = _GalleryOptions

# This CoClass is known by the name 'Photoshop.GallerySecurityOptions.9'
class GallerySecurityOptions(CoClassBaseClass): # A CoClass
	# options for the web photo gallery security
	CLSID = IID('{6A0F1370-78FB-4FBC-B66B-D6A96C9FE7DF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GallerySecurityOptions,
	]
	default_interface = _GallerySecurityOptions

# This CoClass is known by the name 'Photoshop.GalleryThumbnailOptions.9'
class GalleryThumbnailOptions(CoClassBaseClass): # A CoClass
	# options for the web photo gallery thumbnail creation
	CLSID = IID('{DFF332ED-0C72-416B-B128-5CC5BD888865}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GalleryThumbnailOptions,
	]
	default_interface = _GalleryThumbnailOptions

# This CoClass is known by the name 'Photoshop.GrayColor.9'
class GrayColor(CoClassBaseClass): # A CoClass
	# A gray color specification
	CLSID = IID('{F6AEF75A-66C3-49BF-92C9-4232320A2E47}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GrayColor,
	]
	default_interface = _GrayColor

# This CoClass is known by the name 'Photoshop.HSBColor.9'
class HSBColor(CoClassBaseClass): # A CoClass
	# An HSB color specification
	CLSID = IID('{F3831A80-1C6F-4AFF-B19A-13B32DAE9A28}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_HSBColor,
	]
	default_interface = _HSBColor

# This CoClass is known by the name 'Photoshop.IndexedConversionOptions.9'
class IndexedConversionOptions(CoClassBaseClass): # A CoClass
	# Settings related to changing the document mode to Indexed
	CLSID = IID('{4F2F6ABF-E0AC-4377-8474-B60FCB8E7530}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_IndexedConversionOptions,
	]
	default_interface = _IndexedConversionOptions

# This CoClass is known by the name 'Photoshop.JPEGSaveOptions.9'
class JPEGSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a JPEG document
	CLSID = IID('{D9BD1073-009B-48F0-9F6A-5A5FDAF64ABA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_JPEGSaveOptions,
	]
	default_interface = _JPEGSaveOptions

# This CoClass is known by the name 'Photoshop.LabColor.9'
class LabColor(CoClassBaseClass): # A CoClass
	# An Lab color specification
	CLSID = IID('{F01D4F29-35D6-47B5-9E29-74F033BB70D7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_LabColor,
	]
	default_interface = _LabColor

# This CoClass is known by the name 'Photoshop.LensBlurOptions.9'
class LensBlurOptions(CoClassBaseClass): # A CoClass
	# options for the lens blur filter
	CLSID = IID('{BDAAC887-CC96-406C-A0B4-32D453DF078A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_LensBlurOptions,
	]
	default_interface = _LensBlurOptions

# This CoClass is known by the name 'Photoshop.NoColor.9'
class NoColor(CoClassBaseClass): # A CoClass
	# represents a missing color
	CLSID = IID('{43E87BEF-112A-477C-A4E8-813081732C86}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_NoColor,
	]
	default_interface = _NoColor

# This CoClass is known by the name 'Photoshop.PDFOpenOptions.9'
class PDFOpenOptions(CoClassBaseClass): # A CoClass
	# Settings related to opening a generic PDF document
	CLSID = IID('{5FB84343-D1DB-42FA-B5FC-52032CC459C5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PDFOpenOptions,
	]
	default_interface = _PDFOpenOptions

# This CoClass is known by the name 'Photoshop.PDFSaveOptions.9'
class PDFSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a pdf document
	CLSID = IID('{77BA575E-46FB-4D84-9CB2-968FCE815B62}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PDFSaveOptions,
	]
	default_interface = _PDFSaveOptions

# This CoClass is known by the name 'Photoshop.PICTFileSaveOptions.9'
class PICTFileSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a PICT document
	CLSID = IID('{C815086C-036F-4F99-84E0-B2FB14F0180E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PICTFileSaveOptions,
	]
	default_interface = _PICTFileSaveOptions

# This CoClass is known by the name 'Photoshop.PNGSaveOptions.9'
class PNGSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a PNG document
	CLSID = IID('{CAC33536-A1F7-4CD3-8E5A-443F4829A2E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PNGSaveOptions,
	]
	default_interface = _PNGSaveOptions

# This CoClass is known by the name 'Photoshop.PathPointInfo.9'
class PathPointInfo(CoClassBaseClass): # A CoClass
	# Path point information (returned by entire path dataClassProperty of path item class)
	CLSID = IID('{0E2AE636-F285-4493-B504-EA9B96D00C8E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PathPointInfo,
	]
	default_interface = _PathPointInfo

# This CoClass is known by the name 'Photoshop.PhotoCDOpenOptions.9'
class PhotoCDOpenOptions(CoClassBaseClass): # A CoClass
	# Settings related to opening a PhotoCD document
	CLSID = IID('{A55A5C39-4885-445E-A33F-C4376B87A8FF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PhotoCDOpenOptions,
	]
	default_interface = _PhotoCDOpenOptions

# This CoClass is known by the name 'Photoshop.PhotoshopSaveOptions.9'
class PhotoshopSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a Photoshop document
	CLSID = IID('{6814BC96-ED0E-4794-90C8-C50B4C3B25EE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PhotoshopSaveOptions,
	]
	default_interface = _PhotoshopSaveOptions

# This CoClass is known by the name 'Photoshop.PicturePackageOptions.9'
class PicturePackageOptions(CoClassBaseClass): # A CoClass
	# options for the Picture Package command
	CLSID = IID('{8F1E9C09-D03F-4E28-B16C-FBED7540FB92}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PicturePackageOptions,
	]
	default_interface = _PicturePackageOptions

# This CoClass is known by the name 'Photoshop.PixarSaveOptions.9'
class PixarSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a Pixar document
	CLSID = IID('{4EFD5560-B2A7-43E3-A763-86BFA256C871}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PixarSaveOptions,
	]
	default_interface = _PixarSaveOptions

# This CoClass is known by the name 'Photoshop.PresentationOptions.9'
class PresentationOptions(CoClassBaseClass): # A CoClass
	# options for the PDF presentation command
	CLSID = IID('{3A3A8228-FBB4-414D-816B-38B5ADFE07C5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PresentationOptions,
	]
	default_interface = _PresentationOptions

# This CoClass is known by the name 'Photoshop.RGBColor.9'
class RGBColor(CoClassBaseClass): # A CoClass
	# An RGB color specification
	CLSID = IID('{878C878F-617C-46B9-84A7-0FA356D48EFE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_RGBColor,
	]
	default_interface = _RGBColor

# This CoClass is known by the name 'Photoshop.RawFormatOpenOptions.9'
class RawFormatOpenOptions(CoClassBaseClass): # A CoClass
	# Settings related to opening a raw format document
	CLSID = IID('{D0D08DD0-C5F8-4DC7-8D53-51310430C423}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_RawFormatOpenOptions,
	]
	default_interface = _RawFormatOpenOptions

# This CoClass is known by the name 'Photoshop.RawSaveOptions.9'
class RawSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a document in raw format
	CLSID = IID('{0BA89C9F-38BD-4061-A23E-43C69E472BAE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_RawSaveOptions,
	]
	default_interface = _RawSaveOptions

# This CoClass is known by the name 'Photoshop.SGIRGBSaveOptions.9'
class SGIRGBSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a document in the SGI RGB format
	CLSID = IID('{76DE9D01-4D38-4CB8-9C34-5A5E2142C8E2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_SGIRGBSaveOptions,
	]
	default_interface = _SGIRGBSaveOptions

# This CoClass is known by the name 'Photoshop.SolidColor.9'
class SolidColor(CoClassBaseClass): # A CoClass
	# A color value
	CLSID = IID('{6946B6E1-F949-455F-97D6-9EA68BDA11C4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_SolidColor,
	]
	default_interface = _SolidColor

# This CoClass is known by the name 'Photoshop.SubPathInfo.9'
class SubPathInfo(CoClassBaseClass): # A CoClass
	# Sub path information (returned by entire path dataClassProperty of path item class)
	CLSID = IID('{92A24D3F-8A3F-4825-AF4F-5D429A975FFD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_SubPathInfo,
	]
	default_interface = _SubPathInfo

# This CoClass is known by the name 'Photoshop.TargaSaveOptions.9'
class TargaSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a Target document
	CLSID = IID('{AB314690-6BDD-438D-B7D7-C6AFC643BEE2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_TargaSaveOptions,
	]
	default_interface = _TargaSaveOptions

# This CoClass is known by the name 'Photoshop.TiffSaveOptions.9'
class TiffSaveOptions(CoClassBaseClass): # A CoClass
	# Settings related to saving a TIFF document
	CLSID = IID('{E9D36B87-BD83-4920-AA8B-66ACB95EE19A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_TiffSaveOptions,
	]
	default_interface = _TiffSaveOptions

RecordMap = {
}

CLSIDToClassMap = {
	'{7468F85C-D655-4331-890E-4086C70CF67A}' : EPSOpenOptions,
	'{0E2AE636-F285-4493-B504-EA9B96D00C8E}' : PathPointInfo,
	'{3A3A8228-FBB4-414D-816B-38B5ADFE07C5}' : PresentationOptions,
	'{7D14BA29-1672-482F-8F48-9DA1E94800FD}' : PathPoint,
	'{9A37A0AC-E951-4B16-A548-886B77338DE0}' : LayerComp,
	'{B6D22EB9-EC6D-46DB-B52A-5561433A1217}' : SubPathItem,
	'{D334A509-00F8-4092-A9AF-6E1176D06536}' : _PICTFileSaveOptions,
	'{F4D7F5C2-37DB-4DF7-8A7D-528902056596}' : _LabColor,
	'{726B458C-74B0-47AE-B390-99753B55DF2E}' : LayerComps,
	'{B3C35001-B625-48D7-9D3B-C9D66D9CF5F1}' : _PathPointInfo,
	'{B7283EEC-23B1-49A6-B151-0E97E4AF353C}' : SubPathItems,
	'{817C4CED-C2E7-4CE6-839B-812940E412B4}' : ActionDescriptor,
	'{F4E21694-AEBF-44FB-90AB-EECD58C1B6F3}' : _TargaSaveOptions,
	'{6EF2BC9F-827B-455B-89C9-5AB3AA233790}' : BatchOptions,
	'{4EFD5560-B2A7-43E3-A763-86BFA256C871}' : PixarSaveOptions,
	'{8B0CB532-4ACC-4BF3-9E42-0949B679D120}' : PathItem,
	'{861C9290-2A0C-4614-8606-706B31BFD45B}' : Notifiers,
	'{D765F6C2-748B-476B-8884-E5118E646179}' : ContactSheetOptions,
	'{22F619C0-72B1-46FC-B04B-DC364CD0C33E}' : GIFSaveOptions,
	'{746FEF90-A182-4BD0-A4F6-BB6BBAE87A78}' : DocumentInfo,
	'{C815086C-036F-4F99-84E0-B2FB14F0180E}' : PICTFileSaveOptions,
	'{DC865034-A587-4CC4-8A5A-453032562BE4}' : XMPMetadata,
	'{B10D4055-8C78-4C7F-BAE7-5B5FFDED928A}' : GalleryOptions,
	'{EC6A366C-F901-488D-A2C3-9E2E78B72DC6}' : ArtLayers,
	'{643099A1-0B67-4920-9B14-E14BE8F63D5F}' : _BitmapConversionOptions,
	'{FC08B435-5F19-49DF-ABE7-ADCE9F0729FF}' : _ExportOptionsIllustrator,
	'{41EBBED9-0E3C-45B8-8C78-7B07FAF46AD2}' : CMYKColor,
	'{D74B820F-AA86-42DD-8D85-F4D67A62F200}' : _RawSaveOptions,
	'{074B66CB-4BEF-4A83-A699-77F33D3CD5E0}' : EPSSaveOptions,
	'{22D0B851-E811-40E2-9A79-E84EA602C9F1}' : _IndexedConversionOptions,
	'{2DC64F97-8C69-4016-A8EB-89A00217291F}' : Channels,
	'{50D0174F-484D-4A2B-8BF0-A21B84167D82}' : _PDFOpenOptions,
	'{323DD2BC-0205-4A44-9F8E-0CF2556F00DF}' : LayerSets,
	'{436CE722-7369-4395-ACC2-2DE7A09269DF}' : _PhotoshopSaveOptions,
	'{E56C890E-2974-463F-8D39-CEDEA8BED418}' : ActionList,
	'{4F2F6ABF-E0AC-4377-8474-B60FCB8E7530}' : IndexedConversionOptions,
	'{4D40BE2D-FE11-4060-B52A-DE31C837D51D}' : _BMPSaveOptions,
	'{CACEC2F5-EC15-4DFD-8955-244D2A7EFE60}' : ExportOptionsIllustrator,
	'{376C4F3B-0345-440B-90D9-FE78AECA249C}' : _PresentationOptions,
	'{7E8F9046-9F8E-4594-A22C-9F6B4C227CD7}' : _SubPathInfo,
	'{77BA575E-46FB-4D84-9CB2-968FCE815B62}' : PDFSaveOptions,
	'{92A24D3F-8A3F-4825-AF4F-5D429A975FFD}' : SubPathInfo,
	'{2EB2592D-F02D-4117-A22C-26E5CDFAEEE2}' : _GalleryCustomColorOptions,
	'{D5D9C71A-56DC-459D-A433-9B8C334165A5}' : GalleryBannerOptions,
	'{DFF332ED-0C72-416B-B128-5CC5BD888865}' : GalleryThumbnailOptions,
	'{69172A3F-E06E-42E6-B733-4DC36E2AC948}' : HistoryStates,
	'{A35CD676-3F1A-405B-B97B-6FB59011E7E3}' : CameraRAWOpenOptions,
	'{E7A940CD-9AC7-4D76-975D-24D6BA0FDD16}' : TextItem,
	'{95D69B63-B319-44D3-8307-C988E96E7E58}' : _GallerySecurityOptions,
	'{76DE9D01-4D38-4CB8-9C34-5A5E2142C8E2}' : SGIRGBSaveOptions,
	'{61DA6070-5785-4C7F-9785-C7036D01B1BE}' : DCS2_SaveOptions,
	'{750824C6-C347-4CDB-AA96-8ABA1EBDF9EA}' : _NoColor,
	'{6814BC96-ED0E-4794-90C8-C50B4C3B25EE}' : PhotoshopSaveOptions,
	'{CAC33536-A1F7-4CD3-8E5A-443F4829A2E3}' : PNGSaveOptions,
	'{B0D18870-EAC3-4D35-8612-6F734B3FA656}' : _BatchOptions,
	'{F715C957-54CE-4E55-9856-591D4CD082FD}' : _EPSOpenOptions,
	'{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}' : _SolidColor,
	'{EBDBA1ED-D57D-4CCD-BD9E-CB60E5E6CB07}' : BMPSaveOptions,
	'{BDAAC887-CC96-406C-A0B4-32D453DF078A}' : LensBlurOptions,
	'{F1AF982E-2BBD-406D-9FD6-CA6C898A7FFE}' : _DCS2_SaveOptions,
	'{C88838E3-5A82-4EE7-A66C-E0360C9B0356}' : TextFont,
	'{DDA16C46-15B2-472D-A659-41AA7BFDC4FD}' : Layers,
	'{5148663B-F632-4AB0-9484-2DBC197CEA82}' : _JPEGSaveOptions,
	'{B861C213-1A7F-4FE3-A19B-3927EBEA7BD8}' : BitmapConversionOptions,
	'{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}' : ArtLayer,
	'{A7C190CF-534E-4D85-A844-726762F0FAFC}' : ActionReference,
	'{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}' : _RGBColor,
	'{D9BD1073-009B-48F0-9F6A-5A5FDAF64ABA}' : JPEGSaveOptions,
	'{BBCE52D6-5D4B-4691-99E3-62C174BD2855}' : TextFonts,
	'{91B5F8AE-3CC5-4775-BCD3-FF1E0724BB01}' : PathItems,
	'{43E87BEF-112A-477C-A4E8-813081732C86}' : NoColor,
	'{94C4A25A-2C91-4514-A783-3173AFC48430}' : _DCS1_SaveOptions,
	'{C1C35524-2AA4-4630-80B9-011EFE3D5779}' : LayerSet,
	'{662506C7-6AAE-4422-ACA4-C63627CB1868}' : Documents,
	'{6946B6E1-F949-455F-97D6-9EA68BDA11C4}' : SolidColor,
	'{8214A53C-0E67-49D4-A65A-D56F07B17D37}' : PathPoints,
	'{70A60330-E866-46AA-A715-ABF418C41453}' : _ActionDescriptor,
	'{01CD87DE-1F53-485D-A096-0D318611AB6D}' : _SGIRGBSaveOptions,
	'{D0D08DD0-C5F8-4DC7-8D53-51310430C423}' : RawFormatOpenOptions,
	'{878C878F-617C-46B9-84A7-0FA356D48EFE}' : RGBColor,
	'{EDC373C3-FE30-40BA-A31C-0251CA7456F1}' : HistoryState,
	'{6B785D83-5B5F-4402-A712-BAEBD8C5B812}' : _RawFormatOpenOptions,
	'{94C016CD-178F-4FD7-85BB-F5925A34A122}' : _PixarSaveOptions,
	'{E9D36B87-BD83-4920-AA8B-66ACB95EE19A}' : TiffSaveOptions,
	'{8F1E9C09-D03F-4E28-B16C-FBED7540FB92}' : PicturePackageOptions,
	'{26BB16C1-67D1-44A7-AA75-DD2F361352E3}' : GalleryImagesOptions,
	'{09DA6B10-9684-44EE-A575-01F54660BDDC}' : Selection,
	'{5F168D2A-F9EA-4866-8C55-4875E0940622}' : _GalleryBannerOptions,
	'{D54491EF-6F09-4DE3-B49A-D57EDB2F40B8}' : _EPSSaveOptions,
	'{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}' : Notifier,
	'{6A0F1370-78FB-4FBC-B66B-D6A96C9FE7DF}' : GallerySecurityOptions,
	'{1B28B8CD-7578-415F-AC67-DC22A69F4C07}' : _GrayColor,
	'{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}' : _ActionReference,
	'{0BA89C9F-38BD-4061-A23E-43C69E472BAE}' : RawSaveOptions,
	'{F867E6C9-B5DB-4C5A-B3BA-63224D08A01B}' : _PDFSaveOptions,
	'{064BBE94-396D-4B25-9071-AC5B14D0487F}' : _ContactSheetOptions,
	'{29C13F49-BCEF-4FE2-BFC7-6F03B82B726F}' : _CMYKColor,
	'{55031766-E456-4E54-A0D0-8E545601A2D8}' : _ActionList,
	'{4B9E6B85-0613-4873-8AB7-575CD2226768}' : Channel,
	'{B1C1FEB9-C46D-4959-9B92-A962FA41C511}' : DCS1_SaveOptions,
	'{46AB9A1D-1B32-4C59-8142-B223ECCF1F74}' : _GalleryImagesOptions,
	'{B1ADEFB6-C536-42D6-8A83-397354A769F8}' : Document,
	'{A55A5C39-4885-445E-A33F-C4376B87A8FF}' : PhotoCDOpenOptions,
	'{F3831A80-1C6F-4AFF-B19A-13B32DAE9A28}' : HSBColor,
	'{F01D4F29-35D6-47B5-9E29-74F033BB70D7}' : LabColor,
	'{6F3B0065-21DB-44A6-BF09-624D88ECF768}' : GalleryCustomColorOptions,
	'{89417281-E1AF-4800-B82A-9F37ED0478EF}' : _GIFSaveOptions,
	'{C2783141-B50D-4F0C-9E2E-BF76EA8A4E60}' : _GalleryOptions,
	'{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}' : _Application,
	'{F91F9C5B-AC34-45B7-AFF2-871D9DD2E8EC}' : _HSBColor,
	'{372B4D75-EB10-4D0A-8203-5778D521253D}' : _TiffSaveOptions,
	'{D434C3C7-5BCA-4856-8A21-AF46C2147FD0}' : ExportOptionsSaveForWeb,
	'{288BC58E-AB6A-467C-B244-D225349E3EB3}' : Preferences,
	'{91A3D47B-9579-4013-9206-7B6859439DA2}' : _ExportOptionsSaveForWeb,
	'{F6AEF75A-66C3-49BF-92C9-4232320A2E47}' : GrayColor,
	'{478BF855-E42A-4D63-8C9D-F562DE5FF7A8}' : _PNGSaveOptions,
	'{AB314690-6BDD-438D-B7D7-C6AFC643BEE2}' : TargaSaveOptions,
	'{16AA0B9E-79AC-43B5-86CA-AB961FBEED5F}' : Application,
	'{ABD0F9CE-822B-4BB1-A811-3EC852B43C0F}' : _PicturePackageOptions,
	'{97488031-36F2-4E4B-BA38-64C01754BA64}' : _LensBlurOptions,
	'{68F15227-7568-47E1-A4F8-5615C24BDD28}' : _PhotoCDOpenOptions,
	'{46DFAF34-75E0-470E-8217-B0C763137DD0}' : _GalleryThumbnailOptions,
	'{65D1B010-0D87-481C-B2E6-22EFB5A54129}' : _CameraRAWOpenOptions,
	'{5FB84343-D1DB-42FA-B5FC-52032CC459C5}' : PDFOpenOptions,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'Layers' : '{DDA16C46-15B2-472D-A659-41AA7BFDC4FD}',
	'_PhotoshopSaveOptions' : '{436CE722-7369-4395-ACC2-2DE7A09269DF}',
	'TextFont' : '{C88838E3-5A82-4EE7-A66C-E0360C9B0356}',
	'HistoryStates' : '{69172A3F-E06E-42E6-B733-4DC36E2AC948}',
	'SubPathItem' : '{B6D22EB9-EC6D-46DB-B52A-5561433A1217}',
	'_SubPathInfo' : '{7E8F9046-9F8E-4594-A22C-9F6B4C227CD7}',
	'_PresentationOptions' : '{376C4F3B-0345-440B-90D9-FE78AECA249C}',
	'PathItem' : '{8B0CB532-4ACC-4BF3-9E42-0949B679D120}',
	'_GalleryBannerOptions' : '{5F168D2A-F9EA-4866-8C55-4875E0940622}',
	'_CameraRAWOpenOptions' : '{65D1B010-0D87-481C-B2E6-22EFB5A54129}',
	'_ActionReference' : '{DFF407C7-3BCC-45AC-B6CC-EE6D52032D85}',
	'_GrayColor' : '{1B28B8CD-7578-415F-AC67-DC22A69F4C07}',
	'TextItem' : '{E7A940CD-9AC7-4D76-975D-24D6BA0FDD16}',
	'_PixarSaveOptions' : '{94C016CD-178F-4FD7-85BB-F5925A34A122}',
	'XMPMetadata' : '{DC865034-A587-4CC4-8A5A-453032562BE4}',
	'_PDFSaveOptions' : '{F867E6C9-B5DB-4C5A-B3BA-63224D08A01B}',
	'PathPoints' : '{8214A53C-0E67-49D4-A65A-D56F07B17D37}',
	'_GIFSaveOptions' : '{89417281-E1AF-4800-B82A-9F37ED0478EF}',
	'_LabColor' : '{F4D7F5C2-37DB-4DF7-8A7D-528902056596}',
	'Document' : '{B1ADEFB6-C536-42D6-8A83-397354A769F8}',
	'_CMYKColor' : '{29C13F49-BCEF-4FE2-BFC7-6F03B82B726F}',
	'Channel' : '{4B9E6B85-0613-4873-8AB7-575CD2226768}',
	'_PICTFileSaveOptions' : '{D334A509-00F8-4092-A9AF-6E1176D06536}',
	'_BMPSaveOptions' : '{4D40BE2D-FE11-4060-B52A-DE31C837D51D}',
	'LayerComp' : '{9A37A0AC-E951-4B16-A548-886B77338DE0}',
	'_GalleryOptions' : '{C2783141-B50D-4F0C-9E2E-BF76EA8A4E60}',
	'_SolidColor' : '{D2D1665E-C1B9-4CA0-8AC9-529F6A3D9002}',
	'_GalleryThumbnailOptions' : '{46DFAF34-75E0-470E-8217-B0C763137DD0}',
	'_BatchOptions' : '{B0D18870-EAC3-4D35-8612-6F734B3FA656}',
	'_BitmapConversionOptions' : '{643099A1-0B67-4920-9B14-E14BE8F63D5F}',
	'_PNGSaveOptions' : '{478BF855-E42A-4D63-8C9D-F562DE5FF7A8}',
	'HistoryState' : '{EDC373C3-FE30-40BA-A31C-0251CA7456F1}',
	'_ActionList' : '{55031766-E456-4E54-A0D0-8E545601A2D8}',
	'DocumentInfo' : '{746FEF90-A182-4BD0-A4F6-BB6BBAE87A78}',
	'_RawSaveOptions' : '{D74B820F-AA86-42DD-8D85-F4D67A62F200}',
	'ArtLayers' : '{EC6A366C-F901-488D-A2C3-9E2E78B72DC6}',
	'_IndexedConversionOptions' : '{22D0B851-E811-40E2-9A79-E84EA602C9F1}',
	'_NoColor' : '{750824C6-C347-4CDB-AA96-8ABA1EBDF9EA}',
	'_ContactSheetOptions' : '{064BBE94-396D-4B25-9071-AC5B14D0487F}',
	'_TargaSaveOptions' : '{F4E21694-AEBF-44FB-90AB-EECD58C1B6F3}',
	'_EPSSaveOptions' : '{D54491EF-6F09-4DE3-B49A-D57EDB2F40B8}',
	'_TiffSaveOptions' : '{372B4D75-EB10-4D0A-8203-5778D521253D}',
	'ArtLayer' : '{16BE80A3-57B1-4871-83AC-7F844EEEB1CA}',
	'_PDFOpenOptions' : '{50D0174F-484D-4A2B-8BF0-A21B84167D82}',
	'Preferences' : '{288BC58E-AB6A-467C-B244-D225349E3EB3}',
	'_RGBColor' : '{45F1195F-3554-4B3F-A00A-E1D189C0DC3E}',
	'_SGIRGBSaveOptions' : '{01CD87DE-1F53-485D-A096-0D318611AB6D}',
	'_ActionDescriptor' : '{70A60330-E866-46AA-A715-ABF418C41453}',
	'Documents' : '{662506C7-6AAE-4422-ACA4-C63627CB1868}',
	'SubPathItems' : '{B7283EEC-23B1-49A6-B151-0E97E4AF353C}',
	'_GalleryCustomColorOptions' : '{2EB2592D-F02D-4117-A22C-26E5CDFAEEE2}',
	'_DCS2_SaveOptions' : '{F1AF982E-2BBD-406D-9FD6-CA6C898A7FFE}',
	'_PathPointInfo' : '{B3C35001-B625-48D7-9D3B-C9D66D9CF5F1}',
	'_DCS1_SaveOptions' : '{94C4A25A-2C91-4514-A783-3173AFC48430}',
	'Notifier' : '{8B4F1F1E-4ED7-4291-AE61-76ADF4D1D50B}',
	'_PicturePackageOptions' : '{ABD0F9CE-822B-4BB1-A811-3EC852B43C0F}',
	'_EPSOpenOptions' : '{F715C957-54CE-4E55-9856-591D4CD082FD}',
	'_GalleryImagesOptions' : '{46AB9A1D-1B32-4C59-8142-B223ECCF1F74}',
	'_LensBlurOptions' : '{97488031-36F2-4E4B-BA38-64C01754BA64}',
	'Selection' : '{09DA6B10-9684-44EE-A575-01F54660BDDC}',
	'TextFonts' : '{BBCE52D6-5D4B-4691-99E3-62C174BD2855}',
	'_JPEGSaveOptions' : '{5148663B-F632-4AB0-9484-2DBC197CEA82}',
	'LayerSets' : '{323DD2BC-0205-4A44-9F8E-0CF2556F00DF}',
	'PathPoint' : '{7D14BA29-1672-482F-8F48-9DA1E94800FD}',
	'_RawFormatOpenOptions' : '{6B785D83-5B5F-4402-A712-BAEBD8C5B812}',
	'_HSBColor' : '{F91F9C5B-AC34-45B7-AFF2-871D9DD2E8EC}',
	'_PhotoCDOpenOptions' : '{68F15227-7568-47E1-A4F8-5615C24BDD28}',
	'Channels' : '{2DC64F97-8C69-4016-A8EB-89A00217291F}',
	'_GallerySecurityOptions' : '{95D69B63-B319-44D3-8307-C988E96E7E58}',
	'LayerComps' : '{726B458C-74B0-47AE-B390-99753B55DF2E}',
	'_Application' : '{5DE90358-4D0B-4FA1-BA3E-C91BBA863F32}',
	'_ExportOptionsSaveForWeb' : '{91A3D47B-9579-4013-9206-7B6859439DA2}',
	'Notifiers' : '{861C9290-2A0C-4614-8606-706B31BFD45B}',
	'LayerSet' : '{C1C35524-2AA4-4630-80B9-011EFE3D5779}',
	'PathItems' : '{91B5F8AE-3CC5-4775-BCD3-FF1E0724BB01}',
	'_ExportOptionsIllustrator' : '{FC08B435-5F19-49DF-ABE7-ADCE9F0729FF}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

