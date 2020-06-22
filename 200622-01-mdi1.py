# https://stackoverflow.com/questions/62504519/pyqt5-qmdiarea-subclass-with-a-custom-signal-on-close

 
from PyQt5.QtCore import pyqtSignal,pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMdiSubWindow, QMdiArea, QTextEdit,QAction

class MdiSubWindow(QMdiSubWindow):
    sigClosed = pyqtSignal(str)

    def closeEvent(self, event):
        """Get the name of active window about to close
      """
        self.sigClosed.emit(self.windowTitle())
        QMdiSubWindow.closeEvent(self, event)


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New")
        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle("MDI demo")

    @pyqtSlot(str)
    def windowclosed(self, text):
        print(text)

    def windowaction(self, q):
        if q.text() == "New":
            MainWindow.count = MainWindow.count + 1
            sub = MdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setAttribute(Qt.WA_DeleteOnClose)
            sub.setWindowTitle("subwindow" + str(MainWindow.count))
            sub.sigClosed.connect(self.windowclosed)
            self.mdi.addSubWindow(sub)
            sub.show()
 
if __name__ == "__main__":
    app = QApplication([])
    ex = MainWindow()
    ex.show()
    app.exec_()
