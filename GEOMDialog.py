from PyQt5.QtWidgets import QDialog

class GeometryDialog(QDialog):

    def __init__(self, ui):

        self.ui = ui # Ui_SCOPI_Dialog()

        self.ui.GeomPeriodic.toggled.connect(self.ui.GeomPeriodicityWidget.setEnabled)
        
        self.ui.GeomXAxisPeriodicity.toggled.connect(self.ui.GeomXwidget.setEnabled)
        self.ui.GeomYAxisPeriodicity.toggled.connect(self.ui.GeomYwidget.setEnabled)
        self.ui.GeomZAxisPeriodicity.toggled.connect(self.ui.GeomZwidget.setEnabled)

        self.ui.GeomNonPeriodic.toggled.connect(lambda : self.unchecked(self.ui.GeomXAxisPeriodicity))
        self.ui.GeomNonPeriodic.toggled.connect(lambda : self.unchecked(self.ui.GeomYAxisPeriodicity))
        self.ui.GeomNonPeriodic.toggled.connect(lambda : self.unchecked(self.ui.GeomZAxisPeriodicity))

        self.ui.GeomCrowd.toggled.connect(lambda : self.unchecked(self.ui.GeomXAxisPeriodicity))
        self.ui.GeomCrowd.toggled.connect(lambda : self.unchecked(self.ui.GeomYAxisPeriodicity))
        self.ui.GeomCrowd.toggled.connect(lambda : self.unchecked(self.ui.GeomZAxisPeriodicity))
        
    def checked(self, dialog):
        dialog.setChecked(True)

    def unchecked(self,dialog):
        dialog.setChecked(False)

    def writeGeomData(self):
        GeomData  = "================================\n"
        GeomData += "GEOMETRY : name type parameters\n"
        GeomData += "           NonPer    1\n"
        GeomData += "           Per       2   is_per_x,per_xmin,per_xmax,per_gamptx is_per_y,per_ymin,per_ymax,per_gampty  is_per_z,per_zmin,per_zmax,per_gamptz\n"
        GeomData += "           Crowd     3\n"
        GeomData += "================================\n"
        GeomData += "\n"

        if self.ui.GeomNonPeriodic.isChecked():
            GeomData += "NonPer   1\n"

        if self.ui.GeomCrowd.isChecked():
            GeomData += "Crowd   3\n"

        if self.ui.GeomPeriodic.isChecked():
            GeomData += "Per   1     "
            if self.ui.GeomXAxisPeriodicity.isChecked():
                GeomData += str(self.ui.GeomXmin.value())
                GeomData += " "
                GeomData += str(self.ui.GeomXmax.value())
                GeomData += " "
                GeomData += str(self.ui.GeomGamptx.value())
                GeomData += " "
            else:
                GeomData += "0 0 0 "

            if self.ui.GeomYAxisPeriodicity.isChecked():
                GeomData += str(self.ui.GeomYmin.value())
                GeomData += " "
                GeomData += str(self.ui.GeomYmax.value())
                GeomData += " "
                GeomData += str(self.ui.GeomGampty.value())
                GeomData += " "
            else:
                GeomData += "0 0 0 "

            if self.ui.GeomZAxisPeriodicity.isChecked():
                GeomData += str(self.ui.GeomZmin.value())
                GeomData += " "
                GeomData += str(self.ui.GeomZmax.value())
                GeomData += " "
                GeomData += str(self.ui.GeomGamptz.value())
                GeomData += " "
            else:
                GeomData += "0 0 0 "
        GeomData += "\n"

        return GeomData
