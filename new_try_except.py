# -*- coding: utf-8 -*-
import collections
import os,sys
import arcpy
import arcgisscripting
import traceback


#Import modules and create the geoprocessor objectimport arcgisscripting, os  

# Start a blank list for Polygon files, Point files, Line files 
gp=arcgisscripting.create()
# Set the workspace  
gp.workspace = (u"E:\\merge_by_geom\\ESYE\\YPOLOIPH_ELLADA_2011\\Ν. ΚΕΦΑΛΛΗΝΙΑΣ")

polygList = []
pointList = []  
lineList = []
polylineList = []

polygshapefile = "E:\\merge_by_geom\\dest_new\\Mergedpolyg.shp"
pointshapefile = "E:\\merge_by_geom\\dest_new\\Mergedpoint.shp"
lineshapefile = "E:\\merge_by_geom\\dest_new\\Mergedline.shp"
polylineshapefile = "E:\\merge_by_geom\\dest_new\\Mergedpolyline.shp"

# For each subdirectory  

'''
def TypeError():
    msg = arcpy.GetMessages(2)
    arcpy.AddError(msg)
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    #
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # Return python error messages for use in script tool or Python Window
    #
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python Window
    #
    print pymsg + "\n"
    print msgs
'''      

for dirname, dirnames, filenames in os.walk(gp.workspace):
    for filename in filenames:          
            # Get only files that end with .shp  
            if (filename.endswith(".shp")):  
                desc = gp.Describe(dirname + '\\' + filename) 
                shpType = desc.ShapeType
                if shpType == "Polygon":
                    polygpath = polygList.append(os.path.join(dirname, filename))
                    polygshpList = '"'+';'.join(polygList)+'"'
                    
                #if shpType == "Point":
                    #pointPath = pointList.append(os.path.join(dirname, filename))
                    #pointshpList = '"'+';'.join(pointList)+'"'
                #if shpType == "Line":
                    #linePath = lineList.append(os.path.join(dirname, filename))
                    #lineshpList = '"'+';'.join(lineList)+'"'
                #if shpType == "Polyline":
                    #polylinePath = polylineList.append(os.path.join(dirname, filename))

                    #polylineshpList = '"'+';'.join(polylineList)+'"'
try:
        
    gp.merge_management(polygshpList, polygshapefile)
                    #gp.merge_management(pointshpList, pointshapefile)
                    #gp.merge_management(lineshpList, lineshapefile) 
                    #gp.merge_management(polylineshpList, polylineshapefile)
    print gp.getMessages()      
    
   
                        #msg = gp.getMessage(2)
                        #gp.addmessage()
except Exception, ex:
        print "ERROR"
        print polygList[-2:] 
        print gp.getMessages()
        continue
print "\nDone."

                        #print dirname + '\\' + filename
                        #pass 
                                    
                        #print arcpy.AddError(e.message)
                                      

# Get the traceback object
#
#print gp.getMessages()
#msg = gp.getMessages
#gp.addmessage(msg)
#print "\n *** ERROR: Shapefiles (Polygons) failed to merge *** \n" 
#print "\n *** ERROR: Shapefiles (Points) failed to merge *** \n"
#print "\n *** ERROR: Shapefiles (Lines) failed to merge *** \n"
#print "\n *** ERROR: Shapefiles (Polylines) failed to merge *** \n"