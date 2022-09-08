# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
import sys
import os.path
from arcpy import env
from datetime import datetime
import glob
import shutil
import zipfile
import string
import csv

# newflist=[]
# fold = "G:\\dhpe_dgbs\\finished"
# #dstdir = "D:\\gdbs_dgpe_digit\\unrar"
# unzipdir = "G:\\dhpe_dgbs\\user_per_filename\\"
# 
# for fn in os.listdir(fold):
#     if (fn.endswith(".zip")):
#         nflist = os.path.join(fold, fn)
#         newflist.append(nflist)
#         for nf in newflist:
#             nzip = nf.rsplit("\\",-4)[-1]
#             nunrar = string.replace(nzip,".zip",".gdb")
#             fh = open(nf, 'rb')
#             z = zipfile.ZipFile(fh)
#             for name in z.namelist():
#                 unrardir = unzipdir + nunrar
#                 z.extract(name, unrardir)
#             fh.close()

rowlist=[]
# unqlist=[]
f = open(u"G:\\dhpe_dgbs\\user_per_filename\\creators.csv","w")
in_workspace = u"G:\\dhpe_dgbs\\user_per_filename"
for (path, dirs, files) in os.walk(in_workspace):
    if ".gdb" not in path.lower():  
        env.workspace = path
        geodbs = arcpy.ListWorkspaces("*", "FileGDB")
        for geo in geodbs:
            env.workspace = geo
            fcList = arcpy.ListFeatureClasses()
            for fc in fcList:
                if (fc != "WORK_"):
                    field_name = "CREATOR"
                    SQL = field_name + " IS NOT NULL"
                    sc = arcpy.SearchCursor(fc,SQL)
                    row = sc.next()
                    while row:
                        ngeo = geo.rsplit("\\",-4)[-1]
                        newuslist = os.path.join(ngeo, fc, row.getValue(field_name))
#                         f.write(dirpath + '\\' + filename +'\n')
#                         print(ngeo + "--" + fc + "--"+ row.getValue(field_name))
                        row = sc.next()
                        rowlist.append(newuslist)
rowlist=list(set(rowlist))
for rs in rowlist:
    f.write(str(rs) + "\n")
# f.write(reclist)
                    
#                     print rowlist 
#                     rowlist = list(set(newuslist))
#                     print rowlist
#                     for rows in rowlist:
#                         print rows
   
#     for rows in rowlist:
       
# reclist=str(rowlist) 
# f.write(reclist)                        
#                 fields = arcpy.ListFields(fc)
                