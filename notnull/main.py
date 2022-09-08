# -*- coding: utf-8 -*-
import arcpy
import csv
from arcpy import env
f = open( u'C:\\tables.csv','w')
#Set workspace
arcpy.env.workspace = u'C:\\Users\\galionis.ELPHODOMAIN\\AppData\\Roaming\\ESRI\\Desktop10.2\\ArcCatalog\\PatraGIS@144.76.39.165.sde'
#Loop through feature classes looking for a field named 'elev'
fcList = arcpy.ListFeatureClasses() #get a list of feature classes
for fc in fcList:  #loop through feature classes
    fieldList = arcpy.ListFields(fc)  #get a list of fields for each feature class
    for field in fieldList: #loop through each field
        if field.name == 'isRelated':  #look for the name isRelated
            if field.isNullable == True:
                print fc
                f.write(fc +'\n')