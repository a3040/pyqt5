# mdi 방식에 widget 추가하기
# #designer에서 작성된 ui 파일 읽어 와서 subsclass 추가하기.
 
import os
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui


scriptPath = os.path.dirname(os.path.realpath(__file__))

class SubWin(QtWidgets.QWidget): 
    def __init__(self, ui_file, body_str):
        super(SubWin, self).__init__() 
        self.body_str = body_str
        self.ui_file = ui_file
        print('id:', id(self))
        self.initUi()

    def initUi(self):
        uiFile = os.path.join(scriptPath, self.ui_file) 
        uic.loadUi(uiFile, self)
        self.btn.setText(self.body_str)
        self.btn.clicked.connect(lambda bool: print('---@@@??', self.sender(), 'id', id(self), sep=":"))

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
        sub = SubWin( "empty.ui", sub_text)
        sw = self.mdi.addSubWindow(sub)
        sw.resize(300, 300)
        sw.show()
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Win()
    main.show() 
    sys.exit(app.exec_())