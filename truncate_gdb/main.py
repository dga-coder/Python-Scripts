# -*- coding: utf-8 -*-
import arcpy

# Set the workspace.
arcpy.env.workspace = u"G:\\dhpe_dgbs\\final_gdb\\test_final.gdb"

fcList = arcpy.ListFeatureClasses()

# Loop through the list and run truncate
for fc in fcList:
    print fc
    arcpy.TruncateTable_management(fc)