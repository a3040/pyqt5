# https://stackoverflow.com/questions/62706085/how-to-return-the-actual-object-from-a-qlistwidget-in-pyqt5

 
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets


CustomObjectRole = QtCore.Qt.UserRole + 1

class Obj:
    def __init__(self, name):
        self.name = name

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        obj1, obj2, obj3 = Obj('name1'),Obj('name2'),Obj('name3')

        my_objects = [obj1, obj2, obj3]
        self.all_objects = QtWidgets.QListWidget(self)
        self.all_objects.setStyleSheet('border:1px solid purple;')
        self.all_objects.itemClicked.connect(self.listwidgetclicked)

        for i in my_objects:
            item = QtWidgets.QListWidgetItem(i.name)
            self.all_objects.addItem(item)
            item.setData(CustomObjectRole, i)

    def listwidgetclicked(self, item):
        obj = item.data(CustomObjectRole)
        print( obj.__dict__ )

            
 
if __name__ == '__main__':
    app = QtWidgets.QApplication([])  
    MainWindow = MyWidget()   
    MainWindow.show()
    app.exec_()