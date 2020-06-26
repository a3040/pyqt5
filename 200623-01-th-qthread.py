# https://stackoverflow.com/questions/62522653/using-qthread-and-pyqtsignal-why-does-the-process-which-is-in-a-different-threa
# https://doc.qt.io/qt-5/qthread.html
# red버튼을 누르면  time.sleep동안 blue 버튼 클릭에 대한 반응이 지연됨
# QThread 사용법 1. QObject -> moveToThread 사용 2.QThread상속시 run구현
# A QThread object manages one thread of control within the program. QObject에서 상속된 class를 thread로 관리하는데 사용?


import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal, QThread, Qt, QObject, pyqtSlot


class WriteThread(QThread):
    write_signal = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.write_signal.connect(self.worker, Qt.QueuedConnection)

    def worker(self):
        print("Before sleep")
        time.sleep(2)
        print("After sleep")
        return True


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.CustomEvent = None
        self.write_thread = None
        self.init_ui()

    def init_ui(self):
        self.write_thread = WriteThread(self)

        redb = QPushButton('Red', self)
        redb.move(10, 10)

        blueb = QPushButton('Blue', self)
        blueb.move(10, 50)
        blueb.clicked.connect(self.print_method)

        redb.clicked.connect(self.send_event)

        self.write_thread.start()

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Toggle button')
        self.show()

    def send_event(self):
        print("\tSending signal")
        self.write_thread.write_signal.emit()
        print("\tFinished sending signal")

    def print_method(self):
        print("Not frozen")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()
    ex.write_thread.quit() 

class WriteObject(QObject):
    write_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.write_signal.connect(self.worker1, Qt.QueuedConnection)

    @pyqtSlot()
    def worker1(self):
        print("Before sleep")
        time.sleep(2)
        print("After sleep")
        return True


class Example1(QWidget):
    def __init__(self):
        super().__init__()
        self.CustomEvent = None
        self.write_thread = None
        self.init_ui()

    def init_ui(self):
        self.write_object = WriteObject()
        self.write_thread = QThread(self)
        self.write_thread.start()
        self.write_object.moveToThread(self.write_thread)

        redb = QPushButton("Red", self)
        redb.move(10, 10)

        blueb = QPushButton("Blue", self)
        blueb.move(10, 50)
        blueb.clicked.connect(self.print_method)

        redb.clicked.connect(self.send_event)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle("Toggle button")
        self.show()

    def send_event(self):
        print("\tSending signal")
        self.write_object.write_signal.emit()
        print("\tFinished sending signal")

    def print_method(self):
        print("Not frozen")

if __name__ == "__main__":
    app = QApplication.instance()#QApplication(sys.argv)
    ex = Example1()
    ret = app.exec_()
    ex.write_thread.quit()
    ex.write_thread.wait()
    sys.exit(ret)