# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(10, 10, 711, 70))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.label_result.setObjectName("label_result")
        self.label_history = QtWidgets.QLabel(self.centralwidget)
        self.label_history.setEnabled(True)
        self.label_history.setGeometry(QtCore.QRect(730, 10, 211, 671))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.label_history.setFont(font)
        self.label_history.setTabletTracking(False)
        self.label_history.setAcceptDrops(False)
        self.label_history.setScaledContents(False)
        self.label_history.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_history.setObjectName("label_history")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 90, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(152, 90, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(294, 90, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(436, 90, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(294, 240, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtract.setGeometry(QtCore.QRect(436, 240, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_subtract.setFont(font)
        self.btn_subtract.setObjectName("btn_subtract")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(152, 240, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 240, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(294, 390, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(436, 390, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_divide.setFont(font)
        self.btn_divide.setObjectName("btn_divide")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(152, 390, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 390, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(10, 540, 142, 142))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(436, 540, 142, 142))
        font = QtGui.QFont()
        font.setFamily("Lisichka Comic")
        font.setPointSize(35)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 106, 167);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(870, 600, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 8, 0);")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(152, 540, 142, 142))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(35)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.btn_interest = QtWidgets.QPushButton(self.centralwidget)
        self.btn_interest.setGeometry(QtCore.QRect(580, 90, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_interest.setFont(font)
        self.btn_interest.setObjectName("btn_interest")
        self.btn_pow = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pow.setGeometry(QtCore.QRect(580, 240, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.btn_root = QtWidgets.QPushButton(self.centralwidget)
        self.btn_root.setGeometry(QtCore.QRect(580, 390, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_root.setFont(font)
        self.btn_root.setObjectName("btn_root")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(294, 540, 142, 142))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(580, 540, 142, 142))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btn_del.setObjectName("btn_del")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.label_history.setText(_translate("MainWindow", "Історія:"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_subtract.setText(_translate("MainWindow", "-"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_clear.setText(_translate("MainWindow", "DEL"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_interest.setText(_translate("MainWindow", "%"))
        self.btn_pow.setText(_translate("MainWindow", "^"))
        self.btn_root.setText(_translate("MainWindow", "√"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_del.setText(_translate("MainWindow", "←"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
