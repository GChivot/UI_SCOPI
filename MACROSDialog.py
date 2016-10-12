from PyQt5.QtWidgets import QDialog
from NewWindow import *

class MacrosDialog(QDialog):
    
    def __init__(self, ui):

        self.ui = ui # Ui_SCOPI_Dialog()

        self.Macrostring = ""

        self.initEnableSlot()
        self.initAddSlot()

        self.ui.MacroClearButton.clicked.connect(lambda : self.clear())
        self.ui.MacroSeeButton.clicked.connect(lambda : self.see())

        
    def initEnableSlot(self):

        self.ui.MacroChainButton.clicked.connect(lambda : self.enabled(self.ui.MacroChainWidget))
        self.ui.MacroChainButton.clicked.connect(lambda : self.enabled(self.ui.MacroChainAddButton))

        
        self.ui.MacroRedCellButton.clicked.connect(lambda : self.enabled(self.ui.MacroRedCellWidget))
        self.ui.MacroRedCellButton.clicked.connect(lambda : self.enabled(self.ui.MacroRedCellAddButton))


    def initAddSlot(self):
        self.ui.MacroChainAddButton.clicked.connect(lambda : self.disabled(self.ui.MacroChainWidget))
        self.ui.MacroChainAddButton.clicked.connect(lambda : self.disabled(self.ui.MacroChainAddButton))
        self.ui.MacroChainAddButton.clicked.connect(lambda : self.macrosChainAdd())

        self.ui.MacroRedCellAddButton.clicked.connect(lambda : self.disabled(self.ui.MacroRedCellWidget))
        self.ui.MacroRedCellAddButton.clicked.connect(lambda : self.disabled(self.ui.MacroRedCellAddButton))
        self.ui.MacroRedCellAddButton.clicked.connect(lambda : self.macrosRedCellAdd())
        

    def enabled(self, dialog):
        dialog.setEnabled(True)

    def disabled(self,dialog):
        dialog.setEnabled(False)



    def macrosChainAdd(self):
        self.Macrostring += str(self.ui.MacroName.toPlainText())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroNbMacros.value())
        self.Macrostring += " 2 "
        self.Macrostring += str(self.ui.MacroNbPart_NbMacros.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroGPE.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroChainPcr.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroChainCohka.value())
        self.Macrostring += "	(pcr>0.5 !, coh_ka)\n"
        
        
    def macrosRedCellAdd(self):
        self.Macrostring += str(self.ui.MacroName.toPlainText())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroNbMacros.value())
        self.Macrostring += " 1 "
        self.Macrostring += str(self.ui.MacroNbPart_NbMacros.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroGPE.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroRedCellCohrmac.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroRedCellCohk.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroRedCellCohka.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroRedCellPcr.value())
        self.Macrostring += " "
        self.Macrostring += str(self.ui.MacroRedCellPcraux.value())
        self.Macrostring += "	(coh_rmac, coh_k, coh_ka, pcr, pcraux)\n"
        
        
    def clear(self):
        self.Macrostring = ""

    def see(self):
        self._new_window = NewWindow(self.Macrostring)
        self._new_window.show()

    def writeMacrosData(self):
        macro  = "================================\n"
        macro += "MACROS PARTS : name  Nb_macros  type_macro  Nb_part/macro  macro_part_gp(to build macro from this gp part.)  parameters   // Macro_Red_Cell=1, Chain=2\n"
        macro += "================================\n"
        macro += "\n"
        macro += self.Macrostring
        macro += "->MACRO_PART_END<-  //!!!pour cesser la lecture des macros de particules, a ne pas supprimer!!!\n"
        macro += "\n"
        
        return macro











        
