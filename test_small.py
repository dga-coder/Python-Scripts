import collections
import os
import arcgisscripting
import arcpy

shape_files = collections.defaultdict(list)


root = arcpy.GetParameterAsText(0)
dest_path = arcpy.GetParameterAsText(1)


##fileList = []
##fileSize = 0
##folderCount = 0

root = 'E:\merge_by_geom\ESYE'
dest_path = 'E:\merge_by_geom\dest'
gp=arcgisscripting.create()
gp.workspace = ("E:\merge_by_geom\ESYE")

# Start a blank list for Polygon files  
polyList = []  
# Start a blank list for Point files  
pointList = []  
#Start a blank list for the Line files  
lineList = []
    

for r, d, f in os.walk(root):
    shapes = filter(lambda x: x.lower().endswith('.shp'), f)
    #desc = gp.Describe(gp.workspace+"/"+ dir +"/" + file)  
    type = shapes.ShapeType
    for shape_file in shapes:
            if type == "Polygon":  
                print dir+"/"+file + " is Polygon" 
                shape_files[shape_file].append(os.path.join(r, shape_file))
                for file_name, file_list in shape_files.iteritems():
                    arcpy.Merge_management(file_list, os.path.join(dest_path, file_name))
                    print '%s: %r' % (file_name, file_list) 
                #polyPath = polyList.append(dir+"/"+file)  
            if type == "Point":  
                print dir+"//"+file + " is Point" 
                shape_files[shape_file].append(os.path.join(r, shape_file))
                for file_name, file_list in shape_files.iteritems():
                    arcpy.Merge_management(file_list, os.path.join(dest_path, file_name))
                    print '%s: %r' % (file_name, file_list) 
                #pointPath = pointList.append(dir+"/"+file)  
            if type == "Line":  
                print dir+"/"+file + " is Line"  
                shape_files[shape_file].append(os.path.join(r, shape_file))
                for file_name, file_list in shape_files.iteritems():
                    arcpy.Merge_management(file_list, os.path.join(dest_path, file_name))
                    print '%s: %r' % (file_name, file_list)
                #linePath = lineList.append(dir+"/"+file)   