# https://doc.qt.io/qt-5/qwidget.html
# The widget is the atom of the user interface: it receives mouse, keyboard and other events from the window system, and paints a representation of itself on the screen. Every widget is rectangular, and they are sorted in a Z-order. A widget is clipped by its parent and by the widgets in front of it.
# https://doc.qt.io/qt-5/stylesheet-reference.html
# e

from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()

win.resize(200, 200) #윈도우는 사각형, 창크기는 200,200 window 장식 title 등 제외 크기
win.move(100, 100) #widget 10,10 부모 widget이 없어서 윈도우 이고 화면기준으로 움직임

#A widget that is not embedded in a parent widget is called a window
win.show() #부모 없는 대장 widget

win2 = QtWidgets.QWidget(win) #부모가 있는 자식 widget
win2.setStyleSheet('border:1px solid green;') 
win2.resize(200, 200) #부모보다 크기가 커서 clipped 된듯
win2.move(10, 10) #부모가 있어서 부모좌표 사용 이동
#win2.show() #부모창에도 안나타남 
win2.show() #부모창에 보임

print( 'win2.pos()',win2.pos() )
QtCore.QTimer.singleShot(1000, lambda:win2.close()) #1초후 win2 숨김
QtCore.QTimer.singleShot(2000, lambda:win2.show()) #2초후 win2 보임
QtCore.QTimer.singleShot(3000, lambda:win.close()) #부모는 종료되면 app.exec() 탈출
print( 'win.pos()',win.pos() )



app.exec() 
print('1 loop end')

win.show()
app.exec()
print('2 loop end')
exit(-1)
print('exit')