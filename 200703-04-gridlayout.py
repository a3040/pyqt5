# https://stackoverflow.com/questions/62685742/label-word-wrap-in-pyqt5-doesnt-take-up-space-with-stretch


from PyQt5 import QtWidgets, QtGui, QtCore

class CustomWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout  = QtWidgets.QGridLayout()
        self.button1 = QtWidgets.QPushButton("Button A")
        self.button2 = QtWidgets.QPushButton("Button B")
        self.label1  = QtWidgets.QLabel("Long label that can span multiple columns this is actually a long message tbh and it needs word wrap really.")
        self.label1.setWordWrap(True)
        
        self.layout.addWidget(self.button1, 0, 0)
        self.layout.addWidget(self.button2, 0, 1)
        #self.layout.addWidget(self.label1, 1, 0, 1, 2)
        self.layout.addWidget(self.label1, 1, 0, 1, 3)
        self.setLayout(self.layout)
        self.layout.setColumnStretch(2, 1)
        self.layout.setRowStretch(2, 1)


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.cw = CustomWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.cw)

        self.setLayout(self.layout)
        self.show()

QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
app = QtWidgets.QApplication([])
win = App()
status = app.exec_()