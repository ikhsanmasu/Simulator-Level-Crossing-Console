# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'REV03.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

dir = os.getcwd()

#input variable
alarmState = 0
automaticState = 0
semiautomaticState = 0
manualState = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1351, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CONSOLE = QtWidgets.QLabel(self.centralwidget)
        self.CONSOLE.setGeometry(QtCore.QRect(0, 0, 1351, 831))
        self.CONSOLE.setText("")
        self.CONSOLE.setPixmap(QtGui.QPixmap(dir + "/ICON/Console.jpg"))
        self.CONSOLE.setScaledContents(True)
        self.CONSOLE.setObjectName("CONSOLE")
        self.ACKNOWLEDGE = QtWidgets.QPushButton(self.centralwidget)
        self.ACKNOWLEDGE.setGeometry(QtCore.QRect(837, 686, 60, 60))
        self.ACKNOWLEDGE.setText("")
        self.ACKNOWLEDGE.setFlat(True)
        self.ACKNOWLEDGE.setObjectName("ACKNOWLEDGE")
        self.BRAKE = QtWidgets.QPushButton(self.centralwidget)
        self.BRAKE.setGeometry(QtCore.QRect(1021, 686, 60, 60))
        self.BRAKE.setText("")
        self.BRAKE.setFlat(True)
        self.BRAKE.setObjectName("BRAKE")
        self.OPEN_BARIER = QtWidgets.QPushButton(self.centralwidget)
        self.OPEN_BARIER.setGeometry(QtCore.QRect(1116, 686, 60, 60))
        self.OPEN_BARIER.setText("")
        self.OPEN_BARIER.setFlat(True)
        self.OPEN_BARIER.setObjectName("OPEN_BARIER")
        self.CLOSE_BARRIER = QtWidgets.QPushButton(self.centralwidget)
        self.CLOSE_BARRIER.setGeometry(QtCore.QRect(1211, 686, 60, 60))
        self.CLOSE_BARRIER.setText("")
        self.CLOSE_BARRIER.setFlat(True)
        self.CLOSE_BARRIER.setObjectName("CLOSE_BARRIER")
        self.BUZZER = QtWidgets.QLabel(self.centralwidget)
        self.BUZZER.setGeometry(QtCore.QRect(423, 633, 41, 41))
        self.BUZZER.setText("")
        self.BUZZER.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.BUZZER.setScaledContents(True)
        self.BUZZER.setObjectName("BUZZER")
        self.COMMUNICATION = QtWidgets.QLabel(self.centralwidget)
        self.COMMUNICATION.setGeometry(QtCore.QRect(844, 287, 21, 21))
        self.COMMUNICATION.setText("")
        self.COMMUNICATION.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.COMMUNICATION.setScaledContents(True)
        self.COMMUNICATION.setObjectName("COMMUNICATION")
        self.BARIER_DOWN = QtWidgets.QLabel(self.centralwidget)
        self.BARIER_DOWN.setGeometry(QtCore.QRect(844, 227, 21, 21))
        self.BARIER_DOWN.setText("")
        self.BARIER_DOWN.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.BARIER_DOWN.setScaledContents(True)
        self.BARIER_DOWN.setObjectName("BARIER_DOWN")
        self.BARIER_UP = QtWidgets.QLabel(self.centralwidget)
        self.BARIER_UP.setGeometry(QtCore.QRect(844, 197, 21, 21))
        self.BARIER_UP.setText("")
        self.BARIER_UP.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.BARIER_UP.setScaledContents(True)
        self.BARIER_UP.setObjectName("BARIER_UP")
        self.POWER = QtWidgets.QLabel(self.centralwidget)
        self.POWER.setGeometry(QtCore.QRect(1028, 197, 21, 21))
        self.POWER.setText("")
        self.POWER.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.POWER.setScaledContents(True)
        self.POWER.setObjectName("POWER")
        self.DIRECTION_A = QtWidgets.QLabel(self.centralwidget)
        self.DIRECTION_A.setGeometry(QtCore.QRect(196, 456, 63, 73))
        self.DIRECTION_A.setText("")
        self.DIRECTION_A.setPixmap(QtGui.QPixmap(dir + "/ICON/direction-a-off.png"))
        self.DIRECTION_A.setScaledContents(True)
        self.DIRECTION_A.setObjectName("DIRECTION_A")
        self.DIRECTION_B = QtWidgets.QLabel(self.centralwidget)
        self.DIRECTION_B.setGeometry(QtCore.QRect(1090, 456, 64, 73))
        self.DIRECTION_B.setText("")
        self.DIRECTION_B.setPixmap(QtGui.QPixmap(dir + "/ICON/direction-b-off.png"))
        self.DIRECTION_B.setScaledContents(True)
        self.DIRECTION_B.setObjectName("DIRECTION_B")
        self.BUZZER_STOP = QtWidgets.QPushButton(self.centralwidget)
        self.BUZZER_STOP.setGeometry(QtCore.QRect(420, 690, 51, 51))
        self.BUZZER_STOP.setText("")
        self.BUZZER_STOP.setFlat(True)
        self.BUZZER_STOP.setObjectName("BUZZER_STOP")
        self.ALARM = QtWidgets.QPushButton(self.centralwidget)
        self.ALARM.setGeometry(QtCore.QRect(496, 212, 75, 71))
        self.ALARM.setText("")
        self.ALARM.setIconSize(QtCore.QSize(70, 70))
        self.ALARM.setObjectName("ALARM")
        self.AUTOMATIC = QtWidgets.QPushButton(self.centralwidget)
        self.AUTOMATIC.setGeometry(QtCore.QRect(82, 621, 101, 31))
        self.AUTOMATIC.setText("")
        self.AUTOMATIC.setFlat(True)
        self.AUTOMATIC.setObjectName("AUTOMATIC")
        self.SEMI_AUTOMATIC = QtWidgets.QPushButton(self.centralwidget)
        self.SEMI_AUTOMATIC.setGeometry(QtCore.QRect(192, 683, 101, 31))
        self.SEMI_AUTOMATIC.setText("")
        self.SEMI_AUTOMATIC.setFlat(True)
        self.SEMI_AUTOMATIC.setObjectName("SEMI_AUTOMATIC")
        self.MANUAL = QtWidgets.QPushButton(self.centralwidget)
        self.MANUAL.setGeometry(QtCore.QRect(82, 742, 101, 31))
        self.MANUAL.setText("")
        self.MANUAL.setFlat(True)
        self.MANUAL.setObjectName("MANUAL")
        self.SELECTOR_SWITCH = QtWidgets.QLabel(self.centralwidget)
        self.SELECTOR_SWITCH.setGeometry(QtCore.QRect(92, 655, 85, 85))
        self.SELECTOR_SWITCH.setText("")
        self.SELECTOR_SWITCH.setPixmap(QtGui.QPixmap(dir + "/ICON/selector-switch-AUTOMATIC.png"))
        self.SELECTOR_SWITCH.setScaledContents(True)
        self.SELECTOR_SWITCH.setObjectName("SELECTOR_SWITCH")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1351, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
