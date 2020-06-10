# https://stackoverflow.com/questions/62262538/how-to-add-an-image-in-pyqt-qdock-widget

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtCore import Qt
  
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        dockWidget = QtWidgets.QDockWidget()
        dockWidget.setWindowTitle("Image Viewer")
 
        image = QtGui.QImage('pyqt5/img_1.png')
        pixmap = QtGui.QPixmap.fromImage(image) 
        label = QtWidgets.QLabel('testing', self)
        label.setPixmap(pixmap)

        #dockWidget.setWidget(pixmap)
        dockWidget.setWidget(label)
        dockWidget.setFloating(False)
        self.addDockWidget(Qt.RightDockWidgetArea, dockWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()

    sys.exit(app.exec_())