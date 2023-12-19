from PyQt5 import QtCore, QtGui, QtWidgets
import os
import xml.etree.ElementTree as ET

current_directory = os.path.dirname(__file__)
xml_file_path = os.path.join(current_directory, 'Style', 'styles.xml')

tree = ET.parse(xml_file_path)
root = tree.getroot()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 271, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(root.find('QPushButton_style/value').text)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 180, 271, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(root.find('QPushButton_style/value').text)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 300, 271, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(root.find('QPushButton_style/value').text)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 420, 271, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(root.find('QPushButton_style/value').text)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 540, 271, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(root.find('QPushButton_styleNOTWORK/value').text)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(750, 70, 271, 91))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(root.find('QPushButton_style/value').text)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(750, 190, 271, 91))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(root.find('QPushButton_styleNOTWORK/value').text)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(750, 300, 271, 91))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet(root.find('QPushButton_styleNOTWORK/value').text)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Лабораторна робота 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Лабораторна робота 2"))
        self.pushButton_3.setText(_translate("MainWindow", "Лабораторна робота 3"))
        self.pushButton_4.setText(_translate("MainWindow", "Лабораторна робота 4"))
        self.pushButton_5.setText(_translate("MainWindow", "Лабораторна робота 5"))
        self.pushButton_6.setText(_translate("MainWindow", "Лабораторна робота 6"))
        self.pushButton_7.setText(_translate("MainWindow", "Лабораторна робота 7"))
        self.pushButton_8.setText(_translate("MainWindow", "Лабораторна робота 8"))
