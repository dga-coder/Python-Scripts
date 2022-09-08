import arcpy
from arcpy import env

env.workspace = u"E:\\ETAD_RASTERS\\Raster\\KEDRaster500.gdb"

# datasetList = arcpy.ListRasters("*")

datasetList = arcpy.ListDatasets("C*", "Raster ")
for raster in datasetList:
    print(raster)




# for dataset in datasetList:
#     with arcpy.da.SearchCursor(dataset, "*") as cur:
#         for row in cur:
#             print row