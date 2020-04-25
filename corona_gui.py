# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'corona.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import requests,os,json
from fon_lib import speak,recognize
from bs4 import BeautifulSoup 

class Ui_CoronaGui(object):
    def setupUi(self, CoronaGui):
        CoronaGui.setObjectName("CoronaGui")
        CoronaGui.resize(383, 483)
        self.centralwidget = QtWidgets.QWidget(CoronaGui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Cantarell Extra Bold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 130, 71, 71))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 60))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.action)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 200, 111, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 150, 113, 33))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.action)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 351, 250))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        CoronaGui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CoronaGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 383, 25))
        self.menubar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.menubar.setObjectName("menubar")
        CoronaGui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CoronaGui)
        self.statusbar.setObjectName("statusbar")
        CoronaGui.setStatusBar(self.statusbar)

        self.retranslateUi(CoronaGui)
        QtCore.QMetaObject.connectSlotsByName(CoronaGui)
        

    def retranslateUi(self, CoronaGui):
        _translate = QtCore.QCoreApplication.translate
        CoronaGui.setWindowTitle(_translate("CoronaGui", "Coronavirus Live"))
        self.label.setText(_translate("CoronaGui", "CoronaVirus Live"))
        self.label_3.setText(_translate("CoronaGui", "Click To Record"))
        self.label_4.setText(_translate("CoronaGui", "Coronavirus cases and deaths . Just Tell me the country ! "))
    def action(self):

        def output(country):
            country = country+"/"
            country_url = "https://www.worldometers.info/coronavirus/country/"+country
            result = requests.get(country_url)
            country_soup = BeautifulSoup(result.content,'html.parser')
            cases = country_soup.find_all(id="maincounter-wrap")
            text = str()
            if cases==[]:
                speak(" Sorry ,Could not understand you ! or there isn't such country")
            else:
                for column in cases:
                    text = text + ('{}').format(column.text)    
                self.label_2.setText(text)
                speak((('in {} ').format(country+text)))
        if self.lineEdit.text() == '':
            country = recognize()
            output(country)
        else : 
            country = self.lineEdit.text()
            output(country)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CoronaGui = QtWidgets.QMainWindow()
    ui = Ui_CoronaGui()
    ui.setupUi(CoronaGui)
    CoronaGui.show()
    speak(("Coronavirus cases and deaths . Just Tell me the country ! made by Yaseen "))
    sys.exit(app.exec_())
