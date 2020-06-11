# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ground_station.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 857)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #0f0f0f;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: white;\n"
"border-radius: 3.5em;\n"
"margin: 2.5em 4em;\n"
"max-width: 30em;\n"
"max-height: 17em;")
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setStyleSheet("background-color: white;\n"
"border-radius: 3.5em;\n"
"margin: 2.5em 4em;\n"
"max-width: 30em;\n"
"max-height: 17em;")
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setMaximumSize(QtCore.QSize(300, 287))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget1, 2, 1, 1, 1)
        self.gridWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget_5.setStyleSheet("background-color: white;\n"
"border-radius: 1.5em;\n"
"margin: 4em;\n"
"max-height: 8em")
        self.gridWidget_5.setObjectName("gridWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridWidget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout.addWidget(self.gridWidget_5, 3, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setStyleSheet("background-color: white;\n"
"border-radius: 3.5em;\n"
"margin: 2.5em 4em;\n"
"max-width: 30em;\n"
"max-height: 17em;")
        self.widget2.setObjectName("widget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.widget2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget2, 2, 2, 1, 1)
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setStyleSheet("background-color: white;\n"
"border-radius: 3.5em;\n"
"margin: 2.5em 5em;\n"
"max-width: 25em;")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_4 = QtWidgets.QLabel(self.gridWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.gridWidget, 1, 0, 3, 1)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setStyleSheet("background-color: white;\n"
"border-radius: 3.5em;\n"
"margin: 2.5em 4em;\n"
"max-width: 30em;\n"
"max-height: 17em;")
        self.widget3.setObjectName("widget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget3, 1, 1, 1, 1)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setStyleSheet("background-color: white;\n"
"border-radius: 5em;\n"
"margin: 2.5em 4em;\n"
"max-height: 15em;")
        self.widget4.setObjectName("widget4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout.addWidget(self.widget4, 3, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">2.5</span></p><p align=\"center\"><span style=\" font-size:16pt;\">G-force (m/s</span><span style=\" font-size:16pt; vertical-align:super;\">2</span><span style=\" font-size:16pt;\">)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">50</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Pressure (psi)</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">304</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Speed (kl/s)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">68°</span></p><p align=\"center\"><span style=\" font-size:20pt;\">Cubesat</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">102°</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:400;\">Battery</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">102°</span></p><p align=\"center\"><span style=\" font-size:20pt;\">Motor</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">9,000</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Alititude (ft)</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
