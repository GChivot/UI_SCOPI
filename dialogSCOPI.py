import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_SCOPIDialog import Ui_SCOPI_Dialog
import DataGenerate, ConfigGenerate

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_SCOPI_Dialog()
ui.setupUi(window)
DataGenerate.DataGenerate(ui)
ConfigGenerate.ConfigGenerate(ui)
ui.QuitButton.clicked.connect(quit)
window.show()
sys.exit(app.exec_())
