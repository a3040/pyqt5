#https://stackoverflow.com/questions/61914123/is-it-possible-to-render-text-as-being-cut-out-from-a-layer-in-in-qt5
#https://doc.qt.io/qt-5/qpainterpath.html
#e

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap,QPainterPath, QFont, QPainter, QBrush
from PyQt5.QtCore import Qt, QPoint

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        label = QLabel(self)
        label.setPixmap(self.makePixmap("knockout"))

    def makePixmap(self, text):
        background = QPixmap(600, 80)
        background.fill(Qt.red)      # Your background image
        painter = QPainter(background)

        textMask = QPainterPath() 
        textMask.addRect(75, 20, 300, 40) # The white part
        textMask.addText(QPoint(90, 50), QFont("Helvetica [Cronyx]", 24), text) # the path will substract the text to the rect

        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        painter.fillPath(textMask, QBrush(Qt.white)) # Will draw the white part with the text "cut out"

        painter.end()
        return background

app = QApplication([])
win = Widget()
win.show()
win.resize(600,80)
#win.show()
app.exec()
