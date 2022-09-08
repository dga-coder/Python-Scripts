# -*- coding: utf-8 -*-
import os
import csv
import arcpy
 
#t = open( u'D:\\map_from_maira_181114\\ELPHO_TEST\\2011_Dataset\\OT_2.csv','w')
#c = open( u'D:\\map_from_maira_181114\\ELPHO_TEST\\2011_Dataset\\AJONES_polyline.csv','w')
f = open( u'D:\\map_from_maira_181114\\ELPHO_TEST\\2011_Dataset\\AJONES_all_NEW.csv','w')
in_workspace = u"D:\\map_from_maira_181114\\ELPHO_TEST\\2011_Dataset"
 
#a = os.walk(startpath)
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="Polyline"):
    for filename in filenames:
        if filename.endswith(".shp") and '_Ajones_' in filename:
            #for dirpath in dirpath:
            #print dirpath.rsplit("\\",-1)[-1]
            #c.write(filename +'\n')
            f.write(dirpath + '\\' + filename +'\n')            
         
    



''' 
for root, dirs, files in a:
    for filename in files:
        if filename.endswith(".dwg") or filename.endswith(".DWG"):
            f.write(filename +'\n')
        if filename.endswith(".tiff") or filename.endswith(".TIFF"):
            c.write(filename +'\n')
        if filename.endswith(".tif") or filename.endswith(".TIF"):
            t.write(filename +'\n')
'''