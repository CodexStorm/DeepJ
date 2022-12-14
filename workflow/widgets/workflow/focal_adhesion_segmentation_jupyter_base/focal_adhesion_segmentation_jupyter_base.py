import os
import glob
import sys
import functools
import jsonpickle
from collections import OrderedDict
from Orange.widgets import widget, gui, settings
import Orange.data
from Orange.data.io import FileFormat
from DockerClient import DockerClient
from BwBase import OWBwBWidget, ConnectionDict, BwbGuiElements, getIconName, getJsonName
from PyQt5 import QtWidgets, QtGui

class OWfocal_adhesion_segmentation_jupyter_base(OWBwBWidget):
    name = "focal_adhesion_segmentation_jupyter_base"
    description = "Base installation of Jupyter"
    priority = 103
    icon = getIconName(__file__,"jupyter_image.png")
    want_main_area = False
    docker_image_name = "biodepot/jupyter"
    docker_image_tag = "5.6.0__ubuntu-18.04__firefox-61.0.1__081318"
    inputs = [("InputDir",str,"handleInputsInputDir"),("outlineTrigger",str,"handleInputsoutlineTrigger"),("startingNotebook",str,"handleInputsstartingNotebook"),("segmentTrigger",str,"handleInputssegmentTrigger"),("timeout",str,"handleInputstimeout")]
    outputs = [("OutputDir",str),("outputNotebook",str)]
    pset=functools.partial(settings.Setting,schema_only=True)
    runMode=pset(0)
    exportGraphics=pset(False)
    runTriggers=pset([])
    triggerReady=pset({})
    inputConnectionsStore=pset({})
    optionsChecked=pset({})
    subcommand=pset("notebook")
    startingNotebook=pset(None)
    type=pset("notebook")
    timeout=pset(-1)
    outputNotebook=pset(None)
    debug=pset(False)
    generateConfig=pset(False)
    autoyes=pset(True)
    allowRoot=pset(True)
    loglevel=pset("30")
    ip=pset("0.0.0.0")
    port=pset(8888)
    config=pset(None)
    transport=pset(None)
    keyfile=pset(None)
    certfile=pset(None)
    clientca=pset(None)
    nomathjax=pset(False)
    browser=pset(None)
    execute=pset(False)
    def __init__(self):
        super().__init__(self.docker_image_name, self.docker_image_tag)
        with open(getJsonName(__file__,"focal_adhesion_segmentation_jupyter_base")) as f:
            self.data=jsonpickle.decode(f.read())
            f.close()
        self.initVolumes()
        self.inputConnections = ConnectionDict(self.inputConnectionsStore)
        self.drawGUI()
    def handleInputsInputDir(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("InputDir", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsoutlineTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("outlineTrigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputsstartingNotebook(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("startingNotebook", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputssegmentTrigger(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("segmentTrigger", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleInputstimeout(self, value, *args):
        if args and len(args) > 0: 
            self.handleInputs("timeout", value, args[0][0], test=args[0][3])
        else:
            self.handleInputs("inputFile", value, None, False)
    def handleOutputs(self):
        outputValue=None
        if hasattr(self,"OutputDir"):
            outputValue=getattr(self,"OutputDir")
        self.send("OutputDir", outputValue)
        outputValue=None
        if hasattr(self,"outputNotebook"):
            outputValue=getattr(self,"outputNotebook")
        self.send("outputNotebook", outputValue)
