# https://stackoverflow.com/questions/62821244/how-to-reverse-spinbox-selection-in-pyqt5
# 버튼 역할을 거꾸로 하기

import sys
from PyQt5 import QtWidgets

class ReverseSpinBox(QtWidgets.QSpinBox):
    def stepEnabled(self):
        if self.wrapping() or self.isReadOnly():
            return super().stepEnabled()
        ret = QtWidgets.QAbstractSpinBox.StepNone
        if self.value() > self.minimum():
            ret |= QtWidgets.QAbstractSpinBox.StepUpEnabled
        if self.value() < self.maximum():
            ret |= QtWidgets.QAbstractSpinBox.StepDownEnabled
        return ret

    def stepBy(self, steps):
        return super().stepBy(-steps)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = ReverseSpinBox()
    w.resize(320, 20)
    w.show()
    sys.exit(app.exec_())