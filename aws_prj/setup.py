from distutils.core import setup
import py2exe
import time
setup(console=["C:\\Users\\galionis.ELPHODOMAIN\\workspace\\aws_prj\\amazup.py"],
      options={"py2exe" : {
 "includes" : ["boto","zipfile","os","shutil","boto.s3.key"], 
 "packages":["boto"],
 "excludes":["Carbon","_scproxy", "Carbon.Files"]}})
time.sleep(5)