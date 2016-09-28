import PARTDialog, OBSTDialog


class ConfigGenerate(PARTDialog.PARTICLESDialog, OBSTDialog.OBSTDialog):
    def __init__(self, ui):
        super(ConfigGenerate, self).__init__(ui)

        self.ui = ui # Ui_SCOPI_Dialog()

        self.PART = PARTDialog.PARTICLESDialog(self.ui)
        self.OBST = OBSTDialog.OBSTDialog(self.ui)

        self.ui.GenerateConfigFile.clicked.connect(lambda : self.writeConfigFile())


    def writeConfigFile(self):
        initString  = "================================\n"
        initString += "CONFIG\n"
        initString += "================================\n"
        initString += "\n"
        initString += str(self.PART.NbPartTot)+"	NbP	Number of Particles\n"
        initString += str(self.OBST.NbObstTot)+"	NbO	Number of Obstacles\n"
        initString += "0	NbM	Number of Macros\n"
        initString += "0       NbMO    Number of Macros of Obstacles\n"
        initString += "\n"

        
        config = open("config", "w")
        config.write(initString)
        config.write(self.PART.writeParticlesData())
        config.write(self.OBST.writeOBSTData())

        endString  = "================================\n"
        endString += "MACROS PARTS : name  Nb_macros  type_macro  Nb_part/macro  macro_part_gp(to build macro from this gp part.)  parameters   // Macro_Red_Cell=1, Chain=2\n"
        endString += "================================\n"
        endString += "\n"
        endString += "->MACRO_PART_END<-  //!!!pour cesser la lecture des macros, a ne pas supprimer!!!\n"
        endString += "\n"
        endString += "================================\n"
        endString += "MACROS_OBS :  name  type_macro_obs=0       number of obs in macro         obs'numbers    // Macro Room\n"
        endString += "              name  type_macro_obs=1       number of obs in macro         obs'numbers    // Macro Table\n"
        endString += "	      name  type_macro_obs=2       number of obs in macro         obs'numbers    // Macro Stairwell\n"
        endString += "              name  type_macro_obs=3       number of obs in macro         obs'numbers    // Macro Stair\n"
        endString += "              name  type_macro_obs=4       number of obs in macro         obs'numbers    // Macro Door\n"
        endString += "================================\n"
        endString += "\n"
        endString += "->MACRO_OBS_END<-\n"
        
        config.write(endString)
        config.close()
