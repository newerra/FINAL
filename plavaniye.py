# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plavaniye.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("Плавание")
        mainWindow.resize(590, 454)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 75, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 110, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 178, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 144, 81, 20))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 70, 241, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kalorii = QtWidgets.QLineEdit(self.widget)
        self.kalorii.setFocusPolicy(QtCore.Qt.NoFocus)
        self.kalorii.setObjectName("kalorii")
        self.verticalLayout.addWidget(self.kalorii)
        self.distanciya = QtWidgets.QLineEdit(self.widget)
        self.distanciya.setObjectName("distanciya")
        self.verticalLayout.addWidget(self.distanciya)
        self.time = QtWidgets.QLineEdit(self.widget)
        self.time.setObjectName("time")
        self.verticalLayout.addWidget(self.time)
        self.vid = QtWidgets.QComboBox(self.widget)
        self.vid.setObjectName("vid")
        self.verticalLayout.addWidget(self.vid)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(200, 210, 241, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vicheslit = QtWidgets.QPushButton(self.widget1)
        self.vicheslit.setObjectName("vicheslit")
        self.horizontalLayout.addWidget(self.vicheslit)
        self.sbros = QtWidgets.QPushButton(self.widget1)
        self.sbros.setObjectName("sbros")
        self.horizontalLayout.addWidget(self.sbros)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "     Калории"))
        self.label_2.setText(_translate("mainWindow", "  Дистанция"))
        self.label_4.setText(_translate("mainWindow", "         Вид"))
        self.label_5.setText(_translate("mainWindow", "       Время"))
        self.vicheslit.setText(_translate("mainWindow", "Вычислить"))
        self.sbros.setText(_translate("mainWindow", "Сброс"))