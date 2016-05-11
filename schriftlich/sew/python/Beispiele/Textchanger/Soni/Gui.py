# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\adi\Desktop\Textchanger.ui'
#
# Created: Sun May  8 17:10:50 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 183)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonUpper = QtGui.QPushButton(self.centralwidget)
        self.pushButtonUpper.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.pushButtonUpper.setObjectName("pushButton")
        self.pushButtonLower = QtGui.QPushButton(self.centralwidget)
        self.pushButtonLower.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButtonLower.setObjectName("pushButton_2")
        self.pushButtonCV = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCV.setGeometry(QtCore.QRect(380, 20, 91, 21))
        self.pushButtonCV.setObjectName("pushButtonCV")
        self.pushButtonKV = QtGui.QPushButton(self.centralwidget)
        self.pushButtonKV.setGeometry(QtCore.QRect(650, 20, 81, 23))
        self.pushButtonKV.setObjectName("pushButtonKV")
        self.pushButtonCE = QtGui.QPushButton(self.centralwidget)
        self.pushButtonCE.setGeometry(QtCore.QRect(380, 80, 91, 21))
        self.pushButtonCE.setObjectName("pushButtonCE")
        self.pushButtonKE = QtGui.QPushButton(self.centralwidget)
        self.pushButtonKE.setGeometry(QtCore.QRect(650, 80, 81, 23))
        self.pushButtonKE.setObjectName("pushButtonKE")
        self.plainTextEditc = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEditc.setGeometry(QtCore.QRect(260, 20, 104, 31))
        self.plainTextEditc.setObjectName("plainTextEdit")
        self.plainTextEditk = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEditk.setGeometry(QtCore.QRect(530, 20, 104, 31))
        self.plainTextEditk.setObjectName("plainTextEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelect = QtGui.QAction(MainWindow)
        self.actionSelect.setObjectName("actionSelect")
        self.actionUpper_Lower = QtGui.QAction(MainWindow)
        self.actionUpper_Lower.setObjectName("actionUpper_Lower")
        self.menuFile.addAction(self.actionSelect)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Text change", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpper.setText(QtGui.QApplication.translate("MainWindow", "Uppercase", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLower.setText(QtGui.QApplication.translate("MainWindow", "Lowercase", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCV.setText(QtGui.QApplication.translate("MainWindow", "C-Verschlüsseln", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonKV.setText(QtGui.QApplication.translate("MainWindow", "K-Verschlüsseln", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCE.setText(QtGui.QApplication.translate("MainWindow", "C-Entschlüsseln", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonKE.setText(QtGui.QApplication.translate("MainWindow", "K-Entschlüsseln", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))

