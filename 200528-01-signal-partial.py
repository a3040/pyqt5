# https://stackoverflow.com/questions/54712203/how-do-i-assert-the-identity-of-a-pyqt5-signal
# 1. Using sender() method
# 2. Pass the object as an additional parameter
# 2.1 lambda function 
# 2.1 functools.partial function 


import sys
from PyQt5 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.button_1 = QtWidgets.QPushButton("button 1")
        self.button_1.clicked.connect(self.foo)
        self.button_2 = QtWidgets.QPushButton("button 2")
        self.button_2.clicked.connect(self.foo)
        self.button_3 = QtWidgets.QPushButton("button 3")
        self.button_3.clicked.connect(self.foo)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.button_1)
        lay.addWidget(self.button_2)
        lay.addWidget(self.button_3)

    @QtCore.pyqtSlot()
    def foo(self):
        button = self.sender()
        if button is self.button_1:
            print("button_1")
        elif button is self.button_2:
            print("button_2")
        elif button is self.button_3:
            print("button_3")

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())



