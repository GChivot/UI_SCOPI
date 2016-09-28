from PyQt5.QtWidgets import QDialog

class PARAMDialog(QDialog):
    def __init__(self, ui):
        
        self.ui = ui # Ui_SCOPI_Dialog()
        
        self.ui.ParamTOCBound.toggled.connect(self.ui.ParamTOCGammaWidget.setEnabled)
        


    
    def writeContinuousProblemData(self):
        CP  = "================================\n"
        CP += "CONTINUOUS PROBLEM\n"
        CP += "================================\n"
        CP += "\n"
        CP += str(self.ui.ParamDIM.value())
        CP += "       DIM\n"
        CP += "\n"

        if self.ui.ParamTOCBound.isChecked():
            CP += "2       TYPE OF CONTACT LAW (1 = no bound on gamma, 2=bounded)\n"
            CP += str(self.ui.ParamGamma.value())
            CP += "       bound for gamma if bounded contact law"
        else:
            CP += "1       TYPE OF CONTACT LAW (1 = no bound on gamma, 2=bounded)\n"
            CP += "0       bound for gamma if bounded contact law\n"

        CP += "\n"
        

        return CP

    def writeDiscreteProblemData(self):
        DP  = "================================\n"
        DP += "DISCRETE PROBLEM\n"
        DP += "================================\n"
        DP += "\n"
        DP += str(self.ui.ParamDmax_rmax.value())
        DP += "     Dmax/rmax : dist. max. pour qu'il y ait contact / rayon max. (Dmax=1.5*rmax par exemple)\n"
        DP += str(self.ui.ParamEta_rmax.value())
        DP += "    eta/rmax(t=0) : taille des boites / rayon max. (eta=2*rmax(t=0) par exemple)\n"
        DP += "        ATTENTION SI PARTICULES GROSSISSENT QUE RAYON DEVIENNE PAS PLUS GRAND QUE BOITE !!!\n"
        DP += "\n"
        DP += str(self.ui.ParamUmax.value())
        DP += "    umax~sqrt(2*(Hmax-Hmin)*g+u0^2) for example...\n"
        DP += str(self.ui.ParamDtUmax_rmin.value())
        DP += "\n"
        if self.ui.ParamUzawa.isChecked():
            DP += "1    PROJECTION METHOD (1=Uzawa 3=Optimized Uzawa 42=couplage CAFES dim 2, 43=couplage CAFES dim 3)\n"
        if self.ui.ParamOptimizedUzawa.isChecked():
            DP += "3    PROJECTION METHOD (1=Uzawa 3=Optimized Uzawa 42=couplage CAFES dim 2, 43=couplage CAFES dim 3)\n"
        if self.ui.ParamCouplageCafes.isChecked() and ParamDIM.value() == 2:
            DP += "42   PROJECTION METHOD (1=Uzawa 3=Optimized Uzawa 42=couplage CAFES dim 2, 43=couplage CAFES dim 3)\n"
        if self.ui.ParamCouplageCafes.isChecked() and ParamDIM.value() == 3:
            DP += "43   PROJECTION METHOD (1=Uzawa 3=Optimized Uzawa 42=couplage CAFES dim 2, 43=couplage CAFES dim 3)\n"
        DP += str(self.ui.ParamNbcoeur.value())
        DP += "    Nb coeurs pour Intel TBB\n"
        DP += str(self.ui.ParamRhoDtDt_min.value())
        DP += "    rho*dt*dt/min(m)\n"
        DP += str(self.ui.ParamEps_rmin.value())
        DP += "    eps/rmin\n"
        DP += str(self.ui.ParamDmin.value())
        DP += "    Dmin\n"
        DP += str(self.ui.ParamMaxiter.value())
        DP += "    maxiter\n"
        DP += "\n"
        DP += "1	NEIGHBOURGS METHOD (1=Boxes)\n"
        
        return DP
