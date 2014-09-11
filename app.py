from hub import SerialController
from PyQt4 import QtGui
import sys
from mainwindow import MainWindow
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    sc = SerialController()
    win = MainWindow()
    win.show()
    sc.open_serial()
    sc.data_received.connect(win.ui.widget.update_data)
    sys.exit(app.exec_())
