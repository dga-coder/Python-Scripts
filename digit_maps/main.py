# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env
import sys
import arceditor

def main(outputdirec,fgdb,layer,shpfile):
    outputdirec = arcpy.GetParameterAsText(0)
    fgdb = arcpy.GetParameterAsText(1)
    layer = arcpy.GetParameterAsText(2)
    shpfile = arcpy.GetParameterAsText(3)
    out_name = str(fgdb) + ".mdb"
    fulldir = str(outputdirec) + "\\" + out_name
    layerex = fulldir + "\\" + str(layer)
#     sr = arcpy.SpatialReference(2100)
    if (arcpy.Exists(fulldir)):
        if (arcpy.Exists(layerex)):
            newshapex = arcpy.FeatureClassToFeatureClass_conversion(shpfile,fulldir,"tempex")
            arcpy.AddField_management(newshapex, "SHP_DESCR","TEXT")
            uprows = arcpy.da.UpdateCursor(newshapex,("SHP_DESCR"))
            for uprow in uprows:
                uprow[0] = shpfile.rsplit("\\",-4)[-1]
                uprows.updateRow(uprow)
            del uprows 
            field = "Layer" 
            newlayer = str(layer)
            sql = format(arcpy.AddFieldDelimiters(newshapex,field)) +  " = '" + newlayer + "'" 
            i_cursor = arcpy.da.InsertCursor(layerex, ("SHAPE@","SHP_DESCR"))
            s_cursor = arcpy.da.SearchCursor(newshapex, ("SHAPE@","SHP_DESCR"),sql)
            for s_row in s_cursor:
                i_cursor.insertRow(s_row)
            del s_cursor,i_cursor
            del newshapex
            env.workspace = fulldir 
            arcpy.Delete_management("tempex")
        else:
            newfnamex = arcpy.CreateFeatureclass_management(fulldir,layer,"Polyline")
            newshapex = arcpy.FeatureClassToFeatureClass_conversion(shpfile,fulldir,"tempex")
            arcpy.AddField_management(newshapex, "SHP_DESCR","TEXT")
            uprows = arcpy.da.UpdateCursor(newshapex,("SHP_DESCR"))
            for uprow in uprows:
                uprow[0] = shpfile.rsplit("\\",-4)[-1]
                uprows.updateRow(uprow)
            del uprows
            arcpy.AddField_management(newfnamex, "SHP_DESCR","TEXT")
            field = "Layer" 
            newlayer = str(layer)
            sql = format(arcpy.AddFieldDelimiters(newshapex,field)) +  " = '" + newlayer + "'" 
            i_cursor = arcpy.da.InsertCursor(newfnamex, ("SHAPE@","SHP_DESCR"))
            s_cursor = arcpy.da.SearchCursor(newshapex, ("SHAPE@","SHP_DESCR"),sql)
            for s_row in s_cursor:
                i_cursor.insertRow(s_row)
            del s_cursor,i_cursor
            del newshapex
            env.workspace = fulldir 
            arcpy.Delete_management("tempex")
    else :
        MasterGDB=arcpy.CreatePersonalGDB_management(outputdirec,out_name,"10.0")
        newfname = arcpy.CreateFeatureclass_management(MasterGDB, layer,"Polyline")
        arcpy.AddField_management(newfname, "SHP_DESCR","TEXT")
        newshape = arcpy.FeatureClassToFeatureClass_conversion(shpfile,MasterGDB,"tempin")
        arcpy.AddField_management(newshape, "SHP_DESCR","TEXT")
        uprows = arcpy.da.UpdateCursor(newshape,("SHP_DESCR"))
        for uprow in uprows:
            uprow[0] = shpfile.rsplit("\\",-4)[-1]
            uprows.updateRow(uprow)
        del uprows 
        field = "Layer" 
        newlayer = str(layer)
        sql = format(arcpy.AddFieldDelimiters(newshape,field)) +  " = '" + newlayer + "'" 
        i_cursor = arcpy.da.InsertCursor(newfname, ("SHAPE@","SHP_DESCR"))
        s_cursor = arcpy.da.SearchCursor(newshape, ("SHAPE@","SHP_DESCR"),sql)
        for s_row in s_cursor:
            i_cursor.insertRow(s_row)
        del s_cursor,i_cursor
        del newshape
        env.workspace = fulldir 
        arcpy.Delete_management("tempin")
if __name__ == "__main__":
    main(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])