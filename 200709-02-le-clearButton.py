# https://doc.qt.io/qt-5/qlineedit.html#clearButtonEnabled-prop

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

class Gui(QWidget):
    def __init__(self):
        super().__init__()
        edt = QLineEdit('send event', self) 

        edt.setClearButtonEnabled(True)
        
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    gui = Gui()
    app.exec_()
    gui.dispacher.stop()