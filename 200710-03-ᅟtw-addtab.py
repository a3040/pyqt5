# https://stackoverflow.com/questions/62821056/qtabwidget-not-letting-me-use-custom-class

"""from PyQt5 import QtCore, QtGui, QtWidgets


class topLevelWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Function that is used to add tabs
        def insertNewRegionTab(self):
            if self.mainTabWidgetCount == 1 + self.mainTabWidget.currentIndex():
                
                # Attempted method 1:
                tab = QtWidgets.QWidget()  # Want this to be a customTab not a QWidget
                self.mainTabWidget.insertTab(self.mainTabWidget.currentIndex(),
                                              tab, "Tab " + str(self.mainTabWidgetCount))

                # Attempted method 2:
                # self.tabInstaces.append(customTab(self.mainTabWidget))

                self.mainTabWidgetCount += 1

        super().__init__()
        # Initialization of main window
        self.setObjectName("MainWindow")
        self.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")

        # Create the main tab widget and set properties
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.mainTabWidget.setCurrentIndex(0)
        self.gridLayout_5.addWidget(self.mainTabWidget, 1, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)

        # Insert a tab (of the custom, pre-formatted tab class) into this tab widget
        self.tabInstances = [customTab(self.mainTabWidget)]
        self.mainTabWidgetCount = 2

        # Add the tab which creates other tabs to the tan widget
        self.addRegionTab = QtWidgets.QWidget()
        self.addRegionTab.setObjectName("addRegionTab")
        self.mainTabWidget.addTab(self.addRegionTab, "")

        # Add functionality: When '+' tab is selected, add a tab
        self.mainTabWidget.currentChanged.connect(lambda: insertNewRegionTab(self))

        # Show window
        self.show()


class customTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # Initializes the object itself and renames it. Add vertical layout to it
        super(customTab, self).__init__()
        self.setObjectName("tabInstances")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox1 = QtWidgets.QComboBox(self)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")


        # Add self to parent
        parent.addTab(self, "")




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = topLevelWindow()

    sys.exit(app.exec_())"""



from PyQt5 import QtCore, QtGui, QtWidgets


class TabWidget(QtWidgets.QTabWidget):
    plusClicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.tabBar().installEventFilter(self)

        self.add_button = QtWidgets.QToolButton(self, text="+")
        self.add_button.clicked.connect(self.plusClicked)

    def eventFilter(self, obj, event):
        if obj is self.tabBar() and event.type() == QtCore.QEvent.Resize:
            r = self.tabBar().geometry()
            h = r.height()
            self.add_button.setFixedSize((h - 1) * QtCore.QSize(1, 1))
            self.add_button.move(r.right(), 0)
        return super().eventFilter(obj, event)


class topLevelWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialization of main window
        self.setObjectName("MainWindow")
        self.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        lay = QtWidgets.QGridLayout(self.centralwidget)

        # Create the main tab widget and set properties
        self.mainTabWidget = TabWidget()
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.mainTabWidget.setCurrentIndex(0)
        lay.addWidget(self.mainTabWidget, 1, 1, 1, 1)

        self.mainTabWidget.addTab(CustomWidget(), "Tab1")
        self.mainTabWidget.plusClicked.connect(self.add_clicked)

    def add_clicked(self):
        index = self.mainTabWidget.count() + 1
        self.mainTabWidget.addTab(CustomWidget(), "Tab {}".format(index))


class CustomWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # Initializes the object itself and renames it. Add vertical layout to it
        super(CustomWidget, self).__init__(parent)

        self.comboBox1 = QtWidgets.QComboBox()
        self.comboBox1.addItems(list("abcdef"))

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.comboBox1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = topLevelWindow()
    w.show()

    sys.exit(app.exec_())
