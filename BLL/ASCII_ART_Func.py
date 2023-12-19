from pyfiglet import Figlet
from BLL.font import print_ascii_art
from PyQt5.QtWidgets import QFontDialog, QColorDialog
import os
def update_text_browser(textBrowser, lineEdit, symbolcomboBox):
    f = Figlet(font="banner")
    text = f.renderText(lineEdit.text())
    text = text.replace("#", symbolcomboBox.currentText())
    textBrowser.setPlainText(text)
def update_text_browser_nonFiglet(textBrowser, lineEdit, symbolcomboBox):
    text = print_ascii_art(lineEdit.text())
    text = text.replace("#", symbolcomboBox.currentText())
    textBrowser.setPlainText(text)
def saveFunc(textBrowser):
    data_folder = 'Data/ASCII_ART/'

    format = textBrowser.currentCharFormat()
    font = format.font()
    color = format.foreground().color()

    with open(os.path.join(data_folder, 'save.html'), 'w', encoding='utf-8') as html_file:
        txt_content = textBrowser.toPlainText()
        css_content = ".text-block {\n"+f"  font-family: {font.family()};\n"+f"  font-size: {font.pointSize()}pt;\n"+f"  color: {color.name()};\n"+"}"
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            {css_content}
        </style>
        <link href="style.css" rel="stylesheet" type="text/css" />
            <meta charset="UTF-8">
            <title>Save</title>
        </head>
        <body>
            <div class="text-block"><pre>
{txt_content}
                </pre>
            </div>
        </body>
        </html>
        """
        html_file.write(html_content)

    with open(os.path.join(data_folder, 'style.css'), 'w', encoding='utf-8') as css_file:
        css_file.write(".text-block {\n")
        css_file.write(f"  font-family: {font.family()};\n")
        css_file.write(f"  font-size: {font.pointSize()}pt;\n")
        css_file.write(f"  color: {color.name()};\n")
        css_file.write("}\n")

    with open(os.path.join(data_folder, 'save.txt'), 'w', encoding='utf-8') as fileSave:
        fileSave.write(textBrowser.toPlainText())

def formatFunc(textBrowser, lineEdit, symbolcomboBox):
    font, ok = QFontDialog.getFont(textBrowser.currentFont())
    color = QColorDialog.getColor(initial=textBrowser.textColor(), parent=textBrowser)
    if ok:
        textBrowser.setFont(font)
    if color.isValid():
        textBrowser.setTextColor(color)
    update_text_browser(textBrowser, lineEdit, symbolcomboBox)
def formatFunc_nonFiglet(textBrowser, lineEdit, symbolcomboBox):
    font, ok = QFontDialog.getFont(textBrowser.currentFont())
    color = QColorDialog.getColor(initial=textBrowser.textColor(), parent=textBrowser)
    if ok:
        textBrowser.setFont(font)
    if color.isValid():
        textBrowser.setTextColor(color)
    update_text_browser_nonFiglet(textBrowser, lineEdit, symbolcomboBox)