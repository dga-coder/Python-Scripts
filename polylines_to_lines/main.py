from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
#from processing.core.GeoAlgorithm import GeoAlgorithm
#from processing.core.parameters import ParameterVector
#from processing.core.outputs import OutputVector
#from processing.tools import dataobjects, vector


class Explode(GeoAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def processAlgorithm(self, progress):
        vlayer = dataobjects.getObjectFromUri(
                self.getParameterValue(self.INPUT))
        output = self.getOutputFromName(self.OUTPUT)
        vprovider = vlayer.dataProvider()
        fields = vprovider.fields()
        writer = output.getVectorWriter(fields, QGis.WKBLineString,
                vlayer.crs())
        outFeat = QgsFeature()
        inGeom = QgsGeometry()
        nElement = 0
        features = vector.features(vlayer)
        nFeat = len(features)
        for feature in features:
            nElement += 1
            progress.setPercentage(nElement * 100 / nFeat)
            inGeom = feature.geometry()
            atMap = feature.attributes()
            segments = self.extractAsSingleSegments(inGeom)
            outFeat.setAttributes(atMap)
            for segment in segments:
                outFeat.setGeometry(segment)
                writer.addFeature(outFeat)
        del writer

    def extractAsSingleSegments(self, geom):
        segments = []
        if geom.isMultipart():
            multi = geom.asMultiPolyline()
            for polyline in multi:
                segments.extend(self.getPolylineAsSingleSegments(polyline))
        else:
            segments.extend(self.getPolylineAsSingleSegments(
                    geom.asPolyline()))
        return segments

    def getPolylineAsSingleSegments(self, polyline):
        segments = []
        for i in range(len(polyline) - 1):
            ptA = polyline[i]
            ptB = polyline[i + 1]
            segment = QgsGeometry.fromPolyline([ptA, ptB])
            segments.append(segment)
        return segments

    def defineCharacteristics(self):
        self.name = 'Explode lines'
        self.group = 'Vector geometry tools'
        self.addParameter(ParameterVector(self.INPUT, 'Input layer',
                          [ParameterVector.VECTOR_TYPE_LINE]))
        self.addOutput(OutputVector(self.OUTPUT, 'Output layer'))