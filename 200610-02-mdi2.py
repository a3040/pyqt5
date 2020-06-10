# mdi 방식에 widget 추가하기

import os
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui

class SubWin(QtWidgets.QWidget): 
    def __init__(self, body_str):
        super(SubWin, self).__init__() 
        self.body_str = body_str
        self.resize(100, 100)

    def paintEvent( self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawText(10, 10, self.body_str)
        qp.end()

class Win(QtWidgets.QWidget): 
    def __init__(self):
        super(Win, self).__init__()
        self.initUi()

    def initUi(self):
        self.mainbox = QtWidgets.QVBoxLayout()

        self.headbox = QtWidgets.QHBoxLayout()
        for i in range(1, 10):
            btn = QtWidgets.QPushButton('str{0}'.format(i))
            btn.clicked.connect(self.clk)
            self.headbox.addWidget(btn)

        self.mainbox.addLayout(self.headbox)

        self.bodybox =  QtWidgets.QHBoxLayout()
        self.mdi = QtWidgets.QMdiArea()
        self.mdi.setStyleSheet('border:1px solid blue')
        self.mdi.setMinimumHeight(600)
        self.bodybox.addWidget(self.mdi)
        self.mainbox.addLayout(self.bodybox)

        self.setLayout(self.mainbox)


    def clk(self):
        sub_text = self.sender().text()
        #print( self.sender().text())
        sub = SubWin(sub_text)
        sw = self.mdi.addSubWindow(sub)
        sw.resize(100, 100)
        sw.show()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Win()
    main.show() 
    sys.exit(app.exec_())