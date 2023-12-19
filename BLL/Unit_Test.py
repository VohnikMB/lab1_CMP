from PyQt5.QtWidgets import QMessageBox

def unittest_box():
    file_name = f"Data/Unittest/unittest.txt"
    dialog = QMessageBox()
    dialog.setFixedSize(800, 200)
    try:
        file_content = "Помилка, тести не знайдені"
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
        dialog.setText(file_content)
        dialog.setWindowTitle("Unittest")
        dialog.exec_()

    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        import traceback
        traceback.print_exc()
