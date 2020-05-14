import sys
from PyQt5.QtCore    import Qt, QRectF, QDate
from PyQt5.QtGui     import QPainter, QColor, QFont
from PyQt5.QtWidgets import QCalendarWidget, QApplication

class CalendarWidget(QCalendarWidget):

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QPainter.Antialiasing, True)
        if date == QDate().currentDate():
            painter.save()
            painter.drawRect(rect)
            
            painter.setPen(QColor(168, 34, 3))
            #painter.setFont(QFont('Decorative', 10))            

            painter.setFont(QFont('굴림',10))
            painter.drawText(QRectF(rect), Qt.TextSingleLine|Qt.AlignCenter, str(date.day()))
            painter.drawText(rect, Qt.AlignCenter, '한ᄀᅠᆯ') 

            painter.restore()
        else:
            QCalendarWidget.paintCell(self, painter, rect, date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CalendarWidget()
    w.show()
    sys.exit(app.exec_())