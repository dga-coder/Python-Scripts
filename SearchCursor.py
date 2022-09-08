# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting

poaList = []
in_workspace = u"D:\\POA_vs_CSL\\POA"
arcpy.env.workspace = u"D:\\POA_vs_CSL\\POA"
#rsid="2100"

#sort_fields="POA_TYPE A"
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="ALL"):
    for filename in filenames:
        if (filename.endswith("POA.shp")):
            poaList.append(os.path.join(dirpath, filename))
            for poali in poaList:
                #spatial_ref = arcpy.Describe(poali).spatialReference
                #field = ["POA_TYPE"]
                #sql_clause = '\"POA_TYPE"\ = 1' 
                cursor = arcpy.da.SearchCursor(poali,("POA_TYPE"),"\"POA_TYPE\" = '1`'")
                for cur in cursor:
                    print (dirpath + "\\" + filename +"\n")------HAVE TO FIX IT PRINT ALL AFTER FINDING THE FIRST-------
                
                    #print("{0}".format(cur[0]))


