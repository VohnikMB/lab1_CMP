import math
import re


def clear_function(label_history):
    label_history.setText("Історія:\n")


def root_function(label_result, label_history):
    if float(eval(label_result.text())) < 0:
        label_history.setText(label_history.text() + "\n√(" + label_result.text() + ")= Error")
        label_result.setText("Error")
    else:
        res = math.sqrt(eval(label_result.text()))
        label_history.setText(label_history.text() + "\n√(" + label_result.text() + ")=" + str(res))
        label_result.setText(str(res))


def del_function(label_result):
    label_result.setText("0")


def results(label_result, label_history):
    pattern = r"/0\.\d+"
    if ("/0" in label_result.text() or "Error" in label_result.text()) and not re.search(pattern, label_result.text()):
        label_history.setText(label_history.text() + "\n" + label_result.text() + "= Error")
        label_result.setText("Error")
    else:
        res = eval(label_result.text())
        label_history.setText(label_history.text() + "\n" + label_result.text() + "=" + str(res))
        label_result.setText(str(res))