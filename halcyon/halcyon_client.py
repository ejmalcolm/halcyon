from PyQt5 import QtCore, QtGui, QtWidgets

import dill as pickle

def get_gamestate():
    global planets
    global tasks
    global players
    with open('gamestate.pickle', 'rb') as handle:
        superlist = pickle.load(handle)
    planets = superlist[0]
    tasks = superlist[1]
    players = superlist[2]

class DetailView(QtWidgets.QListWidget):
    '''The class for displaying lists of class objects
    Includes context menus for each class object displayed
    '''

    def __init__(self, parent, player):
        super().__init__(parent)
        self.player = player
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_menu)

    def add_class_items(self, item_dict):
        for item_name in item_dict:
            qt_item_widget = QtWidgets.QListWidgetItem(item_name)
            self.addItem(qt_item_widget)
            qt_item_widget.class_obj = item_dict[item_name]

    def open_menu(self, position):
        #grab which class item is being requested by selection
        try:
            item = self.selectedItems()[0].class_obj
        #if there's nothing selected, set the default to the first item
        except Exception as e:
            item = self.item(0).class_obj
        #make the context menu
        menu = QtWidgets.QMenu()
        #get all the client methods of that class as a tuple of tuples
        item_methods = item.client_methods
        #add all the methods as QActions
        for method in item_methods:
            method_text = method[0]
            method_function = method[1]
            method_parameters = method[2]
            method_statechange = method[3]
            if method_parameters:
                #add a an additional menu to the main menu
                parameterMenu = menu.addMenu(method_text)
                #to the secondary menu, add the parameters as actions
                for parameter in method_parameters:
                    parameterAction = parameterMenu.addAction(parameter)
                    parameterAction.bound_function = method_function
                    parameterAction.bound_parameter = parameter
                    parameterAction.statechange = method_statechange
            else:
                baseAction = menu.addAction(method_text)
                baseAction.bound_function = method_function
                #set parameter to None so it can be checked later
                baseAction.bound_parameter = None
                baseAction.statechange = method_statechange
        #connect each to the display_alert function so that the output is shown
        menu.triggered.connect(ui.cause_action)
        #implement the actions each option is linked to
        action = menu.exec_(self.mapToGlobal(position))

class OctantView(QtWidgets.QListWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.current_octant = None
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_menu)

    def open_menu(self, position):
        #grab which class item is being requested by selection
        try:
            item = self.selectedItems()[0].class_obj
        #if there's nothing selected, set the default to the first item
        except Exception as e:
            item = self.item(0).class_obj
        #make the context menu
        menu = QtWidgets.QMenu()
        #get all the client methods of that class as a tuple of tuples
        item_methods = item.client_methods
        #add all the methods as QActions
        for method in item_methods:
            method_text = method[0]
            method_function = method[1]
            method_parameters = method[2]
            method_statechange = method[3]
            if method_parameters:
                #add a an additional menu to the main menu
                parameterMenu = menu.addMenu(method_text)
                #to the secondary menu, add the parameters as actions
                for parameter in method_parameters:
                    parameterAction = parameterMenu.addAction(parameter)
                    parameterAction.bound_function = method_function
                    parameterAction.bound_parameter = parameter
                    parameterAction.statechange = method_statechange
            else:
                baseAction = menu.addAction(method_text)
                baseAction.bound_function = method_function
                #set parameter to None so it can be checked later
                baseAction.bound_parameter = None
                baseAction.statechange = method_statechange
        #connect each to the display_alert function so that the output is shown
        menu.triggered.connect(ui.cause_action)
        #implement the actions each option is linked to
        action = menu.exec_(self.mapToGlobal(position))

    def add_class_items(self, item_dict):
        for item_name in item_dict:
            qt_item_widget = QtWidgets.QListWidgetItem(item_name)
            self.addItem(qt_item_widget)
            qt_item_widget.class_obj = item_dict[item_name]

    def view_octant(self, octant_obj):
        self.clear()
        self.current_octant = octant_obj
        contents = octant_obj.contents
        names = [str(obj) for obj in contents]
        name_object_dict = {key: value for key, value in zip(names, contents)}
        self.add_class_items(name_object_dict)

