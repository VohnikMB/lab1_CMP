import sys
import ASCII_ART_Func
from PyQt5 import QtCore, QtGui, QtWidgets

def _init_():
    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(833, 587)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
            self.textBrowser.setGeometry(QtCore.QRect(20, 20, 791, 441))
            self.textBrowser.setObjectName("textBrowser")
            self.textBrowser.setFont(QtGui.QFont("Consolas", 12))
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit.setGeometry(QtCore.QRect(20, 470, 571, 91))
            self.lineEdit.setObjectName("lineEdit")
            font = QtGui.QFont()
            font.setPointSize(22)
            self.lineEdit.setFont(font)
            self.saveButton = QtWidgets.QPushButton(self.centralwidget)
            self.saveButton.setGeometry(QtCore.QRect(690, 470, 121, 91))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.saveButton.setFont(font)
            self.saveButton.setObjectName("saveButton")
            self.symbolcomboBox = QtWidgets.QComboBox(self.centralwidget)
            self.symbolcomboBox.setGeometry(QtCore.QRect(610, 470, 71, 41))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.symbolcomboBox.setFont(font)
            self.symbolcomboBox.setObjectName("symbolcomboBox")
            self.symbolcomboBox.addItem("")
            self.symbolcomboBox.addItem("")
            self.symbolcomboBox.addItem("")
            self.formatButton = QtWidgets.QPushButton(self.centralwidget)
            self.formatButton.setGeometry(QtCore.QRect(604, 522, 81, 41))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.formatButton.setFont(font)
            self.formatButton.setObjectName("formatButton")
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
            self.addFunc()


        def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "ASCII ART"))
            self.saveButton.setText(_translate("MainWindow", "Зберегти"))
            self.symbolcomboBox.setItemText(0, _translate("MainWindow", "#"))
            self.symbolcomboBox.setItemText(1, _translate("MainWindow", "*"))
            self.symbolcomboBox.setItemText(2, _translate("MainWindow", "@"))
            self.formatButton.setText(_translate("MainWindow", "Формат"))

        def addFunc(self):
            self.lineEdit.textChanged.connect(lambda: ASCII_ART_Func.update_text_browser(self.textBrowser, self.lineEdit, self.symbolcomboBox))
            self.saveButton.clicked.connect(lambda: ASCII_ART_Func.saveFunc(self.textBrowser))
            self.symbolcomboBox.activated.connect(lambda: ASCII_ART_Func.update_text_browser(self.textBrowser, self.lineEdit, self.symbolcomboBox))
            self.formatButton.clicked.connect(lambda: ASCII_ART_Func.formatFunc(self.textBrowser, self.lineEdit, self.symbolcomboBox))

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
