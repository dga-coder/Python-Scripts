# -*- coding: utf-8 -*-
import collections
import os
import sys
import arcpy
import arcgisscripting
import traceback
import shapefile
from arcpy import env


# Set the workspace  
# Set work environment

in_workspace = u"E:\\merge_by_geom\\ESYE"
#env.workspace = u"E:\\merge_by_geom\\ESYE\\ΝΟΜΟΣ ΑΤΤΙΚΗΣ_2011\\Afidnai"
#in_workspace = u"E:\\merge_by_geom\\ESYE\\ΝΟΜΟΣ ΑΤΤΙΚΗΣ_2011\\Afidnai"
#E:\\merge_by_geom\\teswt_add_length

polygList = []
polygshapefile = "E:\\merge_by_geom\\dest_new\\Mergedpolyg.shp"
#shalist=[]
#tfield_precision = 50
#field_precision = 15

#field_names = []
#shalist = '"'+';'.join(dirpath + '\\' + filename)+'"'
#fcList = arcpy.ListFeatureClasses()
#shalist.append(os.path.join(dirpath, filename))
#print dirpath + '\\' + filename
#print shalist

for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polygon"):
    for filename in filenames:
        fields = arcpy.ListFields(dirpath + '\\' + filename,"MUN_CODE")
        for field in fields:
            arcpy.AddField_management(dirpath + '\\' + filename, "temp_field", "TEXT")
            arcpy.CalculateField_management(dirpath + '\\' + filename, "temp_field", "!MUN_CODE!","PYTHON_9.3")
            arcpy.DeleteField_management(dirpath + '\\' + filename, "MUN_CODE")
            arcpy.AddField_management(dirpath + '\\' + filename, "MUN_CODE", "TEXT")
            arcpy.CalculateField_management(dirpath + '\\' + filename, "MUN_CODE", "!temp_field!","PYTHON_9.3")
            arcpy.DeleteField_management(dirpath + '\\' + filename, "temp_field")
        polygList.append(os.path.join(dirpath, filename))         
print "EDITING FIELDS IS FINISHED!! NOW IS MERGING.."
try:
    arcpy.Merge_management(polygList,polygshapefile)
    print "merge:  SUCCESS."
    result1 = int(arcpy.GetCount_management(polygshapefile).getOutput(0)) 
    print result1
except Exception as err:
    arcpy.AddError(err)
    print "merge:  FAIL."
    print err
        
        
        
        #fields = arcpy.ListFields(dirpath + '\\' + filename,"MUN_CODE")
        #for field in fields:
            #print filename + "-----" + field.name + "------" + field.type
            #if field.type == "String":
            
            
            
            
                
                #print filename + "---" + field.name + "---" + field.type + "---" + str(field.length)
                #shalist = '"'+';'.join(dirpath + '\\' + filename)+'"'
                #shalist.append(os.path.join(dirpath,filename))
                #print shalist      
                #arcpy.AddField_management(dirpath + '\\' + filename, "MUN_CODE_NEW", "String")
                
                #arcpy.AddField_management(filename, "MUN_CODE_NEW", "String")
                #arcpy.CalculateField_management(dirpath +filename, "MUN_CODE_NEW", "str(!MUN_CODE!)")
                #arcpy.DeleteField_management(dirpath + '\\' + filename, "MUN_CODE")
                #arcpy.AlterField_management(filename,"MUN_CODE_NEW","MUN_CODE") 
            #field_names.append(field.name)
            #print field_names                           
                #arcpy.AddField_management(dirpath + '\\' + filename, "MUN_CODE_NEW", "String")        
                #arcpy.CalculateField_management(dirpath + '\\' + filename, "MUN_CODE_NEW", """ str(!MUN_CODE!) """)
                #arcpy.DeleteField_management(dirpath + '\\' + filename, "MUN_CODE)               
#print filename + "-----" + field.name + "------" + field.type
#fields = arcpy.ListFields(dirpath + '\\' + filename,"Double")     
'''
        for field in fields:
            field_names.append(field.type)
        print field_names
        #fcs = arcpy.ListFeatureClasses()
#for fc in fcs:
    #print '\t', fc
'''    

