# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env

# projection = "GCS_GGRS_1987"
# proj = "Greek_Grid"
# proje = "2100"
# arcpy.CreateMosaicDataset_management("E:\\mosaic_test\\geodb\\mosaic_db.gdb","mosaic_dts",proje)

arcpy.env.workspace = u"E:\\mosaic_test"
in_workspace = u"E:\\mosaic_test" 
mdname = u"E:\\mosaic_test\\geodb\\mosaic_db.gdb\\mosaic_dts"
rastype = "Raster Dataset"
# inpath = "c:/data/rasds"
updatecs = "UPDATE_CELL_SIZES"
updatebnd = "UPDATE_BOUNDARY"
updateovr = "UPDATE_OVERVIEWS"
maxlevel = "2"
maxcs = "#"
mindim = "#"
spatialref = "Greek_Grid"
inputdatafilter = "*.tif"
subfolder = "NO_SUBFOLDERS"
duplicate = "EXCLUDE_DUPLICATES"
buildpy = "BUILD_PYRAMIDS"
calcstats = "CALCULATE_STATISTICS"
buildthumb = "NO_THUMBNAILS"
comments = "Add Raster Datasets"
forcesr = "#"

for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="RasterDataset", type="TIF"):
    for filename in filenames:
        arcpy.AddRastersToMosaicDataset_management(mdname,rastype, filename)
#                                                    ,updatecs,updatebnd,maxlevel,maxcs,mindim,spatialref,
#                                                     updateovr,inputdatafilter,subfolder, duplicate,
#                                                     buildpy, calcstats, buildthumb, comments,forcesr)
        