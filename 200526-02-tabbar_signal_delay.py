#https://stackoverflow.com/questions/62008886/why-is-qtabbar-giving-me-the-wrong-index-number
# 시그널 발생과 수신사이의 시간차 문제

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.tabs = QTabBar()
        self.tabs.addTab("Main Menu")
        self.tabs.addTab("Network Menu")

        layout = QHBoxLayout()
        layout.addWidget(self.tabs)

        self.tabs.tabBarClicked.connect(self.tab_push)
        self.setLayout(layout)

    def tab_push(self):
        x = self.tabs.currentIndex()
        print(x)

    """def tab_push(self):
        QTimer.singleShot(500, lambda: print(self.tabs.currentIndex()))"""

    """def tab_push(self, index):
        print(index)"""

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())