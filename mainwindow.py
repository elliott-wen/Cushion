from PyQt4 import QtGui
from mainWindowUI import Ui_mainWindow


class MainWindow(QtGui.QMainWindow):

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

