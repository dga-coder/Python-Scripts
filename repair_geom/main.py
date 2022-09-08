# -*- coding: utf-8 -*-
import arcpy

# Set the workspace.
arcpy.env.workspace = u"G:\\dhpe_dgbs\\final_gdb\\test_final_corrected.gdb"

fcList = arcpy.ListFeatureClasses()

# Loop through the list and run repair
for fc in fcList:
    print fc
    arcpy.RepairGeometry_management(fc)