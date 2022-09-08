# -*- coding: utf-8 -*-
import collections
import os
import sys
import arcpy
#import arcgisscripting
import traceback
import shapefile
from arcpy import env


# Set the workspace  
# Set work environment

in_workspace = u"E:\\merge_by_geom\\ESYE"
#env.workspace = u"E:\\merge_by_geom\\ESYE"
#in_workspace = u"E:\\merge_by_geom\\ESYE\\ΝΟΜΟΣ ΑΤΤΙΚΗΣ_2011\\Afidnai"
#E:\\merge_by_geom\\ESYE\\OIKISMOI_MH_PSIFIOPOIHMENOI_2011\\Ν. ΑΙΤΩΛΙΑΣ & ΑΚΑΡΝΑΝΙΑΣ

polygList = []
polygshapefile = "E:\\merge_by_geom\\dest_new\\Mergedpolyg.shp"
fieldNames = []
seen = set()


for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polyline"):
    for filename in filenames:
        #polygList.append(os.path.join(dirpath, filename))
        #polygshpList = '"'+';'.join(polygList)+'"'
        #for polygs in polygList:
        fields = arcpy.ListFields(dirpath + '\\' + filename,'STREETNAME')
        for field in fields:
            #if field.type == "String":
            print filename + "---" + field.name + "---" + field.type + "---" + str(field.length) 
                    



       


        
#targetList = arcpy.ListFields(polygshapefile)
#targetNames = []
#for  field in targetList:
#    targetNames.append(field.Name)
#    print targetNames



'''
try:
    arcpy.Merge_management(polygList,polygshapefile)
    print "merge:  SUCCESS."
    result1 = int(arcpy.GetCount_management(polygshapefile).getOutput(0)) 
    print result1
except Exception as err:
    arcpy.AddError(err)
    print "merge:  FAIL."
    print err
'''