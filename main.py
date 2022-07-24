# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'REV03.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
from pygame import mixer  # Load the popular external library
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer

dir = os.getcwd()

#multi threading untuk nyalakan alarm
class alarmsound(QObject):
    mixer.init()
    tengm = mixer.Sound(dir + '/ICON/teng.mp3')
    nongm = mixer.Sound(dir + '/ICON/nong.mp3')
    teng = pyqtSignal()
    nong = pyqtSignal()

    def __init__(self):
        super(alarmsound, self).__init__()
        self._start = 0

    def run(self):
        while True:
            while self._start:
                self.teng.emit()
                self.tengm.play()
                time.sleep(self.tengm.get_length())

                self.nong.emit()
                self.nongm.play()
                time.sleep(self.nongm.get_length())

    def stop(self):
        self._start = 0

    def start(self):
        self._start = 1

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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(dir + "/ICON/toogle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ALARM.setIcon(icon)
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
        self.ZP1 = QtWidgets.QPushButton(self.centralwidget)
        self.ZP1.setGeometry(QtCore.QRect(290, 430, 93, 28))
        self.ZP1.setObjectName("ZP1")
        self.ZP2 = QtWidgets.QPushButton(self.centralwidget)
        self.ZP2.setGeometry(QtCore.QRect(520, 430, 93, 28))
        self.ZP2.setObjectName("ZP2")
        self.ZP3 = QtWidgets.QPushButton(self.centralwidget)
        self.ZP3.setGeometry(QtCore.QRect(940, 430, 93, 28))
        self.ZP3.setObjectName("ZP3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 41, 131, 131))
        self.frame.setStyleSheet("background-color: rgb(233, 239, 255);\n"
                                 "border-color: rgb(197, 197, 197);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ACK_REQUEST = QtWidgets.QPushButton(self.frame)
        self.ACK_REQUEST.setGeometry(QtCore.QRect(20, 35, 93, 28))
        self.ACK_REQUEST.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.ACK_REQUEST.setObjectName("ACK_REQUEST")
        self.ABCD_HDL = QtWidgets.QPushButton(self.frame)
        self.ABCD_HDL.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.ABCD_HDL.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.ABCD_HDL.setObjectName("ABCD_HDL")
        self.ACK_REQUEST_DO = QtWidgets.QLabel(self.frame)
        self.ACK_REQUEST_DO.setGeometry(QtCore.QRect(20, 104, 21, 21))
        self.ACK_REQUEST_DO.setText("")
        self.ACK_REQUEST_DO.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.ACK_REQUEST_DO.setScaledContents(True)
        self.ACK_REQUEST_DO.setObjectName("ACK_REQUEST_DO")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 107, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 12, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1351, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.JPL_KIRI = QtWidgets.QLabel(self.centralwidget)
        self.JPL_KIRI.setGeometry(QtCore.QRect(630, 319, 181, 161))
        self.JPL_KIRI.setText("")
        self.JPL_KIRI.setPixmap(QtGui.QPixmap(dir + "/ICON/LEFT-JPL-0.png"))
        self.JPL_KIRI.setScaledContents(True)
        self.JPL_KIRI.setObjectName("JPL_KIRI")
        self.JPL_KANAN = QtWidgets.QLabel(self.centralwidget)
        self.JPL_KANAN.setGeometry(QtCore.QRect(540, 494, 181, 161))
        self.JPL_KANAN.setText("")
        self.JPL_KANAN.setPixmap(QtGui.QPixmap(dir + "/ICON/RIGHT-JPL-0.png"))
        self.JPL_KANAN.setScaledContents(True)
        self.JPL_KANAN.setObjectName("JPL_KANAN")
        self.LEFT_JPL_R = QtWidgets.QLabel(self.centralwidget)
        self.LEFT_JPL_R.setGeometry(QtCore.QRect(762, 405, 10, 10))
        self.LEFT_JPL_R.setText("")
        self.LEFT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.LEFT_JPL_R.setScaledContents(True)
        self.LEFT_JPL_R.setObjectName("LEFT_JPL_R")
        self.LEFT_JPL_L = QtWidgets.QLabel(self.centralwidget)
        self.LEFT_JPL_L.setGeometry(QtCore.QRect(741, 405, 10, 10))
        self.LEFT_JPL_L.setText("")
        self.LEFT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.LEFT_JPL_L.setScaledContents(True)
        self.LEFT_JPL_L.setObjectName("LEFT_JPL_L")
        self.RIGHT_JPL_L = QtWidgets.QLabel(self.centralwidget)
        self.RIGHT_JPL_L.setGeometry(QtCore.QRect(579, 580, 10, 10))
        self.RIGHT_JPL_L.setText("")
        self.RIGHT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.RIGHT_JPL_L.setScaledContents(True)
        self.RIGHT_JPL_L.setObjectName("RIGHT_JPL_L")
        self.RIGHT_JPL_R = QtWidgets.QLabel(self.centralwidget)
        self.RIGHT_JPL_R.setGeometry(QtCore.QRect(601, 580, 10, 10))
        self.RIGHT_JPL_R.setText("")
        self.RIGHT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.RIGHT_JPL_R.setScaledContents(True)
        self.RIGHT_JPL_R.setObjectName("RIGHT_JPL_R")

        self.alarmState = 0
        self.automaticState = 0
        self.semiautomaticState = 0
        self.manualState = 0
        self.buzzerState = 0
        self.ackState = 0

        self.threadAlarm = QThread()
        self.bunyiAlarm = alarmsound()
        self.bunyiAlarm.moveToThread(self.threadAlarm)
        self.threadAlarm.started.connect(self.bunyiAlarm.run)
        self.bunyiAlarm.teng.connect(self.flip)
        self.bunyiAlarm.nong.connect(self.flop)
        self.threadAlarm.start()

        self.iconalarmon = QtGui.QIcon()
        self.iconalarmon.addPixmap(QtGui.QPixmap(dir + "/ICON/toogle-on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconalarmoff = QtGui.QIcon()
        self.iconalarmoff.addPixmap(QtGui.QPixmap(dir + "/ICON/toogle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ALARM.setIcon(self.iconalarmoff)
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
        self.ZP1.setText(_translate("MainWindow", "ZP1"))
        self.ZP2.setText(_translate("MainWindow", "ZP2"))
        self.ZP3.setText(_translate("MainWindow", "ZP3"))
        self.ACK_REQUEST.setText(_translate("MainWindow", "ACK REQUEST"))
        self.ABCD_HDL.setText(_translate("MainWindow", "A/B/C/D-HDL-DI"))
        self.label.setText(_translate("MainWindow", "ACK DO"))
        self.label_2.setText(_translate("MainWindow", "PANEL TBI"))

    def flip(self):
        self.LEFT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-red-on.png"))
        self.LEFT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.RIGHT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.RIGHT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-red-on.png"))
    def flop(self):
        self.LEFT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.LEFT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-red-on.png"))
        self.RIGHT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-red-on.png"))
        self.RIGHT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))


    def alarmStopped(self):
        self.LEFT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.LEFT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.RIGHT_JPL_L.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))
        self.RIGHT_JPL_R.setPixmap(QtGui.QPixmap(dir + "/ICON/led-off.png"))

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
        if self.alarmState:
            self.bunyiAlarm.stop()
            self.alarmStopped()

    def switchMANUAL(self):
        if self.semiautomaticState == 1:
            self.SELECTOR_SWITCH.setPixmap(QtGui.QPixmap(dir + "/ICON/selector-switch-MANUAL.png"))
            self.automaticState = 0
            self.semiautomaticState = 0
            self.manualState = 1
            self.writeModbus()
            if self.alarmState and self.manualState:
                self.bunyiAlarm.start()

    def ALARMclicked(self):
        #toogle alarm on atau off
        if self.alarmState == 1:
            self.ALARM.setIcon(self.iconalarmoff)
            self.alarmState = 0
        else:
            self.ALARM.setIcon(self.iconalarmon)
            self.alarmState = 1

        #alarm hanya bisa dinyalakan lewat toogle switch saat operasi manual
        if self.alarmState and self.manualState:
            self.bunyiAlarm.start()
        else:
            self.bunyiAlarm.stop()
            self.alarmStopped()
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
