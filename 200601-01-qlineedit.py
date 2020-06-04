# https://stackoverflow.com/questions/62120999/issue-in-qlineedit-with-title
# 두번째 edit 박스에 글 넣고 처음으로 이동후 입력했을때, title()로 변화하고 커서가 에디트 박스끝으로 이동됨


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Lineedit_title(QWidget):
    def __init__(self):
        super().__init__()

        #self.setGeometry(100,100,500,500)
        self.resize(500,500)

        self.textbox1 = QLineEdit(self)
        self.textbox1.setGeometry(50,50,200,50)
        self.textbox1.setFont(QFont("Caliber", 15, QFont.Bold))

        self.textbox2 = QLineEdit(self)
        self.textbox2.setGeometry(50,140,200,50)
        self.textbox2.setFont(QFont("Caliber",15,QFont.Bold))
        self.textbox2.textChanged.connect(self.textbox_textchange)

    def textbox_textchange(self,txt):
        #position = self.textbox2.cursorPosition()
        self.textbox2.setText(txt.title())
        #self.textbox2.setCursorPosition(position)

def main():
    app = QApplication(sys.argv)
    win = Lineedit_title()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()