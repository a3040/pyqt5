# https://stackoverflow.com/questions/54712203/how-do-i-assert-the-identity-of-a-pyqt5-signal
# 1. Using sender() method
# 2. Pass the object as an additional parameter
# 2.1 lambda function 
# 2.1 functools.partial function 
# e


import sys
from PyQt5 import QtCore, QtWidgets
from functools import partial

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.button_1 = QtWidgets.QPushButton("button 1 sender()")
        self.button_1.clicked.connect(self.foo)
        self.button_2 = QtWidgets.QPushButton("button 2.1 lambda")
        self.button_2.clicked.connect(self.foo)         
        self.button_2.clicked.connect(lambda a, b='뒤에전달' : self.foo21(a,b) ) # signal : slot = M:N 이라고 하는것 같습니다.
        self.button_2.clicked.connect(lambda a, b='앞에전달' : self.foo21(b,a))  # signal : slot = M:N 이라고 하는것 같습니다.
        self.button_3 = QtWidgets.QPushButton("button 2.2 partial")
        self.button_3.clicked.connect(self.foo)
        self.button_3.clicked.connect(partial(self.foo22, '앞에!') )

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.button_1)
        lay.addWidget(self.button_2)
        lay.addWidget(self.button_3)

    def foo(self):
        button = self.sender().text()
        print("sender is ", button)

    def foo21(self, a, b):
        print('foo21이?', a,b)

    def foo22(self, a, b):
        print('foo22이?', a,b)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())



