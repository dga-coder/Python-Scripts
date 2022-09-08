# -*- coding: utf-8 -*-
import boto
import zipfile
import os
import shutil
from boto.s3.key import Key
from boto.s3 import connect_to_region
from boto.s3.connection import Location
boto.set_stream_logger('wrongs')

dirpath = u"C:\\ESMA_BCKPS"
dest = u"C:\\ESMA_BCKPS\\ESMA_RAWS"
for filo in os.listdir(u"C:\\ESMA_BCKPS"):
    if filo.endswith(".bak"):
        newZipFN = filo[0:-4] + ".zip"
        newf = str(newZipFN)
        zipobj = zipfile.ZipFile(os.path.join(dirpath,newf),'w',allowZip64=True)
        if os.path.splitext(filo)[1].lower() != ".zip":
            nfile = os.path.join(dirpath, filo)
            zfile = zipobj.write(nfile,os.path.basename(nfile),zipfile.ZIP_DEFLATED)
            zipobj.close()
            shutil.move(os.path.join(dirpath, filo), os.path.join(dest, filo))
aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxx'
aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
conn =boto.connect_s3(aws_access_key_id,aws_secret_access_key,debug=2)
#conn = connect_to_region(Location.EU,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
#bucket = conn.get_bucket("elpho")
bucketName = "elpho" 
bucket = conn.lookup(bucketName)
#fil="DhpeMetadataDev_201502170500.rar"
fil = newf
#ufname=u"D:\\test_amazon_backup\\DhpeMetadataDev_201502170500.rar"
ufname=os.path.join(dirpath, newZipFN)
k = Key(bucket)
k.key = "esma/" + fil
# print ("Uploading " + ufname + " to Amazon S3")  #use of parethnesis only in python3
print "Uploading " + ufname + " to Amazon S3"  #use of parethnesis only in python3
k.set_contents_from_filename(ufname,policy="public-read",encrypt_key=False)
k.make_public()
os.remove(os.path.join(dirpath, newZipFN))
