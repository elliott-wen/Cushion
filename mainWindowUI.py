# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Sep 10 15:08:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(1440, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = PressureFigure(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.actionDynamic_Tags = QtGui.QAction(mainWindow)
        self.actionDynamic_Tags.setObjectName(_fromUtf8("actionDynamic_Tags"))
        self.actionDangerous_Zones_Settings = QtGui.QAction(mainWindow)
        self.actionDangerous_Zones_Settings.setObjectName(_fromUtf8("actionDangerous_Zones_Settings"))
        self.actionAnchor_Settings = QtGui.QAction(mainWindow)
        self.actionAnchor_Settings.setObjectName(_fromUtf8("actionAnchor_Settings"))
        self.actionHistory_Query = QtGui.QAction(mainWindow)
        self.actionHistory_Query.setObjectName(_fromUtf8("actionHistory_Query"))
        self.actionHistory_Event = QtGui.QAction(mainWindow)
        self.actionHistory_Event.setObjectName(_fromUtf8("actionHistory_Event"))

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Localization System", None))
        self.actionDynamic_Tags.setText(_translate("mainWindow", "Dynamic Tag Settings", None))
        self.actionDangerous_Zones_Settings.setText(_translate("mainWindow", "Dangerous Zones Settings", None))
        self.actionAnchor_Settings.setText(_translate("mainWindow", "Anchor Settings", None))
        self.actionHistory_Query.setText(_translate("mainWindow", "History Trajectory", None))
        self.actionHistory_Event.setText(_translate("mainWindow", "History Event", None))

from pressurefigure import PressureFigure
