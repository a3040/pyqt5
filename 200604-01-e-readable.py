# https://stackoverflow.com/questions/50851350/get-printable-name-of-any-qkeyevent-key-value
# https://stackoverflow.com/questions/21764138/get-the-name-of-a-key-from-qkeyevent-in-qt/21767101#21767101
# keyPressEvent 일경우 발생시킨 키 읽기
# e

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui

keymap = {}
for key, value in vars(Qt).items():
    if isinstance(value, Qt.Key):
        keymap[value] = key.partition('_')[2]
        #print( key, value )

modmap = {
    Qt.ControlModifier: keymap[Qt.Key_Control],
    Qt.AltModifier: keymap[Qt.Key_Alt],
    Qt.ShiftModifier: keymap[Qt.Key_Shift],
    Qt.MetaModifier: keymap[Qt.Key_Meta],
    Qt.GroupSwitchModifier: keymap[Qt.Key_AltGr],
    Qt.KeypadModifier: keymap[Qt.Key_NumLock],
    }

def keyevent_to_string(event):
    sequence = []
    for modifier, text in modmap.items():
        if event.modifiers() & modifier:
            sequence.append(text)
    key = keymap.get(event.key(), event.text())
    if key not in sequence:
        sequence.append(key)
    return '+'.join(sequence)

class Window(QWidget):
    def paintEvent(self, e):
        p = QtGui.QPainter()
        p.begin(self)
        p.drawText(e.rect(), Qt.AlignCenter, '키보드눌러보기')
        p.end()
    
    def keyPressEvent(self, event):
        print(keyevent_to_string(event))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    #window.setGeometry(600, 100, 300, 200)
    window.resize(300,200)
    window.show()
    sys.exit(app.exec_())