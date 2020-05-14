# https://doc.qt.io/qt-5/qwidget.html

from PyQt5 import QtWidgets, QtCore, QtGui

delta = None

def pe(e): 
    """
    마우스 눌림이벤트
    """
    global delta
    print('press')
    delta = e.pos() 
    print( win2.x(), win2.y() )
    print( delta.x(), delta.y() )
    print( e.x(), e.y() )
    
def re(e):
    """
    마우스 해제 이벤트
    """
    print('release')

def me(e):
    """
    마우스이동이벤트
    """
    global delta
    print('move' )  
    np = e.pos() - delta  
    parent_point = win2.mapToParent(np) #부모 좌표계로 전환 하면 win2에서 눌린 위치가 이벤트로 오기때문에 win2를 욺직일경우 win2.pos와 event.pos의 위치차가 존재함

    win2.move(parent_point)
    
def p(e): 
    qp = QtGui.QPainter()
    qp.begin(win2)
    qp.drawText(e.rect(), QtCore.Qt.AlignCenter, 'double click')
    qp.end()    

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
win.show()

win2 = QtWidgets.QWidget(win) 
win2.setStyleSheet('border:1px solid green;') 
win2.resize(100, 100)
win2.move(10, 10)
#Protected Functions 는 이런형태로 사용이 가능한가봅니다.
#https://doc.qt.io/qt-5/qwidget.html#mouseDoubleClickEvent
win2.mousePressEvent = pe #마우스 눌릴때
win2.mouseReleaseEvent = re #마우스 해재 됐을때
win2.mouseMoveEvent = me #마우스가 눌린상태로 이동할때
win2.paintEvent =  lambda event : p(event )   
win2.show()

app.exec() 