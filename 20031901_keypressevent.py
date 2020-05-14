#https://stackoverflow.com/questions/60748770/why-does-my-keypressevent-not-register-or-work-pyqt5

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtCore import Qt


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__() 

    def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Escape:
        #if event.key() == Qt.Key_F5:
        #    print("closed")
        print( event.key())
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    M = Main()
    M.show()
    sys.exit(app.exec())