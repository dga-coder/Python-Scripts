# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting

arcpy.env.workspace = u'D:\\ANTIKEIMENIKES\\gdbs_news\\NEES_EDAXIS_2011_XARTES_DWG_FEK_2038.gdb'

# Get stand alone FCs
fccount = len(arcpy.ListFeatureClasses("",""))

# Get list of Feature Datasets and loop through them
fds = arcpy.ListDatasets("","")
for fd in fds:
    oldws = arcpy.env.workspace
    arcpy.env.workspace = oldws + "\\" + fd
    fccount = fccount + len(arcpy.ListFeatureClasses("",""))
    arcpy.env.workspace = oldws


print fccount
