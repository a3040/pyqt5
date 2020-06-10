# https://stackoverflow.com/questions/62232668/selection-problem-when-drag-drop-moving-pyqt5

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pickle

class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()
        self.setCentralWidget(self.table)

        headers = [None, 'Matreial', 'γ, kg/m3', 'λa', 'λb']

        data = [
            [1, 'Blocks γ=500 GOST 31359-2007', 500, 0.18, 0.22],
            [2, 'Blocks γ=600 GOST 31359-2008', 600, 0.25, 0.27],
            [3, 'Insulation', '80-125', 0.041, 0.042],
            [3, 'Insulation', '80-125', 0.041, 0.042]
            ]

        self.model = Materials(data, headers)
        self.table.setModel(self.model)

        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setSelectionMode(self.table.SingleSelection)
        self.table.setDragDropMode(self.table.InternalMove)
        self.table.setDropIndicatorShown(True)
        self.table.setDragEnabled(True)
        self.table.setAcceptDrops(True)




class Materials(QtCore.QAbstractTableModel):

    def __init__(self, materials = [[]], headers = [], parent = None):
        super(Materials, self).__init__()
        self.materials = materials
        self.headers = headers

    def rowCount(self, parent):
        return len(self.materials)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.materials[row][column]
            return value

    def setData(self, index, value, role = QtCore.Qt.EditRole):

        if role == QtCore.Qt.EditRole:
            row = index.row()
            column = index.column()
            self.materials[row][column] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def headerData(self, section, orientation, role):

        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled

    def insertRows(self, value, position, rows, parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):
            self.materials.insert(position, value)

        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
        self.beginRemoveRows(parent, position, position + rows - 1)

        for i in range(rows):
            item = self.materials[position]
            self.materials.remove(item)

        self.endRemoveRows()
        return True


    def supportedDropActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction

    def supportedDragActions(self):
        return QtCore.Qt.CopyAction | QtCore.Qt.MoveAction


    def mimeTypes(self):
        return ['text']

    def mimeData(self, indexes):
        mimedata = QtCore.QMimeData()
        row = indexes[0].row()
        list_1 = self.materials[row]
        b = bytearray(pickle.dumps(list_1))
        mimedata.setData('text', b)

        return mimedata


    def dropMimeData(self, mimedata, action, row, col, parent):

        drop_data = mimedata.data('text')
        item_list = pickle.loads(drop_data)

        if parent.row() == -1:
            return False
        else:
            if item_list in self.materials:
                position = self.materials.index(item_list)
            self.removeRows(position, 1)
            self.insertRows(item_list, parent.row(), 1)
            return True



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Mainwindow()
    application.show()


    sys.exit(app.exec())