# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting

'''
poaList = []
cslList = []
poashapefile = u"D:\\POA_vs_CSL\\POA_FGDB\\Mergedpoa.shp"
cslshapefile = u"D:\\POA_vs_CSL\\CSL_FGDB\\Mergedcsl.shp"
in_workspace = u"D:\\POA_vs_CSL\\POA"
#fpoa = open(u"D:\\POA_vs_CSL\\POA_FGDB\\poamerg.csv","w")
#fcsl = open(u"D:\\POA_vs_CSL\\CSL_FGDB\\cslmerg.csv","w")
count=0
coun =0
POAGDB = u"D:\\POA_vs_CSL\\POA_FGDB\\POA.gdb"
CSLGDB = u"D:\\POA_vs_CSL\\CSL_FGDB\\CSL.gdb"
if os.path.isfile(u"D:\\POA_vs_CSL\\POA_FGDB\\poamerg.csv"):
    os.remove(u"D:\\POA_vs_CSL\\POA_FGDB\\poamerg.csv")
else:
    fpoa = open(u"D:\\POA_vs_CSL\\POA_FGDB\\poamerg.csv","w")
    #fpoa.close()
if os.path.isfile(u"D:\\POA_vs_CSL\\CSL_FGDB\\cslmerg.csv"):
    os.remove(u"D:\\POA_vs_CSL\\CSL_FGDB\\cslmerg.csv")
else:
    fcsl = open(u"D:\\POA_vs_CSL\\CSL_FGDB\\cslmerg.csv","w")
    #fcsl.close() 
if (arcpy.Exists(POAGDB)):
    arcpy.Delete_management(POAGDB)
else:
    arcpy.management.CreateFileGDB(u"D:\\POA_vs_CSL\\POA_FGDB","POA","10.0")
if (arcpy.Exists(CSLGDB)):
    arcpy.Delete_management(CSLGDB)
else:
    arcpy.management.CreateFileGDB(u"D:\\POA_vs_CSL\\CSL_FGDB","CSL","10.0")
fpoa = open(u"D:\\POA_vs_CSL\\POA_FGDB\\poamerg.csv","w")
fcsl = open(u"D:\\POA_vs_CSL\\CSL_FGDB\\cslmerg.csv","w")
try:
    for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="ALL"):
        for filename in filenames:
            if (filename.endswith("POA.shp")):
                count +=1
                fpoa.write(dirpath + '\\' + filename +'\n')
                poaList.append(os.path.join(dirpath, filename))
                arcpy.FeatureClassToGeodatabase_conversion(poaList,POAGDB)
            if (filename.endswith("CSL.shp")):
                coun +=1
                fcsl.write(dirpath + '\\' + filename +'\n')
                cslList.append(os.path.join(dirpath, filename))  
                arcpy.FeatureClassToGeodatabase_conversion(cslList,CSLGDB)               
    print "\nNumber of POA shapefiles is " + str(count)
    print "\nNumber of CSL shapefiles is " + str(coun)
except Exception as err:
    arcpy.AddError(err)
    print "FAIL."
    print err
'''

vnewflist = []
fnlist = []
poaList = []
cslList = []
poashapefile = u"D:\\POA_vs_CSL\\POA_FGDB\\Mergedpoa.shp"
cslshapefile = u"D:\\POA_vs_CSL\\CSL_FGDB\\Mergedcsl.shp"
valu =0
count=0
coun =0
fpoa = open(u"D:\\POA_vs_CSL\\POA_FGDB\\poamerg.csv","w")
fcsl = open(u"D:\\POA_vs_CSL\\CSL_FGDB\\cslmerg.csv","w")
in_workspace = u"D:\\POA_vs_CSL\\POA_NEW_WITH_DESCR"
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="ALL"):
    for filename in filenames:
        if (filename.endswith("POA.shp")):
            poaList.append(os.path.join(dirpath, filename))
            #vnewflist.append(os.path.join(filename.strip("_CSL.shp")))
            count +=1
            fpoa.write(dirpath + "\\" + filename +"\n") 
        if (filename.endswith("CSL.shp")):
            cslList.append(os.path.join(dirpath, filename))
            coun +=1
            fcsl.write(dirpath + '\\' + filename +'\n')
print "\nNumber of POA shapefiles is " + str(count)
print "\nNumber of CSL shapefiles is " + str(coun)
try:
    arcpy.Merge_management(poaList,poashapefile)
    arcpy.Merge_management(cslList,cslshapefile)
    print "merge:  SUCCESS."
except Exception as err:
    arcpy.AddError(err)
    print "merge:  FAIL."
    print err
            





#for poali in poaList:
    #uprows = arcpy.da.UpdateCursor(poali,("NOMOS_DESC"))
    #for uprow in uprows:
        #uprow[0]  = vnewflist[count]
        #uprows.updateRow(uprow)
    #count = count+1
    #print "\nNumber of rows updated are " + str(sum(1 for row in uprows))
    #del uprow, uprows
                #fnlist.append(os.path.join(filename))
                #for fl in fnlist:
                
            


            
            
        #if (filename.endswith("CSL.shp")):
            #coun +=1
            #fcsl.write(dirpath + '\\' + filename +'\n')
            #cslList.append(os.path.join(dirpath, filename))
            #for cso in cslList:
            #    arcpy.AddField_management(cso, "NOMOS_DESC", "TEXT")
                
                    
                
            
            #print dirpath + '\\' + filename
            #arcpy.AddField_management(dirpath + '\\' + filename, "NOMOS_DESCR", "TEXT")
            #fields = arcpy.ListFields(dirpath + '\\' + filename,"MUN_CODE")
            #for field in fields:       
            #count +=1
            #fpoa.write(dirpath + "\\" + filename +"\n")
            #poaList.append(os.path.join(dirpath, filename))
            #vnewf = filename.strip("_POA.shp")
            #print filename + "--" + vnewf
            
            
            #print (dirpath + "\\" + filename +"\n")
            #print "\nNumber of POA shapefiles is " + str(count) 
