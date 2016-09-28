from PyQt5.QtWidgets import QDialog

class VisualisationDialog(QDialog):
    
    def __init__(self, ui):
        
        self.ui = ui # Ui_SCOPI_Dialog()
      
    def writeVisualisationData(self):
        VisuData  = "================================\n"
        VisuData += "OTHER PARAMETERS :\n"
        VisuData += "================================\n"
        VisuData += "\n"
        VisuData += str(self.ui.ParamFinalTime.value())
        VisuData += "  T	final time\n"
        VisuData += "\n"
        if self.ui.VisuSortieRien.isChecked():
            VisuData += "0"
        if self.ui.VisuSortieCout.isChecked():
            VisuData += "1"
        if self.ui.VisuSortieFile.isChecked():
            VisuData += "2"
        if self.ui.VisuSortieCoutfile.isChecked():
            VisuData += "3"
        VisuData += "		 sortie   0=rien 1=cout 2=file 3=cout+file\n"
        VisuData += "./POS/     prefix_pos\n"
        VisuData += "./VTK/     prefix_vtk\n"
        VisuData += "./POV/     prefix_povray\n"
        VisuData += "resultats.txt	 filename\n"
        VisuData += "\n"
        if self.ui.VisuPTRNon.isChecked():
            VisuData += "0"
        if self.ui.VisuPTROui.isChecked():
            VisuData += "1"
        if self.ui.VisuPTROuiSansInt.isChecked():
            VisuData += "2"
        VisuData += "       plot		trace en temps reel  (0 non ; 1 oui ; 2 oui sans interacteurs)\n"
        VisuData += str(self.ui.VisuIntervalletrace.value())
        VisuData += "	    dn_plot		intervalle de trace\n"
        
        if self.ui.VIsuTP.isChecked():
            VisuData += "1"
        else:
            VisuData += "0"
        VisuData += "       plot_part   	trace des particules ?\n"
        
        if self.ui.VisuDSPAucune.isChecked():
            VisuData += "0"
        if self.ui.VisuDSPGroup.isChecked():
            VisuData += "1"
        if self.ui.VisuDSPP.isChecked():
            VisuData += "2"
        if self.ui.VisuDSPRoura.isChecked():
            VisuData += "3"
        if self.ui.VisuDSPData.isChecked():
            VisuData += "4"
        VisuData += "       data_part	donnees sur les particules : 0=aucune 1=group 2=p 3=r ou ra 4=data\n"
        if self.ui.VisuTC.isChecked():
            VisuData += "1"
        else:
            VisuData += "0"
        VisuData += "       plot_cont   	trace des contacts ?\n"
        if self.ui.VisuDSCAucune.isChecked():
            VisuData += "0"
        if self.ui.VisuDSCGamma.isChecked():
            VisuData += "1"
        if self.ui.VisuDSCLambda.isChecked():
            VisuData += "2"
        VisuData += "       data_cont	donnees sur les contacts : 0=aucune 1=gamma 2=lambda\n"
        
        if self.ui.VisuACVVitesse.isChecked():
            VisuData += "0"
        if self.ui.VisuACVDirection.isChecked():
            VisuData += "1"
        VisuData += "       plot_vect       affichage d'un champ de vecteur : 1=vitesse 2=direction\n"
        
        if self.ui.VisuSFG.isChecked():
            VisuData += "1"
        else:
            VisuData += "0"
        VisuData += "       save_graphic	sauvegarde fichiers graphiques ? si oui, creer un dossier POS\n"

        if self.ui.VisuFSP.isChecked():
            VisuData += "1"
        else:
            VisuData += "0"
        VisuData += "       save_povray     fichiers de sortie pour povray\n"

        VisuData += str(self.ui.VisuSavegraph.value())
        VisuData += "       dn_save_graph   intervalle de sauvegarde graphique\n"
        VisuData += str(self.ui.VisuSaverestart.value())
        VisuData += "	dn_save_restart intervalle de sauvegarde pour restart\n"
        VisuData += str(self.ui.VisuLCX.value())
        VisuData += "	camera location : x\n"
        VisuData += str(self.ui.VisuLCY.value())
        VisuData += "	camera location : y\n"
        VisuData += str(self.ui.VisuLCZ.value())
        VisuData += "	camera location : z\n"
        VisuData += str(self.ui.VisuLPFCX.value())
        VisuData += "	camera focal point : x\n"
        VisuData += str(self.ui.VisuLPFCY.value())
        VisuData += "	camera focal point : y\n"
        VisuData += str(self.ui.VisuLPFCZ.value())
        VisuData += "	camera focal point : z\n"
        VisuData += "\n"

        return VisuData










        
