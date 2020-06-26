# https://stackoverflow.com/questions/62522417/qdialog-is-destroyed-before-i-get-data-form-it

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, name, parent=None):
        super(Dialog, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) #옵션 확인용
        
        #
        self.title = QtWidgets.QLabel('name')
        self.val   = QtWidgets.QLineEdit()
        self.val.setText("{} is my infor".format(name))
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.title)
        hbox.addWidget(self.val)
        
        #
        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        #
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(hbox)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
 


def main(): 
    app = QtWidgets.QApplication(sys.argv)
    ex = Dialog('text')
    if ex.exec_() == QtWidgets.QDialog.Accepted:
        myinformation = ex.val.text()
        print(myinformation)

if __name__ == '__main__':
    main()