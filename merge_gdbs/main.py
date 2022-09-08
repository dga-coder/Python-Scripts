# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env

# outLocation = "D:\\gdbs_dgpe_digit\\merged_fgdb\\dipe_ext.gdb"
outLocation = u"G:\\dhpe_dgbs\\final_gdb\\test_final.gdb"
#outLocation = "D:\\gdbs_dgpe_digit\\TESTS_MERGED\\LAST\\dipe_ext.gdb"
FCPALAIOS_AIGIALOS = "PALAIOS_AIGIALOS_ALL"
FCPAROXTHIA_ZONE = "PAROXTHIA_ZONE_ALL"
FCXERS_ZON_LIMENA = "XERS_ZON_LIMENA_ALL"
FCMAP_WORKS = "MAP_WORKS_ALL"
FCPALAIA_OXTHI = "PALAIA_OXTHI_ALL"
FCGEN_POINT = "GEN_POINT_ALL"
FCGEN_POLY = "GEN_POLY_ALL"
FCOXTHI = "OXTHI_ALL"
FCPARALIA = "PARALIA_ALL"
FCWORK_ = "WORK_ALL"
FCAMMOLIPSIES = "AMMOLIPSIES_ALL"
FCAPALO_ZONE_POLY = "APALO_ZONE_POLY_ALL"
FCDHMOSIA_AKINHTA = "DHMOSIA_AKINHTA_ALL"
FCGEN_LINE = "GEN_LINE_ALL"
FCAKTOGRAMMI = "AKTOGRAMMI_ALL"
FCAIGIALOS = "AIGIALOS_ALL"
FCACTION_POLY = "ACTION_POLY_ALL"
FCACTION_POINT = "ACTION_POINT_ALL"
FCACTION_LINE = "ACTION_LINE_ALL"

schemaType = "TEST"
fieldMappings = ""
subtype = ""
# in_workspace = "D:\\gdbs_dgpe_digit\\Last_for_merge"

# if (arcpy.Exists(outLocation)):
#     arcpy.Delete_management(outLocation)
# arcpy.management.CreateFileGDB(u"D:\\gdbs_dgpe_digit","dipe_ext","10.0")

in_workspace = u"G:\\dhpe_dgbs\\FINAL_COPY_EXTRACT\\unzip_rename"
for (path, dirs, files) in os.walk(in_workspace):
    if ".gdb" not in path.lower():  
        env.workspace = path
        geodbs = arcpy.ListWorkspaces("*", "FileGDB")
        for geo in geodbs:
            env.workspace = geo
            fcList = arcpy.ListFeatureClasses()
            for fc in fcList:
                if (fc=="PALAIOS_AIGIALOS"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCPALAIOS_AIGIALOS, schemaType, fieldMappings, subtype)
                if (fc=="PAROXTHIA_ZONE"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCPAROXTHIA_ZONE, schemaType, fieldMappings, subtype)
                if (fc=="XERS_ZON_LIMENA"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCXERS_ZON_LIMENA, schemaType, fieldMappings, subtype)
                if (fc=="MAP_WORKS"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCMAP_WORKS, schemaType, fieldMappings, subtype)
                if (fc=="GEN_POINT"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCGEN_POINT, schemaType, fieldMappings, subtype)
                if (fc=="GEN_POLY"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCGEN_POLY, schemaType, fieldMappings, subtype)
                if (fc=="OXTHI"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCOXTHI, schemaType, fieldMappings, subtype)
                if (fc=="PARALIA"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCPARALIA, schemaType, fieldMappings, subtype)
                if (fc=="WORK_"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCWORK_, schemaType, fieldMappings, subtype)
                if (fc=="AMMOLIPSIES"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAMMOLIPSIES, schemaType, fieldMappings, subtype)
                if (fc=="APALO_ZONE_POLY"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAPALO_ZONE_POLY, schemaType, fieldMappings, subtype)
                if (fc=="DHMOSIA_AKINHTA"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCDHMOSIA_AKINHTA, schemaType, fieldMappings, subtype)
                if (fc=="GEN_LINE"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCGEN_LINE, schemaType, fieldMappings, subtype)
                if (fc=="AKTOGRAMMI"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAKTOGRAMMI, schemaType, fieldMappings, subtype)
                if (fc=="AIGIALOS"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAIGIALOS, schemaType, fieldMappings, subtype)
                if (fc=="ACTION_POLY"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCACTION_POLY, schemaType, fieldMappings, subtype)
                if (fc=="ACTION_POINT"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCACTION_POINT, schemaType, fieldMappings, subtype)
                if (fc=="ACTION_LINE"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCACTION_LINE, schemaType, fieldMappings, subtype)
               
