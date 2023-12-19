import sys
from BLL import ASCII_ART_Func
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget

class Lab4MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ASCII ART")
        self.setGeometry(0, 0, 833, 587)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

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
        font.setPointSize(14)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.symbolcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.symbolcomboBox.setGeometry(QtCore.QRect(610, 470, 71, 41))
        font.setPointSize(16)
        self.symbolcomboBox.setFont(font)
        self.symbolcomboBox.setObjectName("symbolcomboBox")
        self.symbolcomboBox.addItem("")
        self.symbolcomboBox.addItem("")
        self.symbolcomboBox.addItem("")
        self.formatButton = QtWidgets.QPushButton(self.centralwidget)
        self.formatButton.setGeometry(QtCore.QRect(604, 522, 81, 41))
        font.setPointSize(14)
        self.formatButton.setFont(font)
        self.formatButton.setObjectName("formatButton")


        self.retranslateUi()
        self.addFunc()

    def retranslateUi(self):

        self.saveButton.setText("Зберегти")
        self.symbolcomboBox.setItemText(0,  "#")
        self.symbolcomboBox.setItemText(1,  "*")
        self.symbolcomboBox.setItemText(2,  "@")
        self.formatButton.setText("Формат")

    def addFunc(self):
        self.lineEdit.textChanged.connect(
            lambda: ASCII_ART_Func.update_text_browser_nonFiglet(self.textBrowser, self.lineEdit, self.symbolcomboBox))
        self.saveButton.clicked.connect(lambda: ASCII_ART_Func.saveFunc(self.textBrowser))
        self.symbolcomboBox.activated.connect(
            lambda: ASCII_ART_Func.update_text_browser_nonFiglet(self.textBrowser, self.lineEdit, self.symbolcomboBox))
        self.formatButton.clicked.connect(
            lambda: ASCII_ART_Func.formatFunc_nonFiglet(self.textBrowser, self.lineEdit, self.symbolcomboBox))
