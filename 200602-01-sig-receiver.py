# 시그널에 연결된 함수 찾기  
# #In pyqt5 SIGNAL is deprecated. It is replaced with signal attribute of each QObject
# https://stackoverflow.com/questions/8166571/how-to-find-if-a-signal-is-connected-to-anything
# https://stackoverflow.com/questions/40221947/pyqt5-receivers
# https://stackoverflow.com/questions/7609291/pyqtsignal-and-qobject-receivers


from PyQt5 import QtWidgets, QtCore

def prt(b):
    sig_no = btn.receivers( btn.clicked )
    list_widget.addItem('sig_no:{0}'.format(sig_no ))

    idx = btn.metaObject().indexOfSlot("prt(b)")
    mm = btn.metaObject().method(idx)
    print( mm )
    
app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()

win.setLayout(QtWidgets.QVBoxLayout())
l = win.layout()

btn = QtWidgets.QPushButton('signal 찾기')
l.addWidget(btn)

list_widget = QtWidgets.QListWidget()
l.addWidget(list_widget)

btn.clicked.connect(prt)
btn.clicked.connect(lambda:print('x'))

metaobject = btn.metaObject()
for i in range(metaobject.methodCount()):
    print(metaobject.method(i).methodSignature())

win.show()
#win.show()
app.exec()
