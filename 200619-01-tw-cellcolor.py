# https://stackoverflow.com/questions/62445354/how-to-change-background-color-of-selected-or-clicked-cell-in-a-pyqt5-qtablewidg

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 801)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 40, 1000, 600))
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        for i, col_name in enumerate(['symbol', 'step', 'factor', 'initial_lot', 'max_streak', 'status']):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(col_name))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{"
            "border-bottom: 1px solid #4a4848;"
            "background-color:white;"
        "}")


        self.tableWidget.setItemDelegate(ColorDelegate())
        self.tableWidget.cellClicked.connect(lambda r,c : self.print_selected(r, c))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def print_selected(self, *s):
        print(s)

class ColorDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        color = index.data(QtCore.Qt.UserRole)
        option.palette.setColor(QtGui.QPalette.Highlight, (QtGui.QColor('red') ) )
        QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
