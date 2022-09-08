# -*- coding: utf-8 -*-
import arcpy,os
import arcpy
from arcpy import env
import arcgisscripting

poaList = []
in_workspace = u"D:\\POA_vs_CSL\\POA"
arcpy.env.workspace = u"D:\\POA_vs_CSL\\POA"
f = open("D:\\POA_vs_CSL\\POA\\POATYPEFIELD.csv","w")
count =0 
for dirpath, dirnames, filenames in arcpy.da.Walk(in_workspace, datatype="FeatureClass", type="ALL"):
    for filename in filenames:
        if (filename.endswith("POA.shp")):
            count +=1
            f.write(dirpath + '\\' + filename +'\n')
            poaList.append(os.path.join(dirpath, filename))
            for poali in poaList:
                uprows = arcpy.da.UpdateCursor(poali,("POA_TYPE","TYP_DESCR"))
                uprow = uprows.next()
                for uprow in uprows:
                    if (uprow[0] == "1"):    uprow[1] = "Οριο βλάστησης"
                    elif ( uprow[0] == "2" ):    uprow[1] = "Ιχνος μέγιστης ανάβασης κύματος"
                    elif ( uprow[0] == "3" ):    uprow[1] = "Στέψη  πρανούς"
                    elif ( uprow[0] == "4" ):    uprow[1] = "Στέψη  κρηπιδώματος ή  τεχνικού έργου"
                    elif ( uprow[0] == "5" ):    uprow[1] = "Γραμμή δόμησης"
                    elif ( uprow[0] == "6" ):    uprow[1] = "Αραιοδομημένες περιοχές"
                    elif ( uprow[0] == "7" ):    uprow[1] = "Δέλτα ποταμών,περιοχές εκροών ρεμάτων και χειμάρρων"
                    elif ( uprow[0] == "8" ):    uprow[1] = "Αλυκές και λιμνοθάλασσες χωρίς επικοινωνία"
                    elif ( uprow[0] == "9" ):    uprow[1] = "Αλυκές και λιμνοθάλασσες  με ελεύθερη-συνεχή επικοινωνία"
                    elif ( uprow[0] == "10" ):   uprow[1] = "Λοιπά κριτήρια"    
                    #else:    pass
                    uprows.updateRow(uprow)
            print "\nNumber of rows updated are " + str(sum(1 for row in uprows))
            del uprow, uprows