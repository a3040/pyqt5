# https://stackoverflow.com/questions/62291103/how-do-i-dock-a-subwindow-in-an-mdi-area-in-pyqt5-using-qtdesigner
# mdi 사용.
# e

import os
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui

scriptPath = os.path.dirname(os.path.realpath(__file__))
uiFile = os.path.join(scriptPath, "tmp.ui")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        # load the UI page
        self.ui_main = uic.loadUi(uiFile, self)
        self.action1.triggered.connect(lambda: self.fileBarTrig("test"))

    def fileBarTrig(self, p):
        sw1 = self.mdiArea.addSubWindow(self.subwindow)
        sw1.show()
        sw2 = self.mdiArea.addSubWindow(self.subwindow_2)
        sw2.show()

        sub3 = Sub3(self)
        sw3 = self.mdiArea.addSubWindow(sub3)
        sw3.show()
        self.mdiArea.tileSubWindows()


class Sub3(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(100, 100)

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.begin(self)
        qp.drawText(20,20, 'ssss' )
        qp.end()
        

        #return super().paintEvent(self, QPaintEvent)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()