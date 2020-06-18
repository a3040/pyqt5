#https://doc.qt.io/qt-5/signalsandslots.html
#e
 
from PyQt5 import QtWidgets, QtCore, QtGui

class Foo(QtCore.QObject): 
    sig_obj = QtCore.pyqtSignal(object) 
    sig_str = QtCore.pyqtSignal(str) 

class Win(QtWidgets.QWidget):
    foo = Foo()
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.installEventFilter(self)

        self.btn = QtWidgets.QPushButton('--click signal')
        self.l = QtWidgets.QVBoxLayout()
        self.l.addWidget(self.btn)
        self.setLayout(self.l)
        self.btn.clicked.connect(lambda b: print( self.sender().text()))

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.begin(self)
        qp.drawText(10,20, '이제 화면에 글쓸줄 안다!! 사각형 크기도 안다!그런데 뭔가 에러가..마우스 클릭해보자!두줄은 언제쯤' )
        qp.drawRect(event.rect())
        qp.end()

    #def eventFilter(self): #TypeError: eventFilter() takes 1 positional argument but 3 were given 
    #def eventFilter(self, a): #TypeError: eventFilter() takes 2 positional arguments but 3 were given
    #def eventFilter(self, a, c ,d): #TypeError: eventFilter() missing 1 required positional argument: 'd'
    def eventFilter(self, a, b):
        if b.type() == QtCore.QEvent.MouseButtonPress:
            print( 'press', b.button(), b.button(), 'left button' if b.button() == QtCore.Qt.LeftButton else '??' )
            self.foo.sig_obj.emit(('obj????-- press', 'obj', 'send tuple'))
        if b.type() == QtCore.QEvent.MouseButtonDblClick:
            print( 'db click press', b.button() ) 
            self.foo.sig_str.emit('str????-- db click press')
            
        return super().eventFilter(a,b)

    """def eventFilter(self, QObject, QEvent):
        for k, v in vars(QtCore.QEvent).items():
            if QEvent.type() == v:
                print( 'event type()', QEvent.type(), 'key', k )

        return super().eventFilter( QObject, QEvent )"""


if __name__ == '__main__':
    app = QtWidgets.QApplication([]) 
    win =Win()
    win.foo.sig_obj.connect(lambda o: print(o))
    win.foo.sig_str.connect(lambda s: print(s))
    win.show() 
    app.exec() 