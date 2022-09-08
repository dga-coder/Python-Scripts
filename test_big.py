# -*- coding: utf-8 -*-
import collections
import os,sys
import arcpy
import arcgisscripting

#Import modules and create the geoprocessor objectimport arcgisscripting, os  

gp=arcgisscripting.create()
# Set the workspace  
gp.workspace = ("E:\merge_by_geom\ESYE\ΝΟΜΟΣ ΑΤΤΙΚΗΣ_2011\Afidnai")
# Start a blank list for Polygon files  
polyList = []  
# Start a blank list for Point files  
pointList = []  
#Start a blank list for the Line files  
lineList = []
# For each subdirectory  
for dir in os.listdir(gp.workspace):  
    if os.path.isdir(gp.workspace+"/"+dir):  
        # Get a list of the files in each directory  
        files = os.listdir(gp.workspace+"/"+dir)      
        # For each file in a given directory  
        for file in files:          
            # Get only files that end with .shp  
            if (file.endswith(".shp")):  
                print file  
                # Describe feature class  
                desc = gp.Describe(gp.workspace+"/"+dir+"/"+file)  
                type = desc.ShapeType  
                #print dir+"/"+file + " type is: " + type             
                if type == "Polygon":  
                    print dir+"/"+file + " is Polygon"  
                    polyPath = polyList.append(dir+"/"+file)  
                if type == "Point":  
                    print dir+"//"+file + " is Point"  
                    pointPath = pointList.append(dir+"/"+file)  
                if type == "Line":  
                    print dir+"/"+file + " is Line"  
                    linePath = lineList.append(dir+"/"+file) 
# Hard-code the output merged shapefile names  
                    polyshapefile = "Mergedpoly.shp"  
                    pointshapefile = "Mergedpoint.shp"  
                    lineshapefile = "Mergedline.shp"            
# Given a list of shapefiles, separate each by a ";"  
# and put quotes around the whole thing  
                    def polyshpList(polyPath):  
                                return '"%s"' % ';'.join(polyList)  
                    def pointshpList(pointPath):  
                                return '"%s"' % ';'.join(pointList)  
                    def lineshpList(linePath):  
                                return'"%s"' % ";".join(lineList)
# Set the variable to the newly formatted list of shapefiles              
                    polymergedlist = polyshpList(polyPath)  
                    pointmergedlist = pointshpList(pointPath)  
                    linemergedlist = lineshpList(linePath)
# Polygons            
try:  
    print "\nMerging " + polymergedlist + " to get " + polyshapefile + "...\n"      
    gp.merge_management(polymergedlist, polyshapefile)  
    #gp.clip_analysis("Mergedpoly.shp", "E:\\merge_by_geom\\dest\\CANADAOUTLINEMA1.shp", gp.workspace, ".000001")  
    print gp.getMessages()      
except:  
    print gp.getMessages()  
    print "\n *** ERROR: Shapefiles (Polygon) failed to merge *** \n"# Points  
try:  
    print "\nMerging " + pointmergedlist + " to get " + pointshapefile + "...\n"      
    gp.merge_management(pointmergedlist, pointshapefile)  
    #gp.clip_analysis("Mergedpoint.shp", "E:\\merge_by_geom\\dest\\CANADAOUTLINEMA2.shp", gp.workspace, ".000001")  
    print gp.getMessages()      
except:  
    print gp.getMessages()  
    print "\n *** ERROR: Shapefiles (Point) failed to merge *** \n"    # Lines  
try:  
    print "\nMerging " + linemergedlist + " to get " + lineshapefile + "...\n"      
    gp.merge_management(linemergedlist, lineshapefile)  
    #gp.clip_analysis("Mergedline.shp", "E:\\merge_by_geom\\dest\\CANADAOUTLINEMA3.shp", gp.workspace, ".000001")  
    print gp.getMessages()      
except:  
    print gp.getMessages()  
    print "\n *** ERROR: Shapefiles (Line) failed to merge *** \n"    
print "\nDone."  