#https://stackoverflow.com/questions/60748770/why-does-my-keypressevent-not-register-or-work-pyqt5

import sys
from PyQt5 import QtWidgets 
 
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__() 

    def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Escape:
        #if event.key() == Qt.Key_F5:
        #    print("closed")
        print( 'in class', event.key())

def ke(e):
        print( 'in fn:', e.key())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    M = Main()
    M.setStyleSheet('QLabel{border:1px solid green;}')
    QtWidgets.QLabel('키보드 누르세요.',M).resize(200, 50)
    #M.keyPressEvent = ke
    M.show()
    sys.exit(app.exec())