# https://stackoverflow.com/questions/57506101/qlabel-is-not-updated-unless-the-mainwindow-is-unfocused
# 포커스 안맞을때 label이 변경 안되는 현상// 버그라고 하고 수정되었다고함
# pip list 해서 버전 확인 후 업데이트 : 

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelloWorld(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 201, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "foobar"))
        self.pushButton.setText(_translate("Dialog", "Click"))



import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow 

class HelloWorldGui(QMainWindow, Ui_HelloWorld):
    def __init__(self, parent=None):
        super(HelloWorldGui, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setTextHelloWorld)

    def setTextHelloWorld(self):
        self.label.setText("Hello World")


if __name__ == '__main__':
    argvs = sys.argv
    app = QApplication(argvs)
    hello_world_gui = HelloWorldGui()
    hello_world_gui.show()
    sys.exit(app.exec_())