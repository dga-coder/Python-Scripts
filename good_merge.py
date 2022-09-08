import collections
import os

import arcpy

shape_files = collections.defaultdict(list)


root = arcpy.GetParameterAsText(0)
dest_path = arcpy.GetParameterAsText(1)


##fileList = []
##fileSize = 0
##folderCount = 0

root = 'D:\\esye_root'
dest_path = 'D:\\esye_dest'
    

for r, d, f in os.walk(root):
    shapes = filter(lambda x: x.lower().endswith('topo.shp'), f)
    for shape_file in shapes:
        shape_files[shape_file].append(os.path.join(r, shape_file))

for file_name, file_list in shape_files.iteritems():
    arcpy.Merge_management(file_list, os.path.join(dest_path, file_name))
    print '%s: %r' % (file_name, file_list)