import sys
import unittest
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow
from PyQt5.QtTest import QTest
from BLL.calcProgramFunctionality import *
from UI.lab2 import Lab2MainWindow

class TestMargaritaMixer(unittest.TestCase):
    def test_history_text(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        label_history = window.label_history
        self.assertEqual(label_history.text(), "Історія:\n")
        window.close()

    def test_history_clear_function(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_history = QLabel(centralwidget)
        self.assertEqual(clear_function(label_history), "Історія:\n")
        window.close()

    def test_root_function(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_result.setText("9")
        label_history = QLabel(centralwidget)
        root_function(label_result, label_history)
        self.assertEqual(float(label_result.text()), 3.0)
        window.close()

    def test_root_function_negative_number(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_result.setText("-9")
        label_history = QLabel(centralwidget)
        root_function(label_result, label_history)
        self.assertEqual(label_result.text(), "Error")
        window.close()

    def test_root_multiplication(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_history = QLabel(centralwidget)
        label_result.setText("11*9")
        results(label_result, label_history)
        self.assertEqual((label_result.text()), "99")

    def test_del_function(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        del_function(label_result)
        self.assertEqual((label_result.text()), "0")

    def test_results_addition(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_history = QLabel(centralwidget)
        label_result.setText("1+9")
        results(label_result, label_history)
        self.assertEqual((label_result.text()), "10")

    def test_results_subtraction(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_history = QLabel(centralwidget)
        label_result.setText("8-5")
        results(label_result, label_history)
        self.assertEqual((label_result.text()), "3")

    def test_results_division_by_zero(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_result.setText("12/0")
        label_history = QLabel(centralwidget)
        results(label_result, label_history)
        self.assertEqual((label_result.text()), "Error")

    def test_results_division(self):
        app = QApplication(sys.argv)
        window = Lab2MainWindow()
        centralwidget = QWidget()
        window.setCentralWidget(centralwidget)
        label_result = QLabel(centralwidget)
        label_result.setText("8/2")
        label_history = QLabel(centralwidget)
        results(label_result, label_history)
        self.assertEqual((label_result.text()), "4.0")


if __name__ == "__main__":
    unittest.main()
