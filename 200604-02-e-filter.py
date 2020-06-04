# https://doc.qt.io/qt-5/qevent.html#Type-enum
# qevent

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self ):
        super().__init__()
        self.installEventFilter(self)

    def eventFilter(self, QObject, QEvent):
        for k, v in vars(QtCore.QEvent).items():
            if QEvent.type() == v:
                print( 'event type()', QEvent.type(), 'key', k )

        return super().eventFilter( QObject, QEvent)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window() 
    window.resize(300,200)
    window.show()
    app.exec()