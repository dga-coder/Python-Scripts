import os
import arcpy

in_workspace = u"D:\\POA_vs_CSL\\POA"
count=0
coun =0
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass",type="ALL"):
        for filename in filenames:
            if (filename.endswith("POA.shp")):
                count +=1
                #f.write(dirpath + '\\' + filename +'\n')
            if (filename.endswith("CSL.shp")):
                coun +=1    
print "\nNumber of POA shapefiles is " + str(count)
print "\nNumber of CSL shapefiles is " + str(coun)
            