#Tambahan
        self.ALARM.setIconSize(QtCore.QSize(70, 70))
        self.ALARM.setObjectName("alrm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1351, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.alarmState = 0
        self.automaticState = 0
        self.semiautomaticState = 0
        self.manualState = 0
        self.buzzerState = 0
        self.ackState = 0

        self.iconon = QtGui.QIcon()
        self.iconon.addPixmap(QtGui.QPixmap(dir + "/ICON/toogle-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconoff = QtGui.QIcon()
        self.iconoff.addPixmap(QtGui.QPixmap(dir + "/ICON/toogle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ALARM.setIcon(self.iconon)
        self.ALARM.clicked.connect(self.ALARMclicked)

        self.AUTOMATIC.clicked.connect(self.switchAUTO)
        self.SEMI_AUTOMATIC.clicked.connect(self.switchSEMI)
        self.MANUAL.clicked.connect(self.switchMANUAL)

        self.BUZZER_STOP.pressed.connect(self.buzzerPressed)
        self.BUZZER_STOP.released.connect(self.buzzerReleased)

        self.ACKNOWLEDGE.pressed.connect(self.ackPressed)
        self.ACKNOWLEDGE.released.connect(self.ackReleased)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def switchAUTO(self):
        if self.semiautomaticState == 1:
            self.SELECTOR_SWITCH.setPixmap(QtGui.QPixmap(dir + "/ICON/selector-switch-AUTOMATIC.png"))
            self.automaticState = 1
            self.semiautomaticState = 0
            self.manualState = 0
            self.writeModbus()

    def switchSEMI(self):
        self.SELECTOR_SWITCH.setPixmap(QtGui.QPixmap(dir + "/ICON/selector-switch-SEMI AUTOMATIC.png"))
        self.automaticState = 0
        self.semiautomaticState = 1
        self.manualState = 0
        self.writeModbus()

    def switchMANUAL(self):
        if self.semiautomaticState == 1:
            self.SELECTOR_SWITCH.setPixmap(QtGui.QPixmap(dir + "/ICON/selector-switch-MANUAL.png"))
            self.automaticState = 0
            self.semiautomaticState = 0
            self.manualState = 1
            self.writeModbus()


    def ALARMclicked(self):
        if self.alarmState == 1:
            self.ALARM.setIcon(self.iconoff)
            self.alarmState = 0
        else:
            self.ALARM.setIcon(self.iconon)
            self.alarmState = 1
        self.writeModbus()

    def buzzerPressed(self):
        self.buzzerState = 1
        self.writeModbus()

    def buzzerReleased(self):
        self.buzzerState = 0
        self.writeModbus()

    def ackPressed(self):
        self.backState = 1
        self.writeModbus()

    def ackReleased(self):
        self.ackState = 0
        self.writeModbus()

    def writeModbus(self):
        print(self.buzzerState)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
