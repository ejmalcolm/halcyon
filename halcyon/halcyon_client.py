# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'halcyon_client.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Halcyon(object):
    def setupUi(self, Halcyon):
        Halcyon.setObjectName("Halcyon")
        Halcyon.resize(1200, 745)
        self.centralwidget = QtWidgets.QWidget(Halcyon)
        self.centralwidget.setObjectName("centralwidget")
        self.PlanetView = QtWidgets.QListView(self.centralwidget)
        self.PlanetView.setGeometry(QtCore.QRect(10, 10, 225, 550))
        self.PlanetView.setToolTip("")
        self.PlanetView.setObjectName("PlanetView")
        self.PlayerView = QtWidgets.QListView(self.centralwidget)
        self.PlayerView.setGeometry(QtCore.QRect(965, 10, 225, 550))
        self.PlayerView.setToolTip("")
        self.PlayerView.setObjectName("PlayerView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 0, 211, 31))
        self.label.setStyleSheet("font: 24pt \"Sitka\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(250, 40, 701, 521))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(10, 570, 581, 121))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(610, 570, 581, 121))
        self.listView_3.setObjectName("listView_3")
        Halcyon.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Halcyon)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menutewst = QtWidgets.QMenu(self.menubar)
        self.menutewst.setObjectName("menutewst")
        Halcyon.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Halcyon)
        self.statusbar.setObjectName("statusbar")
        Halcyon.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menutewst.menuAction())

        self.retranslateUi(Halcyon)
        QtCore.QMetaObject.connectSlotsByName(Halcyon)

    def retranslateUi(self, Halcyon):
        _translate = QtCore.QCoreApplication.translate
        Halcyon.setWindowTitle(_translate("Halcyon", "Halcyon -- Client"))
        self.label.setText(_translate("Halcyon", "Octant View"))
        self.menutewst.setTitle(_translate("Halcyon", "Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Halcyon = QtWidgets.QMainWindow()
    ui = Ui_Halcyon()
    ui.setupUi(Halcyon)
    Halcyon.show()
    sys.exit(app.exec_())
