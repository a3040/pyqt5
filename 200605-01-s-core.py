#e
# 
from PyQt5.QtCore import QObject, QTimer, pyqtSignal, pyqtSlot
from PyQt5 import QtWidgets, QtCore

class Foo(QObject):
    sig = pyqtSignal(str) 

def hello(xx):
    print('----------recv:', xx)
    if xx == '1':
        app = QtWidgets.QApplication.instance()
        app.quit()
    elif xx == '2':
        foo.sig.disconnect(hello)
        pass

def send():
    foo.sig.emit('3')
    print('3 send')
    app = QtWidgets.QApplication.instance()
    app.quit()

app = QtCore.QCoreApplication([])
foo = Foo()
foo.sig.connect(hello)
QTimer.singleShot(100, lambda:foo.sig.emit('1'))
app.exec()
del app

app = QtWidgets.QApplication([])
foo = Foo()
foo.sig.connect(hello)
QTimer.singleShot(200, lambda:foo.sig.emit('2'))
QTimer.singleShot(300, send)

app.exec()

