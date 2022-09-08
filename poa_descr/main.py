# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting
import zipfile
import glob
import re
import shutil

poaList = []
#shp_files = []
in_workspace = u"D:\\POA_vs_CSL\\POA"
arcpy.env.workspace = u"D:\\POA_vs_CSL\\POA"
f = open("D:\\POA_vs_CSL\\POA\\POAZIP.csv","w")
#count =0 
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="ALL"):
    shp_files = glob.glob(dirpath + '\\' + "*POA.shp")
    for sf in shp_files:
        #print 'Zipping ' + sf
        
        #newZipFN = sf[0:-3] + 'zip'
        newZipFN = sf[0:-4] + ".zip"
        newf = str(newZipFN)
        vnewf = newf.rsplit("\\",-1)[-1]
        zipobj = zipfile.ZipFile(os.path.join(dirpath,vnewf),'w')
        #TAKE SHAPEFILE COMPONENTS
        for infile in glob.glob(sf.replace(".shp",".*")):
            #print 'zipping ' + infile + ' into ' + vnewf
            if os.path.splitext(infile)[1].lower() != ".zip": 
                # Avoid zipping the zip file!  
                zipobj.write(infile,os.path.basename(infile))
        print 'ShapeFile zipped!'  
        zipobj.close()     
        
        
        
        #print newf
        #print vnewf
        
        #patterns = ["\*_POA.zip"]
        #match = re.search(patterns, newZipFN)
        
        
        #for pattern in patterns:
            #re.search(pattern,newZipFN):
            #print 
             
        #newZname = newZipFN[0:]
        #print newZipFN 
    
    
    
    '''
    for filename in filenames:
        if (filename.endswith("POA.shp")):
            zipf = zipfile.ZipFile(os.path.join(dirpath,filename[0:-4]+".zip"), mode='w')
            for infile in glob.glob( sf.lower().replace(".shp",".*")):
                print 'zipping ' + infile + ' into ' + newZipFN
                '''  
            
            
            
            
            
            #zipf.write(dirpath,filename)
            
            
            
            #shp_files = glob.glob(dirpath + '\\' + filename +'\n')
            #for shp in shp_files:
                #print shp 
    
    
    #for shp in  shp_files:
        #print shp
   
    
    #for filename in filenames:
        
        
'''good
        if (filename.endswith("POA.shp")):
            zipf = zipfile.ZipFile(os.path.join(dirpath,filename[0:-4]+".zip"), mode='w')
           ''' 
            
            #zipf.write(os.path.join(dirpath,filename))
            #zipf.close()
            
            
            #shp_List = glob.glob(str(search_Folder) + "\*.shp")  
            
            #poaList.append(os.path.join(filename))
            #for poali in poaList:
                #print 'creating archive'
                #zipf = zipfile.ZipFile(os.path.join(dirpath,poali[0:-4]+".zip"), mode='w')
                #zipf.write(os.path.join(dirpath,poali))
                #zipf.close()
                
                #zf = zipfile.ZipFile('zipfile_write.zip', mode='w')
            #count +=1
            #print (filename[0:-4])
            #zipf = zipfile.ZipFile(filename[0:-4]+".zip", mode='w')
            #
            #f.write(dirpath + '\\' + filename +'\n')
            #poaList.append(os.path.join(dirpath, filename))