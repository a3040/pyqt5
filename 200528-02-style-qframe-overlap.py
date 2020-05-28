# https://stackoverflow.com/questions/62046679/qframe-background-color-overlapped-with-other-widgets-like-qlineedit-qlistboxwi

import sys
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *

item = ["Python", "Python 2.7", "Python 2.9", "Python 3.5", "Python 3.7", "National", "Zebra",
                "Apple", "X Ray","Boat", "Tiger", "Item001", "Item002", "Item003", "Item004", "Item005",
                "001Item", "002Item", "003Item","004Item", "005Item", "Ball", "Cat", "Dog", "Fish",
                "Gold Fish", "Star Fish"]


class myList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Frame Example")
        self.myui()

    def myui(self):

        self.textbox = QLineEdit(self)
        self.listbox = QListWidget(self)
        self.listbox.addItems(item)

        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.listbox)

        '''frame = QFrame()
        frame.setLayout(vbox)
        frame.setStyleSheet("background-color:orange")'''

        frame = QFrame()
        frame.setObjectName("frame")
        frame.setLayout(vbox)
        frame.setStyleSheet("QFrame#frame{background-color:orange}")

        main_layout =QHBoxLayout()
        main_layout.addWidget(frame)
        self.setLayout(main_layout)

def main():
    myapp = QApplication(sys.argv)
    mywin = myList()
    mywin.show()
    sys.exit(myapp.exec_())

if __name__ == '__main__':
    main()