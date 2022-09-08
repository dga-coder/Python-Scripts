# -*- coding: utf-8 -*-
import os
import arcpy
from collections import Counter
from arcpy import env
 
 
def recursive_list_fcs(workspace, wild_card=None, feature_type=None):
    """Returns a list of all feature classes in a tree.  Returned
    list can be limited by a wildcard, and feature type.
    """
    preexisting_wks = arcpy.env.workspace
    arcpy.env.workspace = workspace
 
    try:
        list_fcs = []
        for root, dirs, files in os.walk(workspace):
            arcpy.env.workspace = root
            fcs = arcpy.ListFeatureClasses(wild_card, feature_type)
            if fcs:
                list_fcs += [os.path.join(root, fc) for fc in fcs]
 
            # Pick up workspace types that don't have a folder
            #  structure (coverages, file geodatabase do)
            workspaces = set(arcpy.ListWorkspaces()) - \
                         set(arcpy.ListWorkspaces('', 'FILEGDB')) -\
                         set(arcpy.ListWorkspaces('', 'COVERAGE'))
 
            for workspace in workspaces:
                arcpy.env.workspace = os.path.join(root, workspace)
                fcs = arcpy.ListFeatureClasses(wild_card,
                                               feature_type)
 
                #if fcs:
                    #list_fcs += [os.path.join(root, workspace, fc)
                                 #for fc in fcs]
 
            for dataset in arcpy.ListDatasets('', 'FEATURE'):
                ds_fcs = arcpy.ListFeatureClasses(wild_card,
                                                  feature_type,
                                                  dataset)
                if ds_fcs:
                    list_fcs += [os.path.join(
                        root, workspace, dataset, fc)
                                 for fc in ds_fcs]
 
    except Exception as err:
        raise err
    finally:
        arcpy.env.workspace = preexisting_wks
 
    return list_fcs
    #print list_fcs


#werk = u"E:\\merge_by_geom\\ESYE\\OIKISMOI_MH_PSIFIOPOIHMENOI_2011\\Ν. ΑΙΤΩΛΙΑΣ & ΑΚΑΡΝΑΝΙΑΣ\\ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ"
#recursive_list_fcs(werk, wild_card=None, feature_type=None)

#shplist = []
#shplist = arcpy.ListFeatureClasses()
count = 0 
for i in recursive_list_fcs(u"E:\\merge_by_geom\\ESYE", feature_type="Polyline"):
    #print i
    #shplist.append(i)
    #result1 = int(arcpy.GetCount_management(i).getOutput(0))
    count +=1
print "\n Number of shapefiles is " + str(count)
#print shplist

