# https://stackoverflow.com/questions/62582661/pyqt5-widgets-get-shifted-to-center-using-gridlayout
# https://doc.qt.io/qt-5/qgridlayout.html#addWidget-2
# https://doc.qt.io/qt-5/qgridlayout.html#setRowStretch


from PyQt5 import QtWidgets, QtCore

class Win(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.createlayout()

    def createlayout(self):
        self.label1=QtWidgets.QLabel('self.label',self)
        self.label2=QtWidgets.QLabel('self.label2',self)
        self.textbox2 = QtWidgets.QLineEdit(self)
        self.textbox = QtWidgets.QLineEdit(self)
        txbx=[self.textbox2,self.textbox]

        [tx.setFixedWidth(190) for tx in txbx]

        #self.textbox.setFixedWidth(120)
        vbox=QtWidgets.QGridLayout()
        #vbox=QVBoxLayout()
        vbox.addWidget(self.label1,0,0,1,1, alignment=QtCore.Qt.AlignLeft)
        vbox.addWidget(self.textbox,1,0,1,1, alignment=QtCore.Qt.AlignLeft)
        vbox.addWidget(self.label2,2,0,1,1, alignment=QtCore.Qt.AlignLeft)
        vbox.addWidget(self.textbox2, 3, 0, 1, 1, alignment=QtCore.Qt.AlignLeft)

        #vbox.setContentsMargins(0,0,0,0)
        #vbox.setAlignment('AlignCenter')
        vbox.setRowStretch(4,1)
        #vbox.setRowStretch(3,1)
        #vbox.setRowStretch(2,3)
        self.setLayout(vbox)



app = QtWidgets.QApplication([])
win = Win()
win.show()
app.exec()