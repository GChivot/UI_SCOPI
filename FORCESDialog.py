from PyQt5.QtWidgets import QDialog

class ForcesDialog(QDialog):
    
    def __init__(self, ui):

        self.ui = ui # Ui_SCOPI_Dialog()

        self.ui.ForceGravity.toggled.connect(self.ui.ForceGravityWidget.setEnabled)
        self.ui.ForceAlea.toggled.connect(self.ui.ForceAleaWidget.setEnabled)
        self.ui.ForceCoh.toggled.connect(self.ui.ForceCohWidget.setEnabled)
        self.ui.ForceCohmacro.toggled.connect(self.ui.ForceCohmacroWidget.setEnabled)
        self.ui.ForceCismacro.toggled.connect(self.ui.ForceCismacroWidget.setEnabled)
        self.ui.ForceExtfield.toggled.connect(self.ui.ForceExtfieldWidget.setEnabled)
        self.ui.ForcePlanete.toggled.connect(self.ui.ForcePlaneteWidget.setEnabled)
        self.ui.ForceAttraction.toggled.connect(self.ui.ForceAttractionWidget.setEnabled)
        self.ui.ForceFriction.toggled.connect(self.ui.ForceFrictionWidget.setEnabled)


    def writeForcesData(self):
        ForcesData  = "================================\n"
        ForcesData += "FORCES : name type run(0=no) parameters\n"
        ForcesData += "================================\n"
        ForcesData += "\n"
        ForcesData += "12       Number of type of forces\n"
        ForcesData += "11       Max. number of parameters for the forces\n"
        
        ForcesData += "gravity      "
        if self.ui.ForceGravity.isChecked():
            ForcesData += "1    1     "
            ForcesData += str(self.ui.ForceGravityGx.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceGravityGy.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceGravityGz.value())
            ForcesData += "    0   0   0   0   0   0   0  0 (gx gy gz)\n"
        else:
            ForcesData += "0    1     0   0    0    0   0   0   0   0   0   0  0 (gx gy gz)\n"

        ForcesData += "alea	      "
        if self.ui.ForceAlea.isChecked():
            ForcesData += "1    2     "
            ForcesData += str(self.ui.ForceAleaC.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAleaA.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAleaB.value())
            ForcesData += "    0   0   0   0   0   0   0  0 (c a b)\n"
        else:
           ForcesData += "0    2     0    0    0    0   0   0   0   0   0   0  0 (c a b)\n"

        ForcesData += "coh 	      "
        if self.ui.ForceCoh.isChecked():
            ForcesData += "1    3     "
            ForcesData += str(self.ui.ForceCohCohst.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohCoha.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohCohb.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohCohc.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohCohdr.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohCohstart.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohCohend.value())
            ForcesData += " 0   0   0  0 (coh_st,coh_a,coh_b,coh_c,coh_dr,coh_start,coh_end)\n"
        else:
            ForcesData += "0    3     0    0    0    0   0   0   0   0   0   0  0 (coh_st,coh_a,coh_b,coh_c,coh_dr,coh_start,coh_end)\n"

        ForcesData += "coh_macro     "
        if self.ui.ForceCohmacro.isChecked():
            ForcesData += "1    4     "
            ForcesData += str(self.ui.ForceCohmacroCoha.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohmacroCohb.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohmacroCohc.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohmacroCohd.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCohmacroCohangle.value())
            ForcesData += "     "
            ForcesData += "0   0   0   0   0  0 (coh_a,coh_b,coh_c,coh_d,coh_angle)\n"
        else:
            ForcesData += "0    4     0    0    0    0   0   0   0   0   0   0  0 (coh_a,coh_b,coh_c,coh_d,coh_angle)\n"

        ForcesData += "cis_macro     "
        if self.ui.ForceCismacro.isChecked():
            ForcesData += "1    5     "
            ForcesData += str(self.ui.ForceCismacroPtax.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroPtay.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroPtaz.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroPtbx.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroPtby.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroPtbz.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroEx.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroEy.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroEz.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroUf.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceCismacroUf.value())
            ForcesData += " (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"
        else:
            ForcesData += "0    5     0    0    0    0   0   0   0   0   0   0  0 (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"

        if self.ui.ForceCisailmacro.isChecked():
            ForcesData += "cis_macro     1    7     0    0    0    0   0.5 0   1   0   0   1  1 (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"
        else:
            ForcesData += "cis_macro     0    7     0    0    0    0   0.5 0   1   0   0   1  1 (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"

        if self.ui.ForcePoiseuille.isChecked():
            ForcesData += "poiseuille    1	   8	 0    0	   0	0   0	0   0	0   0	0  0\n"
        else:
            ForcesData += "poiseuille    0	   8	 0    0	   0	0   0	0   0	0   0	0  0\n"

        ForcesData += "ext_field     "
        if self.ui.ForceExtfield.isChecked():
            ForcesData += "1    9     "
            ForcesData += str(self.ui.ForceExtfieldFilenumber.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceExtfieldCoef.value())
            ForcesData += "     "
            ForcesData += "0    0   0   0   0   0   0   0  0 (file_number, coef)\n"
        else:
            ForcesData += "0	   9     0    0	   0    0   0   0   0   0   0   0  0 (file_number, coef)\n"

        ForcesData += "planete	      "
        if self.ui.ForcePlanete.isChecked():
            ForcesData += "1    10     "
            ForcesData += str(self.ui.ForcePlaneteGrav.value())
            ForcesData += "     "
            ForcesData += "0     0    0   0     0   0   0   0   0  0 (grav)\n"
        else:
            ForcesData += "0	   10     0     0     0    0   0     0   0   0   0   0  0 (grav)\n"

        ForcesData += "attraction    "
        if self.ui.ForceAttraction.isChecked():
            ForcesData += "1    11     "
            ForcesData += str(self.ui.ForceAttractionCoef.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAttractionRadius.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAttractionTmax.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAttractionciblex.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAttractioncibley.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceAttractionciblez.value())
            ForcesData += "     "
            ForcesData += "0   0   0   0  0 (coef, radius, Tmax, cible_x, cible_y, cible_z)\n"
        else:
            ForcesData += "0	  11     0    0    0    0   0   0   0   0   0   0  0 (coef, radius, Tmax, cible_x, cible_y, cible_z)\n"

        if self.ui.ForceLubrification.isChecked():
            ForcesData += "lubrication   1   12     0    0    0    0   0   0   0   0   0   0  0 (no param at all)\n"
        else:
            ForcesData += "lubrication   0   12     0    0    0    0   0   0   0   0   0   0  0 (no param at all)\n"

        ForcesData += "friction_tang   "
        if self.ui.ForceFriction.isChecked():
            ForcesData += "1    15     "
            ForcesData += str(self.ui.ForceFrictionKt.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceFrictionMut.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceFrictionKsit.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceFrictionKr.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceFrictionMur.value())
            ForcesData += "     "
            ForcesData += str(self.ui.ForceFrictionKsir.value())
            ForcesData += "     "
            ForcesData += "0   0   0   0  0 (kt,mut,ksit,kr,mur,ksir)\n"
        else:
            ForcesData += "0   12     0    0    0    0   0   0   0   0   0   0  0 (kt,mut,ksit,kr,mur,ksir)\n"
            
        ForcesData += "\n"

        return ForcesData

            
