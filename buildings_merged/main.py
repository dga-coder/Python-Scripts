# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env

in_workspace = u"D:\\map_from_maira_181114\\ELPHO_TEST\\2001_Dataset"
f = open(u"D:\\map_from_maira_181114\\ELPHO_TEST\\2001_Dataset\\build_merg.csv","w")
polygList = []
polygshapefile = u"D:\\map_from_maira_181114\\ELPHO_TEST\\2001_Dataset\\Merged_buildings.shp"
count=0
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polygon"):
    for filename in filenames:
        if (filename.endswith(".shp") and 'build' in filename):
            count +=1
            f.write(dirpath + '\\' + filename +'\n')
#             arcpy.AddField_management(dirpath + '\\' + filename, "REG_DESCR","TEXT")
#             fields = arcpy.ListFields(dirpath + '\\' + filename,"MUN_CODE")
#             for field in fields:
#                 arcpy.AddField_management(dirpath + '\\' + filename, "temp_field", "TEXT")
#                 arcpy.CalculateField_management(dirpath + '\\' + filename, "temp_field", "!MUN_CODE!","PYTHON_9.3")
#                 arcpy.DeleteField_management(dirpath + '\\' + filename, "MUN_CODE")
#                 arcpy.AddField_management(dirpath + '\\' + filename, "MUN_CODE", "TEXT")
#                 arcpy.CalculateField_management(dirpath + '\\' + filename, "MUN_CODE", "!temp_field!","PYTHON_9.3")
#                 arcpy.DeleteField_management(dirpath + '\\' + filename, "temp_field")   
            #polygList.append(os.path.join(dirpath, filename))
            parent_path = os.path.join(dirpath, filename)
            #for poali in polygList:
#             uprows = arcpy.da.UpdateCursor(parent_path,("REG_DESCR"))
#             for uprow in uprows:
#                 uprow[0] = dirpath.rsplit("\\",-1)[-1]
#                 uprows.updateRow(uprow)
#             del uprow, uprows
            polygList.append(parent_path)             
print "\nNumber of shapefiles is " + str(count)
print "EDITING FIELDS IS FINISHED!! NOW IS MERGING.."
try:
    arcpy.Merge_management(polygList,polygshapefile)
    print "merge:  SUCCESS."
except Exception as err:
    arcpy.AddError(err)
    print "merge:  FAIL."
    print err