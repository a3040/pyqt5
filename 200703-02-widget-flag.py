#https://stackoverflow.com/questions/62704519/reset-window-attribute-to-default-pyqt5

import sys
from PyQt5 import QtWidgets, QtCore


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet('.QWidget {background-color: blue;}')
        self.widget.setObjectName('widget')
        self.widget.setFixedSize(700, 500)

        close_button = QtWidgets.QPushButton('close window', clicked=self.close)

        self.change_button = QtWidgets.QPushButton('change StyleSheet')
        self.change_button.setCheckable(True)
        self.change_button.toggled.connect(self.button_state_func)   

        layout = QtWidgets.QGridLayout(self.widget)
        layout.addWidget(close_button)
        layout.addWidget(self.change_button)

    def button_state_func(self, state):
        if state:
            self.widget.setStyleSheet('QWidget#widget {background-color: transparent;}')
        else:
            self.widget.setStyleSheet('QWidget#widget {background-color: yellow;}')       
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())