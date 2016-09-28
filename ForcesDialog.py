from PyQt5.QtWidgets import QDialog

class ForcesDialog(QDialog):
    
    def __init__(self, ui):

        self.ui = ui # Ui_SCOPI_Dialog()

        self.ui.ForceGravity.toggled.connect(self.ui.ForceGravityWidget.setEnabled)
        self.ui.ForceAlea.toggled.connect(self.ui.ForceAleaWidget.setEnabled)
        self.ui.ForceCoh.toggled.connect(self.ui.ForceCohWidget.setEnabled)
        self.ui.ForceCohmacro.toggled.connect(self.ui.ForceCohmacroWidget.setEnabled)
        self.ui.ForceCismacro.toggled.connect(self.ui.ForceCismacroWiget.setEnabled)
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
        if ForceGravity.isChecked():
            ForcesData += "1    1     "
            ForcesData += str(ForceGravityGx.value())
            ForcesData += "     "
            ForcesData += str(ForceGravityGy.value())
            ForcesData += "     "
            ForcesData += str(ForceGravityGz.value())
            ForcesData += "    0   0   0   0   0   0   0  0 (gx gy gz)\n"
        else:
            ForcesData += "0    1     0   0    0    0   0   0   0   0   0   0  0 (gx gy gz)\n"

        ForcesData += "alea	      "
        if ForceAlea.isChecked():
            ForcesData += "1    2     "
            ForcesData += str(ForceAleaC.value())
            ForcesData += "     "
            ForcesData += str(ForceAleaA.value())
            ForcesData += "     "
            ForcesData += str(ForceAleaB.value())
            ForcesData += "    0   0   0   0   0   0   0  0 (c a b)\n"
        else:
           ForcesData += "0    2     0    0    0    0   0   0   0   0   0   0  0 (c a b)\n"

        ForcesData += "coh 	      "
        if ForceCoh.isChecked():
            ForcesData += "1    3     "
            ForcesData += str(ForceCohCohst.value())
            ForcesData += "     "
            ForcesData += str(ForceCohCoha.value())
            ForcesData += "     "
            ForcesData += str(ForceCohCohb.value())
            ForcesData += "     "
            ForcesData += str(ForceCohCohc.value())
            ForcesData += "     "
            ForcesData += str(ForceCohCohdr.value())
            ForcesData += "     "
            ForcesData += str(ForceCohCohstart.value())
            ForcesData += "     "
            ForcesData += str(ForceCohCohend.value())
            ForcesData += " 0   0   0  0 (coh_st,coh_a,coh_b,coh_c,coh_dr,coh_start,coh_end)\n"
        else:
            ForcesData += "0    3     0    0    0    0   0   0   0   0   0   0  0 (coh_st,coh_a,coh_b,coh_c,coh_dr,coh_start,coh_end)\n"

        ForcesData += "coh_macro     "
        if ForceCohmacro.isChecked():
            ForcesData += "1    4     "
            ForcesData += str(ForceCohmacroCoha.value())
            ForcesData += "     "
            ForcesData += str(ForceCohmacroCohb.value())
            ForcesData += "     "
            ForcesData += str(ForceCohmacroCohc.value())
            ForcesData += "     "
            ForcesData += str(ForceCohmacroCohd.value())
            ForcesData += "     "
            ForcesData += str(ForceCohmacroCohangle.value())
            ForcesData += "     "
            ForcesData += "0   0   0   0   0  0 (coh_a,coh_b,coh_c,coh_d,coh_angle)\n"
        else:
            ForcesData += "0    4     0    0    0    0   0   0   0   0   0   0  0 (coh_a,coh_b,coh_c,coh_d,coh_angle)\n"

        ForcesData += "cis_macro     "
        if ForceCismacro.isChecked():
            ForcesData += "1    5     "
            ForcesData += str(ForceCismacroPtax.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroPtay.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroPtaz.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroPtbx.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroPtby.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroPtbz.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroEx.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroEy.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroEz.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroUf.value())
            ForcesData += "     "
            ForcesData += str(ForceCismacroUf.value())
            ForcesData += " (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"
        else:
            ForcesData += "0    5     0    0    0    0   0   0   0   0   0   0  0 (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"

        if ForceCisailmacro.isChecked():
            ForcesData += "cis_macro     0    7     0    0    0    0   0.5 0   1   0   0   1  1 (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"
        else:
            ForcesData += "cis_macro     1    7     0    0    0    0   0.5 0   1   0   0   1  1 (ptax,ptay,ptaz,ptbx,ptby,ptbz,ex,ey,ez,Uf,nu)\n"

        if ForcePoiseuille.isChecked():
            ForcesData += "poiseuille    1	   8	 0    0	   0	0   0	0   0	0   0	0  0\n"
        else:
            ForcesData += "poiseuille    0	   8	 0    0	   0	0   0	0   0	0   0	0  0\n"

        ForcesData += "ext_field     "
        if ForceExtfield.isChecked():
            ForcesData += "1    9     "
            ForcesData += str(ForceExtfieldFilenumber.value())
            ForcesData += "     "
            ForcesData += str(ForceExtfieldCoef.value())
            ForcesData += "     "
            ForcesData += "0    0   0   0   0   0   0   0  0 (file_number, coef)\n"
        else:
            ForcesData += "0	   9     0    0	   0    0   0   0   0   0   0   0  0 (file_number, coef)\n"

        ForcesData += "planete	      "
        if ForcePlanete.isChecked():
            ForcesData += "1    10     "
            ForcesData += str(ForcePlaneteGrav.value())
            ForcesData += "     "
            ForcesData += "0     0    0   0     0   0   0   0   0  0 (grav)\n"
        else:
            ForcesData += "0	   10     0     0     0    0   0     0   0   0   0   0  0 (grav)\n"

        ForcesData += "attraction    "
        if ForceAttraction.isChecked():
            ForcesData += "1    11     "
            ForcesData += str(ForceAttractionCoef.value())
            ForcesData += "     "
            ForcesData += str(ForceAttractionRadius.value())
            ForcesData += "     "
            ForcesData += str(ForceAttractionTmax.value())
            ForcesData += "     "
            ForcesData += str(ForceAttractionciblex.value())
            ForcesData += "     "
            ForcesData += str(ForceAttractioncibley.value())
            ForcesData += "     "
            ForcesData += str(ForceAttractionciblez.value())
            ForcesData += "     "
            ForcesData += "0   0   0   0  0 (coef, radius, Tmax, cible_x, cible_y, cible_z)\n"
        else:
            ForcesData += "0	  11     0    0    0    0   0   0   0   0   0   0  0 (coef, radius, Tmax, cible_x, cible_y, cible_z)\n"

        if ForceLubrification.isChecked():
            ForcesData += "lubrication   1   12     0    0    0    0   0   0   0   0   0   0  0 (no param at all)\n"
        else:
            ForcesData += "lubrication   0   12     0    0    0    0   0   0   0   0   0   0  0 (no param at all)\n"

        ForcesData += "friction_tang   "
        if ForceFriction.isChecked():
            ForcesData += "1    15     "
            ForcesData += str(ForceFrictionKt.value())
            ForcesData += "     "
            ForcesData += str(ForceFrictionMut.value())
            ForcesData += "     "
            ForcesData += str(ForceFrictionKsit.value())
            ForcesData += "     "
            ForcesData += str(ForceFrictionKr.value())
            ForcesData += "     "
            ForcesData += str(ForceFrictionMur.value())
            ForcesData += "     "
            ForcesData += str(ForceFrictionKsir.value())
            ForcesData += "     "
            ForcesData += "0   0   0   0  0 (kt,mut,ksit,kr,mur,ksir)\n"
        else:
            ForcesData += "0   12     0    0    0    0   0   0   0   0   0   0  0 (kt,mut,ksit,kr,mur,ksir)\n"
            
        ForcesData += "\n"

        return ForcesData



            
