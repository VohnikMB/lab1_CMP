from pyfiglet import Figlet
from PyQt5.QtWidgets import QFontDialog, QColorDialog

def update_text_browser(textBrowser, lineEdit, symbolcomboBox):
    f = Figlet(font="banner")
    text = f.renderText(lineEdit.text())
    text = text.replace("#", symbolcomboBox.currentText())
    textBrowser.setPlainText(text)

def saveFunc(textBrowser):
    format = textBrowser.currentCharFormat()
    font = format.font()
    color = format.foreground().color()

    with open("save.html", "w") as html_file:
        txt_content = textBrowser.toPlainText()
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
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

    with open('style.css', 'w') as css_file:
        css_file.write(".text-block {\n")
        css_file.write(f"  font-family: "{font.family()}";\n")
        css_file.write(f"  font-size: {font.pointSize()}pt;\n")
        css_file.write(f"  color: {color.name()};\n")
        css_file.write("}\n")

    with open('save.txt', 'w') as fileSave:
        fileSave.write(textBrowser.toPlainText())

def formatFunc(textBrowser, lineEdit, symbolcomboBox):
    font, ok = QFontDialog.getFont(textBrowser.currentFont())
    color = QColorDialog.getColor(initial=textBrowser.textColor(), parent=textBrowser)
    if ok:
        textBrowser.setFont(font)
    if color.isValid():
        textBrowser.setTextColor(color)
    update_text_browser(textBrowser, lineEdit, symbolcomboBox)
