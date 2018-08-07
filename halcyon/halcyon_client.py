from PyQt5 import QtCore, QtGui, QtWidgets

import pika
import sys
import datetime, time
import dill as pickle

from initialize_game import save_to_file

def client_load_gamestate():
    global planets
    global tasks
    global players
    with open('gamestate.pickle', 'rb') as handle:
        superlist = pickle.load(handle)
    planets = superlist[0]
    tasks = superlist[1]
    players = superlist[2]
    ui.PlanetView.clear()
    ui.PlanetView.add_class_items(planets)
    ui.PlayerView.clear()
    ui.PlayerView.add_class_items(players)
    ui.TaskView.clear()
    ui.TaskView.add_class_items(tasks)

def filter_player_vision(class_items):
    '''Takes an input of class items and returns only the ones that the current player has vision of'''
    filtered_dict = {}
    for item_name in class_items:
        class_obj = class_items[item_name]
        if class_obj.player.name == current_player:
            filtered_dict[item_name] = class_obj
    return filtered_dict

def check_octant_vision(octant_class_items):
    '''Takes an input of class items- the contents of a given octant- and checks if the current player has vision'''
    for item_name in octant_class_items:
        class_obj = octant_class_items[item_name]
        try:
            if class_obj.player.name == current_player:
                return True
        #if theres an object in the octant with no player
        except:
            continue
    return False

class LoginDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Login')
        self.setGeometry(QtCore.QRect(500, 500, 200, 200))
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.loginButton = QtWidgets.QPushButton('Login', self)
        self.loginButton.clicked.connect(self.handle_login)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.loginButton)

    def handle_login(self):
        userpass = {'Gamemaster' : 'gm'}
        username = self.textName.text()
        password = self.textPass.text()
        if (username in userpass and
            userpass[username] == password):
            global current_player
            current_player = self.textName.text()
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect user or password')

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
    '''View class for seeing the contents of given octant
    '''

    def __init__(self, parent):
        super().__init__(parent)
        self.current_octant = None
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_menu)

    def create_building_plan(self, menu_object, creator):
        #set the SMDialog to the Dialog we'll be using for the building plan creator
        SMDialog = QtWidgets.QDialog(self)
        SMDialog.setGeometry(QtCore.QRect(700, 500, 500, 500))
        SMDialog.setWindowTitle('Create Building Plan')
        #add the label
        CBPLabel = QtWidgets.QLabel('Double-click the tags you wish to apply to the building you are creating.',
                                    parent=SMDialog)
        CBPLabel.setGeometry(QtCore.QRect(0, 0, 500, 25))
        CBPLabel.setIndent(85)
        #add the box for the NameBox
        self.CBPNameBox = QtWidgets.QLineEdit(SMDialog)
        self.CBPNameBox.setGeometry(QtCore.QRect(200, 300, 100, 20))
        #set up MaterialList
        MaterialList = QtWidgets.QListWidget(SMDialog)
        MaterialList.setGeometry(QtCore.QRect(0, 25, 100, 250))
        #when item clicked, get the item row, remove the item by row, add the item to ActiveList
        MaterialList.itemDoubleClicked.connect(lambda x:
                                                self.ActiveList.addItem(
                                                MaterialList.takeItem(
                                                MaterialList.row(x))))
        #set up StructureList
        StructureList = QtWidgets.QListWidget(SMDialog)
        StructureList.setGeometry(QtCore.QRect(200, 25, 100, 250))
        StructureList.itemDoubleClicked.connect(lambda x:
                                                self.ActiveList.addItem(
                                                StructureList.takeItem(
                                                StructureList.row(x))))
        #set up FunctionList
        FunctionList = QtWidgets.QListWidget(SMDialog)
        FunctionList.setGeometry(QtCore.QRect(400, 25, 100, 250))
        FunctionList.itemDoubleClicked.connect(lambda x:
                                                self.ActiveList.addItem(
                                                FunctionList.takeItem(
                                                FunctionList.row(x))))
        ##below here add all possible tags##
        kuh = QtWidgets.QListWidgetItem('KUH')
        kuh.home_list = MaterialList
        MaterialList.addItem(kuh)
        #####################################
        #set up ActiveList that shows which tags are active
        self.ActiveList = QtWidgets.QListWidget(SMDialog)
        self.ActiveList.setGeometry(QtCore.QRect(100, 350, 300, 100))
        #on double click, access the homelist of the item and return it
        self.ActiveList.itemDoubleClicked.connect(lambda x:
                                                x.home_list.addItem(
                                                self.ActiveList.takeItem(
                                                self.ActiveList.row(x))))
        #set it up so that it works as a menu button
        menu = menu_object
        CBPAction = menu.addAction('Create Building Plan')
        CBPAction.bound_function = SMDialog.show
        #set up the QPushButton
        CBPButton = QtWidgets.QPushButton(SMDialog)
        CBPButton.setGeometry(QtCore.QRect(200, 450, 100, 50))
        CBPButton.setText('Create plan')
        #set up the stuff to send to the trigger_CBP_button
        self.creator = creator
        CBPButton.clicked.connect(self.trigger_CBP_button)

    def trigger_CBP_button(self):
        self.creator.plan_name = self.CBPNameBox
        self.creator.plan_tags = []
        for index in range(self.ActiveList.count()):
            self.creator.plan_tags.append(self.ActiveList.item(index).text())
        print(self.creator.plan_tags)
        #self.creator.make_building_plan()

    def open_menu(self, position):
        #grab which class item is being requested by selection
        try:
            item = self.selectedItems()[0].class_obj
        #if there's nothing selected, set the default to the first item
        except:
            if self.item(0) == None:
                return
            else:
                item = self.item(0).class_obj
        #make the context menu
        menu = QtWidgets.QMenu()
        #get all the client methods of that class as a tuple of tuples
        item_methods = item.client_methods
        #add all the methods as QActions
        for method in item_methods:
            #check if it's a special-case method
            #works via checking if there's just method text or is there more
            try:
                method_text = method[0]
                method_function = method[1]
                method_parameters = method[2]
                method_statechange = method[3]
            except Exception as e:
                print('Special method detected %s' % method_text)
                if method_text == 'Create Building Plan':
                    self.create_building_plan(menu, item)
                continue
            if method_parameters:
                #add a an additional menu to the main menu
                parameterMenu = menu.addMenu(method_text)
                #to the secondary menu, add the parameters as actions
                for parameter in method_parameters:
                    try:
                        parameterAction = parameterMenu.addAction(parameter)
                        parameterAction.bound_function = method_function
                        parameterAction.bound_parameter = parameter
                        parameterAction.statechange = method_statechange
                    except Exception as e:
                        print(e)
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
        if check_octant_vision(name_object_dict):
            self.add_class_items(name_object_dict)

