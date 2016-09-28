import PARAMDialog, VAPDialog, GEOMDialog, FORCESDialog, VISUDialog


class DataGenerate(PARAMDialog.PARAMDialog, VAPDialog.VAPDialog, GEOMDialog.GeometryDialog, FORCESDialog.ForcesDialog, VISUDialog.VisualisationDialog):
    def __init__(self, ui):
        super(DataGenerate, self).__init__(ui)

        self.ui = ui # Ui_SCOPI_Dialog()
        
        self.PARAM  = PARAMDialog.PARAMDialog(self.ui)
        self.VAP    = VAPDialog.VAPDialog(self.ui)
        self.GEOM   = GEOMDialog.GeometryDialog(self.ui)
        self.FORCES = FORCESDialog.ForcesDialog(self.ui)
        self.VISU   = VISUDialog.VisualisationDialog(self.ui)
        
        self.ui.GenerateDataFile.clicked.connect(lambda : self.writeDataFile())

        
    def writeDataFile(self):
        data = open("data", "w")
        data.write(self.PARAM.writeContinuousProblemData())
        data.write(self.VAP.writeVAPData())
        data.write(self.GEOM.writeGeomData())
        data.write(self.FORCES.writeForcesData())
        data.write(self.VISU.writeVisualisationData())
        data.write(self.PARAM.writeDiscreteProblemData())
        data.close()












        
