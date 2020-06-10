# https://stackoverflow.com/questions/62249426/qmenubar-reimplementing-mousepressevent 


from PyQt5 import QtWidgets, QtCore

class menubarclass(QtWidgets.QMenuBar):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent

    def mousePressEvent(self, event):
        print("menubar clicked")    
        self.parent.close()
        super().mousePressEvent(event) 

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__()
        #bar = self.menuBar()
        bar = menubarclass(self)
        self.setMenuBar(bar)
        q = bar.addMenu("Quit")
        
        label = QtWidgets.QLabel('@____@') 
        self.setCentralWidget(label) 


app = QtWidgets.QApplication([])
win = Main()
win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
win.show()
#win.show()
app.exec()
