# https://stackoverflow.com/questions/61859385/keypressevent-without-focus
# non focus 일때도 입력 이벤트를 받고 자 함
# pip install pynput

"""import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.first = True

    def openselect(self): 
        self.setStyleSheet('background-color:yellow')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space and self.first:
            self.openselect()
            self.first = False
        print('Key Pressed!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())"""


import sys

from PyQt5 import QtCore, QtWidgets

from pynput.keyboard import Key, Listener, KeyCode


class KeyMonitor(QtCore.QObject):
    keyPressed = QtCore.pyqtSignal(KeyCode)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.listener = Listener(on_release=self.on_release)

    def on_release(self, key):
        self.keyPressed.emit(key)

    def stop_monitoring(self):
        self.listener.stop()

    def start_monitoring(self):
        self.listener.start()


class MainWindow(QtWidgets.QWidget):
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    monitor = KeyMonitor()
    monitor.keyPressed.connect(print)
    monitor.start_monitoring()

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())