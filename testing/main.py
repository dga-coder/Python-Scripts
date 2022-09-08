# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting

#path = 'E:\\merge_by_geom\\test_workspace'
#env.workspace = path

#fcs_in_workspace=[]

#workspaces = arcpy.ListWorkspaces("*", "Folder")
#for ws in workspaces:
#    for fc in fcs_in_workspace(os.path.join(ws, ws)):
#        print fc

env.workspace = u"E:\\merge_by_geom\\ESYE"
#env.workspace = u"E:\\merge_by_geom\\test_workspace"
MasterGDB = u"E:\\merge_by_geom\\ESYE\\polinegeo.gdb"
if (arcpy.Exists(MasterGDB)):
    arcpy.Delete_management(MasterGDB)
else:
    arcpy.management.CreateFileGDB(env.workspace,"polinegeo","10.0")
#OutGDB = env.workspace +"\\polinegeo.gdb"
f = open(u"E:\\merge_by_geom\\ESYE\\polylinelog.csv","w")

fcList = []
count = 0
try:
    for dirname, dirnames, filenames in os.walk(arcpy.env.workspace):
        for subdirame in dirnames:
            env.workspace = os.path.join(dirname,subdirame)
            fcList = arcpy.ListFeatureClasses("*.shp","Polyline")
            for fc in fcList:
                count = count + 1
                f.write(dirname + '\\' + fc +'\n')
                arcpy.FeatureClassToGeodatabase_conversion(fc,MasterGDB)
    print "Number of shapefiles imported in Geodatabase is " + str(count)
    #print len(fcList)            


except Exception as e:
    print(e)
else :
    print("Compressing FileGDB...")
    arcpy.CompressFileGeodatabaseData_management(MasterGDB)
    print(MasterGDB + " has been compressed.")



                 
'''
fcList = []
count = 0
for dirname, dirnames, filenames in os.walk(env.workspace):
    for s in dirnames:
        print s
'''
'''
        print os.path.join(dirname, subdirname)
        env.workspace = os.path.join(dirname, subdirname)
        fcList = arcpy.ListFeatureClasses()
        for fc in fcList:
            print fc
            count = count + 1
            print count
'''



'''
features = []

workspaces = arcpy.ListWorkspaces("*", "Folder")
for ws in workspaces:
    env.workspace = ws
    #diras = arcpy.ListWorkspaces("*","Folder")
    #for dira in diras:
        #env.workspace = dira
    print ws
#print diras
'''        
'''
        subas = arcpy.ListWorkspaces("*","Folder")
        for suba in subas:
            env.workspace = suba
            #print ws
            #print dira
print workspaces
print diras   
print subas   
'''    
  
     


'''
try:
    f = open(u"E:\\merge_by_geom\\test_workspace\\polylinelog.csv","w")
    fcs = arcpy.ListFeatureClasses("*.shp")#,"Polyline")
    for fc in fcs:
                features.append(os.path.join(fc))
    workspaces = arcpy.ListWorkspaces("*", "Folder")
    
    for ws in workspaces:
        arcpy.env.workspace = ws
        fcs = arcpy.ListFeatureClasses("*.shp")#,"Polyline")
        for fc in fcs:
            features.append(os.path.join(fc)) 
        subfols = arcpy.ListWorkspaces("*", "Folder")
        for subfol in subfols:
            arcpy.env.workspace = subfol
            
            fcs = arcpy.ListFeatureClasses("*.shp")#,"Polyline")
            for fc in fcs:
                features.append(os.path.join(fc))
                
            subdirs = arcpy.ListWorkspaces("*", "Folder")
            for subdir in subdirs:
                arcpy.env.workspace = subdir
                
                fcs = arcpy.ListFeatureClasses("*.shp")#,"Polyline")
                for fc in fcs:
                    features.append(os.path.join(fc))
            folds = arcpy.ListWorkspaces("*", "Folder")                     
            for fold in folds:
                arcpy.env.workspace = fold
                fcs = arcpy.ListFeatureClasses("*.shp")#,"Polyline")
                for fc in fcs:
                    features.append(os.path.join(fc))
                    #features = arcpy.ListFeatureClasses()
                    #for feature in features:  
                        arcpy.FeatureClassToGeodatabase_conversion(feature,OutGDB)
                        #f.write(feature +"\n")
                print feature              
    print "Number of shapefiles copied is"
    print len(features)
                     
                #print subdir
            #fcs = arcpy.ListFeatureClasses("*","Polyline")
            #for fc in fcs:
                #arcpy.FeatureClassToGeodatabase_conversion(fc,OutGDB)
                #count +=1
                #f.write(subfol + '\\' + fc +'\n')
    #print "\n Number of shapefiles copied is " + str(count)
except Exception as e:
    print(e)
else :
    print("Compressing FileGDB...")
    arcpy.CompressFileGeodatabaseData_management(OutGDB)
    print(OutGDB + " has been compressed.")
    
'''  


 
'''     
def fcs_in_workspace(workspace):
    arcpy.env.workspace = workspace
    for fc in arcpy.ListFeatureClasses():
        yield os.path.join(workspace, fc)
        for ws in arcpy.ListWorkspaces():
            for fc in fcs_in_workspace(os.path.join(workspace, ws)):
                yield fc

for fc in fcs_in_workspace(u"E:\\merge_by_geom\\test_workspace\\Ν. ΑΙΤΩΛΙΑΣ & ΑΚΑΡΝΑΝΙΑΣ"):
    print(fc)
'''    
'''
    
    
        

#arcpy.management.CreateFileGDB(env.workspace,"Project","10.0")

#try:
#def fcs_in_workspace(workspace):
#fcs_in_workspace = []

#for fc in arcpy.ListFeatureClasses():
#    for ws in arcpy.ListWorkspaces():
#        print ws
        
        
        #for fc in fcs_in_workspace(os.path.join(path, ws)):
            #print fc

'''
'''           
            if ws != path +"\\Project.gdb":
                        yield fc
                        OutGDB = env.workspace +"\\Project.gdb"
                        for fc in fcs_in_workspace(env.workspace):
                            arcpy.FeatureClassToGeodatabase_conversion(fc,OutGDB)
                            print(fc +' copied.')

except Exception as e:
    print(e)
else:
    OutGDB = env.workspace +"\\Project.gdb"
    env.workspace = path
    print("Compressing FileGDB.")
    arcpy.CompressFileGeodatabaseData_management(OutGDB)
    print(OutGDB + " has been compressed.")
'''