# -*- coding: utf-8 -*-
import arcpy
from arcpy import env
import os
import os.path
import sys
import traceback

if (arcpy.Exists(u"G:\\jpgs\\bb_report.csv")):
    arcpy.Delete_management(u"G:\\jpgs\\bb_report.csv")
    f = open(u"G:\\jpgs\\bb_report.csv","w")
else:
    f = open(u"G:\\jpgs\\bb_report.csv","w")
if (arcpy.Exists(u"G:\\jpgs\\bb_report_error.csv")):
    arcpy.Delete_management(u"G:\\jpgs\\bb_report_error.csv")
    fe = open(u"G:\\jpgs\\bb_report_error.csv","w")
else:
    fe = open(u"G:\\jpgs\\bb_report_error.csv","w")
# rootdir = u"M:\\SCANS_GEO\\DHPE_SCANS"
rootdir = u"G:\\jpgs"
fullist=[]
# out_path = u"C:\\poly_bbs"
out_path = u"G:\\jpgs"
out_name = "poly_bbs.shp"
geometry_type = "POLYGON"
fieldName = "FILENAME"
fieldLength = 255
if (arcpy.Exists(u"G:\\jpgs\\poly_bbs.shp")):
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.cpg")
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.dbf")
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.sbn")
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.sbx")
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.shp")
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.shp.xml")
    arcpy.Delete_management(u"G:\\jpgs\\poly_bbs.shx")
    npoly = arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, "", "", "", "")
    arcpy.AddField_management(npoly, fieldName, "TEXT","","", fieldLength)
else :
    npoly = arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, "", "", "", "")
    arcpy.AddField_management(npoly, fieldName, "TEXT","","", fieldLength)
for root, dirs, files in os.walk(rootdir):
    for filename in files:
        if filename.endswith(".jpg"):
            fullist.append(os.path.join(root, filename))
# print fullist
for fulli in fullist:
    try:
        desc= arcpy.sa.Raster(fulli)
        myExtent = desc.extent
        #Array to hold points
        array = arcpy.Array()
        #Create the bounding box
        array.add(myExtent.lowerLeft)
        array.add(myExtent.lowerRight)
        array.add(myExtent.upperRight)
        array.add(myExtent.upperLeft)
        #ensure the polygon is closed
        array.add(myExtent.lowerLeft)
        # Create the polygon object
        polyin = arcpy.Polygon(array)
        array.removeAll()
        inscursor = arcpy.da.InsertCursor(npoly,("SHAPE@","FILENAME"))
        inscursor.insertRow((polyin,fulli))
        f.write(fulli +"\n")
        print "\nCurrent Filename is " +  fulli
        del inscursor
    except Exception, e:
        print e
#         fe.write(sys.stdout.buffer.write(e.encode("utf8")))
        fe.write(str(e).decode("utf-8") +"\n")
        continue