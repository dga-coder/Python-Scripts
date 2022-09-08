import os
import csv



f = open('C:\\Users\\galionis.ELPHODOMAIN\\Desktop\\DSM.csv','w')
startpath = 'S:\\FROM_DHPE\\KTIMATOLOGIO\\DSM'

a = os.walk(startpath)
 
for root, dirs, files in a:
    for filename in files:
        if filename.endswith('.img'):
            f.write(root+';'+filename +'\n')

'''
print "Root directory: %s" % (root)   
'''
