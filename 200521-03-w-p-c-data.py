# https://doc.qt.io/qt-5/qwidget.html
# widget 간 데이터 송수신? 필요 없음 직접 참조하면 됨
#E
from PyQt5 import QtWidgets, QtCore, QtGui

class Data(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.data = '여기에요'
        btn = QtWidgets.QPushButton('닫기', self)
        btn.clicked.connect(lambda: self.close())

def c(e): 
    p = win3.parentWidget()
    if not p:    
        win3.setParent(win)
        win3.move(110,110)
    else:
        win3.setParent(None)
         
    win3.show()

def p(e): 
    qp = QtGui.QPainter()
    qp.begin(win2)
    qp.drawText(e.rect(), QtCore.Qt.AlignCenter, 'double click')
    qp.end()    

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
win.show()
data = Data()

win2 = QtWidgets.QWidget(win) 
win2.setStyleSheet('border:1px solid green;') 
win2.resize(100, 100)
win2.move(10, 10)
#Protected Functions 는 이런형태로 사용이 가능한가보네요
#https://doc.qt.io/qt-5/qwidget.html#mouseDoubleClickEvent
win2.mouseDoubleClickEvent = c 
win2.paintEvent =  lambda event : p( event )   
win2.show()

win3 = QtWidgets.QWidget() 
win3.resize(100, 100)
win3.setStyleSheet('background-color:red')
win3.setLayout(QtWidgets.QVBoxLayout())
l = win3.layout()
btn = QtWidgets.QPushButton('win4 자료 찾기', win3)
btn.clicked.connect(lambda: print(data.data))
l.addWidget(btn)

btn1 = QtWidgets.QPushButton('data 보이기', data)
btn1.clicked.connect(lambda:data.show())
l.addWidget(btn1)

win3.show()


app.exec() 