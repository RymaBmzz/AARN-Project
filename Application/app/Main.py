# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1112, 728)
        MainWindow.setStyleSheet("background-image: url(arr.jpg);\n"
"")
        MainWindow.setProperty("resource", "")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(410, 330, 171, 61))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 471, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(400, 190, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 16pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 291, 261))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setStyleSheet("background-image: url(labelarriere.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 16pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(790, 190, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 16pt \"Comic Sans MS\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(790, 280, 291, 251))
        self.label_6.setStyleSheet("background-image: url(labelarriere.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 330, 91, 61))
        self.pushButton.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1112, 17))
        self.menuBar.setObjectName("menuBar")
        self.menumenu = QtWidgets.QMenu(self.menuBar)
        self.menumenu.setObjectName("menumenu")
        self.menuQuitter = QtWidgets.QMenu(self.menuBar)
        self.menuQuitter.setObjectName("menuQuitter")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionA_propos = QtWidgets.QAction(MainWindow)
        self.actionA_propos.setObjectName("actionA_propos")
        self.menumenu.addAction(self.actionA_propos)
        self.menuBar.addAction(self.menumenu.menuAction())
        self.menuBar.addAction(self.menuQuitter.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Package1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Package2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Package3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Package4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Package5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Package6"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Package7"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Package8"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Package9"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Package10"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Package11"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Package12"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Package13"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Package14"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Package15"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Package16"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Package17"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Package18"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Package19"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Package20"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Package21"))
        self.comboBox.setItemText(22, _translate("MainWindow", "Package22"))
        self.comboBox.setItemText(23, _translate("MainWindow", "Package23"))
        self.comboBox.setItemText(24, _translate("MainWindow", "Package24"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-style:italic;\">Silent Monitoring</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", " Choisir une instance"))
        self.label_4.setText(_translate("MainWindow", "           Cible"))
        self.label_5.setText(_translate("MainWindow", "         Resultat"))
        self.pushButton.setText(_translate("MainWindow", "Verifier "))
        self.menumenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuQuitter.setTitle(_translate("MainWindow", "Quitter"))
        self.actionA_propos.setText(_translate("MainWindow", "Architecture du Modele de RN "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
