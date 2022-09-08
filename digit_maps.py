myList=[]
field=layer
in_workspace = u"E:\\DIGITAL_MAPS"
f = open(u"E:\\DIGITAL_MAPS\\unique_layer.csv","w")
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass"):
    for filename in filenames:
        if (filename.endswith(".shp")):
            parent_path = os.path.join(dirpath, filename)
            unique_values = {row[0] for row in arcpy.da.SearchCursor(parent_path, field)}
            for un in unique_values:
                f.write(str(un) +'\n')
				
if __name__ == "__main__":
    main()

	#arcpy.FeatureClassToGeodatabase_conversion(shpfile,MasterGDB)
	YPOMNHMA
	Shape
	"OID@","SHAPE@"
	
    with arcpy.da.InsertCursor(newfname, ("*")) as i_cursor:
        with arcpy.da.SearchCursor(shpfile, ("SHAPE@","Layer"), "\"Layer\" = " + layer) as s_cursor:
            for s_row in s_cursor:
                i_cursor.insertRow(s_row)
				
				"\"Layer\" = " + layer
				"\"Layer\"" +  " = "  + layer
			
				"""Layer = 'YPOMNHMA'"""--sosto
				
				s_cursor = arcpy.SearchCursor(shpfile, ("Shape"),"Layer = YPOMNHMA")
				,where_clause="Layer = YPOMNHMA"
	--------------------------------
	# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env
import sys

def main(shpfile,layer,outputdirec,fgdb):
    #shpfile = sys.argv[1]
    #layer = sys.argv[2]
    #outputdirec=  sys.argv[3]
    #fgdb = sys.argv[4]
#arcpy.management.CreateFileGDB(u"E:\\merge_by_geom\\ESYE","polinegeo","10.0")
# #mastergdb=str(fgdb)

    shpfile = arcpy.GetParameterAsText(0)
    layer = arcpy.GetParameterAsText(1)
    outputdirec = arcpy.GetParameterAsText(2)
    fgdb = arcpy.GetParameterAsText(3)

#     shpfile = sys.argv[0:]
#     layer = sys.argv[1:]
#     outputdirec=  sys.argv[2:]
#     fgdb = sys.argv[3:]

#     shapef = str(shpfile) 
#     laye = str(layer) 
#     outputdirect=  str(outputdirec)
#     fd = str(fgdb) 

    out_name = str(fgdb) + ".gdb"
    MasterGDB=arcpy.management.CreateFileGDB(outputdirec,out_name,"10.0")
#inpot=os.path.join()
#arcpy.MakeFeatureLayer_management("C:/data/mexico.gdb/cities","cities_lyr")

#     newshp=arcpy.CreateFeatureclass_management(MasterGDB, layer,'GREK_GRID')

#fields = arcpy.ListFields("c:/data/municipal.gdb/hospitals")
#expression = Layer + " = " + layer 
#     arcpy.FeatureClassToFeatureClass_conversion(shpfile,MasterGDB,layer,"\"Layer\" = " + layer)

if __name__ == "__main__":
    main(sys.argv[0],sys.argv[1],sys.argv[2], sys.argv[3])
	
---------------------------------------------------very good---------------------------------------------
# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env
import sys
import arceditor

def main(outputdirec,fgdb,layer,shpfile):
    #shpfile = sys.argv[1]
    #layer = sys.argv[2]
    #outputdirec=  sys.argv[3]
    #fgdb = sys.argv[4]
#arcpy.management.CreateFileGDB(u"E:\\merge_by_geom\\ESYE","polinegeo","10.0")
# #mastergdb=str(fgdb)

    outputdirec = arcpy.GetParameterAsText(0)
    fgdb = arcpy.GetParameterAsText(1)
    layer = arcpy.GetParameterAsText(2)
    shpfile = arcpy.GetParameterAsText(3)

#     shpfile = sys.argv[0:]
#     layer = sys.argv[1:]
#     outputdirec=  sys.argv[2:]
#     fgdb = sys.argv[3:]

#     shapef = str(shpfile) 
#     laye = str(layer) 
#     outputdirect=  str(outputdirec)
#     fd = str(fgdb) 

    out_name = str(fgdb) + ".gdb"
    MasterGDB=arcpy.management.CreateFileGDB(outputdirec,out_name,"10.0")
#inpot=os.path.join()
#arcpy.MakeFeatureLayer_management("C:/data/mexico.gdb/cities","cities_lyr")

#     spatial_reference = arcpy.Describe(shpfile).spatialReference
    newfname = arcpy.CreateFeatureclass_management(MasterGDB, layer,"Polyline")
#     temp = arcpy.CreateFeatureclass_management(MasterGDB, "temp","Polyline")
    newshape = arcpy.FeatureClassToFeatureClass_conversion(shpfile,MasterGDB,"temp2")
    where_clause = """Layer = """ + layer
    i_cursor = arcpy.da.InsertCursor(newfname, ("SHAPE@"))
    s_cursor = arcpy.da.SearchCursor(newshape, ("SHAPE@"),where_clause)
    for s_row in s_cursor:
        shape = s_row[0]
        i_cursor.insertRow(shape)
    del s_cursor,i_cursor
#     del i_cursor

#fields = arcpy.ListFields("c:/data/municipal.gdb/hospitals")
#expression = Layer + " = " + layer 
#     arcpy.FeatureClassToFeatureClass_conversion(shpfile,MasterGDB,layer,"\"Layer\" = " + layer)
    

if __name__ == "__main__":
    main(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])
	