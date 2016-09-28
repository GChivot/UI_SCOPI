from PyQt5.QtWidgets import QLabel, QMainWindow


class NewWindow(QMainWindow):
    def __init__(self,text):
        super(NewWindow, self).__init__()
        self._new_window = None
        self._label = QLabel(text)
        self.setCentralWidget(self._label)