class PlanetDialog(QtWidgets.QDialog):

    def __init__(self, octant_view):
        super().__init__()
        dialog = QtWidgets.QDialog(Halcyon)
        dialog.setGeometry(QtCore.QRect(500, 500, 200, 200))
        self.planet_display = QtWidgets.QComboBox(dialog)
        self.planet_display.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.planet_display.addItems(planets)

        self.octant_display = QtWidgets.QComboBox(dialog)
        self.octant_display.setGeometry(QtCore.QRect(0, 50, 200, 20))
        self.octant_display.addItems(['North', 'Northeast', 'East', 'Southeast', 'South', 'Southwest', 'West', 'Northwest'])

        self.select_button = QtWidgets.QPushButton(dialog)
        self.select_button.setGeometry(QtCore.QRect(50, 115, 100, 30))
        self.select_button.setText('Display Octant')
        self.select_button.clicked.connect(lambda x: self.change_view(x))
        dialog.show()

    def change_view(self, bool):
        self.octant_view = ui.OctantView
        planet_str = self.planet_display.currentText()
        octant_str = self.octant_display.currentText()
        planet = planets[planet_str]
        octant = planet.octants[octant_str]
        self.octant_view.view_octant(octant)

class Ui_Halcyon(object):

    def setupUi(self, Halcyon):
        Halcyon.setObjectName("Halcyon")
        Halcyon.resize(1200, 745)
        self.centralwidget = QtWidgets.QWidget(Halcyon)
        self.centralwidget.setObjectName("centralwidget")
        ##define planetview
        self.PlanetView = DetailView(self.centralwidget, 'placeholder')
        self.PlanetView.setGeometry(QtCore.QRect(10, 10, 225, 550))
        self.PlanetView.setObjectName("PlanetView")
        #add the "view octant in OctantView" option
        ##define playerview
        self.PlayerView = DetailView(self.centralwidget, 'placeholder')
        self.PlayerView.setGeometry(QtCore.QRect(965, 10, 225, 550))
        self.PlayerView.setObjectName("PlayerView")
        ##define the octant selector that controls the octantview
        self.OctantSelect = QtWidgets.QPushButton(self.centralwidget)
        self.OctantSelect.clicked.connect(PlanetDialog)
        self.OctantSelect.setGeometry(QtCore.QRect(470, 0, 211, 31))
        self.OctantSelect.setStyleSheet("font: 15pt \"Sitka\";")
        self.OctantSelect.setObjectName("OctantSelect")
        ##define the central large octant view
        self.OctantView = OctantView(self.centralwidget)
        self.OctantView.setGeometry(QtCore.QRect(250, 40, 701, 521))
        self.OctantView.setObjectName("OctantView")
        ##define the alert view for messages/alerts
        self.AlertView = QtWidgets.QTextEdit(self.centralwidget)
        self.AlertView.setReadOnly(True)
        self.AlertView.setGeometry(QtCore.QRect(10, 570, 581, 121))
        self.AlertView.setObjectName("AlertView")
        self.AlertView.setFontPointSize(20)
        ##define the task queue that shows all tasks
        self.TaskView = DetailView(self.centralwidget, 'placeholder')
        self.TaskView.setGeometry(QtCore.QRect(610, 570, 581, 121))
        self.TaskView.setObjectName("TaskView")

        Halcyon.setCentralWidget(self.centralwidget)

        self.retranslateUi(Halcyon)
        QtCore.QMetaObject.connectSlotsByName(Halcyon)

    def retranslateUi(self, Halcyon):
        _translate = QtCore.QCoreApplication.translate
        Halcyon.setWindowTitle(_translate("Halcyon", "Halcyon -- Client"))
        self.OctantSelect.setText(_translate("Halcyon", "Select Octant"))

    def cause_action(self, action):
        '''Sets the AlertView to show the results of the alert_actionself.
        If there is a .bound_parameter to the alert_action:
        pass the bound_function with the parameter
        Else, just pass the bound_function naked
        Either way, set Alertview to display the result
        '''
        statechange_prefix = 'This action will be launched at the next half-hour mark: '
        if action.bound_parameter and not action.statechange:
            self.AlertView.setHtml(action.bound_function(action.bound_parameter))
        elif not action.bound_parameter and not action.statechange:
            self.AlertView.setHtml(action.bound_function())
        elif action.bound_parameter and action.statechange:
            self.AlertView.setHtml(statechange_prefix + action.bound_function(action.bound_parameter))
            #ActionDock.dock_action(action)
        elif not action.bound_parameter and action.statechange:
            self.AlertView.setHtml(statechange_prefix + action.bound_function())
            #ActionDock.dock_action(action)

if __name__ == "__main__":
    import sys
    get_gamestate()
    app = QtWidgets.QApplication(sys.argv)
    Halcyon = QtWidgets.QMainWindow()
    ui = Ui_Halcyon()
    ui.setupUi(Halcyon)
    ####add custom code between here####
    ui.PlanetView.add_class_items(planets)
    ui.PlayerView.add_class_items(players)
    ui.TaskView.add_class_items(tasks)
    ####add custome code above here####
    Halcyon.show()
    sys.exit(app.exec_())
