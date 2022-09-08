import sys
import arcpy, os
from arcpy import env

env.workspace = "E:\\merge_by_geom\\ESYE\\uncomp_repair\\polinegeo.gdb"

#geodatabase = "polinegeo.gdb"
fcs = arcpy.ListFeatureClasses()
outTable = "E:\\merge_by_geom\\ESYE\\uncomp_repair\\polinegeo.gdb\\checkGeometryResult"
if (arcpy.Exists(outTable)):
    arcpy.Delete_management(outTable)
else:
    outTable = "E:\\merge_by_geom\\ESYE\\uncomp_repair\\polinegeo.gdb\\checkGeometryResult" 
try:
    #Process: Compress the data
    #arcpy.UncompressFileGeodatabaseData_management(geodatabase)
    print "Running the check geometry tool on %i feature classes" % len(fcs)
    arcpy.CheckGeometry_management(fcs, outTable)
    print (str(arcpy.GetCount_management(outTable)) + " geometry problems were found.")
    print ("See " + outTable + " for full details")
#     print ("RepairGeometry is starting")
#     for fc in fcs:
#         arcpy.RepairGeometry_management (fc)
#     print ("RepairGeometry has been finished")
except:
    # If an error occurred while running the tool print the messages
    print arcpy.GetMessages()