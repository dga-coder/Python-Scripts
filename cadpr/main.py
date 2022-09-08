# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting

# Set local variables
input_cad_folder = u"D:\\ANTIKEIMENIKES\\XARTES_2007_FEK_270_VERSION\\DRIVE_D\\ANTIKEIMENIKES\\XARTES_2007_FEK_270_VERSION"


output_gdb_folder = u"D:\\ANTIKEIMENIKES\\XARTES_2006_FEK_1982_SHP2FGDB"
output_gdb = "cadfile.gdb"
output_gdb_path = os.path.join(output_gdb_folder, output_gdb)
if (arcpy.Exists(output_gdb_path)):
    arcpy.Delete_management(output_gdb_path)
    arcpy.management.CreateFileGDB(output_gdb_folder,output_gdb,"10.0")
else:
    #arcpy.management.CreateFileGDB(u"D:\\POA_vs_CSL\\POA_FGDB","POA","10.0")
    arcpy.management.CreateFileGDB(output_gdb_folder,output_gdb,"10.0")
    #arcpy.CreateFileGDB_management(output_gdb_folder, output_gdb)

reference_scale = "1000"
spatial_reference = u"D:\\2100.prj"

# Create a FileGDB for the fds
#try:
#    arcpy.CreateFileGDB_management(output_gdb_folder, output_gdb)
#except:
#    pass

# For loop iterates through every file in input folder
for found_file in os.listdir(input_cad_folder):
    # Searches for .dwg files
    if found_file.endswith(".dwg"):

        print "Converting: " + found_file
        input_cad_dataset = os.path.join(input_cad_folder, found_file)
        #print input_cad_dataset
        try:
            arcpy.CADToGeodatabase_conversion(input_cad_dataset, output_gdb_path,found_file[:-4],reference_scale, spatial_reference)
        except Exception as err:
            arcpy.AddError(err)
            #print arcpy.GetMessage(err)