from PyQt5.QtWidgets import QDialog
from NewWindow import *

class PARTICLESDialog(QDialog):
    def __init__(self, ui):

        self.ui = ui # Ui_SCOPI_Dialog()

        self.ParticleString = ""
        self.NbPartTot = 0

        self.ui.ParticleAddButton.clicked.connect(lambda : self.Add())
        self.ui.ParticleClearButton.clicked.connect(lambda : self.clear())
        self.ui.ParticleSeeButton.clicked.connect(lambda : self.see())


    def Add(self):
        self.ParticleString += str(self.ui.ParticleGPEName.toPlainText())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleGPE.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleNBPart.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleRmin.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleRmax.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleMtype.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleMdense.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleMval.value())
        
        if self.ui.ParticleInitUniform.isChecked():
            self.ParticleString += " 0 "
        else:
            self.ParticleString += " 1 "
            
        self.ParticleString += str(self.ui.ParticleSeed.value())
        
        if self.ui.ParticleTypegrowingNo.isChecked():
            self.ParticleString += " 0 "
        else:
            self.ParticleString += " 1 "
            
        self.ParticleString += str(self.ui.ParticleGrowingcoef.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.Particlexmin.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.Particlexmax.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.Particleymin.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.Particleymax.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.Particlezmin.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.Particlezmax.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleUx.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleUy.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleUz.value())
        
        if self.ui.ParticleRotationNo.isChecked():
            self.ParticleString += " 0 0 0 0 0 0 0 0"
        else:
            self.ParticleString += " 1 "
            self.ParticleString += str(self.ui.ParticleAngle.value())
            self.ParticleString += " "
            self.ParticleString += str(self.ui.ParticleAngleX.value())
            self.ParticleString += " "
            self.ParticleString += str(self.ui.ParticleAngleY.value())
            self.ParticleString += " "
            self.ParticleString += str(self.ui.ParticleAngleZ.value())
            self.ParticleString += " "
            self.ParticleString += str(self.ui.ParticleOmegax.value())
            self.ParticleString += " "
            self.ParticleString += str(self.ui.ParticleOmegay.value())
            self.ParticleString += " "
            self.ParticleString += str(self.ui.ParticleOmegaz.value())

        if self.ui.ParticleRbmin.value()>0.0 and self.ui.ParticleRcmin.value()>0.0:
            self.ParticleString += " 1 "
        else:
            self.ParticleString += " 0 "
            
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleRbmin.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleRbmax.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleRcmin.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleRcmax.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleVision.value())
        self.ParticleString += " "
        self.ParticleString += str(self.ui.ParticleDistancesociale.value())
        self.ParticleString += "\n"

        self.NbPartTot += self.ui.ParticleNBPart.value()

    def clear(self):
        self.ParticleString = ""
        self.NbPartTot = 0

    def see(self):
        self._new_window = NewWindow(self.ParticleString)
        self._new_window.show()
        
    def writeParticlesData(self):
        Part  = "================================\n" 
        Part += "PARTICLES : gpe_name gpe partnb rmin rmax mtype mdens mval typeinit(0=unif, 1=random) seed typegrowing(0=no, 1=yes) parameters \n" 
        Part += "	  // mass=(1-mtype)*m+mtype*mdens*Vol //\n"
        Part += "	  // parameters : growing_coef xmin xmax ymin ymax zmin zmax uinit(3) with_rot rot_angle(rad) rot_vec(3) omega(3) isellipse(0=no, 1=yes) rbmin rbmax rcmin rcmax vision(en degre) distance_sociale\n"
        Part += "================================\n"
        Part += "\n"
        Part += self.ParticleString
        Part += "->PART_END<-  //!!!pour cesser la lecture des particules, a ne pas supprimer!!!\n"
        Part += "\n"

        return Part
