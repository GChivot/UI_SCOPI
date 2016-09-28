from PyQt5.QtWidgets import QDialog
from NewWindow import *

class OBSTDialog(QDialog):
    
    def __init__(self, ui):
        
        self.ui = ui # Ui_SCOPI_Dialog()

        self.OBSTstring = ""
        self.NbObstTot = 0

        self.initEnableSlot()
        self.initAddSlot()

        self.ui.ObstaclesClear.clicked.connect(lambda : self.clear())
        self.ui.ObstaclesSee.clicked.connect(lambda : self.see())
        

    def initEnableSlot(self):
        self.ui.ObstaclesDisqueButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesDisque))
        self.ui.ObstaclesDisqueButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesDisqueAdd))
        
        self.ui.ObstaclesSphereButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesSphere))
        self.ui.ObstaclesSphereButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesSphereAdd))
        
        self.ui.ObstaclesSegmentButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesSegment))
        self.ui.ObstaclesSegmentButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesSegmentAdd))
        
        self.ui.ObstaclesPlanButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesPlan))
        self.ui.ObstaclesPlanButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesPlanAdd))
        
        self.ui.ObstaclesCylindreButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesCylindre))
        self.ui.ObstaclesCylindreButton.clicked.connect(lambda : self.enabled(self.ui.ObstaclesCylindreAdd))


    def initAddSlot(self):
        self.ui.ObstaclesDisqueAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesDisque))
        self.ui.ObstaclesDisqueAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesDisqueAdd))
        self.ui.ObstaclesDisqueAdd.clicked.connect(lambda : self.disqueAdd())

        self.ui.ObstaclesSphereAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesSphere))
        self.ui.ObstaclesSphereAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesSphereAdd))
        self.ui.ObstaclesSphereAdd.clicked.connect(lambda : self.sphereAdd())
        
        self.ui.ObstaclesSegmentAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesSegment))
        self.ui.ObstaclesSegmentAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesSegmentAdd))
        self.ui.ObstaclesSegmentAdd.clicked.connect(lambda : self.segmentAdd())

        self.ui.ObstaclesPlanAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesPlan))
        self.ui.ObstaclesPlanAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesPlanAdd))
        self.ui.ObstaclesPlanAdd.clicked.connect(lambda : self.planAdd())


        self.ui.ObstaclesCylindreAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesCylindre))
        self.ui.ObstaclesCylindreAdd.clicked.connect(lambda : self.disabled(self.ui.ObstaclesCylindreAdd))
        self.ui.ObstaclesCylindreAdd.clicked.connect(lambda : self.cylinderAdd())

        
    def enabled(self, dialog):
        dialog.setEnabled(True)

    def disabled(self,dialog):
        dialog.setEnabled(False)



    def disqueAdd(self):
        self.OBSTstring += "Disque 1 1 "
        self.OBSTstring += str(self.ui.ObstaclesDisqueX.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesDisqueY.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesDisqueRadius.value())+" 1 "
        self.OBSTstring += str(self.ui.ObstaclesDisqueUx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesDisqueUy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesDisqueRandx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesDisqueRandy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesDisqueW.value())+"\n"
        self.NbObstTot += 1

    def sphereAdd(self):
        self.OBSTstring += "Sphere 1 1 "
        self.OBSTstring += str(self.ui.ObstaclesSphereX.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereY.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereZ.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereRadius.value())+" 1 "
        self.OBSTstring += str(self.ui.ObstaclesSphereUx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereUy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereUz.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereRandx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereRandy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereRandz.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSphereW.value())+"\n"
        self.NbObstTot += 1
        
    def segmentAdd(self):
        self.OBSTstring += "Segment 2 1 "
        self.OBSTstring += str(self.ui.ObstaclesSegmentX1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentY1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentX2.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentY2.value())+" 1 "
        self.OBSTstring += str(self.ui.ObstaclesSegmentUx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentUy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentRandx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentRandy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesSegmentW.value())+"\n"
        self.NbObstTot += 1
        
    def planAdd(self):
        self.OBSTstring += "Plan 3 1 "
        self.OBSTstring += str(self.ui.ObstaclesPlanX1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanY1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanZ1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanX2.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanY2.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanZ2.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanX3.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanY3.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanZ3.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanX4.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanY4.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanZ4.value())
        if self.ui.ObstaclesPlanBeta.value()==0:
            self.OBSTstring += " 1 "
        else:
            self.OBSTstring += " 2 "
        self.OBSTstring += str(self.ui.ObstaclesPlanUx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanUy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanUz.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanRandx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanRandy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanRandz.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesPlanW.value())+" "
        if self.ui.ObstaclesPlanBeta.value()==0:
            self.OBSTstring += "\n"
        else:
            self.OBSTstring += str(self.ui.ObstaclesPlanBeta.value())+"\n"
        self.NbObstTot += 1
        
    def cylinderAdd(self):
        self.OBSTstring += "Plan 4 1 "
        self.OBSTstring += str(self.ui.ObstaclesCylindreRadius.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreXc1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreYc1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreZc1.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreXc2.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreYc2.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreZc2.value())
        if self.ui.ObstaclesCylindreBeta.value()==0:
            self.OBSTstring += " 1 "
        else:
            self.OBSTstring += " 2 "
        self.OBSTstring += str(self.ui.ObstaclesCylindreUx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreUy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreUz.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreRandx.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreRandy.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreRandz.value())+" "
        self.OBSTstring += str(self.ui.ObstaclesCylindreW.value())+" "
        if self.ui.ObstaclesCylindreBeta.value()==0:
            self.OBSTstring += "\n"
        else:
            self.OBSTstring += str(self.ui.ObstaclesCylindreBeta.value())+"\n"
        self.NbObstTot += 1


            
    def clear(self):
        self.OBSTstring = ""
        self.NbObstTot = 0

    def see(self):
        self._new_window = NewWindow(self.OBSTstring)
        self._new_window.show()


    def writeOBSTData(self):
        OBST  = "================================\n"
        OBST += "OBSTACLES : Obs_Name Obs_Type Obs_isrun Obs_q Obs_Param Obs_Type_Mvt Obs_Mvt_Param \n"
        OBST += "	        type_obs=1 isrun q(2) r type_mvt=1 u(2) x(2) w //disque2D\n"
        OBST += "            type_obs=1 isrun q(3) r type_mvt=1 u(3) x(3) w //sphere3D\n"
        OBST += "	        type_obs=2 isrun q1(2) q2(2) type_mvt=1 u(2) x(2) w // segment 2D\n"
        OBST += "	        type_obs=3 isrun q1(3) q2(3) q3(3) q4(3) type_mvt=1 u(3) x(3) w // plan 3D\n"
        OBST += "            type_obs=3 isrun q1(3) q2(3) q3(3) q4(3) type_mvt=2 u(3)*cos(beta*t) x(3) w beta// plan 3D\n"
        OBST += "            type_obs=4 isrun r bot_c(3) top_c(3) type_mvt=1 u(3) x(3) w // cyl 3D\n"
        OBST += "            type_obs=4 isrun r bot_c(3) top_c(3) type_mvt=2 u(3)*cos(beta*t) x(3) w beta// cyl 3D\n"
        OBST += "================================\n"
        OBST += "\n"
        OBST += self.OBSTstring
        OBST += "->OBS_END<-  //!!!pour cesser la lecture des obstacles, a ne pas supprimer!!!\n"
        OBST += "\n"

        return OBST






        
