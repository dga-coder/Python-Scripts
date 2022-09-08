# -*- coding: utf-8 -*-
import os
import arcpy
import arcgisscripting
from arcpy import env

# outLocation = "D:\\gdbs_dgpe_digit\\merged_fgdb\\dipe_ext.gdb"
outLocation = u"G:\\dhpe_dgbs\\gdbs\\ALL_MERGED_TILL_03062015\\test_final.gdb"
#outLocation = "D:\\gdbs_dgpe_digit\\TESTS_MERGED\\LAST\\dipe_ext.gdb"
FCPALAIOS_AIGIALOS = "PALAIOS_AIGIALOS_NEW"
FCPAROXTHIA_ZONE = "PAROXTHIA_ZONE_NEW"
FCXERS_ZON_LIMENA = "XERS_ZON_LIMENA_NEW"
FCMAP_WORKS = "MAP_WORKS_NEW"
FCPALAIA_OXTHI = "PALAIA_OXTHI_NEW"
FCGEN_POINT = "GEN_POINT_NEW"
FCGEN_POLY = "GEN_POLY_NEW"
FCOXTHI = "OXTHI_NEW"
FCPARALIA = "PARALIA_NEW"
FCWORK_ = "WORK_NEW"
FCAMMOLIPSIES = "AMMOLIPSIES_NEW"
FCAPALO_ZONE_POLY = "APALO_ZONE_POLY_NEW"
FCDHMOSIA_AKINHTA = "DHMOSIA_AKINHTA_NEW"
FCGEN_LINE = "GEN_LINE_NEW"
FCAKTOGRAMMI = "AKTOGRAMMI_NEW"
FCAIGIALOS = "AIGIALOS_NEW"
FCACTION_POLY = "ACTION_POLY_NEW"
FCACTION_POINT = "ACTION_POINT_NEW"
FCACTION_LINE = "ACTION_LINE_NEW"

schemaType = "TEST"
fieldMappings = ""
subtype = ""
# in_workspace = "D:\\gdbs_dgpe_digit\\Last_for_merge"

# if (arcpy.Exists(outLocation)):
#     arcpy.Delete_management(outLocation)
# arcpy.management.CreateFileGDB(u"D:\\gdbs_dgpe_digit","dipe_ext","10.0")

in_workspace = u"G:\\dhpe_dgbs\\gdbs\\INSGDBS"
for (path, dirs, files) in os.walk(in_workspace):
    if ".gdb" not in path.lower():  
        env.workspace = path
        geodbs = arcpy.ListWorkspaces("*", "FileGDB")
        for geo in geodbs:
            env.workspace = geo
            fcList = arcpy.ListFeatureClasses()
            for fc in fcList:
                if (fc=="PALAIOS_AIGIALOS_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCPALAIOS_AIGIALOS, schemaType, fieldMappings, subtype)
                if (fc=="PAROXTHIA_ZONE_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCPAROXTHIA_ZONE, schemaType, fieldMappings, subtype)
                if (fc=="XERS_ZON_LIMENA_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCXERS_ZON_LIMENA, schemaType, fieldMappings, subtype)
                if (fc=="MAP_WORKS_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCMAP_WORKS, schemaType, fieldMappings, subtype)
                if (fc=="GEN_POINT_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCGEN_POINT, schemaType, fieldMappings, subtype)
                if (fc=="GEN_POLY_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCGEN_POLY, schemaType, fieldMappings, subtype)
                if (fc=="OXTHI_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCOXTHI, schemaType, fieldMappings, subtype)
                if (fc=="PARALIA_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCPARALIA, schemaType, fieldMappings, subtype)
                if (fc=="WORK_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCWORK_, schemaType, fieldMappings, subtype)
                if (fc=="AMMOLIPSIES_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAMMOLIPSIES, schemaType, fieldMappings, subtype)
                if (fc=="APALO_ZONE_POLY_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAPALO_ZONE_POLY, schemaType, fieldMappings, subtype)
                if (fc=="DHMOSIA_AKINHTA_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCDHMOSIA_AKINHTA, schemaType, fieldMappings, subtype)
                if (fc=="GEN_LINE_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCGEN_LINE, schemaType, fieldMappings, subtype)
                if (fc=="AKTOGRAMMI_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAKTOGRAMMI, schemaType, fieldMappings, subtype)
                if (fc=="AIGIALOS_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCAIGIALOS, schemaType, fieldMappings, subtype)
                if (fc=="ACTION_POLY_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCACTION_POLY, schemaType, fieldMappings, subtype)
                if (fc=="ACTION_POINT_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCACTION_POINT, schemaType, fieldMappings, subtype)
                if (fc=="ACTION_LINE_ALL"):
                    arcpy.Append_management(fc, outLocation + os.sep + FCACTION_LINE, schemaType, fieldMappings, subtype)
               
