#e
# 
from PyQt5 import QtWidgets, QtCore

class Foo(QtCore.QObject):
    sig = QtCore.pyqtSignal(object) 

def hello(e):
    print('-------------:', e)    
    for k, v in vars(QtCore.Qt).items():
        if e.type() == v:
            print( 'event type()', e.type(), 'key enum Qt.', k )

app = QtWidgets.QApplication([])
foo = Foo()
foo.sig.connect(hello)
win = QtWidgets.QWidget()
win.show()
win.keyPressEvent = lambda e: foo.sig.emit(e)
app.exec() 