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

newflist=[]
fold = "G:\\dhpe_dgbs\\final_files"
#dstdir = "D:\\gdbs_dgpe_digit\\unrar"
unzipdir = "G:\\dhpe_dgbs\\FINAL_COPY_EXTRACT\\unzip_rename\\"

for fn in os.listdir(fold):
    if (fn.endswith(".zip")):
        nflist = os.path.join(fold, fn)
        newflist.append(nflist)
        for nf in newflist:
            nzip = nf.rsplit("\\",-4)[-1]
            nunrar = string.replace(nzip,".zip",".gdb")
            fh = open(nf, 'rb')
            z = zipfile.ZipFile(fh)
            for name in z.namelist():
                unrardir = unzipdir + nunrar
                z.extract(name, unrardir)
            fh.close()