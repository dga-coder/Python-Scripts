import sys
import math
import os

sys.path.extend([r"C:\Program Files (x86)\QGIS Dufour\apps\Python27",r"C:\Program Files (x86)\QGIS Dufour\apps\qgis\bin"])
sys.path.reverse()




class Create_vlayer(object):
    def __init__(self,nom,type):
        self.type=type
        self.name = nom
        self.layer = QgsVectorLayer("C:\Users\galionis.ELPHODOMAIN\Desktop\test_distance\galionis.shp", "galio" , "memory")
        if not self.layer.isValid():
            print "Layer failed to load!"
        self.pr =self.layer.dataProvider() 
    def create_point(self,geometry):
        self.seg = QgsFeature()
        self.seg.setGeometry(QgsGeometry.fromPoint(geometry))
        self.pr.addFeatures([self.seg])
        self.layer.updateExtents()
    def display_layer(self):
        QgsMapLayerRegistry.instance().addMapLayers([self.couche])
    
    
    def mag(point):
        # magnitude of a vector
        return math.sqrt(point.x()**2 + point.y()**2)
    def diff(point2, point1):
        # substraction betwen two vector
        return QgsPoint(point2.x()-point1.x(), point2.y() - point1.y())
    def length(point1,point2):
    # with PyQGIS: sqrDist
        return math.sqrt(point1.sqrDist(point2))
    
    
    
    

    def length(point1,point2):
        return math.sqrt(point1.sqrDist(point2))
    
    
    
    
    def dircos(point):
        cosa = point.x() / mag(point)
        cosb = point.y()/ mag(point)
        return cosa,cosb