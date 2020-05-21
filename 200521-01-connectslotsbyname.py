#https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html#connecting-slots-by-name


"""from PyQt5 import QtWidgets, QtCore # 안됨 원인

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()


btn = QtWidgets.QPushButton('btn_!', win)
btn.setObjectName('btn1')
print(btn.objectName())


QtCore.QMetaObject.connectSlotsByName(btn)

def on_btn1_clicked(bool):
    print( bool )

win.show()
#win.show()
app.exec()
"""


from PyQt5 import QtWidgets, QtCore


class Win(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        btn = QtWidgets.QPushButton('btn_!', self)
        btn.setObjectName('btn1')
        print(btn.objectName())

        QtCore.QMetaObject.connectSlotsByName(self)

    def on_btn1_clicked(self):
        print( 'receive signal by name:', self.sender().objectName() )

    """@QtCore.pyqtSlot(bool) 
    def on_btn1_clicked(self, b):
        print( 'receive signal by name:', self.sender().objectName(), b )"""

 
    @QtCore.pyqtSlot(bool, name='on_btn1_clicked')
    def on_btxxxxxxxxxxxxxxxn11_clicked(self, b):
        print( 'receive signal by name, decorator:', self.sender().objectName(), b )


app = QtWidgets.QApplication([])
win = Win() 
win.show()
#win.show()
app.exec()
