# https://stackoverflow.com/questions/62798322/drag-and-drop-functionality-in-pyqt5-with-custom-widgets-creates-widgets-with-c

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout, QAbstractItemView
import os
import PyQt5
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap, QColor, QBrush, QFontDatabase, QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtCore import QRect, QSize, Qt, QThread, QProcess

class CustomQWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomQWidget, self).__init__(parent)

        formLayoutWidget = QtWidgets.QWidget()
        # formLayoutWidget.setGeometry(QtCore.QRect(139, 69, 291, 131))
        formLayoutWidget.setObjectName("formLayoutWidget")
        formLayout = QtWidgets.QFormLayout(formLayoutWidget)
        formLayout.setContentsMargins(0, 0, 0, 0)
        formLayout.setObjectName("formLayout")

        lineEdit = QtWidgets.QLineEdit(formLayoutWidget)
        lineEdit.setObjectName("lineEdit")
        formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, lineEdit)

        lineEdit_2 = QtWidgets.QLineEdit(formLayoutWidget)
        lineEdit_2.setObjectName("lineEdit_2")
        formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, lineEdit_2)

        lineEdit_3 = QtWidgets.QLineEdit(formLayoutWidget)
        lineEdit_3.setObjectName("lineEdit_3")
        formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, lineEdit_3)

        label = QtWidgets.QLabel(formLayoutWidget)
        label.setObjectName("label")
        label.setText("TextLabel")
        formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)

        label_2 = QtWidgets.QLabel(formLayoutWidget)
        label_2.setObjectName("label_2")
        label_2.setText("TextLabel")
        formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, label_2)

        label_3 = QtWidgets.QLabel(formLayoutWidget)
        label_3.setObjectName("label_3")
        label_3.setText("TextLabel")
        formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, label_3)

        self.setLayout(formLayout)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.myListWidget1 = QListWidget()
        # self.myListWidget1.setViewMode(QListWidget.IconMode)

        self.myListWidget2 = QListWidget()
        self.myListWidget2.setViewMode(QListWidget.IconMode)
        self.myListWidget1.setAcceptDrops(False)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)
        self.myListWidget2.setGridSize( QSize( 130, 130 ) )
        self.myListWidget2.setMovement(2)
        self.setGeometry(300, 350, 990, 970)
        self.myLayout = QHBoxLayout()
        self.myLayout.addWidget(self.myListWidget1)
        self.myLayout.addWidget(self.myListWidget2)

        self.setFixedSize(self.size())

        self.item = QListWidgetItem(self.myListWidget1)
        self.item_widget = CustomQWidget()
        self.item.setSizeHint(self.item_widget.sizeHint())
        self.myListWidget1.addItem(self.item)
        self.myListWidget1.setItemWidget(self.item, self.item_widget)

        self.item2 = QListWidgetItem(self.myListWidget1)
        self.item_widget2 = CustomQWidget()
        self.item2.setSizeHint(self.item_widget2.sizeHint())
        self.myListWidget1.addItem(self.item2)
        self.myListWidget1.setItemWidget(self.item2, self.item_widget2)
        self.myListWidget1.setDragDropMode(QAbstractItemView.DragDrop)

        self.setWindowTitle('Drag and Drop Example');
        self.setLayout(self.myLayout)

        self.show()

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
