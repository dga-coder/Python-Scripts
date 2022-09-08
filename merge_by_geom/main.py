# -*- coding: utf-8 -*-
import collections
import os
import sys
import arcpy
import arcgisscripting
import traceback
from arcpy import env
import shutil
#===============================================================================
# import explode
#===============================================================================


# Set the workspace  
# Set work environment

polygList = []

polygshapefile = "E:\\merge_by_geom\\dest_new\\Mergedpolyline.shp"

#outTable = u"E:\\merge_by_geom\\check_geom\\cgom.gdb\\checkGeometryResult"
#outWorkspace = u"E:\\merge_by_geom\\check_geom\\cgom.gdb"

#env.workspace = u"E:\\merge_by_geom\\ESYE\\OIKISMOI_MH_PSIFIOPOIHMENOI_2011\\Ν. ΑΙΤΩΛΙΑΣ & ΑΚΑΡΝΑΝΙΑΣ\\ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ"

in_workspace = u"E:\\merge_by_geom\\ESYE\\YPOLOIPH_ELLADA_2011\\Ν. ΚΟΡΙΝΘΙΑΣ\\ArxaiaKorinthia"

#env.workspace = (for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polyline"): 
#for filename in filenames: )

#fcList = arcpy.ListFeatureClasses()
#out_data = "E:\\merge_by_geom\\onlypoly" + filename

coun = 0
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polyline"):
    for filename in filenames:
        #print filename.strip(".shp") + "_" + str(coun +1) + ".shp"
        out_data = "E:\\merge_by_geom\\onlypoly\\" + filename.strip(".shp") + "_" + str(coun +1) + ".shp"
        arcpy.Copy_management(filename,out_data)
        
        #fields = arcpy.ListFields(dirpath + '\\' + filename,"MUN_CODE")
        #for field in fields:
            #arcpy.AddField_management(dirpath + '\\' + filename, "temp_field", "TEXT")
            #arcpy.CalculateField_management(dirpath + '\\' + filename, "temp_field", "!MUN_CODE!","PYTHON_9.3")
            #arcpy.DeleteField_management(dirpath + '\\' + filename, "MUN_CODE")
            #arcpy.AddField_management(dirpath + '\\' + filename, "MUN_CODE", "TEXT")
            #arcpy.CalculateField_management(dirpath + '\\' + filename, "MUN_CODE", "!temp_field!","PYTHON_9.3")
            #arcpy.DeleteField_management(dirpath + '\\' + filename, "temp_field")
        #polygList.append(os.path.join(dirpath, filename))         
#print "EDITING FIELDS IS FINISHED!! NOW IS MERGING.."


#arcpy.CreateFileGDB_management("E:\\merge_by_geom\\check_geom", "cgom.gdb")
#polygList  = arcpy.ListFeatureClasses()
#print polygList


#polygList  = arcpy.ListFeatureClasses()

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



#for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polyline"):
    #for filename in filenames:
        #polygList.append(os.path.join(dirpath, filename))
#polygList  = arcpy.ListFeatureClasses()
#print polygList

#env.workspace = u"E:\\merge_by_geom\\ESYE\\OIKISMOI_MH_PSIFIOPOIHMENOI_2011\\Ν. ΑΙΤΩΛΙΑΣ & ΑΚΑΡΝΑΝΙΑΣ\\ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ"

        
        
#print polygList
'''
arcpy.CreateFileGDB_management("E:\\merge_by_geom\\check_geom", "cgom.gdb")
polygList  = arcpy.ListFeatureClasses()
#for sh in polygList:
    #outFeatureClass = os.path.join(outWorkspace, sh.strip(".shp"))
    #arcpy.CopyFeatures_management(sh, outFeatureClass)
arcpy.CheckGeometry_management(polygList, outTable)
print "CHECK GEOMETRY HAS FINISHED!!"
        
        #print outFeatureClass
#print env.workspace
        #arcpy.CopyFeatures_management(filename, outFeatureClass)
'''
    