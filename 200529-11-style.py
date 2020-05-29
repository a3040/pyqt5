#e
# 
#  
from PyQt5.QtWidgets import *

 
app = QApplication([])
win = QWidget()
win.resize(400, 400)
win.setStyleSheet('background-color:blue')


b = QPushButton('-----------------------------', win)
b.setObjectName('aa')
#win.setStyleSheet('QPushButton#aa{background-color:green;}') #111
b.setStyleSheet('QPushButton#aa{background-color:green;}')

c =  QPushButton('-----------------------------', win)
c.setStyleSheet('{background-color:yellow;}')#바탕이 노란색이었으면 얼마나 좋을까...
c.move(200,200)
win.show()
#win.show()
app.exec()