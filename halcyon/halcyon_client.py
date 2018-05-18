# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'halcyon_client.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import inspect

from planet import Planet

PLANETS = {'Dune' : Planet('Dune', 1, 2), 'Hoth' : Planet('Hoth', 2, 4)}
TASKS = {}

class DetailView(QtWidgets.QListWidget):
    '''The class for displaying lists of class objects
    Includes context menus for each class object displayed
    '''

    def __init__(self, parent, class_dict, player):
        super().__init__(parent)
        self.class_dict = class_dict
        self.player = player
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.openMenu)

    def openMenu(self, position):
        #grab which class item is being requested
        item = self.class_dict[self.selectedItems()[0].text()]
        #make the context menu
        menu = QtWidgets.QMenu()
        #get all the client methods of that class as a dictionary
        #dictionary is in the form {'Method name' : method_object}
        item_methods = item.client_methods
        #add all the methods as QActions
        ##!!need a way of getting additional parameters if the function needs it
        ##!!for example, get_octant_biome needs the octant name
        ##!!have to be able to give that from the gui somehow
        for method in item_methods:
            text = method
            action = item_methods[method]
            newAction = menu.addAction(text)
            newAction.function = action
        #connect each to the display_alert function so that the output is shown
        try:
            menu.triggered.connect(ui.display_alert)
        except Exception as e:
            print(e)
        #implement the actions each option is linked to
        action = menu.exec_(self.mapToGlobal(position))


class Ui_Halcyon(object):

    def setupUi(self, Halcyon):
        Halcyon.setObjectName("Halcyon")
        Halcyon.resize(1200, 745)
        self.centralwidget = QtWidgets.QWidget(Halcyon)
        self.centralwidget.setObjectName("centralwidget")
        ##define planetview
        self.PlanetView = DetailView(self.centralwidget, PLANETS, 2)
        self.PlanetView.setGeometry(QtCore.QRect(10, 10, 225, 550))
        self.PlanetView.setObjectName("PlanetView")
        ##define playerview
        self.PlayerView = QtWidgets.QListWidget(self.centralwidget)
        self.PlayerView.setGeometry(QtCore.QRect(965, 10, 225, 550))
        self.PlayerView.setObjectName("PlayerView")
        ##define the octant label that says 'OctantView'
        self.OctantLabel = QtWidgets.QLabel(self.centralwidget)
        self.OctantLabel.setGeometry(QtCore.QRect(470, 0, 211, 31))
        self.OctantLabel.setStyleSheet("font: 24pt \"Sitka\";")
        self.OctantLabel.setTextFormat(QtCore.Qt.AutoText)
        self.OctantLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OctantLabel.setIndent(-1)
        self.OctantLabel.setObjectName("OctantLabel")
        ##define the central large octant view
        self.OctantView = QtWidgets.QListWidget(self.centralwidget)
        self.OctantView.setGeometry(QtCore.QRect(250, 40, 701, 521))
        self.OctantView.setObjectName("OctantView")
        ##define the alert view for messages/alerts
        self.AlertView = QtWidgets.QTextEdit(self.centralwidget)
        self.AlertView.setReadOnly(True)
        self.AlertView.setGeometry(QtCore.QRect(10, 570, 581, 121))
        self.AlertView.setObjectName("AlertView")
        ##define the task queue that shows all tasks
        self.TaskQueue = QtWidgets.QListWidget(self.centralwidget)
        self.TaskQueue.setGeometry(QtCore.QRect(610, 570, 581, 121))
        self.TaskQueue.setObjectName("TaskQueue")

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
        self.OctantLabel.setText(_translate("Halcyon", "Octant View"))
        self.menutewst.setTitle(_translate("Halcyon", "Menu"))

    def display_alert(self, alert_action):
        try:
            #get the alert, activate its function, and display the result
            self.AlertView.setHtml(alert_action.bound_function())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Halcyon = QtWidgets.QMainWindow()
    ui = Ui_Halcyon()
    ui.setupUi(Halcyon)
    ####add custom code between here####
    ui.PlanetView.addItems(list(PLANETS.keys()))
    ####add custome code above here####
    Halcyon.show()
    sys.exit(app.exec_())
