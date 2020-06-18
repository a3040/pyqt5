# https://stackoverflow.com/questions/62436540/drag-and-drop-from-one-qlistview-to-another-qlistview

import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QListView, QApplication, QWidget, QHBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        draggable_list_view = QListView()
        draggable_list_view.setDragEnabled(True)
        model1 = QStandardItemModel()
        draggable_list_view.setModel(model1)
        for it in ["yo", "yi", "ya"]:
            item = QStandardItem(it)
            model1.appendRow(item)

        droppable_list_view = QListView()
        droppable_list_view.setAcceptDrops(True)
        droppable_list_view.setDropIndicatorShown(True)
        model2 = QStandardItemModel()
        droppable_list_view.setModel(model2)

        lay = QHBoxLayout(self)
        lay.addWidget(draggable_list_view)
        lay.addWidget(droppable_list_view)

        self.setGeometry(300, 300, 300, 150)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == "__main__":
    main()