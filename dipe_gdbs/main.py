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

newest=[]
users=[]
fold = "D:\\gdbs_dgpe_digit\\BackupGeorefMetadaGDB"
dstdir = "D:\\gdbs_dgpe_digit\\unrar"
unzipdir = "D:\\gdbs_dgpe_digit\\unrar\\unzip_rename\\"
for fn in os.listdir(fold):
    if (fn.endswith(".zip")):
        usr = fn.rsplit('@', 1)[0]
        users.append(usr)
for us in users:
    newfn = os.path.join(fold, fn)
    newus = us + '*'
    newuslist = os.path.join(fold, newus)
#             print newuslist
    newest.append(max(glob.iglob(newuslist), key=os.path.getmtime))
    newest=list(set(newest))
for nw in newest:
    shutil.copy(nw, dstdir)
    nzip = nw.rsplit("\\",-4)[-1]
    nunrar = string.replace(nzip,".zip",".gdb")
    fh = open(nw, 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        unrardir = unzipdir + nunrar
        z.extract(name, unrardir)
    fh.close()
    

# print newest
#     modifiedTime = os.path.getmtime(newfn)
#     print datetime.fromtimestamp(modifiedTime).strftime("%d%m%Y %H:%M:%S")  
    
    
#print os.path.getmtime(newfn)          
#print os.path.getmtime(str(us)) 
#print fn.rsplit('@', 1)[0]
