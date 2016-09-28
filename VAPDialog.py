from PyQt5.QtWidgets import QDialog
from NewWindow import *

class VAPDialog(QDialog):
    
    def __init__(self, ui):
        
        self.ui = ui # Ui_SCOPI_Dialog()

        self.VAPstring = ""

        self.initEnableSlot()
        self.initAddSlot()
        
        self.ui.VAPClear.clicked.connect(lambda : self.clear())
        self.ui.VAPSee.clicked.connect(lambda : self.see())
      
       


    def initEnableSlot(self):
        self.ui.VAPEDOButton.clicked.connect(lambda : self.enabled(self.ui.VAPEDOWidget))
        self.ui.VAPEDOButton.clicked.connect(lambda : self.enabled(self.ui.VAPEDOAdd))

        
        self.ui.VAPGeoButton.clicked.connect(lambda : self.enabled(self.ui.VAPGeoWidget))
        self.ui.VAPGeoButton.clicked.connect(lambda : self.enabled(self.ui.VAPGeoAdd))


        
        self.ui.VAPStairsButton.clicked.connect(lambda : self.enabled(self.ui.VAPStairsWidget))
        self.ui.VAPStairsButton.clicked.connect(lambda : self.enabled(self.ui.VAPStairsAdd))


        self.ui.VAPCstButton.clicked.connect(lambda : self.enabled(self.ui.VAPCstWidget))
        self.ui.VAPCstButton.clicked.connect(lambda : self.enabled(self.ui.VAPCstAdd))


        self.ui.VAPGivenButton.clicked.connect(lambda : self.enabled(self.ui.VAPGivenWidget))
        self.ui.VAPGivenButton.clicked.connect(lambda : self.enabled(self.ui.VAPGivenAdd))

        
        self.ui.VAPEDOmomentButton.clicked.connect(lambda : self.enabled(self.ui.VAPEDOmomentWidget))
        self.ui.VAPEDOmomentButton.clicked.connect(lambda : self.enabled(self.ui.VAPEDOmomentAdd))


        self.ui.VAPGoalButton.clicked.connect(lambda : self.enabled(self.ui.VAPGoalWidget))
        self.ui.VAPGoalButton.clicked.connect(lambda : self.enabled(self.ui.VAPGoalAdd))

        
        self.ui.VAPStokesButton.clicked.connect(lambda : self.enabled(self.ui.VAPStokesAdd))

                
        self.ui.VAPCouplageButton.clicked.connect(lambda : self.enabled(self.ui.VAPCouplageAdd))



        
    def initAddSlot(self):
        self.ui.VAPEDOAdd.clicked.connect(lambda : self.disabled(self.ui.VAPEDOWidget))
        self.ui.VAPEDOAdd.clicked.connect(lambda : self.disabled(self.ui.VAPEDOAdd))
        self.ui.VAPEDOAdd.clicked.connect(lambda : self.EDOAdd())


        self.ui.VAPGeoAdd.clicked.connect(lambda : self.disabled(self.ui.VAPGeoWidget))
        self.ui.VAPGeoAdd.clicked.connect(lambda : self.disabled(self.ui.VAPGeoAdd))
        self.ui.VAPGeoAdd.clicked.connect(lambda : self.geoAdd())

        
        self.ui.VAPStairsAdd.clicked.connect(lambda : self.disabled(self.ui.VAPStairsWidget))
        self.ui.VAPStairsAdd.clicked.connect(lambda : self.disabled(self.ui.VAPStairsAdd))
        self.ui.VAPStairsAdd.clicked.connect(lambda : self.stairsAdd())
        

        self.ui.VAPCstAdd.clicked.connect(lambda : self.disabled(self.ui.VAPCstWidget))
        self.ui.VAPCstAdd.clicked.connect(lambda : self.disabled(self.ui.VAPCstAdd))
        self.ui.VAPCstAdd.clicked.connect(lambda : self.cstAdd())


        self.ui.VAPGivenAdd.clicked.connect(lambda : self.disabled(self.ui.VAPGivenWidget))
        self.ui.VAPGivenAdd.clicked.connect(lambda : self.disabled(self.ui.VAPGivenAdd))
        self.ui.VAPGivenAdd.clicked.connect(lambda : self.givenAdd())
                                            
        
        self.ui.VAPEDOmomentAdd.clicked.connect(lambda : self.disabled(self.ui.VAPEDOmomentWidget))
        self.ui.VAPEDOmomentAdd.clicked.connect(lambda : self.disabled(self.ui.VAPEDOmomentAdd))
        self.ui.VAPEDOmomentAdd.clicked.connect(lambda : self.EDOmomentAdd())
                                        

        self.ui.VAPGoalAdd.clicked.connect(lambda : self.disabled(self.ui.VAPGoalWidget))
        self.ui.VAPGoalAdd.clicked.connect(lambda : self.disabled(self.ui.VAPGoalAdd))
        self.ui.VAPGoalAdd.clicked.connect(lambda : self.goalAdd())

        
        self.ui.VAPStokesAdd.clicked.connect(lambda : self.disabled(self.ui.VAPStokesAdd))
        self.ui.VAPStokesAdd.clicked.connect(lambda : self.stokesAdd())
        
                
        self.ui.VAPCouplageAdd.clicked.connect(lambda : self.disabled(self.ui.VAPCouplageAdd))
        self.ui.VAPCouplageAdd.clicked.connect(lambda : self.couplagAdd())
        
        
    def enabled(self, dialog):
        dialog.setEnabled(True)

    def disabled(self,dialog):
        dialog.setEnabled(False)


        

    def EDOAdd(self):
        self.VAPstring += "EDO 1 "+str(self.ui.VAPEDODissip.value())+"\n"

    def geoAdd(self):
        self.VAPstring += "Geo 2 "+str(self.ui.VAPGeoNumlevel.value())+" "+str(self.ui.VAPGeoHpmm.value())+str(self.ui.VAPGeoTypecreation.value())+"\n"
        
    def stairsAdd(self):
        self.VAPstring += "Stairs 3 "+str(self.ui.VAPStairsNumlevel.value())+"\n"

    def cstAdd(self):
        self.VAPstring += "Cst 4 "+str(self.ui.VAPCstNumlevel.value())+" "+str(self.ui.VAPCstNumgroup.value())+" "+str(self.ui.VAPCstUx.value())+" "+str(self.ui.VAPCstuy.value())+" "+str(self.ui.VAPCstuz.value())+"\n"

    def givenAdd(self):
        self.VAPstring += "Given 5 "+str(self.ui.VAPGivenNumlevel.value())+"\n"

    def EDOmomentAdd(self):
        self.VAPstring += "EDO_moments 6 "+str(self.ui.VAPEDOmomentDissip.value())+"\n"

    def goalAdd(self):
        self.VAPstring += "Goal 7 "+str(self.ui.VAPGoalNumlevel.value())+"\n"
        
    def stokesAdd(self):
        self.VAPstring += "Stokes  12 \n"
        
    def couplagAdd(self):
        self.VAPstring += "Couplage -1 \n"


        

    def clear(self):
        self.VAPstring = ""

    def see(self):
        self._new_window = NewWindow(self.VAPstring)
        self._new_window.show()

        
    def writeVAPData(self):
        VAP  = "================================\n"
        VAP += "VITESSE A PRIORI : name type parameters\n"
        VAP += "                   LUB     0   viscosity dseuil\n"
        VAP += "                   EDO     1   dissip\n"
        VAP += "                   Geo     2   num_level h_FMM type_creation // if type_creation=1, geodesic distance already computed\n"
        VAP += "                   Stairs  3   num_level\n"
        VAP += "                   Cst     4   num_level num_group ux uy (uz) \n"
        VAP += "                   Given   5   num_level\n"
        VAP += "                   EDO_moments 6 dissip\n"
        VAP += "                   Goal    7   num_level  // Several VAP (La Mecque)\n"
        VAP += "                   Stokes  10+dim \n"
        VAP += "================================\n"
        VAP += "\n"
        VAP += self.VAPstring
        VAP += "->VAPS_END<-   // do not remove it !\n"
        VAP += "\n"

        return VAP
