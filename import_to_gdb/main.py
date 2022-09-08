# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env

#in_workspace = u"E:\\merge_by_geom\\ESYE"
in_workspace = u"E:\\merge_by_geom\\test_workspace"

#f = open("E:\\merge_by_geom\\new_merge_shp\\polyline.csv","w")
#env.workspace = u"E:\\merge_by_geom\\ESYE"
env.workspace = u"E:\\merge_by_geom\\test_workspace"
#arcpy.management.CreateFileGDB(env.workspace,"polinegeo","10.0")

#MasterGDB = u"E:\\merge_by_geom\\ESYE\\polinegeo.gdb"
MasterGDB = u"E:\\merge_by_geom\\test_workspace\\polinegeo.gdb"

if (arcpy.Exists(MasterGDB)):
    arcpy.Delete_management(MasterGDB)

#arcpy.management.CreateFileGDB(u"E:\\merge_by_geom\\ESYE","polinegeo","10.0")
arcpy.management.CreateFileGDB(u"E:\\merge_by_geom\\test_workspace","polinegeo","10.0")

#f = open("E:\\merge_by_geom\\ESYE\\polylinegdb.csv","w")
f = open("E:\\merge_by_geom\\test_workspace\\polylinegdb.csv","w")

polygList = []
#polygshapefile = "E:\\merge_by_geom\\new_merge_shp\\Mergedpolygon.shp"
count=0
try:
    for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type = "Polyline"):
        for filename in filenames:
            if (filename.endswith(".shp")):
                count +=1
                f.write(dirpath + '\\' + filename +'\n')
                #print filename         
        
        
        #fields = arcpy.ListFields(dirpath + '\\' + filename,"MUN_CODE")
        #for field in fields:
            #arcpy.AddField_management(dirpath + '\\' + filename, "temp_field", "TEXT")
            #arcpy.CalculateField_management(dirpath + '\\' + filename, "temp_field", "!MUN_CODE!","PYTHON_9.3")
            #arcpy.DeleteField_management(dirpath + '\\' + filename, "MUN_CODE")
            #arcpy.AddField_management(dirpath + '\\' + filename, "MUN_CODE", "TEXT")
            #arcpy.CalculateField_management(dirpath + '\\' + filename, "MUN_CODE", "!temp_field!","PYTHON_9.3")
            #arcpy.DeleteField_management(dirpath + '\\' + filename, "temp_field")
                
                
                #polygList.append(os.path.join(dirpath, filename))
                polygList.append(os.path.join(filename))
                #for p in polygList:  
                arcpy.FeatureClassToGeodatabase_conversion(polygList,MasterGDB)
                #f.write(subfol + '\\' + fc +'\n')
    print "\nNumber of shapefiles is " + str(count)
    print len(polygList)
#print "EDITING FIELDS IS FINISHED!! NOW IS MERGING.."
    #arcpy.Merge_management(polygList,polygshapefile)
    #print "merge:  SUCCESS."
except Exception as err:
    arcpy.AddError(err)
    print "FeatureClassToGeodatabase_conversion:  FAIL."
    print err
#else :
    #print("Compressing FileGDB...")
    #arcpy.CompressFileGeodatabaseData_management(MasterGDB)
    #print(MasterGDB + " has been compressed.")