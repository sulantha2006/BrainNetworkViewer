__author__ = 'sulantha'
import wx
from View.BrainNetworkViewer import BrainNetworkViewer
from Model.BrainNetworkModel import BrainNetworkModel


class BrainNetworkControl():
    def __init__(self):
        pass

    def readTemplateFile(self, filePath):
        pass

    def setTemplateInModel(self, templateData, templateDataLoc):
        if templateDataLoc == 'l':
            pass
        elif templateDataLoc == 'r':
            pass
        elif templateDataLoc == 'f':
            pass

    def readSurfaceFile(self, filePath):
        pass

    def setSurfaceInModel(self, surfaceData, surfaceDataLoc):
        if surfaceDataLoc == 'l':
            pass
        elif surfaceDataLoc == 'r':
            pass
        elif surfaceDataLoc == 'f':
            pass

    def readNodesFile(self, filePath):
        pass

    def setNodesInModel(self, nodesData):
        pass

    def readEdgesFile(self, filePath):
        pass

    def setEdgesInModel(self, edgesData):
        pass