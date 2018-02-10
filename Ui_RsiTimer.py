# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_RsiTimer.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RsiTimer(object):
    def setupUi(self, RsiTimer):
        RsiTimer.setObjectName("RsiTimer")
        RsiTimer.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(RsiTimer)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(RsiTimer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), RsiTimer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), RsiTimer.reject)
        QtCore.QMetaObject.connectSlotsByName(RsiTimer)

    def retranslateUi(self, RsiTimer):
        RsiTimer.setWindowTitle(QtGui.QApplication.translate("RsiTimer", "RsiTimer", None, QtGui.QApplication.UnicodeUTF8))