class PlanetDialog(QtWidgets.QDialog):

    def __init__(self, octant_view):
        super().__init__()
        dialog = QtWidgets.QDialog(Halcyon)
        dialog.setGeometry(QtCore.QRect(500, 500, 200, 200))
        dialog.setWindowTitle('Select Octant')
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

class ActionThread(QtCore.QThread):

    def run(self):
        while True:
            if (datetime.datetime.utcnow().minute == 30
            or datetime.datetime.utcnow().minute == 00):
                print('Actions launched! Loading new gamestate...')
                time.sleep(10)
                client_load_gamestate()
            time.sleep(30)

class ActionDock():

    def __init__(self):
        self.dock = []

    def launch_action(self, action_ship):
        #need to launch the action to the rabbitmq queue
        #first serializes the action with dill
        #then sends the serialized text to the queue
        #serialize the action ship
        serialized_action = pickle.dumps(action_ship)
        ##RabbitMQ queue##
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='action')
        channel.basic_publish(exchange='',
                              routing_key='action',
                              body=serialized_action)
        print("Sent serialized action to server")
        connection.close()
        ui.ActionDockView.addItem(action_ship[0] + ' at next half-hour interval')
        #clear the ActionDockView
        ui.ActionDockView.clear()

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
        ##define the ActionDock that runs in the background
        ##manages sending actions to the server every 30 minutes
        self.ActionDock = ActionDock()
        ##define the ActionDockView that shows the actions that are going to be sent to the server
        self.ActionDockView = QtWidgets.QListWidget(self.centralwidget)
        self.ActionDockView.setGeometry(QtCore.QRect(610, 570, 270, 121))
        self.ActionDockView.setObjectName("ActionDockView")
        ##define the TaskView that shows tasks that are already active in the gamestate
        self.TaskView = DetailView(self.centralwidget, 'placeholder')
        self.TaskView.setGeometry(QtCore.QRect(900, 570, 290, 121))
        self.TaskView.setObjectName("TaskView")

        Halcyon.setCentralWidget(self.centralwidget)

        self.retranslateUi(Halcyon)
        QtCore.QMetaObject.connectSlotsByName(Halcyon)

    def retranslateUi(self, Halcyon):
        _translate = QtCore.QCoreApplication.translate
        Halcyon.setWindowTitle(_translate("Halcyon", "Halcyon -- Client"))
        self.OctantSelect.setText(_translate("Halcyon", "Select Octant"))

    def cause_action(self, action):
        '''The unique functions
        Return so it doesn't go through the result
        '''
        if action.text() == 'Create Building Plan':
            return action.bound_function()
        '''Sets the AlertView to show the results of the alert_actionself.
        If there is a .bound_parameter to the alert_action:
        pass the bound_function with the parameter
        Else, just pass the bound_function naked
        Either way, set AlertView to display the result
        '''
        statechange_prefix = 'Action docked: '
        if action.bound_parameter and not action.statechange:
            self.AlertView.setHtml(action.bound_function(action.bound_parameter))
        elif not action.bound_parameter and not action.statechange:
            self.AlertView.setHtml(action.bound_function())
        elif action.bound_parameter and action.statechange:
            returned_action_text = action.bound_function(action.bound_parameter)
            self.AlertView.setHtml(statechange_prefix + returned_action_text)
            action_ship = (returned_action_text, action.bound_function, action.bound_parameter)
            self.ActionDock.launch_action(action_ship)
        elif not action.bound_parameter and action.statechange:
            returned_action_text = action.bound_function(action.bound_parameter)
            self.AlertView.setHtml(statechange_prefix + returned_action_text)
            action_ship = (returned_action_text, action.bound_function, action.bound_parameter)
            self.ActionDock.launch_action(action_ship)

if __name__ == "__main__":
    import sys
    #setup the GUI basics
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('halcyonicon.png'))
    Halcyon = QtWidgets.QMainWindow()
    ui = Ui_Halcyon()
    ui.setupUi(Halcyon)
    #start the login dialog
    ##login = LoginDialog()
    #if login credentials are correct
    ##if login.exec_() == QtWidgets.QDialog.Accepted:
    #loads gamestate from file and updates all views
    client_load_gamestate()
    current_player = 'Gamemaster'
    #starts the ActionLoop
    thread = ActionThread()
    thread.start()
    #starts the main app
    Halcyon.show()
    sys.exit(app.exec_())
