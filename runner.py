import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.menu import Ui_MainWindow
from UI.lab1 import Lab1MainWindow
from UI.lab2 import Lab2MainWindow
from UI.lab3 import Lab3MainWindow
from UI.lab4 import Lab4MainWindow
class MenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_lab1_function)
        self.pushButton_2.clicked.connect(self.login_lab2_function)
        self.pushButton_3.clicked.connect(self.login_lab3_function)
        self.pushButton_4.clicked.connect(self.login_lab4_function)
        self.pushButton_6.clicked.connect(self.login_lab6_function)

    def login_lab1_function(self):
        self.window = Lab1MainWindow()
        self.window.show()
    def login_lab2_function(self):
        self.window = Lab2MainWindow()
        self.window.show()
    def login_lab3_function(self):
        self.window = Lab3MainWindow()
        self.window.show()

    def login_lab4_function(self):
        self.window = Lab4MainWindow()
        self.window.show()

    def login_lab6_function(self):
        from BLL.Unit_Test import unittest_box
        unittest_box()

if __name__ == '__main__':
    # Ініціалізація додатку та головного вікна
    app = QApplication(sys.argv)
    login_window = MenuWindow()
    login_window.show()
    app.exec_()
